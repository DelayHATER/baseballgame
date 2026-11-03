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

GAME_HTML = r'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<title>컴투스아마추어야구2026</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@400;600;800&display=swap">
<style>
:root {
  --ink: #0b1726;
  --deep: #060d17;
  --chalk: #f3f4f6;
  --lamp: #fbbf24;
  --lamp-glow: #f59e0b;
  --dim: #9ca3af;
  --line: #1f2937;
}
* { box-sizing: border-box; touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
body {
  margin: 0; background: var(--deep); color: var(--chalk);
  font-family: 'Noto Sans KR', sans-serif;
  min-height: 100vh; display: flex; justify-content: center; align-items: center;
  padding: 8px; overflow-x: hidden;
}
.font-title { font-family: 'Black Han Sans', sans-serif; }
#stage {
  position: relative; width: 100%; aspect-ratio: 16/10;
  border-radius: 12px; overflow: hidden; background: #000;
  box-shadow: 0 10px 30px rgba(0,0,0,0.8);
}
@media (max-aspect-ratio: 1/1) {
  #stage { aspect-ratio: 4/5; max-height: 55vh; }
}
#stage canvas { display: block; width: 100%; height: 100%; }

/* 야구장 상황판 다이아몬드 */
#dia { position: absolute; top: 12px; right: 12px; width: 54px; height: 54px; pointer-events: none; }
.bs { position: absolute; width: 14px; height: 14px; transform: rotate(45deg); border: 2px solid rgba(255,255,255,0.4); background: rgba(0,0,0,0.4); transition: all 0.2s; }
.bs.on { background: var(--lamp); border-color: var(--lamp); box-shadow: 0 0 8px var(--lamp); }

/* 메시지 팝업 패널 */
#msg { position: absolute; left: 0; right: 0; top: 25%; text-align: center; pointer-events: none; opacity: 0; z-index: 20; }
#msg b { display: block; font-size: clamp(32px, 6vw, 56px); color: var(--lamp); text-shadow: 0 4px 12px rgba(0,0,0,0.9); font-family: 'Black Han Sans'; }
#msg span { display: block; margin-top: 4px; font-size: 15px; text-shadow: 0 2px 6px rgba(0,0,0,0.9); color: #fff; font-weight: 600; }
#msg.on { animation: pop 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
@keyframes pop { 0%{opacity:0;transform:scale(0.7)} 15%{opacity:1;transform:scale(1.05)} 80%{opacity:1} 100%{opacity:0;transform:scale(1)} }

/* 타격 타이밍 게이지 바 */
#timingWrap {
  position: absolute; bottom: 12px; left: 50%; transform: translateX(-50%);
  width: 85%; max-width: 320px; height: 20px; background: rgba(15,23,42,0.85);
  border: 2px solid rgba(255,255,255,0.3); border-radius: 10px; overflow: hidden; display: none; z-index: 15;
}
#timingTarget { position: absolute; left: 65%; width: 20%; height: 100%; background: rgba(34,197,94,0.6); border-left: 2px solid #22c55e; border-right: 2px solid #22c55e; }
#timingPerfect { position: absolute; left: 72%; width: 6%; height: 100%; background: #fbbf24; }
#timingCursor { position: absolute; left: 0%; width: 4px; height: 100%; background: #ef4444; box-shadow: 0 0 6px #ef4444; }
#timingHint { display:none; position:absolute; left:50%; bottom:38px; transform:translateX(-50%); z-index:15; padding:3px 8px; border-radius:6px; background:rgba(2,6,23,.88); color:#fbbf24; font-size:12px; font-weight:800; white-space:nowrap; pointer-events:none; }

/* 오버레이 메뉴 */
#ov { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; gap: 7px; padding: 12px; overflow-y:auto; background: rgba(6,13,23,0.92); backdrop-filter: blur(4px); z-index: 30; }
#ov[hidden] { display: none; }

