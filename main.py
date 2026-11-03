  board();$('types').hidden=true;
  overlay(d>0?'승리!':d<0?'패배':'무승부','나 '+S.sc[0]+' : '+S.sc[1]+' 상대\n안타 '+S.hits+'개, 홈런 '+S.hr+'개'+(nb&&d>0?'\n최고 득실차 기록!':''),'');
}
function start(m){
  clearTimeout(timer);S.fm=S.mode=m||S.fm;S.h=0;S.sc=[0,0];Object.assign(S,{outs:0,balls:0,strikes:0,hits:0,hr:0});
  loadBest();clearRun();$('types').hidden=S.mode!=='pitch';
  board();P=null;hit=null;sw=null;resetField();$('ov').hidden=true;S.phase='wait';flash('플레이 볼',S.mode==='bat'?'초 공격':'초 수비');
  timer=setTimeout(S.mode==='pitch'?ready:pitch,1100);
}
function act(){
  if(!ac){try{ac=new(window.AudioContext||window.webkitAudioContext)()}catch(e){}}
  if(ac&&ac.state==='suspended')ac.resume();
  if(S.phase==='idle'||S.phase==='over')return start(S.fm);
  if(S.phase==='aim')return throwPitch();
  if(S.phase!=='pitch'||sw||S.mode==='pitch')return;
  const now=performance.now();sw={t:now};resolve(now+CONTACT-P.arrive);
}

/* ---------- 매 프레임 ---------- */
const lerp=(a,b,t)=>a+(b-a)*C(t,0,1);
function tick(now){
  const dt=Math.min(.033,(now-last)/1000);last=now;
  if(S.phase==='pitch'&&!P.done&&now+CONTACT>P.arrive+200)resolve(null);
  /* 투수 팔 */
  let th=-.2;
  if(P){const tt=(now-(P.t0-WIND))/WIND;
    if(tt>=0&&tt<1)th=tt<.45?lerp(-.2,-3.4,tt/.45):lerp(-3.4,-1.9,(tt-.45)/.55);
    else if(tt>=1)th=lerp(-1.9,-.1,(now-P.t0)/250)}
  arm.rotation.x=th;
  /* 타자 스윙 */
  let yaw=-.9;
  if(sw){const dt2=now-sw.t;yaw=dt2<170?-.9+2.4*dt2/170:dt2<500?1.5:1.5-2.4*C((dt2-500)/300,0,1)}
  up.rotation.y=yaw;
  /* 주자 이동 */
  pool.forEach(r=>{
    if(!r.on||now<r.t0)return;
    if(r.b>=r.to){
      if(r.out&&!r.h){r.h=1;setTimeout(()=>{r.on=false;r.g.visible=false},500)}
      else if(r.to>=4){r.on=false;r.g.visible=false}
      return;
    }
    const tg=BP[r.b+1],q=r.g.position,dx=tg.x-q.x,dz=tg.z-q.z,d=Math.hypot(dx,dz),st=r.sp*dt;
    if(d<=st){q.x=tg.x;q.z=tg.z;r.b++}else{q.x+=dx/d*st;q.z+=dz/d*st}
    r.g.rotation.y=Math.atan2(dx,dz);
  });
  /* 수비 AI 이동 */
  if(hit&&now>=hit.t+300){
    const pl=hit.plan,i=Math.min(hit.path.length-1,Math.floor((now-hit.t)*.06));
    F.forEach(f=>{
      let tg=null;
      if(pl){if(f===pl.f)tg=hit.path[pl.i];else if(pl.out&&!pl.air&&f===F[0])tg=B1;else if(pl.dp&&f===F[1])tg=B2P}
      else if(hit.chase===f)tg=hit.path[i];
      if(tg){const q=f.g.position,dx=tg.x-q.x,dz=tg.z-q.z,d=Math.hypot(dx,dz);
        if(d>.05){const st=Math.min(SPDF*dt,d);q.x+=dx/d*st;q.z+=dz/d*st;f.g.rotation.y=Math.atan2(dx,dz)}}
    });
  }
  ret.visible=S.phase==='aim';ret.position.set(aim.x,aim.y,.15);
  /* 공 */
  let vis=false;
  if(P&&now>=P.t0&&!(hit&&now>=hit.t)){const p=(now-P.t0)/P.dur;if(p<1.15){bp(p,ball.position);vis=true;ball.rotation.x-=dt*22}}
  let follow=false;
  if(hit&&now>=hit.t){
    const k=(now-hit.t)/1000,pl=hit.plan,n=hit.path.length,i=Math.min(n-1,Math.floor(k*60));
    let q=hit.path[i];
    if(pl&&k>=pl.i/60){
      const fp=pl.f.g.position,ts=pl.i/60+.35;
      q=V3(fp.x,1.1,fp.z);
      if(!pl.air&&pl.seq&&k>ts){
        let a=pl.cp||(pl.cp=q.clone()),t=ts;
        for(const tg of pl.seq){
          if(k<t)break;
          const du=a.distanceTo(tg)/28;
          if(k<t+du){const u=(k-t)/du;q=a.clone().lerp(tg,u);q.y+=Math.sin(u*Math.PI)*1.5;break}
          q=tg;a=tg;t+=du+.2;
        }
      }
    }
    ball.position.copy(q);ball.rotation.x-=dt*18;vis=!(hit.hr&&i>=n-1);follow=k<n/60+.5;
  }
  ball.visible=vis;shd.visible=vis;
  if(vis){shd.position.set(ball.position.x,.06,ball.position.z);shd.scale.setScalar(1/(1+ball.position.y*.12))}
  /* 카메라 */
  if(follow)lookT.set(ball.position.x*.9,Math.max(1,ball.position.y*.8),Math.min(ball.position.z,-6));else lookT.copy(DEF);
  look.lerp(lookT,1-Math.pow(.02,dt));
  cam.position.set(camPos.x+(follow?look.x*.08:0),camPos.y,camPos.z);cam.lookAt(look);
  ren.render(scene,cam);requestAnimationFrame(tick);
}

stage.addEventListener('pointerdown',e=>{if(e.target.tagName==='BUTTON')return;e.preventDefault();if(S.mode==='pitch'&&S.phase==='aim')aimAt(e);act()});
stage.addEventListener('pointermove',e=>{if(S.mode==='pitch'&&S.phase==='aim')aimAt(e)});
$('types').addEventListener('click',e=>{const b=e.target.closest('button');if(b){setPT(+b.dataset.i);b.blur()}});
const pre=()=>{if(!ac){try{ac=new(window.AudioContext||window.webkitAudioContext)()}catch(e){}}if(ac&&ac.state==='suspended')ac.resume()};
$('go').addEventListener('click',()=>{pre();start('bat');$('go').blur()});
$('go2').addEventListener('click',()=>{pre();start('pitch');$('go2').blur()});
addEventListener('keydown',e=>{
  if(e.code==='Space'){e.preventDefault();if(!e.repeat)act()}
  else if(S.mode==='pitch'&&S.phase==='aim'){
    if(e.key>='1'&&e.key<='7')setPT(+e.key-1);
    const m={ArrowLeft:[-.04,0],ArrowRight:[.04,0],ArrowUp:[0,.04],ArrowDown:[0,-.04]}[e.key];
    if(m){e.preventDefault();aim.x=C(aim.x+m[0],-.5,.5);aim.y=C(aim.y+m[1],.3,1.4)}
  }
});
loadBest();board();requestAnimationFrame(tick);
})();
</script>
</body>
</html>
"""

components.html(
    GAME_HTML,
    height=1050,
    scrolling=True,
)
