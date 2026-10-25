/**
 * GRAPHITE '26 — ARENA LIVE HACKATHON COUNTDOWN CONTROLLER (24 HRS 30 MIN)
 * Phase 1: 30-Minute Opening Briefing (1800s)
 * Phase 2: 24-Hour Hackathon Arena Sprint (86400s) [Starts immediately after 30 mins]
 */

function initArenaCountdown() {
  const daysValEl = document.getElementById('daysVal');
  const hoursValEl = document.getElementById('hoursVal');
  const minsValEl = document.getElementById('minsVal');
  const secsValEl = document.getElementById('secsVal');

  const missionStatusBadge = document.getElementById('missionStatusBadge');
  const missionStatusText = document.getElementById('missionStatusText');
  const terminalHeading = document.getElementById('terminalHeading');
  const arenaStatusLabel = document.getElementById('arenaStatusLabel');
  const finishOverlay = document.getElementById('finishOverlay');
  const countdownBgVideo = document.getElementById('countdownBgVideo');

  const BRIEFING_DURATION_SECS = 30 * 60; // 1,800 seconds (30 mins)
  const HACKATHON_DURATION_SECS = 24 * 60 * 60; // 86,400 seconds (24 hrs)
  const TOTAL_DURATION_SECS = BRIEFING_DURATION_SECS + HACKATHON_DURATION_SECS; // 88,200 seconds

  const STORAGE_KEY_START = 'graphite_arena_seq_start';

  // Read start time from URL query or localStorage, or initialize fresh now
  let arenaStartTime = null;
  const urlParams = new URLSearchParams(window.location.search);
  const paramStart = urlParams.get('start');

  if (paramStart) {
    const parsedParam = parseInt(paramStart, 10);
    if (!isNaN(parsedParam)) {
      arenaStartTime = parsedParam;
      try {
        localStorage.setItem(STORAGE_KEY_START, String(arenaStartTime));
      } catch (e) {}
    }
  }

  if (!arenaStartTime) {
    try {
      const stored = localStorage.getItem(STORAGE_KEY_START);
      if (stored) {
        const parsedStored = parseInt(stored, 10);
        const elapsed = Math.floor((Date.now() - parsedStored) / 1000);
        if (elapsed >= 0 && elapsed < TOTAL_DURATION_SECS) {
          arenaStartTime = parsedStored;
        }
      }
    } catch (e) {}
  }

  // If still not set or expired, start from current instant
  if (!arenaStartTime) {
    arenaStartTime = Date.now();
    try {
      localStorage.setItem(STORAGE_KEY_START, String(arenaStartTime));
    } catch (e) {}
  }

  let audioEnabled = true;
  let lastSecondTicked = -1;
  let lastPhaseLogged = null;

  // Web Audio Synthesizer for chimes
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
  // ARENA SEQUENCE CLOCK ENGINE
  // ==========================================
  function updateArenaClock() {
    const now = Date.now();
    const totalElapsedSecs = Math.max(0, Math.floor((now - arenaStartTime) / 1000));

    // ------------------------------------------
    // PHASE 1: 30-MINUTE OPENING BRIEFING (0 to 1800s)
    // ------------------------------------------
    if (totalElapsedSecs < BRIEFING_DURATION_SECS) {
      const remainingSecs = BRIEFING_DURATION_SECS - totalElapsedSecs;
      const mins = Math.floor(remainingSecs / 60);
      const secs = remainingSecs % 60;

      if (daysValEl) daysValEl.textContent = '00';
      if (hoursValEl) hoursValEl.textContent = '00';
      if (minsValEl) minsValEl.textContent = pad(mins);
      if (secsValEl) secsValEl.textContent = pad(secs);

      if (terminalHeading) {
        terminalHeading.textContent = 'PHASE 1 // 30-MINUTE OPENING BRIEFING';
      }

      if (missionStatusBadge && missionStatusText) {
        missionStatusBadge.className = 'hud-status-badge status-running';
        missionStatusText.textContent = '30M BRIEFING COUNTDOWN';
      }

      if (arenaStatusLabel) {
        arenaStatusLabel.textContent = 'BRIEFING RUNNING';
      }

      // Audio tick on final 10 seconds of 30-min phase
      if (remainingSecs <= 10 && secs !== lastSecondTicked) {
        lastSecondTicked = secs;
        playTone(920, 0.08, 'sine');
      }

      document.title = `${pad(mins)}m ${pad(secs)}s [30M Briefing] — GRAPHITE '26`;
      lastPhaseLogged = 'phase1';
      return;
    }

    // ------------------------------------------
    // PHASE 2: 24-HOUR HACKATHON SPRINT (1800s to 88200s)
    // Immediately begins as soon as 30 mins complete!
    // ------------------------------------------
    const hackathonElapsedSecs = totalElapsedSecs - BRIEFING_DURATION_SECS;

    if (hackathonElapsedSecs < HACKATHON_DURATION_SECS) {
      const remainingSecs = HACKATHON_DURATION_SECS - hackathonElapsedSecs;
      const days = 0;
      const hrs = Math.floor(remainingSecs / 3600);
      const mins = Math.floor((remainingSecs % 3600) / 60);
      const secs = remainingSecs % 60;

      // Transition Fanfare Chime when switching from 30m briefing to 24h hackathon!
      if (lastPhaseLogged === 'phase1') {
        playTone(660, 0.2, 'sine');
        setTimeout(() => playTone(880, 0.25, 'sine'), 160);
        setTimeout(() => playTone(1175, 0.5, 'sine'), 340);
      }
      lastPhaseLogged = 'phase2';

      if (daysValEl) daysValEl.textContent = pad(days);
      if (hoursValEl) hoursValEl.textContent = pad(hrs);
      if (minsValEl) minsValEl.textContent = pad(mins);
      if (secsValEl) secsValEl.textContent = pad(secs);

      if (terminalHeading) {
        terminalHeading.textContent = 'ROUND 2 ARENA // 24-HOUR HACKATHON SPRINT';
      }

      if (missionStatusBadge && missionStatusText) {
        missionStatusBadge.className = 'hud-status-badge status-running';
        missionStatusText.textContent = 'LIVE COUNTDOWN';
      }

      if (arenaStatusLabel) {
        arenaStatusLabel.textContent = 'HACKATHON LIVE';
      }

      // Audio tick on final 10 seconds of 24 hours
      if (remainingSecs <= 10 && secs !== lastSecondTicked) {
        lastSecondTicked = secs;
        playTone(920, 0.08, 'sine');
      }

      document.title = `${pad(hrs)}h ${pad(mins)}m ${pad(secs)}s [24H Hackathon Live] — GRAPHITE '26`;
      return;
    }

    // ------------------------------------------
    // PHASE 3: 24 HOURS OVER — HACKATHON COMPLETE
    // ------------------------------------------
    if (daysValEl) daysValEl.textContent = '00';
    if (hoursValEl) hoursValEl.textContent = '00';
    if (minsValEl) minsValEl.textContent = '00';
    if (secsValEl) secsValEl.textContent = '00';

    if (terminalHeading) {
      terminalHeading.textContent = 'ROUND 2 ARENA // 24-HOUR SPRINT COMPLETE';
    }

    if (missionStatusBadge && missionStatusText) {
      missionStatusBadge.className = 'hud-status-badge status-complete';
      missionStatusText.textContent = 'HACKATHON CONCLUDED // TIME OVER';
    }

    if (arenaStatusLabel) {
      arenaStatusLabel.textContent = 'CONCLUDED';
    }

    if (finishOverlay) {
      finishOverlay.style.display = 'flex';
    }

    document.title = '00:00:00 [HACKATHON COMPLETE] — GRAPHITE \'26';
  }

  // Fullscreen Projector Toggle
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) document.exitFullscreen().catch(() => {});
    }
  }

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

  // Keyboard Shortcuts (F for Fullscreen, Shift+T, Shift+H, Shift+R for Organizer Testing)
  window.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

    if (e.code === 'KeyF') {
      e.preventDefault();
      toggleFullscreen();
    } else if (e.code === 'KeyT' && e.shiftKey) {
      // Fast forward to 5 seconds before 30-minute briefing ends
      e.preventDefault();
      arenaStartTime = Date.now() - ((BRIEFING_DURATION_SECS - 5) * 1000);
      try { localStorage.setItem(STORAGE_KEY_START, String(arenaStartTime)); } catch (err) {}
      updateArenaClock();
    } else if (e.code === 'KeyH' && e.shiftKey) {
      // Fast forward to 5 seconds before 24-hour sprint ends
      e.preventDefault();
      arenaStartTime = Date.now() - ((TOTAL_DURATION_SECS - 5) * 1000);
      try { localStorage.setItem(STORAGE_KEY_START, String(arenaStartTime)); } catch (err) {}
      updateArenaClock();
    } else if (e.code === 'KeyR' && e.shiftKey) {
      // Restart sequence from 0
      e.preventDefault();
      arenaStartTime = Date.now();
      try { localStorage.setItem(STORAGE_KEY_START, String(arenaStartTime)); } catch (err) {}
      lastPhaseLogged = null;
      lastSecondTicked = -1;
      if (finishOverlay) finishOverlay.style.display = 'none';
      playTone(440, 0.2, 'sine');
      updateArenaClock();
    }
  });

  // Run immediately & start interval loop
  updateArenaClock();
  setInterval(updateArenaClock, 250);

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
  document.addEventListener('DOMContentLoaded', initArenaCountdown);
} else {
  initArenaCountdown();
}
