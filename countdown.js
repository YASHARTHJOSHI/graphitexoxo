/**
 * GRAPHITE '26 — MAIN EVENT COUNTDOWN TERMINAL
 * Live countdown from now to 27 October 2026, 10:00:00 AM IST.
 * Bottom-left START button launches the 24h 30m hackathon countdown in a new tab.
 */

function initCountdownTerminal() {
  const daysValEl = document.getElementById('daysVal');
  const hoursValEl = document.getElementById('hoursVal');
  const minsValEl = document.getElementById('minsVal');
  const secsValEl = document.getElementById('secsVal');

  const missionStatusBadge = document.getElementById('missionStatusBadge');
  const missionStatusText = document.getElementById('missionStatusText');
  const terminalHeading = document.getElementById('terminalHeading');
  const arenaStartBtn = document.getElementById('arenaStartBtn');
  const arenaStartLabel = document.getElementById('arenaStartLabel');
  const finishOverlay = document.getElementById('finishOverlay');
  const countdownBgVideo = document.getElementById('countdownBgVideo');

  // Target: 27 October 2026, 10:00:00 AM Indian Standard Time (IST = UTC+05:30)
  const TARGET_LAUNCH_DATE_MS = new Date('2026-10-27T10:00:00+05:30').getTime();

  let audioEnabled = true;

  // Web Audio Synthesizer
  let audioCtx = null;
  function getAudioContext() {
    if (!audioCtx) {
      const AudioCtxClass = window.AudioContext || window.webkitAudioContext;
      if (AudioCtxClass) audioCtx = new AudioCtxClass();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    return audioCtx;
  }

  function playTone(freq = 880, duration = 0.2, type = 'sine') {
    if (!audioEnabled) return;
    try {
      const ctx = getAudioContext();
      if (!ctx) return;
      const now = ctx.currentTime;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, now);
      gain.gain.setValueAtTime(0.18, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + duration);
    } catch (e) {}
  }

  function pad(num) {
    return String(Math.max(0, Math.floor(num))).padStart(2, '0');
  }

  // ==========================================
  // CLOCK ENGINE: LIVE TO 27 OCT 2026, 10:00 AM IST
  // ==========================================
  function updateClockEngine() {
    const now = Date.now();
    const diff = TARGET_LAUNCH_DATE_MS - now;

    if (diff > 0) {
      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hrs = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const secs = Math.floor((diff % (1000 * 60)) / 1000);

      if (daysValEl) daysValEl.textContent = pad(days);
      if (hoursValEl) hoursValEl.textContent = pad(hrs);
      if (minsValEl) minsValEl.textContent = pad(mins);
      if (secsValEl) secsValEl.textContent = pad(secs);

      document.title = `${pad(days)}d ${pad(hrs)}h ${pad(mins)}m ${pad(secs)}s — GRAPHITE '26`;
    } else {
      if (daysValEl) daysValEl.textContent = '00';
      if (hoursValEl) hoursValEl.textContent = '00';
      if (minsValEl) minsValEl.textContent = '00';
      if (secsValEl) secsValEl.textContent = '00';
      document.title = '00:00:00 — GRAPHITE \'26';
    }

    if (terminalHeading) {
      terminalHeading.textContent = 'ROUND 2 ARENA // HACKATHON COUNTDOWN';
    }
    if (missionStatusBadge && missionStatusText) {
      missionStatusBadge.className = 'hud-status-badge status-running';
      missionStatusText.textContent = 'LIVE COUNTDOWN';
    }
    if (finishOverlay) {
      finishOverlay.style.display = 'none';
    }
  }

  // ==========================================
  // START BUTTON: OPENS 24H 30M COUNTDOWN IN A NEW TAB
  // ==========================================
  function launchArenaNewTab() {
    const startTime = Date.now();
    try {
      localStorage.setItem('graphite_arena_seq_start', String(startTime));
    } catch (e) {}

    playTone(660, 0.15, 'sine');
    setTimeout(() => playTone(990, 0.25, 'sine'), 130);

    // Open another countdown of 24 hrs 30 min in a different tab
    window.open('arena.html?start=' + startTime, '_blank');
  }

  if (arenaStartBtn) {
    arenaStartBtn.className = 'btn-arena-start';
    arenaStartBtn.disabled = false;
    if (arenaStartLabel) arenaStartLabel.textContent = 'START';
    arenaStartBtn.addEventListener('click', launchArenaNewTab);
  }

  // Fullscreen Projector Toggle (Key F)
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) document.exitFullscreen().catch(() => {});
    }
  }

  // Keyboard Shortcuts (Space opens arena, F for fullscreen)
  window.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

    if (e.code === 'Space') {
      e.preventDefault();
      launchArenaNewTab();
    } else if (e.code === 'KeyF') {
      e.preventDefault();
      toggleFullscreen();
    }
  });

  // Background Video Init
  if (countdownBgVideo) {
    countdownBgVideo.muted = true;
    countdownBgVideo.defaultMuted = true;
    countdownBgVideo.playsInline = true;
    countdownBgVideo.play().catch(() => {
      const resume = () => {
        countdownBgVideo.play().catch(() => {});
        window.removeEventListener('pointerdown', resume);
        window.removeEventListener('keydown', resume);
      };
      window.addEventListener('pointerdown', resume, { once: true });
      window.addEventListener('keydown', resume, { once: true });
    });
  }

  // Run immediately & start interval loop
  updateClockEngine();
  setInterval(updateClockEngine, 250);

  // Ambient Particles Canvas
  const canvas = document.getElementById('timerParticleCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const particles = Array.from({ length: 30 }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.35,
      vy: -Math.random() * 0.5 - 0.2,
      size: Math.random() * 2 + 1,
      color: Math.random() > 0.5 ? 'rgba(0, 210, 255,' : 'rgba(255, 183, 3,',
      alpha: Math.random() * 0.45 + 0.15
    }));

    function animateParticles() {
      ctx.clearRect(0, 0, width, height);

      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;

        if (p.y < 0) {
          p.y = height;
          p.x = Math.random() * width;
        }
        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;

        ctx.fillStyle = `${p.color} ${p.alpha})`;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
      });

      requestAnimationFrame(animateParticles);
    }
    animateParticles();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initCountdownTerminal);
} else {
  initCountdownTerminal();
}
