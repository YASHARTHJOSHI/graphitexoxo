# -*- coding: utf-8 -*-
"""
Script to update app.js with the device-aware cinematic background system:
1. Desktop/laptop: Preserves instant hover-driven background image changes unchanged.
2. Mobile/touch devices: Automatic continuous cinematic rotation of the 5 category background images (~4.5s interval, ~1s smooth crossfade).
3. Immediate touch synchronization: Tapping a menu item immediately crossfades to that item's image and syncs rotation index.
4. Clean lifecycle: Stops rotation in category hubs/sub-pages/exit modal or when tab is hidden; resumes on return to Main Menu.
5. Hybrid & reduced motion awareness.
"""

new_app_js = '''/**
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
  }

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

  function startBgMusic() {
    if (!audioEnabled || !bgMusic) return;
    initAudio();
    if (bgMusic.paused) {
      bgMusic.play().then(() => {}).catch(() => {});
    }
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

  function navigateToRoute(route, sound = 'launch') {
    if (isExitModalOpen) {
      closeExitModal();
    }

    const clean = normalizeRoute(route);
    if (sound === 'launch') {
      playLaunchSound();
    } else if (sound === 'back') {
      playBackSound();
    }

    const currentClean = normalizeRoute(window.location.hash);
    if (currentClean === clean) {
      applyRoute(clean);
    } else {
      window.location.hash = clean ? '#/' + clean : '#/';
    }
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
    if (isExitModalOpen) {
      const insideModal = e.target.closest('#exitModalOverlay');
      if (!insideModal) {
        closeExitModal();
        return;
      }
    }

    // 1. Check for dedicated exit action
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
        navigateToRoute(targetRoute, 'launch');
      }
      return;
    }

    // 3. Check for data-back-route trigger
    const backTrigger = e.target.closest('[data-back-route]');
    if (backTrigger) {
      e.preventDefault();
      const backRoute = backTrigger.getAttribute('data-back-route');
      navigateToRoute(backRoute, 'back');
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
            } else if (curItem.route) {
              navigateToRoute(curItem.route, 'launch');
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
            navigateToRoute(MENU_ITEMS_DATA[num].route, 'launch');
          }
          break;

        case '6':
          selectMenuItem(5, true);
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
      if (bgMusic && bgMusic.paused) {
        bgMusic.play().catch(() => {});
      }
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
  // 14. REAL-TIME CLOCK
  // ==========================================
  function updateHUDClocks() {
    if (!systemClock) return;
    const now = new Date();
    const hh = String(now.getHours()).padStart(2, '0');
    const mm = String(now.getMinutes()).padStart(2, '0');
    const ss = String(now.getSeconds()).padStart(2, '0');
    systemClock.textContent = `${hh}:${mm}:${ss}`;
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

  // Mouse parallax tilt on background (Desktop only)
  window.addEventListener('mousemove', (e) => {
    if (window.innerWidth <= 768) return;
    const mouseX = (e.clientX / window.innerWidth - 0.5) * 8;
    const mouseY = (e.clientY / window.innerHeight - 0.5) * 8;
    
    bgLayerA.style.transform = `scale(1.02) translate(${mouseX * 0.3}px, ${mouseY * 0.3}px)`;
    bgLayerB.style.transform = `scale(1.02) translate(${mouseX * 0.3}px, ${mouseY * 0.3}px)`;
  });

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
  let introStartTime = performance.now();
  let loadingFinished = false;
  let displayedProgress = 0;
  let animFrameId = null;

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
    }, 180);
  }

  function skipLoadingSequence() {
    if (loadingFinished) return;
    displayedProgress = 100;
    finishLoadingSequence();
  }

  if (loaderSkipBtn) {
    loaderSkipBtn.addEventListener('click', skipLoadingSequence);
  }

  if (loaderVideo) {
    loaderVideo.play().catch(() => {});
    loaderVideo.addEventListener('ended', () => {
      finishLoadingSequence();
    });
  }

  function updateLoadingProgress(timestamp) {
    if (loadingFinished) return;

    const elapsed = timestamp - introStartTime;
    let targetProgress = 0;

    if (loaderVideo && loaderVideo.duration > 0 && !isNaN(loaderVideo.duration)) {
      const vidRatio = (loaderVideo.currentTime / loaderVideo.duration) * 100;
      const timeRatio = (elapsed / INTRO_DURATION_MS) * 100;
      targetProgress = Math.max(vidRatio, timeRatio);
    } else {
      targetProgress = (elapsed / INTRO_DURATION_MS) * 100;
    }

    targetProgress = Math.min(100, Math.max(0, targetProgress));
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

  // Initialize main menu
  selectMenuItem(0, false);

  // Start smooth progress loop
  introStartTime = performance.now();
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

  // Unlock Web Audio
  const unlockAudio = () => {
    initAudio();
    if (loadingFinished) {
      startBgMusic();
    }
  };
  window.addEventListener('click', unlockAudio, { once: true });
  window.addEventListener('keydown', unlockAudio, { once: true });
  window.addEventListener('pointerdown', unlockAudio, { once: true });
  window.addEventListener('touchstart', unlockAudio, { once: true });
  window.addEventListener('touchend', unlockAudio, { once: true });
});
'''

with open("app.js", "w", encoding="utf-8") as f:
    f.write(new_app_js)

print("app.js updated successfully with mobile cinematic background rotation!")
