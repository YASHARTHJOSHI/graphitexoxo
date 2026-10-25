# -*- coding: utf-8 -*-
"""
Python script to assemble the complete multi-page, multi-category architecture in index.html.
Preserves existing intro loader, video, audio, styles, and responsive layout.
"""

import re

# Read current index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Verify markers
start_marker = '<div class="pages-overlay-container" id="pagesContainer" aria-hidden="true">'
end_marker = '<!-- Notification Toast -->'

if start_marker not in content or end_marker not in content:
    print("Error: markers not found")
    exit(1)

# Generate HTML for all 5 hubs + 28 sub-pages + exit overlay
pages_html = '''  <div class="pages-overlay-container" id="pagesContainer" aria-hidden="true">

    <!-- ========================================================
         CATEGORY HUB 01: START HACKATHON (#hub-start)
         ======================================================== -->
    <article class="detail-page" id="hub-start" data-bg="assets/reference_spiderman_codes.png">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO MAIN MENU [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 01 // CATEGORY HUB</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">CATEGORY HUB</span>
            <span class="pill-badge blue">MAIN ARENA</span>
            <span class="pill-badge green">8–18 OCT REGISTRATION</span>
          </div>
          <h1 class="page-main-title">START HACKATHON // MISSION DEPLOYMENT</h1>
          <p class="page-tagline">SELECT A DOSSIER TERMINAL BELOW TO ACCESS COMPETITION PROTOCOLS</p>
          <p class="page-summary">
            Welcome to the main arena operations hub. Access specific information tracks below for eligibility, team formation, Round 1 PPT submission, competition domains, and Round 2 on-site rules.
          </p>
        </div>

        <div class="hub-card-grid">
          <button class="hub-mission-card" data-route="start/about-graphite">
            <span class="hub-card-index">01</span>
            <div class="hub-card-content">
              <span class="hub-card-title">ABOUT GRAPHITE</span>
              <span class="hub-card-sub">OVERVIEW · GEHU BHIMTAL · SPIDER-VERSE THEME</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="start/registration">
            <span class="hub-card-index">02</span>
            <div class="hub-card-content">
              <span class="hub-card-title">REGISTRATION & ELIGIBILITY</span>
              <span class="hub-card-sub">DATES 8–18 OCT · CAMPUSES · ₹1,200 ROUND 2 FEE</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="start/team-formation">
            <span class="hub-card-index">03</span>
            <div class="hub-card-content">
              <span class="hub-card-title">TEAM FORMATION</span>
              <span class="hub-card-sub">EXACTLY 4 MEMBERS · CROSS-CAMPUS COLLABORATION</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="start/round-1">
            <span class="hub-card-index">04</span>
            <div class="hub-card-content">
              <span class="hub-card-title">ROUND 1 — THE WEB SLINGERS</span>
              <span class="hub-card-sub">ONLINE PPT EVALUATION · 8 CORE PILLARS</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="start/tracks">
            <span class="hub-card-index">05</span>
            <div class="hub-card-content">
              <span class="hub-card-title">DOMAINS & TRACKS</span>
              <span class="hub-card-sub">AI/ML · WEB/APP · CYBER · IOT · WEB3 · OPEN</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="start/round-2">
            <span class="hub-card-index">06</span>
            <div class="hub-card-content">
              <span class="hub-card-title">ROUND 2 — INTO THE SPIDER-VERSE</span>
              <span class="hub-card-sub">24-HOUR OFFLINE ON-SITE HACKATHON · VENUE SPECS</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="start/ppt-template">
            <span class="hub-card-index">07</span>
            <div class="hub-card-content">
              <span class="hub-card-title">ROUND 1 PRESENTATION TEMPLATE</span>
              <span class="hub-card-sub">OFFICIAL GOOGLE SLIDES TEMPLATE & CHECKLIST</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
      </div>
    </article>

    <!-- 01.A: ABOUT GRAPHITE -->
    <article class="detail-page" id="page-start-about" data-bg="assets/reference_spiderman_codes.png">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="start">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 01.A // ABOUT GRAPHITE</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">FOUNDATION</span>
            <span class="pill-badge blue">GEHU BHIMTAL</span>
            <span class="pill-badge green">COMMUNITY DRIVEN</span>
          </div>
          <h1 class="page-main-title">ABOUT GRAPHITE '26</h1>
          <p class="page-tagline">STUDENT-DRIVEN HIMALAYAN TECH SUMMIT & HACKATHON</p>
          <p class="page-summary">
            GRAPHITE '26 is the flagship student-driven community hackathon hosted at Graphic Era Hill University, Bhimtal Campus. Designed to bridge academic theory and engineering reality, it brings together passionate student developers, designers, and problem solvers to build tangible solutions for pressing real-world challenges.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">THE SPIDER-VERSE METAPHOR</span>
              <span class="info-card-tag">CORE PHILOSOPHY</span>
            </div>
            <p class="info-card-text">
              In the Spider-Verse, diverse individuals across separate dimensions discover that their unique capabilities weave into an unstoppable web when united. At GRAPHITE '26, our theme mirrors this reality: developers, designers, hardware builders, and researchers combine their individual threads of skill into resilient, deployable systems.
            </p>
          </div>

          <div class="info-grid-2">
            <div class="info-card">
              <div class="info-card-header">
                <span class="info-card-title">CORE PURPOSE</span>
                <span class="info-card-tag">MISSION</span>
              </div>
              <p class="info-card-text">
                Move past toy projects and shallow landing pages. GRAPHITE '26 challenges participants to identify systemic root causes and engineer working prototypes with measurable impact.
              </p>
            </div>

            <div class="info-card">
              <div class="info-card-header">
                <span class="info-card-title">TWO-ROUND FORMAT</span>
                <span class="info-card-tag">STRUCTURE</span>
              </div>
              <p class="info-card-text">
                A selective two-tier competition: Round 1 evaluates conceptual depth, technical architecture, and feasibility via online PPT submissions. Shortlisted teams qualify for the intensive 24-hour on-site hackathon at GEHU Bhimtal.
              </p>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">READY TO ENTER THE ARENA?</div>
          <p class="cta-desc">Review eligibility criteria or proceed to team formation protocols.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="start/registration">
              <span>VIEW REGISTRATION PROTOCOLS</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="start">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 01.B: REGISTRATION & ELIGIBILITY -->
    <article class="detail-page" id="page-start-registration" data-bg="assets/reference_spiderman_codes.png">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="start">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 01.B // REGISTRATION & ELIGIBILITY</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">8–18 OCT 2026</span>
            <span class="pill-badge blue">QUALIFICATION PROTOCOL</span>
            <span class="pill-badge green">ROUND 1: FREE</span>
          </div>
          <h1 class="page-main-title">REGISTRATION & ELIGIBILITY</h1>
          <p class="page-tagline">OFFICIAL TIMELINES, INSTITUTION RULES & FEE STRUCTURE</p>
          <p class="page-summary">
            Ensure your squad meets all verified entry conditions prior to application. Round 1 evaluation is open and free of charge. Only squads selected for the on-site finals pay the Round 2 qualification fee.
          </p>
        </div>

        <div class="page-grid-metrics">
          <div class="pg-card">
            <span class="pg-label">REGISTRATION WINDOW</span>
            <span class="pg-val">8 – 18 OCT 2026</span>
            <span class="pg-sub">Online submission portal</span>
          </div>
          <div class="pg-card">
            <span class="pg-label">SHORTLIST ANNOUNCED</span>
            <span class="pg-val">21 OCT 2026</span>
            <span class="pg-sub">Round 2 finalists declared</span>
          </div>
          <div class="pg-card">
            <span class="pg-label">ROUND 1 ENTRY FEE</span>
            <span class="pg-val" style="color: var(--accent-green);">FREE (₹0)</span>
            <span class="pg-sub">Online PPT submission</span>
          </div>
          <div class="pg-card">
            <span class="pg-label">ROUND 2 TEAM FEE</span>
            <span class="pg-val">₹1,200 / SQUAD</span>
            <span class="pg-sub">Only for shortlisted teams</span>
          </div>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">ELIGIBLE INSTITUTIONS</span>
              <span class="info-card-tag">CAMPUS MATRIX</span>
            </div>
            <p class="info-card-text">
              Participation is confirmed for bonafide students of:
            </p>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">✓</span> Graphic Era Hill University (GEHU), Bhimtal Campus</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> Graphic Era Hill University (GEHU), Dehradun Campus</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> Graphic Era Hill University (GEHU), Haldwani Campus</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> Graphic Era Deemed to be University (GEU), Dehradun</div>
            </div>
            <p class="info-card-text" style="margin-top: 0.8rem; font-size: 0.88rem; color: var(--text-muted);">
              Notice: Outside-institution eligibility is not confirmed in the hacker guide. External applicants must contact organizers for clarification before applying.
            </p>
          </div>

          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">FEE TRANSPARENCY NOTICE</span>
              <span class="info-card-tag">₹1,200 PER TEAM</span>
            </div>
            <p class="info-card-text">
              The ₹1,200 team fee applies strictly to squads qualified for Round 2 to cover on-site infrastructure, Wi-Fi, accommodation, food, and facilities during the 24-hour hackathon. Submitting your Round 1 PPT does not incur any fee.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">APPLICATION DESTINATION</div>
          <p class="cta-desc">The official registration destination is awaiting final activation.</p>
          <div class="cta-row-buttons">
            <button class="action-btn btn-placeholder" disabled>
              <span>REGISTRATION LINK TO BE CONFIRMED (ANNOUNCEMENT PENDING)</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="start">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 01.C: TEAM FORMATION -->
    <article class="detail-page" id="page-start-team" data-bg="assets/reference_spiderman_codes.png">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="start">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 01.C // TEAM FORMATION</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">SQUAD RULE</span>
            <span class="pill-badge blue">EXACTLY 4 MEMBERS</span>
            <span class="pill-badge green">CROSS-CAMPUS OK</span>
          </div>
          <h1 class="page-main-title">TEAM FORMATION</h1>
          <p class="page-tagline">STRICT SQUAD COMPOSITION & ROLE DISTRIBUTION</p>
          <p class="page-summary">
            Every participating team must consist of exactly four student builders. No solo participants, pairs, or trios will be admitted. Construct a balanced roster that covers the complete engineering and presentation lifecycle.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">MANDATORY TEAM SIZE</span>
              <span class="info-card-tag">EXACTLY 4 MEMBERS</span>
            </div>
            <p class="info-card-text">
              The official guide establishes that team size is strictly four members. Ensure all four members' verified details (Full Name, Student ID, Campus, Email, Phone) are submitted accurately during registration.
            </p>
          </div>

          <div class="info-grid-2">
            <div class="info-card">
              <div class="info-card-header">
                <span class="info-card-title">CROSS-CAMPUS COLLABORATION</span>
                <span class="info-card-tag">ALLOWED</span>
              </div>
              <p class="info-card-text">
                Students from eligible campuses (GEHU Bhimtal, GEHU Dehradun, GEHU Haldwani, and GEU) may collaborate freely to form joint squads. Team up across disciplines and year levels.
              </p>
            </div>

            <div class="info-card">
              <div class="info-card-header">
                <span class="info-card-title">ROSTER STABILITY</span>
                <span class="info-card-tag">IDENTITY LOCK</span>
              </div>
              <p class="info-card-text">
                All members registered for Round 1 must be present for Round 2. If a member faces an unavoidable emergency, the team lead must contact the organizing team immediately.
              </p>
            </div>
          </div>

          <div class="info-card">
            <div class="info-card-header">
              <span class="info-card-title">RECOMMENDED SQUAD ROLES</span>
              <span class="info-card-tag">BALANCE MATRIX</span>
            </div>
            <div class="info-grid-2" style="margin-top: 0.8rem;">
              <div class="checklist-item"><span class="checklist-icon">01</span> <strong>Lead Architect & Backend:</strong> System design, APIs, database logic.</div>
              <div class="checklist-item"><span class="checklist-icon">02</span> <strong>Frontend / Client Engineer:</strong> UI implementation, interaction, mobile responsiveness.</div>
              <div class="checklist-item"><span class="checklist-icon">03</span> <strong>Specialist (AI/IoT/Cyber):</strong> Core algorithmic modeling, hardware interfacing, security.</div>
              <div class="checklist-item"><span class="checklist-icon">04</span> <strong>Product & Pitch Lead:</strong> UX workflow, problem validation, slide deck, demo narrative.</div>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">SQUAD READY? PREPARE ROUND 1 PPT</div>
          <p class="cta-desc">Review the 8 presentation pillars required for the online submission round.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="start/round-1">
              <span>EXPLORE ROUND 1 PROTOCOLS</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="start">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 01.D: ROUND 1 — THE WEB SLINGERS -->
    <article class="detail-page" id="page-start-round1" data-bg="assets/reference_spiderman_codes.png">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="start">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 01.D // ROUND 1 EVALUATION</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">ROUND 1</span>
            <span class="pill-badge blue">THE WEB SLINGERS</span>
            <span class="pill-badge green">ONLINE PPT SELECTION</span>
          </div>
          <h1 class="page-main-title">ROUND 1 — THE WEB SLINGERS</h1>
          <p class="page-tagline">ONLINE CONCEPTUAL EVALUATION & ARCHITECTURAL SCREENING</p>
          <p class="page-summary">
            Round 1 is a competitive presentation-based evaluation where squads submit their problem analysis, technical proposal, and architecture deck using the official template. Only high-caliber proposals advance to the on-site hackathon.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">THE 8 MANDATORY PRESENTATION PILLARS</span>
              <span class="info-card-tag">OFFICIAL STRUCTURE</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">1</span> <strong>Problem Statement:</strong> Clear, granular identification of the target real-world challenge.</div>
              <div class="checklist-item"><span class="checklist-icon">2</span> <strong>Proposed Solution:</strong> Concise explanation of your software/hardware mechanism.</div>
              <div class="checklist-item"><span class="checklist-icon">3</span> <strong>Key Features:</strong> Functional capabilities that directly address the core problem.</div>
              <div class="checklist-item"><span class="checklist-icon">4</span> <strong>Innovation & Originality:</strong> What makes this approach distinct from existing solutions?</div>
              <div class="checklist-item"><span class="checklist-icon">5</span> <strong>Technical Architecture & Stack:</strong> Concrete technologies, frameworks, APIs, and data flows.</div>
              <div class="checklist-item"><span class="checklist-icon">6</span> <strong>Impact & Scalability:</strong> Societal, economic, or industrial value and scaling potential.</div>
              <div class="checklist-item"><span class="checklist-icon">7</span> <strong>Feasibility & Execution:</strong> Realistic implementation plan within modern engineering constraints.</div>
              <div class="checklist-item"><span class="checklist-icon">8</span> <strong>Research & References:</strong> Cited data sources, academic papers, or industry benchmarks.</div>
            </div>
          </div>

          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">EVALUATION ADVICE & STANDARDS</span>
              <span class="info-card-tag">HIGH SIGNAL</span>
            </div>
            <p class="info-card-text">
              Generic, shallow AI-generated summaries and ordinary CRUD dashboards without real engineering insight will not pass evaluation. The selection panel seeks teams that investigate root causes, dissect existing market gaps, and justify the concrete technical novelty of their proposed architecture.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">OFFICIAL ROUND 1 PPT TEMPLATE</div>
          <p class="cta-desc">All submissions must strictly use the official Google Slides template.</p>
          <div class="cta-row-buttons">
            <a href="https://docs.google.com/presentation/d/1WQn2Az1YHpqFcdagdQt1FoSmZVFXa7jD/preview?usp=sharing" target="_blank" rel="noopener noreferrer" class="action-btn primary-action">
              <span>OPEN OFFICIAL PPT TEMPLATE (GOOGLE SLIDES)</span>
            </a>
            <button class="action-btn secondary-action" data-route="start/tracks">
              <span>VIEW COMPETITION DOMAINS</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 01.E: DOMAINS & TRACKS -->
    <article class="detail-page" id="page-start-tracks" data-bg="assets/reference_spiderman_codes.png">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="start">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 01.E // DOMAINS & TRACKS</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">5 SPECIALIZED TRACKS</span>
            <span class="pill-badge blue">OPEN INNOVATION</span>
            <span class="pill-badge green">CHOOSE 1 FOR ROUND 1</span>
          </div>
          <h1 class="page-main-title">DOMAINS & TRACKS</h1>
          <p class="page-tagline">SIX DISTINCT TECHNOLOGICAL CHALLENGE ARENAS</p>
          <p class="page-summary">
            Squads select one primary domain for their Round 1 presentation. If your innovation spans multiple sectors or introduces an entirely unconventional paradigm, select the Open Innovation category.
          </p>
        </div>

        <div class="tracks-card-grid">
          <div class="track-card">
            <div class="tc-num">TRACK 01</div>
            <div class="tc-title">ARTIFICIAL INTELLIGENCE & MACHINE LEARNING</div>
            <p class="tc-desc">
              Predictive models, neural architectures, computer vision, specialized LLM agents, and applied data science addressing real operational bottlenecks.
            </p>
            <div class="tc-tag">AI // ML // COMPUTER VISION // AGENTS</div>
          </div>

          <div class="track-card">
            <div class="tc-num">TRACK 02</div>
            <div class="tc-title">WEB & MOBILE APP DEVELOPMENT</div>
            <p class="tc-desc">
              High-performance web apps, cross-platform mobile solutions, resilient backends, real-time collaboration engines, and accessibility-first user interfaces.
            </p>
            <div class="tc-tag">FULL-STACK // MOBILE // CLOUD // DISTRIBUTED</div>
          </div>

          <div class="track-card">
            <div class="tc-num">TRACK 03</div>
            <div class="tc-title">CYBERSECURITY & THREAT DEFENSE</div>
            <p class="tc-desc">
              Offensive & defensive security utilities, vulnerability analyzers, cryptographic integrity tools, identity verification, and privacy preservation.
            </p>
            <div class="tc-tag">INFOSEC // CRYPTOGRAPHY // SECURE OPS</div>
          </div>

          <div class="track-card">
            <div class="tc-num">TRACK 04</div>
            <div class="tc-title">INTERNET OF THINGS & ROBOTICS</div>
            <p class="tc-desc">
              Embedded systems, sensor telemetries, microcontrollers, edge processing, environmental monitoring, smart automation, and robotics control.
            </p>
            <div class="tc-tag">HARDWARE // EMBEDDED // SENSORS // AUTOMATION</div>
          </div>

          <div class="track-card">
            <div class="tc-num">TRACK 05</div>
            <div class="tc-title">BLOCKCHAIN & WEB3 ARCHITECTURES</div>
            <p class="tc-desc">
              Smart contracts, decentralized registries, verifiable computation, supply chain provenance, and trustless governance tools.
            </p>
            <div class="tc-tag">SMART CONTRACTS // DECENTRALIZED // TRUSTLESS</div>
          </div>

          <div class="track-card" style="border-left: 3px solid var(--accent-gold);">
            <div class="tc-num" style="color: var(--accent-gold);">TRACK 06</div>
            <div class="tc-title">OPEN INNOVATION</div>
            <p class="tc-desc">
              For ambitious cross-disciplinary ideas, environmental solutions, fintech, or novel concepts that transcend conventional track boundaries.
            </p>
            <div class="tc-tag" style="color: var(--accent-gold);">INTERDISCIPLINARY // HYBRID // MOONSHOT</div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">UNDERSTAND ROUND 2 QUALIFICATION</div>
          <p class="cta-desc">Learn how selected teams transition from Round 1 tracks to on-site challenges.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="start/round-2">
              <span>EXPLORE ROUND 2 PROTOCOLS</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="start">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 01.F: ROUND 2 — INTO THE SPIDER-VERSE -->
    <article class="detail-page" id="page-start-round2" data-bg="assets/reference_spiderman_codes.png">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="start">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 01.F // ROUND 2 ON-SITE HACKATHON</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">ROUND 2</span>
            <span class="pill-badge blue">ON-SITE FINALS</span>
            <span class="pill-badge green">24-HOUR HACKATHON</span>
          </div>
          <h1 class="page-main-title">ROUND 2 — INTO THE SPIDER-VERSE</h1>
          <p class="page-tagline">24-HOUR OFFLINE HACKATHON AT GEHU BHIMTAL CAMPUS</p>
          <p class="page-summary">
            Shortlisted teams assemble at Graphic Era Hill University, Bhimtal (elevation 4,494.75 ft AMSL) for the high-intensity on-site hackathon. Fresh on-site challenge statements are revealed at the venue, and code must be authored live during the 24-hour sprint.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">CRITICAL DISTINCTION BETWEEN ROUNDS</span>
              <span class="info-card-tag">NEW PROBLEM SET</span>
            </div>
            <p class="info-card-text">
              <strong>Round 1 PPT work is NOT permission to submit a pre-built Round 2 project.</strong> In Round 2, a fresh set of on-site challenge problem statements is revealed directly at the venue. Shortlisted teams choose from these on-site challenges and must engineer their solution from scratch during the hackathon.
            </p>
          </div>

          <div class="info-grid-2">
            <div class="info-card">
              <div class="info-card-header">
                <span class="info-card-title">EXACT DURATION</span>
                <span class="info-card-tag">24 HOURS</span>
              </div>
              <p class="info-card-text">
                While the on-site event spans the calendar dates 27–28 October 2026, the actual coding sprint duration is strictly <strong>24 hours</strong>. Teams must manage sleep, sprint velocity, and debugging accordingly.
              </p>
            </div>

            <div class="info-card">
              <div class="info-card-header">
                <span class="info-card-title">LIVE GIT TRACKING</span>
                <span class="info-card-tag">VERIFICATION</span>
              </div>
              <p class="info-card-text">
                All development must be regularly committed to a public GitHub repository. Custom monitoring software is expected to verify commit timelines and prevent pre-built code injection.
              </p>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">REVIEW SUBMISSION PROTOCOLS</div>
          <p class="cta-desc">Inspect repository structures, README expectations, and Git guidelines.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="crunch/submission">
              <span>VIEW SUBMISSION GUIDELINES</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="start">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 01.G: ROUND 1 PRESENTATION TEMPLATE -->
    <article class="detail-page" id="page-start-template" data-bg="assets/reference_spiderman_codes.png">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="start">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 01.G // OFFICIAL PPT TEMPLATE</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">MANDATORY FORMAT</span>
            <span class="pill-badge blue">GOOGLE SLIDES</span>
            <span class="pill-badge green">8 PILLARS</span>
          </div>
          <h1 class="page-main-title">ROUND 1 PRESENTATION TEMPLATE</h1>
          <p class="page-tagline">OFFICIAL SLIDE DECK SPECIFICATIONS & PREPARATION GUIDANCE</p>
          <p class="page-summary">
            All Round 1 applicants must strictly structure their proposal inside the official GRAPHITE '26 Google Slides presentation template. Deviating from the required format risks immediate disqualification.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">SUBMISSION CHECKLIST</span>
              <span class="info-card-tag">REQUIRED SLIDES</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">01</span> Slide 1: Title, Team Name, Member IDs & Campus Affiliations.</div>
              <div class="checklist-item"><span class="checklist-icon">02</span> Slide 2: Problem Statement & Root Cause Evidence.</div>
              <div class="checklist-item"><span class="checklist-icon">03</span> Slide 3: Proposed Solution Mechanism & Value Proposition.</div>
              <div class="checklist-item"><span class="checklist-icon">04</span> Slide 4: Key Functional Features & Architecture Diagram.</div>
              <div class="checklist-item"><span class="checklist-icon">05</span> Slide 5: Innovation, Novelty & Differentiation from Existing Solutions.</div>
              <div class="checklist-item"><span class="checklist-icon">06</span> Slide 6: Technology Stack & Implementation Feasibility.</div>
              <div class="checklist-item"><span class="checklist-icon">07</span> Slide 7: Societal / Industrial Impact & Scalability Pathway.</div>
              <div class="checklist-item"><span class="checklist-icon">08</span> Slide 8: Research Citations, References & Team Contributions.</div>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">ACCESS OFFICIAL TEMPLATE LINK</div>
          <p class="cta-desc">Make a copy in Google Slides, populate with verified research, and export as PDF/link.</p>
          <div class="cta-row-buttons">
            <a href="https://docs.google.com/presentation/d/1WQn2Az1YHpqFcdagdQt1FoSmZVFXa7jD/preview?usp=sharing" target="_blank" rel="noopener noreferrer" class="action-btn primary-action">
              <span>OPEN GOOGLE SLIDES TEMPLATE</span>
            </a>
            <button class="action-btn secondary-action" data-back-route="start">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- ========================================================
         CATEGORY HUB 02: STORY MODE (#hub-story)
         ======================================================== -->
    <article class="detail-page" id="hub-story" data-bg="assets/reference_room_coding.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO MAIN MENU [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 02 // CATEGORY HUB</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">STORY MODE</span>
            <span class="pill-badge blue">THE CHRONICLES</span>
            <span class="pill-badge green">CONNECTING THREADS</span>
          </div>
          <h1 class="page-main-title">STORY MODE // ENTER THE SPIDER-VERSE</h1>
          <p class="page-tagline">THE NARRATIVE ARCHITECTURE & STUDENT BUILDER JOURNEY</p>
          <p class="page-summary">
            Discover the founding narrative, the Spider-Verse philosophy of interconnected talent, the structured 9-stage hackathon journey, and our long-term vision beyond the final pitch.
          </p>
        </div>

        <div class="hub-card-grid">
          <button class="hub-mission-card" data-route="story/origin">
            <span class="hub-card-index">01</span>
            <div class="hub-card-content">
              <span class="hub-card-title">THE ORIGIN STORY</span>
              <span class="hub-card-sub">STUDENT-DRIVEN VISION · REAL-WORLD PURPOSE</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="story/spider-verse">
            <span class="hub-card-index">02</span>
            <div class="hub-card-content">
              <span class="hub-card-title">THE SPIDER-VERSE</span>
              <span class="hub-card-sub">ABSTRACT WEB METAPHOR · INTERCONNECTED TALENT</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="story/journey">
            <span class="hub-card-index">03</span>
            <div class="hub-card-content">
              <span class="hub-card-title">YOUR HACKATHON JOURNEY</span>
              <span class="hub-card-sub">9 SEQUENTIAL MILESTONE STAGES · INTERACTIVE TRAIL</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="story/mission-objective">
            <span class="hub-card-index">04</span>
            <div class="hub-card-content">
              <span class="hub-card-title">YOUR MISSION OBJECTIVE</span>
              <span class="hub-card-sub">DEMONSTRABLE SOFTWARE & HARDWARE EXPECTATIONS</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="story/beyond-graphite">
            <span class="hub-card-index">05</span>
            <div class="hub-card-content">
              <span class="hub-card-title">BEYOND GRAPHITE</span>
              <span class="hub-card-sub">MENTOR MENTORSHIP & NATIONAL HACKATHON NOMINATIONS</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
      </div>
    </article>

    <!-- 02.A: THE ORIGIN STORY -->
    <article class="detail-page" id="page-story-origin" data-bg="assets/reference_room_coding.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="story">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 02.A // THE ORIGIN STORY</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">THE GENESIS</span>
            <span class="pill-badge blue">STUDENT LED</span>
            <span class="pill-badge green">BHIMTAL 4,494 FT</span>
          </div>
          <h1 class="page-main-title">THE ORIGIN STORY</h1>
          <p class="page-tagline">HOW GRAPHITE '26 EMERGED IN THE HIMALAYAN FOOTHILLS</p>
          <p class="page-summary">
            GRAPHITE was conceived by students at Graphic Era Hill University, Bhimtal who realized that textbook algorithms find their true meaning only when deployed against real-world friction. Set against serene pine forests and misty Himalayan peaks, it provides a sanctuary where builders transform curiosity into code.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">STUDENT-DRIVEN ETHOS</span>
              <span class="info-card-tag">GRASSROOTS</span>
            </div>
            <p class="info-card-text">
              Organized for students, by students. From challenge design to technical judging, the entire hackathon is curated to cultivate genuine builders rather than test-takers. Here, late-night debugging sessions forge lifelong partnerships.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">EXPLORE THE METAPHOR</div>
          <p class="cta-desc">Discover how the Spider-Verse philosophy inspires our technical community.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="story/spider-verse">
              <span>EXPLORE THE SPIDER-VERSE THEME</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="story">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 02.B: THE SPIDER-VERSE -->
    <article class="detail-page" id="page-story-verse" data-bg="assets/reference_room_coding.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="story">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 02.B // THE SPIDER-VERSE</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">ABSTRACT THEME</span>
            <span class="pill-badge blue">INTERCONNECTED THREADS</span>
            <span class="pill-badge green">COLLECTIVE RESILIENCE</span>
          </div>
          <h1 class="page-main-title">THE SPIDER-VERSE THEME</h1>
          <p class="page-tagline">IDEAS, PEOPLE, CODE & USERS AS CONNECTED WEBS</p>
          <p class="page-summary">
            A single strand of spider silk is microscopic and fragile. But woven geometrically into a web, it withstands mountain storms. At GRAPHITE '26, ideas, people, code, and users are the individual threads that connect into an unbreakable whole.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-grid-2">
            <div class="info-card accent-cyan">
              <div class="info-card-header">
                <span class="info-card-title">ORIGINAL WEB MOTIF</span>
                <span class="info-card-tag">BRAND IDENTITY</span>
              </div>
              <p class="info-card-text">
                GRAPHITE '26 utilizes original, abstract geometric web motifs symbolizing distributed systems, network nodes, and collaborative teamwork. We uphold ethical design principles and celebrate collective engineering over individual glory.
              </p>
            </div>

            <div class="info-card accent-red">
              <div class="info-card-header">
                <span class="info-card-title">CROSS-DISCIPLINARY WEAVING</span>
                <span class="info-card-tag">COLLABORATION</span>
              </div>
              <p class="info-card-text">
                No single discipline builds great software. Hardware hackers connect with front-end crafters; data researchers connect with UI strategists. The web holds because every node carries tension together.
              </p>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">FOLLOW THE TRAIL</div>
          <p class="cta-desc">Follow the 9 milestone stages of your hackathon campaign.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="story/journey">
              <span>VIEW HACKATHON JOURNEY</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="story">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 02.C: YOUR HACKATHON JOURNEY -->
    <article class="detail-page" id="page-story-journey" data-bg="assets/reference_room_coding.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="story">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 02.C // YOUR HACKATHON JOURNEY</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">CAMPAIGN ROADMAP</span>
            <span class="pill-badge blue">9 STAGES</span>
            <span class="pill-badge green">CLICK TO INSPECT</span>
          </div>
          <h1 class="page-main-title">YOUR HACKATHON JOURNEY</h1>
          <p class="page-tagline">THE NINE STRATEGIC PHASES FROM REGISTRATION TO RECOGNITION</p>
          <p class="page-summary">
            Your campaign at GRAPHITE '26 progresses through nine clearly defined stages. Click on any stage below to inspect its dedicated briefing terminal.
          </p>
        </div>

        <div class="journey-flow-grid">
          <div class="journey-step-row" data-route="start/registration">
            <span class="journey-step-num">01</span>
            <div class="journey-step-content">
              <div class="journey-step-title">REGISTRATION & SQUAD ASSEMBLY (8–18 OCT)</div>
              <div class="journey-step-desc">Register your 4-member squad from eligible campuses. Free Round 1 entry.</div>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>

          <div class="journey-step-row" data-route="start/round-1">
            <span class="journey-step-num">02</span>
            <div class="journey-step-content">
              <div class="journey-step-title">ROUND 1: PPT SUBMISSION</div>
              <div class="journey-step-desc">Submit your research and technical proposal using the official 8-pillar template.</div>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>

          <div class="journey-step-row" data-route="press/announcements">
            <span class="journey-step-num">03</span>
            <div class="journey-step-content">
              <div class="journey-step-title">SHORTLIST ANNOUNCEMENT (21 OCT)</div>
              <div class="journey-step-desc">Evaluation panel reveals the qualified squads advancing to the on-site finals.</div>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>

          <div class="journey-step-row" data-route="chill/workshops">
            <span class="journey-step-num">04</span>
            <div class="journey-step-content">
              <div class="journey-step-title">WORKSHOPS & LEARNING (26 OCT)</div>
              <div class="journey-step-desc">Pre-hackathon workshops and technical briefings at GEHU Bhimtal (optional attendance).</div>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>

          <div class="journey-step-row" data-route="start/round-2">
            <span class="journey-step-num">05</span>
            <div class="journey-step-content">
              <div class="journey-step-title">ROUND 2: ON-SITE PROBLEM SELECTION (27 OCT)</div>
              <div class="journey-step-desc">Fresh problem statements revealed at venue. Squads analyze and lock their target problem.</div>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>

          <div class="journey-step-row" data-route="crunch/timeline">
            <span class="journey-step-num">06</span>
            <div class="journey-step-content">
              <div class="journey-step-title">24-HOUR DEVELOPMENT SPRINT (27–28 OCT)</div>
              <div class="journey-step-desc">Code authored live on-site with regular Git commits tracked by monitoring systems.</div>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>

          <div class="journey-step-row" data-route="crunch/submission">
            <span class="journey-step-num">07</span>
            <div class="journey-step-content">
              <div class="journey-step-title">FINAL PROJECT SUBMISSION</div>
              <div class="journey-step-desc">Public GitHub repository lock, README documentation, and deployment check.</div>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>

          <div class="journey-step-row" data-route="crunch/judging">
            <span class="journey-step-num">08</span>
            <div class="journey-step-content">
              <div class="journey-step-title">JURY EVALUATION & WORKING DEMO</div>
              <div class="journey-step-desc">Live presentation and code demonstration across 5 official criteria.</div>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>

          <div class="journey-step-row" data-route="press/prizes">
            <span class="journey-step-num">09</span>
            <div class="journey-step-content">
              <div class="journey-step-title">RESULTS & PRIZE DISTRIBUTION</div>
              <div class="journey-step-desc">Closing ceremony, recognition, and allocation of ₹1,00,000+ total prize pool.</div>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </div>
      </div>
    </article>

    <!-- 02.D: YOUR MISSION OBJECTIVE -->
    <article class="detail-page" id="page-story-objective" data-bg="assets/reference_room_coding.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="story">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 02.D // MISSION OBJECTIVE</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">CORE MANDATE</span>
            <span class="pill-badge blue">DEMONSTRABLE PROTOTYPE</span>
            <span class="pill-badge green">HIGH RIGOR</span>
          </div>
          <h1 class="page-main-title">YOUR MISSION OBJECTIVE</h1>
          <p class="page-tagline">BUILD ORIGINAL, TECHNICALLY SOUND & WORKING SYSTEMS</p>
          <p class="page-summary">
            The core expectation of GRAPHITE '26 is unambiguous: every squad must build an original, technically meaningful, and demonstrable solution for a verified real problem. Superficial mockups without backend integration will not suffice.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-grid-2">
            <div class="info-card accent-cyan">
              <div class="info-card-header">
                <span class="info-card-title">WORKING CODE REQUIRED</span>
                <span class="info-card-tag">NO SMOKE & MIRRORS</span>
              </div>
              <p class="info-card-text">
                Your demonstration must run live. Judges will interact with the system, test edge cases, and inspect the underlying codebase. Ensure dependencies build cleanly and APIs respond reliably.
              </p>
            </div>

            <div class="info-card accent-red">
              <div class="info-card-header">
                <span class="info-card-title">AUTHENTIC UNDERSTANDING</span>
                <span class="info-card-tag">AUTHORSHIP</span>
              </div>
              <p class="info-card-text">
                While open-source libraries and AI assistants are permitted, every team member must be able to explain the architectural design choices, algorithms, and logic in their submission.
              </p>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">BEYOND THE ARENA</div>
          <p class="cta-desc">Learn how top GRAPHITE '26 projects receive post-event mentorship.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="story/beyond-graphite">
              <span>EXPLORE OPPORTUNITIES BEYOND GRAPHITE</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="story">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 02.E: BEYOND GRAPHITE -->
    <article class="detail-page" id="page-story-beyond" data-bg="assets/reference_room_coding.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="story">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 02.E // BEYOND GRAPHITE</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">INCUBATION</span>
            <span class="pill-badge blue">MENTOR SUPPORT</span>
            <span class="pill-badge green">NATIONAL NOMINATIONS</span>
          </div>
          <h1 class="page-main-title">BEYOND GRAPHITE</h1>
          <p class="page-tagline">INCUBATION, MENTORSHIP & NATIONAL-LEVEL NOMINATIONS</p>
          <p class="page-summary">
            The hackathon does not end with the awards ceremony. Selected high-potential projects and stand-out presentations may receive continued mentor guidance to refine their prototypes into production-grade systems or venture-backed concepts.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">NATIONAL HACKATHON NOMINATIONS</span>
              <span class="info-card-tag">OPPORTUNITY PATHWAY</span>
            </div>
            <p class="info-card-text">
              Selected top teams with demonstrated technical excellence and validated impact may be recommended and nominated for prestigious national-level hackathons and competitions following structured refinement with faculty and industry mentors.
            </p>
            <p class="info-card-text" style="margin-top: 0.8rem; font-size: 0.88rem; color: var(--accent-gold);">
              Notice: These follow-up opportunities and nominations depend on post-event evaluation, prototype maturity, and mentor review, and are not guaranteed to any team.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">OFFICIAL INTELLIGENCE</div>
          <p class="cta-desc">Review verified announcements, prize distributions, and official channels.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="press">
              <span>VISIT DAILY BUGLE PRESS PASS</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="story">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- ========================================================
         CATEGORY HUB 03: DAILY BUGLE PRESS PASS (#hub-press)
         ======================================================== -->
    <article class="detail-page" id="hub-press" data-bg="assets/reference_spiderman_editorial.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO MAIN MENU [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 03 // CATEGORY HUB</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">PRESS PASS</span>
            <span class="pill-badge blue">VERIFIED INTEL</span>
            <span class="pill-badge green">TOTAL POOL ₹1,00,000+</span>
          </div>
          <h1 class="page-main-title">DAILY BUGLE PRESS PASS // OFFICIAL INTELLIGENCE</h1>
          <p class="page-tagline">EVENT ANNOUNCEMENTS, CONFIRMED PRIZES & OFFICIAL CHANNELS</p>
          <p class="page-summary">
            Directly inspect verified intelligence for GRAPHITE '26. View confirmed prize pools, participant perks, mentorship networks, and join the official community communication channels.
          </p>
        </div>

        <div class="hub-card-grid">
          <button class="hub-mission-card" data-route="press/announcements">
            <span class="hub-card-index">01</span>
            <div class="hub-card-content">
              <span class="hub-card-title">MISSION BRIEFINGS & ANNOUNCEMENTS</span>
              <span class="hub-card-sub">CONFIRMED MILESTONES VS PENDING NOTICES</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="press/prizes">
            <span class="hub-card-index">02</span>
            <div class="hub-card-content">
              <span class="hub-card-title">PRIZES & PERKS</span>
              <span class="hub-card-sub">CONFIRMED ₹1,00,000+ POOL · GOODIES & CERTIFICATES</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="press/mentorship">
            <span class="hub-card-index">03</span>
            <div class="hub-card-content">
              <span class="hub-card-title">MENTORS & JUDGES</span>
              <span class="hub-card-sub">INDUSTRY NETWORK (TCS, AMI, COGNIZANT & AMAZON)</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="press/official-channels">
            <span class="hub-card-index">04</span>
            <div class="hub-card-content">
              <span class="hub-card-title">OFFICIAL CHANNELS</span>
              <span class="hub-card-sub">INSTAGRAM (@GRAPHITE.XO) · WHATSAPP · EMAIL</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
      </div>
    </article>

    <!-- 03.A: MISSION BRIEFINGS / ANNOUNCEMENTS -->
    <article class="detail-page" id="page-press-announcements" data-bg="assets/reference_spiderman_editorial.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="press">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 03.A // DISPATCHES & ANNOUNCEMENTS</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">VERIFIED DISPATCH</span>
            <span class="pill-badge blue">LIVE BULLETIN</span>
            <span class="pill-badge green">OCTOBER 2026</span>
          </div>
          <h1 class="page-main-title">MISSION BRIEFINGS & ANNOUNCEMENTS</h1>
          <p class="page-tagline">CURRENT VERIFIED INTELLIGENCE & STATUS UPDATES</p>
          <p class="page-summary">
            Transparency is a founding tenet of GRAPHITE '26. Review all confirmed milestones alongside parameters that remain pending final committee announcement.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">CONFIRMED EVENT DATES</span>
              <span class="info-card-tag">OFFICIAL</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>8–18 October 2026:</strong> Official Online Registration Window.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>21 October 2026:</strong> Shortlisted Round 2 Finalists Announcement.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>26 October 2026:</strong> Pre-hackathon Workshops & Tech Briefings (Optional).</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>27–28 October 2026:</strong> Round 2 On-Site 24-Hour Hackathon at GEHU Bhimtal.</div>
            </div>
          </div>

          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">STATUS: AWAITING ANNOUNCEMENT</span>
              <span class="info-card-tag">PENDING CONFIRMATION</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">⏳</span> <strong>Exact Clock Schedule:</strong> Daily check-in hour, opening ceremony time, and presentation slots remain TBD.</div>
              <div class="checklist-item"><span class="checklist-icon">⏳</span> <strong>Prize Breakup:</strong> Exact distribution between cash awards and sponsor credits is pending publication.</div>
              <div class="checklist-item"><span class="checklist-icon">⏳</span> <strong>Travel Reaching Guide:</strong> Detailed shuttle and transit instructions to Bhimtal will be shared before the event.</div>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">STAY SYNCHRONIZED</div>
          <p class="cta-desc">Join our official WhatsApp group for instant notifications.</p>
          <div class="cta-row-buttons">
            <a href="https://chat.whatsapp.com/HA71ajtj1bkLNJ2MQAGIyN" target="_blank" rel="noopener noreferrer" class="action-btn primary-action">
              <span>JOIN OFFICIAL WHATSAPP GROUP</span>
            </a>
            <button class="action-btn secondary-action" data-back-route="press">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 03.B: PRIZES & PERKS -->
    <article class="detail-page" id="page-press-prizes" data-bg="assets/reference_spiderman_editorial.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="press">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 03.B // PRIZES & PERKS</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">REWARDS</span>
            <span class="pill-badge blue">TOTAL POOL ₹1,00,000+</span>
            <span class="pill-badge green">ALL FINALISTS PERKS</span>
          </div>
          <h1 class="page-main-title">PRIZES & PERKS</h1>
          <p class="page-tagline">OFFICIALLY ANNOUNCED ₹1,00,000+ COMBINED PRIZE POOL</p>
          <p class="page-summary">
            GRAPHITE '26 features a confirmed total prize pool exceeding <strong>₹1,00,000</strong>, encompassing competitive cash rewards and valuable in-kind developer tooling. Every participating finalist receives verified certificates and perks.
          </p>
        </div>

        <div class="page-grid-metrics">
          <div class="pg-card">
            <span class="pg-label">ANNOUNCED PRIZE POOL</span>
            <span class="pg-val" style="color: var(--accent-gold);">₹1,00,000+</span>
            <span class="pg-sub">Cash awards & in-kind tooling</span>
          </div>
          <div class="pg-card">
            <span class="pg-label">PARTICIPATION PERK</span>
            <span class="pg-val">CERTIFICATES</span>
            <span class="pg-sub">All shortlisted finalists</span>
          </div>
          <div class="pg-card">
            <span class="pg-label">HOSPITALITY PERK</span>
            <span class="pg-val">FOOD & STAY</span>
            <span class="pg-sub">Covered during Round 2</span>
          </div>
          <div class="pg-card">
            <span class="pg-label">SWAG & GOODIES</span>
            <span class="pg-val">GRAPHITE KIT</span>
            <span class="pg-sub">Badges, stickers & sponsor swag</span>
          </div>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">CONFIRMED PARTICIPANT BENEFITS</span>
              <span class="info-card-tag">ROUND 2 FINALISTS</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">✓</span> Official Participation Certificates acknowledging hackathon finalists.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> High-speed campus Wi-Fi and power facilities during the 24-hour sprint.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> Nutritious meals, midnight refreshments, and ongoing hydration.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> Secure accommodation provided at GEHU Bhimtal campus.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> Direct 1-on-1 mentorship interactions with visiting industry engineers.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> Potential nomination for national-level innovation competitions for top prototypes.</div>
            </div>
            <p class="info-card-text" style="margin-top: 0.8rem; font-size: 0.88rem; color: var(--text-muted);">
              Notice: The precise numerical distribution of the ₹1,00,000+ pool between 1st, 2nd, 3rd places and track prizes has not yet been announced in the official guide.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">MENTOR SUPPORT</div>
          <p class="cta-desc">Discover the industry organizations supporting participants.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="press/mentorship">
              <span>VIEW MENTORS & INDUSTRY NETWORK</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="press">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 03.C: MENTORS & JUDGES -->
    <article class="detail-page" id="page-press-mentors" data-bg="assets/reference_spiderman_editorial.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="press">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 03.C // MENTORS & JUDGES</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">INDUSTRY ALLIANCE</span>
            <span class="pill-badge blue">TECH SUPPORT</span>
            <span class="pill-badge green">PITCH GUIDANCE</span>
          </div>
          <h1 class="page-main-title">MENTORS & JUDGES</h1>
          <p class="page-tagline">INDUSTRY NETWORK & ARCHITECTURAL GUIDANCE</p>
          <p class="page-summary">
            Participants in Round 2 will have access to mentorship support to navigate system architecture, debugging bottlenecks, and pitch articulation.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">ASSOCIATED INDUSTRY NETWORK</span>
              <span class="info-card-tag">MENTOR ECOSYSTEM</span>
            </div>
            <p class="info-card-text">
              Industry organizations referenced in the official hacker guide include professionals from:
            </p>
            <div class="checklist-box" style="margin-top: 0.8rem;">
              <div class="checklist-item"><span class="checklist-icon">◆</span> <strong>Tata Consultancy Services (TCS)</strong></div>
              <div class="checklist-item"><span class="checklist-icon">◆</span> <strong>American Megatrends (AMI)</strong></div>
              <div class="checklist-item"><span class="checklist-icon">◆</span> <strong>Cognizant</strong></div>
              <div class="checklist-item"><span class="checklist-icon">◆</span> <strong>Amazon</strong></div>
              <div class="checklist-item"><span class="checklist-icon">◆</span> <strong>Miro</strong></div>
              <div class="checklist-item"><span class="checklist-icon">◆</span> <strong>ruinrun.ai</strong></div>
              <div class="checklist-item"><span class="checklist-icon">◆</span> <strong>Resolve AI</strong></div>
            </div>
            <p class="info-card-text" style="margin-top: 0.8rem; font-size: 0.88rem; color: var(--text-muted);">
              Notice: The finalized roster of individual mentor profiles, speaker sessions, and judging panel members is awaiting announcement. Individual profiles will be published once officially confirmed.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">COMMUNICATION CHANNELS</div>
          <p class="cta-desc">Connect directly with organizing leads on official channels.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="press/official-channels">
              <span>VIEW OFFICIAL CHANNELS</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="press">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 03.D: OFFICIAL CHANNELS -->
    <article class="detail-page" id="page-press-channels" data-bg="assets/reference_spiderman_editorial.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="press">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 03.D // OFFICIAL CHANNELS</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">VERIFIED LINKS</span>
            <span class="pill-badge blue">COMMUNITY HUB</span>
            <span class="pill-badge green">DIRECT ACCESS</span>
          </div>
          <h1 class="page-main-title">OFFICIAL CHANNELS</h1>
          <p class="page-tagline">DIRECT DISPATCHES, SOCIAL DISCUSSIONS & CONTACT POINTS</p>
          <p class="page-summary">
            Connect directly with verified GRAPHITE '26 communication endpoints. Avoid third-party rumors and rely only on official links.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-grid-3">
            <div class="info-card accent-red">
              <div class="info-card-header">
                <span class="info-card-title">INSTAGRAM</span>
                <span class="info-card-tag">SOCIAL HUB</span>
              </div>
              <p class="info-card-text">
                Visual dispatches, teaser drops, and event reels.
              </p>
              <div style="margin-top: 1rem;">
                <a href="https://www.instagram.com/graphite.xo/" target="_blank" rel="noopener noreferrer" class="action-btn primary-action" style="padding: 0.6rem 1rem; font-size: 0.85rem;">
                  <span>@GRAPHITE.XO</span>
                </a>
              </div>
            </div>

            <div class="info-card accent-cyan">
              <div class="info-card-header">
                <span class="info-card-title">WHATSAPP</span>
                <span class="info-card-tag">PARTICIPANTS</span>
              </div>
              <p class="info-card-text">
                Real-time participant community, queries, and team coordination.
              </p>
              <div style="margin-top: 1rem;">
                <a href="https://chat.whatsapp.com/HA71ajtj1bkLNJ2MQAGIyN" target="_blank" rel="noopener noreferrer" class="action-btn primary-action" style="padding: 0.6rem 1rem; font-size: 0.85rem;">
                  <span>JOIN GROUP</span>
                </a>
              </div>
            </div>

            <div class="info-card">
              <div class="info-card-header">
                <span class="info-card-title">OFFICIAL EMAIL</span>
                <span class="info-card-tag">SUPPORT</span>
              </div>
              <p class="info-card-text">
                Formal queries, institution verifications, and sponsorships.
              </p>
              <div style="margin-top: 1rem;">
                <a href="mailto:graphite2k26@gmail.com" class="action-btn secondary-action" style="padding: 0.6rem 1rem; font-size: 0.85rem;">
                  <span>GRAPHITE2K26@GMAIL.COM</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">EXPLORE CRUNCH MODE</div>
          <p class="cta-desc">Review competition protocols, timelines, and Git submission guidelines.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="crunch">
              <span>ENTER CRUNCH MODE // LOAD STATE</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="press">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- ========================================================
         CATEGORY HUB 04: CRUNCH MODE // LOAD STATE (#hub-crunch)
         ======================================================== -->
    <article class="detail-page" id="hub-crunch" data-bg="assets/reference_spiderman_surprised.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO MAIN MENU [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 04 // CATEGORY HUB</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">CRUNCH MODE</span>
            <span class="pill-badge blue">COMPETITION SPECS</span>
            <span class="pill-badge green">24-HOUR SPRINT</span>
          </div>
          <h1 class="page-main-title">CRUNCH MODE // SYSTEM STATUS</h1>
          <p class="page-tagline">COMPETITION PROTOCOLS, TIMELINES, GIT RULES & FAQ</p>
          <p class="page-summary">
            Technical build guidelines, real-time Git commit monitoring, judging criteria, and comprehensive FAQ answering verified event logistics.
          </p>
        </div>

        <div class="hub-card-grid">
          <button class="hub-mission-card" data-route="crunch/timeline">
            <span class="hub-card-index">01</span>
            <div class="hub-card-content">
              <span class="hub-card-title">TIMELINE & EVENT SCHEDULE</span>
              <span class="hub-card-sub">24-HOUR HACKATHON TIMELINE (27–28 OCT)</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="crunch/judging">
            <span class="hub-card-index">02</span>
            <div class="hub-card-content">
              <span class="hub-card-title">JUDGING CRITERIA</span>
              <span class="hub-card-sub">5 OFFICIAL EVALUATION PILLARS</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="crunch/submission">
            <span class="hub-card-index">03</span>
            <div class="hub-card-content">
              <span class="hub-card-title">SUBMISSION GUIDELINES</span>
              <span class="hub-card-sub">GITHUB REPOSITORY & README CHECKLIST</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="crunch/git-protocol">
            <span class="hub-card-index">04</span>
            <div class="hub-card-content">
              <span class="hub-card-title">GIT & DEVELOPMENT PROTOCOL</span>
              <span class="hub-card-sub">LIVE COMMITS · ANTI-PLAGIARISM MONITORING</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="crunch/preflight">
            <span class="hub-card-index">05</span>
            <div class="hub-card-content">
              <span class="hub-card-title">PRE-FLIGHT CHECKLIST</span>
              <span class="hub-card-sub">TOOLING SETUP · EXTENSION BOARD · HARDWARE</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="crunch/faq">
            <span class="hub-card-index">06</span>
            <div class="hub-card-content">
              <span class="hub-card-title">VERIFIED FAQ</span>
              <span class="hub-card-sub">11 VERIFIED QUESTIONS & ANSWERS FROM GUIDE</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
      </div>
    </article>

    <!-- 04.A: TIMELINE & EVENT SCHEDULE -->
    <article class="detail-page" id="page-crunch-timeline" data-bg="assets/reference_spiderman_surprised.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="crunch">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 04.A // TIMELINE & EVENT SCHEDULE</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">EVENT SCHEDULE</span>
            <span class="pill-badge blue">24-HOUR CODING DURATION</span>
            <span class="pill-badge green">OCTOBER 2026</span>
          </div>
          <h1 class="page-main-title">TIMELINE & EVENT SCHEDULE</h1>
          <p class="page-tagline">OFFICIAL HACKATHON CALENDAR & DURATION BOUNDARIES</p>
          <p class="page-summary">
            Review the confirmed competition dates. Note that while the on-site event spans 27–28 October, the actual hackathon coding duration is strictly <strong>24 hours</strong>.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">CONFIRMED MILESTONE SCHEDULE</span>
              <span class="info-card-tag">OFFICIAL DATES</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">01</span> <strong>8 – 18 October 2026:</strong> Registrations Open (Round 1 Online PPT Submissions).</div>
              <div class="checklist-item"><span class="checklist-icon">02</span> <strong>21 October 2026:</strong> Shortlisted Round 2 Finalists Announced.</div>
              <div class="checklist-item"><span class="checklist-icon">03</span> <strong>26 October 2026:</strong> Pre-Hackathon Workshops & Briefings at GEHU Bhimtal (Attendance Optional).</div>
              <div class="checklist-item"><span class="checklist-icon">04</span> <strong>27 – 28 October 2026:</strong> On-Site 24-Hour Offline Hackathon (Round 2).</div>
            </div>
          </div>

          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">DAILY SCHEDULE NOTICE</span>
              <span class="info-card-tag">TBD</span>
            </div>
            <p class="info-card-text">
              The exact clock times for participant reporting, opening ceremony, problem statement reveal, mentoring rounds, final code freeze, and evaluation slots are currently <strong>To be announced</strong> by the organizing committee.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">CHECK JUDGING CRITERIA</div>
          <p class="cta-desc">Understand how your prototype will be evaluated by the jury.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="crunch/judging">
              <span>VIEW JUDGING CRITERIA</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="crunch">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 04.B: JUDGING CRITERIA -->
    <article class="detail-page" id="page-crunch-judging" data-bg="assets/reference_spiderman_surprised.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="crunch">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 04.B // JUDGING CRITERIA</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">EVALUATION</span>
            <span class="pill-badge blue">5 CRITERIA</span>
            <span class="pill-badge green">OBJECTIVE REVIEW</span>
          </div>
          <h1 class="page-main-title">JUDGING CRITERIA</h1>
          <p class="page-tagline">THE FIVE OFFICIAL DIMENSIONS OF SYSTEM EVALUATION</p>
          <p class="page-summary">
            Prototypes submitted in Round 2 are evaluated by a multidisciplinary jury across five official pillars established in the GRAPHITE '26 Hacker Guide.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">THE FIVE CORE CRITERIA</span>
              <span class="info-card-tag">OFFICIAL MATRIX</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">01</span> <strong>Innovation and Originality:</strong> Novelty of the approach, uniqueness of the architecture, and departure from routine solutions.</div>
              <div class="checklist-item"><span class="checklist-icon">02</span> <strong>Technical Complexity and Execution:</strong> Architectural depth, effective utilization of algorithms, APIs, database modeling, and code hygiene.</div>
              <div class="checklist-item"><span class="checklist-icon">03</span> <strong>Real-World Impact and Relevance:</strong> Practical utility, scalability, and measurable effectiveness in solving the chosen problem statement.</div>
              <div class="checklist-item"><span class="checklist-icon">04</span> <strong>UI/UX and Usability:</strong> Design intuition, user flow coherence, mobile responsiveness, error handling, and visual clarity.</div>
              <div class="checklist-item"><span class="checklist-icon">05</span> <strong>Presentation and Demonstration:</strong> Coherence of the live demo, clarity of technical articulation, and ability to address jury questions.</div>
            </div>
            <p class="info-card-text" style="margin-top: 0.8rem; font-size: 0.88rem; color: var(--text-muted);">
              Notice: The precise numerical percentage weightages for each criterion have not been published in the official guide. Focus on balanced excellence across all five pillars.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">PREPARE DELIVERABLES</div>
          <p class="cta-desc">Review the required project artifacts and GitHub repo structure.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="crunch/submission">
              <span>VIEW SUBMISSION GUIDELINES</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="crunch">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 04.C: SUBMISSION GUIDELINES -->
    <article class="detail-page" id="page-crunch-submission" data-bg="assets/reference_spiderman_surprised.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="crunch">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 04.C // SUBMISSION GUIDELINES</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">ROUND 2</span>
            <span class="pill-badge blue">DELIVERABLES</span>
            <span class="pill-badge green">PUBLIC REPO</span>
          </div>
          <h1 class="page-main-title">SUBMISSION GUIDELINES</h1>
          <p class="page-tagline">MANDATORY PROJECT ARTIFACTS FOR JURY EVALUATION</p>
          <p class="page-summary">
            At the conclusion of the 24-hour development sprint, squads must submit their deliverables via the designated portal. Ensure all required components are completed before the deadline.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">SUBMISSION CHECKLIST</span>
              <span class="info-card-tag">MANDATORY ARTIFACTS</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>Project Title:</strong> Concise, descriptive name for your solution.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>One-Line Pitch:</strong> High-impact summary explaining the value proposition.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>Public GitHub Repository:</strong> Accessible repository containing all project source code.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>README Documentation:</strong> Detailed document covering problem overview, solution architecture, tech stack, API documentation, and local execution instructions.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>Working Demonstrable Prototype:</strong> Live web app, mobile build, CLI tool, or hardware demo that runs before the jury.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>Presentation Deck:</strong> Concise slide deck explaining the problem, architecture, business value, and demo flow.</div>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">REVIEW GIT POLICIES</div>
          <p class="cta-desc">Learn about commit tracking and open-source disclosure rules.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="crunch/git-protocol">
              <span>INSPECT GIT & DEV PROTOCOL</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="crunch">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 04.D: GIT & DEVELOPMENT PROTOCOL -->
    <article class="detail-page" id="page-crunch-git" data-bg="assets/reference_spiderman_surprised.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="crunch">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 04.D // GIT PROTOCOL</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">VERSION CONTROL</span>
            <span class="pill-badge blue">LIVE COMMITS</span>
            <span class="pill-badge green">COMMIT TRACKING</span>
          </div>
          <h1 class="page-main-title">GIT & DEVELOPMENT PROTOCOL</h1>
          <p class="page-tagline">STRICT CODE AUTHORSHIP RULES & AUTOMATED VERIFICATION</p>
          <p class="page-summary">
            All code for Round 2 must be written on-site during the 24-hour hackathon. Custom-built monitoring software is expected to track Git commit velocity and detect pre-built codebase injections.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">MANDATORY DEVELOPMENT POLICIES</span>
              <span class="info-card-tag">COMPLIANCE RULES</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">01</span> <strong>On-Site Coding Only:</strong> All source code for the chosen Round 2 problem must be authored during the hackathon. Pre-built codebases are strictly prohibited.</div>
              <div class="checklist-item"><span class="checklist-icon">02</span> <strong>Frequent Git Commits:</strong> Squads must push incremental commits throughout the event. Sudden monolithic commits of thousands of lines at the end will trigger investigation.</div>
              <div class="checklist-item"><span class="checklist-icon">03</span> <strong>Commit Tracking Software:</strong> Custom-built monitoring software is expected to check Git commits and verify continuous development activity.</div>
              <div class="checklist-item"><span class="checklist-icon">04</span> <strong>Third-Party & AI Tools:</strong> Open-source libraries, public APIs, and AI coding assistants are permitted provided they are fully disclosed in the README and understood by the team.</div>
              <div class="checklist-item"><span class="checklist-icon">05</span> <strong>Authorship Accountability:</strong> Team members must be capable of explaining every module and architectural decision in their submission.</div>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">PREPARE YOUR MACHINE</div>
          <p class="cta-desc">Review the hardware and software checklist before arriving on campus.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="crunch/preflight">
              <span>VIEW PRE-FLIGHT CHECKLIST</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="crunch">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 04.E: PRE-FLIGHT CHECKLIST -->
    <article class="detail-page" id="page-crunch-preflight" data-bg="assets/reference_spiderman_surprised.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="crunch">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 04.E // PRE-FLIGHT CHECKLIST</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">HARDWARE & SETUP</span>
            <span class="pill-badge blue">DEV ENVIRONMENT</span>
            <span class="pill-badge green">PRE-FLIGHT</span>
          </div>
          <h1 class="page-main-title">PRE-FLIGHT CHECKLIST</h1>
          <p class="page-tagline">ENVIRONMENT PREPARATION & ESSENTIAL EQUIPMENT</p>
          <p class="page-summary">
            Arrive fully prepared. Configure development toolchains and install heavy packages in advance to avoid wasting bandwidth during the opening hours of the hackathon.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-grid-2">
            <div class="info-card accent-cyan">
              <div class="info-card-header">
                <span class="info-card-title">DEV ENVIRONMENT (SOFTWARE)</span>
                <span class="info-card-tag">CONFIGURE IN ADVANCE</span>
              </div>
              <div class="checklist-box">
                <div class="checklist-item"><span class="checklist-icon">✓</span> Git installed, configured with SSH keys, and verified with GitHub.</div>
                <div class="checklist-item"><span class="checklist-icon">✓</span> Node.js, Python, Docker, or runtime frameworks pre-installed.</div>
                <div class="checklist-item"><span class="checklist-icon">✓</span> Heavy packages and SDK dependencies cached locally.</div>
                <div class="checklist-item"><span class="checklist-icon">✓</span> Preferred IDE (VS Code, Cursor, JetBrains) updated and ready.</div>
              </div>
            </div>

            <div class="info-card accent-red">
              <div class="info-card-header">
                <span class="info-card-title">HARDWARE & GEAR</span>
                <span class="info-card-tag">BRING YOUR OWN</span>
              </div>
              <div class="checklist-box">
                <div class="checklist-item"><span class="checklist-icon">✓</span> Laptops and original charging adapters for all 4 members.</div>
                <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>Power Extension Board:</strong> Mandatory to bring your own board.</div>
                <div class="checklist-item"><span class="checklist-icon">✓</span> Any required microcontrollers (Arduino, ESP32, Raspberry Pi) and sensors.</div>
                <div class="checklist-item"><span class="checklist-icon">✓</span> External mouse, keyboards, or testing smartphones.</div>
              </div>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">HAVE QUESTIONS?</div>
          <p class="cta-desc">Review the official FAQ answering verified logistics.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="crunch/faq">
              <span>EXPLORE VERIFIED FAQ</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="crunch">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 04.F: FAQ -->
    <article class="detail-page" id="page-crunch-faq" data-bg="assets/reference_spiderman_surprised.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="crunch">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 04.F // FREQUENTLY ASKED QUESTIONS</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">FAQ</span>
            <span class="pill-badge blue">VERIFIED FACTS ONLY</span>
            <span class="pill-badge green">HACKER GUIDE</span>
          </div>
          <h1 class="page-main-title">FREQUENTLY ASKED QUESTIONS</h1>
          <p class="page-tagline">OFFICIAL CLARIFICATIONS DIRECTLY FROM THE HACKER GUIDE</p>
          <p class="page-summary">
            All answers below are derived strictly from confirmed documentation. No speculative or fabricated rules are included.
          </p>
        </div>

        <div class="faq-grid">
          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q01</span> Who is eligible to participate?</div>
            <div class="faq-a">Bonafide students from GEHU Bhimtal, GEHU Dehradun, GEHU Haldwani, and Graphic Era University. Outside-institution eligibility is not confirmed in the guide and must be verified with organizers.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q02</span> What is the required squad size?</div>
            <div class="faq-a">Exactly four members per team. No solo entries, pairs, or trios will be permitted.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q03</span> Are cross-campus teams permitted?</div>
            <div class="faq-a">Yes. Students across eligible Graphic Era campuses may freely collaborate to form a squad.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q04</span> Is attendance on the 26 October workshop day mandatory?</div>
            <div class="faq-a">No. The official FAQ explicitly states that attending the workshop day is optional.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q05</span> Is there a registration fee?</div>
            <div class="faq-a">Round 1 PPT submission is free. A registration fee of ₹1,200 per team applies strictly to squads shortlisted for Round 2.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q06</span> Are meals and accommodation provided during Round 2?</div>
            <div class="faq-a">Yes. Accommodation, food, water, and medical aid are provided on-site at the GEHU Bhimtal campus.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q07</span> Do participants need to bring their own hardware?</div>
            <div class="faq-a">Yes. Bring your own laptops, chargers, specialized hardware/sensors, and power extension boards.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q08</span> Can AI tools and open-source libraries be used?</div>
            <div class="faq-a">Yes, provided they are disclosed in the README and team members can explain the implementation.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q09</span> What happens if a team member cannot attend Round 2?</div>
            <div class="faq-a">Team leads must inform the organizing committee immediately for review and guidance.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q10</span> Is the Round 2 problem statement known in advance?</div>
            <div class="faq-a">No. A fresh set of on-site problem statements will be revealed directly at the venue during the event.</div>
          </div>

          <div class="faq-card">
            <div class="faq-q"><span class="faq-q-badge">Q11</span> When will the exact daily schedule and prize breakdown be released?</div>
            <div class="faq-a">These details are pending final confirmation and will be published across official communication channels prior to the event.</div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">EXPLORE CHILL ZONE</div>
          <p class="cta-desc">Review venue logistics, facilities, packing list, and support.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="chill">
              <span>VISIT CHILL ZONE // WEB HAMMOCK</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="crunch">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- ========================================================
         CATEGORY HUB 05: CHILL ZONE // WEB HAMMOCK (#hub-chill)
         ======================================================== -->
    <article class="detail-page" id="hub-chill" data-bg="assets/reference_spiderman_web.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO MAIN MENU [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 05 // CATEGORY HUB</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">CHILL ZONE</span>
            <span class="pill-badge blue">VENUE & LOGISTICS</span>
            <span class="pill-badge green">BHIMTAL 4,494 FT</span>
          </div>
          <h1 class="page-main-title">CHILL ZONE // WEB HAMMOCK</h1>
          <p class="page-tagline">VENUE SERVICES, PACKING LIST, WORKSHOPS & COMMUNITY SUPPORT</p>
          <p class="page-summary">
            The practical, human side of GRAPHITE '26. Access venue navigation, accommodation facilities, packing requirements, workshops, and official support contacts.
          </p>
        </div>

        <div class="hub-card-grid">
          <button class="hub-mission-card" data-route="chill/workshops">
            <span class="hub-card-index">01</span>
            <div class="hub-card-content">
              <span class="hub-card-title">WORKSHOPS & SESSIONS</span>
              <span class="hub-card-sub">26 OCT PRE-HACKATHON SESSIONS (ATTENDANCE OPTIONAL)</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="chill/venue">
            <span class="hub-card-index">02</span>
            <div class="hub-card-content">
              <span class="hub-card-title">VENUE & TRAVEL</span>
              <span class="hub-card-sub">GEHU BHIMTAL (4,494 FT AMSL) · GOOGLE MAPS NAVIGATION</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="chill/facilities">
            <span class="hub-card-index">03</span>
            <div class="hub-card-content">
              <span class="hub-card-title">FOOD, ACCOMMODATION & FACILITIES</span>
              <span class="hub-card-sub">WI-FI · MEALS · RECOVERY ZONES · MEDICAL HELPDESK</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="chill/packing-list">
            <span class="hub-card-index">04</span>
            <div class="hub-card-content">
              <span class="hub-card-title">WHAT TO BRING (PACKING LIST)</span>
              <span class="hub-card-sub">MANDATORY COLLEGE ID · CONSENT FORM · EXTENSION BOARD</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="chill/community">
            <span class="hub-card-index">05</span>
            <div class="hub-card-content">
              <span class="hub-card-title">NETWORKING & COMMUNITY</span>
              <span class="hub-card-sub">DEVELOPER MIXER · MENTOR CONNECTIONS</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <button class="hub-mission-card" data-route="chill/contact">
            <span class="hub-card-index">06</span>
            <div class="hub-card-content">
              <span class="hub-card-title">CONTACT & SUPPORT</span>
              <span class="hub-card-sub">ORGANIZING DESK · WHATSAPP · EMAIL ESCALATION</span>
            </div>
            <svg class="hub-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
      </div>
    </article>

    <!-- 05.A: WORKSHOPS & SESSIONS -->
    <article class="detail-page" id="page-chill-workshops" data-bg="assets/reference_spiderman_web.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="chill">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 05.A // WORKSHOPS & SESSIONS</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">26 OCT 2026</span>
            <span class="pill-badge blue">OPTIONAL ATTENDANCE</span>
            <span class="pill-badge green">PREPARATION DAY</span>
          </div>
          <h1 class="page-main-title">WORKSHOPS & SESSIONS</h1>
          <p class="page-tagline">PRE-HACKATHON SKILL ELEVATION & TECHNICAL BRIEFINGS</p>
          <p class="page-summary">
            Scheduled for 26 October 2026, the workshop day provides an opportunity to interact with visiting mentors, inspect campus infrastructure, and refine development toolchains before the 24-hour sprint.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">WORKSHOP PARAMETERS</span>
              <span class="info-card-tag">OFFICIAL FAQ NOTE</span>
            </div>
            <p class="info-card-text">
              Attendance at the workshop sessions is <strong>optional</strong>. Teams arriving on campus early are encouraged to attend to familiarize themselves with lab setups and connect with peer builders.
            </p>
            <p class="info-card-text" style="margin-top: 0.8rem; font-size: 0.88rem; color: var(--text-muted);">
              Notice: The detailed hourly schedule and topics for individual workshop tracks are awaiting announcement.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">PLAN YOUR TRAVEL</div>
          <p class="cta-desc">Review venue coordinates and campus address at Bhimtal.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="chill/venue">
              <span>VIEW VENUE & TRAVEL GUIDE</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="chill">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 05.B: VENUE & TRAVEL -->
    <article class="detail-page" id="page-chill-venue" data-bg="assets/reference_spiderman_web.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="chill">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 05.B // VENUE & TRAVEL</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">HOST CAMPUS</span>
            <span class="pill-badge blue">4,494.75 FT ELEVATION</span>
            <span class="pill-badge green">BHIMTAL, UTTARAKHAND</span>
          </div>
          <h1 class="page-main-title">VENUE & TRAVEL</h1>
          <p class="page-tagline">GRAPHIC ERA HILL UNIVERSITY · BHIMTAL CAMPUS</p>
          <p class="page-summary">
            Nestled at an elevation of 4,494.75 feet above sea level in the Kumaon Himalayas, GEHU Bhimtal provides an idyllic mountain backdrop for 24 hours of focused coding, debugging, and innovation.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">OFFICIAL POSTAL ADDRESS</span>
              <span class="info-card-tag">CAMPUS LOCATION</span>
            </div>
            <p class="info-card-text" style="font-size: 1.05rem; font-weight: 600; color: #ffffff;">
              Graphic Era Hill University, Bhimtal Campus<br>
              SatTal Road, Nagri Gaon, Bhimtal,<br>
              District Nainital, Uttarakhand – 263136
            </p>
          </div>

          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">TRANSIT & REACHING GUIDELINES</span>
              <span class="info-card-tag">STATUS: PENDING</span>
            </div>
            <p class="info-card-text">
              Nearest railhead: Kathgodam Railway Station (~22 km). Nearest airport: Pantnagar Airport (~55 km). Local transit and detailed shuttle pickup schedules will be published across official channels before the event.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">OPEN MAP NAVIGATION</div>
          <p class="cta-desc">View verified campus location on Google Maps.</p>
          <div class="cta-row-buttons">
            <a href="https://www.google.com/maps/place/Graphic+Era+Hill+University+-+Bhimtal+Campus/@29.375376,79.5308465,17z/" target="_blank" rel="noopener noreferrer" class="action-btn primary-action">
              <span>OPEN GOOGLE MAPS PIN</span>
            </a>
            <button class="action-btn secondary-action" data-back-route="chill">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 05.C: FOOD, ACCOMMODATION & FACILITIES -->
    <article class="detail-page" id="page-chill-facilities" data-bg="assets/reference_spiderman_web.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="chill">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 05.C // FACILITIES & HOSPITALITY</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">HOSPITALITY</span>
            <span class="pill-badge blue">INCLUDED IN ROUND 2</span>
            <span class="pill-badge green">CAMPUS SUPPORT</span>
          </div>
          <h1 class="page-main-title">FOOD, ACCOMMODATION & FACILITIES</h1>
          <p class="page-tagline">OFFICIALLY CONFIRMED ON-SITE PROVISIONS</p>
          <p class="page-summary">
            Participants qualified for Round 2 will receive on-site hospitality to ensure focus throughout the 24-hour competition.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">CONFIRMED AMENITIES</span>
              <span class="info-card-tag">HACKER GUIDE SPECS</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>High-Speed Wi-Fi:</strong> Dedicated campus connectivity across hackathon labs.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>Meals & Refreshments:</strong> Nutritious meals, snacks, coffee, and drinking water provided throughout the event.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>Accommodation:</strong> Resting facilities provided on-site for participating squads.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>Medical Support & Helpdesk:</strong> On-call first-aid assistance and round-the-clock student helpdesk.</div>
              <div class="checklist-item"><span class="checklist-icon">⚡</span> <strong>Power Policy:</strong> Dedicated wall sockets provided, but participants <strong>must bring their own power extension boards</strong>.</div>
            </div>
            <p class="info-card-text" style="margin-top: 0.8rem; font-size: 0.88rem; color: var(--text-muted);">
              Notice: Specific hostel room allocations and exact meal serving hours will be briefed during check-in.
            </p>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">PREPARE YOUR PACKING LIST</div>
          <p class="cta-desc">Ensure you have all mandatory documentation before travelling.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="chill/packing-list">
              <span>VIEW WHAT TO BRING (PACKING LIST)</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="chill">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 05.D: WHAT TO BRING -->
    <article class="detail-page" id="page-chill-packing" data-bg="assets/reference_spiderman_web.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="chill">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 05.D // WHAT TO BRING</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">MANDATORY ENTRY</span>
            <span class="pill-badge blue">ORIGINAL ID REQUIRED</span>
            <span class="pill-badge green">CHECKLIST</span>
          </div>
          <h1 class="page-main-title">WHAT TO BRING (PACKING LIST)</h1>
          <p class="page-tagline">STRICT ENTRY DOCUMENTATION & TECHNICAL EQUIPMENT</p>
          <p class="page-summary">
            Review the official checklist before departure. Participants without verified identification will not be granted campus entry under any circumstances.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-card accent-red">
            <div class="info-card-header">
              <span class="info-card-title">MANDATORY ENTRY DOCUMENTS</span>
              <span class="info-card-tag">NO ENTRY WITHOUT THESE</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">⚠️</span> <strong>Original College ID Card:</strong> Physical, bonafide institutional identity card is strictly required for campus admission.</div>
              <div class="checklist-item"><span class="checklist-icon">⚠️</span> <strong>Signed Undertaking & Consent Form:</strong> One signed copy per squad member (format provided upon shortlist announcement).</div>
            </div>
          </div>

          <div class="info-card accent-cyan">
            <div class="info-card-header">
              <span class="info-card-title">ESSENTIAL TECHNICAL HARDWARE</span>
              <span class="info-card-tag">EQUIPMENT</span>
            </div>
            <div class="checklist-box">
              <div class="checklist-item"><span class="checklist-icon">✓</span> Laptops and original power bricks.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> <strong>Power Extension Board:</strong> Minimum 3-4 socket extension per team.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> Prototyping hardware, microcontrollers, jumper cables, and sensors if competing in IoT/hardware.</div>
              <div class="checklist-item"><span class="checklist-icon">✓</span> Personal warm clothing suitable for Himalayan autumn evenings (~15°C / 59°F).</div>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">COMMUNITY & SOCIALS</div>
          <p class="cta-desc">Connect with the student builders attending GRAPHITE '26.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="chill/community">
              <span>VIEW COMMUNITY & NETWORKING</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="chill">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 05.E: NETWORKING & COMMUNITY -->
    <article class="detail-page" id="page-chill-community" data-bg="assets/reference_spiderman_web.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="chill">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 05.E // COMMUNITY & NETWORKING</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">COMMUNITY</span>
            <span class="pill-badge blue">ECOSYSTEM</span>
            <span class="pill-badge green">COLLABORATION</span>
          </div>
          <h1 class="page-main-title">NETWORKING & COMMUNITY</h1>
          <p class="page-tagline">FORGING LASTING BONDS ABOVE 4,494 FEET IN THE CLOUDS</p>
          <p class="page-summary">
            A hackathon is more than a race against the clock; it is an incubator for lasting developer friendships, co-founder connections, and mentor partnerships that continue long after the final commit.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-grid-2">
            <div class="info-card accent-cyan">
              <div class="info-card-header">
                <span class="info-card-title">CROSS-CAMPUS EXCHANGE</span>
                <span class="info-card-tag">CONNECTIONS</span>
              </div>
              <p class="info-card-text">
                Engage with peers from Dehradun, Bhimtal, and Haldwani campuses. Exchange code patterns, discuss emerging stacks, and explore future collaborative research.
              </p>
            </div>

            <div class="info-card accent-red">
              <div class="info-card-header">
                <span class="info-card-title">INDUSTRY EXPOSURE</span>
                <span class="info-card-tag">ENGAGEMENT</span>
              </div>
              <p class="info-card-text">
                Showcase your problem-solving depth directly to visiting industry mentors and alumni who understand the grit required to build functional software under pressure.
              </p>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">OFFICIAL CONTACT DETAILS</div>
          <p class="cta-desc">Access direct organizing desk email and escalation channels.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-route="chill/contact">
              <span>VIEW CONTACT & SUPPORT</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="chill">
              <span>RETURN TO CATEGORY HUB [ESC]</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- 05.F: CONTACT & SUPPORT -->
    <article class="detail-page" id="page-chill-contact" data-bg="assets/reference_spiderman_web.jpg">
      <div class="page-backdrop"></div>
      <div class="page-scroller">
        <header class="page-top-hud">
          <button class="back-to-menu-btn" data-back-route="chill">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
            <span>RETURN TO CATEGORY [ESC]</span>
          </button>
          <div class="page-hud-tag">MISSION 05.F // CONTACT & SUPPORT</div>
        </header>

        <div class="page-hero">
          <div class="page-badge-row">
            <span class="pill-badge red">DIRECT DESK</span>
            <span class="pill-badge blue">HELPDESK</span>
            <span class="pill-badge green">CONFIRMED ENDPOINTS</span>
          </div>
          <h1 class="page-main-title">CONTACT & SUPPORT</h1>
          <p class="page-tagline">OFFICIAL ORGANIZING COMMITTEE CHANNELS</p>
          <p class="page-summary">
            Have questions regarding campus eligibility, team formation, or technical submissions? Contact the core organizing desk through verified channels.
          </p>
        </div>

        <div class="info-section-group">
          <div class="info-grid-3">
            <div class="info-card accent-cyan">
              <div class="info-card-header">
                <span class="info-card-title">EMAIL DESK</span>
                <span class="info-card-tag">PRIMARY</span>
              </div>
              <p class="info-card-text">
                For administrative, eligibility, and formal inquiries.
              </p>
              <div style="margin-top: 1rem;">
                <a href="mailto:graphite2k26@gmail.com" class="action-btn primary-action" style="padding: 0.6rem 1rem; font-size: 0.85rem;">
                  <span>GRAPHITE2K26@GMAIL.COM</span>
                </a>
              </div>
            </div>

            <div class="info-card accent-red">
              <div class="info-card-header">
                <span class="info-card-title">INSTAGRAM</span>
                <span class="info-card-tag">DIRECT MESSAGE</span>
              </div>
              <p class="info-card-text">
                Direct messages and prompt visual announcements.
              </p>
              <div style="margin-top: 1rem;">
                <a href="https://www.instagram.com/graphite.xo/" target="_blank" rel="noopener noreferrer" class="action-btn primary-action" style="padding: 0.6rem 1rem; font-size: 0.85rem;">
                  <span>@GRAPHITE.XO</span>
                </a>
              </div>
            </div>

            <div class="info-card">
              <div class="info-card-header">
                <span class="info-card-title">WHATSAPP</span>
                <span class="info-card-tag">COMMUNITY</span>
              </div>
              <p class="info-card-text">
                Instant group discussions with fellow hackathon builders.
              </p>
              <div style="margin-top: 1rem;">
                <a href="https://chat.whatsapp.com/HA71ajtj1bkLNJ2MQAGIyN" target="_blank" rel="noopener noreferrer" class="action-btn primary-action" style="padding: 0.6rem 1rem; font-size: 0.85rem;">
                  <span>JOIN CHAT</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <div class="page-cta-section">
          <div class="cta-title">RETURN TO MAIN MENU</div>
          <p class="cta-desc">Resume session overview or explore other category terminals.</p>
          <div class="cta-row-buttons">
            <button class="action-btn primary-action" data-back-route="">
              <span>RETURN TO MAIN MENU [ESC]</span>
            </button>
            <button class="action-btn secondary-action" data-back-route="chill">
              <span>RETURN TO CATEGORY HUB</span>
            </button>
          </div>
        </div>
      </div>
    </article>

    <!-- ========================================
         EXIT CONSOLE CONFIRMATION OVERLAY (#page-exit)
         ======================================== -->
    <article class="detail-page exit-page-view" id="page-exit" data-bg="assets/reference_spiderman_codes.png">
      <div class="page-backdrop"></div>
      <div class="exit-dialog-centered">
        <div class="exit-card">
          <div class="exit-crest">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path>
              <line x1="12" y1="2" x2="12" y2="12"></line>
            </svg>
          </div>
          <h2 class="exit-title">LEAVE CURRENT SESSION?</h2>
          <p class="exit-desc">
            Return to the main terminal screen or continue browsing the GRAPHITE '26 mission dossiers.
          </p>
          <div class="exit-actions">
            <button class="action-btn secondary-action" data-back-route="">
              <span>CANCEL / STAY IN SESSION</span>
            </button>
            <button class="action-btn primary-action" data-back-route="" style="background: var(--accent-red);">
              <span>RETURN TO MAIN MENU</span>
            </button>
          </div>
        </div>
      </div>
    </article>

  </div>'''

# Replace from start_marker to before end_marker
start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"Error: markers not found (start: {start_idx}, end: {end_idx})")
    exit(1)

new_content = content[:start_idx] + pages_html + "\n\n  " + content[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("index.html updated successfully with all 5 Category Hubs and 28 Dedicated Pages!")
