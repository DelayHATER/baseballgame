# BaseBall 3D Pro - Streamlit app
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="컴투스아마추어야구2026", page_icon="⚾", layout="wide")
st.markdown("""
<style>
  [data-testid="stHeader"], [data-testid="stToolbar"] {visibility:hidden; height:0;}
  .block-container {padding:0.5rem 0.5rem 0; max-width:1100px;}
  iframe {border:0;}
</style>
""", unsafe_allow_html=True)

GAME_HTML = r"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<title>컴투스아마추어야구2026</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@400;600;800&display=swap">
<style>
:root { --ink: #0b1726; --deep: #060d17; --chalk: #f3f4f6; --lamp: #fbbf24; }
* { box-sizing: border-box; touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
body { margin: 0; background: var(--deep); color: var(--chalk); font-family: 'Noto Sans KR', sans-serif; min-height: 100vh; display: flex; justify-content: center; align-items: center; padding: 8px; overflow-x: hidden; }
.font-title { font-family: 'Black Han Sans', sans-serif; }
#stage { position: relative; width: 100%; aspect-ratio: 16/10; border-radius: 12px; overflow: hidden; background: #000; box-shadow: 0 10px 30px rgba(0,0,0,0.8); outline: none; }
@media (max-aspect-ratio: 1/1) { #stage { aspect-ratio: 4/5; max-height: 55vh; } }
#stage canvas { display: block; width: 100%; height: 100%; outline: none; }

#dia { position: relative; width:54px; height:54px; flex:none; pointer-events:none; }
.bs { position: absolute; width: 14px; height: 14px; transform: rotate(45deg); border: 2px solid rgba(255,255,255,0.4); background: rgba(0,0,0,0.4); transition: all 0.2s; }
.bs.on { background: var(--lamp); border-color: var(--lamp); box-shadow: 0 0 8px var(--lamp); }

#msg { position: absolute; left: 0; right: 0; top: 22%; text-align: center; pointer-events: none; opacity: 0; z-index: 25; }
#msg b { display: block; font-size: clamp(30px, 5.5vw, 54px); color: var(--lamp); text-shadow: 0 4px 12px rgba(0,0,0,0.9); font-family: 'Black Han Sans'; }
#msg span { display: block; margin-top: 4px; font-size: 14px; text-shadow: 0 2px 6px rgba(0,0,0,0.9); color: #fff; font-weight: 600; }
#msg.on { animation: pop 1.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
@keyframes pop { 0%{opacity:0;transform:scale(0.7)} 15%{opacity:1;transform:scale(1.05)} 80%{opacity:1} 100%{opacity:0;transform:scale(1)} }

#timingWrap { position: absolute; bottom: 12px; left: 50%; transform: translateX(-50%); width: 85%; max-width: 320px; height: 20px; background: rgba(15,23,42,0.85); border: 2px solid rgba(255,255,255,0.3); border-radius: 10px; overflow: hidden; display: none; z-index: 15; }
#timingTarget { position: absolute; left: 65%; width: 20%; height: 100%; background: rgba(34,197,94,0.6); border-left: 2px solid #22c55e; border-right: 2px solid #22c55e; }
#timingPerfect { position: absolute; left: 72%; width: 6%; height: 100%; background: #fbbf24; }
#timingCursor { position: absolute; left: 0%; width: 4px; height: 100%; background: #ef4444; box-shadow: 0 0 6px #ef4444; }
#timingHint { display:none; position:absolute; left:50%; bottom:38px; transform:translateX(-50%); z-index:15; padding:3px 8px; border-radius:6px; background:rgba(2,6,23,.88); color:#fbbf24; font-size:12px; font-weight:800; white-space:nowrap; pointer-events:none; }

#manualThrowBtn { position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); z-index:50; background:rgba(220,38,38,0.9); color:white; font-family:'Black Han Sans'; font-size:1.5rem; padding:12px 24px; border-radius:12px; border:2px solid #fff; box-shadow:0 0 15px rgba(220,38,38,0.8); cursor:pointer; display:none; user-select:none; }
#manualThrowBtn:active { transform:translate(-50%,-50%) scale(0.95); background:#991b1b; }

#ov { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; gap: 7px; padding: 12px; overflow-y:auto; background: rgba(6,13,23,0.94); backdrop-filter: blur(4px); z-index: 40; }

.btn-action { background: linear-gradient(135deg, #fbbf24, #d97706); color: #0b1726; font-weight: 800; border-radius: 8px; box-shadow: 0 4px 12px rgba(251,191,36,0.3); cursor: pointer; }
.btn-action:active { transform: translateY(1px); }
.pitch-btn { background: #1e293b; border: 1px solid #334155; color: #cbd5e1; border-radius: 6px; font-size: 13px; font-weight: 600; padding: 8px 4px; cursor: pointer; }
.pitch-btn.on { background: var(--lamp); color: #0b1726; border-color: var(--lamp); font-weight: 800; }
.stadium-choice { background:#172554; border:1px solid #475569; border-radius:8px; color:#e2e8f0; padding:8px 10px; font-weight:700; cursor: pointer; }
.stadium-choice.on { background:#fbbf24; color:#0b1726; border-color:#fbbf24; }

#absPanel { position:absolute; left:10px; bottom:10px; z-index:18; padding:8px; border-radius:8px; background:rgba(2,6,23,.88); border:1px solid rgba(226,232,240,.35); color:#f8fafc; font-size:10px; }
#absGrid { display:grid; grid-template-columns:repeat(7,14px); gap:2px; margin:5px auto; }
.abs-cell { width:14px; height:14px; border:1px solid rgba(255,255,255,.22); background:rgba(148,163,184,.12); }
.abs-cell.zone { background:rgba(34,197,94,.25); }
.abs-cell.point { background:#fbbf24; box-shadow:0 0 7px #fbbf24; border-radius:50%; }
.abs-cell.challenge { outline:1px solid #f87171; }
#absCall { display:block; text-align:center; color:#fbbf24; min-height:14px; }
#absPanel #challengeBtn { display:block !important; width:100%; margin-top:4px; padding:5px; font-size:10px; }

.setting-row { display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:6px; }
.setting-label { color:#cbd5e1; font-size:12px; font-weight:700; margin:0 3px; }
.pitch-info { display:flex; align-items:center; justify-content:center; min-height:34px; border:1px solid #334155; border-radius:8px; background:#0f172a; color:#fbbf24; font-weight:800; font-size:13px; letter-spacing:.04em; }

.top-summaries { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
.summary-card { min-width:0; border:1px solid #334155; border-radius:9px; background:#0f172a; padding:8px 10px; color:#e2e8f0; font-size:11px; }
.summary-card b { display:block; font-size:12px; margin-bottom:3px; }

.lineup-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:5px; width:min(100%,440px); max-height:210px; overflow:auto; padding:4px; }
.lineup-grid label { color:#cbd5e1; font-size:10px; text-align:left; }
.lineup-grid input { display:block; width:100%; min-width:0; margin-top:2px; border:1px solid #475569; border-radius:5px; background:#0f172a; color:#fff; padding:5px; font-size:11px; }
.lineup-card { min-width:0; padding:4px; border:1px solid #334155; border-radius:6px; background:rgba(15,23,42,.7); }

.team-name-inputs { display:grid; grid-template-columns:1fr 1fr; gap:8px; width:min(100%,440px); }
.team-name-inputs label { color:#cbd5e1; font-size:11px; text-align:left; }
.team-name-inputs input { display:block; width:100%; margin-top:3px; border:1px solid #475569; border-radius:6px; background:#0f172a; color:#fff; padding:6px; font-size:12px; }

#gameHud { position:absolute; right:8px; bottom:48px; z-index:19; width:min(260px,74%); display:flex; flex-direction:column; gap:5px; padding:7px; border:1px solid rgba(226,232,240,.35); border-radius:9px; background:rgba(2,6,23,.9); color:#f8fafc; box-shadow:0 4px 14px rgba(0,0,0,.35); }
.game-hud-score { display:grid; grid-template-columns:1fr auto; align-items:center; gap:2px 8px; }
.game-hud-score #scoreTeams { grid-column:1; grid-row:1; color:#cbd5e1; font-size:10px; }
.game-hud-score #score { grid-column:1; grid-row:2; font-size:20px; line-height:1.05; }
.game-hud-score #inn { grid-column:2; grid-row:1 / span 2; color:#fbbf24; font-size:15px; white-space:nowrap; }

#gameHud #pitchInfo { min-height:22px; padding:2px 5px; border:0; background:rgba(30,41,59,.72); font-size:11px; }
#gameHud .hud-count { display:flex; justify-content:space-around; padding:3px 6px; border-radius:6px; background:rgba(15,23,42,.9); }
#gameHud .hud-count > div { display:flex; align-items:center; gap:5px; }
#gameHud .hud-pitcher { display:flex; justify-content:space-between; align-items:center; gap:6px; font-size:10px; }
#gameHud .hud-stamina { display:flex; align-items:center; gap:6px; color:#cbd5e1; font-size:9px; }
.stamina-track { flex:1; height:8px; overflow:hidden; border:1px solid rgba(255,255,255,.24); border-radius:99px; background:rgba(15,23,42,.95); }
#pitcherStaminaFill { display:block; width:100%; height:100%; border-radius:99px; background:linear-gradient(90deg,#22c55e,#a3e635); transition:width .25s ease; }
#pitcherStaminaText { min-width:29px; text-align:right; color:#fbbf24; }

#gameHud .hud-base { display:flex; align-items:center; justify-content:space-between; gap:8px; padding:2px 6px; border-radius:6px; background:rgba(15,23,42,.9); color:#cbd5e1; font-size:10px; }
#gameHud .hud-cameras { display:grid; grid-template-columns:1fr 1fr 1fr auto; gap:3px; }
#gameHud .hud-cameras button, #videoReviewBtn { color:#e2e8f0; background:#1e293b; border:1px solid #475569; border-radius:5px; padding:4px 3px; font-size:9px; font-weight:700; cursor: pointer; }
#gameHud .hud-cameras button.on { color:#0b1726; background:#fbbf24; border-color:#fbbf24; }

#replayBadge { position:absolute; top:12px; left:12px; z-index:30; background:rgba(220,38,38,0.9); color:#fff; font-weight:800; font-size:12px; padding:4px 10px; border-radius:6px; display:none; animation:blink 1s infinite alternate; }
@keyframes blink { 0%{opacity:1;} 100%{opacity:0.4;} }
#videoReviewPanel { position:absolute; inset:50% auto auto 50%; transform:translate(-50%,-50%); z-index:35; width:min(320px,88%); padding:12px; border:1px solid #64748b; border-radius:10px; background:rgba(2,6,23,.96); color:#f8fafc; box-shadow:0 8px 30px rgba(0,0,0,.6); }
#videoReviewText { white-space:pre-line; }

@media (max-width:480px) { 
  #gameHud { width:min(205px,64%); right:6px; bottom:46px; padding:5px; gap:4px; } 
  #gameHud #pitchInfo { font-size:10px; } 
  #gameHud .hud-cameras button, #videoReviewBtn { font-size:8px; } 
}
</style>
</head>
<body>

<main class="w-full max-w-4xl flex flex-col gap-2">
  <header class="flex items-center justify-between bg-slate-900 border border-slate-800 rounded-xl px-3 py-2 shadow-lg text-xs md:text-sm">
    <b class="font-bold text-slate-200">⚾ 컴투스아마추어야구2026</b>
    <div class="flex items-center gap-2">
      <span id="pitcherName" class="font-bold text-slate-200">ACE 류현진</span>
      <button id="changePitcherBtn" class="bg-slate-700 px-2 py-1 rounded text-white border border-slate-500 cursor-pointer">투수 교체</button>
    </div>
  </header>

  <section class="top-summaries">
    <div class="summary-card">
      <b id="batterSideLabel" class="text-amber-400">내 타자</b>
      <div id="batterSummary">1번 타자 · AVG — · OPS —</div>
    </div>
    <div class="summary-card">
      <b id="pitcherSideLabel" class="text-sky-400">상대 투수</b>
      <div id="pitcherSummaryTop">상대 선발 · ERA — · K 0 · WHIP —</div>
    </div>
  </section>

  <!-- 3D 캔버스 영역 -->
  <div id="stage" tabindex="0">
    <div id="replayBadge">🔴 REPLAY</div>
    <div id="msg"></div>
    <div id="manualThrowBtn">1루 송구! (홀드)</div>
    
    <!-- 비디오 판독 패널 -->
    <div id="videoReviewPanel" style="display: none;">
      <b class="block text-amber-400 text-base mb-2">📺 비디오 판독 & 수동 조작</b>
      <div id="videoReviewText" class="text-xs leading-relaxed text-slate-200">아직 판독할 투구가 없습니다.</div>
      <div class="mt-3 pt-3 border-t border-slate-700 text-xs">
        <span class="block mb-1 text-slate-300 font-bold">주루 판정 수동 번복</span>
        <div class="flex gap-2">
          <button id="overrideOutBtn" class="bg-red-900/80 border border-red-500 hover:bg-red-800 text-red-100 px-2 py-1.5 rounded flex-1 font-bold cursor-pointer">아웃 처리</button>
          <button id="overrideSafeBtn" class="bg-blue-900/80 border border-blue-500 hover:bg-blue-800 text-blue-100 px-2 py-1.5 rounded flex-1 font-bold cursor-pointer">세이프 처리</button>
        </div>
      </div>
      <div class="flex gap-2 mt-3">
        <button id="playSlowReplayBtn" class="btn-action flex-1 py-1.5 text-xs">🎬 슬로우 재생</button>
        <button id="closeVideoReview" class="stadium-choice flex-1 py-1.5 text-xs">판독 종료(재개)</button>
      </div>
    </div>
    
    <!-- ESC 타임 메뉴 패널 -->
    <div id="timeoutMenu" class="absolute inset-0 bg-black/85 z-40 flex flex-col items-center justify-center p-4 backdrop-blur-sm" style="display: none;">
      <h2 class="text-4xl text-amber-400 font-title mb-8 drop-shadow-lg">타임 선언</h2>
      <button id="resumeGameBtn" class="btn-action w-64 py-4 text-lg mb-4">경기 재개</button>
      <button id="openPinchHitterBtn" class="bg-blue-700 hover:bg-blue-600 text-white font-bold w-64 py-4 text-lg rounded-lg border border-blue-500 shadow-lg mb-4 cursor-pointer">대타 기용</button>
    </div>

    <!-- 대타 기용 모달 -->
    <div id="pinchHitterModal" class="absolute inset-0 bg-slate-900/95 z-50 flex flex-col items-center justify-center p-4" style="display: none;">
      <h2 class="text-2xl text-amber-400 font-title mb-3">대타 기용 (랜덤 생성)</h2>
      <p class="text-[11px] text-slate-300 mb-3 text-center">투수의 폼/손 방향과 강점/약점이 일치하면<br>타격에 큰 영향을 줍니다.</p>
      
      <div class="w-full max-w-sm mb-3">
        <label class="text-xs text-amber-200 font-bold block mb-1">교체할 타순 선택</label>
        <select id="pinchTargetSelect" class="w-full bg-slate-800 text-white p-2 rounded border border-slate-600 outline-none text-sm cursor-pointer"></select>
      </div>
      <div id="pinchHitterList" class="flex flex-col gap-2 w-full max-w-sm max-h-60 overflow-y-auto pr-1"></div>
      <button id="closePinchHitterBtn" class="stadium-choice w-full max-w-sm mt-3 py-2">취소</button>
    </div>

    <!-- 투수 교체 모달 -->
    <div id="pitcherModal" class="absolute inset-0 bg-black/85 backdrop-blur-sm z-50 flex items-center justify-center p-4" style="display: none;">
      <div class="bg-slate-900 border border-slate-700 rounded-xl p-5 max-w-sm w-full shadow-2xl">
        <h3 class="font-title text-xl text-amber-400 mb-3">투수 교체</h3>
        <div id="pitcherList" class="flex flex-col gap-2 mb-4 max-h-60 overflow-y-auto"></div>
        <button id="closePitcherModal" type="button" class="w-full bg-slate-800 text-slate-300 py-2.5 rounded-lg font-bold border border-slate-700 cursor-pointer">닫기</button>
      </div>
    </div>

    <!-- ABS UI -->
    <div id="absPanel">
      <b>ABS 존 · 최근 투구</b>
      <div id="absGrid"></div>
      <span id="absCall">아직 투구 기록 없음</span>
      <button id="challengeBtn" class="stadium-choice" disabled>⚖️ ABS 챌린지 대기 (2)</button>
    </div>

    <section id="gameHud">
      <div class="pitch-info" id="pitchInfo">투구 후 구종과 구속이 표시됩니다</div>
      <div class="game-hud-score bg-slate-900 rounded-md px-2 py-1">
        <span id="scoreTeams">우리 팀 : 상대 팀</span><b id="score" class="text-white font-title">0 : 0</b><b id="inn" class="font-title">1회 초</b>
      </div>
      <div class="hud-count">
        <div><span class="text-emerald-400 font-bold">B</span><b id="b" class="text-amber-300 font-mono tracking-widest">○○○</b></div>
        <div><span class="text-yellow-400 font-bold">S</span><b id="s" class="text-amber-300 font-mono tracking-widest">○○</b></div>
        <div><span class="text-red-400 font-bold">O</span><b id="o" class="text-amber-300 font-mono tracking-widest">○○</b></div>
      </div>
      <div class="hud-pitcher">
        <span class="text-slate-400">투수</span><b id="pitcherStats" class="text-amber-300">구속 A | 변화구 A</b>
      </div>
      <div class="hud-stamina">
        <span>체력</span><div class="stamina-track"><i id="pitcherStaminaFill"></i></div><b id="pitcherStaminaText">100%</b>
      </div>
      <div class="hud-base">
        <span>베이스 상황</span>
        <div id="dia"><i class="bs" style="left:20px;top:2px"></i><i class="bs" style="left:38px;top:20px"></i><i class="bs" style="left:2px;top:20px"></i></div>
      </div>
      <div class="hud-cameras">
        <button type="button" data-camera="plate">포수 뒤</button>
        <button type="button" data-camera="pitcher">투수 뒤</button>
        <button type="button" data-camera="batter">1인칭</button>
        <!-- 송구 모드 토글 -->
        <button type="button" id="throwToggleBtn" class="text-slate-200">송구: 자동</button>
      </div>
      <button id="videoReviewBtn" type="button">📺 비디오 판독 (일시정지)</button>
    </section>

    <div id="timingWrap">
      <div id="timingTarget"></div>
      <div id="timingPerfect"></div>
      <div id="timingCursor"></div>
    </div>
    <div id="timingHint"></div>

    <!-- 시작 화면 오버레이 -->
    <div id="ov">
      <h2 id="ovT" class="font-title text-3xl md:text-5xl text-amber-400 drop-shadow">컴투스아마추어야구2026</h2>
      <p id="ovP" class="text-sm md:text-base text-slate-300 max-w-md text-center leading-relaxed">
        선수 능력치와 상성(대타 기용 시)이 경기에 직접 적용됩니다.<br>
        1루 수동 송구 설정은 게임 중 우측 하단 패널에서도 바꿀 수 있습니다.
      </p>
      <div class="flex flex-wrap justify-center gap-2 mt-1" id="stadiumChoices">
        <button type="button" class="stadium-choice on" data-stadium="0">🌙 야간 클래식</button>
        <button type="button" class="stadium-choice" data-stadium="1">🏟️ 돔구장</button>
        <button type="button" class="stadium-choice" data-stadium="2">🌊 해안 구장</button>
        <button type="button" class="stadium-choice" data-stadium="3">🌿 그린 파크</button>
      </div>
      <div class="setting-row" id="difficultyChoices">
        <span class="setting-label">난이도</span>
        <button type="button" class="stadium-choice" data-difficulty="easy">쉬움</button>
        <button type="button" class="stadium-choice on" data-difficulty="normal">보통</button>
        <button type="button" class="stadium-choice" data-difficulty="hard">어려움</button>
      </div>
      <div class="setting-row" id="inningChoices">
        <span class="setting-label">이닝</span>
        <button type="button" class="stadium-choice on" data-innings="3">3이닝</button>
        <button type="button" class="stadium-choice" data-innings="5">5이닝</button>
        <button type="button" class="stadium-choice" data-innings="9">9이닝</button>
      </div>
      <div class="lineup-grid" id="lineupInputs"></div>
      <div class="team-name-inputs">
        <label>내 팀 이름<input id="ownTeamName" maxlength="12" value="우리 팀"></label>
        <label>상대 팀 이름<input id="opponentTeamName" maxlength="12" value="상대 팀"></label>
      </div>
      <div class="flex gap-3 mt-2">
        <button type="button" id="go" class="btn-action px-6 py-3 text-base">공격(타자)부터 시작</button>
        <button type="button" id="go2" class="btn-action px-6 py-3 text-base" style="background: linear-gradient(135deg, #38bdf8, #0284c7); color:white;">수비(투수)부터 시작</button>
      </div>
    </div>
  </div>

  <div id="types" class="grid grid-cols-4 sm:grid-cols-7 gap-1.5" hidden>
    <button class="pitch-btn on" data-i="0">포심(1)</button>
    <button class="pitch-btn" data-i="1">투심(2)</button>
    <button class="pitch-btn" data-i="2">슬라이더(3)</button>
    <button class="pitch-btn" data-i="3">커브(4)</button>
    <button class="pitch-btn" data-i="4">체인지업(5)</button>
    <button class="pitch-btn" data-i="5">스위퍼(6)</button>
    <button class="pitch-btn" data-i="6">너클볼(7)</button>
  </div>

  <div class="setting-row" id="battingModeChoices" style="display:none">
    <span class="setting-label">타격 모드</span>
    <button class="stadium-choice" data-batting-mode="power">💥 파워스윙</button>
    <button class="stadium-choice" data-batting-mode="normal">⚖️ 노말</button>
    <button class="stadium-choice" data-batting-mode="contact">🎯 컨택</button>
  </div>

  <div class="grid grid-cols-3 gap-2 mt-1">
    <button id="mobileAct" class="col-span-2 btn-action py-3.5 text-lg font-title tracking-wider shadow-lg">스윙!</button>
    <button id="mobileSteal" class="bg-indigo-600 hover:bg-indigo-500 active:bg-indigo-700 text-white font-bold rounded-lg py-3 text-sm flex items-center justify-center gap-1 shadow-lg disabled:opacity-40" disabled>
      🏃 질주 (태그업)
    </button>
    <button id="mobilePitchShift" class="col-span-3 stadium-choice py-3" style="display:none;touch-action:none">⚾ 투구 타이밍 · 누르고 있다가 떼기</button>
    <button id="buntBtn" class="col-span-3 stadium-choice py-2">번트 대기</button>
    <button id="pciBtn" class="col-span-3 stadium-choice py-2" hidden>🎯 조준 원: OFF (Shift)</button>
  </div>

  <p class="text-xs text-slate-400 text-center mt-1">
    📱 모바일: 터치 조작 / 💻 PC: [마우스 휠] 줌, [Space] 타격/투구, [S] 질주(도루/태그업), [B] 번트, [ESC] 타임/대타
  </p>
  <section id="statsPanel" class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
    <div class="bg-slate-900 border border-slate-700 rounded-lg p-2">
      <b class="text-amber-400">내 타자 전체 기록</b>
      <div id="batterStats" class="text-slate-200 mt-1">AVG — · OBP — · SLG — · OPS —<br>득점 0 · 타점 0</div>
    </div>
    <div class="bg-slate-900 border border-slate-700 rounded-lg p-2">
      <b class="text-sky-400">내 투수 전체 기록</b>
      <div id="pitcherGameStats" class="text-slate-200 mt-1">ERA — · K 0 · BB 0 · WHIP — · HBP 0</div>
    </div>
  </section>
</main>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(() => {
const $ = id => document.getElementById(id);

// 라인업 초기화
$('lineupInputs').innerHTML = Array.from({ length: 9 }, (_, i) => `
  <div class="lineup-card"><label>${i + 1}번 타자<input id="lineupName${i}" maxlength="12" value="${i + 1}번 타자"></label></div>`).join('');

const R = (a, b) => a + Math.random() * (b - a);
const C = (v, a, b) => Math.max(a, Math.min(b, v));

let currentTimeScale = 1.0;
let targetTimeScale = 1.0;
let simTime = performance.now();
let lastReal = performance.now();
const gameTimers = [];

function setGameTimeout(fn, delayMs) {
  const tObj = { triggerAt: simTime + delayMs, fn: fn, canceled: false };
  gameTimers.push(tObj);
  return tObj;
}
function clearGameTimeout(tObj) {
  if (tObj) tObj.canceled = true;
}

let isReviewPaused = false;
let isTimeOut = false;
let camZoom = 1.0;
let lastRace = null;
let pendingTagUp = null;
let manualThrowMode = false;
let throwCharge = null;

const TRAIT_TYPES = ['우완', '좌완', '오버핸드', '쓰리쿼터', '사이드암', '언더핸드'];
const PINCH_NAMES = ['김대타', '이한방', '박승부', '최역전', '정클러치', '강스윙', '조타격', '장홈런'];

const PITCHERS = [
  { id: 0, title: 'MONSTER', name: '류현진', hand: 'L', form: 'over', formName: '오버핸드', releaseX: -0.24, releaseY: 1.92, speed: 1.15, break: 1.2, ctrl: 0.027, endurance: 1.12, pitches: [0,2,3,4], desc: '좌완 · 구속 A · 변화 A · 제구 S' },
  { id: 1, title: '뱀직구', name: '임창용', hand: 'R', form: 'side', formName: '사이드암', releaseX: 0.52, releaseY: 1.48, speed: 1.05, break: 1.45, ctrl: 0.045, endurance: 0.94, pitches: [0,1,2,5], desc: '우완 · 구속 B · 변화 A · 제구 B' },
  { id: 2, title: 'K-RIVERA', name: '고우석', hand: 'R', form: 'over', formName: '오버핸드', releaseX: 0.18, releaseY: 1.92, speed: 1.25, break: 0.85, ctrl: 0.06, endurance: 0.86, pitches: [1,4,6], desc: '우완 · 구속 S · 변화 B · 제구 C' },
  { id: 3, title: '광현', name: '김광현', hand: 'L', form: 'threeQuarter', formName: '쓰리쿼터', releaseX: -0.39, releaseY: 1.7, speed: 1.0, break: 1.3, ctrl: 0.035, endurance: 1.04, pitches: [0,2,3,5], desc: '좌완 · 구속 B · 변화 A · 제구 A' },
  { id: 4, title: '고퀄스', name: '고영표', hand: 'R', form: 'side', formName: '사이드암', releaseX: 0.48, releaseY: 1.36, speed: 0.98, break: 1.55, ctrl: 0.028, endurance: 1.18, pitches: [0,1,4,6], desc: '우완 · 구속 B · 변화 S · 제구 S' },
  { id: 5, title: '문동주', name: '문동주', hand: 'R', form: 'over', formName: '오버핸드', releaseX: 0.18, releaseY: 2.04, speed: 1.3, break: 0.9, ctrl: 0.052, endurance: 0.82, pitches: [0,1,2,3], desc: '우완 · 구속 S · 변화 B · 제구 C' },
  { id: 6, title: '무쇠팔', name: '최동원', hand: 'R', form: 'over', formName: '역동적 오버핸드', releaseX: 0.3, releaseY: 1.95, speed: 1.18, break: 1.3, ctrl: 0.03, endurance: 1.4, pitches: [0,3,2], desc: '우완 · 강철체력 S · 구속 A · 폭포수 커브' },
  { id: 7, title: '석민어린이', name: '윤석민', hand: 'R', form: 'threeQuarter', formName: '쓰리쿼터', releaseX: 0.35, releaseY: 1.75, speed: 1.1, break: 1.35, ctrl: 0.025, endurance: 1.05, pitches: [0,2,4,3], desc: '우완 · 구속 A · 고속슬라이더 S · 제구 S' }
];

let currentPitcherIdx = 0;
let usedPitcherIds = new Set();
let pitcherStamina = 100;
let pitcherStaminaById = Object.fromEntries(PITCHERS.map(p => [p.id, 100]));
function pitcherFatigueFactor() { return 0.72 + 0.28 * C(pitcherStamina / 100, 0, 1); }
function savePitcherStamina() { pitcherStaminaById[currentPitcherIdx] = pitcherStamina; }

let selectedStadium = 0;
let teamNames = ['우리 팀', '상대 팀'];
let difficulty = 'normal';
let maxInnings = 3;
let batterSide = 'R';
let cameraMode = 'plate';
let battingMode = 'normal';
let pciEnabled = false;
let pciInsideContact = false;
let homeRunCelebrationUntil = 0;
let fireworks = [];
let defensiveThrow = null;

const DIFFICULTIES = { 
  easy: { label: '쉬움', pitchSpeed: 0.86, aiContact: 0.68, zoneRate: 0.52 }, 
  normal: { label: '보통', pitchSpeed: 1, aiContact: 1, zoneRate: 0.6 }, 
  hard: { label: '어려움', pitchSpeed: 1.14, aiContact: 1.24, zoneRate: 0.68 } 
};
const emptyBatterStats = () => ({ pa: 0, ab: 0, hits: 0, walks: 0, hbp: 0, totalBases: 0, runs: 0, rbi: 0 });
const emptyPitcherStats = () => ({ outs: 0, strikeouts: 0, walks: 0, hits: 0, hbp: 0, earnedRuns: 0 });

let batterStats = emptyBatterStats();
let lineup = Array.from({ length: 9 }, (_, i) => ({ name: `${i + 1}번 타자`, stats: emptyBatterStats(), speed: 3, power: 3, contact: 3, eye: 3, side: 'R', str: null, wk: null }));
let battingOrderIndex = 0;
let batterPAComplete = false;
let pitcherStatsById = Object.fromEntries(PITCHERS.map(p => [p.id, emptyPitcherStats()]));
let opponentPitcherStats = emptyPitcherStats();
let opponentLineup = Array.from({ length: 9 }, (_, i) => ({ name: `상대 ${i + 1}번 타자`, side: Math.random() < 0.5 ? 'L' : 'R', stats: emptyBatterStats(), speed: 3, power: 3, contact: 3, eye: 3, str: null, wk: null }));
let opponentBatterIndex = 0;
let batterPAMode = null;
let challengeCount = 2;
let pendingABSCall = null;
let lastPitchReview = null;

const CONTACT = 64;
const V3 = (x, y, z) => new THREE.Vector3(x, y, z);
const BASE_RUN_SUCCESS_SCALE = 0.65;
const S = { phase: 'idle', mode: 'bat', pt: 0, fm: 'bat', h: 0, sc: [0, 0], outs: 0, balls: 0, strikes: 0, hits: 0, hr: 0, bases: [0, 0, 0] };
let P = null, sw = null, hit = null, ac = null;
let timingAnimId = null, pitchCharge = null;
let isStealing = false, stealSpeedBonus = 0, activeStealRunner = null, stealRace = null, stealTimerObj = null;
let batterRace = null, pendingFieldingPlay = null, buntMode = false;

const REPLAY_MAX_FRAMES = 450;
const replayBuffer = [];
let isReplaying = false;
let replayFrameIndex = 0;
let hrSequence = null;
let hrContactFrame = 0;

// Three.js 설정
const stage = $('stage');
const ren = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
ren.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
ren.shadowMap.enabled = true; 
ren.shadowMap.type = THREE.PCFSoftShadowMap; 
ren.toneMapping = THREE.ACESFilmicToneMapping; 
ren.toneMappingExposure = 1.05;
stage.prepend(ren.domElement);

const scene = new THREE.Scene(); 
scene.background = new THREE.Color(0x07101c); 
scene.fog = new THREE.Fog(0x07101c, 85, 340);

const cam = new THREE.PerspectiveCamera(52, 1, 0.3, 600);
const camPos = V3(-0.8, 1.55, 1.8);
const DEF = V3(0, 0.82, 0.1);
const look = DEF.clone();
const lookT = DEF.clone();
const liveCamPos = camPos.clone();
cam.position.copy(camPos);

function rs() { 
  const w = stage.clientWidth || 800;
  const h = stage.clientHeight || 500; 
  ren.setSize(w, h, false); 
  cam.aspect = w / h; 
  cam.updateProjectionMatrix(); 
}
addEventListener('resize', rs); 
new ResizeObserver(rs).observe(stage); 
setTimeout(rs, 50);

const hemi = new THREE.HemisphereLight(0xc8dcff, 0x183824, 0.75); 
scene.add(hemi);

const sun = new THREE.DirectionalLight(0xfff5e0, 1.35); 
sun.position.set(16, 32, 18); 
sun.target.position.set(0, 0, -8);
sun.castShadow = true; 
sun.shadow.mapSize.set(2048, 2048); 
sun.shadow.bias = -0.0005;
Object.assign(sun.shadow.camera, { left: -16, right: 16, top: 16, bottom: -16, near: 5, far: 85 }); 
scene.add(sun, sun.target);

function tex(w, h, fn, rep) { 
  const k = document.createElement('canvas'); 
  k.width = w; k.height = h; 
  fn(k.getContext('2d'), w, h); 
  const t = new THREE.CanvasTexture(k); 
  if (rep) { t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(rep[0], rep[1]); } 
  return t; 
}

const mat = (c, r) => new THREE.MeshStandardMaterial({ color: c, roughness: r == null ? 0.85 : r });
function mk(geo, m, x, y, z, parent, sh) { 
  const o = new THREE.Mesh(geo, m); 
  o.position.set(x, y, z); 
  o.castShadow = sh !== false; 
  (parent || scene).add(o); 
  return o; 
}
function flat(geo, m, x, y, z, rz) { 
  const o = new THREE.Mesh(geo, m); 
  o.rotation.x = -Math.PI / 2; 
  o.rotation.z = rz || 0; 
  o.receiveShadow = true; 
  scene.add(o); 
  return o; 
}

const grass = tex(256, 256, (g, w, h) => {
  g.fillStyle = '#26683f'; g.fillRect(0, 0, w, h); 
  g.fillStyle = '#2d7447'; g.fillRect(0, 0, w, h / 2);
  for (let i = 0; i < 2200; i++) { 
    g.fillStyle = 'rgba(0,0,0,' + R(0.02, 0.08) + ')'; 
    g.fillRect(R(0, w), R(0, h), 2, 2); 
  }
}, [34, 34]);

const fieldMat = new THREE.MeshStandardMaterial({ map: grass, roughness: 0.95 }); 
flat(new THREE.PlaneGeometry(500, 500), fieldMat, 0, 0, -100);
const dirt = mat(0x8a5a3b, 0.98); 
flat(new THREE.PlaneGeometry(33, 33), dirt, 0, 0.02, -19.4, Math.PI / 4); 
flat(new THREE.PlaneGeometry(21, 21), new THREE.MeshStandardMaterial({ map: grass, roughness: 0.95 }), 0, 0.03, -19.4, Math.PI / 4); 
flat(new THREE.CircleGeometry(7.5, 40), dirt, 0, 0.04, 0);

const mound = mk(new THREE.CylinderGeometry(2.7, 3.3, 0.28, 32), dirt, 0, 0.14, -18.4, scene, false); 
mound.receiveShadow = true; 
mk(new THREE.BoxGeometry(0.6, 0.05, 0.15), mat(0xffffff), 0, 0.3, -18.4, scene, false);

const chalk = new THREE.MeshBasicMaterial({ color: 0xf2f2ec }); 
[[1, Math.PI / 4], [-1, 3 * Math.PI / 4]].forEach(([s, a]) => { 
  const l = mk(new THREE.BoxGeometry(110, 0.02, 0.15), chalk, s * 38.9, 0.05, -38.9, scene, false); 
  l.rotation.y = a; 
});
[[19.4, -19.4], [0, -38.8], [-19.4, -19.4]].forEach(([x, z]) => { 
  const b = mk(new THREE.BoxGeometry(0.55, 0.12, 0.55), mat(0xffffff), x, 0.08, z, scene, false); 
  b.rotation.y = Math.PI / 4; 
});

const ps = new THREE.Shape(); 
[[-.24, 0], [.24, 0], [.24, -.24], [0, -.48], [-.24, -.24]].forEach(([x, y], i) => i ? ps.lineTo(x, y) : ps.moveTo(x, y));
const plate = new THREE.Mesh(new THREE.ExtrudeGeometry(ps, { depth: 0.04, bevelEnabled: false }), mat(0xffffff)); 
plate.rotation.x = -Math.PI / 2; plate.position.set(0, 0.05, -0.1); 
scene.add(plate);

const zone = new THREE.LineLoop(
  new THREE.BufferGeometry().setFromPoints([V3(-0.384, 0.34, 0.1), V3(0.384, 0.34, 0.1), V3(0.384, 1.30, 0.1), V3(-0.384, 1.30, 0.1)]), 
  new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.85 })
); 
scene.add(zone);

const TS = Math.PI * 1.5 - 1.05, TL = 2.1;
const wall = new THREE.Mesh(new THREE.CylinderGeometry(100, 100, 4, 72, 1, true, TS, TL), new THREE.MeshStandardMaterial({ color: 0x14402e, roughness: 0.8, side: THREE.DoubleSide })); 
wall.position.y = 2; scene.add(wall);
const stands = new THREE.Mesh(new THREE.CylinderGeometry(119, 119, 16, 72, 1, true, TS, TL), new THREE.MeshStandardMaterial({ color: 0x26364c, roughness: 0.88, side: THREE.DoubleSide })); 
stands.position.y = 8; scene.add(stands);

const ump = figure(0x1a1a1a, 0x1a1a1a, 0, 1.55); 
ump.scale.set(1.05, 1.05, 1.05);

const dugoutGroup = new THREE.Group(); 
scene.add(dugoutGroup);
const dMat = mat(0x0f172a, 0.9), dRoof = mat(0x1e293b, 0.9);
const crowdPalette = [0xe2e8f0, 0xfbbf24, 0x38bdf8, 0xf87171, 0x34d399, 0xc4b5fd, 0xffffff];

[-1, 1].forEach(s => {
    const d = new THREE.Group(); 
    d.position.set(s * 28, 0, -14); 
    d.rotation.y = s * -Math.PI / 7; 
    dugoutGroup.add(d);
    
    mk(new THREE.BoxGeometry(16, 1.2, 4), dMat, 0, 0.6, 0, d); 
    mk(new THREE.BoxGeometry(17, 0.2, 5), dRoof, 0, 2.2, 0, d); 
    mk(new THREE.BoxGeometry(0.2, 2.2, 4), dMat, -8, 1.1, 0, d); 
    mk(new THREE.BoxGeometry(0.2, 2.2, 4), dMat, 8, 1.1, 0, d);
    
    const cp = [], cc = [];
    for(let i=0; i<300; i++) { 
      cp.push(R(-8, 8), R(2.4, 4.8), R(-2, 2.5)); 
      const col = new THREE.Color(crowdPalette[Math.floor(Math.random() * crowdPalette.length)]); 
      cc.push(col.r, col.g, col.b); 
    }
    const cGeo = new THREE.BufferGeometry(); 
    cGeo.setAttribute('position', new THREE.Float32BufferAttribute(cp, 3)); 
    cGeo.setAttribute('color', new THREE.Float32BufferAttribute(cc, 3));
    d.add(new THREE.Points(cGeo, new THREE.PointsMaterial({ size: 1.8, sizeAttenuation: false, vertexColors: true })));
});

const fences = [];
[-1, 1].forEach(s => { 
  const f = mk(new THREE.BoxGeometry(60, 2.4, 0.4), mat(0x14402e, 0.8), s * 45, 1.2, -45, scene); 
  f.rotation.y = s * Math.PI / 4; 
  fences.push(f); 
});

const crowdPositions = [], crowdColors = [];
for (let i = 0; i < 4200; i++) { 
  const angle = TS + R(0.04, TL - 0.04), radius = R(115.5, 120.5), y = R(4.2, 16.2); 
  crowdPositions.push(Math.cos(angle) * radius, y, Math.sin(angle) * radius); 
  const color = new THREE.Color(crowdPalette[Math.floor(Math.random() * crowdPalette.length)]); 
  crowdColors.push(color.r, color.g, color.b); 
}
const crowdGeometry = new THREE.BufferGeometry(); 
crowdGeometry.setAttribute('position', new THREE.Float32BufferAttribute(crowdPositions, 3)); 
crowdGeometry.setAttribute('color', new THREE.Float32BufferAttribute(crowdColors, 3)); 
const crowd = new THREE.Points(crowdGeometry, new THREE.PointsMaterial({ size: 2.1, sizeAttenuation: false, vertexColors: true, transparent: true, opacity: 0.9 })); 
crowd.frustumCulled = false; 
scene.add(crowd);

const boardFrame = mk(new THREE.BoxGeometry(25, 7, 1.4), mat(0x111827, 0.6), 0, 12, -105, scene, false);
const boardFace = mk(new THREE.BoxGeometry(23, 5.4, 0.12), new THREE.MeshBasicMaterial({ color: 0x0f766e }), 0, 12, -104.2, scene, false);
const scoreTexture = tex(512, 128, (g, w, h) => { 
  g.fillStyle = '#0f766e'; g.fillRect(0, 0, w, h); 
}); 
boardFace.material.map = scoreTexture; 
boardFace.material.color.setHex(0xffffff);

const stadiumLights = []; 
[-1, 1].forEach(side => [-1, 1].forEach(depth => { 
  const tower = new THREE.Group(); 
  tower.position.set(side * 112, 0, depth * 72); 
  scene.add(tower); 
  mk(new THREE.CylinderGeometry(0.35, 0.65, 27, 8), mat(0x64748b), 0, 13.5, 0, tower, false); 
  const lamps = mk(new THREE.BoxGeometry(7, 2, 1), new THREE.MeshBasicMaterial({ color: 0xfff7d6 }), 0, 27.2, 0, tower, false); 
  stadiumLights.push(lamps); 
}));

const DOME_RADIUS = 112, DOME_Y = -42, DOME_Z = -25; 
const dome = new THREE.Mesh(
  new THREE.SphereGeometry(DOME_RADIUS, 64, 32, 0, Math.PI * 2, 0, Math.PI / 2), 
  new THREE.MeshBasicMaterial({ color: 0x9bd6ef, transparent: true, opacity: 0.45, side: THREE.DoubleSide, depthWrite: false })
); 
dome.position.set(0, DOME_Y, DOME_Z); 
dome.visible = false; 
scene.add(dome);

const STADIUMS = [
  { name: '야간 클래식', sky: 0x07101c, fog: 0x07101c, seats: 0x24364b, wall: 0x14402e, grass: 0xffffff, dome: false, board: 0x0f766e },
  { name: '돔구장', sky: 0x182b3b, fog: 0x182b3b, seats: 0x334155, wall: 0x155e63, grass: 0xe7f1ea, dome: true, board: 0x1d4ed8 },
  { name: '해안 구장', sky: 0x164e63, fog: 0x164e63, seats: 0x0e7490, wall: 0x0f766e, grass: 0xe1f0ff, dome: false, board: 0x0284c7 },
  { name: '그린 파크', sky: 0x183b2b, fog: 0x183b2b, seats: 0x36533b, wall: 0x2f6b3f, grass: 0xf1f7e8, dome: false, board: 0x3f6212 }
];

function applyStadium(index) {
  selectedStadium = index; 
  const stadium = STADIUMS[index];
  scene.background.setHex(stadium.sky); 
  scene.fog.color.setHex(stadium.fog);
  stands.material.color.setHex(stadium.seats); 
  wall.material.color.setHex(stadium.wall);
  fieldMat.color.setHex(stadium.grass); 
  dome.visible = stadium.dome;
  fences.forEach(f => f.material.color.setHex(stadium.wall)); 
  drawScoreboard();
}

function drawScoreboard() {
  if (!scoreTexture || !scoreTexture.image) return; 
  const g = scoreTexture.image.getContext('2d'), w = 512, h = 128; 
  const color = '#' + STADIUMS[selectedStadium].board.toString(16).padStart(6, '0');
  g.fillStyle = '#07111d'; g.fillRect(0, 0, w, h); 
  g.fillStyle = color; g.fillRect(8, 8, w - 16, h - 16); 
  g.fillStyle = '#ffffff'; g.font = 'bold 22px sans-serif'; g.textAlign = 'left'; 
  g.fillText(STADIUMS[selectedStadium].name.toUpperCase(), 24, 38); 
  g.font = 'bold 17px sans-serif'; g.textAlign = 'left'; 
  g.fillText(teamNames[0].slice(0, 12), 24, 64); 
  g.textAlign = 'right'; g.fillText(teamNames[1].slice(0, 12), w - 24, 64); 
  g.font = 'bold 32px sans-serif'; g.textAlign = 'center'; g.fillText(`${S.sc[0]}  :  ${S.sc[1]}`, w / 2, 94); 
  g.font = 'bold 19px sans-serif'; g.textAlign = 'right'; 
  g.fillText(`${Math.min((S.h >> 1) + 1, maxInnings)}회 ${S.h % 2 ? '말' : '초'}   O ${S.outs}`, w - 22, 113); 
  scoreTexture.needsUpdate = true;
}

applyStadium(0);

function figure(shirt, cap, x, z) {
  const g = new THREE.Group(), m1 = mat(shirt); 
  mk(new THREE.CylinderGeometry(0.09, 0.08, 0.85, 8), mat(0xdddddd), -0.1, 0.43, 0, g); 
  mk(new THREE.CylinderGeometry(0.09, 0.08, 0.85, 8), mat(0xdddddd), 0.1, 0.43, 0, g); 
  mk(new THREE.CylinderGeometry(0.2, 0.17, 0.62, 10), m1, 0, 1.15, 0, g); 
  mk(new THREE.SphereGeometry(0.13, 12, 10), mat(0xe8c9a0), 0, 1.6, 0, g); 
  mk(new THREE.SphereGeometry(0.14, 12, 8, 0, Math.PI * 2, 0, Math.PI / 2), mat(cap), 0, 1.62, 0, g); 
  g.position.set(x, 0, z); scene.add(g); return g;
}

const SPDF = 5.8, B1 = V3(19.4, 0, -19.4), B1T = V3(19.4, 1.2, -19.4), B2P = V3(0, 0, -38.8);
const F = [[17, -20], [7, -31], [-7, -31], [-17, -20], [-40, -62], [0, -76], [40, -62]].map(([x, z]) => { 
  const g = figure(0xcfd6e0, 0xb02020, x, z); 
  g.rotation.y = Math.atan2(-x, 5 - z); 
  return { g, home: V3(x, 0, z) }; 
});

function resetField() { 
  F.forEach(f => { f.g.position.copy(f.home); f.g.rotation.y = Math.atan2(-f.home.x, 5 - f.home.z); }); 
}

const BP = [V3(0, 0, 0.6), V3(19.4, 0, -19.4), V3(0, 0, -38.8), V3(-19.4, 0, -19.4), V3(0, 0, 0.6)];
const pool = [...Array(8)].map(() => { 
  const g = figure(0xf0f0f0, 0x1b2a5c, 0, 0); 
  g.visible = false; 
  return { g, on: false, b: 0, to: 0, t0: 0, sp: 16, out: false, h: 0 }; 
});
let occ = [null, null, null, null];

const pit = figure(0xffffff, 0x1b2a5c, 0, -18.4); 
pit.position.y = 0.28; pit.rotation.y = Math.PI;

const arm = new THREE.Group(); 
arm.position.set(0.24, 2, -18.4); scene.add(arm); 
mk(new THREE.CylinderGeometry(0.05, 0.045, 0.62, 8), mat(0xffffff), 0, -0.31, 0, arm);

const catcher = figure(0x24385f, 0x1b2a5c, 0, 0.9); 
catcher.scale.set(0.92, 0.72, 0.92); catcher.position.set(0, 0.08, 0.9);
const catcherMask = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(0.32, 0.25, 0.12)), new THREE.LineBasicMaterial({ color: 0xd1d5db })); 
catcherMask.position.set(0, 1.45, 0.11); catcher.add(catcherMask);

const bt = new THREE.Group(); scene.add(bt); bt.scale.x = batterSide === 'L' ? -1 : 1;
const batterLegs = [-0.1, 0.1].map((dx) => { 
  const leg = new THREE.Group(); leg.position.set(-0.95 + dx, 0.82, 0.1); bt.add(leg); 
  mk(new THREE.CylinderGeometry(0.09, 0.08, 0.85, 8), mat(0xdddddd), 0, -0.39, 0, leg); return leg; 
});
const up = new THREE.Group(); up.position.set(-0.95, 0.85, 0.1); bt.add(up); 
mk(new THREE.CylinderGeometry(0.2, 0.17, 0.62, 10), mat(0xf0f0f0), 0, 0.3, 0, up); 
mk(new THREE.SphereGeometry(0.13, 12, 10), mat(0xe8c9a0), 0, 0.77, 0, up); 
mk(new THREE.SphereGeometry(0.15, 12, 8, 0, Math.PI * 2, 0, Math.PI / 2), mat(0x1b2a5c), 0, 0.79, 0, up);

const swingArms = new THREE.Group(); swingArms.position.set(0, 0.375, 0); up.add(swingArms); 
[-0.06, 0.06].forEach(dz => { 
  const a = mk(new THREE.CylinderGeometry(0.045, 0.04, 0.42, 8), mat(0xf0f0f0), 0.22, 0, dz, swingArms); a.rotation.z = -2.54; 
});
const BAT_READY = -0.72; 
const bat = new THREE.Group(); bat.position.set(0.28, -0.025, -0.08); bat.rotation.z = BAT_READY; swingArms.add(bat); 
mk(new THREE.CylinderGeometry(0.05, 0.02, 1, 10), mat(0xc99a5b, 0.6), 0, 0.5, 0, bat);

const seam = tex(128, 64, (g, w, h) => { 
  g.fillStyle = '#f4f4ee'; g.fillRect(0, 0, w, h); g.strokeStyle = '#c0392b'; g.lineWidth = 3; 
  [32, 96].forEach(x => { 
    g.beginPath(); g.arc(x + (x < 64 ? -26 : 26), 32, 28, x < 64 ? -0.9 : Math.PI - 0.9, x < 64 ? 0.9 : Math.PI + 0.9); g.stroke(); 
  }); 
});
const ball = new THREE.Mesh(new THREE.SphereGeometry(0.13, 16, 12), new THREE.MeshStandardMaterial({ map: seam, roughness: 0.5 })); 
ball.castShadow = true; ball.visible = false; scene.add(ball);
const shd = new THREE.Mesh(new THREE.CircleGeometry(0.14, 16), new THREE.MeshBasicMaterial({ color: 0, transparent: true, opacity: 0.45, depthWrite: false })); 
shd.rotation.x = -Math.PI / 2; shd.visible = false; scene.add(shd);

const TYPES = [
  { name: '포심', dur: [520, 620], c: 0, l: 0.05, err: 0.035, bias: 0 }, 
  { name: '투심', dur: [580, 700], c: 0.32, l: 0.08, err: 0.055, bias: 12 }, 
  { name: '슬라이더', dur: [720, 840], c: 0.95, l: 0.08, err: 0.07, bias: 35 }, 
  { name: '커브', dur: [850, 960], c: 1.05, l: 0.4, err: 0.09, bias: 25 }, 
  { name: '체인지업', dur: [920, 1040], c: 0.1, l: 0.1, err: 0.06, bias: -95 }, 
  { name: '스위퍼', dur: [800, 920], c: 1.5, l: 0.04, err: 0.08, bias: 55 }, 
  { name: '너클볼', dur: [820, 1050], c: 1.25, l: 0.25, err: 0.16, bias: 100 }
];

const ret = new THREE.Mesh(new THREE.TorusGeometry(0.06, 0.008, 8, 24), new THREE.MeshBasicMaterial({ color: 0xf2b632, fog: false })); 
ret.visible = false; scene.add(ret);
const rc = new THREE.Raycaster(), pln = new THREE.Plane(V3(0, 0, 1), -0.1), mv = new THREE.Vector2(), aim = V3(0, 0.82, 0.15); 
const pciCenter = aim.clone();
const pciRing = new THREE.Mesh(new THREE.TorusGeometry(1, 0.012, 8, 48), new THREE.MeshBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.92, depthTest: false })); 
pciRing.visible = false; scene.add(pciRing);

function pciRadiusFor(hitter, mode = battingMode) { 
  const rating = hitter?.contact || 3; 
  const base = 0.08 + (rating * 0.03); 
  return base * (mode === 'contact' ? 1.35 : mode === 'power' ? 0.82 : 1.12); 
}

function aimAt(e) {
  const r = stage.getBoundingClientRect(); 
  mv.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1); 
  rc.setFromCamera(mv, cam); 
  const h = V3(0, 0, 0);
  if (rc.ray.intersectPlane(pln, h)) { 
    const x = C(h.x, -0.5, 0.5), y = C(h.y, 0.3, 1.4); 
    if (S.mode === 'bat' && pciEnabled) { 
      pciCenter.set(x, y, 0.15); 
      if (S.phase === 'aim') aim.set(x, y, 0.15); 
    } else aim.set(x, y, 0.15); 
  }
}

function setPT(i) { 
  if (PITCHERS[currentPitcherIdx].pitches.includes(i)) { S.pt = i; refreshPitchButtons(); } 
}

function refreshPitchButtons() { 
  const allowed = PITCHERS[currentPitcherIdx].pitches; 
  if (!allowed.includes(S.pt)) S.pt = allowed[0]; 
  document.querySelectorAll('#types button').forEach((btn, i) => { 
    btn.hidden = !allowed.includes(i); 
    btn.classList.toggle('on', S.pt === i); 
  }); 
}

function zoneCall(tx, ty, eyeRating = 3) {
  const eyeBonus = (eyeRating - 3) * 0.025;
  const actual = Math.abs(tx) <= (0.96 - eyeBonus) && Math.abs(ty) <= (0.96 - eyeBonus);
  const edge = Math.min(Math.abs(Math.abs(tx) - 0.96), Math.abs(Math.abs(ty) - 0.96)); 
  const challengeable = edge <= 0.20, wrong = challengeable && Math.random() < 0.04; 
  return { actual, called: wrong ? !actual : actual, challengeable, wrong };
}

function initABSGrid() { 
  const grid = $('absGrid'); if (grid.childElementCount) return; 
  for (let row = 0; row < 7; row++) for (let col = 0; col < 7; col++) { 
    const cell = document.createElement('i'); 
    cell.className = 'abs-cell' + (row >= 1 && row <= 5 && col >= 1 && col <= 5 ? ' zone' : ''); 
    grid.appendChild(cell); 
  } 
}

function updateABS(tx, ty, callText, wrong = false) { 
  initABSGrid(); 
  const col = C(Math.floor((tx + 1.344) / 2.688 * 7), 0, 6); 
  const row = 6 - C(Math.floor((ty + 1.344) / 2.688 * 7), 0, 6); 
  const cell = row * 7 + col; 
  document.querySelectorAll('.abs-cell').forEach((el, i) => { 
    el.classList.toggle('point', i === cell); 
    el.classList.toggle('challenge', i === cell && wrong); 
  }); 
  $('absCall').textContent = callText; 
}

function updatePitchInfo(pitchData) { 
  if (!pitchData) return; 
  const kind = TYPES[S.pt], pitcher = PITCHERS[currentPitcherIdx]; 
  $('pitchInfo').textContent = `⚾ ${kind.name} · ${pitchData.speedKmh} km/h · ${pitcher.arm==='L'?'좌완':'우완'} ${pitcher.formName}`; 
}

function challengeABS() {
  if (!pendingABSCall || challengeCount <= 0 || simTime > pendingABSCall.expires) return;
  const call = pendingABSCall; pendingABSCall = null; challengeCount--;
  if (call.called === call.actual) { 
    updateABS(P.tx, P.ty, `챌린지 실패 · 판정 유지`, false); 
    if (lastPitchReview) { lastPitchReview.review = '실패 · 원심 유지'; renderVideoReview(); } 
    flash('챌린지 실패', `원심 판정 유지 · 남은 횟수 ${challengeCount}`); 
  } else {
    if (call.called === 'strike') { S.strikes = Math.max(0, S.strikes - 1); S.balls++; } 
    else { S.balls = Math.max(0, S.balls - 1); S.strikes++; }
    updateABS(P.tx, P.ty, `챌린지 성공 · ${call.actual === 'strike' ? '스트라이크' : '볼'}`, false); 
    if (lastPitchReview) { lastPitchReview.called = call.actual; lastPitchReview.review = '성공 · 판정 번복'; renderVideoReview(); } 
    flash('판정 번복!', `ABS 챌린지 성공 · 남은 횟수 ${challengeCount}`); 
    snd(880, 0.14, 'sine', 0.2, 1250);
  } 
  board();
}

function currentPitcherStats() { return pitcherStatsById[currentPitcherIdx]; }

function totalBatterStats(players) { 
  return players.reduce((sum, player) => { 
    for (const key of ['pa','ab','hits','walks','hbp','totalBases','runs','rbi']) sum[key] += player.stats[key] || 0; 
    return sum; 
  }, emptyBatterStats()); 
}

function totalPitcherStats() { 
  return Object.values(pitcherStatsById).reduce((sum, ps) => { 
    for (const key of ['outs','strikeouts','walks','hits','hbp','earnedRuns']) sum[key] += ps[key] || 0; 
    return sum; 
  }, emptyPitcherStats()); 
}

function updateStatsUI() {
  const ownBatter = S.mode === 'bat', bs = ownBatter ? batterStats : opponentLineup[opponentBatterIndex].stats, ps = ownBatter ? opponentPitcherStats : currentPitcherStats();
  const avg = bs.ab ? bs.hits / bs.ab : 0, obpDen = bs.ab + bs.walks + bs.hbp, obp = obpDen ? (bs.hits + bs.walks + bs.hbp) / obpDen : 0, slg = bs.ab ? bs.totalBases / bs.ab : 0;
  const ip = ps.outs / 3, era = ip ? (ps.earnedRuns * 9 / ip).toFixed(2) : '—', whip = ip ? ((ps.walks + ps.hits) / ip).toFixed(2) : '—';
  
  const teamBat = totalBatterStats(lineup), teamAvg = teamBat.ab ? teamBat.hits / teamBat.ab : 0, teamOBPden = teamBat.ab + teamBat.walks + teamBat.hbp, teamOBP = teamOBPden ? (teamBat.hits + teamBat.walks + teamBat.hbp) / teamOBPden : 0, teamSLG = teamBat.ab ? teamBat.totalBases / teamBat.ab : 0;
  const teamPitch = totalPitcherStats(), teamIP = teamPitch.outs / 3, teamERA = teamIP ? (teamPitch.earnedRuns * 9 / teamIP).toFixed(2) : '—', teamWHIP = teamIP ? ((teamPitch.walks + teamPitch.hits) / teamIP).toFixed(2) : '—';
  
  $('batterStats').innerHTML = `AVG ${teamAvg.toFixed(3)} · OBP ${teamOBP.toFixed(3)} · SLG ${teamSLG.toFixed(3)} · OPS ${(teamOBP + teamSLG).toFixed(3)}<br>득점 ${teamBat.runs} · 타점 ${teamBat.rbi} · 안타 ${teamBat.hits}`; 
  $('pitcherGameStats').textContent = `ERA ${teamERA} · K ${teamPitch.strikeouts} · BB ${teamPitch.walks} · WHIP ${teamWHIP}`;
  
  const currentHitter = ownBatter ? lineup[battingOrderIndex] : opponentLineup[opponentBatterIndex];
  const traitStr = currentHitter.str ? ` | 강점:${currentHitter.str} 약점:${currentHitter.wk}` : '';
  const statsStr = `[주력 ${currentHitter.speed} | 파워 ${currentHitter.power} | 컨택 ${currentHitter.contact} | 선구 ${currentHitter.eye}${traitStr}]`;
  
  if ($('batterSummary')) $('batterSummary').innerHTML = `<strong>${ownBatter ? '내 타자' : '상대 타자'} · ${ownBatter ? battingOrderIndex + 1 : opponentBatterIndex + 1}번</strong><br><span class="text-emerald-300 text-[10px]">${statsStr}</span><br>AVG ${avg.toFixed(3)} · OBP ${obp.toFixed(3)}`;
  if ($('pitcherSummaryTop')) $('pitcherSummaryTop').innerHTML = `<strong>${ownBatter ? '상대 선발' : PITCHERS[currentPitcherIdx].name}</strong><br>ERA ${era} · K ${ps.strikeouts} · BB ${ps.walks} · WHIP ${whip}`;
}

function recordBatterHit(bases) { 
  const stats = S.mode === 'bat' ? batterStats : opponentLineup[opponentBatterIndex].stats; 
  stats.pa++; stats.ab++; stats.hits++; stats.totalBases += bases; 
  if (S.mode === 'bat') opponentPitcherStats.hits++; else currentPitcherStats().hits++; 
  batterPAMode = S.mode; batterPAComplete = true; 
}
function recordBatterOut() { 
  const stats = S.mode === 'bat' ? batterStats : opponentLineup[opponentBatterIndex].stats; 
  stats.pa++; stats.ab++; 
  batterPAMode = S.mode; batterPAComplete = true; 
}
function finishBatterPA() { 
  if (!batterPAComplete) return; 
  if (batterPAMode === 'bat') { 
    battingOrderIndex = (battingOrderIndex + 1) % lineup.length; 
    batterStats = lineup[battingOrderIndex].stats; 
  } else if (batterPAMode === 'pitch') {
    opponentBatterIndex = (opponentBatterIndex + 1) % opponentLineup.length; 
  }
  batterPAComplete = false; batterPAMode = null; syncBatterAppearance(); 
}

function sim(p0, v0, dur) { 
  const a = [], p = p0.clone(), v = v0.clone(); 
  for (let i = 0; i < dur * 60; i++) { 
    v.y -= 14 / 60; p.addScaledVector(v, 1 / 60); 
    if (p.y < 0.13) { p.y = 0.13; if (v.y < 0) v.y = Math.abs(v.y) > 2.2 ? -v.y * 0.42 : 0; } 
    if (p.y <= 0.14) { 
      v.x *= 1 - 1.0 / 60; v.z *= 1 - 1.0 / 60; 
      if (v.y === 0 && Math.hypot(v.x, v.z) < 0.35) { a.push(p.clone()); break; } 
    } 
    a.push(p.clone()); 
  } 
  return a; 
}

function defend(path, buntPlay = false) {
  const speed = SPDF * 1.5 * (buntPlay ? 1.6 : 1.0);
  for (let i = 12; i < Math.min(path.length, 210); i += 2) { 
    const b = path[i], elapsed = i / 60, air = b.y >= 1.1 && b.y <= 2.8, ground = b.y <= 0.25 && i <= 145 && Math.hypot(b.x, b.z) <= 38; 
    if (!air && !ground) continue; 
    let best = null; 
    for (const f of F) { 
      const q = f.g.position, distance = Math.hypot(q.x - b.x, q.z - b.z), reach = buntPlay ? 1.5 : (air ? 1.0 : 1.3); 
      if (distance <= speed * Math.max(0, elapsed - (buntPlay ? 0.05 : 0)) + reach && (!best || distance < best.distance)) best = { i, f, air, distance }; 
    } 
    if (best) return best; 
  }
  return null;
}

function deferForFielding(bases, t0, extraBase) {
  const target = hit && hit.fieldOpportunity; 
  if (S.mode !== 'pitch' || !target) return false; 
  const impactAt = hit.t + target.i / 60 / 1.7 * 1000;
  pendingFieldingPlay = { target, bases, t0, extraBase, impactAt }; 
  targetTimeScale = 0.25;
  pendingFieldingPlay.cueTimer = setGameTimeout(() => { 
    if (pendingFieldingPlay) { flash('⚡ 질주 버튼 연타!', '호수비 찬스! 시간이 느려집니다!'); board(); } 
  }, Math.max(0, impactAt - simTime - 850));
  pendingFieldingPlay.settleTimer = setGameTimeout(() => resolveFieldingPlay(false), Math.max(0, impactAt - simTime + 950)); 
  return true;
}

function resolveFieldingPlay(saved) {
  const play = pendingFieldingPlay; if (!play) return;
  targetTimeScale = 1.0; 
  clearGameTimeout(play.cueTimer); 
  clearGameTimeout(play.settleTimer); 
  pendingFieldingPlay = null;
  
  if (saved) { 
    const { f, air } = play.target; 
    hit.fieldOpportunity = null; hit.plan = { f, air, out: false, cover: null, throwTo: null }; 
    f.g.scale.y = 1.18; setTimeout(() => { f.g.scale.y = 1; }, 520); 
    recordBatterOut(); addOut(1); finishBatterPA(); 
    flash('슈퍼 캐치!', air ? '다이빙 캐치 성공!' : '강습 타구를 걷어냈습니다!'); 
    snd(880, 0.18, 'sine', 0.25, 1450); 
  }
  else { 
    hit.fieldOpportunity = null; hit.plan = null; hit.chase = play.target.f; 
    recordBatterHit(play.bases); advance(play.bases, play.extraBase, play.t0); finishBatterPA(); 
    flash(play.bases === 2 ? '2루타!' : '안타!', '수비수가 잡지 못했습니다.'); 
  }
  board();
}

function attemptHighlightCatch() {
  const play = pendingFieldingPlay; if (!play || S.mode !== 'pitch') return false;
  if (simTime - play.impactAt >= -850 && simTime - play.impactAt <= 950) { resolveFieldingPlay(true); return true; } 
  return false;
}

function beginThrowCharge() {
  if (!hit || !hit.plan || !hit.plan.waitingManualThrow) return;
  throwCharge = { start: simTime, duration: 800 }; $('timingWrap').style.display = 'block';
  const animate = () => { 
    if (!throwCharge) return; 
    const pct = C((simTime - throwCharge.start) / throwCharge.duration, 0, 1) * 100; 
    $('timingCursor').style.left = pct + '%'; 
    timingAnimId = requestAnimationFrame(animate); 
  }
  timingAnimId = requestAnimationFrame(animate);
}

function releaseThrowCharge() {
  if (!throwCharge) return;
  const pct = C((simTime - throwCharge.start) / throwCharge.duration, 0, 1) * 100; 
  const quality = C(1 - Math.abs(pct - 75) / 18, 0, 1);
  throwCharge = null; $('timingWrap').style.display = 'none'; $('manualThrowBtn').style.display = 'none';
  hit.plan.waitingManualThrow = false; hit.plan.manualThrown = true;
  hit.plan.throwDuration = 1.8 - (quality * 0.8); 
  hit.plan.manualThrowStartTime = simTime; targetTimeScale = 1.0;
  flash(quality > 0.8 ? '총알 송구!' : '송구 완료', '');
}
$('manualThrowBtn').addEventListener('pointerdown', beginThrowCharge);
$('manualThrowBtn').addEventListener('pointerup', releaseThrowCharge);
$('manualThrowBtn').addEventListener('pointercancel', releaseThrowCharge);

function useSprintAction() {
  if (pendingFieldingPlay && S.mode === 'pitch') { attemptHighlightCatch(); return; }
  if (pendingTagUp) {
    const now = simTime; const tag = pendingTagUp; pendingTagUp = null;
    if (now < tag.catchAt - 150) { 
      flash('태그업 아웃!', '포구 전에 출발하여 아웃되었습니다.'); 
      tag.runner.out = true; occ[3] = null; setOcc(occ); addOut(1); board(); 
    } 
    else {
      const reaction = Math.max(0, now - tag.catchAt); 
      const runner = tag.runner; occ[3] = null; setOcc(occ);
      const spd = runnerSpeed(runner, 18) - (reaction * 0.005); 
      runner.to = 4; runner.t0 = now; runner.sp = Math.max(12, spd);
      const throwerPos = hit.path[hit.plan ? hit.plan.i : hit.path.length-1];
      defensiveThrow = { from: throwerPos.clone().setY(1.5), to: BP[4].clone().setY(0.5), start: now, duration: tag.throwDuration, thrower: 'outfield', targetBase: 4 };
      batterRace = { kind: 'sacfly', runner, callAt: now + tag.throwDuration }; S.phase = 'running'; 
      flash('홈 쇄도!', '태그업 성공! 홈을 향해 뜁니다!'); board();
    }
    return;
  }
  if (S.phase === 'running') sprintBatter(); else attemptSteal();
}

function snd(f, d, t, v, f2) { 
  if (!ac) return; 
  try { 
    const T = ac.currentTime, o = ac.createOscillator(), g = ac.createGain(); 
    o.type = t; o.frequency.setValueAtTime(f, T); 
    if (f2) o.frequency.exponentialRampToValueAtTime(f2, T + d); 
    g.gain.setValueAtTime(v, T); g.gain.exponentialRampToValueAtTime(0.001, T + d); 
    o.connect(g); g.connect(ac.destination); o.start(); o.stop(T + d); 
  } catch(e){} 
}
function hitSound() { snd(145, 0.16, 'triangle', 0.28, 52); setTimeout(() => snd(1250, 0.055, 'triangle', 0.12, 420), 8); }
const dots = (n, m) => '●'.repeat(n) + '○'.repeat(m - n);

function addScore(amount) { 
  if (S.mode === 'bat') { S.sc[0] += amount; batterStats.rbi += amount; opponentPitcherStats.earnedRuns += amount; } 
  else { S.sc[1] += amount; opponentLineup[opponentBatterIndex].stats.rbi += amount; if (S.mode === 'pitch') currentPitcherStats().earnedRuns += amount; } 
}

function board() {
  $('mobileAct').textContent = S.mode === 'pitch' ? '투구!' : S.phase === 'aim' ? '타격 준비' : S.phase === 'running' ? '주루 중…' : '스윙!';
  const mobilePitchShift = $('mobilePitchShift'); 
  mobilePitchShift.style.display = S.mode === 'pitch' && S.phase === 'aim' ? 'block' : 'none'; 
  mobilePitchShift.classList.toggle('on', !!pitchCharge);
  
  $('mobileSteal').textContent = '🏃 질주 (태그업)'; 
  $('buntBtn').textContent = buntMode ? '번트 대기 중 · 취소' : '번트 대기'; 
  $('buntBtn').classList.toggle('on', buntMode); 
  $('buntBtn').disabled = S.mode !== 'bat' || S.phase === 'running';
  
  $('battingModeChoices').style.display = S.mode === 'bat' ? 'flex' : 'none'; 
  document.querySelectorAll('#battingModeChoices [data-batting-mode]').forEach(b => b.classList.toggle('on', b.dataset.battingMode === battingMode));
  
  // 송구 모드 UI 토글 버튼
  const tBtn = $('throwToggleBtn');
  if(tBtn) {
      tBtn.textContent = `수비 1루 송구: ${manualThrowMode ? '수동' : '자동'}`;
      tBtn.style.color = manualThrowMode ? '#fbbf24' : '#e2e8f0';
  }

  $('pciBtn').hidden = S.mode !== 'bat'; 
  $('pciBtn').disabled = S.phase === 'running'; 
  $('pciBtn').textContent = `🎯 조준 원: ${pciEnabled ? 'ON' : 'OFF'} (Shift)`;
  
  $('inn').textContent = (Math.min(S.h >> 1, maxInnings - 1) + 1) + '회 ' + (S.h % 2 ? '말' : '초') + (S.mode === 'bat' ? ' 공격' : ' 수비'); 
  $('score').textContent = S.sc[0] + ' : ' + S.sc[1]; 
  $('scoreTeams').textContent = `${teamNames[0].slice(0, 8)} : ${teamNames[1].slice(0, 8)}`;
  
  $('b').textContent = dots(S.balls, 3); $('s').textContent = dots(S.strikes, 2); $('o').textContent = dots(S.outs, 2); 
  document.querySelectorAll('.bs').forEach((e, i) => e.classList.toggle('on', !!S.bases[[1, 0, 2][i]])); 
  document.querySelectorAll('[data-camera]').forEach(b => b.classList.toggle('on', b.dataset.camera === cameraMode));
  
  const canSprint = (S.mode === 'bat' && ((S.bases[0] || S.bases[1]) && (S.phase === 'aim' || S.phase === 'wait') || S.phase === 'running' && !!batterRace || !!pendingTagUp)) || (S.mode === 'pitch' && !!pendingFieldingPlay); 
  $('mobileSteal').disabled = !canSprint;
  
  const challengeButton = $('challengeBtn'); 
  challengeButton.style.display = 'block'; 
  challengeButton.disabled = !pendingABSCall || challengeCount <= 0; 
  challengeButton.textContent = pendingABSCall ? `⚖️ 챌린지 가능 (${challengeCount})` : `⚖️ ABS 챌린지 (${challengeCount})`;
  
  refreshPitchButtons(); updateStatsUI(); updatePitcherUI(); drawScoreboard();
}

// 송구 모드 토글 (인게임 HUD)
$('throwToggleBtn')?.addEventListener('click', () => {
    manualThrowMode = !manualThrowMode;
    board();
});

function flash(t, sub) { 
  const m = $('msg'); m.innerHTML = ''; 
  const a = document.createElement('b'), s = document.createElement('span'); 
  a.textContent = t; s.textContent = sub || ''; 
  m.append(a, s); m.classList.remove('on'); void m.offsetWidth; m.classList.add('on'); 
}

function spawnFirework() {
  const count = 72, positions = new Float32Array(count * 3), colors = new Float32Array(count * 3), velocities = new Float32Array(count * 3), palette = [0xffd43b, 0xff4d6d, 0x38bdf8, 0x4ade80, 0xc084fc, 0xffffff];
  for (let i = 0; i < count; i++) { 
    const theta = R(0, Math.PI * 2), phi = R(0, Math.PI), speed = R(7, 16), ci = new THREE.Color(palette[Math.floor(Math.random() * palette.length)]); 
    velocities[i * 3] = Math.cos(theta) * Math.sin(phi) * speed; velocities[i * 3 + 1] = Math.cos(phi) * speed + 1.5; velocities[i * 3 + 2] = Math.sin(theta) * Math.sin(phi) * speed; 
    colors[i * 3] = ci.r; colors[i * 3 + 1] = ci.g; colors[i * 3 + 2] = ci.b; 
  }
  const geometry = new THREE.BufferGeometry(); 
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3)); 
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
  const material = new THREE.PointsMaterial({ size: 6, sizeAttenuation: false, vertexColors: true, transparent: true, opacity: 0.98, blending: THREE.AdditiveBlending, depthWrite: false }), points = new THREE.Points(geometry, material); 
  points.position.set(R(-44, 44), R(25, 34), R(-105, -82)); points.frustumCulled = false; scene.add(points); fireworks.push({ points, velocities, age: 0 });
}

function updateFireworks(dt) {
  fireworks = fireworks.filter(firework => {
    firework.age += dt; const positions = firework.points.geometry.attributes.position.array;
    for (let i = 0; i < positions.length; i += 3) { 
      firework.velocities[i + 1] -= 10 * dt; positions[i] += firework.velocities[i] * dt; positions[i + 1] += firework.velocities[i + 1] * dt; positions[i + 2] += firework.velocities[i + 2] * dt; 
    }
    firework.points.geometry.attributes.position.needsUpdate = true; firework.points.material.opacity = C(1 - firework.age / 2.2, 0, 1);
    if (firework.age < 2.2) return true; 
    scene.remove(firework.points); firework.points.geometry.dispose(); firework.points.material.dispose(); return false;
  });
}

function triggerHomeRunCelebration() { 
  homeRunCelebrationUntil = simTime + 2600; targetTimeScale = 1.0; bt.visible = true; 
  flash('홈런! 🎆', '장외로 날아갑니다!'); snd(180, 0.38, 'sawtooth', 0.2, 760); 
  [0, 260, 520, 780].forEach(delay => setTimeout(spawnFirework, delay)); 
}
function overlay(t, p) { $('ovT').textContent = t; $('ovP').textContent = p; $('ov').style.display = 'flex'; }

function newRunner(t0, sp) { 
  const q = pool.find(x => !x.on) || pool[0], batterIndex = S.mode === 'bat' ? battingOrderIndex : opponentBatterIndex, rating = S.mode === 'bat' ? (lineup[batterIndex]?.speed || 3) : 3; 
  Object.assign(q, { on: true, b: 0, to: 0, out: false, h: 0, t0, sp: sp * (0.84 + rating * 0.04), speedRating: rating, batterIndex, batterSide: S.mode }); 
  q.g.visible = true; q.g.position.copy(BP[0]); return q; 
}

function runnerSpeed(runner, baseSpeed) { return baseSpeed * (0.84 + (runner?.speedRating || 3) * 0.04); }
function recordRunnerScore(r) { if (!Number.isInteger(r?.batterIndex)) return; const players = r.batterSide === 'bat' ? lineup : opponentLineup; players[r.batterIndex].stats.runs++; }
function setOcc(no) { occ = no; S.bases = [no[1] ? 1 : 0, no[2] ? 1 : 0, no[3] ? 1 : 0]; }
function clearRun() { batterRace = null; pendingTagUp = null; pool.forEach(q => { q.on = false; q.g.visible = false; }); setOcc([null, null, null, null]); }

function advance(n, ex, t0) {
  const no = [null, null, null, null], sp = n >= 4 ? 28 : 16;
  for (let i = 3; i >= 1; i--) { 
    const r = occ[i]; if (!r) continue; 
    const t = Math.min(4, i + n + ex); r.to = t; r.t0 = t0; r.sp = runnerSpeed(r, sp); 
    if (t >= 4) { recordRunnerScore(r); addScore(1); } else no[t] = r; 
  }
  const b = newRunner(t0, sp); b.to = Math.min(n, 4); 
  if (n >= 4) { recordRunnerScore(b); addScore(1); } else no[n] = b; 
  setOcc(no); S.balls = S.strikes = 0; if (S.mode === 'bat') S.hits++;
}
function walk(t0) {
  const r = occ, no = [null, null, null, null], mv = (x, to) => { x.to = to; x.t0 = t0; x.sp = runnerSpeed(x, 16); };
  if (r[1]) { if (r[2]) { if (r[3]) { mv(r[3], 4); recordRunnerScore(r[3]); addScore(1); } mv(r[2], 3); no[3] = r[2]; } else no[3] = r[3]; mv(r[1], 2); no[2] = r[1]; } else { no[2] = r[2]; no[3] = r[3]; }
  const b = newRunner(t0, 16); b.to = 1; no[1] = b; setOcc(no); S.balls = S.strikes = 0;
}

function changeSide() { 
  S.outs = 0; clearRun(); buntMode = false; S.h++; S.mode = S.mode === 'bat' ? 'pitch' : 'bat'; syncBatterAppearance(); 
  const hm = S.fm === 'bat' ? 1 : 0; if (S.h === 2 * maxInnings - 1 && S.sc[hm] > S.sc[1 - hm]) S.h = 2 * maxInnings; 
  $('types').hidden = S.mode !== 'pitch' || S.h >= 2 * maxInnings; 
}
function addOut(n) { S.outs += n; S.balls = S.strikes = 0; if (S.mode === 'pitch') currentPitcherStats().outs += n; else if (S.mode === 'bat') opponentPitcherStats.outs += n; if (S.outs >= 3) changeSide(); }

function beginBatterRace(t0) {
  const runner = newRunner(t0, 9.5); runner.to = 1;
  for (let base = 3; base >= 2; base--) { const other = occ[base]; if (!other) continue; const target = base + 1; other.to = target; other.t0 = t0; other.sp = runnerSpeed(other, 16); occ[base] = null; if (target >= 4) addScore(1); else occ[target] = other; }
  setOcc(occ); const play = hit.plan, raceTime = play.i / (60 * 1.7) + play.throwDuration / 1.7 + 0.2; batterRace = { runner, callAt: t0 + raceTime * 1000 }; S.phase = 'running';
}
function beginBuntRace(t0) {
  const advanced = [null, null, null, null];
  for (let base = 3; base >= 1; base--) { const runner = occ[base]; if (!runner) continue; const target = base + 1; runner.to = target; runner.t0 = t0; runner.sp = runnerSpeed(runner, 13); if (target >= 4) { recordRunnerScore(runner); addScore(1); } else advanced[target] = runner; }
  setOcc(advanced); const runner = newRunner(t0, 9.5); runner.to = 1; const play = hit.plan, raceTime = play.i / (60 * 1.7) + play.throwDuration / 1.7 + 0.2; batterRace = { kind: 'first', runner, callAt: t0 + raceTime * 1000 }; S.phase = 'running';
}
function sprintBatter() { if (S.phase !== 'running' || !batterRace) return; const runner = batterRace.runner; runner.sp = Math.min(30, runner.sp + 3.2); snd(500 + runner.sp * 25, 0.045, 'triangle', 0.13); }

function settleBatterRace() {
  if (!batterRace) return;
  const runner = batterRace.runner;
  const isError = Math.random() < 0.05;
  
  if (batterRace.kind === 'sacfly') {
    const safe = isError || (runner.g.position.distanceTo(BP[4]) < 1.0);
    batterRace = null; targetTimeScale = 1.0; runner.sp = 0;
    lastRace = { kind: 'batter', base: 4, wasSafe: safe, runner: runner };
    if (safe) { runner.g.position.copy(BP[4]); recordRunnerScore(runner); addScore(1); runner.on = false; runner.g.visible = false; flash(isError ? '⚠️ 포구 실책! 득점!' : '세이프!', isError ? '포수가 송구를 놓쳤습니다!' : '희생플라이 득점!'); snd(760, 0.16, 'sine', 0.22, 1120); }
    else { runner.out = true; runner.h = 0; runner.on = false; runner.g.visible = false; flash('아웃!', '홈 보살 아웃!'); snd(210, 0.2, 'sawtooth', 0.2, 90); addOut(1); }
    finishBatterPA(); S.phase = 'result'; board(); return;
  }

  let safe = false;
  if (manualThrowMode && hit.plan && hit.plan.throwTo) {
      if (!hit.plan.manualThrown) safe = true;
      else { const ballArriveTime = hit.plan.manualThrowStartTime + (hit.plan.throwDuration * 1000); safe = simTime < ballArriveTime || isError; }
  } else {
      const reachesFirst = runner.b >= 1 || runner.g.position.distanceTo(BP[1]) <= 0.9;
      safe = isError || (reachesFirst && Math.random() < BASE_RUN_SUCCESS_SCALE);
  }

  batterRace = null; runner.to = safe ? 1 : runner.b; runner.b = safe ? 1 : runner.b; runner.sp = 0;
  lastRace = { kind: 'batter', base: 1, wasSafe: safe, runner: runner };
  if (safe) { runner.g.position.copy(BP[1]); occ[1] = runner; setOcc(occ); if (!isError) S.hits++; recordBatterHit(1); flash(isError ? '⚠️ 1루 송구 실책!' : '세이프!', isError ? '수비수가 공을 흘렸습니다!' : '1루 세이프!'); snd(760, 0.16, 'sine', 0.22, 1120); } 
  else { runner.out = true; recordBatterOut(); flash('아웃!', '1루 아웃!'); snd(210, 0.2, 'sawtooth', 0.2, 90); addOut(1); }
  finishBatterPA(); S.phase = 'result'; board();
}

function finishStealRace(safe) {
  const race = stealRace; if (!race) return;
  const isError = Math.random() < 0.05; safe = isError || (safe && Math.random() < BASE_RUN_SUCCESS_SCALE);
  clearGameTimeout(stealTimerObj); stealTimerObj = null; stealRace = null; const { runner, runnerIdx, targetBase } = race;
  lastRace = { kind: 'steal', base: targetBase, wasSafe: safe, runner: runner };
  if (safe) { runner.g.position.copy(BP[targetBase]); runner.b = targetBase; runner.to = targetBase; occ[targetBase] = runner; occ[runnerIdx] = null; setOcc(occ); flash(isError ? '⚠️ 악송구 실책!' : '⚡ 도루 성공!', isError ? '송구가 빗나갔습니다.' : '완벽한 슬라이딩!'); snd(700, 0.15, 'sine', 0.25, 1000); } 
  else { runner.out = true; runner.h = 0; occ[runnerIdx] = null; setOcc(occ); addOut(1); flash('도루 아웃!', '태그 아웃되었습니다.'); snd(200, 0.2, 'sawtooth', 0.3, 100); }
  isStealing = false; activeStealRunner = null; board();
}
function attemptSteal() {
  if (S.mode !== 'bat' || (S.phase !== 'aim' && S.phase !== 'wait')) return;
  const runnerIdx = occ[2] ? 2 : (occ[1] ? 1 : 0); if (!runnerIdx) return;
  if (!isStealing) {
    isStealing = true; activeStealRunner = occ[runnerIdx]; const runnerScale = 0.84 + (activeStealRunner.speedRating || 3) * 0.04; stealSpeedBonus = 12.0 * runnerScale; const targetBase = runnerIdx + 1;
    activeStealRunner.to = targetBase; activeStealRunner.t0 = simTime; activeStealRunner.sp = stealSpeedBonus;
    const thrower = runnerIdx === 2 || Math.random() < 0.45 ? 'catcher' : 'pitcher', target = BP[targetBase].clone(); target.y = 1.25;
    const pHand = PITCHERS[currentPitcherIdx].hand === 'L' ? -1 : 1;
    const throwFrom = thrower === 'catcher' ? V3(0.15, 1.45, 0.8) : V3(PITCHERS[currentPitcherIdx].releaseX * pHand, PITCHERS[currentPitcherIdx].releaseY, -17.8), throwDuration = 1500 / 1.1;
    defensiveThrow = { from: throwFrom, to: target, start: simTime, duration: throwDuration, thrower, targetBase };
    stealRace = { runner: activeStealRunner, runnerIdx, targetBase, throwAt: simTime + throwDuration }; flash('⚠️ 견제 송구!', `${thrower === 'catcher' ? '포수' : '투수'} 견제구!`); snd(500, 0.1, 'sine', 0.2);
    stealTimerObj = setGameTimeout(() => { if (!stealRace) return; const atBase = stealRace.runner.b >= targetBase || stealRace.runner.g.position.distanceTo(BP[targetBase]) <= 0.7; finishStealRace(atBase); }, throwDuration);
  } else { const runnerScale = 0.84 + (activeStealRunner?.speedRating || 3) * 0.04; stealSpeedBonus = Math.min(30 * runnerScale, stealSpeedBonus + 3.2 * runnerScale); if (activeStealRunner) activeStealRunner.sp = stealSpeedBonus; snd(600 + stealSpeedBonus * 15, 0.05, 'triangle', 0.15); } board();
}

function triggerPassedBall(tt) {
  flash('⚠️ 포수 포일!', '포수가 공을 뒤로 빠뜨렸습니다!'); snd(180, 0.2, 'sawtooth', 0.25);
  const no = [null, null, null, null];
  for (let b = 3; b >= 1; b--) {
    const r = occ[b]; if (!r) continue;
    const t = b + 1; r.to = t; r.t0 = tt; r.sp = runnerSpeed(r, 16);
    if (t >= 4) { recordRunnerScore(r); addScore(1); } else no[t] = r;
  }
  setOcc(no); defensiveThrow = { from: V3(0, 0.4, 0.9), to: V3(R(-2, 2), 0.1, 7.5), start: simTime, duration: 1200, thrower: 'passed', targetBase: 0 };
}

const WIND = 500;
function pitch() {
  if (stealRace) { setGameTimeout(pitch, 80); return; } if (S.mode === 'bat') pciCenter.copy(aim); resetField();
  const profile = DIFFICULTIES[difficulty], targetZone = Math.random() < profile.zoneRate, pData = PITCHERS[currentPitcherIdx];
  if (S.mode === 'bat') S.pt = pData.pitches[Math.floor(Math.random() * pData.pitches.length)];
  let tx = R(-0.5, 0.5), ty = R(-0.5, 0.5); if (!targetZone) { if (Math.random() < 0.6) tx = (Math.random() < 0.5 ? -1 : 1) * R(0.98, 1.3); else ty = (Math.random() < 0.5 ? -1 : 1) * R(0.98, 1.3); }
  
  const currentHitter = S.mode === 'bat' ? lineup[battingOrderIndex] : opponentLineup[opponentBatterIndex];
  const curType = TYPES[S.pt], umpire = zoneCall(tx, ty, currentHitter.eye || 3), fatigue = pitcherFatigueFactor(), baseDur = R(curType.dur[0], curType.dur[1]) / (pData.speed * fatigue * profile.pitchSpeed), speedKmh = Math.round(18.4 / (baseDur / 1000) * 3.6);
  const drain = (1.5 / pData.endurance) * (difficulty === 'hard' ? 1.2 : 1);
  pitcherStamina = Math.max(0, pitcherStamina - drain); savePitcherStamina();
  const pHand = pData.hand === 'L' ? -1 : 1;
  P = { tx, ty, inZone: umpire.called, actualInZone: umpire.actual, challengeable: umpire.challengeable, speedKmh, release: V3(pData.releaseX * pHand, pData.releaseY, -17.8), curve: (Math.random() < 0.4 ? R(-1, 1) : 0) * curType.c * pData.break * fatigue, lift: R(0, 0.35) * curType.l, t0: simTime + WIND, dur: baseDur, done: false }; P.arrive = P.t0 + baseDur; S.phase = 'pitch'; sw = null; hit = null; board(); startTimingGauge(P.t0, P.arrive);
}
function bp(p, o) { const e = Math.min(p, 1.2), a = Math.sin(Math.min(p, 1) * Math.PI), rel = P.release; return o.set(rel.x + (P.tx * 0.4 - rel.x) * e + P.curve * a * 0.5, rel.y + (0.82 + P.ty * 0.5 - rel.y) * e + P.lift * a, rel.z + (0.1 - rel.z) * e); }

function ready() { resetField(); P = null; hit = null; sw = null; isStealing = false; activeStealRunner = null; pitchCharge = null; throwCharge = null; targetTimeScale = 1.0; if (S.mode === 'bat' && pciEnabled) aim.copy(pciCenter); bt.visible = true; defensiveThrow = null; pendingTagUp = null; S.phase = 'aim'; flash(S.mode === 'pitch' ? '투구 준비' : '타격 준비', S.mode === 'bat' ? '투구를 지켜보세요.' : '구종 선택 후 투구'); $('manualThrowBtn').style.display = 'none'; board(); }
function beginPitchCharge() {
  if (S.mode !== 'pitch' || S.phase !== 'aim' || pitchCharge) return; const wrap = $('timingWrap'), cursor = $('timingCursor'), hint = $('timingHint');
  const pData = PITCHERS[currentPitcherIdx], baseDur = 1300 - (pData.ctrl - 0.02) * 18000;
  pitchCharge = { start: simTime, duration: baseDur }; wrap.style.display = 'block'; wrap.dataset.kind = 'pitch'; hint.textContent = '구간 안에서 SHIFT를 놓으세요'; hint.style.display = 'block'; cancelAnimationFrame(timingAnimId);
  const animateCharge = () => { if (!pitchCharge) return; const pct = C((simTime - pitchCharge.start) / pitchCharge.duration, 0, 1) * 100; cursor.style.left = pct + '%'; timingAnimId = requestAnimationFrame(animateCharge); }; timingAnimId = requestAnimationFrame(animateCharge);
}
function cancelPitchCharge() { if (!pitchCharge) return; pitchCharge = null; cancelAnimationFrame(timingAnimId); $('timingWrap').style.display = 'none'; $('timingHint').style.display = 'none'; }
function releasePitchCharge() { if (!pitchCharge) return; const pct = C((simTime - pitchCharge.start) / pitchCharge.duration, 0, 1) * 100, quality = C(1 - Math.abs(pct - 75) / 18, 0, 1); pitchCharge = null; cancelAnimationFrame(timingAnimId); $('timingWrap').style.display = 'none'; $('timingHint').style.display = 'none'; flash(quality >= 0.82 ? '완벽한 릴리스!' : '릴리스 성공', quality > 0 ? '구속 보너스!' : ''); throwPitch(quality, true); }
function throwPitch(releaseQuality = 0, timedRelease = false) {
  const pData = PITCHERS[currentPitcherIdx]; if (S.mode === 'pitch') usedPitcherIds.add(pData.id);
  const T = TYPES[S.pt], quality = C(releaseQuality, 0, 1), fatigue = pitcherFatigueFactor(), timingControlPenalty = timedRelease ? 1 + (1 - quality) * 0.8 : 1, e = T.err * (pData.ctrl / 0.04) / fatigue * timingControlPenalty * (1 - quality * 0.1);
  let tx = C((aim.x + R(-e, e)) / 0.4, -1.3, 1.3), ty = C((aim.y + R(-e, e) - 0.82) / 0.5, -1.3, 1.3);
  const currentHitter = S.mode === 'bat' ? opponentLineup[opponentBatterIndex] : lineup[battingOrderIndex];
  const dur = R(T.dur[0], T.dur[1]) / (pData.speed * fatigue * (1 + quality * 0.1)), speedKmh = Math.round(18.4 / (dur / 1000) * 3.6), drain = (1.5 / pData.endurance) * (difficulty === 'hard' ? 1.2 : 1);
  pitcherStamina = Math.max(0, pitcherStamina - drain); savePitcherStamina();
  const pHand = pData.hand === 'L' ? -1 : 1;
  const umpire = zoneCall(tx, ty, currentHitter.eye || 3), me = { tx, ty, inZone: umpire.called, actualInZone: umpire.actual, challengeable: umpire.challengeable, speedKmh, release: V3(pData.releaseX * pHand, pData.releaseY, -17.8), curve: (T.c * pData.break * fatigue * (1 + quality * 0.55) + quality * 0.12) * (Math.random() < 0.5 ? -1 : 1), lift: T.l, t0: simTime + WIND, dur, done: false };
  me.arrive = me.t0 + me.dur; P = me; S.phase = 'pitch'; sw = null; hit = null; board();
  const sp = S.strikes === 2, aiChance = DIFFICULTIES[difficulty].aiContact;
  if (Math.random() < C((me.actualInZone ? (sp ? 0.95 : 0.75) : (sp ? 0.4 : 0.2)) * aiChance, 0, 0.98)) { const off = T.bias + 170 * (1 + Math.max(Math.abs(tx), Math.abs(ty)) * 0.8) * (R(-1, 1) + R(-1, 1)) / 1.5; setGameTimeout(() => { if (P !== me || S.phase !== 'pitch') return; sw = { t: simTime, ai: true }; resolve(off); }, me.arrive - CONTACT + off - simTime); }
}
function startTimingGauge(startT, arriveT) { const wrap = $('timingWrap'), cursor = $('timingCursor'); wrap.style.display = 'block'; function updateGauge() { const pct = C((simTime - startT) / (arriveT - startT), 0, 1.1) * 100; cursor.style.left = Math.min(100, pct) + '%'; if (simTime < arriveT + 100 && S.phase === 'pitch') timingAnimId = requestAnimationFrame(updateGauge); else setTimeout(() => { wrap.style.display = 'none'; }, 300); } cancelAnimationFrame(timingAnimId); timingAnimId = requestAnimationFrame(updateGauge); }

const LABEL = { hr: '홈런!', double: '2루타', single: '안타', bunt: '번트!', groundout: '땅볼 아웃', flyout: '뜬공 아웃', foul: '파울', whiff: '헛스윙', strike: '스트라이크', ball: '볼' };
const SPD = { hr: [36, 24], double: [27, 11], single: [21, 5.5], groundout: [15.5, 0.35], bunt: [6.8, 0.025], flyout: [17, 16], foul: [20, 12] };

function resolve(off) {
  P.done = true; S.phase = 'result'; updatePitchInfo(P); let r, parts = [], perfectPerfect = false;
  const hitter = S.mode === 'bat' ? lineup[battingOrderIndex] : opponentLineup[opponentBatterIndex];
  
  const pData = PITCHERS[currentPitcherIdx];
  const pHandName = pData.hand === 'L' ? '좌완' : '우완';
  let traitMult = 1.0;
  if (hitter.str === pHandName || hitter.str === pData.formName) { traitMult = 1.25; flash('대타 강점 발동!', '타격 능력이 상승합니다!'); }
  else if (hitter.wk === pHandName || hitter.wk === pData.formName) { traitMult = 0.75; flash('대타 약점 발동!', '타격 능력이 하락합니다!'); }

  if (off === null) {
    r = P.inZone ? 'strike' : 'ball'; const wrongCall = P.inZone !== P.actualInZone; if (!P.actualInZone && Math.abs(P.tx) > 0.96 && Math.abs(P.ty) < 0.85 && Math.random() < 0.1) r = 'hbp';
    updateABS(P.tx, P.ty, `${r === 'strike' ? '스트라이크' : r === 'hbp' ? '몸에 맞음' : '볼'} 판정`, wrongCall);
    const safeToChallenge = r === 'strike' ? S.strikes < 2 : r === 'ball' ? S.balls < 3 : false; pendingABSCall = P.challengeable && safeToChallenge ? { called: r, actual: P.actualInZone ? 'strike' : 'ball', expires: simTime + 4500 } : null; snd(220, 0.08, 'triangle', 0.3, 90);
  } else {
    pendingABSCall = null; updateABS(P.tx, P.ty, '스윙 · 타격 판정');
    const contactScale = hitter && !buntMode ? 1 - (hitter.contact * traitMult - 3) * 0.045 : 1, powerBonus = hitter && !buntMode ? (hitter.power * traitMult - 3) * 2.8 : 0; pciInsideContact = false; let q = Math.max(0, Math.abs(off) * contactScale - powerBonus - (battingMode === 'power' && hitter ? 10 : 0)) + (P.actualInZone ? 0 : 70);
    if (hitter && sw?.user && pciEnabled && !buntMode) { const radius = pciRadiusFor(hitter), pitchDistance = Math.hypot(P.tx * 0.4 - pciCenter.x, 0.82 + P.ty * 0.5 - pciCenter.y); pciInsideContact = pitchDistance <= radius; q *= pciInsideContact ? 0.76 : 1.15; }
    if (hitter && battingMode === 'contact' && !buntMode) q *= 0.78; perfectPerfect = !!(hitter && sw?.user && !buntMode && Math.abs(off) < 30 && P.actualInZone && (!pciEnabled || pciInsideContact)); if (perfectPerfect) q *= 0.52;
    if (buntMode && S.mode === 'bat' && sw?.user) { r = q < 82 ? 'bunt' : q < 140 ? 'foul' : 'whiff'; buntMode = false; board(); parts.push('번트 시도'); } else { if (off < -280) r = 'whiff'; else r = q < 6 ? 'hr' : q < 28 ? 'double' : q < 62 ? 'single' : q < 170 ? (Math.random() < 0.5 ? 'groundout' : 'flyout') : q < 245 ? 'foul' : 'whiff'; parts.push(perfectPerfect ? 'PERFECT PERFECT!' : off < 0 ? '타이밍 빠름' : '타이밍 늦음'); }
    if (r === 'whiff') snd(420, 0.14, 'sine', 0.08, 140); else setTimeout(hitSound, CONTACT); hrContactFrame = replayBuffer.length > 0 ? replayBuffer.length - 1 : 0;
  }
  lastPitchReview = { pitchName: TYPES[S.pt].name, speedKmh: P.speedKmh, called: off === null ? r : '스윙', actual: P.actualInZone ? 'strike' : 'ball', tx: P.tx, ty: P.ty, review: '' }; renderVideoReview();
  const isPassedBall = (r === 'strike' || r === 'ball' || r === 'whiff') && Math.random() < 0.05;

  if (SPD[r]) {
    if (r !== 'foul' && r !== 'hr') setTimeout(() => { bt.visible = false; }, 560);
    const T = simTime + CONTACT, d = C(off / 110, -1, 1), ang = r === 'bunt' ? R(-0.08, 0.08) : r === 'foul' ? (d < 0 ? -1 : 1) * R(0.95, 1.3) : C(d, -0.7, 0.7) * 0.85, [vh, vy] = SPD[r];
    const powerScale = S.mode === 'bat' && r !== 'bunt' ? (1 + (lineup[battingOrderIndex].power * traitMult - 3) * 0.05) * (battingMode === 'power' ? 1.18 : 1) * (perfectPerfect ? 1.18 : 1) : 1;
    const s = vh * R(0.9, 1.1) * powerScale, path = sim(bp(C((T - P.t0) / P.dur, 0, 1), V3(0, 0, 0)), V3(Math.sin(ang) * s, vy * R(0.9, 1.1) * powerScale, -Math.cos(ang) * s), r === 'hr' ? 5.2 : 6.5);
    hit = { t: T, path, plan: null, hr: r === 'hr', bunt: r === 'bunt', chase: null };
    if (r !== 'hr' && r !== 'foul') {
      const possiblePlay = defend(path, r === 'bunt');
      if (possiblePlay) {
        const errorCatch = Math.random() < 0.05;
        if (errorCatch) { r = 'single'; flash('⚠️ 수비 포구 실책!', '공을 놓쳤습니다!'); } else {
          if (r === 'single' || r === 'double') { if (Math.random() < 0.25) r = possiblePlay.air ? 'flyout' : 'groundout'; }
          hit.plan = { f: possiblePlay.f, i: possiblePlay.i, air: possiblePlay.air, out: r === 'groundout' || r === 'bunt' || r === 'flyout', cover: F[0], throwTo: r === 'groundout' || r === 'bunt' ? B1T.clone() : null, throwDuration: 1.6, waitingManualThrow: false, manualThrown: false };
        }
      } else hit.chase = F[4];
      if (S.mode === 'pitch' && (r === 'single' || r === 'double') && possiblePlay && possiblePlay.distance > 0.45 && Math.random() < 0.5) hit.fieldOpportunity = possiblePlay;
    }
  }

  const h0 = S.h, tt = hit ? hit.t : simTime, ex = hit && !hit.plan ? 1 : 0; let label = LABEL[r], dp = false;
  if (isPassedBall) triggerPassedBall(tt);

  if (r === 'hr') { recordBatterHit(4); if (S.mode === 'bat') S.hr++; advance(4, 0, tt); }
  else if (r === 'double') { if (deferForFielding(2, tt, ex)) label = '호수비 찬스!'; else { recordBatterHit(2); advance(2, ex, tt); } }
  else if (r === 'single') { if (deferForFielding(1, tt, ex)) label = '호수비 찬스!'; else { recordBatterHit(1); advance(1, ex, tt); } }
  else if (r === 'bunt') { beginBuntRace(tt); label = '번트 1루 승부!'; }
  else if (r === 'groundout') { if (!occ[1] && hit && hit.plan && hit.plan.throwTo) { beginBatterRace(tt); label = '1루 승부!'; } else { recordBatterOut(); dp = !!(occ[1] && S.outs <= 1 && Math.random() < 0.6); if (dp) label = '병살타!'; addOut(dp ? 2 : 1); } }
  else if (r === 'flyout') { recordBatterOut(); addOut(1); if (S.outs <= 2 && occ[3] && S.mode === 'bat') { const catchAt = tt + (hit.plan ? hit.plan.i / 60 / 1.7 * 1000 : 1200); pendingTagUp = { runner: occ[3], catchAt, throwDuration: 1800 }; label = '태그업 대기!'; parts.push('공이 잡히는 순간 질주 버튼을 누르세요!'); } }
  else if (r === 'foul') { if (S.strikes < 2) S.strikes++; }
  else if (r === 'strike' || r === 'whiff') { S.strikes++; if (S.strikes >= 3) { label = '삼진 아웃!'; recordBatterOut(); if (S.mode === 'pitch') currentPitcherStats().strikeouts++; else opponentPitcherStats.strikeouts++; addOut(1); } }
  else if (r === 'ball') { S.balls++; if (S.balls >= 4) { label = '볼넷'; walk(tt); } }
  else if (r === 'hbp') { label = '몸에 맞는 공'; walk(tt); }

  if (!batterRace && !pendingFieldingPlay && !pendingTagUp) finishBatterPA();
  flash(label, parts.join(', ')); if (r === 'hr') triggerHomeRunCelebration(); board();
  const afterPlayWait = r === 'hr' ? 3800 : S.h !== h0 ? 2600 : 2200;
  setGameTimeout(() => { targetTimeScale = 1.0; if (r === 'hr') startHomeRunCinematicReplay(); else continueAfterPlay(h0); }, afterPlayWait);
}

function continueAfterPlay(h0) { if (S.h >= 2 * maxInnings) end(); else if (S.mode === 'pitch') ready(); else { ready(); setGameTimeout(pitch, 1200); } }

function startHomeRunCinematicReplay() {
  if (replayBuffer.length < 30) { continueAfterPlay(S.h); return; }
  isReplaying = true; $('replayBadge').style.display = 'block';
  const angles = [
    { name: '투수-타자 사이', pos: V3(-1.0, 1.3, -9.2), lookOff: V3(0, 0, 0), fov: 60, text: '앵글 1: 타격 순간 (전측면)' },
    { name: '타자 1인칭', pos: V3(batterSide === 'R' ? -0.8 : 0.8, 1.45, 1.2), lookOff: V3(0, 0, -18.4), fov: 68, text: '앵글 2: 타격 순간 (1인칭)' },
    { name: '포수 1인칭', pos: V3(0, 1.05, 1.6), lookOff: V3(0, 0.5, -18.4), fov: 58, text: '앵글 3: 타격 순간 (포수)' }
  ];
  hrSequence = { angles, curIdx: 0, startFrame: Math.max(0, hrContactFrame - 15), endFrame: hrContactFrame + 30 }; replayFrameIndex = hrSequence.startFrame; flash('홈런 리플레이', angles[0].text);
}

function end() { S.phase = 'over'; const d = S.sc[0] - S.sc[1]; board(); $('types').hidden = true; overlay(d > 0 ? '승리!' : d < 0 ? '패배' : '무승부', `${teamNames[0]} ${S.sc[0]} : ${S.sc[1]} ${teamNames[1]}\n안타 ${S.hits}개, 홈런 ${S.hr}개`); }
function toggleBunt() { if (S.mode !== 'bat' || S.phase === 'running') return; buntMode = !buntMode; board(); }
function setBattingMode(mode) { if (!['power', 'normal', 'contact'].includes(mode)) return; battingMode = mode; board(); }
function togglePCI() { if (S.mode !== 'bat' || S.phase === 'running' || S.phase === 'over') return; pciEnabled = !pciEnabled; if (S.phase === 'aim') pciCenter.copy(aim); board(); }
function syncBatterAppearance() { const currentHitter = S.mode === 'bat' ? lineup[battingOrderIndex] : opponentLineup[opponentBatterIndex]; batterSide = currentHitter?.side || 'R'; bt.scale.x = batterSide === 'L' ? -1 : 1; }
function selectCamera(mode) { if (!['plate', 'pitcher', 'batter'].includes(mode)) return; cameraMode = mode; document.querySelectorAll('[data-camera]').forEach(button => button.classList.toggle('on', button.dataset.camera === cameraMode)); board(); }
function renderVideoReview() { const review = lastPitchReview, box = $('videoReviewText'); if (!review) { box.textContent = '판독할 투구 기록이 없습니다.'; return; } box.textContent = `${review.pitchName} · ${review.speedKmh} km/h\n심판 판정: ${review.called}\nABS 기준: ${review.actual}\n존 위치: X ${review.tx.toFixed(2)} · Y ${review.ty.toFixed(2)}`; }

function openVideoReview() { renderVideoReview(); $('videoReviewPanel').style.display = 'block'; isReviewPaused = true; }
function closeVideoReview() { $('videoReviewPanel').style.display = 'none'; isReviewPaused = false; }
function startSlowReplay() { if (replayBuffer.length < 10) return; $('videoReviewPanel').style.display = 'none'; isReplaying = true; replayFrameIndex = Math.max(0, replayBuffer.length - 200); $('replayBadge').style.display = 'block'; flash('비디오 판독', '슬로우 리플레이 재생 중'); }

$('overrideOutBtn').addEventListener('click', () => { if (lastRace && lastRace.wasSafe) { lastRace.wasSafe = false; occ[lastRace.base] = null; setOcc(occ); addOut(1); lastRace.runner.on = false; lastRace.runner.g.visible = false; flash('판정 번복', '아웃으로 정정되었습니다.'); board(); } else flash('변경 불가', '이미 아웃이거나 최근 주루 기록이 없습니다.'); });
$('overrideSafeBtn').addEventListener('click', () => { if (lastRace && !lastRace.wasSafe) { if (S.outs > 0) { lastRace.wasSafe = true; S.outs = Math.max(0, S.outs - 1); lastRace.runner.b = lastRace.base; lastRace.runner.to = lastRace.base; lastRace.runner.on = true; lastRace.runner.g.visible = true; lastRace.runner.g.position.copy(BP[lastRace.base]); occ[lastRace.base] = lastRace.runner; setOcc(occ); flash('판정 번복', '세이프로 정정되었습니다.'); board(); } } else flash('변경 불가', '이미 세이프거나 최근 주루 기록이 없습니다.'); });

function openPinchHitterMenu() {
  if (S.mode !== 'bat' || (S.phase !== 'wait' && S.phase !== 'aim')) { flash('대타 불가', '타석 대기 중에만 기용할 수 있습니다.'); return; }
  const select = $('pinchTargetSelect'); select.innerHTML = '';
  lineup.forEach((batter, i) => { const opt = document.createElement('option'); opt.value = i; opt.textContent = `${i+1}번 타자: ${batter.name}`; if (i === battingOrderIndex) opt.selected = true; select.appendChild(opt); });
  const list = $('pinchHitterList'); list.innerHTML = '';
  for(let i=0; i<3; i++) {
    const pName = PINCH_NAMES[Math.floor(Math.random() * PINCH_NAMES.length)], pStr = TRAIT_TYPES[Math.floor(Math.random() * TRAIT_TYPES.length)];
    let pWk = TRAIT_TYPES[Math.floor(Math.random() * TRAIT_TYPES.length)]; while(pWk === pStr) pWk = TRAIT_TYPES[Math.floor(Math.random() * TRAIT_TYPES.length)];
    const pSpd = 2 + Math.floor(Math.random() * 4), pPow = 2 + Math.floor(Math.random() * 4), pCon = 2 + Math.floor(Math.random() * 4), pEye = 2 + Math.floor(Math.random() * 4), pSide = Math.random() < 0.5 ? 'L' : 'R';
    const btn = document.createElement('button'); btn.className = 'w-full text-left p-3 rounded-lg border border-slate-700 bg-slate-800 hover:bg-slate-700 text-white cursor-pointer';
    btn.innerHTML = `<div class="font-bold text-amber-300 text-base mb-1">${pName} <span class="text-xs text-slate-300">(${pSide === 'R' ? '우타' : '좌타'})</span></div><div class="text-[10px] text-slate-300 mb-1">파워 ${pPow} | 컨택 ${pCon} | 주력 ${pSpd} | 선구 ${pEye}</div><div class="text-[11px] text-emerald-300">강점: ${pStr} / 약점: ${pWk}</div>`;
    btn.onclick = () => {
      const targetIdx = parseInt(select.value);
      lineup[targetIdx] = { name: pName + ' (대타)', stats: emptyBatterStats(), speed: pSpd, power: pPow, contact: pCon, eye: pEye, side: pSide, str: pStr, wk: pWk };
      if (targetIdx === battingOrderIndex) { batterStats = lineup[battingOrderIndex].stats; syncBatterAppearance(); }
      updateStatsUI(); $('pinchHitterModal').style.display = 'none'; $('timeoutMenu').style.display = 'none'; isTimeOut = false; flash('대타 기용!', `${targetIdx+1}번 타자가 교체되었습니다.`); board();
    }; list.appendChild(btn);
  }
  $('pinchHitterModal').style.display = 'flex';
}
$('openPinchHitterBtn').addEventListener('click', openPinchHitterMenu);
$('closePinchHitterBtn').addEventListener('click', () => { $('pinchHitterModal').style.display = 'none'; });

function start(m) {
  gameTimers.forEach(t => clearGameTimeout(t)); gameTimers.length = 0;
  cancelPitchCharge(); S.fm = S.mode = m || S.fm; S.h = 0; S.sc = [0, 0]; buntMode = false; battingMode = 'normal'; pciEnabled = false; isReviewPaused = false; isTimeOut = false; lastRace = null; $('manualThrowBtn').style.display = 'none'; throwCharge = null;
  teamNames = [$('ownTeamName')?.value?.trim().slice(0, 12) || '우리 팀', $('opponentTeamName')?.value?.trim().slice(0, 12) || '상대 팀'];
  Object.assign(S, { outs: 0, balls: 0, strikes: 0, hits: 0, hr: 0 });
  lineup = Array.from({ length: 9 }, (_, i) => { const entered = $(`lineupName${i}`)?.value?.trim(); return { name: entered || `${i + 1}번 타자`, speed: 1 + Math.floor(Math.random() * 5), power: 1 + Math.floor(Math.random() * 5), contact: 1 + Math.floor(Math.random() * 5), eye: 1 + Math.floor(Math.random() * 5), side: Math.random() < 0.5 ? 'L' : 'R', str: null, wk: null, stats: emptyBatterStats() }; });
  battingOrderIndex = 0; batterStats = lineup[0].stats; batterPAComplete = false; opponentPitcherStats = emptyPitcherStats(); opponentLineup = Array.from({ length: 9 }, (_, i) => ({ name: `상대 ${i + 1}번 타자`, side: Math.random() < 0.5 ? 'L' : 'R', stats: emptyBatterStats(), speed: 3, power: 3, contact: 3, eye: 3, str: null, wk: null })); opponentBatterIndex = 0; batterPAMode = null; lastPitchReview = null; 
  $('videoReviewPanel').style.display = 'none'; $('timeoutMenu').style.display = 'none'; $('pinchHitterModal').style.display = 'none'; $('pitcherModal').style.display = 'none';
  syncBatterAppearance();
  pitcherStatsById = Object.fromEntries(PITCHERS.map(p => [p.id, emptyPitcherStats()])); pitcherStaminaById = Object.fromEntries(PITCHERS.map(p => [p.id, 100])); usedPitcherIds.clear(); challengeCount = 2; pendingABSCall = null; clearRun(); bt.visible = true; defensiveThrow = null; $('types').hidden = S.mode !== 'pitch'; board(); P = null; hit = null; sw = null; resetField();
  $('ov').style.display = 'none'; S.phase = 'wait'; flash('플레이 볼!', S.mode === 'bat' ? '초 공격 시작' : '초 수비 시작'); pitcherStamina = 100; refreshPitchButtons(); updateStatsUI(); updatePitcherUI();
  setGameTimeout(() => { if (S.mode === 'pitch') ready(); else { ready(); setGameTimeout(pitch, 1200); } }, 900);
}

function act() {
  if (pitchCharge) return; if (!ac) { try { ac = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) {} } if (ac && ac.state === 'suspended') ac.resume();
  if (S.phase === 'idle' || S.phase === 'over') return start(S.fm);
  if (S.phase === 'aim') { if (S.mode === 'pitch') return throwPitch(); return; }
  if (S.phase !== 'pitch' || sw || S.mode === 'pitch') return; sw = { t: simTime, user: true, bunt: buntMode }; resolve(simTime + CONTACT - P.arrive);
}

stage.addEventListener('wheel', e => { e.preventDefault(); camZoom += e.deltaY * 0.001; camZoom = C(camZoom, 0.4, 1.8); });

/* ---------------- 메인 틱 (Tick) ---------------- */
function tick(realNow) {
  const realDt = Math.min(0.04, (realNow - lastReal) / 1000); lastReal = realNow;
  let dt = 0;
  if (!isReviewPaused && !isTimeOut) {
    currentTimeScale += (targetTimeScale - currentTimeScale) * Math.min(1, realDt * 8); dt = realDt * currentTimeScale; simTime += dt * 1000;
    for (let i = gameTimers.length - 1; i >= 0; i--) { const t = gameTimers[i]; if (t.canceled) { gameTimers.splice(i, 1); continue; } if (simTime >= t.triggerAt) { gameTimers.splice(i, 1); try { t.fn(); } catch(e){ console.error(e); } } }
  }

  // --- 리플레이 모드 ---
  if (isReplaying) {
    if (replayBuffer.length > 0) {
      const snapIndex = Math.floor(replayFrameIndex), snap = replayBuffer[Math.min(snapIndex, replayBuffer.length - 1)];
      if (snap) {
        ball.visible = snap.ballVis; ball.position.copy(snap.ballPos); shd.visible = snap.ballVis; shd.position.set(snap.ballPos.x, 0.06, snap.ballPos.z);
        bt.visible = snap.btVis; bt.position.copy(snap.btPos); bt.rotation.y = snap.btRotY; swingArms.rotation.copy(snap.armsRot); bat.rotation.copy(snap.batRot);
        snap.fielders.forEach((pos, idx) => { if (F[idx]) F[idx].g.position.copy(pos); }); snap.runners.forEach((r, idx) => { if (pool[idx]) { pool[idx].g.visible = r.vis; pool[idx].g.position.copy(r.pos); } });
      }

      if (hrSequence) {
        const distToContact = Math.abs(replayFrameIndex - hrContactFrame);
        let replaySpeed = (distToContact < 15) ? 0.15 : 0.8; // 스피드 램핑
        
        const curAngle = hrSequence.angles[hrSequence.curIdx];
        cam.position.lerp(curAngle.pos, 0.1); look.lerp(curAngle.lookOff.lengthSq() > 0 ? curAngle.lookOff : (snap ? snap.ballPos : DEF), 0.1); cam.lookAt(look);
        if (cam.fov !== curAngle.fov * camZoom) { cam.fov = curAngle.fov * camZoom; cam.updateProjectionMatrix(); }
        
        replayFrameIndex += replaySpeed;
        let currentEndFrame = (hrSequence.curIdx === 0) ? hrSequence.endFrame : Math.min(hrSequence.endFrame, hrContactFrame + 40);
        if (replayFrameIndex > currentEndFrame) { hrSequence.curIdx++; if (hrSequence.curIdx < hrSequence.angles.length) { replayFrameIndex = hrSequence.startFrame; flash('홈런 리플레이', hrSequence.angles[hrSequence.curIdx].text); } else { isReplaying = false; hrSequence = null; $('replayBadge').style.display = 'none'; continueAfterPlay(S.h); } }
      } else {
        if (snap) { lookT.set(snap.ballPos.x, Math.max(0.5, snap.ballPos.y), snap.ballPos.z); liveCamPos.set(snap.ballPos.x * 0.5, Math.max(2, snap.ballPos.y + 1), snap.ballPos.z + 5); cam.position.lerp(liveCamPos, 0.1); look.lerp(lookT, 0.1); cam.lookAt(look); }
        replayFrameIndex += 0.4; if (replayFrameIndex >= replayBuffer.length) { isReplaying = false; $('replayBadge').style.display = 'none'; $('videoReviewPanel').style.display = 'block'; }
      }
    }
    const finalFovReplay = (hrSequence ? hrSequence.angles[hrSequence.curIdx].fov : 54) * camZoom;
    if (cam.fov !== finalFovReplay) { cam.fov = finalFovReplay; cam.updateProjectionMatrix(); } ren.render(scene, cam); requestAnimationFrame(tick); return;
  }

  if (S.phase !== 'idle' && S.phase !== 'over' && !isReviewPaused && !isTimeOut) {
    replayBuffer.push({ ballPos: ball.position.clone(), ballVis: ball.visible, btPos: bt.position.clone(), btRotY: bt.rotation.y, btVis: bt.visible, armsRot: swingArms.rotation.clone(), batRot: bat.rotation.clone(), fielders: F.map(f => f.g.position.clone()), runners: pool.map(r => ({ vis: r.g.visible, pos: r.g.position.clone() })) });
    if (replayBuffer.length > REPLAY_MAX_FRAMES) replayBuffer.shift();
  }

  if (S.phase === 'pitch' && !P.done && simTime + CONTACT > P.arrive + 200) resolve(null);

  const pitcher = PITCHERS[currentPitcherIdx];
  const pHandMult = pitcher.hand === 'L' ? -1 : 1;
  arm.position.set(pitcher.releaseX * pHandMult, pitcher.releaseY + 0.08, -18.4);
  
  const deliveryStart = P ? P.t0 - WIND : 0, deliveryActive = !!P && simTime >= deliveryStart && simTime <= deliveryStart + 660, deliveryT = deliveryActive ? C((simTime - deliveryStart) / 660, 0, 1) : 1, drive = deliveryT < 0.48 ? deliveryT / 0.48 : 1 - (deliveryT - 0.48) / 0.52, recover = deliveryT < 0.48 ? 0 : (deliveryT - 0.48) / 0.52;
  if (!deliveryActive) arm.rotation.set(-0.2, 0, 0); 
  else if (pitcher.form === 'over') arm.rotation.set(deliveryT < 0.48 ? -0.2 - 3.15 * drive : -3.35 + 3.15 * recover, 0.04 * pHandMult, 0.08 * pHandMult); 
  else if (pitcher.form === 'side') arm.rotation.set(-0.32 - 0.35 * drive + 0.67 * recover, 0, (deliveryT < 0.48 ? -0.18 - 2.0 * drive : -2.18 + 2.0 * recover) * pHandMult); 
  else if (pitcher.form === 'under') arm.rotation.set(deliveryT < 0.48 ? 0.55 + 1.05 * drive : 1.6 - 1.8 * recover, 0.12 * pHandMult, (0.25 + 0.3 * drive - 0.37 * recover) * pHandMult); 
  else arm.rotation.set(deliveryT < 0.48 ? -0.1 - 2.45 * drive : -2.55 + 2.45 * recover, 0.12 * pHandMult, (deliveryT < 0.48 ? 0.18 - 0.48 * drive : -0.3 + 0.3 * recover) * pHandMult);
  
  if (defensiveThrow && simTime >= defensiveThrow.start) { const throwPose = C((simTime - defensiveThrow.start) / 280, 0, 1); if (defensiveThrow.thrower === 'pitcher') arm.rotation.z = -1.5 * throwPose * pHandMult; else { catcher.rotation.y += (defensiveThrow.targetBase === 2 ? -0.3 : 0.3) * throwPose; catcher.position.y = 0.08 + 0.5 * throwPose; } } else { catcher.rotation.y = Math.PI; catcher.position.y = 0.08; }

  if (sw?.bunt) { const hold = 1 - C((simTime - sw.t - 250) / 260, 0, 1); swingArms.rotation.set(-0.28 * hold, 0.08 * hold, 0.02 * hold); bat.position.x = (batterSide === 'L' ? 0.58 : 0.48); bat.rotation.set(0, 0, Math.PI / 2 * hold + BAT_READY * (1 - hold)); }
  else if (sw) { bat.position.x = 0.28; const elapsed = simTime - sw.t, smooth = x => { x = C(x, 0, 1); return x * x * (3 - 2 * x); }, load = smooth(elapsed / 170), drv = smooth((elapsed - 170) / 190), finish = smooth((elapsed - 360) / 360); swingArms.rotation.y = elapsed < 170 ? -0.22 - 0.92 * load : elapsed < 360 ? -1.14 + 2.35 * drv : 1.21 - 0.42 * finish; swingArms.rotation.z = elapsed < 170 ? -0.12 * load : elapsed < 360 ? -0.12 + 0.48 * drv : 0.36 - 0.18 * finish; bat.rotation.z = elapsed < 170 ? BAT_READY - 0.62 * load : elapsed < 360 ? BAT_READY - 0.62 + 2.05 * drv : BAT_READY + 1.43 - 0.5 * finish; } 
  else if (buntMode && S.mode === 'bat') { bat.position.x = batterSide === 'L' ? 0.58 : 0.48; bat.rotation.set(0, 0, Math.PI / 2); } else { bat.position.x = 0.28; swingArms.rotation.set(0, 0, 0); bat.rotation.z = BAT_READY; }
  
  if (homeRunCelebrationUntil > simTime) { const celebrationT = simTime / 1000; bt.visible = true; swingArms.rotation.set(-0.32, 0.12, 0.82 + Math.sin(celebrationT * 7) * 0.12); }

  pool.forEach(r => {
    if (!r.on || simTime < r.t0) return;
    if (r.b >= r.to) { if (r.out && !r.h) { r.h = 1; setTimeout(() => { r.on = false; r.g.visible = false; }, 500); } else if (r.to >= 4) { r.on = false; r.g.visible = false; } return; }
    const tg = BP[r.b + 1], q = r.g.position, dx = tg.x - q.x, dz = tg.z - q.z, d = Math.hypot(dx, dz), st = r.sp * dt;
    if (d <= st) { q.x = tg.x; q.z = tg.z; r.b++; } else { q.x += dx / d * st; q.z += dz / d * st; } r.g.rotation.y = Math.atan2(dx, dz);
  });
  if (stealRace) { const atBase = stealRace.runner.b >= stealRace.targetBase || stealRace.runner.g.position.distanceTo(BP[stealRace.targetBase]) <= 0.7; if (atBase && simTime < stealRace.throwAt) finishStealRace(true); }
  
  if (hit && hit.plan && hit.plan.throwTo && manualThrowMode && S.mode === 'pitch') {
      const catchK = hit.plan.i / 60, k = (simTime - hit.t) / 1000 * 1.7;
      if (k >= catchK && !hit.plan.manualThrown && !hit.plan.waitingManualThrow) {
          hit.plan.waitingManualThrow = true;
          const proj = B1.clone().project(cam);
          const btn = $('manualThrowBtn'); btn.style.left = (proj.x * 0.5 + 0.5) * stage.clientWidth + 'px'; btn.style.top = (-(proj.y * 0.5) + 0.5) * stage.clientHeight + 'px'; btn.style.display = 'block';
          targetTimeScale = 0.2; flash('1루 송구 대기!', '수동 버튼(화면 중앙/1루 위치)을 길게 누르세요!');
      }
  }
  
  let readyToSettle = false;
  if (batterRace && batterRace.kind !== 'sacfly') {
      readyToSettle = simTime >= batterRace.callAt || batterRace.runner.b >= 1;
      if (manualThrowMode && hit?.plan?.throwTo && !hit.plan.manualThrown) readyToSettle = false;
      if (batterRace.runner.b >= 1) readyToSettle = true;
  }
  if (batterRace && batterRace.kind === 'sacfly') {
      const distToHome = batterRace.runner.g.position.distanceTo(BP[4]);
      if (distToHome < 6.0) targetTimeScale = 0.25;
      readyToSettle = simTime >= batterRace.callAt || batterRace.runner.b >= 4;
  }
  if (readyToSettle) settleBatterRace();

  if (hit && hit.path && hit.path.length > 0) {
    const k = (simTime - hit.t) / 1000 * 1.7;
    if (k >= 0) {
      const idx = Math.min(hit.path.length - 1, Math.floor(k * 60)), ballPos = hit.path[idx], pl = hit.plan;
      F.forEach(f => {
        let tg = null;
        if (pl && f === pl.f) tg = hit.path[pl.i] || ballPos; else if (hit.fieldOpportunity && hit.fieldOpportunity.f === f) tg = hit.path[hit.fieldOpportunity.i] || ballPos; else if (hit.chase === f) tg = ballPos;
        if (tg) { const q = f.g.position, dx = tg.x - q.x, dz = tg.z - q.z, d = Math.hypot(dx, dz); if (d > 0.1) { const st = Math.min(SPDF * 1.5 * 1.7 * dt, d); q.x += (dx / d) * st; q.z += (dz / d) * st; f.g.rotation.y = Math.atan2(dx, dz); } }
      });
    }
  }

  ret.visible = S.mode === 'pitch' && S.phase === 'aim'; ret.position.set(aim.x, aim.y, 0.15);
  const activeHitter = lineup[battingOrderIndex], pciRadius = pciRadiusFor(activeHitter), pciAim = S.phase === 'aim' ? aim : pciCenter;
  pciRing.visible = S.mode === 'bat' && pciEnabled && (S.phase === 'aim' || S.phase === 'pitch'); pciRing.position.set(pciAim.x, pciAim.y, 0.15); pciRing.scale.set(pciRadius, pciRadius * 1.12, 1);

  let vis = false, follow = false;
  if (P && simTime >= P.t0 && !(hit && simTime >= hit.t)) { const p = (simTime - P.t0) / P.dur; if (p < 1.15) { bp(p, ball.position); vis = true; ball.rotation.x -= dt * 22; } }
  if (hit && simTime >= hit.t) {
    const k = (simTime - hit.t) / 1000 * 1.7, n = hit.path.length, rawIndex = Math.min(n - 1, Math.floor(k * 60)), plan = hit.plan;
    if (plan && plan.throwTo) {
      if (manualThrowMode && !plan.manualThrown) { ball.position.copy(hit.path[plan.i]); vis = true; follow = true; } 
      else {
          let startT = manualThrowMode ? plan.manualThrowStartTime : hit.t + (plan.i / 60 / 1.7 * 1000);
          let tProg = C((simTime - startT) / (plan.throwDuration * 1000), 0, 1);
          ball.position.lerpVectors(hit.path[plan.i], plan.throwTo, tProg); vis = tProg < 1.0; follow = true;
      }
    } else if (plan) { ball.position.copy(hit.path[Math.min(rawIndex, plan.i)]); vis = k < plan.i / 60 + 0.14; follow = true; } else { ball.position.copy(hit.path[rawIndex]); vis = rawIndex < n - 1; follow = true; }
    ball.rotation.x -= dt * 18;
  }
  if (defensiveThrow && simTime >= defensiveThrow.start) {
    const progress = C((simTime - defensiveThrow.start) / defensiveThrow.duration, 0, 1);
    ball.position.lerpVectors(defensiveThrow.from, defensiveThrow.to, progress); ball.position.y += Math.sin(progress * Math.PI) * 2.2; ball.rotation.x -= dt * 28; vis = progress < 1; if (progress >= 1) defensiveThrow = null;
  }
  ball.visible = vis; shd.visible = vis; if (vis) { shd.position.set(ball.position.x, 0.06, ball.position.z); shd.scale.setScalar(1 / (1 + ball.position.y * 0.12)); }

  catcher.visible = !(cameraMode === 'batter');
  
  if (isStealing && activeStealRunner) {
    const runPos = activeStealRunner.g.position, tgtPos = BP[activeStealRunner.to], dir = new THREE.Vector3().subVectors(tgtPos, runPos).normalize();
    lookT.copy(tgtPos).setY(1.0); liveCamPos.set(runPos.x - dir.x * 3.5, 2.2, runPos.z - dir.z * 3.5); fov = 60;
  } else if (defensiveThrow && simTime >= defensiveThrow.start) {
    lookT.set(ball.position.x, ball.position.y, ball.position.z); liveCamPos.set(ball.position.x - 2, Math.max(1.5, ball.position.y + 1), ball.position.z + 4); fov = 50;
  } else if (hit?.hr && simTime >= hit.t) {
    lookT.set(ball.position.x, ball.position.y, ball.position.z); liveCamPos.set(ball.position.x - 2.5, Math.max(1.8, ball.position.y + 1.5), ball.position.z + 4.5); fov = 54;
  } else if (follow) {
    lookT.set(ball.position.x * 0.9, Math.max(1, ball.position.y * 0.8), Math.min(ball.position.z, -6));
  } else {
    if (cameraMode === 'pitcher') { desiredCamPos = V3(1.5, 1.8, -21.4); lookT.set(0, 0.85, 0); fov = 55; }
    else if (cameraMode === 'batter') { desiredCamPos = V3(0, 1.45, 1.2); lookT.set(0, 1.0, -18.4); fov = 65; }
    else { desiredCamPos = camPos.clone(); lookT.copy(DEF); fov = 52; }
    liveCamPos.lerp(desiredCamPos, 0.08); 
  }
  
  const finalFov = fov * camZoom;
  if (cam.fov !== finalFov) { cam.fov = finalFov; cam.updateProjectionMatrix(); }
  look.lerp(lookT, 0.1); cam.position.copy(liveCamPos); cam.lookAt(look);

  if (!isReviewPaused && !isTimeOut) updateFireworks(dt);
  ren.render(scene, cam); requestAnimationFrame(tick);
}

document.querySelectorAll('#throwChoices [data-throw]').forEach(b => b.addEventListener('click', () => { manualThrowMode = b.dataset.throw === 'manual'; document.querySelectorAll('#throwChoices [data-throw]').forEach(btn => btn.classList.toggle('on', btn === b)); board(); }));
stage.addEventListener('pointerdown', e => { if (e.target.closest('#ov, #gameHud, #absPanel, #videoReviewPanel, #timingWrap, #timeoutMenu, #pinchHitterModal, #pitcherModal, button, input, select')) return; e.preventDefault(); if (attemptHighlightCatch()) return; if (S.mode === 'pitch' && S.phase === 'aim') { aimAt(e); act(); } else if (S.mode === 'bat' && pciEnabled && S.phase === 'aim') aimAt(e); else act(); });
stage.addEventListener('pointermove', e => { if ((S.mode === 'pitch' && S.phase === 'aim') || (S.mode === 'bat' && pciEnabled)) aimAt(e); });
$('types').addEventListener('click', e => { const b = e.target.closest('button'); if (b) { setPT(+b.dataset.i); } });
$('mobileAct').addEventListener('click', () => act()); $('mobileSteal').addEventListener('click', useSprintAction); $('buntBtn').addEventListener('click', toggleBunt); $('pciBtn').addEventListener('click', togglePCI);
document.querySelectorAll('#battingModeChoices [data-batting-mode]').forEach(b => b.addEventListener('click', () => setBattingMode(b.dataset.battingMode))); document.querySelectorAll('[data-camera]').forEach(b => b.addEventListener('click', () => selectCamera(b.dataset.camera)));
$('videoReviewBtn').addEventListener('click', openVideoReview); $('playSlowReplayBtn').addEventListener('click', startSlowReplay); $('closeVideoReview').addEventListener('click', closeVideoReview);
$('changePitcherBtn').addEventListener('click', openPitcherModal); $('closePitcherModal').addEventListener('click', () => { $('pitcherModal').style.display = 'none'; });

$('go').addEventListener('click', (e) => { e.stopPropagation(); start('bat'); }); $('go2').addEventListener('click', (e) => { e.stopPropagation(); start('pitch'); });
document.querySelectorAll('#stadiumChoices .stadium-choice').forEach(button => { button.addEventListener('click', () => { applyStadium(Number(button.dataset.stadium)); document.querySelectorAll('#stadiumChoices .stadium-choice').forEach(b => b.classList.toggle('on', b === button)); }); });
document.querySelectorAll('#difficultyChoices [data-difficulty]').forEach(button => { button.addEventListener('click', () => { difficulty = button.dataset.difficulty; document.querySelectorAll('#difficultyChoices [data-difficulty]').forEach(b => b.classList.toggle('on', b === button)); }); });
document.querySelectorAll('#inningChoices [data-innings]').forEach(button => { button.addEventListener('click', () => { maxInnings = Number(button.dataset.innings); document.querySelectorAll('#inningChoices [data-innings]').forEach(b => b.classList.toggle('on', b === button)); drawScoreboard(); }); });
$('challengeBtn').addEventListener('click', challengeABS);

$('resumeGameBtn').addEventListener('click', () => { $('timeoutMenu').style.display = 'none'; isTimeOut = false; flash('경기 재개', '타임이 해제되었습니다.'); board(); });

addEventListener('keydown', e => {
  if (e.target instanceof HTMLElement && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
  if (e.code === 'Escape') { 
    e.preventDefault(); 
    if (!isTimeOut && !isReviewPaused && !isReplaying && S.phase !== 'idle' && S.phase !== 'over') { 
      isTimeOut = true; $('timeoutMenu').style.display = 'flex';
      $('openPinchHitterBtn').style.display = (S.mode === 'bat' && (S.phase === 'wait' || S.phase === 'aim')) ? 'block' : 'none';
    } 
  }
  else if (e.code === 'ShiftLeft' || e.code === 'ShiftRight') { e.preventDefault(); if (!e.repeat) { if (S.mode === 'bat') togglePCI(); else beginPitchCharge(); } }
  else if (e.code === 'Space') { e.preventDefault(); if (!e.repeat) act(); }
  else if (e.code === 'KeyS') useSprintAction();
  else if (e.code === 'KeyB') toggleBunt();
});
addEventListener('keyup', e => { if ((e.code === 'ShiftLeft' || e.code === 'ShiftRight') && pitchCharge) { e.preventDefault(); releasePitchCharge(); } });

updatePitcherUI(); initABSGrid(); board(); requestAnimationFrame(tick);
})();
</script>
</body>
</html>"""
components.html(GAME_HTML, height=1050, scrolling=True)
