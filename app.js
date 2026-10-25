/**
 * GRAPHITE '26 — AAA GAME MENU & DEDICATED MISSION PAGES CONTROLLER
 * Inspired by Marvel's Spider-Man 2 & Insomniac Game Interfaces
 */

document.addEventListener('DOMContentLoaded', () => {
  // ==========================================
  // 1. DATA CONFIGURATION & ROUTE ARCHITECTURE
  // ==========================================
  const MENU_ITEMS_DATA = [
    {
      id: 'start',
      route: 'start',
      pageId: 'hub-start',
      bgImage: 'assets/reference_spiderman_codes.png',
      title: 'START HACKATHON'
    },
    {
      id: 'story',
      route: 'story',
      pageId: 'hub-story',
      bgImage: 'assets/reference_room_coding.jpg',
      title: 'STORY MODE'
    },
    {
      id: 'press',
      route: 'press',
      pageId: 'hub-press',
      bgImage: 'assets/reference_spiderman_editorial.jpg',
      title: 'DAILY BUGLE PRESS PASS'
    },
    {
      id: 'crunch',
      route: 'crunch',
      pageId: 'hub-crunch',
      bgImage: 'assets/reference_spiderman_surprised.jpg',
      title: 'CRUNCH MODE // LOAD STATE'
    },
    {
      id: 'chill',
      route: 'chill',
      pageId: 'hub-chill',
      bgImage: 'assets/reference_spiderman_web.jpg',
      title: 'CHILL ZONE // WEB HAMMOCK'
    },
    {
      id: 'countdown',
      action: 'open-countdown',
      bgImage: 'assets/reference_spiderman_codes.png',
      title: 'HACKATHON COUNTDOWN'
    },
    {
      id: 'exit',
      action: 'exit-console',
      bgImage: 'assets/reference_spiderman_codes.png',
      title: 'EXIT CONSOLE'
    }
  ];

  const ROUTE_CONFIG = {
    '': { pageId: null, parent: null, bgImage: 'assets/reference_spiderman_codes.png', index: 0 },
    
    // Category 01: Start Hackathon
    'start': { pageId: 'hub-start', parent: '', bgImage: 'assets/reference_spiderman_codes.png', index: 0 },
    'start/about-graphite': { pageId: 'page-start-about', parent: 'start', bgImage: 'assets/reference_spiderman_codes.png', index: 0 },
    'start/registration': { pageId: 'page-start-registration', parent: 'start', bgImage: 'assets/reference_spiderman_codes.png', index: 0 },
    'start/team-formation': { pageId: 'page-start-team', parent: 'start', bgImage: 'assets/reference_spiderman_codes.png', index: 0 },
    'start/round-1': { pageId: 'page-start-round1', parent: 'start', bgImage: 'assets/reference_spiderman_codes.png', index: 0 },
    'start/tracks': { pageId: 'page-start-tracks', parent: 'start', bgImage: 'assets/reference_spiderman_codes.png', index: 0 },
    'start/round-2': { pageId: 'page-start-round2', parent: 'start', bgImage: 'assets/reference_spiderman_codes.png', index: 0 },
    'start/ppt-template': { pageId: 'page-start-template', parent: 'start', bgImage: 'assets/reference_spiderman_codes.png', index: 0 },

    // Category 02: Story Mode
    'story': { pageId: 'hub-story', parent: '', bgImage: 'assets/reference_room_coding.jpg', index: 1 },
    'story/origin': { pageId: 'page-story-origin', parent: 'story', bgImage: 'assets/reference_room_coding.jpg', index: 1 },
    'story/spider-verse': { pageId: 'page-story-verse', parent: 'story', bgImage: 'assets/reference_room_coding.jpg', index: 1 },
    'story/journey': { pageId: 'page-story-journey', parent: 'story', bgImage: 'assets/reference_room_coding.jpg', index: 1 },
    'story/mission-objective': { pageId: 'page-story-objective', parent: 'story', bgImage: 'assets/reference_room_coding.jpg', index: 1 },
    'story/beyond-graphite': { pageId: 'page-story-beyond', parent: 'story', bgImage: 'assets/reference_room_coding.jpg', index: 1 },

    // Category 03: Daily Bugle Press Pass
    'press': { pageId: 'hub-press', parent: '', bgImage: 'assets/reference_spiderman_editorial.jpg', index: 2 },
    'press/announcements': { pageId: 'page-press-announcements', parent: 'press', bgImage: 'assets/reference_spiderman_editorial.jpg', index: 2 },
    'press/prizes': { pageId: 'page-press-prizes', parent: 'press', bgImage: 'assets/reference_spiderman_editorial.jpg', index: 2 },
    'press/mentorship': { pageId: 'page-press-mentors', parent: 'press', bgImage: 'assets/reference_spiderman_editorial.jpg', index: 2 },
    'press/official-channels': { pageId: 'page-press-channels', parent: 'press', bgImage: 'assets/reference_spiderman_editorial.jpg', index: 2 },

    // Category 04: Crunch Mode // Load State
    'crunch': { pageId: 'hub-crunch', parent: '', bgImage: 'assets/reference_spiderman_surprised.jpg', index: 3 },
    'crunch/timeline': { pageId: 'page-crunch-timeline', parent: 'crunch', bgImage: 'assets/reference_spiderman_surprised.jpg', index: 3 },
    'crunch/judging': { pageId: 'page-crunch-judging', parent: 'crunch', bgImage: 'assets/reference_spiderman_surprised.jpg', index: 3 },
    'crunch/submission': { pageId: 'page-crunch-submission', parent: 'crunch', bgImage: 'assets/reference_spiderman_surprised.jpg', index: 3 },
    'crunch/git-protocol': { pageId: 'page-crunch-git', parent: 'crunch', bgImage: 'assets/reference_spiderman_surprised.jpg', index: 3 },
    'crunch/preflight': { pageId: 'page-crunch-preflight', parent: 'crunch', bgImage: 'assets/reference_spiderman_surprised.jpg', index: 3 },
    'crunch/faq': { pageId: 'page-crunch-faq', parent: 'crunch', bgImage: 'assets/reference_spiderman_surprised.jpg', index: 3 },

    // Category 05: Chill Zone // Web Hammock
    'chill': { pageId: 'hub-chill', parent: '', bgImage: 'assets/reference_spiderman_web.jpg', index: 4 },
    'chill/workshops': { pageId: 'page-chill-workshops', parent: 'chill', bgImage: 'assets/reference_spiderman_web.jpg', index: 4 },
    'chill/venue': { pageId: 'page-chill-venue', parent: 'chill', bgImage: 'assets/reference_spiderman_web.jpg', index: 4 },
    'chill/facilities': { pageId: 'page-chill-facilities', parent: 'chill', bgImage: 'assets/reference_spiderman_web.jpg', index: 4 },
    'chill/packing-list': { pageId: 'page-chill-packing', parent: 'chill', bgImage: 'assets/reference_spiderman_web.jpg', index: 4 },
    'chill/community': { pageId: 'page-chill-community', parent: 'chill', bgImage: 'assets/reference_spiderman_web.jpg', index: 4 },
    'chill/contact': { pageId: 'page-chill-contact', parent: 'chill', bgImage: 'assets/reference_spiderman_web.jpg', index: 4 }
  };

  // ==========================================
  // 2. DOM REFERENCES
  // ==========================================
  const bgLayerA = document.getElementById('bgLayerA');
  const bgLayerB = document.getElementById('bgLayerB');
  const mainMenuShell = document.getElementById('mainMenuShell');
  const menuItems = Array.from(document.querySelectorAll('.menu-item'));
  const activePill = document.getElementById('activePill');

  const pagesContainer = document.getElementById('pagesContainer');
  const detailPages = Array.from(document.querySelectorAll('.detail-page'));

  // Exit Modal Elements
  const exitModalOverlay = document.getElementById('exitModalOverlay');
  const cancelExitModalBtn = document.getElementById('cancelExitModalBtn');
  const confirmExitModalBtn = document.getElementById('confirmExitModalBtn');
  const exitModalBackdrop = document.getElementById('exitModalBackdrop');

  const systemClock = document.getElementById('systemClock');
  const soundToggle = document.getElementById('soundToggle');
  const soundLabel = document.getElementById('soundLabel');
  const iconSoundOn = soundToggle ? soundToggle.querySelector('.icon-sound.on') : null;
  const iconSoundOff = soundToggle ? soundToggle.querySelector('.icon-sound.off') : null;
  const fsToggle = document.getElementById('fsToggle');
  const gameToast = document.getElementById('gameToast');

  // Interactive buttons
  const pageCopySpecsBtn = document.getElementById('pageCopySpecsBtn');
  const refillCoffeeBtn = document.getElementById('refillCoffeeBtn');
  const summonMentorBtn = document.getElementById('summonMentorBtn');
  const rollbackCommitBtn = document.getElementById('rollbackCommitBtn');
  const chillLoFiBtn = document.getElementById('chillLoFiBtn');
  const chillLoFiLabel = document.getElementById('chillLoFiLabel');
  const bgMusic = document.getElementById('bgMusic');
  if (bgMusic) {
    bgMusic.volume = 0.35;
    bgMusic.pause();
    bgMusic.currentTime = 0;
  }

  // Mission Transition HUD Elements
  const missionTransitionScreen = document.getElementById('missionTransitionScreen');
  const transVideo = document.getElementById('transVideo');
  const transBadgeText = document.getElementById('transBadgeText');
  const transDestTitle = document.getElementById('transDestTitle');
  const transDestSub = document.getElementById('transDestSub');
  const transStatusPhase = document.getElementById('transStatusPhase');
  const transStatusDetail = document.getElementById('transStatusDetail');
  const transCircleFill = document.getElementById('transCircleFill');
  const transPctValue = document.getElementById('transPctValue');
  const transDockRight = document.getElementById('transDockRight');
  const transSkipBtn = document.getElementById('transSkipBtn');

  // Sub-Page Gentle 1-Second Fade Transition Overlay
  const subpageFadeOverlay = document.getElementById('subpageFadeOverlay');
  let isSubTransitioning = false;

  // Spiderweb FX Layer
  const spiderwebFxLayer = document.getElementById('spiderwebFxLayer');

  // State
  let currentIndex = 0;
  let currentLayer = 'A';
  let currentRoute = '';
  let isExitModalOpen = false;
  let audioEnabled = true;
  let audioCtx = null;
  let toastTimer = null;
  let loFiPlaying = false;
  let loFiOscillators = [];

  // ==========================================
  // 3. SYNTHESIZED WEB AUDIO ENGINE
  // ==========================================
  function initAudio() {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) {
        audioCtx = new AudioContextClass();
      }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
  }

  function playHoverSound() {
    if (!audioEnabled) return;
    try {
      initAudio();
      if (!audioCtx) return;
      const now = audioCtx.currentTime;
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();

      osc.type = 'triangle';
      osc.frequency.setValueAtTime(1400, now);
      osc.frequency.exponentialRampToValueAtTime(2200, now + 0.04);

      gain.gain.setValueAtTime(0.045, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);

      osc.connect(gain);
      gain.connect(audioCtx.destination);

      osc.start(now);
      osc.stop(now + 0.045);
    } catch (e) {}
  }

  function playLaunchSound() {
    if (!audioEnabled) return;
    try {
      initAudio();
      if (!audioCtx) return;
      const now = audioCtx.currentTime;

      const subOsc = audioCtx.createOscillator();
      const subGain = audioCtx.createGain();
      subOsc.type = 'sine';
      subOsc.frequency.setValueAtTime(280, now);
      subOsc.frequency.exponentialRampToValueAtTime(50, now + 0.28);
      subGain.gain.setValueAtTime(0.2, now);
      subGain.gain.exponentialRampToValueAtTime(0.001, now + 0.28);
      subOsc.connect(subGain);
      subGain.connect(audioCtx.destination);
      subOsc.start(now);
      subOsc.stop(now + 0.28);

      const chimeOsc = audioCtx.createOscillator();
      const chimeGain = audioCtx.createGain();
      chimeOsc.type = 'sine';
      chimeOsc.frequency.setValueAtTime(440, now);
      chimeOsc.frequency.exponentialRampToValueAtTime(880, now + 0.15);
      chimeGain.gain.setValueAtTime(0.08, now);
      chimeGain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
      chimeOsc.connect(chimeGain);
      chimeGain.connect(audioCtx.destination);
      chimeOsc.start(now);
      chimeOsc.stop(now + 0.15);
    } catch (e) {}
  }

  function playBackSound() {
    if (!audioEnabled) return;
    try {
      initAudio();
      if (!audioCtx) return;
      const now = audioCtx.currentTime;
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(650, now);
      osc.frequency.exponentialRampToValueAtTime(320, now + 0.16);
      gain.gain.setValueAtTime(0.08, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.16);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.16);
    } catch (e) {}
  }

  function playThwipSound() {
    if (!audioEnabled) return;
    try {
      initAudio();
      if (!audioCtx) return;
      const now = audioCtx.currentTime;

      // 1. High-tension web string snap (frequency plunge)
      const osc = audioCtx.createOscillator();
      const oscGain = audioCtx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(1750, now);
      osc.frequency.exponentialRampToValueAtTime(160, now + 0.12);
      oscGain.gain.setValueAtTime(0.18, now);
      oscGain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
      osc.connect(oscGain);
      oscGain.connect(audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.13);

      // 2. High-pressure web spray noise burst
      const bufferSize = Math.floor(audioCtx.sampleRate * 0.09);
      const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
      const output = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        output[i] = Math.random() * 2 - 1;
      }
      const whiteNoise = audioCtx.createBufferSource();
      whiteNoise.buffer = buffer;

      const filter = audioCtx.createBiquadFilter();
      filter.type = 'bandpass';
      filter.frequency.setValueAtTime(3600, now);
      filter.frequency.exponentialRampToValueAtTime(700, now + 0.09);
      filter.Q.setValueAtTime(3.2, now);

      const noiseGain = audioCtx.createGain();
      noiseGain.gain.setValueAtTime(0.22, now);
      noiseGain.gain.exponentialRampToValueAtTime(0.001, now + 0.09);

      whiteNoise.connect(filter);
      filter.connect(noiseGain);
      noiseGain.connect(audioCtx.destination);
      whiteNoise.start(now);
    } catch (e) {}
  }

  function spawnSpiderwebBurst(x, y) {
    if (!spiderwebFxLayer) return;
    playThwipSound();

    const burst = document.createElement('div');
    burst.className = 'web-splat-burst';
    burst.style.left = `${x}px`;
    burst.style.top = `${y}px`;

    burst.innerHTML = `
      <svg class="web-splat-svg" viewBox="0 0 100 100" fill="none" stroke="currentColor">
        <line x1="50" y1="50" x2="50" y2="2" stroke-width="2.5" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="84" y2="16" stroke-width="2" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="98" y2="50" stroke-width="2.5" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="84" y2="84" stroke-width="2" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="50" y2="98" stroke-width="2.5" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="16" y2="84" stroke-width="2" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="2" y2="50" stroke-width="2.5" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="16" y2="16" stroke-width="2" stroke-linecap="round"/>
        <polygon points="50,14 75,25 86,50 75,75 50,86 25,75 14,50 25,25" stroke-width="1.8" fill="rgba(255,255,255,0.06)"/>
        <polygon points="50,28 66,34 72,50 66,66 50,72 34,66 28,50 34,34" stroke-width="1.6" fill="rgba(255,42,59,0.12)"/>
        <polygon points="50,39 58,42 61,50 58,58 50,61 42,58 39,50 42,42" stroke-width="1.4"/>
        <circle cx="50" cy="50" r="4.5" fill="#ffffff" stroke="#ff2a3b" stroke-width="2"/>
      </svg>
      <div class="web-splat-ripple"></div>
    `;

    spiderwebFxLayer.appendChild(burst);

    setTimeout(() => {
      if (burst.parentNode) {
        burst.parentNode.removeChild(burst);
      }
    }, 600);
  }

  let bgmAutoStarted = false;
  let bgmRetryInterval = null;

  function startBgMusic() {
    // STRICT RULE: Music must ONLY play AFTER intro video has fully finished!
    if (!loadingFinished || !audioEnabled || !bgMusic) return;
    initAudio();

    bgMusic.volume = 0.35;
    bgMusic.muted = false;

    try {
      const playPromise = bgMusic.play();
      if (playPromise !== undefined) {
        playPromise.then(() => {
          bgmAutoStarted = true;
          if (bgmRetryInterval) {
            clearInterval(bgmRetryInterval);
            bgmRetryInterval = null;
          }
          if (iconSoundOn) iconSoundOn.style.display = 'block';
          if (iconSoundOff) iconSoundOff.style.display = 'none';
        }).catch(() => {
          // If browser temporarily blocks unmuted autoplay without prior gesture,
          // rapidly poll every 100ms so it starts the microsecond any interaction or focus occurs
          if (!bgmRetryInterval && !bgmAutoStarted) {
            let attempts = 0;
            bgmRetryInterval = setInterval(() => {
              attempts++;
              if (bgmAutoStarted || !audioEnabled || attempts > 60) {
                clearInterval(bgmRetryInterval);
                bgmRetryInterval = null;
                return;
              }
              initAudio();
              bgMusic.play().then(() => {
                bgmAutoStarted = true;
                if (bgmRetryInterval) {
                  clearInterval(bgmRetryInterval);
                  bgmRetryInterval = null;
                }
              }).catch(() => {});
            }, 100);
          }
        });
      }
    } catch (e) {}
  }

  function toggleLoFiSound() {
    initAudio();
    if (!audioCtx) return;

    if (loFiPlaying) {
      loFiOscillators.forEach(node => {
        try { node.stop(); } catch(e){}
      });
      loFiOscillators = [];
      loFiPlaying = false;
      if (chillLoFiLabel) chillLoFiLabel.textContent = 'PLAY CHILL AMBIENCE';
      if (bgMusic) bgMusic.volume = 0.35;
      showToast('Lo-Fi Ambience stopped.');
    } else {
      if (bgMusic) bgMusic.volume = 0.12;
      const freqs = [110, 130.81, 164.81, 196.00, 246.94];
      const masterGain = audioCtx.createGain();
      masterGain.gain.setValueAtTime(0.04, audioCtx.currentTime);

      const filter = audioCtx.createBiquadFilter();
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(450, audioCtx.currentTime);

      masterGain.connect(filter);
      filter.connect(audioCtx.destination);

      loFiOscillators = [];
      freqs.forEach(freq => {
        const osc = audioCtx.createOscillator();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        osc.connect(masterGain);
        osc.start();
        loFiOscillators.push(osc);
      });

      loFiPlaying = true;
      if (chillLoFiLabel) chillLoFiLabel.textContent = 'STOP CHILL AMBIENCE';
      showToast('🎧 Himalayan Lo-Fi Synthesizer Active.');
    }
  }

  // ==========================================
  // 4. PRELOAD ASSETS WITH ASYNC DECODE
  // ==========================================
  const preloadedImages = {};
  MENU_ITEMS_DATA.forEach(item => {
    if (item.bgImage && !preloadedImages[item.bgImage]) {
      const img = new Image();
      img.src = item.bgImage;
      if (img.decode) {
        img.decode().catch(() => {});
      }
      preloadedImages[item.bgImage] = img;
    }
  });

  bgLayerA.style.backgroundImage = `url('${MENU_ITEMS_DATA[0].bgImage}')`;
  bgLayerA.classList.add('active');

  // ==========================================
  // 5. SMOOTH DUAL-BUFFER BACKGROUND CROSSFADER
  // ==========================================
  function setBackgroundImage(imageUrl) {
    if (!imageUrl) return;
    const activeLayer = currentLayer === 'A' ? bgLayerA : bgLayerB;
    const nextLayer = currentLayer === 'A' ? bgLayerB : bgLayerA;

    // Avoid redundant fade if active layer already displays this image
    if (activeLayer.style.backgroundImage && activeLayer.style.backgroundImage.includes(imageUrl)) {
      return;
    }

    nextLayer.style.backgroundImage = `url('${imageUrl}')`;
    
    requestAnimationFrame(() => {
      nextLayer.classList.add('active');
      activeLayer.classList.remove('active');
      currentLayer = currentLayer === 'A' ? 'B' : 'A';
    });
  }

  // ==========================================
  // 6. DEVICE-AWARE CINEMATIC BACKGROUND ROTATION
  // ==========================================
  const ROTATION_ITEMS = MENU_ITEMS_DATA.slice(0, 5); // Start, Story, Press, Crunch, Chill
  let mobileRotationIndex = 0;
  let mobileRotationTimer = null;
  const ROTATION_INTERVAL_MS = 4600; // ~4.6 seconds between cinematic transitions

  const finePointerQuery = window.matchMedia('(hover: hover) and (pointer: fine)');
  const coarsePointerQuery = window.matchMedia('(hover: none) and (pointer: coarse)');
  const reducedMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');

  let hasRecentMouseInput = false;
  let mouseInputTimeout = null;

  // Track real pointer events to cleanly support hybrid touch laptops
  window.addEventListener('pointermove', (e) => {
    if (e.pointerType === 'mouse') {
      hasRecentMouseInput = true;
      if (mouseInputTimeout) clearTimeout(mouseInputTimeout);
      mouseInputTimeout = setTimeout(() => {
        hasRecentMouseInput = false;
      }, 5000);
    }
  }, { passive: true });

  function isTouchOriented() {
    // True if touch-oriented device without active mouse hover
    if (coarsePointerQuery.matches) return true;
    if (finePointerQuery.matches && !hasRecentMouseInput && window.innerWidth <= 1024) return true;
    if (finePointerQuery.matches && window.innerWidth > 1024) return false;
    return ('ontouchstart' in window || navigator.maxTouchPoints > 0) && window.innerWidth <= 1024;
  }

  function startMobileRotation() {
    stopMobileRotation();

    // Do not rotate if desktop mouse is active, if reduced motion is preferred, or if off main menu
    if (!isTouchOriented()) return;
    if (reducedMotionQuery.matches) return;
    if (currentRoute || isExitModalOpen || !loadingFinished || document.hidden) return;

    mobileRotationTimer = setTimeout(() => {
      if (currentRoute || isExitModalOpen || !loadingFinished || document.hidden) return;

      // Advance to next existing category background in sequence
      mobileRotationIndex = (mobileRotationIndex + 1) % ROTATION_ITEMS.length;
      const nextItem = ROTATION_ITEMS[mobileRotationIndex];
      if (nextItem && nextItem.bgImage) {
        setBackgroundImage(nextItem.bgImage);
      }

      startMobileRotation();
    }, ROTATION_INTERVAL_MS);
  }

  function stopMobileRotation() {
    if (mobileRotationTimer) {
      clearTimeout(mobileRotationTimer);
      mobileRotationTimer = null;
    }
  }

  // Pause rotation when tab is hidden, resume when tab is active
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      stopMobileRotation();
    } else {
      if (!currentRoute && !isExitModalOpen && loadingFinished) {
        startMobileRotation();
      }
    }
  });

  // ==========================================
  // 7. MENU SELECTION CONTROLLER
  // ==========================================
  function selectMenuItem(index, playSound = true) {
    if (index < 0 || index >= MENU_ITEMS_DATA.length) return;

    if (playSound && index !== currentIndex) {
      playHoverSound();
    }

    currentIndex = index;
    const data = MENU_ITEMS_DATA[index];

    menuItems.forEach((btn, i) => {
      btn.classList.toggle('active', i === index);
    });

    const targetItem = menuItems[index];
    if (targetItem && activePill) {
      const topOffset = targetItem.offsetTop;
      const height = targetItem.offsetHeight;
      activePill.style.transform = `translateY(${topOffset}px)`;
      activePill.style.height = `${height}px`;
    }

    if (!currentRoute && data && data.bgImage) {
      setBackgroundImage(data.bgImage);
    }
  }

  // Unified user selection (hover on desktop, tap on mobile)
  function onUserSelectMenuItem(index, isHover = false) {
    selectMenuItem(index, isHover);

    // Keep rotation synchronized with user's selected category
    if (index >= 0 && index < ROTATION_ITEMS.length) {
      mobileRotationIndex = index;
    }

    // Reset rotation timer so the selected background stays visible for full duration
    if (isTouchOriented() && !currentRoute && !isExitModalOpen) {
      startMobileRotation();
    }
  }

  // ==========================================
  // 8. EXPLICIT EXIT CONSOLE MODAL CONTROLS
  // ==========================================
  function openExitModal() {
    stopMobileRotation();
    playLaunchSound();
    isExitModalOpen = true;
    if (exitModalOverlay) {
      exitModalOverlay.style.display = 'flex';
      requestAnimationFrame(() => {
        exitModalOverlay.classList.add('open');
        exitModalOverlay.setAttribute('aria-hidden', 'false');
      });
    }
  }

  function closeExitModal() {
    playBackSound();
    isExitModalOpen = false;
    if (exitModalOverlay) {
      exitModalOverlay.classList.remove('open');
      exitModalOverlay.setAttribute('aria-hidden', 'true');
      setTimeout(() => {
        if (!isExitModalOpen) {
          exitModalOverlay.style.display = 'none';
        }
      }, 220);
    }
    if (!currentRoute && loadingFinished) {
      startMobileRotation();
    }
  }

  if (cancelExitModalBtn) {
    cancelExitModalBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      closeExitModal();
    });
  }

  if (confirmExitModalBtn) {
    confirmExitModalBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      closeExitModal();
      navigateToRoute('', 'back');
    });
  }

  if (exitModalBackdrop) {
    exitModalBackdrop.addEventListener('click', (e) => {
      e.preventDefault();
      closeExitModal();
    });
  }

  // ==========================================
  // 9. MULTI-LEVEL ROUTER & DEDICATED PAGES
  // ==========================================
  function normalizeRoute(route) {
    if (!route) return '';
    let clean = String(route).replace(/^#\/?/, '').trim();
    if (clean.endsWith('/')) clean = clean.slice(0, -1);
    return clean;
  }

  const MISSION_TELEMETRY = {
    'start': {
      badge: 'CATEGORY 01 // MISSION BRIEFING',
      title: 'START HACKATHON',
      subtitle: 'GE GRAPHITE 2026 // HACKATHON PROTOCOLS & TRACK BRIEFINGS',
      phases: [
        'INITIALIZING MISSION DIRECTIVES...',
        'ALLOCATING 24-HOUR HACKATHON PROTOCOLS...',
        'LOADING TRACK SPECS & SUBMISSION PIPELINE...',
        'CALIBRATING JUDGING MATRIX & SPIDER-SUIT HUD...',
        'DISPATCH READY // ENTERING HACKATHON HUB'
      ],
      details: [
        'Connecting to GE Bhimtal Mainframe...',
        'Synchronizing Web3, AI, and Autonomous Systems tracks...',
        'Validating team allocation and submission criteria...',
        'Finalizing hardware kits and cloud credits handshake...',
        'Hackathon command deck initialized.'
      ]
    },
    'story': {
      badge: 'CATEGORY 02 // NARRATIVE ARCHIVE',
      title: 'STORY MODE',
      subtitle: 'FROM PETER PARKER TO BHIMTAL // THE GRAPHITE SAGA',
      phases: [
        'DECRYPTING ARCHIVAL NARRATIVE DATABASE...',
        'RECONSTRUCTING SPIDER-VERSE ORIGIN LOGS...',
        'TRACING BHIMTAL HIMALAYAN TECH ROOTS...',
        'RENDERING CHARACTER TIMELINE & LEGACY...',
        'ARCHIVE UNLOCKED // ACCESSING STORY MODE'
      ],
      details: [
        'Reading encrypted Daily Bugle audio reels...',
        'Compiling Spider-Verse temporal anomalies...',
        'Aligning Himalayan mountain tech node data...',
        'Synthesizing legacy codex from 2018-2026...',
        'Narrative archive ready for inspection.'
      ]
    },
    'press': {
      badge: 'CATEGORY 03 // PRESS CLEARANCE',
      title: 'DAILY BUGLE PRESS PASS',
      subtitle: 'OFFICIAL ANNOUNCEMENTS, PRIZE POOLS & MEDIA LOGS',
      phases: [
        'CONNECTING TO BUGLE NEWSROOM FEED...',
        'FETCHING PRIZE VAULT LEDGER & CERTIFICATES...',
        'STREAMING MENTOR NETWORK AVAILABILITY...',
        'VERIFYING ACCREDITATION & BROADCAST LINK...',
        'PRESS CLEARANCE GRANTED // OPENING WIRE'
      ],
      details: [
        'Tuning in to J. Jonah Jameson frequency...',
        'Confirming ₹2,50,000+ prize pool allocation...',
        'Syncing mentor roster across top tech firms...',
        'Establishing Discord & official Bugle uplink...',
        'Newsroom dispatch verified.'
      ]
    },
    'crunch': {
      badge: 'CATEGORY 04 // REAL-TIME OPS',
      title: 'CRUNCH MODE // LOAD STATE',
      subtitle: 'SCHEDULE CRUNCH, GIT PROTOCOLS & SUBMISSION TERMINAL',
      phases: [
        'PINGING BHIMTAL CRUNCH TIMELINE NODES...',
        'INITIALIZING GIT COMMIT RECOVERY BUFFER...',
        'AUDITING EVALUATION RUBRICS & CHECKPOINTS...',
        'PRE-FLIGHT REPOSITORY HEALTH AUDIT...',
        'CRUNCH TERMINAL ARMED // ENGAGING HUB'
      ],
      details: [
        'Synchronizing 24h countdown clocks...',
        'Inspecting GitHub repository commit protocols...',
        'Loading Round 1 and Round 2 judge checkpoints...',
        'Verifying pre-flight checklists and slide decks...',
        'Crunch load state fully active.'
      ]
    },
    'chill': {
      badge: 'CATEGORY 05 // SANCTUARY RETREAT',
      title: 'CHILL ZONE // WEB HAMMOCK',
      subtitle: 'HIMALAYAN WORKSHOPS, AMBIENT LO-FI & FACILITIES',
      phases: [
        'RESONATING HIMALAYAN CHILL FREQUENCY...',
        'TUNING WEB HAMMOCK RELAXATION MATRIX...',
        'LOCATING CAMPUS WORKSHOPS & REST ROOMS...',
        'GENERATING LO-FI ACOUSTIC FIELD...',
        'SANCTUARY GRANTED // ENTERING CHILL ZONE'
      ],
      details: [
        'Bhimtal mountain breeze audio simulation...',
        'Mapping recreation zones, dining, and coffee refill hubs...',
        'Loading packing checklists and travel route maps...',
        'Calibrating lo-fi ambient frequency generator...',
        'Web Hammock sanctuary primed.'
      ]
    }
  };

  let isMissionTransitioning = false;
  let missionTransitionAnimId = null;

  function runMissionTransition(targetRoute, onComplete) {
    if (!missionTransitionScreen) {
      onComplete();
      return;
    }

    const parts = targetRoute.split('/');
    const catKey = parts[0] || 'start';
    const tele = MISSION_TELEMETRY[catKey] || MISSION_TELEMETRY['start'];
    const cfg = ROUTE_CONFIG[targetRoute] || {};

    let destTitle = tele.title;
    if (targetRoute.includes('/')) {
      const subKey = parts.slice(1).join(' ').replace(/-/g, ' ').toUpperCase();
      destTitle = subKey;
    }

    if (transBadgeText) transBadgeText.textContent = tele.badge;
    if (transDestTitle) transDestTitle.textContent = destTitle;
    if (transDestSub) transDestSub.textContent = tele.subtitle;

    if (transPctValue) transPctValue.textContent = '0';
    if (transCircleFill) transCircleFill.style.strokeDashoffset = '125.66';
    if (transStatusPhase) transStatusPhase.textContent = tele.phases[0];
    if (transStatusDetail) transStatusDetail.textContent = tele.details[0];
    if (transDockRight) transDockRight.classList.remove('ready');

    missionTransitionScreen.classList.remove('slide-up');
    missionTransitionScreen.classList.add('active');
    missionTransitionScreen.setAttribute('aria-hidden', 'false');

    if (transVideo) {
      transVideo.muted = true;
      transVideo.currentTime = 0;
      const p = transVideo.play();
      if (p !== undefined) p.catch(() => {});
    }

    isMissionTransitioning = true;
    const startTime = performance.now();
    const DEFAULT_TRANSITION_MS = 6350; // 6.35s matching IMG_0458

    function completeTransition() {
      if (!isMissionTransitioning) return;
      isMissionTransitioning = false;
      if (missionTransitionAnimId) cancelAnimationFrame(missionTransitionAnimId);
      if (transVideo) {
        transVideo.pause();
      }

      if (transPctValue) transPctValue.textContent = '100';
      if (transCircleFill) transCircleFill.style.strokeDashoffset = '0';
      if (transStatusPhase) transStatusPhase.textContent = tele.phases[4];
      if (transStatusDetail) transStatusDetail.textContent = tele.details[4];
      if (transDockRight) transDockRight.classList.add('ready');

      setTimeout(() => {
        playSlideUpSound();
        missionTransitionScreen.classList.add('slide-up');
        setTimeout(() => {
          missionTransitionScreen.classList.remove('active');
          missionTransitionScreen.classList.remove('slide-up');
          missionTransitionScreen.setAttribute('aria-hidden', 'true');
        }, 750);
        onComplete();
      }, 180);
    }

    if (transSkipBtn) {
      transSkipBtn.onclick = (e) => {
        e.stopPropagation();
        completeTransition();
      };
    }

    if (transVideo) {
      transVideo.onended = () => {
        completeTransition();
      };
    }

    function transitionStep(now) {
      if (!isMissionTransitioning) return;
      
      let rawPct = 0;
      if (transVideo && transVideo.duration > 0 && !isNaN(transVideo.duration) && transVideo.currentTime > 0) {
        rawPct = (transVideo.currentTime / transVideo.duration) * 100;
        if (transVideo.ended || transVideo.currentTime >= transVideo.duration - 0.12) {
          rawPct = 100;
        }
      } else {
        const elapsed = now - startTime;
        rawPct = Math.min(100, (elapsed / DEFAULT_TRANSITION_MS) * 100);
      }

      const currentPct = Math.min(100, Math.floor(rawPct));
      if (transPctValue) transPctValue.textContent = currentPct;

      if (transCircleFill) {
        const offset = 125.66 - (125.66 * (rawPct / 100));
        transCircleFill.style.strokeDashoffset = Math.max(0, offset);
      }

      const phaseIdx = Math.min(4, Math.floor(rawPct / 20));
      if (transStatusPhase) transStatusPhase.textContent = tele.phases[phaseIdx];
      if (transStatusDetail) transStatusDetail.textContent = tele.details[phaseIdx];

      if (rawPct >= 100) {
        completeTransition();
      } else {
        missionTransitionAnimId = requestAnimationFrame(transitionStep);
      }
    }

    missionTransitionAnimId = requestAnimationFrame(transitionStep);
  }

  function runSubpageFadeTransition(targetRoute, onComplete) {
    if (isSubTransitioning || isMissionTransitioning) {
      if (typeof onComplete === 'function') onComplete();
      return;
    }
    isSubTransitioning = true;

    if (subpageFadeOverlay) {
      subpageFadeOverlay.classList.remove('fading-out');
      subpageFadeOverlay.classList.add('active');
    }

    // Gentle fade out phase (420ms)
    setTimeout(() => {
      if (typeof onComplete === 'function') {
        onComplete();
      }

      // Smooth fade in phase to reveal destination (520ms)
      if (subpageFadeOverlay) {
        subpageFadeOverlay.classList.remove('active');
        subpageFadeOverlay.classList.add('fading-out');
      }

      setTimeout(() => {
        if (subpageFadeOverlay) {
          subpageFadeOverlay.classList.remove('fading-out');
        }
        isSubTransitioning = false;
      }, 520);
    }, 420);
  }

  function navigateToRoute(route, sound = 'launch', isMainMenuLaunch = false) {
    if (isExitModalOpen) {
      closeExitModal();
    }

    const clean = normalizeRoute(route);

    if (clean === 'exit') {
      openExitModal();
      return;
    }

    if (sound === 'back') {
      playBackSound();
    } else {
      playLaunchSound();
    }
    startBgMusic();

    const doApplyRoute = () => {
      const currentClean = normalizeRoute(window.location.hash);
      if (currentClean === clean) {
        applyRoute(clean);
      } else {
        window.location.hash = clean ? '#/' + clean : '#/';
      }
    };

    // ONLY the 5 main menu buttons clicked directly from the Main Menu shell
    // trigger the cinematic video loading screen
    if (isMainMenuLaunch && ['start', 'story', 'press', 'crunch', 'chill'].includes(clean)) {
      runMissionTransition(clean, doApplyRoute);
      return;
    }

    // For ALL sub-buttons inside pages, category hubs, sub-links, back buttons:
    // Execute a gentle 1-second fade transition
    runSubpageFadeTransition(clean, doApplyRoute);
  }

  function applyRoute(route) {
    if (isExitModalOpen) {
      closeExitModal();
    }

    const clean = normalizeRoute(route);

    if (clean === 'exit') {
      openExitModal();
      return;
    }

    const cfg = ROUTE_CONFIG[clean] || (clean === '' ? ROUTE_CONFIG[''] : null);

    if (!cfg || !cfg.pageId) {
      // Return to Main Menu Shell
      currentRoute = '';
      pagesContainer.classList.remove('active');
      pagesContainer.setAttribute('aria-hidden', 'true');
      detailPages.forEach(p => p.classList.remove('active-page'));
      mainMenuShell.classList.remove('menu-hidden');

      if (cfg && cfg.index !== undefined) {
        selectMenuItem(cfg.index, false);
      } else {
        selectMenuItem(currentIndex, false);
      }

      // Resume mobile rotation when returning to Main Menu
      startMobileRotation();
      return;
    }

    // Entering a Category Hub or Sub-Page: Stop main-menu rotation
    stopMobileRotation();

    currentRoute = clean;
    if (cfg.index !== undefined) {
      selectMenuItem(cfg.index, false);
    }

    mainMenuShell.classList.add('menu-hidden');

    pagesContainer.classList.add('active');
    pagesContainer.setAttribute('aria-hidden', 'false');

    const targetElement = document.getElementById(cfg.pageId);
    detailPages.forEach(p => {
      const isTarget = p === targetElement;
      p.classList.toggle('active-page', isTarget);
      if (isTarget) {
        const scroller = p.querySelector('.page-scroller');
        if (scroller) scroller.scrollTop = 0;
      }
    });

    if (cfg.bgImage) {
      setBackgroundImage(cfg.bgImage);
    }
  }

  // Browser Back/Forward navigation listener
  window.addEventListener('hashchange', () => {
    applyRoute(window.location.hash);
  });

  // Global Delegated Click Listeners
  document.addEventListener('click', (e) => {
    // Unconditionally activate background music on any user click ONLY after intro has finished
    if (loadingFinished && !bgmAutoStarted && audioEnabled && bgMusic) {
      startBgMusic();
    }

    // Authentic Spider-Man Web Splat FX on any button or interactive element click
    const clickable = e.target.closest('button, .menu-item, .card, .back-to-menu-btn, .page-card, a, [data-route], [data-back-route], [data-action], .action-btn, .sound-btn, .fs-btn, .hud-btn, .control-btn');
    if (clickable) {
      let clickX = e.clientX;
      let clickY = e.clientY;
      if (!clickX && !clickY) {
        const rect = clickable.getBoundingClientRect();
        clickX = rect.left + rect.width / 2;
        clickY = rect.top + rect.height / 2;
      }
      spawnSpiderwebBurst(clickX, clickY);
    }

    if (isExitModalOpen) {
      const insideModal = e.target.closest('#exitModalOverlay');
      if (!insideModal) {
        closeExitModal();
        return;
      }
    }

    // 1. Check for dedicated countdown action
    const countdownActionTrigger = e.target.closest('[data-action="open-countdown"], #menuCountdownBtn');
    if (countdownActionTrigger) {
      playSelectSound();
      if (!e.ctrlKey && !e.metaKey && !e.shiftKey) {
        e.preventDefault();
        window.location.href = 'countdown.html';
      }
      return;
    }

    // 2. Check for dedicated exit action
    const exitActionTrigger = e.target.closest('[data-action="exit-console"]');
    if (exitActionTrigger) {
      e.preventDefault();
      openExitModal();
      return;
    }

    // 2. Check for data-route trigger
    const routeTrigger = e.target.closest('[data-route]');
    if (routeTrigger) {
      e.preventDefault();
      const targetRoute = routeTrigger.getAttribute('data-route');
      if (targetRoute === 'exit') {
        openExitModal();
      } else {
        // Only the top-level 5 main menu buttons clicked directly from the main menu shell
        // trigger the video loading screen. All sub-buttons use the gentle 1s fade transition.
        const isMainMenuBtn = routeTrigger.classList.contains('menu-item') && !currentRoute;
        if (isMainMenuBtn) {
          const itemIdx = parseInt(routeTrigger.getAttribute('data-index'), 10);
          if (!isNaN(itemIdx)) {
            onUserSelectMenuItem(itemIdx, false);
          }
        }
        navigateToRoute(targetRoute, 'launch', isMainMenuBtn);
      }
      return;
    }

    // 3. Check for data-back-route trigger
    const backTrigger = e.target.closest('[data-back-route]');
    if (backTrigger) {
      e.preventDefault();
      const backRoute = backTrigger.getAttribute('data-back-route');
      navigateToRoute(backRoute, 'back', false);
      return;
    }
  });

  // Main menu hover preview (Desktop) & Touch preview (Mobile)
  menuItems.forEach((btn, idx) => {
    // Desktop mouseenter: immediate preview
    btn.addEventListener('mouseenter', () => {
      if (currentIndex !== idx && !currentRoute && !isExitModalOpen) {
        onUserSelectMenuItem(idx, true);
      }
    });

    // Touch interaction: immediately preview tapped button's background image
    btn.addEventListener('touchstart', () => {
      if (!currentRoute && !isExitModalOpen) {
        onUserSelectMenuItem(idx, false);
      }
    }, { passive: true });
  });

  // ==========================================
  // 10. INTERACTIVE FEATURES & DEMOS
  // ==========================================
  if (pageCopySpecsBtn) {
    pageCopySpecsBtn.addEventListener('click', () => {
      playLaunchSound();
      const text = "GRAPHITE '26 Hackathon | Graphic Era Hill University, Bhimtal (4494.75 ft AMSL) | Dates: 27-28 Oct 2026 | Squad: Exactly 4 Devs | Prize: ₹1,00,000+ | Instagram: @graphite.xo";
      navigator.clipboard.writeText(text).then(() => {
        showToast('✓ GRAPHITE 26 Specs copied to clipboard!');
      }).catch(() => {
        showToast('GRAPHITE 26: 27-28 Oct 2026 at GEHU Bhimtal');
      });
    });
  }

  if (refillCoffeeBtn) {
    refillCoffeeBtn.addEventListener('click', () => {
      playLaunchSound();
      showToast('☕ Double Espresso Injected! Energy at 100% capacity.');
    });
  }

  if (summonMentorBtn) {
    summonMentorBtn.addEventListener('click', () => {
      playLaunchSound();
      showToast('⚡ Mentor SOS Beacon Dispatched! Lead Mentor arriving at lab.');
    });
  }

  if (rollbackCommitBtn) {
    rollbackCommitBtn.addEventListener('click', () => {
      playLaunchSound();
      showToast('✓ Rolled back to commit [ae91f3b]. All unit tests green!');
    });
  }

  if (chillLoFiBtn) {
    chillLoFiBtn.addEventListener('click', () => {
      toggleLoFiSound();
    });
  }

  // ==========================================
  // 11. TOAST NOTIFICATIONS
  // ==========================================
  function showToast(message) {
    if (toastTimer) clearTimeout(toastTimer);
    if (!gameToast) return;
    gameToast.textContent = message;
    gameToast.classList.add('visible');
    toastTimer = setTimeout(() => {
      gameToast.classList.remove('visible');
    }, 3200);
  }

  // ==========================================
  // 12. KEYBOARD CONTROLS & SHORTCUTS
  // ==========================================
  window.addEventListener('keydown', (e) => {
    if (!loadingFinished) {
      if (e.key === ' ' || e.key === 'Enter' || e.key === 'Escape') {
        e.preventDefault();
        skipLoadingSequence();
      }
      return;
    }

    if (isExitModalOpen) {
      if (e.key === 'Escape') {
        e.preventDefault();
        closeExitModal();
        return;
      }
      if (e.key === 'Enter') {
        e.preventDefault();
        closeExitModal();
        navigateToRoute('', 'back');
        return;
      }
      return;
    }

    if (e.key === 'Escape') {
      e.preventDefault();
      if (currentRoute) {
        const cfg = ROUTE_CONFIG[currentRoute];
        const parentRoute = cfg ? cfg.parent : '';
        navigateToRoute(parentRoute || '', 'back');
      } else {
        openExitModal();
      }
      return;
    }

    if (!currentRoute) {
      switch (e.key) {
        case 'ArrowUp':
        case 'w':
        case 'W':
          e.preventDefault();
          const prevIndex = (currentIndex - 1 + MENU_ITEMS_DATA.length) % MENU_ITEMS_DATA.length;
          onUserSelectMenuItem(prevIndex, true);
          break;

        case 'ArrowDown':
        case 's':
        case 'S':
          e.preventDefault();
          const nextIndex = (currentIndex + 1) % MENU_ITEMS_DATA.length;
          onUserSelectMenuItem(nextIndex, true);
          break;

        case 'Enter':
        case ' ':
          e.preventDefault();
          const curItem = MENU_ITEMS_DATA[currentIndex];
          if (curItem) {
            if (curItem.action === 'exit-console') {
              openExitModal();
            } else if (curItem.action === 'open-countdown') {
              playSelectSound();
              window.location.href = 'countdown.html';
            } else if (curItem.route) {
              navigateToRoute(curItem.route, 'launch', true);
            }
          }
          break;

        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
          const num = parseInt(e.key, 10) - 1;
          if (num >= 0 && num < 5) {
            onUserSelectMenuItem(num, true);
            navigateToRoute(MENU_ITEMS_DATA[num].route, 'launch', true);
          }
          break;

        case '6':
          onUserSelectMenuItem(5, true);
          playSelectSound();
          window.location.href = 'countdown.html';
          break;

        case '7':
          onUserSelectMenuItem(6, true);
          openExitModal();
          break;
      }
    }

    if (e.key === 'm' || e.key === 'M') {
      toggleSound();
    } else if (e.key === 'f' || e.key === 'F') {
      toggleFullscreen();
    }
  });

  // ==========================================
  // 13. HUD SOUND & FULLSCREEN TOGGLE
  // ==========================================
  function toggleSound() {
    audioEnabled = !audioEnabled;
    if (audioEnabled) {
      initAudio();
      playLaunchSound();
      startBgMusic();
      if (iconSoundOn) iconSoundOn.style.display = 'block';
      if (iconSoundOff) iconSoundOff.style.display = 'none';
      if (soundLabel) soundLabel.textContent = 'SFX';
      showToast('♪ Background Music & SFX: ACTIVE');
    } else {
      if (bgMusic) {
        bgMusic.pause();
      }
      if (loFiPlaying) toggleLoFiSound();
      if (iconSoundOn) iconSoundOn.style.display = 'none';
      if (iconSoundOff) iconSoundOff.style.display = 'block';
      if (soundLabel) soundLabel.textContent = 'MUTED';
      showToast('Audio Muted');
    }
  }

  if (soundToggle) soundToggle.addEventListener('click', toggleSound);

  function toggleFullscreen() {
    playHoverSound();
    const doc = document.documentElement;
    const isFs = document.fullscreenElement || document.webkitFullscreenElement;
    if (!isFs) {
      if (doc.requestFullscreen) {
        doc.requestFullscreen().catch(() => {});
      } else if (doc.webkitRequestFullscreen) {
        doc.webkitRequestFullscreen().catch(() => {});
      } else {
        showToast('Fullscreen managed by browser');
      }
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen().catch(() => {});
      } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen().catch(() => {});
      }
    }
  }

  if (fsToggle) fsToggle.addEventListener('click', toggleFullscreen);

  // ==========================================
  // 14. GRAPHITE '26 LAUNCH COUNTDOWN TIMER
  // ==========================================
  // Target: October 27, 2026, 09:00:00 IST (Bhimtal, India +05:30)
  const EVENT_TARGET_MS = new Date('2026-10-27T09:00:00+05:30').getTime();

  function updateHUDClocks() {
    if (!systemClock) return;
    const now = Date.now();
    const diff = EVENT_TARGET_MS - now;

    if (diff <= 0) {
      systemClock.textContent = 'EVENT LIVE // ACTIVE';
      systemClock.classList.add('live');
      return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((diff / (1000 * 60)) % 60);
    const seconds = Math.floor((diff / 1000) % 60);

    const padH = String(hours).padStart(2, '0');
    const padM = String(minutes).padStart(2, '0');
    const padS = String(seconds).padStart(2, '0');

    systemClock.textContent = `T-${days}D ${padH}:${padM}:${padS}`;
  }

  setInterval(updateHUDClocks, 1000);
  updateHUDClocks();

  // ==========================================
  // 15. SUBTLE AMBIENT PARTICLE DUST
  // ==========================================
  const canvas = document.getElementById('particleCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
      selectMenuItem(currentIndex, false);
      if (!currentRoute && !isExitModalOpen && loadingFinished) {
        startMobileRotation();
      }
    });

    const particles = [];
    const PARTICLE_COUNT = 20;

    for (let i = 0; i < PARTICLE_COUNT; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * 1.4 + 0.6,
        speedX: (Math.random() - 0.5) * 0.25,
        speedY: -Math.random() * 0.4 - 0.1,
        opacity: Math.random() * 0.3 + 0.1,
        color: Math.random() > 0.4 ? 'rgba(255, 42, 59,' : 'rgba(0, 210, 255,'
      });
    }

    function renderParticles() {
      ctx.clearRect(0, 0, width, height);

      particles.forEach(p => {
        p.x += p.speedX;
        p.y += p.speedY;

        if (p.y < -10) {
          p.y = height + 10;
          p.x = Math.random() * width;
        }
        if (p.x < -10) p.x = width + 10;
        if (p.x > width + 10) p.x = -10;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = `${p.color} ${p.opacity})`;
        ctx.shadowBlur = 4;
        ctx.shadowColor = p.color === 'rgba(255, 42, 59,' ? '#ff2a3b' : '#00d2ff';
        ctx.fill();
      });

      requestAnimationFrame(renderParticles);
    }

    renderParticles();
  }

  // ==========================================
  // 15B. BUTTERY 60FPS BACKGROUND PARALLAX LERP
  // ==========================================
  let targetParallaxX = 0;
  let targetParallaxY = 0;
  let currentParallaxX = 0;
  let currentParallaxY = 0;

  window.addEventListener('mousemove', (e) => {
    // Normalized [-1, 1] relative to viewport center
    const normX = (e.clientX / window.innerWidth) * 2 - 1;
    const normY = (e.clientY / window.innerHeight) * 2 - 1;
    targetParallaxX = normX;
    targetParallaxY = normY;
  }, { passive: true });

  window.addEventListener('deviceorientation', (e) => {
    if (e.gamma !== null && e.beta !== null) {
      targetParallaxX = Math.max(-1, Math.min(1, e.gamma / 25));
      targetParallaxY = Math.max(-1, Math.min(1, (e.beta - 40) / 25));
    }
  }, { passive: true });

  function updateParallaxLoop() {
    currentParallaxX += (targetParallaxX - currentParallaxX) * 0.055;
    currentParallaxY += (targetParallaxY - currentParallaxY) * 0.055;

    // Background moves opposite for immersive depth illusion
    const bgPx = (-currentParallaxX * 18).toFixed(2);
    const bgPy = (-currentParallaxY * 18).toFixed(2);
    const webPx = (currentParallaxX * 10).toFixed(2);
    const webPy = (currentParallaxY * 10).toFixed(2);

    document.documentElement.style.setProperty('--bg-px', `${bgPx}px`);
    document.documentElement.style.setProperty('--bg-py', `${bgPy}px`);
    document.documentElement.style.setProperty('--web-px', `${webPx}px`);
    document.documentElement.style.setProperty('--web-py', `${webPy}px`);

    requestAnimationFrame(updateParallaxLoop);
  }
  requestAnimationFrame(updateParallaxLoop);

  // ==========================================
  // 16. AAA CINEMATIC INTRO VIDEO & LOADING SCREEN CONTROLLER
  // ==========================================
  const gameIntroLoader = document.getElementById('gameIntroLoader');
  const loaderVideo = document.getElementById('loaderVideo');
  const loaderCircleFill = document.getElementById('loaderCircleFill');
  const loaderPctValue = document.getElementById('loaderPctValue');
  const loaderStatusPhase = document.getElementById('loaderStatusPhase');
  const loaderDockRight = document.getElementById('loaderDockRight');
  const loaderSkipBtn = document.getElementById('loaderSkipBtn');

  const CIRCLE_CIRCUMFERENCE = 125.66;
  const INTRO_DURATION_MS = 3800;
  let loadingFinished = false;
  let displayedProgress = 0;
  let animFrameId = null;
  let videoStarted = false;
  let isVideoMode = false;
  let pageLoadTime = performance.now();
  let videoStartTime = 0;

  function playSlideUpSound() {
    try {
      initAudio();
      if (!audioCtx) return;
      const now = audioCtx.currentTime;

      const sub = audioCtx.createOscillator();
      const subG = audioCtx.createGain();
      sub.type = 'sine';
      sub.frequency.setValueAtTime(150, now);
      sub.frequency.exponentialRampToValueAtTime(32, now + 0.48);
      subG.gain.setValueAtTime(0.3, now);
      subG.gain.exponentialRampToValueAtTime(0.001, now + 0.48);
      sub.connect(subG);
      subG.connect(audioCtx.destination);
      sub.start(now);
      sub.stop(now + 0.48);

      const sweep = audioCtx.createOscillator();
      const sweepG = audioCtx.createGain();
      sweep.type = 'triangle';
      sweep.frequency.setValueAtTime(240, now);
      sweep.frequency.exponentialRampToValueAtTime(860, now + 0.36);
      sweepG.gain.setValueAtTime(0.07, now);
      sweepG.gain.exponentialRampToValueAtTime(0.001, now + 0.36);
      sweep.connect(sweepG);
      sweepG.connect(audioCtx.destination);
      sweep.start(now);
      sweep.stop(now + 0.36);
    } catch (e) {}
  }

  function finishLoadingSequence() {
    if (loadingFinished) return;
    loadingFinished = true;
    if (animFrameId) cancelAnimationFrame(animFrameId);

    if (loaderPctValue) loaderPctValue.textContent = '100';
    if (loaderCircleFill) loaderCircleFill.style.strokeDashoffset = '0';
    if (loaderStatusPhase) loaderStatusPhase.textContent = 'SYSTEM READY // ACCESS GRANTED';
    if (loaderDockRight) loaderDockRight.classList.add('ready');

    setTimeout(() => {
      playSlideUpSound();

      if (gameIntroLoader) {
        gameIntroLoader.classList.add('slide-up');
      }

      document.body.classList.remove('loading');
      startBgMusic();

      if (window.location.hash) {
        applyRoute(window.location.hash);
      } else {
        // Start mobile cinematic background rotation if on main menu
        startMobileRotation();
      }

      setTimeout(() => {
        if (gameIntroLoader) {
          gameIntroLoader.classList.add('loader-hidden');
        }
        if (loaderVideo) {
          loaderVideo.pause();
        }
      }, 1000);
    }, 220);
  }

  function skipLoadingSequence() {
    if (loadingFinished) return;
    displayedProgress = 100;
    finishLoadingSequence();
  }

  if (loaderSkipBtn) {
    loaderSkipBtn.addEventListener('click', skipLoadingSequence);
  }

  window.addEventListener('keydown', (e) => {
    if (!loadingFinished && (e.code === 'Space' || e.key === 'Escape' || e.key === ' ')) {
      e.preventDefault();
      skipLoadingSequence();
    } else if (isMissionTransitioning && (e.code === 'Space' || e.key === 'Escape' || e.key === ' ')) {
      e.preventDefault();
      if (transSkipBtn) transSkipBtn.click();
    }
  });

  if (loaderVideo) {
    loaderVideo.muted = true;
    loaderVideo.defaultMuted = true;
    loaderVideo.playsInline = true;
    loaderVideo.setAttribute('playsinline', '');
    loaderVideo.setAttribute('webkit-playsinline', '');
    loaderVideo.setAttribute('x5-playsinline', '');

    const tryStartVideo = () => {
      if (loadingFinished) return;
      loaderVideo.muted = true;
      const promise = loaderVideo.play();
      if (promise !== undefined) {
        promise.then(() => {
          videoStarted = true;
          isVideoMode = true;
          if (!videoStartTime) videoStartTime = performance.now();
        }).catch(() => {
          // If mobile strictly requires a gesture, auto-unlock on first touch
          const forceStart = () => {
            loaderVideo.play().catch(() => {});
            window.removeEventListener('touchstart', forceStart);
            window.removeEventListener('touchend', forceStart);
          };
          window.addEventListener('touchstart', forceStart, { once: true, passive: true });
          window.addEventListener('touchend', forceStart, { once: true, passive: true });
        });
      }
    };

    loaderVideo.addEventListener('playing', () => {
      videoStarted = true;
      isVideoMode = true;
      if (!videoStartTime) videoStartTime = performance.now();
    });

    loaderVideo.addEventListener('canplay', tryStartVideo, { once: true });
    loaderVideo.addEventListener('loadeddata', tryStartVideo, { once: true });

    tryStartVideo();

    loaderVideo.addEventListener('ended', () => {
      finishLoadingSequence();
    });
  }

  function updateLoadingProgress(timestamp) {
    if (loadingFinished) return;

    let targetProgress = 0;

    if (loaderVideo && isVideoMode && loaderVideo.duration > 0 && !isNaN(loaderVideo.duration)) {
      // Driven by actual video playback progress: full duration is guaranteed!
      const duration = loaderVideo.duration;
      const current = loaderVideo.currentTime;
      targetProgress = (current / duration) * 100;

      // When video is almost finished (within 0.1s of end) or has ended
      if (current >= duration - 0.1 || loaderVideo.ended) {
        targetProgress = 100;
      }
    } else if (!videoStarted) {
      const waitElapsed = timestamp - pageLoadTime;
      if (waitElapsed < 1400) {
        // While waiting for video to initialize, gently advance initial telemetry (up to 15%)
        targetProgress = (waitElapsed / 1400) * 15;
      } else {
        // Fallback: If video failed or cannot play after 1.4s, smoothly complete loader
        const fallbackElapsed = waitElapsed - 1400;
        targetProgress = 15 + (fallbackElapsed / INTRO_DURATION_MS) * 85;
      }
    } else {
      // Fallback timer
      const elapsed = timestamp - (videoStartTime || pageLoadTime);
      targetProgress = (elapsed / INTRO_DURATION_MS) * 100;
    }

    targetProgress = Math.min(100, Math.max(0, targetProgress));
    
    // Smooth progress interpolation
    displayedProgress += (targetProgress - displayedProgress) * 0.22;
    if (targetProgress >= 99.4) {
      displayedProgress = 100;
    }

    const currentPct = Math.min(100, Math.floor(displayedProgress));

    if (loaderPctValue) {
      loaderPctValue.textContent = currentPct;
    }

    if (loaderCircleFill) {
      const strokeOffset = CIRCLE_CIRCUMFERENCE - (CIRCLE_CIRCUMFERENCE * (displayedProgress / 100));
      loaderCircleFill.style.strokeDashoffset = Math.max(0, strokeOffset);
    }

    if (loaderStatusPhase) {
      if (currentPct < 22) {
        loaderStatusPhase.textContent = 'INITIALIZING ENGINE...';
      } else if (currentPct < 48) {
        loaderStatusPhase.textContent = 'SYNCHRONIZING SPIDER-SUIT HUD...';
      } else if (currentPct < 76) {
        loaderStatusPhase.textContent = 'STREAMING BHIMTAL TERRAIN MESH...';
      } else if (currentPct < 96) {
        loaderStatusPhase.textContent = 'MOUNTING GRAPHITE TERMINAL...';
      } else {
        loaderStatusPhase.textContent = 'SYSTEM READY // ACCESS GRANTED';
      }
    }

    if (displayedProgress >= 100) {
      finishLoadingSequence();
    } else {
      animFrameId = requestAnimationFrame(updateLoadingProgress);
    }
  }

  // Safety watchdog: ensure page is NEVER stuck even if tab throttled or video stalled
  setTimeout(() => {
    if (!loadingFinished) {
      finishLoadingSequence();
    }
  }, 6500);

  // Initialize main menu
  selectMenuItem(0, false);

  // Start smooth progress loop
  pageLoadTime = performance.now();
  animFrameId = requestAnimationFrame(updateLoadingProgress);

  // Mobile Swipe-Right-to-Return Gesture
  let touchStartX = 0;
  let touchStartY = 0;
  if (pagesContainer) {
    pagesContainer.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches[0]) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
      }
    }, { passive: true });

    pagesContainer.addEventListener('touchend', (e) => {
      if (e.changedTouches && e.changedTouches[0] && currentRoute && !isExitModalOpen) {
        const diffX = e.changedTouches[0].clientX - touchStartX;
        const diffY = Math.abs(e.changedTouches[0].clientY - touchStartY);
        if (diffX > 75 && diffY < 90) {
          const cfg = ROUTE_CONFIG[currentRoute];
          const parentRoute = cfg ? cfg.parent : '';
          navigateToRoute(parentRoute || '', 'back');
        }
      }
    }, { passive: true });
  }

  // Universal Passive Audio Activation — Unlocks music on ANY interaction
  // (swipe, thumb touch, mouse move, scroll, key, or tap) without waiting for any button click!
  const PASSIVE_AUDIO_EVENTS = [
    'pointerdown', 'pointerup', 'pointermove',
    'touchstart', 'touchend', 'touchmove',
    'mousedown', 'mouseup', 'mousemove',
    'wheel', 'scroll', 'keydown', 'keyup',
    'focus', 'click'
  ];

  const triggerAutoAudio = () => {
    initAudio();
    // STRICT RULE: Background music must ONLY start AFTER the intro video sequence has finished!
    if (!loadingFinished) return;
    if (!bgmAutoStarted && audioEnabled && bgMusic) {
      startBgMusic();
    }
  };

  PASSIVE_AUDIO_EVENTS.forEach(evt => {
    window.addEventListener(evt, triggerAutoAudio, { capture: true, passive: true });
    document.addEventListener(evt, triggerAutoAudio, { capture: true, passive: true });
  });

  if (gameIntroLoader) {
    ['pointerdown', 'touchstart', 'click'].forEach(evt => {
      gameIntroLoader.addEventListener(evt, () => {
        initAudio();
      }, { passive: true });
    });
  }

  // ========================================================
  // 24-HOUR COUNTDOWN CORNER LAUNCHER (NEW WINDOW CONTROLLER)
  // ========================================================
  const cornerCountdownBtn = document.getElementById('cornerCountdownBtn');
  if (cornerCountdownBtn) {
    cornerCountdownBtn.addEventListener('click', (e) => {
      playSelectSound();
      
      // If clicked without special key modifiers, open as a sleek dedicated window
      if (!e.ctrlKey && !e.metaKey && !e.shiftKey) {
        e.preventDefault();
        const width = 1260;
        const height = 820;
        const left = Math.max(0, Math.round((window.screen.width - width) / 2));
        const top = Math.max(0, Math.round((window.screen.height - height) / 2));
        const winFeatures = `width=${width},height=${height},left=${left},top=${top},resizable=yes,scrollbars=yes,status=no`;

        try {
          const newWin = window.open('countdown.html', 'GraphiteCountdownWindow', winFeatures);
          if (newWin) {
            newWin.focus();
            return;
          }
        } catch (err) {
          // Fallback to new tab if popups restricted
        }
        window.open('countdown.html', '_blank');
      }
    });
  }
});