/* 컨트롤 */
.btn-action { background: linear-gradient(135deg, #fbbf24, #d97706); color: #0b1726; font-weight: 800; border-radius: 8px; box-shadow: 0 4px 12px rgba(251,191,36,0.3); }
.btn-action:active { transform: translateY(1px); }
.pitch-btn { background: #1e293b; border: 1px solid #334155; color: #cbd5e1; border-radius: 6px; font-size: 13px; font-weight: 600; padding: 8px 4px; }
.pitch-btn.on { background: var(--lamp); color: #0b1726; border-color: var(--lamp); font-weight: 800; }
.stadium-choice { background:#172554; border:1px solid #475569; border-radius:8px; color:#e2e8f0; padding:8px 10px; font-weight:700; }
.stadium-choice.on { background:#fbbf24; color:#0b1726; border-color:#fbbf24; }
#absPanel { position:absolute; left:10px; bottom:10px; z-index:18; padding:8px; border-radius:8px; background:rgba(2,6,23,.88); border:1px solid rgba(226,232,240,.35); color:#f8fafc; font-size:10px; }
#absGrid { display:grid; grid-template-columns:repeat(5,15px); gap:2px; margin:5px auto; }
.abs-cell { width:15px; height:15px; border:1px solid rgba(255,255,255,.22); background:rgba(148,163,184,.12); }
.abs-cell.zone { background:rgba(34,197,94,.25); }
.abs-cell.point { background:#fbbf24; box-shadow:0 0 7px #fbbf24; border-radius:50%; }
.abs-cell.challenge { outline:1px solid #f87171; }
#absCall { display:block; text-align:center; color:#fbbf24; min-height:14px; }
.setting-row { display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:6px; }
.setting-label { color:#cbd5e1; font-size:12px; font-weight:700; margin:0 3px; }
.pitch-info { display:flex; align-items:center; justify-content:center; min-height:34px; border:1px solid #334155; border-radius:8px; background:#0f172a; color:#fbbf24; font-weight:800; font-size:13px; letter-spacing:.04em; }
.top-summaries { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
.summary-card { min-width:0; border:1px solid #334155; border-radius:9px; background:#0f172a; padding:8px 10px; color:#e2e8f0; font-size:11px; }
.summary-card b { display:block; font-size:12px; margin-bottom:3px; }
.lineup-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:5px; width:min(100%,440px); max-height:230px; overflow:auto; padding:4px; }
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
@media (max-width:480px) { #gameHud { width:min(190px,58%); right:6px; bottom:46px; padding:5px; gap:4px; } #gameHud #pitchInfo { font-size:10px; } }
</style>
</head>
<body>

<main class="w-full max-w-4xl flex flex-col gap-2">
  <header class="flex items-center justify-between bg-slate-900 border border-slate-800 rounded-xl px-3 py-2 shadow-lg text-xs md:text-sm">
    <b class="font-bold text-slate-200">⚾ 컴투스아마추어야구2026</b>
    <div class="flex items-center gap-2"><span id="pitcherName" class="font-bold text-slate-200">ACE 류현진</span><button id="changePitcherBtn" class="bg-slate-700 px-2 py-1 rounded text-white border border-slate-500">투수 교체</button></div>
  </header>

  <section class="top-summaries">
    <div class="summary-card"><b id="batterSideLabel" class="text-amber-400">내 타자</b><div id="batterSummary">1번 타자 · AVG — · OPS —</div></div>
    <div class="summary-card"><b id="pitcherSideLabel" class="text-sky-400">상대 투수</b><div id="pitcherSummaryTop">상대 선발 · ERA — · K 0 · WHIP —</div></div>
  </section>

  <!-- 3D 캔버스 영역 -->
  <div id="stage">
    <div id="dia">
      <i class="bs" style="left:20px;top:2px"></i>
      <i class="bs" style="left:38px;top:20px"></i>
      <i class="bs" style="left:2px;top:20px"></i>
    </div>

    <div id="msg"></div>
    <div id="absPanel"><b>ABS 존 · 최근 투구</b><div id="absGrid"></div><span id="absCall">아직 투구 기록 없음</span><button id="challengeBtn" class="stadium-choice" style="display:none;width:100%;margin-top:4px;padding:5px" disabled>⚖️ 챌린지 (2)</button></div>

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
      <div class="hud-pitcher"><span class="text-slate-400">투수</span><b id="pitcherStats" class="text-amber-300">구속 A | 변화구 A</b></div>
    </section>

    <!-- 타이밍 게이지 바 -->
    <div id="timingWrap">
      <div id="timingTarget"></div>
      <div id="timingPerfect"></div>
      <div id="timingCursor"></div>
    </div>
    <div id="timingHint"></div>

    <!-- 시작 및 결과 오버레이 -->
    <div id="ov">
      <h2 id="ovT" class="font-title text-3xl md:text-5xl text-amber-400 drop-shadow">컴투스아마추어야구2026</h2>
      <p id="ovP" class="text-sm md:text-base text-slate-300 max-w-md text-center leading-relaxed">
        경기 전에 구장을 고르세요. 돔구장과 야외 구장이 준비되어 있습니다.<br>
        선택한 이닝 동안 공격과 수비를 번갈아 플레이합니다. 난이도와 이닝도 여기서 고를 수 있습니다.
      </p>
      <div class="flex flex-wrap justify-center gap-2 mt-1" id="stadiumChoices">
        <button class="stadium-choice on" data-stadium="0">🌙 야간 클래식</button>
        <button class="stadium-choice" data-stadium="1">🏟️ 돔구장</button>
        <button class="stadium-choice" data-stadium="2">🌊 해안 구장</button>
        <button class="stadium-choice" data-stadium="3">🌿 그린 파크</button>
      </div>
      <div class="setting-row" id="difficultyChoices">
        <span class="setting-label">난이도</span>
        <button class="stadium-choice" data-difficulty="easy">쉬움</button>
        <button class="stadium-choice on" data-difficulty="normal">보통</button>
        <button class="stadium-choice" data-difficulty="hard">어려움</button>
      </div>
      <div class="setting-row" id="inningChoices">
        <span class="setting-label">이닝</span>
        <button class="stadium-choice on" data-innings="3">3이닝</button>
        <button class="stadium-choice" data-innings="5">5이닝</button>
        <button class="stadium-choice" data-innings="9">9이닝</button>
      </div>
      <div class="setting-row" id="batterSideChoices">
        <span class="setting-label">타석 방향</span>
        <button class="stadium-choice on" data-batside="R">우타</button>
        <button class="stadium-choice" data-batside="L">좌타</button>
      </div>
      <div class="text-xs text-slate-300 mt-1">타자 능력치(주력·파워·컨택)는 경기 시작 때 무작위 배정됩니다.</div>
      <div class="lineup-grid" id="lineupInputs"></div>
      <div class="team-name-inputs">
        <label>내 팀 이름<input id="ownTeamName" maxlength="12" value="우리 팀"></label>
        <label>상대 팀 이름<input id="opponentTeamName" maxlength="12" value="상대 팀"></label>
      </div>
      <div class="flex gap-3 mt-2">
        <button id="go" class="btn-action px-6 py-3 text-base">공격(타자)부터 시작</button>
        <button id="go2" class="btn-action px-6 py-3 text-base" style="background: linear-gradient(135deg, #38bdf8, #0284c7); color:white;">수비(투수)부터 시작</button>
      </div>
    </div>
  </div>

  <!-- 수비 투구구종 선택 패널 -->
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

  <!-- 모바일 메인 컨트롤 액션 바 -->
  <div class="grid grid-cols-3 gap-2 mt-1">
    <button id="mobileAct" class="col-span-2 btn-action py-3.5 text-lg font-title tracking-wider shadow-lg">스윙!</button>
    <button id="mobileSteal" class="bg-indigo-600 hover:bg-indigo-500 active:bg-indigo-700 text-white font-bold rounded-lg py-3 text-sm flex items-center justify-center gap-1 shadow-lg disabled:opacity-40" disabled>
      🏃 질주
    </button>
    <button id="buntBtn" class="col-span-3 stadium-choice py-2">번트 대기</button>
    <button id="pciBtn" class="col-span-3 stadium-choice py-2" hidden>🎯 조준 원: OFF (Shift)</button>
  </div>

  <!-- 조작 안내 -->
  <p class="text-xs text-slate-400 text-center mt-1">
    📱 모바일: 질주 버튼으로 도루·주루·태그업·호수비를, 조준 원 버튼으로 타격 조준을 하세요.<br>
    💻 PC: [스페이스바] 타격/일반 투구, 타격 Shift 조준 원 켜기/끄기, 투구 Shift 홀드 후 릴리스, [B] 번트, [S] 질주.
  </p>
  <section id="statsPanel" class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
    <div class="bg-slate-900 border border-slate-700 rounded-lg p-2"><b class="text-amber-400">내 타자 전체 기록</b><div id="batterStats" class="text-slate-200 mt-1">AVG — · OBP — · SLG — · OPS —<br>득점 0 · 타점 0</div></div>
    <div class="bg-slate-900 border border-slate-700 rounded-lg p-2"><b class="text-sky-400">내 투수 전체 기록</b><div id="pitcherGameStats" class="text-slate-200 mt-1">ERA — · K 0 · BB 0 · WHIP — · HBP 0</div></div>
  </section>
</main>

<!-- 투수 교체 모달 -->
<div id="pitcherModal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4" hidden style="display: none;">
  <div class="bg-slate-900 border border-slate-700 rounded-xl p-5 max-w-sm w-full shadow-2xl">
    <h3 class="font-title text-xl text-amber-400 mb-3">투수 교체</h3>
    <div id="pitcherList" class="flex flex-col gap-2 mb-4 max-h-60 overflow-y-auto"></div>
    <button id="closePitcherModal" type="button" class="w-full bg-slate-800 text-slate-300 py-2.5 rounded-lg font-bold border border-slate-700 active:bg-slate-700">닫기</button>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(() => {
const $ = id => document.getElementById(id);
$('lineupInputs').innerHTML = Array.from({ length: 9 }, (_, i) => `
  <div class="lineup-card"><label>${i + 1}번 타자<input id="lineupName${i}" maxlength="12" value="${i + 1}번 타자"></label></div>`).join('');
const R = (a, b) => a + Math.random() * (b - a);
const C = (v, a, b) => Math.max(a, Math.min(b, v));

if (!window.THREE) {
  $('ovP').textContent = '3D 라이브러리를 불러오지 못했습니다. 네트워크를 확인하세요.';
  return;
}

/* ---------- 로스터 / 투수 스탯 데이터 ---------- */
const PITCHERS = [
  { id: 0, title: 'MONSTER', name: '류현진', form: 'over', formName: '오버핸드', releaseX: 0.24, releaseY: 1.92, speed: 1.15, break: 1.2, ctrl: 0.03, endurance: 1.12, pitches: [0,2,3,4], desc: '높은 릴리스 · 구속 A · 변화 A · 제구 A · 체력 A' },
  { id: 1, title: '뱀직구', name: '임창용', form: 'side', formName: '사이드암', releaseX: 0.52, releaseY: 1.48, speed: 1.05, break: 1.45, ctrl: 0.04, endurance: 0.94, pitches: [0,1,2,5], desc: '사이드암 · 구속 B · 변화 A · 제구 B · 체력 B' },
  { id: 2, title: 'KOREAN RIVERA', name: '고우석', form: 'under', formName: '언더핸드', releaseX: 0.12, releaseY: 1.02, speed: 1.25, break: 0.85, ctrl: 0.06, endurance: 0.86, pitches: [1,4,6], desc: '언더핸드 · 구속 S · 변화 B · 제구 C · 체력 C' },
  { id: 3, title: 'THE ORAL', name: '김광현', form: 'threeQuarter', formName: '쓰리쿼터', releaseX: 0.39, releaseY: 1.7, speed: 1.0, break: 1.3, ctrl: 0.035, endurance: 1.04, pitches: [0,2,3,5], desc: '쓰리쿼터 · 구속 B · 변화 A · 제구 A · 체력 B' },
  { id: 4, title: '고퀄스', name: '고영표', form: 'side', formName: '사이드암', releaseX: 0.48, releaseY: 1.36, speed: 0.98, break: 1.55, ctrl: 0.028, endurance: 1.18, pitches: [0,1,4,6], desc: '사이드암 · 구속 B · 변화 S · 제구 S · 체력 S' },
  { id: 5, title: 'KOREAN SASAKI', name: '문동주', form: 'over', formName: '오버핸드', releaseX: 0.18, releaseY: 2.04, speed: 1.3, break: 0.9, ctrl: 0.052, endurance: 0.82, pitches: [0,1,2,3], desc: '오버핸드 · 구속 S · 변화 B · 제구 C · 체력 C' },
  { id: 6, title: '17MVP', name: '양현종', form: 'threeQuarter', formName: '쓰리쿼터', releaseX: 0.42, releaseY: 1.62, speed: 1.04, break: 1.25, ctrl: 0.032, endurance: 1.16, pitches: [0,2,3,4,5], desc: '쓰리쿼터 · 구속 B · 변화 A · 제구 A · 체력 S' },
  { id: 7, title: '궁내체고', name: '정대현', form: 'under', formName: '언더핸드', releaseX: 0.56, releaseY: 0.92, speed: 0.96, break: 1.6, ctrl: 0.04, endurance: 1.1, pitches: [1,4,5,6], desc: '잠수함 · 구속 B · 변화 S · 제구 B · 체력 A' }
];
let currentPitcherIdx = 0;
let pitcherStamina = 100;
let selectedStadium = 0;
let teamNames = ['우리 팀', '상대 팀'];
let difficulty = 'normal';
let maxInnings = 3;
let batterSide = 'R';
let battingMode = 'normal';
let pciEnabled = false;
let pciInsideContact = false;
let pciOutsideContact = false;
let defensiveThrow = null;
const DIFFICULTIES = { easy: { label: '쉬움', pitchSpeed: 0.86, aiContact: 0.68, zoneRate: 0.52 }, normal: { label: '보통', pitchSpeed: 1, aiContact: 1, zoneRate: 0.6 }, hard: { label: '어려움', pitchSpeed: 1.14, aiContact: 1.24, zoneRate: 0.68 } };
const emptyBatterStats = () => ({ pa: 0, ab: 0, hits: 0, walks: 0, hbp: 0, totalBases: 0, runs: 0, rbi: 0 });
const emptyPitcherStats = () => ({ outs: 0, strikeouts: 0, walks: 0, hits: 0, hbp: 0, earnedRuns: 0 });
let batterStats = emptyBatterStats();
let lineup = Array.from({ length: 9 }, (_, i) => ({ name: `${i + 1}번 타자`, stats: emptyBatterStats() }));
let battingOrderIndex = 0;
let batterPAComplete = false;
let pitcherStatsById = Object.fromEntries(PITCHERS.map(p => [p.id, emptyPitcherStats()]));
let opponentPitcherStats = emptyPitcherStats();
let opponentLineup = Array.from({ length: 9 }, (_, i) => ({ name: `상대 ${i + 1}번 타자`, stats: emptyBatterStats() }));
let opponentBatterIndex = 0;
let batterPAMode = null;
let challengeCount = 2;
let pendingABSCall = null;

/* ---------- 게임 상태 ---------- */
const CONTACT = 64, V3 = (x,y,z) => new THREE.Vector3(x,y,z);
const S = {
  phase: 'idle', mode: 'bat', pt: 0, fm: 'bat', h: 0,
  sc: [0, 0], outs: 0, balls: 0, strikes: 0, hits: 0, hr: 0,
  bases: [0, 0, 0]
};
let P = null, sw = null, hit = null, timer = 0, ac = null, last = performance.now();
let timingAnimId = null;
let pitchCharge = null;

// 도루 관련 변수
let isStealing = false;
let stealSpeedBonus = 0;
let activeStealRunner = null;
let stealRace = null;
let stealTimer = 0;
let batterRace = null;
let pendingFieldingPlay = null;
let buntMode = false;

/* ---------- Three.js 3D 그래픽 설정 ---------- */
const stage = $('stage');
const ren = new THREE.WebGLRenderer({ antialias: true });
ren.setPixelRatio(Math.min(devicePixelRatio, 2));
ren.shadowMap.enabled = true;
stage.prepend(ren.domElement);

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x07101c);
scene.fog = new THREE.Fog(0x07101c, 80, 320);

const cam = new THREE.PerspectiveCamera(52, 1, 0.3, 600);
const camPos = V3(0.7, 2, 5.4);
const DEF = V3(0, 1.1, -9);
const look = DEF.clone(), lookT = DEF.clone();
cam.position.copy(camPos);

function rs() {
  const w = stage.clientWidth, h = stage.clientHeight;
  ren.setSize(w, h, false);
  cam.aspect = w / h;
  cam.updateProjectionMatrix();
}
addEventListener('resize', rs);
new ResizeObserver(rs).observe(stage);
rs();

// 조명
scene.add(new THREE.HemisphereLight(0xbcd0ff, 0x14301f, 0.7));
const sun = new THREE.DirectionalLight(0xfff0d0, 1.2);
sun.position.set(14, 30, 16);
sun.target.position.set(0, 0, -8);
sun.castShadow = true;
sun.shadow.mapSize.set(1024, 1024);
Object.assign(sun.shadow.camera, { left: -14, right: 14, top: 14, bottom: -14, near: 5, far: 80 });
scene.add(sun, sun.target);

/* 텍스처 및 필드 메시 생성 */
function tex(w, h, fn, rep) {
  const k = document.createElement('canvas'); k.width = w; k.height = h;
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
  g.fillStyle = '#2b6e45'; g.fillRect(0, 0, w, h);
  g.fillStyle = '#307a4c'; g.fillRect(0, 0, w, h / 2);
  for (let i = 0; i < 2000; i++) {
    g.fillStyle = 'rgba(0,0,0,' + R(0.02, 0.07) + ')';
    g.fillRect(R(0, w), R(0, h), 2, 2);
  }
}, [34, 34]);

const fieldMat = new THREE.MeshStandardMaterial({ map: grass, roughness: 1 });
flat(new THREE.PlaneGeometry(500, 500), fieldMat, 0, 0, -100);
const dirt = mat(0x8a5a3b, 1);
flat(new THREE.PlaneGeometry(33, 33), dirt, 0, 0.02, -19.4, Math.PI / 4);
flat(new THREE.PlaneGeometry(21, 21), new THREE.MeshStandardMaterial({ map: grass, roughness: 1 }), 0, 0.03, -19.4, Math.PI / 4);
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
plate.rotation.x = -Math.PI / 2; plate.position.set(0, 0.05, -0.1); scene.add(plate);

const zone = new THREE.LineLoop(
  new THREE.BufferGeometry().setFromPoints([V3(-0.22, 0.56, 0.1), V3(0.22, 0.56, 0.1), V3(0.22, 1.08, 0.1), V3(-0.22, 1.08, 0.1)]),
  new THREE.LineBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.6 })
);
scene.add(zone);

/* 외야/팬스 */
const TS = Math.PI * 1.5 - 1.05, TL = 2.1;
const wall = new THREE.Mesh(new THREE.CylinderGeometry(100, 100, 4, 72, 1, true, TS, TL), new THREE.MeshStandardMaterial({ color: 0x14402e, roughness: 0.8, side: THREE.DoubleSide }));
wall.position.y = 2; scene.add(wall);

// 관중석, 전광판, 조명탑과 돔 지붕으로 구장마다 분위기를 구분합니다.
const stands = new THREE.Mesh(new THREE.CylinderGeometry(119, 119, 16, 72, 1, true, TS, TL), new THREE.MeshStandardMaterial({ color: 0x26364c, roughness: 0.88, side: THREE.DoubleSide }));
stands.position.y = 8; scene.add(stands);
const crowdPositions = [], crowdColors = [], crowdPalette = [0xe2e8f0, 0xfbbf24, 0x38bdf8, 0xf87171, 0x34d399, 0xc4b5fd, 0xffffff];
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
crowd.frustumCulled = false; scene.add(crowd);
const upperDeck = new THREE.Mesh(new THREE.CylinderGeometry(128, 128, 2.5, 72, 1, true, TS, TL), new THREE.MeshStandardMaterial({ color: 0xe5e7eb, roughness: 0.8, side: THREE.DoubleSide }));
upperDeck.position.y = 16; scene.add(upperDeck);
const boardFrame = mk(new THREE.BoxGeometry(25, 7, 1.4), mat(0x111827, 0.6), 0, 12, -105, scene, false);
const boardFace = mk(new THREE.BoxGeometry(23, 5.4, 0.12), new THREE.MeshBasicMaterial({ color: 0x0f766e }), 0, 12, -104.2, scene, false);
const scoreTexture = tex(512, 128, (g, w, h) => { g.fillStyle = '#0f766e'; g.fillRect(0, 0, w, h); });
boardFace.material.map = scoreTexture; boardFace.material.color.setHex(0xffffff); boardFace.material.needsUpdate = true;
const stadiumLights = [];
[-1, 1].forEach(side => [-1, 1].forEach(depth => {
  const tower = new THREE.Group(); tower.position.set(side * 112, 0, depth * 72); scene.add(tower);
  mk(new THREE.CylinderGeometry(0.35, 0.65, 27, 8), mat(0x64748b), 0, 13.5, 0, tower, false);
  const lamps = mk(new THREE.BoxGeometry(7, 2, 1), new THREE.MeshBasicMaterial({ color: 0xfff7d6 }), 0, 27.2, 0, tower, false);
  stadiumLights.push(lamps);
}));
const DOME_RADIUS = 112, DOME_Y = -42, DOME_Z = -25;
const dome = new THREE.Mesh(new THREE.SphereGeometry(DOME_RADIUS, 64, 32, 0, Math.PI * 2, 0, Math.PI / 2), new THREE.MeshBasicMaterial({ color: 0x9bd6ef, transparent: true, opacity: 0.5, side: THREE.DoubleSide, depthWrite: false }));
dome.position.set(0, DOME_Y, DOME_Z); dome.visible = false; scene.add(dome);
const domeRibs = new THREE.Group(); domeRibs.visible = false; scene.add(domeRibs);
const domeRibMat = new THREE.LineBasicMaterial({ color: 0xdaf4ff, transparent: true, opacity: 0.62 });
for (let longitude = 0; longitude < 12; longitude++) {
  const phi = longitude / 12 * Math.PI * 2, points = [];
  for (let step = 0; step <= 36; step++) {
    const theta = step / 36 * Math.PI / 2;
    points.push(V3(DOME_RADIUS * Math.sin(theta) * Math.cos(phi), DOME_Y + DOME_RADIUS * Math.cos(theta), DOME_Z + DOME_RADIUS * Math.sin(theta) * Math.sin(phi)));
  }
  domeRibs.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(points), domeRibMat));
}
for (const theta of [0.28, 0.55, 0.82, 1.1, 1.36]) {
  const points = [];
  for (let step = 0; step <= 96; step++) {
    const phi = step / 96 * Math.PI * 2;
    points.push(V3(DOME_RADIUS * Math.sin(theta) * Math.cos(phi), DOME_Y + DOME_RADIUS * Math.cos(theta), DOME_Z + DOME_RADIUS * Math.sin(theta) * Math.sin(phi)));
  }
  domeRibs.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(points), domeRibMat));
}
const STADIUMS = [
  { name: '야간 클래식', sky: 0x07101c, fog: 0x07101c, seats: 0x24364b, wall: 0x14402e, grass: 0xffffff, dome: false, board: 0x0f766e },
  { name: '돔구장', sky: 0x182b3b, fog: 0x182b3b, seats: 0x334155, wall: 0x155e63, grass: 0xe7f1ea, dome: true, board: 0x1d4ed8 },
  { name: '해안 구장', sky: 0x164e63, fog: 0x164e63, seats: 0x0e7490, wall: 0x0f766e, grass: 0xe1f0ff, dome: false, board: 0x0284c7 },
  { name: '그린 파크', sky: 0x183b2b, fog: 0x183b2b, seats: 0x36533b, wall: 0x2f6b3f, grass: 0xf1f7e8, dome: false, board: 0x3f6212 }
];
function applyStadium(index) {
  selectedStadium = index;
  const stadium = STADIUMS[index];
  scene.background.setHex(stadium.sky); scene.fog.color.setHex(stadium.fog);
  stands.material.color.setHex(stadium.seats); wall.material.color.setHex(stadium.wall);
  fieldMat.color.setHex(stadium.grass); boardFace.material.color.setHex(0xffffff);
  dome.visible = stadium.dome;
  domeRibs.visible = stadium.dome;
  stadiumLights.forEach(light => light.material.color.setHex(index === 1 ? 0xdbeafe : 0xfff7d6));
  document.querySelectorAll('#stadiumChoices .stadium-choice').forEach((button, i) => button.classList.toggle('on', i === index));
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
  g.font = 'bold 32px sans-serif'; g.textAlign = 'center';
  g.fillText(`${S.sc[0]}  :  ${S.sc[1]}`, w / 2, 94);
  g.font = 'bold 19px sans-serif'; g.textAlign = 'right';
  g.fillText(`${Math.min((S.h >> 1) + 1, maxInnings)}회 ${S.h % 2 ? '말' : '초'}   O ${S.outs}`, w - 22, 113);
  scoreTexture.needsUpdate = true;
}
applyStadium(0);

/* ---------- 선수 및 공 ---------- */
function figure(shirt, cap, x, z) {
  const g = new THREE.Group(), m1 = mat(shirt);
  mk(new THREE.CylinderGeometry(0.09, 0.08, 0.85, 8), mat(0xdddddd), -0.1, 0.43, 0, g);
  mk(new THREE.CylinderGeometry(0.09, 0.08, 0.85, 8), mat(0xdddddd), 0.1, 0.43, 0, g);
  mk(new THREE.CylinderGeometry(0.2, 0.17, 0.62, 10), m1, 0, 1.15, 0, g);
  mk(new THREE.SphereGeometry(0.13, 12, 10), mat(0xe8c9a0), 0, 1.6, 0, g);
  mk(new THREE.SphereGeometry(0.14, 12, 8, 0, Math.PI * 2, 0, Math.PI / 2), mat(cap), 0, 1.62, 0, g);
  g.position.set(x, 0, z); scene.add(g); return g;
}
const SPDF = 5.8, B1 = V3(19.4, 0, -19.4), B1T = V3(19.4, 1.2, -19.4), MT = V3(0, 1.2, -18.4), B2T = V3(0, 1.2, -38.8), B2P = V3(0, 0, -38.8);
const F = [[17, -20], [7, -31], [-7, -31], [-17, -20], [-40, -62], [0, -76], [40, -62]].map(([x, z]) => {
  const g = figure(0xcfd6e0, 0xb02020, x, z); g.rotation.y = Math.atan2(-x, 5 - z);
  return { g, home: V3(x, 0, z) };
});
function resetField() {
  F.forEach(f => { f.g.position.copy(f.home); f.g.rotation.y = Math.atan2(-f.home.x, 5 - f.home.z); });
}
const BP = [V3(0, 0, 0.6), V3(19.4, 0, -19.4), V3(0, 0, -38.8), V3(-19.4, 0, -19.4), V3(0, 0, 0.6)];
const pool = [...Array(8)].map(() => {
  const g = figure(0xf0f0f0, 0x1b2a5c, 0, 0); g.visible = false;
  return { g, on: false, b: 0, to: 0, t0: 0, sp: 16, out: false, h: 0 };
});
let occ = [null, null, null, null];

const pit = figure(0xffffff, 0x1b2a5c, 0, -18.4); pit.position.y = 0.28; pit.rotation.y = Math.PI;
const arm = new THREE.Group(); arm.position.set(0.24, 2, -18.4); scene.add(arm);
mk(new THREE.CylinderGeometry(0.05, 0.045, 0.62, 8), mat(0xffffff), 0, -0.31, 0, arm);
const catcher = figure(0x24385f, 0x1b2a5c, 0, 0.9);
catcher.scale.set(0.92, 0.72, 0.92); catcher.position.y = 0.08;
const catcherMask = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(0.32, 0.25, 0.12)), new THREE.LineBasicMaterial({ color: 0xd1d5db }));
catcherMask.position.set(0, 1.45, 0.11); catcher.add(catcherMask);
mk(new THREE.SphereGeometry(0.13, 10, 8), mat(0xdbeafe), 0.3, 0.96, 0.2, catcher);

const bt = new THREE.Group(); scene.add(bt); bt.scale.x = batterSide === 'L' ? -1 : 1;
const batterLegs = [-0.1, 0.1].map((dx, i) => {
  const leg = new THREE.Group(); leg.position.set(-0.95 + dx, 0.82, 0.1); bt.add(leg);
  mk(new THREE.CylinderGeometry(0.09, 0.08, 0.85, 8), mat(0xdddddd), 0, -0.39, 0, leg);
  return leg;
});
const up = new THREE.Group(); up.position.set(-0.95, 0.85, 0.1); bt.add(up);
mk(new THREE.CylinderGeometry(0.2, 0.17, 0.62, 10), mat(0xf0f0f0), 0, 0.3, 0, up);
mk(new THREE.SphereGeometry(0.13, 12, 10), mat(0xe8c9a0), 0, 0.77, 0, up);
mk(new THREE.SphereGeometry(0.15, 12, 8, 0, Math.PI * 2, 0, Math.PI / 2), mat(0x1b2a5c), 0, 0.79, 0, up);
const swingArms = new THREE.Group(); swingArms.position.set(0, 0.375, 0); up.add(swingArms);
[-0.06, 0.06].forEach(dz => {
  const a = mk(new THREE.CylinderGeometry(0.045, 0.04, 0.42, 8), mat(0xf0f0f0), 0.22, 0, dz, swingArms);
  a.rotation.z = -2.54;
});
const BAT_READY = -0.72;
const bat = new THREE.Group(); bat.position.set(0.28, -0.025, -0.08); bat.rotation.z = BAT_READY; swingArms.add(bat);
mk(new THREE.CylinderGeometry(0.05, 0.02, 1, 10), mat(0xc99a5b, 0.6), 0, 0.5, 0, bat);

/* 야구공 */
const seam = tex(128, 64, (g, w, h) => {
  g.fillStyle = '#f4f4ee'; g.fillRect(0, 0, w, h); g.strokeStyle = '#c0392b'; g.lineWidth = 3;
  [32, 96].forEach(x => {
    g.beginPath(); g.arc(x + (x < 64 ? -26 : 26), 32, 28, x < 64 ? -0.9 : Math.PI - 0.9, x < 64 ? 0.9 : Math.PI + 0.9); g.stroke();
  });
});
const ball = new THREE.Mesh(new THREE.SphereGeometry(0.13, 16, 12), new THREE.MeshStandardMaterial({ map: seam, roughness: 0.6 }));
ball.castShadow = true; ball.visible = false; scene.add(ball);
const shd = new THREE.Mesh(new THREE.CircleGeometry(0.14, 16), new THREE.MeshBasicMaterial({ color: 0, transparent: true, opacity: 0.45, depthWrite: false }));
shd.rotation.x = -Math.PI / 2; shd.visible = false; scene.add(shd);

/* 구종 정의 */
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
pciRing.visible = false; pciRing.renderOrder = 10; scene.add(pciRing);

function aimAt(e) {
  const r = stage.getBoundingClientRect();
  mv.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
  rc.setFromCamera(mv, cam);
  const h = V3(0, 0, 0);
  if (rc.ray.intersectPlane(pln, h)) {
    aim.x = C(h.x, -0.5, 0.5);
    aim.y = C(h.y, 0.3, 1.4);
  }
}

function setPT(i) {
  if (!PITCHERS[currentPitcherIdx].pitches.includes(i)) return;
  S.pt = i;
  refreshPitchButtons();
}

function refreshPitchButtons() {
  const allowed = PITCHERS[currentPitcherIdx].pitches;
  if (!allowed.includes(S.pt)) S.pt = allowed[0];
  document.querySelectorAll('#types button').forEach((button, i) => {
    button.hidden = !allowed.includes(i);
    button.classList.toggle('on', S.pt === i);
  });
}

function zoneCall(tx, ty) {
  // ABS 표시의 3x3 중앙 셀(±0.9)과 실제 판정 존을 동일하게 맞춥니다.
  const actual = Math.abs(tx) <= 0.9 && Math.abs(ty) <= 0.9;
  const edge = Math.min(Math.abs(Math.abs(tx) - 0.9), Math.abs(Math.abs(ty) - 0.9));
  const challengeable = edge <= 0.22;
  const wrong = challengeable && Math.random() < 0.24;
  return { actual, called: wrong ? !actual : actual, challengeable, wrong };
}

function initABSGrid() {
  const grid = $('absGrid');
  if (grid.childElementCount) return;
  for (let row = 0; row < 5; row++) for (let col = 0; col < 5; col++) {
    const cell = document.createElement('i');
    cell.className = 'abs-cell' + (row >= 1 && row <= 3 && col >= 1 && col <= 3 ? ' zone' : '');
    grid.appendChild(cell);
  }
}

function updateABS(tx, ty, callText, wrong = false) {
  initABSGrid();
  const col = C(Math.floor((tx + 1.5) / 3 * 5), 0, 4);
  const row = 4 - C(Math.floor((ty + 1.5) / 3 * 5), 0, 4);
  const cell = row * 5 + col;
  document.querySelectorAll('.abs-cell').forEach((el, i) => {
    el.classList.toggle('point', i === cell);
    el.classList.toggle('challenge', i === cell && wrong);
  });
  $('absCall').textContent = callText;
}

function updatePitchInfo(pitchData) {
  if (!pitchData) return;
  const kind = TYPES[S.pt], pitcher = PITCHERS[currentPitcherIdx];
  $('pitchInfo').textContent = `⚾ ${kind.name} · ${pitchData.speedKmh} km/h · ${pitcher.formName} · ${batterSide === 'R' ? '우타' : '좌타'}`;
}

function challengeABS() {
  if (!pendingABSCall || challengeCount <= 0 || performance.now() > pendingABSCall.expires) return;
  const call = pendingABSCall;
  pendingABSCall = null; challengeCount--;
  if (call.called === 'strike') { S.strikes = Math.max(0, S.strikes - 1); S.balls++; }
  else { S.balls = Math.max(0, S.balls - 1); S.strikes++; }
  updateABS(P.tx, P.ty, `챌린지 성공 · ${call.actual === 'strike' ? '스트라이크' : '볼'}`, false);
  flash('판정 번복!', `ABS 챌린지 성공 · 남은 횟수 ${challengeCount}`);
  snd(880, 0.14, 'sine', 0.2, 1250);
  board();
}

function currentPitcherStats() { return pitcherStatsById[currentPitcherIdx]; }
function battingAverage() { return batterStats.ab ? batterStats.hits / batterStats.ab : 0; }
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
  const ownBatter = S.mode === 'bat';
  const bs = ownBatter ? batterStats : opponentLineup[opponentBatterIndex].stats;
  const ps = ownBatter ? opponentPitcherStats : currentPitcherStats();
  const avg = bs.ab ? bs.hits / bs.ab : 0;
  const obpDen = bs.ab + bs.walks + bs.hbp;
  const obp = obpDen ? (bs.hits + bs.walks + bs.hbp) / obpDen : 0;
  const slg = bs.ab ? bs.totalBases / bs.ab : 0;
  const ip = ps.outs / 3;
  const era = ip ? (ps.earnedRuns * 9 / ip).toFixed(2) : '—';
  const whip = ip ? ((ps.walks + ps.hits) / ip).toFixed(2) : '—';
  const teamBat = totalBatterStats(lineup), teamAvg = teamBat.ab ? teamBat.hits / teamBat.ab : 0;
  const teamOBPden = teamBat.ab + teamBat.walks + teamBat.hbp;
  const teamOBP = teamOBPden ? (teamBat.hits + teamBat.walks + teamBat.hbp) / teamOBPden : 0;
  const teamSLG = teamBat.ab ? teamBat.totalBases / teamBat.ab : 0;
  const teamPitch = totalPitcherStats(), teamIP = teamPitch.outs / 3;
  const teamERA = teamIP ? (teamPitch.earnedRuns * 9 / teamIP).toFixed(2) : '—';
  const teamWHIP = teamIP ? ((teamPitch.walks + teamPitch.hits) / teamIP).toFixed(2) : '—';
  $('batterStats').innerHTML = `AVG ${teamAvg.toFixed(3)} · OBP ${teamOBP.toFixed(3)} · SLG ${teamSLG.toFixed(3)} · OPS ${(teamOBP + teamSLG).toFixed(3)}<br>득점 ${teamBat.runs} · 타점 ${teamBat.rbi} · 안타 ${teamBat.hits} · BB ${teamBat.walks} · HBP ${teamBat.hbp}`;
  $('pitcherGameStats').textContent = `ERA ${teamERA} · K ${teamPitch.strikeouts} · BB ${teamPitch.walks} · WHIP ${teamWHIP} · 피안타 ${teamPitch.hits} · HBP ${teamPitch.hbp}`;
  const batterTop = $('batterSummary');
  $('batterSideLabel').textContent = ownBatter ? '내 타자 기록' : '상대 타자 기록';
  $('pitcherSideLabel').textContent = ownBatter ? '상대 투수 기록' : '내 투수 기록';
  const hitterAbilities = ownBatter ? lineup[battingOrderIndex] : null;
  const abilitySummary = hitterAbilities ? `<br>능력 · 주력 ${hitterAbilities.speed} · 파워 ${hitterAbilities.power} · 컨택 ${hitterAbilities.contact}` : '';
  if (batterTop) batterTop.innerHTML = `<strong>${ownBatter ? '내 타자' : '상대 타자'} · ${ownBatter ? battingOrderIndex + 1 : opponentBatterIndex + 1}번 ${ownBatter ? lineup[battingOrderIndex].name : opponentLineup[opponentBatterIndex].name}</strong><br>AVG ${avg.toFixed(3)} · OBP ${obp.toFixed(3)} · SLG ${slg.toFixed(3)} · OPS ${(obp + slg).toFixed(3)}<br>득점 ${bs.runs} · 타점 ${bs.rbi} · 안타 ${bs.hits}${abilitySummary}`;
  const pitcherTop = $('pitcherSummaryTop');
  if (pitcherTop) pitcherTop.innerHTML = `<strong>${ownBatter ? '상대 선발' : PITCHERS[currentPitcherIdx].name}</strong><br>ERA ${era} · K ${ps.strikeouts} · BB ${ps.walks} · WHIP ${whip} · 피안타 ${ps.hits} · HBP ${ps.hbp}`;
}

function recordBatterHit(bases) {
  const stats = S.mode === 'bat' ? batterStats : opponentLineup[opponentBatterIndex].stats;
  stats.pa++; stats.ab++; stats.hits++; stats.totalBases += bases;
  if (S.mode === 'bat') opponentPitcherStats.hits++;
  else currentPitcherStats().hits++;
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
  } else if (batterPAMode === 'pitch') opponentBatterIndex = (opponentBatterIndex + 1) % opponentLineup.length;
  batterPAComplete = false; batterPAMode = null;
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
  // path는 시뮬레이션 시간(초) 기준입니다. 렌더링 가속 배율을 다시 곱하면
  // 수비수가 외야 타구를 비현실적으로 멀리서 잡는 것으로 판정됩니다.
  const speed = SPDF * 1.5 * (buntPlay ? 0.38 : 1);
  for (let i = 12; i < Math.min(path.length, 210); i += 2) {
    const b = path[i], elapsed = i / 60;
    const air = b.y >= 1.1 && b.y <= 2.8;
    // 땅볼은 내야에서 초기에 수비수와 맞닿을 때만 처리합니다.
    const ground = b.y <= 0.25 && i <= 145 && Math.hypot(b.x, b.z) <= 38;
    if (!air && !ground) continue;
    let best = null;
    for (const f of F) {
      const q = f.g.position;
      const distance = Math.hypot(q.x - b.x, q.z - b.z);
      if (distance <= speed * elapsed + (air ? 1.0 : 1.3) && (!best || distance < best.distance)) best = { i, f, air, distance };
    }
    if (best) return best;
  }
  return null;
}

function deferForFielding(bases, t0, extraBase) {
  const target = hit && hit.fieldOpportunity;
  if (S.mode !== 'pitch' || !target) return false;
  const impactAt = hit.t + target.i / 60 / 1.7 * 1000;
  const play = { target, bases, t0, extraBase, impactAt, cueTimer: 0, settleTimer: 0 };
  pendingFieldingPlay = play;
  play.cueTimer = setTimeout(() => {
    if (pendingFieldingPlay === play) flash('질주 버튼!', '호수비 타이밍입니다. 여유 있게 버튼을 누르세요!');
    board();
  }, Math.max(0, impactAt - performance.now() - 850));
  play.settleTimer = setTimeout(() => resolveFieldingPlay(false), Math.max(0, impactAt - performance.now() + 950));
  return true;
}

function resolveFieldingPlay(saved) {
  const play = pendingFieldingPlay;
  if (!play) return;
  pendingFieldingPlay = null;
  clearTimeout(play.cueTimer); clearTimeout(play.settleTimer);
  if (saved) {
    const { f, i, air } = play.target;
    hit.fieldOpportunity = null;
    hit.plan = { f, i, air, out: false, cover: null, throwTo: null };
    f.g.scale.y = 1.18;
    setTimeout(() => { f.g.scale.y = 1; }, 520);
    recordBatterOut(); addOut(1); finishBatterPA();
    flash('호수비!', air ? '빠른 타구를 몸을 날려 잡았습니다!' : '내야 강습을 정확한 타이밍에 잡았습니다!');
    snd(880, 0.18, 'sine', 0.25, 1450);
  } else {
    hit.fieldOpportunity = null; hit.plan = null;
    hit.chase = play.target.f;
    recordBatterHit(play.bases); advance(play.bases, play.extraBase, play.t0); finishBatterPA();
    flash(play.bases === 2 ? '2루타!' : '안타!', '수비수가 잡지 못했습니다.');
  }
  board();
}

function attemptHighlightCatch() {
  const play = pendingFieldingPlay;
  if (!play || S.mode !== 'pitch') return false;
  const delta = performance.now() - play.impactAt;
  if (delta >= -850 && delta <= 950) { resolveFieldingPlay(true); return true; }
  return false;
}

function useSprintAction() {
  if (pendingFieldingPlay && S.mode === 'pitch') { attemptHighlightCatch(); return; }
  if (S.phase === 'running') sprintBatter();
  else attemptSteal();
}

/* ---------- 소리 효과 ---------- */
function snd(f, d, t, v, f2) {
  if (!ac) return;
  try {
    const T = ac.currentTime, o = ac.createOscillator(), g = ac.createGain();
    o.type = t; o.frequency.setValueAtTime(f, T);
    if (f2) o.frequency.exponentialRampToValueAtTime(f2, T + d);
    g.gain.setValueAtTime(v, T); g.gain.exponentialRampToValueAtTime(0.001, T + d);
    o.connect(g); g.connect(ac.destination);
    o.start(); o.stop(T + d);
  } catch(e){}
}

function hitSound() {
  // 짧은 타구음에 저음 임팩트를 겹쳐 배트에 맞는 느낌을 냅니다.
  snd(145, 0.16, 'triangle', 0.28, 52);
  setTimeout(() => snd(1250, 0.055, 'triangle', 0.12, 420), 8);
}

/* ---------- 로직 및 UI 업데이트 ---------- */
const dots = (n, m) => '●'.repeat(n) + '○'.repeat(m - n);

function addScore(amount) {
  if (S.mode === 'bat') {
    S.sc[0] += amount;
    batterStats.rbi += amount; opponentPitcherStats.earnedRuns += amount;
  } else {
    S.sc[1] += amount;
    opponentLineup[opponentBatterIndex].stats.rbi += amount;
    if (S.mode === 'pitch') currentPitcherStats().earnedRuns += amount;
  }
}

function board() {
  $('mobileAct').textContent = S.mode === 'pitch' ? '투구!' : S.phase === 'aim' ? '타격 준비' : S.phase === 'running' ? '주루 중…' : '스윙!';
  $('mobileSteal').textContent = '🏃 질주';
  $('buntBtn').textContent = buntMode ? '번트 대기 중 · 취소' : '번트 대기';
  $('buntBtn').classList.toggle('on', buntMode);
  $('buntBtn').disabled = S.mode !== 'bat' || S.phase === 'running';
  $('battingModeChoices').style.display = S.mode === 'bat' ? 'flex' : 'none';
  document.querySelectorAll('#battingModeChoices [data-batting-mode]').forEach(button => button.classList.toggle('on', button.dataset.battingMode === battingMode));
  $('pciBtn').hidden = S.mode !== 'bat';
  $('pciBtn').disabled = S.phase === 'running';
  $('pciBtn').textContent = `🎯 조준 원: ${pciEnabled ? 'ON' : 'OFF'} (Shift)`;
  $('inn').textContent = (Math.min(S.h >> 1, maxInnings - 1) + 1) + '회 ' + (S.h % 2 ? '말' : '초') + (S.mode === 'bat' ? ' 공격' : ' 수비');
  $('score').textContent = S.sc[0] + ' : ' + S.sc[1];
  $('scoreTeams').textContent = `${teamNames[0].slice(0, 8)} : ${teamNames[1].slice(0, 8)}`;
  $('b').textContent = dots(S.balls, 3);
  $('s').textContent = dots(S.strikes, 2);
  $('o').textContent = dots(S.outs, 2);
  document.querySelectorAll('.bs').forEach((e, i) => e.classList.toggle('on', !!S.bases[[1, 0, 2][i]]));

  const canSprint = (S.mode === 'bat' && ((S.bases[0] || S.bases[1]) && (S.phase === 'aim' || S.phase === 'wait') || S.phase === 'running' && !!batterRace)) || (S.mode === 'pitch' && !!pendingFieldingPlay);
  $('mobileSteal').disabled = !canSprint;
  const challengeButton = $('challengeBtn');
  challengeButton.style.display = pendingABSCall ? 'block' : 'none';
  challengeButton.disabled = !pendingABSCall || challengeCount <= 0;
  challengeButton.textContent = `⚖️ ABS 판정 번복 (${challengeCount})`;
  refreshPitchButtons();
  updateStatsUI();
  updatePitcherUI();
  drawScoreboard();
}

function flash(t, sub) {
  const m = $('msg'); m.innerHTML = '';
  const a = document.createElement('b'), s = document.createElement('span');
  a.textContent = t; s.textContent = sub || '';
  m.append(a, s);
  m.classList.remove('on'); void m.offsetWidth; m.classList.add('on');
}

function overlay(t, p, b) {
  $('ovT').textContent = t; $('ovP').textContent = p; $('ov').hidden = false;
}

function newRunner(t0, sp) {
  const q = pool.find(x => !x.on) || pool[0];
  const batterIndex = S.mode === 'bat' ? battingOrderIndex : opponentBatterIndex;
  const rating = S.mode === 'bat' ? (lineup[batterIndex]?.speed || 3) : 3;
  Object.assign(q, { on: true, b: 0, to: 0, out: false, h: 0, t0, sp: sp * (0.84 + rating * 0.04), speedRating: rating, batterIndex, batterSide: S.mode });
  q.g.visible = true; q.g.position.copy(BP[0]); return q;
}
function runnerSpeed(runner, baseSpeed) { return baseSpeed * (0.84 + (runner?.speedRating || 3) * 0.04); }
function recordRunnerScore(r) {
  if (!Number.isInteger(r?.batterIndex)) return;
  const players = r.batterSide === 'bat' ? lineup : opponentLineup;
  players[r.batterIndex].stats.runs++;
}
function setOcc(no) { occ = no; S.bases = [no[1] ? 1 : 0, no[2] ? 1 : 0, no[3] ? 1 : 0]; }
function clearRun() { batterRace = null; pool.forEach(q => { q.on = false; q.g.visible = false; }); setOcc([null, null, null, null]); }

function advance(n, ex, t0) {
  const no = [null, null, null, null], sp = n >= 4 ? 28 : 16;
  for (let i = 3; i >= 1; i--) {
    const r = occ[i]; if (!r) continue;
    const t = Math.min(4, i + n + ex); r.to = t; r.t0 = t0; r.sp = runnerSpeed(r, sp);
    if (t >= 4) { recordRunnerScore(r); addScore(1); } else no[t] = r;
  }
  const b = newRunner(t0, sp); b.to = Math.min(n, 4);
  if (n >= 4) { recordRunnerScore(b); addScore(1); } else no[n] = b;
  setOcc(no); S.balls = S.strikes = 0;
  if (S.mode === 'bat') S.hits++;
}

function advanceRunnersOnBunt(t0) {
  const no = [null, null, null, null];
  for (let base = 3; base >= 1; base--) {
    const runner = occ[base];
    if (!runner) continue;
    runner.to = base + 1; runner.t0 = t0; runner.sp = runnerSpeed(runner, 13);
    if (base === 3) { recordRunnerScore(runner); addScore(1); }
    else no[base + 1] = runner;
  }
  setOcc(no);
}

function walk(t0) {
  const r = occ, no = [null, null, null, null], mv = (x, to) => { x.to = to; x.t0 = t0; x.sp = runnerSpeed(x, 16); };
  if (r[1]) {
    if (r[2]) { if (r[3]) { mv(r[3], 4); recordRunnerScore(r[3]); addScore(1); } mv(r[2], 3); no[3] = r[2]; } else no[3] = r[3];
    mv(r[1], 2); no[2] = r[1];
  } else { no[2] = r[2]; no[3] = r[3]; }
  const b = newRunner(t0, 16); b.to = 1; no[1] = b; setOcc(no); S.balls = S.strikes = 0;
}

function changeSide() {
  S.outs = 0; clearRun(); buntMode = false; S.h++; S.mode = S.mode === 'bat' ? 'pitch' : 'bat';
  const hm = S.fm === 'bat' ? 1 : 0;
  if (S.h === 2 * maxInnings - 1 && S.sc[hm] > S.sc[1 - hm]) S.h = 2 * maxInnings;
  $('types').hidden = S.mode !== 'pitch' || S.h >= 2 * maxInnings;
}

function addOut(n) { S.outs += n; S.balls = S.strikes = 0; if (S.mode === 'pitch') currentPitcherStats().outs += n; else if (S.mode === 'bat') opponentPitcherStats.outs += n; if (S.outs >= 3) changeSide(); }

function beginBatterRace(t0) {
  const runner = newRunner(t0, 9.5);
  runner.to = 1;
  for (let base = 3; base >= 2; base--) {
    const other = occ[base];
    if (!other) continue;
    const target = base + 1;
    other.to = target; other.t0 = t0; other.sp = runnerSpeed(other, 16);
    occ[base] = null;
    if (target >= 4) addScore(1); else occ[target] = other;
  }
  setOcc(occ);
  const play = hit.plan;
  const raceTime = play.i / (60 * 1.7) + play.throwDuration / 1.7 + 0.2;
  batterRace = { runner, callAt: t0 + raceTime * 1000 };
  S.phase = 'running';
}

function beginBuntRace(t0) {
  const advanced = [null, null, null, null];
  for (let base = 3; base >= 1; base--) {
    const runner = occ[base];
    if (!runner) continue;
    const target = base + 1;
    runner.to = target; runner.t0 = t0; runner.sp = runnerSpeed(runner, 13);
    if (target >= 4) { recordRunnerScore(runner); addScore(1); }
    else advanced[target] = runner;
  }
  setOcc(advanced);
  const runner = newRunner(t0, 9.5); runner.to = 1;
  const play = hit.plan;
  const raceTime = play.i / (60 * 1.7) + play.throwDuration / 1.7 + 0.2;
  batterRace = { kind: 'first', runner, callAt: t0 + raceTime * 1000 };
  S.phase = 'running';
}

function beginSacFlyRace(t0) {
  const runner = occ[3];
  if (!runner) return false;
  occ[3] = null; setOcc(occ);
  const play = hit?.plan;
  const catchAt = t0 + (play ? play.i / 60 / 1.7 * 1000 : 450);
  const from = (play && hit.path[play.i] ? hit.path[play.i] : runner.g.position).clone();
  from.y = 1.35;
  const to = BP[0].clone(); to.y = 1.25;
  const throwDuration = 2200;
  defensiveThrow = { from, to, start: catchAt, duration: throwDuration, thrower: 'fielder', targetBase: 0 };
  runner.to = 4; runner.t0 = catchAt; runner.sp = runnerSpeed(runner, 10);
  batterRace = { kind: 'sacfly', runner, callAt: catchAt + throwDuration, hitterIndex: battingOrderIndex };
  S.phase = 'running';
  flash('희생플라이 승부!', '3루 주자가 홈으로 뜁니다. 송구 전에 연타하세요!');
  return true;
}

function sprintBatter() {
  if (S.phase !== 'running' || !batterRace) return;
  const runner = batterRace.runner;
  runner.sp = Math.min(23, runner.sp + 1.6);
  snd(500 + runner.sp * 25, 0.045, 'triangle', 0.13);
}

function settleBatterRace(now) {
  if (!batterRace) return;
  const race = batterRace, runner = race.runner;
  if (race.kind === 'sacfly') {
    const safe = runner.b >= 4 || runner.g.position.distanceTo(BP[4]) <= 0.5;
    batterRace = null; runner.sp = 0; runner.to = safe ? 4 : runner.b;
    if (safe) {
      runner.b = 4; recordRunnerScore(runner); addScore(1); runner.on = false; runner.g.visible = false;
      flash('세이프! 득점!', '홈 송구보다 주자가 먼저 도착했습니다.');
      snd(820, 0.18, 'sine', 0.24, 1250);
    } else {
      runner.out = true; runner.on = false; runner.g.visible = false; addOut(1);
      flash('홈에서 아웃!', '포수의 태그가 먼저 들어왔습니다.');
      snd(190, 0.2, 'sawtooth', 0.22, 75);
    }
    finishBatterPA(); S.phase = 'result'; board(); return;
  }
  const safe = runner.b >= 1 || runner.g.position.distanceTo(BP[1]) <= 0.9;
  batterRace = null;
  runner.to = safe ? 1 : runner.b;
  runner.b = safe ? 1 : runner.b;
  runner.sp = 0;
  if (safe) {
    runner.g.position.copy(BP[1]);
    occ[1] = runner; setOcc(occ); S.hits++;
    recordBatterHit(1);
    flash('세이프!', '타자 주자가 송구보다 먼저 1루에 도착했습니다.');
    snd(760, 0.16, 'sine', 0.22, 1120);
  } else {
    runner.out = true;
    recordBatterOut();
    flash('아웃!', '송구가 먼저 1루에 도착했습니다.');
    snd(210, 0.2, 'sawtooth', 0.2, 90);
    addOut(1);
  }
  finishBatterPA();
  S.phase = 'result';
  board();
}

/* ---------- 도루(Steal) 연타 기능 ---------- */
function finishStealRace(safe) {
  const race = stealRace;
  if (!race) return;
  clearTimeout(stealTimer); stealTimer = 0; stealRace = null;
  const { runner, runnerIdx, targetBase } = race;
  if (safe) {
    runner.g.position.copy(BP[targetBase]); runner.b = targetBase; runner.to = targetBase;
    occ[targetBase] = runner; occ[runnerIdx] = null; setOcc(occ);
    flash('⚡ 도루 성공!', '주자가 송구보다 먼저 베이스에 닿았습니다.');
    snd(700, 0.15, 'sine', 0.25, 1000);
  } else {
    runner.out = true; runner.h = 0;
    occ[runnerIdx] = null; setOcc(occ); addOut(1);
    flash('도루 아웃!', '송구가 주자보다 먼저 베이스에 도착했습니다.');
    snd(200, 0.2, 'sawtooth', 0.3, 100);
  }
  isStealing = false; activeStealRunner = null; board();
}

function attemptSteal() {
  if (S.mode !== 'bat' || (S.phase !== 'aim' && S.phase !== 'wait')) return;
  
  const runnerIdx = occ[2] ? 2 : (occ[1] ? 1 : 0);
  if (!runnerIdx) return;

  const now = performance.now();
  if (!isStealing) {
    isStealing = true;
    // 주자가 송구 전에 베이스에 닿을 수 있도록 연타 속도와 송구 시간을 맞춥니다.
    activeStealRunner = occ[runnerIdx];
    const runnerScale = 0.84 + (activeStealRunner.speedRating || 3) * 0.04;
    stealSpeedBonus = 12.0 * runnerScale;
    const targetBase = runnerIdx + 1;
    
    activeStealRunner.to = targetBase;
    activeStealRunner.t0 = now;
    activeStealRunner.sp = stealSpeedBonus;

    const thrower = runnerIdx === 2 || Math.random() < 0.45 ? 'catcher' : 'pitcher';
    const target = BP[targetBase].clone(); target.y = 1.25;
    const throwFrom = thrower === 'catcher' ? V3(0.15, 1.45, 0.8) : V3(PITCHERS[currentPitcherIdx].releaseX, PITCHERS[currentPitcherIdx].releaseY, -17.8);
    const throwDuration = 1500;
    defensiveThrow = { from: throwFrom, to: target, start: now, duration: throwDuration, thrower, targetBase };
    stealRace = { runner: activeStealRunner, runnerIdx, targetBase, throwAt: now + throwDuration };
    flash('⚠️ 견제 송구!', `${thrower === 'catcher' ? '포수' : '투수'}가 ${targetBase}루로 던집니다.`);
    snd(500, 0.1, 'sine', 0.2);
    stealTimer = setTimeout(() => {
      if (!stealRace) return;
      const runner = stealRace.runner;
      const atBase = runner.b >= targetBase || runner.g.position.distanceTo(BP[targetBase]) <= 0.7;
      finishStealRace(atBase);
    }, throwDuration);
  } else {
    // 도루 진행 중 연타 시 주자 속도 증가
    const runnerScale = 0.84 + (activeStealRunner?.speedRating || 3) * 0.04;
    stealSpeedBonus = Math.min(24.5 * runnerScale, stealSpeedBonus + 1.8 * runnerScale);
    if (activeStealRunner) {
      activeStealRunner.sp = stealSpeedBonus;
    }
    snd(600 + stealSpeedBonus * 15, 0.05, 'triangle', 0.15);
  }
  board();
}

/* ---------- 투구 알고리즘 ---------- */
const WIND = 500;

function pitch() {
  if (stealRace) { timer = setTimeout(pitch, 80); return; }
  if (S.mode === 'bat') pciCenter.copy(aim);
  resetField(); const now = performance.now(), profile = DIFFICULTIES[difficulty], targetZone = Math.random() < profile.zoneRate;
  const pData = PITCHERS[currentPitcherIdx];
  if (S.mode === 'bat') S.pt = pData.pitches[Math.floor(Math.random() * pData.pitches.length)];
  let tx = R(-0.5, 0.5), ty = R(-0.5, 0.5);
  if (!targetZone) {
    if (Math.random() < 0.6) tx = (Math.random() < 0.5 ? -1 : 1) * R(0.56, 1.1);
    else ty = (Math.random() < 0.5 ? -1 : 1) * R(0.54, 1.1);
  }
  
  const curType = TYPES[S.pt];
  const umpire = zoneCall(tx, ty);
  const fatigue = 1 - (100 - pitcherStamina) * 0.0018;
  const baseDur = R(curType.dur[0], curType.dur[1]) / (pData.speed * fatigue * profile.pitchSpeed);
  const speedKmh = Math.round(18.4 / (baseDur / 1000) * 3.6);
  pitcherStamina = Math.max(0, pitcherStamina - 1.1 / pData.endurance);
  
  P = {
    tx, ty, inZone: umpire.called, actualInZone: umpire.actual, challengeable: umpire.challengeable,
    speedKmh,
    release: V3(pData.releaseX, pData.releaseY, -17.8),
    curve: (Math.random() < 0.4 ? R(-1, 1) : 0) * curType.c * pData.break,
    lift: R(0, 0.35) * curType.l,
    t0: now + WIND, dur: baseDur, done: false
  };
  P.arrive = P.t0 + baseDur;
  S.phase = 'pitch'; sw = null; hit = null;
  board();
  startTimingGauge(P.t0, P.arrive);
}

function bp(p, o) {
  const e = Math.min(p, 1.2), a = Math.sin(Math.min(p, 1) * Math.PI);
  const rel = P.release;
  return o.set(
    rel.x + (P.tx * 0.4 - rel.x) * e + P.curve * a * 0.5,
    rel.y + (0.82 + P.ty * 0.5 - rel.y) * e + P.lift * a,
    rel.z + (0.1 - rel.z) * e
  );
}

function ready() {
  resetField(); P = null; hit = null; sw = null; isStealing = false; activeStealRunner = null;
  pitchCharge = null;
  bt.visible = true; defensiveThrow = null;
  S.phase = 'aim'; flash(S.mode === 'pitch' ? '투구 준비' : '타격 준비', S.mode === 'bat' ? '상대 투수가 곧 투구합니다.' : '구종을 고르고 투구하세요.');
  board();
}

function beginPitchCharge() {
  if (S.mode !== 'pitch' || S.phase !== 'aim' || pitchCharge) return;
  const wrap = $('timingWrap'), cursor = $('timingCursor'), hint = $('timingHint');
  pitchCharge = { start: performance.now(), duration: 1100 };
  wrap.style.display = 'block'; wrap.dataset.kind = 'pitch';
  hint.textContent = '구간 안에서 SHIFT를 놓으세요'; hint.style.display = 'block';
  cancelAnimationFrame(timingAnimId);
  const animateCharge = () => {
    if (!pitchCharge) return;
    const pct = C((performance.now() - pitchCharge.start) / pitchCharge.duration, 0, 1) * 100;
    cursor.style.left = pct + '%';
    timingAnimId = requestAnimationFrame(animateCharge);
  };
  timingAnimId = requestAnimationFrame(animateCharge);
  flash('릴리스 타이밍!', 'SHIFT를 누르고 있다가 초록 구간에서 놓으세요.');
}

function cancelPitchCharge() {
  if (!pitchCharge) return;
  pitchCharge = null; cancelAnimationFrame(timingAnimId);
  $('timingWrap').style.display = 'none'; $('timingHint').style.display = 'none';
}

function releasePitchCharge() {
  if (!pitchCharge) return;
  const charge = pitchCharge;
  const pct = C((performance.now() - charge.start) / charge.duration, 0, 1) * 100;
  const quality = C(1 - Math.abs(pct - 75) / 18, 0, 1);
  pitchCharge = null; cancelAnimationFrame(timingAnimId);
  $('timingWrap').style.display = 'none'; $('timingHint').style.display = 'none';
  flash(quality >= 0.82 ? '완벽한 릴리스!' : quality >= 0.35 ? '좋은 릴리스!' : '릴리스 타이밍 놓침', quality > 0 ? '구속과 변화량 보너스가 적용됩니다.' : '다음 투구에서 타이밍을 맞춰 보세요.');
  throwPitch(quality);
}

function throwPitch(releaseQuality = 0) {
  const pData = PITCHERS[currentPitcherIdx];
  const T = TYPES[S.pt];
  const quality = C(releaseQuality, 0, 1);
  const fatigue = 1 - (100 - pitcherStamina) * 0.0018;
  const e = T.err * (pData.ctrl / 0.04) / fatigue * (1 - quality * 0.1);
  const tx = C((aim.x + R(-e, e)) / 0.4, -1.3, 1.3);
  const ty = C((aim.y + R(-e, e) - 0.82) / 0.5, -1.3, 1.3);
  const now = performance.now();
  const dur = R(T.dur[0], T.dur[1]) / (pData.speed * fatigue * (1 + quality * 0.1));
  const speedKmh = Math.round(18.4 / (dur / 1000) * 3.6);
  pitcherStamina = Math.max(0, pitcherStamina - 1.1 / pData.endurance);
  const umpire = zoneCall(tx, ty);
  
  const me = {
    tx, ty, inZone: umpire.called, actualInZone: umpire.actual, challengeable: umpire.challengeable, speedKmh,
    release: V3(pData.releaseX, pData.releaseY, -17.8),
    curve: (T.c * pData.break * (1 + quality * 0.55) + quality * 0.12) * (Math.random() < 0.5 ? -1 : 1),
    lift: T.l, t0: now + WIND, dur, done: false
  };
  me.arrive = me.t0 + me.dur; P = me; S.phase = 'pitch'; sw = null; hit = null;
  
  const sp = S.strikes === 2;
  const aiChance = DIFFICULTIES[difficulty].aiContact;
  if (Math.random() < C((me.actualInZone ? (sp ? 0.95 : 0.75) : (sp ? 0.4 : 0.2)) * aiChance, 0, 0.98)) {
    const off = T.bias + 170 * (1 + Math.max(Math.abs(tx), Math.abs(ty)) * 0.8) * (R(-1, 1) + R(-1, 1)) / 1.5;
    setTimeout(() => {
      if (P !== me || S.phase !== 'pitch') return;
      sw = { t: performance.now(), ai: true }; resolve(off);
    }, me.arrive - CONTACT + off - now);
  }
}

/* ---------- 타격 타이밍 게이지 UI ---------- */
function startTimingGauge(startT, arriveT) {
  const wrap = $('timingWrap');
  const cursor = $('timingCursor');
  wrap.style.display = 'block';
  
  function updateGauge() {
    const now = performance.now();
    const pct = C((now - startT) / (arriveT - startT), 0, 1.1) * 100;
    cursor.style.left = Math.min(100, pct) + '%';
    if (now < arriveT + 100 && S.phase === 'pitch') {
      timingAnimId = requestAnimationFrame(updateGauge);
    } else {
      setTimeout(() => { wrap.style.display = 'none'; }, 300);
    }
  }
  cancelAnimationFrame(timingAnimId);
  timingAnimId = requestAnimationFrame(updateGauge);
}

/* ---------- 타격 판정 연산 ---------- */
const LABEL = { hr: '홈런!', double: '2루타', single: '안타', bunt: '번트!', groundout: '땅볼 아웃', flyout: '뜬공 아웃', foul: '파울', whiff: '헛스윙', strike: '스트라이크', ball: '볼' };
const SPD = { hr: [36, 24], double: [27, 11], single: [21, 5.5], groundout: [15.5, 0.35], bunt: [6.8, 0.025], flyout: [17, 16], foul: [20, 12] };

function resolve(off) {
  P.done = true; S.phase = 'result';
  updatePitchInfo(P);
  let r, parts = [];
  if (off === null) {
    r = P.inZone ? 'strike' : 'ball';
    const wrongCall = P.inZone !== P.actualInZone;
    if (!P.actualInZone && Math.abs(P.tx) > 1.0 && Math.abs(P.ty) < 0.85 && Math.random() < 0.1) r = 'hbp';
    updateABS(P.tx, P.ty, `${r === 'strike' ? '스트라이크' : r === 'hbp' ? '몸에 맞음' : '볼'} 판정`, wrongCall);
    const safeToChallenge = r === 'strike' ? S.strikes < 2 : r === 'ball' ? S.balls < 3 : false;
    pendingABSCall = P.challengeable && wrongCall && safeToChallenge
      ? { called: r, actual: P.actualInZone ? 'strike' : 'ball', expires: performance.now() + 3000 }
      : null;
    if (pendingABSCall) setTimeout(() => { if (pendingABSCall && performance.now() >= pendingABSCall.expires) { pendingABSCall = null; board(); } }, 3050);
    snd(220, 0.08, 'triangle', 0.3, 90);
  } else {
    pendingABSCall = null;
    updateABS(P.tx, P.ty, '스윙 · 타격 판정');
    const hitter = S.mode === 'bat' ? lineup[battingOrderIndex] : null;
    const contactScale = hitter && !buntMode ? 1 - (hitter.contact - 3) * 0.035 : 1;
    const powerBonus = hitter && !buntMode ? (hitter.power - 3) * 2.4 : 0;
    pciInsideContact = false; pciOutsideContact = false;
    let q = Math.max(0, Math.abs(off) * contactScale - powerBonus - (battingMode === 'power' && hitter ? 8 : 0)) + (P.actualInZone ? 0 : 70);
    if (hitter && sw?.user && pciEnabled && !buntMode) {
      const radius = 0.07 + ((hitter.contact - 1) / 4) * 0.11;
      const dx = P.tx * 0.4 - pciCenter.x, dy = 0.82 + P.ty * 0.5 - pciCenter.y;
      pciInsideContact = Math.hypot(dx, dy) <= radius;
      pciOutsideContact = !pciInsideContact;
      q *= pciInsideContact ? 0.76 : 1.15;
    }
    if (hitter && battingMode === 'contact' && !buntMode) q *= 0.78;
    if (buntMode && S.mode === 'bat' && sw?.user) {
      r = q < 82 ? 'bunt' : q < 140 ? 'foul' : 'whiff';
      buntMode = false; board(); parts.push('번트 시도 · 공을 맞췄습니다');
    } else {
      const weakContactWhiff = hitter ? (5 - hitter.contact) * 0.018 : 0;
      const contactWhiff = battingMode === 'contact' ? weakContactWhiff * 0.15 : weakContactWhiff;
      const modeWhiff = battingMode === 'power' ? 0.12 : battingMode === 'contact' ? 0.003 : 0.015;
      const extraWhiff = hitter && sw?.user && Math.random() < contactWhiff + modeWhiff;
      if (off < -280 || extraWhiff || (pciOutsideContact && Math.random() < 0.78)) r = 'whiff';
      else r = q < 6 ? 'hr' : q < 26 ? 'double' : q < 52 ? 'single' : q < 170 ? (Math.random() < 0.5 ? 'groundout' : 'flyout') : q < 245 ? 'foul' : 'whiff';
      if (hitter && battingMode === 'contact' && !buntMode) {
        if (r === 'hr') r = 'double';
        else if (r === 'double' && Math.random() < 0.75) r = 'single';
      }
      parts.push(Math.abs(off) < 30 ? 'PERFECT PERFECT!' : off < 0 ? '타이밍 빠름' : '타이밍 늦음');
      if (pciEnabled && hitter) parts.push(pciInsideContact ? '조준 성공 · 타구 보너스' : pciOutsideContact ? '조준원 밖 · 헛스윙 위험' : '');
    }
    if (r === 'whiff') snd(420, 0.14, 'sine', 0.08, 140);
    else setTimeout(hitSound, CONTACT);
  }

  if (SPD[r]) {
    if (r !== 'foul') setTimeout(() => { bt.visible = false; }, 560);
    const T = performance.now() + CONTACT, d = C(off / 110, -1, 1), ang = r === 'bunt' ? R(-0.08, 0.08) : r === 'foul' ? (d < 0 ? -1 : 1) * R(0.95, 1.3) : C(d, -0.7, 0.7) * 0.85, [vh, vy] = SPD[r];
    const modePowerScale = S.mode !== 'bat' || r === 'bunt' ? 1 : battingMode === 'power' ? 1.18 : battingMode === 'contact' ? 0.78 : 1;
    const pciPowerScale = S.mode === 'bat' && pciInsideContact ? 1.18 : S.mode === 'bat' && pciOutsideContact ? 0.82 : 1;
    const powerScale = S.mode === 'bat' && r !== 'bunt' ? (1 + (lineup[battingOrderIndex].power - 3) * 0.04) * modePowerScale * pciPowerScale : 1;
    const s = vh * R(0.9, 1.1) * powerScale;
    const path = sim(bp(C((T - P.t0) / P.dur, 0, 1), V3(0, 0, 0)), V3(Math.sin(ang) * s, vy * R(0.9, 1.1) * powerScale, -Math.cos(ang) * s), r === 'hr' ? 5.2 : 6.5);
    hit = { t: T, path, plan: null, hr: r === 'hr', bunt: r === 'bunt', chase: null };
    if (r !== 'hr' && r !== 'foul') {
      const possiblePlay = defend(path, r === 'bunt');
      // 안타/2루타로 판정된 타구는 포구 추정만으로 아웃으로 뒤집지 않습니다.
      const wasHit = r === 'single' || r === 'double';
      const dd = possiblePlay;
      if (dd) {
        if (dd.air) {
          // 가까운 플라이를 야수가 실제로 잡도록 하되, 안타성 타구는 일부만 포구 처리합니다.
          if (!wasHit || Math.random() < 0.14) r = 'flyout';
        } else if (r === 'groundout' || r === 'bunt') {
          // 내야수가 포구 가능한 땅볼은 안타로 되돌리지 않고 아웃/1루 승부로 처리합니다.
        } else if (r === 'flyout') r = 'single';
        const cover = !dd.air && dd.f === F[0] ? F[1] : F[0];
        hit.plan = { f: dd.f, i: dd.i, air: dd.air, out: r === 'groundout' || r === 'bunt' || r === 'flyout', cover, throwTo: r === 'groundout' || r === 'bunt' ? B1T.clone() : null, throwDuration: 1.3 };
      } else {
        // 포구 가능한 수비수가 없으면 플라이도 인플레이 안타로 처리합니다.
        if (r === 'groundout' || r === 'flyout') {
          const endPos = path[path.length - 1];
          r = Math.hypot(endPos.x, endPos.z) > 48 ? 'double' : 'single';
        }
        const landing = path[path.length - 1];
        const outfieldOrder = F.slice(4).map(f => ({ f, distance: Math.hypot(f.g.position.x - landing.x, f.g.position.z - landing.z) })).sort((a, b) => a.distance - b.distance);
        hit.chase = outfieldOrder[0]?.f || F[4];
        hit.backup = outfieldOrder[1]?.f || F[5];
      }
      if (r === 'bunt' && !hit.plan) {
        let i = Math.min(36, path.length - 1);
        for (let j = 12; j < Math.min(path.length, 80); j += 2) {
          if (path[j].y <= 0.3) { i = j; break; }
        }
        const target = path[i];
        const f = F.slice(0, 4).map(player => ({ player, d: Math.hypot(player.g.position.x - target.x, player.g.position.z - target.z) })).sort((a, b) => a.d - b.d)[0].player;
        hit.plan = { f, i, air: false, out: true, cover: F[1], throwTo: B1T.clone(), throwDuration: 1.3 };
      }
      if (S.mode === 'pitch' && (r === 'single' || r === 'double') && possiblePlay && possiblePlay.distance > 0.45 && Math.random() < 0.22) {
        hit.fieldOpportunity = possiblePlay;
      }
    }
  }

  const h0 = S.h, tt = hit ? hit.t : performance.now(), ex = hit && !hit.plan ? 1 : 0;
  let label = LABEL[r], dp = false;

  if (r === 'hr') { recordBatterHit(4); if (S.mode === 'bat') S.hr++; advance(4, 0, tt); }
  else if (r === 'double') {
    if (deferForFielding(2, tt, ex)) label = '호수비 찬스!';
    else { recordBatterHit(2); advance(2, ex, tt); }
  }
  else if (r === 'single') {
    if (deferForFielding(1, tt, ex)) label = '호수비 찬스!';
    else { recordBatterHit(1); advance(1, ex, tt); }
  }
  else if (r === 'bunt') {
    beginBuntRace(tt); label = '번트 1루 승부!';
  }
  else if (r === 'groundout') {
    if (!occ[1] && hit && hit.plan && hit.plan.throwTo) {
      beginBatterRace(tt);
      label = '1루 승부!';
    } else {
      recordBatterOut();
      dp = !!(occ[1] && S.outs <= 1 && hit && hit.plan && !hit.plan.air && hit.plan.i < 75 && Math.random() < 0.7);
      if (dp) label = '병살타';
      addOut(dp ? 2 : 1);
    }
  }
  else if (r === 'flyout') {
    const sacFlyChance = S.mode === 'bat' && S.outs < 2 && !!occ[3];
    recordBatterOut(); addOut(1);
    if (sacFlyChance) { beginSacFlyRace(tt); label = '희생플라이 승부!'; parts.push('질주 버튼을 연타해 홈 송구보다 먼저 도착하세요'); }
  }
  else if (r === 'foul') { if (S.strikes < 2) S.strikes++; }
  else if (r === 'strike' || r === 'whiff') { S.strikes++; if (S.strikes >= 3) { label = '삼진 아웃'; recordBatterOut(); if (S.mode === 'pitch') currentPitcherStats().strikeouts++; else opponentPitcherStats.strikeouts++; addOut(1); } }
  else if (r === 'ball') { S.balls++; if (S.balls >= 4) { label = '볼넷'; if (S.mode === 'bat') { batterStats.pa++; batterStats.walks++; opponentPitcherStats.walks++; batterPAMode = 'bat'; batterPAComplete = true; } else if (S.mode === 'pitch') { currentPitcherStats().walks++; opponentLineup[opponentBatterIndex].stats.pa++; opponentLineup[opponentBatterIndex].stats.walks++; batterPAMode = 'pitch'; batterPAComplete = true; } walk(tt); } }
  else if (r === 'hbp') { label = '몸에 맞는 공'; if (S.mode === 'bat') { batterStats.pa++; batterStats.hbp++; opponentPitcherStats.hbp++; batterPAMode = 'bat'; batterPAComplete = true; } else if (S.mode === 'pitch') { currentPitcherStats().hbp++; opponentLineup[opponentBatterIndex].stats.pa++; opponentLineup[opponentBatterIndex].stats.hbp++; batterPAMode = 'pitch'; batterPAComplete = true; } walk(tt); }

  if (!batterRace && !pendingFieldingPlay) finishBatterPA();
  flash(label, parts.join(', ')); board();
  const n2 = performance.now(), run = Math.max(0, ...pool.filter(q => q.on).map(q => q.t0 - n2 + (q.to - q.b) * 27400 / q.sp));
  
  const pathRun = !hit ? 0 : hit.plan
    ? (hit.plan.i / 60 + (hit.plan.throwTo ? hit.plan.throwDuration + 0.2 : 0.2)) / 1.7 * 1000 + 150
    : hit.path.length / (60 * 1.7) * 1000 + 250;
  const raceWait = batterRace ? Math.max(0, batterRace.callAt - performance.now() + 150) : 0;
  const fieldingWait = pendingFieldingPlay ? Math.max(0, pendingFieldingPlay.impactAt + 1000 - performance.now()) : 0;
  timer = setTimeout(() => { if (pendingFieldingPlay) resolveFieldingPlay(false); if (S.h >= 2 * maxInnings) end(); else if (S.mode === 'pitch') ready(); else { ready(); timer = setTimeout(pitch, 1200); } }, Math.max(r === 'hr' ? 3600 : S.h !== h0 ? 2600 : 2300, run + 700, pathRun, raceWait, fieldingWait));
}

function end() {
  S.phase = 'over'; const d = S.sc[0] - S.sc[1];
  board(); $('types').hidden = true;
  overlay(d > 0 ? '승리!' : d < 0 ? '패배' : '무승부', `${teamNames[0]} ${S.sc[0]} : ${S.sc[1]} ${teamNames[1]}\n안타 ${S.hits}개, 홈런 ${S.hr}개`, '');
}

function toggleBunt() {
  if (S.mode !== 'bat' || S.phase === 'running') return;
  buntMode = !buntMode;
  board();
  flash(buntMode ? '번트 준비!' : '번트 취소', buntMode ? '다음 스윙에서 번트를 시도합니다.' : '일반 스윙으로 돌아갑니다.');
}

function setBattingMode(mode) {
  if (!['power', 'normal', 'contact'].includes(mode)) return;
  battingMode = mode;
  board();
  const labels = { power: '파워스윙', normal: '노말', contact: '컨택' };
  flash(`${labels[mode]} 모드`, mode === 'power' ? '장타력이 올라가고 헛스윙 위험도 커집니다.' : mode === 'contact' ? '타이밍 판정이 넓어지고 타구 거리는 짧아집니다.' : '파워와 컨택의 균형을 맞춥니다.');
}

function togglePCI() {
  if (S.mode !== 'bat' || S.phase === 'running' || S.phase === 'over') return;
  pciEnabled = !pciEnabled;
  if (S.phase === 'aim') pciCenter.copy(aim);
  board();
  flash(pciEnabled ? '조준 원 ON' : '조준 원 OFF', pciEnabled ? '마우스로 원을 옮긴 뒤, 원 안에 들어온 공을 노리세요.' : '조준 보정 없이 타격합니다.');
}

function setBatterSide(side) {
  batterSide = side === 'L' ? 'L' : 'R';
  bt.scale.x = batterSide === 'L' ? -1 : 1;
  document.querySelectorAll('#batterSideChoices [data-batside]').forEach(button => button.classList.toggle('on', button.dataset.batside === batterSide));
  if (P) updatePitchInfo(P);
  else $('pitchInfo').textContent = `${batterSide === 'R' ? '우타' : '좌타'} · 투구 후 구종과 구속이 표시됩니다`;
}

function start(m) {
  clearTimeout(timer); cancelPitchCharge(); S.fm = S.mode = m || S.fm; S.h = 0; S.sc = [0, 0];
  buntMode = false; battingMode = 'normal'; pciEnabled = false; pciInsideContact = pciOutsideContact = false;
  teamNames = [
    $('ownTeamName')?.value?.trim().slice(0, 12) || '우리 팀',
    $('opponentTeamName')?.value?.trim().slice(0, 12) || '상대 팀'
  ];
  if (pendingFieldingPlay) { clearTimeout(pendingFieldingPlay.cueTimer); clearTimeout(pendingFieldingPlay.settleTimer); pendingFieldingPlay = null; }
  Object.assign(S, { outs: 0, balls: 0, strikes: 0, hits: 0, hr: 0 });
  lineup = Array.from({ length: 9 }, (_, i) => {
    const entered = $(`lineupName${i}`)?.value?.trim();
    const name = entered && entered !== `${i + 1}번 타자` ? entered : `${i + 1}번 타자`;
    return {
      name,
      speed: 1 + Math.floor(Math.random() * 5),
      power: 1 + Math.floor(Math.random() * 5),
      contact: 1 + Math.floor(Math.random() * 5),
      stats: emptyBatterStats()
    };
  });
  battingOrderIndex = 0; batterStats = lineup[0].stats; batterPAComplete = false;
  opponentPitcherStats = emptyPitcherStats();
  opponentLineup = Array.from({ length: 9 }, (_, i) => ({ name: `상대 ${i + 1}번 타자`, stats: emptyBatterStats() }));
  opponentBatterIndex = 0; batterPAMode = null;
  pitcherStatsById = Object.fromEntries(PITCHERS.map(p => [p.id, emptyPitcherStats()]));
  challengeCount = 2; pendingABSCall = null;
  clearRun(); bt.visible = true; defensiveThrow = null; $('types').hidden = S.mode !== 'pitch';
  board(); P = null; hit = null; sw = null; resetField();
  $('ov').hidden = true; S.phase = 'wait';
  $('pitchInfo').textContent = `${batterSide === 'R' ? '우타' : '좌타'} · 투구 후 구종과 구속이 표시됩니다`;
  flash('플레이 볼', S.mode === 'bat' ? '초 공격' : '초 수비');
  pitcherStamina = 100;
  refreshPitchButtons(); updateStatsUI(); updatePitcherUI();
  timer = setTimeout(() => { if (S.mode === 'pitch') ready(); else { ready(); timer = setTimeout(pitch, 1200); } }, 900);
}

function act() {
  if (pitchCharge) return;
  if (!ac) { try { ac = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) {} }
  if (ac && ac.state === 'suspended') ac.resume();
  if (S.phase === 'idle' || S.phase === 'over') return start(S.fm);
  if (S.phase === 'aim') { if (S.mode === 'pitch') return throwPitch(); return; }
  if (S.phase !== 'pitch' || sw || S.mode === 'pitch') return;
  const now = performance.now(); sw = { t: now, user: true, bunt: buntMode }; resolve(now + CONTACT - P.arrive);
}

/* ---------- 메인 프레임 렌더링 Loop ---------- */
function tick(now) {
  const dt = Math.min(0.033, (now - last) / 1000); last = now;
  if (S.phase === 'pitch' && !P.done && now + CONTACT > P.arrive + 200) resolve(null);
  
  // 투수마다 팔이 지나가는 높이와 투구 궤도가 다릅니다.
  const pitcher = PITCHERS[currentPitcherIdx];
  arm.position.set(pitcher.releaseX, pitcher.releaseY + 0.08, -18.4);
  const deliveryStart = P ? P.t0 - WIND : 0;
  const deliveryActive = !!P && now >= deliveryStart && now <= deliveryStart + 660;
  const deliveryT = deliveryActive ? C((now - deliveryStart) / 660, 0, 1) : 1;
  const drive = deliveryT < 0.48 ? deliveryT / 0.48 : 1 - (deliveryT - 0.48) / 0.52;
  const recover = deliveryT < 0.48 ? 0 : (deliveryT - 0.48) / 0.52;
  if (!deliveryActive) {
    arm.rotation.set(-0.2, 0, 0);
  } else if (pitcher.form === 'over') {
    arm.rotation.set(deliveryT < 0.48 ? -0.2 - 3.15 * drive : -3.35 + 3.15 * recover, 0.04, 0.08);
  } else if (pitcher.form === 'side') {
    arm.rotation.set(-0.32 - 0.35 * drive + 0.67 * recover, 0, deliveryT < 0.48 ? -0.18 - 2.0 * drive : -2.18 + 2.0 * recover);
  } else if (pitcher.form === 'under') {
    arm.rotation.set(deliveryT < 0.48 ? 0.55 + 1.05 * drive : 1.6 - 1.8 * recover, 0.12, 0.25 + 0.3 * drive - 0.37 * recover);
  } else {
    arm.rotation.set(deliveryT < 0.48 ? -0.1 - 2.45 * drive : -2.55 + 2.45 * recover, 0.12, deliveryT < 0.48 ? 0.18 - 0.48 * drive : -0.3 + 0.3 * recover);
  }
  const pitcherStride = deliveryT < 0.48 ? drive : 1 - recover;
  pit.position.set(0.12 * pitcherStride, 0.28 + 0.1 * pitcherStride, -18.4 + 0.62 * pitcherStride);
  pit.rotation.x = deliveryActive ? -0.08 * pitcherStride : 0;
  pit.rotation.y = Math.PI + (pitcher.form === 'side' ? 0.2 : 0.08) * pitcherStride;
  pit.rotation.z = (pitcher.form === 'under' ? 0.22 : -0.13) * pitcherStride;
  catcher.rotation.set(0, Math.PI, 0);
  if (defensiveThrow) {
    const throwPose = C((now - defensiveThrow.start) / 240, 0, 1);
    if (defensiveThrow.thrower === 'pitcher') arm.rotation.z = -1.2 * throwPose;
    else {
      catcher.rotation.y += (defensiveThrow.targetBase === 2 ? -0.28 : 0.28) * throwPose;
      catcher.rotation.z = -0.12 * throwPose;
    }
  }
  
  // 준비 동작에서 뒤로 당겼다가, 작은 체중 이동과 함께 배트를 앞쪽으로 크게 가속합니다.
  if (sw?.bunt) {
    const elapsed = now - sw.t;
    const smooth = x => { x = C(x, 0, 1); return x * x * (3 - 2 * x); };
    const hold = 1 - smooth((elapsed - 250) / 260);
    swingArms.rotation.set(-0.28 * hold, 0.08 * hold, 0.02 * hold);
    bat.position.x = (batterSide === 'L' ? 0.58 : 0.48);
    bat.rotation.set(0, 0, Math.PI / 2 * hold + BAT_READY * (1 - hold));
    up.rotation.set(-0.06 * hold, 0.04 * hold, 0);
    bt.rotation.set(0.015 * hold, 0.035 * hold, 0);
    bt.position.set(0, 0.018 * hold, -0.075 * hold);
    batterLegs.forEach((leg, i) => leg.rotation.set(0, 0, i === 1 ? -0.035 * hold : 0.015 * hold));
  } else if (sw) {
    bat.position.x = 0.28;
    const elapsed = now - sw.t;
    const smooth = x => { x = C(x, 0, 1); return x * x * (3 - 2 * x); };
    const load = smooth(elapsed / 170), drive = smooth((elapsed - 170) / 190), finish = smooth((elapsed - 360) / 360);
    const recoil = Math.sin(Math.min(1, elapsed / 170) * Math.PI / 2);
    swingArms.rotation.y = elapsed < 170 ? -0.22 - 0.92 * load : elapsed < 360 ? -1.14 + 2.35 * drive : 1.21 - 0.42 * finish;
    swingArms.rotation.z = elapsed < 170 ? -0.12 * load : elapsed < 360 ? -0.12 + 0.48 * drive : 0.36 - 0.18 * finish;
    bat.rotation.y = elapsed < 170 ? -0.25 * load : elapsed < 360 ? -0.25 + 0.58 * drive : 0.33 - 0.25 * finish;
    bat.rotation.z = elapsed < 170 ? BAT_READY - 0.62 * recoil : elapsed < 360 ? BAT_READY - 0.62 + 2.05 * drive : BAT_READY + 1.43 - 0.5 * finish;
    up.rotation.y = elapsed < 170 ? -0.05 - 0.14 * load : elapsed < 360 ? -0.19 + 0.36 * drive : 0.17 - 0.09 * finish;
    up.rotation.x = elapsed < 170 ? -0.015 * load : elapsed < 360 ? -0.015 + 0.075 * drive : 0.06 - 0.04 * finish;
    bt.rotation.y = elapsed < 170 ? -0.05 * load : elapsed < 360 ? -0.05 + 0.15 * drive : 0.10 - 0.04 * finish;
    bt.position.z = elapsed < 170 ? -0.025 * load : elapsed < 360 ? -0.025 + 0.075 * drive : 0.05 - 0.035 * finish;
    bt.position.y = elapsed < 170 ? 0.008 * load : elapsed < 360 ? 0.008 + 0.022 * drive : 0.03 - 0.02 * finish;
    const frontLeg = batterSide === 'R' ? batterLegs[1] : batterLegs[0];
    frontLeg.rotation.z = elapsed < 170 ? 0.03 * load : elapsed < 360 ? 0.03 - 0.13 * drive : -0.10 + 0.07 * finish;
  } else if (buntMode && S.mode === 'bat') {
    bt.position.set(0, 0, 0);
    bt.rotation.set(0, 0, 0);
    batterLegs.forEach(leg => leg.rotation.set(0, 0, 0));
    up.rotation.set(-0.05, 0.04, 0);
    swingArms.rotation.set(-0.24, 0.08, 0.02);
    bat.position.x = batterSide === 'L' ? 0.58 : 0.48;
    bat.rotation.set(0, 0, Math.PI / 2);
  } else {
    bat.position.x = 0.28;
    bt.position.set(0, 0, 0);
    bt.rotation.set(0, 0, 0);
    batterLegs.forEach(leg => leg.rotation.set(0, 0, 0));
    up.rotation.set(0, 0.03, 0);
    swingArms.rotation.set(0, 0, 0);
    swingArms.rotation.y += (0 - swingArms.rotation.y) * 0.18;
    swingArms.rotation.z += (0 - swingArms.rotation.z) * 0.18;
    bat.rotation.y += (0 - bat.rotation.y) * 0.22;
    bat.rotation.z += (BAT_READY - bat.rotation.z) * 0.18;
  }
  
  // 주자 위치 갱신
  pool.forEach(r => {
    if (!r.on || now < r.t0) return;
    if (r.b >= r.to) {
      if (r.out && !r.h) { r.h = 1; setTimeout(() => { r.on = false; r.g.visible = false; }, 500); }
      else if (r.to >= 4) { r.on = false; r.g.visible = false; }
      return;
    }
    const tg = BP[r.b + 1], q = r.g.position, dx = tg.x - q.x, dz = tg.z - q.z, d = Math.hypot(dx, dz), st = r.sp * dt;
    if (d <= st) { q.x = tg.x; q.z = tg.z; r.b++; } else { q.x += dx / d * st; q.z += dz / d * st; }
    r.g.rotation.y = Math.atan2(dx, dz);
  });
  if (stealRace) {
    const runner = stealRace.runner, targetBase = stealRace.targetBase;
    const atBase = runner.b >= targetBase || runner.g.position.distanceTo(BP[targetBase]) <= 0.7;
    if (atBase && now < stealRace.throwAt) finishStealRace(true);
  }
  if (batterRace && (now >= batterRace.callAt || batterRace.runner.b >= (batterRace.kind === 'sacfly' ? 4 : 1))) settleBatterRace(now);
  
  // 수비 AI 이동
  if (hit && hit.path && hit.path.length > 0) {
    const k = (now - hit.t) / 1000 * 1.7;
    if (k >= 0) {
      const idx = Math.min(hit.path.length - 1, Math.floor(k * 60));
      const ballPos = hit.path[idx];
      const pl = hit.plan;

      F.forEach(f => {
        let tg = null;
        if (pl) {
          if (f === pl.f) {
            tg = hit.path[pl.i] || ballPos;
          } else if (pl.out && !pl.air && f === pl.cover) {
            tg = B1;
          } else if (pl.dp && f === F[1]) {
            tg = B2P;
          }
        } else if (hit.fieldOpportunity && hit.fieldOpportunity.f === f) {
          tg = hit.path[hit.fieldOpportunity.i] || ballPos;
        } else if (hit.chase === f) {
          tg = ballPos;
        } else if (hit.backup === f) {
          tg = ballPos.clone().add(V3(ballPos.x >= 0 ? -4 : 4, 0, 4));
        }

        if (tg) {
          const q = f.g.position, dx = tg.x - q.x, dz = tg.z - q.z, d = Math.hypot(dx, dz);
          if (d > 0.1) {
            const buntSpeed = hit.bunt ? 0.38 : 1;
            const st = Math.min(SPDF * 1.5 * 1.7 * dt * buntSpeed, d);
            q.x += (dx / d) * st;
            q.z += (dz / d) * st;
            f.g.rotation.y = Math.atan2(dx, dz);
          }
        }
      });
    }
  }

  ret.visible = S.mode === 'pitch' && S.phase === 'aim'; ret.position.set(aim.x, aim.y, 0.15);
  const activeHitter = lineup[battingOrderIndex];
  const pciRadius = 0.07 + (((activeHitter?.contact || 3) - 1) / 4) * 0.11;
  const pciAim = S.phase === 'aim' ? aim : pciCenter;
  pciRing.visible = S.mode === 'bat' && pciEnabled && (S.phase === 'aim' || S.phase === 'pitch');
  pciRing.position.set(pciAim.x, pciAim.y, 0.15);
  pciRing.scale.set(pciRadius, pciRadius * 1.12, 1);
  
  // 공 위치 갱신
  let vis = false;
  if (P && now >= P.t0 && !(hit && now >= hit.t)) {
    const p = (now - P.t0) / P.dur;
    if (p < 1.15) { bp(p, ball.position); vis = true; ball.rotation.x -= dt * 22; }
  }
  let follow = false;
  if (hit && now >= hit.t) {
    const k = (now - hit.t) / 1000 * 1.7, n = hit.path.length;
    const rawIndex = Math.min(n - 1, Math.floor(k * 60));
    const plan = hit.plan;
    if (plan && plan.throwTo) {
      const catchK = plan.i / 60, throwProgress = C((k - catchK) / plan.throwDuration, 0, 1);
      if (k < catchK) ball.position.copy(hit.path[rawIndex]);
      else ball.position.lerpVectors(hit.path[plan.i], plan.throwTo, throwProgress);
      vis = k < catchK + plan.throwDuration + 0.18;
      follow = k < catchK + plan.throwDuration + 0.35;
    } else if (plan) {
      ball.position.copy(hit.path[Math.min(rawIndex, plan.i)]);
      const catchWindow = hit.fieldOpportunity && pendingFieldingPlay ? 1.0 : 0.14;
      vis = k < plan.i / 60 + catchWindow;
      follow = k < plan.i / 60 + catchWindow + 0.14;
    } else {
      ball.position.copy(hit.path[rawIndex]);
      vis = !(hit.hr && rawIndex >= n - 1) && rawIndex < n - 1;
      follow = k < n / 60 + 0.5;
    }
    ball.rotation.x -= dt * 18;
  }
  if (defensiveThrow && now >= defensiveThrow.start) {
    const progress = C((now - defensiveThrow.start) / defensiveThrow.duration, 0, 1);
    ball.position.lerpVectors(defensiveThrow.from, defensiveThrow.to, progress);
    ball.position.y += Math.sin(progress * Math.PI) * 2.2;
    ball.rotation.x -= dt * 28;
    vis = progress < 1;
    if (progress >= 1) defensiveThrow = null;
  }
  ball.visible = vis; shd.visible = vis;
  if (vis) { shd.position.set(ball.position.x, 0.06, ball.position.z); shd.scale.setScalar(1 / (1 + ball.position.y * 0.12)); }
  
  // 카메라 워킹
  if (follow) lookT.set(ball.position.x * 0.9, Math.max(1, ball.position.y * 0.8), Math.min(ball.position.z, -6));
  else lookT.copy(DEF);
  look.lerp(lookT, 1 - Math.pow(0.02, dt));
  cam.position.set(camPos.x + (follow ? look.x * 0.08 : 0), camPos.y, camPos.z);
  cam.lookAt(look);

  ren.render(scene, cam);
  requestAnimationFrame(tick);
}

/* ---------- 이벤트 리스너 및 투수 교체 모달 ---------- */
function updatePitcherUI() {
  const p = PITCHERS[currentPitcherIdx];
  $('pitcherName').textContent = p.name;
  $('pitcherStats').textContent = `${p.formName} | 구속:${Math.round(p.speed*140)}km | 체력:${Math.round(pitcherStamina)}%`;
}

function openPitcherModal() {
  const list = $('pitcherList');
  list.innerHTML = '';
  
  PITCHERS.forEach((p, idx) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = `w-full text-left p-3 rounded-lg border transition-all ${
      idx === currentPitcherIdx 
        ? 'border-amber-400 bg-amber-400/20 text-white font-bold' 
        : 'border-slate-700 bg-slate-800/80 text-slate-200 hover:bg-slate-700'
    }`;
    btn.innerHTML = `
      <div class="flex justify-between items-center mb-1">
        <span class="font-bold ${idx === currentPitcherIdx ? 'text-amber-400' : 'text-white'}">${p.title} ${p.name}</span>
        <span class="text-xs bg-slate-900 px-2 py-0.5 rounded text-amber-300 border border-slate-700">${p.formName} · ${Math.round(p.speed*140)} km/h</span>
      </div>
      <div class="text-xs text-slate-400">${p.desc}</div>
      <div class="text-[10px] text-emerald-300 mt-1">사용 구종: ${p.pitches.map(i => TYPES[i].name).join(' · ')}</div>
    `;
    btn.onclick = () => { 
      currentPitcherIdx = idx;
      pitcherStamina = 100;
      if (!p.pitches.includes(S.pt)) S.pt = p.pitches[0];
      updatePitcherUI(); 
      refreshPitchButtons(); updateStatsUI();
      $('pitcherModal').hidden = true; 
      $('pitcherModal').style.display = 'none';
    };
    list.appendChild(btn);
  });
  
  $('pitcherModal').hidden = false;
  $('pitcherModal').style.display = 'flex';
}

stage.addEventListener('pointerdown', e => {
  // 시작 설정 오버레이 안의 입력·버튼 클릭은 경기 캔버스 조작으로 전달하지 않습니다.
  if (e.target.closest('#ov, #gameHud, #absPanel, #timingWrap, button, input, select, textarea, label')) return;
  e.preventDefault();
  if (attemptHighlightCatch()) return;
  if (S.mode === 'pitch' && S.phase === 'aim') {
    aimAt(e);
    if (!window.matchMedia('(pointer: coarse)').matches) act();
  } else if (S.mode === 'bat' && pciEnabled && S.phase === 'aim') aimAt(e);
  else act();
});
stage.addEventListener('pointermove', e => { if ((S.mode === 'pitch' || (S.mode === 'bat' && pciEnabled)) && S.phase === 'aim') aimAt(e); });

$('types').addEventListener('click', e => { const b = e.target.closest('button'); if (b) { setPT(+b.dataset.i); b.blur(); } });
$('mobileAct').addEventListener('click', () => act());
$('mobileSteal').addEventListener('click', useSprintAction);
$('buntBtn').addEventListener('click', toggleBunt);
$('pciBtn').addEventListener('click', togglePCI);
document.querySelectorAll('#battingModeChoices [data-batting-mode]').forEach(button => button.addEventListener('click', () => setBattingMode(button.dataset.battingMode)));
$('changePitcherBtn').addEventListener('click', openPitcherModal);
$('closePitcherModal').addEventListener('click', () => { 
  $('pitcherModal').hidden = true; 
  $('pitcherModal').style.display = 'none';
});

$('go').addEventListener('click', () => { start('bat'); });
$('go2').addEventListener('click', () => { start('pitch'); });
document.querySelectorAll('#stadiumChoices .stadium-choice').forEach(button => {
  button.addEventListener('click', () => applyStadium(Number(button.dataset.stadium)));
});
document.querySelectorAll('#difficultyChoices [data-difficulty]').forEach(button => button.addEventListener('click', () => {
  difficulty = button.dataset.difficulty;
  document.querySelectorAll('#difficultyChoices [data-difficulty]').forEach(b => b.classList.toggle('on', b === button));
}));
document.querySelectorAll('#inningChoices [data-innings]').forEach(button => button.addEventListener('click', () => {
  maxInnings = Number(button.dataset.innings);
  document.querySelectorAll('#inningChoices [data-innings]').forEach(b => b.classList.toggle('on', b === button));
  drawScoreboard();
}));
document.querySelectorAll('#batterSideChoices [data-batside]').forEach(button => button.addEventListener('click', () => setBatterSide(button.dataset.batside)));
$('challengeBtn').addEventListener('click', challengeABS);

addEventListener('keydown', e => {
  if (e.target instanceof HTMLElement && (e.target.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName))) return;
  if (e.code === 'ShiftLeft' || e.code === 'ShiftRight') { e.preventDefault(); if (!e.repeat) { if (S.mode === 'bat') togglePCI(); else beginPitchCharge(); } }
  else if (e.code === 'Space') { if (e.target instanceof HTMLElement && e.target.tagName === 'BUTTON') return; e.preventDefault(); if (!e.repeat) act(); }
  else if (e.code === 'KeyS') useSprintAction();
  else if (e.code === 'KeyB' && !e.repeat) toggleBunt();
  else if (S.mode === 'pitch' && S.phase === 'aim') {
    if (e.key >= '1' && e.key <= '7') setPT(+e.key - 1);
    const m = { ArrowLeft: [-0.04, 0], ArrowRight: [0.04, 0], ArrowUp: [0, 0.04], ArrowDown: [0, -0.04] }[e.key];
    if (m) { e.preventDefault(); aim.x = C(aim.x + m[0], -0.5, 0.5); aim.y = C(aim.y + m[1], 0.3, 1.4); }
  }
});
addEventListener('keyup', e => {
  if ((e.code === 'ShiftLeft' || e.code === 'ShiftRight') && pitchCharge) { e.preventDefault(); releasePitchCharge(); }
});
addEventListener('blur', cancelPitchCharge);

updatePitcherUI();
initABSGrid();
board();
requestAnimationFrame(tick);
})();
</script>
</body>
</html>'''
components.html(GAME_HTML, height=1050, scrolling=True)





