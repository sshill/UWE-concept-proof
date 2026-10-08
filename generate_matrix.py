import subprocess
import os

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1660" width="2400" height="1660">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050912"/>
      <stop offset="40%" stop-color="#091322"/>
      <stop offset="100%" stop-color="#0b172a"/>
    </linearGradient>

    <!-- Card Backgrounds -->
    <linearGradient id="cardGradCyan" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0e1f36" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#081424" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="cardGradAmber" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e1a12" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#120f0a" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="cardGradEmerald" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0d2424" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#061617" stop-opacity="0.96"/>
    </linearGradient>

    <!-- Accent Gradients -->
    <linearGradient id="accentCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e5ff"/>
      <stop offset="100%" stop-color="#0088ff"/>
    </linearGradient>
    <linearGradient id="accentAmber" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffb703"/>
      <stop offset="100%" stop-color="#fb8500"/>
    </linearGradient>
    <linearGradient id="accentEmerald" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="100%" stop-color="#05b292"/>
    </linearGradient>

    <!-- Tactical Grid Pattern -->
    <pattern id="tacticalGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#162b45" stroke-width="0.6" stroke-opacity="0.35"/>
      <circle cx="40" cy="40" r="1.2" fill="#00d2ff" fill-opacity="0.18"/>
    </pattern>
  </defs>

  <style>
    .font-sans { font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Consolas', 'Roboto Mono', 'Courier New', monospace; }
  </style>

  <!-- Base Canvas -->
  <rect width="2400" height="1660" fill="url(#bgGrad)"/>
  <rect width="2400" height="1660" fill="url(#tacticalGrid)"/>

  <!-- Top Tactical Accent Bar -->
  <rect x="0" y="0" width="2400" height="7" fill="url(#accentCyan)"/>

  <!-- ==================== HEADER SECTION ==================== -->
  <g transform="translate(80, 52)">
    <!-- Miltech Badge -->
    <rect x="0" y="0" width="300" height="34" rx="6" fill="#002b4d" stroke="#00a8e8" stroke-width="1.3"/>
    <text x="150" y="22" fill="#00e5ff" class="font-sans" font-size="14" font-weight="700" letter-spacing="2.5" text-anchor="middle">MILTECH ARCHITECTURE</text>
    
    <!-- Title -->
    <text x="0" y="78" fill="#ffffff" class="font-sans" font-size="44" font-weight="900" letter-spacing="0.5">THE UWE USV 6-CHARACTER TAXONOMY BREAKDOWN</text>
    
    <!-- Subtitle with formula -->
    <text x="0" y="118" fill="#94a3b8" class="font-sans" font-size="21">
      Dual-Read Hardware Abstraction Matrix for Autonomous Surface Warfare:
    </text>
    <!-- Highlighted Formula Tokens -->
    <g transform="translate(780, 95)">
      <rect x="0" y="0" width="115" height="34" rx="6" fill="#003459" stroke="#00e5ff" stroke-width="1.4"/>
      <text x="57" y="23" fill="#00e5ff" class="font-mono" font-size="19" font-weight="bold" text-anchor="middle">[ A H ]</text>
      
      <text x="135" y="24" fill="#64748b" class="font-sans" font-size="22" font-weight="bold">—</text>
      
      <rect x="158" y="0" width="115" height="34" rx="6" fill="#422e0a" stroke="#ffb703" stroke-width="1.4"/>
      <text x="215" y="23" fill="#ffb703" class="font-mono" font-size="19" font-weight="bold" text-anchor="middle">[ D E ]</text>
      
      <text x="293" y="24" fill="#64748b" class="font-sans" font-size="22" font-weight="bold">—</text>
      
      <rect x="316" y="0" width="115" height="34" rx="6" fill="#064035" stroke="#00f5d4" stroke-width="1.4"/>
      <text x="373" y="23" fill="#00f5d4" class="font-mono" font-size="19" font-weight="bold" text-anchor="middle">[ P C ]</text>
    </g>
  </g>

  <!-- ==================== COLUMN 1: [AH] HYDRODYNAMICS ==================== -->
  <g transform="translate(75, 195)">
    <!-- Card Frame (width 725, height 1390) -->
    <rect width="725" height="1390" rx="16" fill="url(#cardGradCyan)" stroke="#1a3b66" stroke-width="2"/>
    <rect x="0" y="0" width="725" height="70" rx="16" fill="#0c233c" stroke="#00a8e8" stroke-width="1.4"/>
    <path d="M 0 52 L 0 70 L 725 70 L 725 52 Z" fill="#0c233c"/>
    
    <!-- Card Header Badge & Title -->
    <rect x="22" y="16" width="100" height="38" rx="6" fill="#00e5ff" fill-opacity="0.2" stroke="#00e5ff" stroke-width="1.6"/>
    <text x="72" y="42" fill="#00e5ff" class="font-mono" font-size="21" font-weight="bold" text-anchor="middle">[ A H ]</text>
    <text x="140" y="42" fill="#ffffff" class="font-sans" font-size="22" font-weight="bold" letter-spacing="0.5">OCTET 1: HYDRODYNAMICS</text>

    <!-- SECTION A: AQUATIC OPERATING DOMAIN -->
    <g transform="translate(22, 84)">
      <rect width="680" height="44" rx="6" fill="#102a48" stroke="#1f4b7a" stroke-width="1.2"/>
      <text x="18" y="28" fill="#00e5ff" class="font-sans" font-size="17.5" font-weight="bold" letter-spacing="1.5">A : AQUATIC OPERATING DOMAIN</text>

      <!-- Items Container (5 items, row height 68px, gap 8px -> step 76px) -->
      <!-- Item F -->
      <g transform="translate(0, 52)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#003459" stroke="#00a8e8" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00e5ff" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">F</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Fluvial &amp; Estuary</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Rivers, deltas, zero salinity, shallow draft &lt; 1m</text>
      </g>
      <!-- Item L -->
      <g transform="translate(0, 126)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#003459" stroke="#00a8e8" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00e5ff" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">L</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Littoral Brown-Water</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Coastal bays, sounds, surf zones, Sea State 1–2</text>
      </g>
      <!-- Item S -->
      <g transform="translate(0, 200)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#003459" stroke="#00a8e8" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00e5ff" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">S</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Shelf Green-Water</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Marginal continental seas, steep chop, Sea State 3–4</text>
      </g>
      <!-- Item P -->
      <g transform="translate(0, 274)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#003459" stroke="#00a8e8" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00e5ff" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">P</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Pelagic Deep-Sea</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Open trans-basin, water depth &gt; 200m, Sea State 4–5</text>
      </g>
      <!-- Item O -->
      <g transform="translate(0, 348)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#003459" stroke="#00a8e8" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00e5ff" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">O</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Oceanic Blue-Water</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Global oceanic swells, infinite endurance, Sea State 6+</text>
      </g>
    </g>

    <!-- SECTION H: HULL SEAKEEPING REGIME -->
    <g transform="translate(22, 524)">
      <rect width="680" height="44" rx="6" fill="#102a48" stroke="#1f4b7a" stroke-width="1.2"/>
      <text x="18" y="28" fill="#00e5ff" class="font-sans" font-size="17.5" font-weight="bold" letter-spacing="1.5">H : HULL SEAKEEPING REGIME</text>

      <!-- Items Container (7 items, row height 66px, step 74px) -->
      <!-- Item P -->
      <g transform="translate(0, 52)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#08233d" stroke="#0284c7" stroke-width="1.5"/>
        <text x="36" y="41" fill="#38bdf8" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">P</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Planing Monohull</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">High-speed stepped sprint (45–55+ kts terminal intercept)</text>
      </g>
      <!-- Item R -->
      <g transform="translate(0, 126)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#08233d" stroke="#0284c7" stroke-width="1.5"/>
        <text x="36" y="41" fill="#38bdf8" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">R</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">RIB Collar Sponson</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Foam/pneumatic collar, unsinkable reserve buoyancy</text>
      </g>
      <!-- Item D -->
      <g transform="translate(0, 200)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#08233d" stroke="#0284c7" stroke-width="1.5"/>
        <text x="36" y="41" fill="#38bdf8" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">D</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Displacement Hull</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Maximum fuel transit efficiency &amp; heavy kinetic payload</text>
      </g>
      <!-- Item W -->
      <g transform="translate(0, 274)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#08233d" stroke="#0284c7" stroke-width="1.5"/>
        <text x="36" y="41" fill="#38bdf8" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">W</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Wave-Piercing Cat/Tri</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Axe-bow multihull, suppresses vertical wave slamming shock</text>
      </g>
      <!-- Item F -->
      <g transform="translate(0, 348)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#08233d" stroke="#0284c7" stroke-width="1.5"/>
        <text x="36" y="41" fill="#38bdf8" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">F</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Hydrofoil Lift</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Submerged dynamic wings elevate hull above wave crests</text>
      </g>
      <!-- Item C -->
      <g transform="translate(0, 422)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#08233d" stroke="#0284c7" stroke-width="1.5"/>
        <text x="36" y="41" fill="#38bdf8" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">C</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Air-Cushion (ACV)</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Amphibious hovercraft traversing mudflats, surf zone &amp; ice</text>
      </g>
      <!-- Item G -->
      <g transform="translate(0, 496)">
        <rect width="680" height="66" rx="6" fill="#0a192c" stroke="#163252" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#08233d" stroke="#0284c7" stroke-width="1.5"/>
        <text x="36" y="41" fill="#38bdf8" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">G</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Ground-Effect (WIG)</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Wing-in-ground dynamic aerodynamic cushion skimmer</text>
      </g>
    </g>

    <!-- Hydrodynamic Note at bottom of card 1 -->
    <g transform="translate(22, 1140)">
      <rect width="680" height="116" rx="8" fill="#04223d" stroke="#00a8e8" stroke-width="1.3" stroke-dasharray="5 4"/>
      <text x="22" y="32" fill="#00e5ff" class="font-sans" font-size="16.5" font-weight="bold" letter-spacing="1">HYDRODYNAMIC COUPLING ARCHITECTURE</text>
      <text x="22" y="62" fill="#f1f5f9" class="font-sans" font-size="16">
        Domain (A) and Hull (H) define environmental survivability.
      </text>
      <text x="22" y="88" fill="#cbd5e1" class="font-sans" font-size="16">
        Selection locks the maximum operational sea state and transit speed envelope.
      </text>
    </g>
  </g>

  <!-- ==================== COLUMN 2: [DE] LOGISTICS & POWERPLANT ==================== -->
  <g transform="translate(838, 195)">
    <!-- Card Frame -->
    <rect width="725" height="1390" rx="16" fill="url(#cardGradAmber)" stroke="#523e16" stroke-width="2"/>
    <rect x="0" y="0" width="725" height="70" rx="16" fill="#2d2008" stroke="#d97706" stroke-width="1.4"/>
    <path d="M 0 52 L 0 70 L 725 70 L 725 52 Z" fill="#2d2008"/>
    
    <!-- Card Header Badge & Title -->
    <rect x="22" y="16" width="100" height="38" rx="6" fill="#ffb703" fill-opacity="0.2" stroke="#ffb703" stroke-width="1.6"/>
    <text x="72" y="42" fill="#ffb703" class="font-mono" font-size="21" font-weight="bold" text-anchor="middle">[ D E ]</text>
    <text x="140" y="42" fill="#ffffff" class="font-sans" font-size="22" font-weight="bold" letter-spacing="0.5">OCTET 2: LOGISTICS &amp; POWER</text>

    <!-- SECTION D: DEPLOYMENT CLASS & MMG -->
    <g transform="translate(22, 84)">
      <rect width="680" height="44" rx="6" fill="#33240a" stroke="#664914" stroke-width="1.2"/>
      <text x="18" y="28" fill="#ffb703" class="font-sans" font-size="17.5" font-weight="bold" letter-spacing="1.5">D : DEPLOYMENT CLASS &amp; MMG</text>

      <!-- Items Container (6 items, row height 66px, step 74px) -->
      <!-- Item M -->
      <g transform="translate(0, 52)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#422e0a" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="36" y="41" fill="#ffb703" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">M</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Micro (&#8804;100 kg)</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Hand-portable, 2-person beach / rubber dinghy launch</text>
      </g>
      <!-- Item T -->
      <g transform="translate(0, 126)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#422e0a" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="36" y="41" fill="#ffb703" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">T</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Trailer (1.0–3.5 t)</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Towed by standard 4x4 pickup, zero port dependence</text>
      </g>
      <!-- Item V -->
      <g transform="translate(0, 200)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#422e0a" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="36" y="41" fill="#ffb703" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">V</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Vessel Davit (3.5–12 t)</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Shipboard stern ramp or dual single-point crane handling</text>
      </g>
      <!-- Item W -->
      <g transform="translate(0, 274)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#422e0a" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="36" y="41" fill="#ffb703" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">W</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Well-Deck (15–100 t)</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Heavy amphibious floodable well-deck mothership / LPD</text>
      </g>
      <!-- Item A -->
      <g transform="translate(0, 348)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#422e0a" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="36" y="41" fill="#ffb703" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">A</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Air-Dropped Parachute</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Ramp extraction from tactical cargo aircraft (C-130 / Il-76)</text>
      </g>
      <!-- Item B -->
      <g transform="translate(0, 422)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#422e0a" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="36" y="41" fill="#ffb703" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">B</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Hard Bunker / Pen</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Hardened sub-surface rock tunnel or protected naval slipway</text>
      </g>
    </g>

    <!-- SECTION E: ENERGY ARCHITECTURE -->
    <g transform="translate(22, 574)">
      <rect width="680" height="44" rx="6" fill="#33240a" stroke="#664914" stroke-width="1.2"/>
      <text x="18" y="28" fill="#ffb703" class="font-sans" font-size="17.5" font-weight="bold" letter-spacing="1.5">E : ENERGY ARCHITECTURE</text>

      <!-- Items Container (5 items) -->
      <!-- Item I -->
      <g transform="translate(0, 52)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#382206" stroke="#b45309" stroke-width="1.5"/>
        <text x="36" y="41" fill="#f59e0b" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">I</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Internal Combustion</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Marine diesel / gasoline, maximum volumetric energy density</text>
      </g>
      <!-- Item H -->
      <g transform="translate(0, 126)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#382206" stroke="#b45309" stroke-width="1.5"/>
        <text x="36" y="41" fill="#f59e0b" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">H</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Hybrid Diesel-Electric</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Diesel cruise transit + battery silent electric terminal creep</text>
      </g>
      <!-- Item B -->
      <g transform="translate(0, 200)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#382206" stroke="#b45309" stroke-width="1.5"/>
        <text x="36" y="41" fill="#f59e0b" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">B</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Battery Electric</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">100% electrochemical, zero thermal &amp; acoustic signature</text>
      </g>
      <!-- Item Y -->
      <g transform="translate(0, 274)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#382206" stroke="#b45309" stroke-width="1.5"/>
        <text x="36" y="41" fill="#f59e0b" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">Y</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Hydrogen Fuel Cell</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">High gravimetric density with zero thermal exhaust plume</text>
      </g>
      <!-- Item R -->
      <g transform="translate(0, 348)">
        <rect width="680" height="66" rx="6" fill="#1b1407" stroke="#3b2b0e" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#382206" stroke="#b45309" stroke-width="1.5"/>
        <text x="36" y="41" fill="#f59e0b" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">R</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">100% Renewable</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Solar PV deck arrays, rigid wing-sails &amp; wave motion harvesting</text>
      </g>
    </g>

    <!-- Tactical Architectural Card Note -->
    <g transform="translate(22, 1065)">
      <rect width="680" height="190" rx="8" fill="#281b08" stroke="#8a5a12" stroke-width="1.3" stroke-dasharray="5 4"/>
      <text x="22" y="34" fill="#ffb703" class="font-sans" font-size="16.5" font-weight="bold" letter-spacing="1">LOGISTICS &amp; POWER INTEGRATION NOTE</text>
      <text x="22" y="66" fill="#f1f5f9" class="font-sans" font-size="16">
        Deployability defines survival: USVs constrained to deep-water ports
      </text>
      <text x="22" y="92" fill="#cbd5e1" class="font-sans" font-size="16">
        invite pre-emptive strikes. Class T (Trailer) and M ensure dispersed launch.
      </text>
      <text x="22" y="122" fill="#ffb703" class="font-sans" font-size="15.5" font-weight="bold">
        Dual propulsion decoupling:
      </text>
      <text x="22" y="148" fill="#cbd5e1" class="font-sans" font-size="16">
        Displacement diesel enables 1,000+ km transit; sprint battery powers final kinetic rush.
      </text>
    </g>
  </g>

  <!-- ==================== COLUMN 3: [PC] KINEMATICS & SIGNAL GATEWAY ==================== -->
  <g transform="translate(1600, 195)">
    <!-- Card Frame -->
    <rect width="725" height="1390" rx="16" fill="url(#cardGradEmerald)" stroke="#165249" stroke-width="2"/>
    <rect x="0" y="0" width="725" height="70" rx="16" fill="#082b27" stroke="#00f5d4" stroke-width="1.4"/>
    <path d="M 0 52 L 0 70 L 725 70 L 725 52 Z" fill="#082b27"/>
    
    <!-- Card Header Badge & Title -->
    <rect x="22" y="16" width="100" height="38" rx="6" fill="#00f5d4" fill-opacity="0.2" stroke="#00f5d4" stroke-width="1.6"/>
    <text x="72" y="42" fill="#00f5d4" class="font-mono" font-size="21" font-weight="bold" text-anchor="middle">[ P C ]</text>
    <text x="140" y="42" fill="#ffffff" class="font-sans" font-size="22" font-weight="bold" letter-spacing="0.5">OCTET 3: KINEMATICS &amp; C2</text>

    <!-- SECTION P: PROPULSOR MECHANISM -->
    <g transform="translate(22, 84)">
      <rect width="680" height="44" rx="6" fill="#0c3831" stroke="#156e61" stroke-width="1.2"/>
      <text x="18" y="28" fill="#00f5d4" class="font-sans" font-size="17.5" font-weight="bold" letter-spacing="1.5">P : PROPULSOR MECHANISM</text>

      <!-- Items Container (6 items, row height 66px, step 74px) -->
      <!-- Item J -->
      <g transform="translate(0, 52)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#0a3d35" stroke="#10b981" stroke-width="1.5"/>
        <text x="36" y="41" fill="#34d399" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">J</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Waterjet Tunnel</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Flush-intake pump-jet, zero snag, shallow debris safe</text>
      </g>
      <!-- Item S -->
      <g transform="translate(0, 126)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#0a3d35" stroke="#10b981" stroke-width="1.5"/>
        <text x="36" y="41" fill="#34d399" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">S</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Marine Screw</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Fixed/variable-pitch propeller for open-water thrust efficiency</text>
      </g>
      <!-- Item A -->
      <g transform="translate(0, 200)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#0a3d35" stroke="#10b981" stroke-width="1.5"/>
        <text x="36" y="41" fill="#34d399" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">A</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Air-Propeller / Airdrive</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Shrouded aerial fan, traverses ice, mud &amp; heavy kelp beds</text>
      </g>
      <!-- Item W -->
      <g transform="translate(0, 274)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#0a3d35" stroke="#10b981" stroke-width="1.5"/>
        <text x="36" y="41" fill="#34d399" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">W</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Wing-Sail / Flettner</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Rigid vertical wing or Magnus rotor for wind propulsion</text>
      </g>
      <!-- Item C -->
      <g transform="translate(0, 348)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#0a3d35" stroke="#10b981" stroke-width="1.5"/>
        <text x="36" y="41" fill="#34d399" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">C</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Cable-Winch Crawler</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Active tether traction for severe surf-zone breaching</text>
      </g>
      <!-- Item H -->
      <g transform="translate(0, 422)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#0a3d35" stroke="#10b981" stroke-width="1.5"/>
        <text x="36" y="41" fill="#34d399" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">H</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Wave-Harvest Hydrofoil</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Submerged articulating wings convert wave pitch to thrust</text>
      </g>
    </g>

    <!-- SECTION C: GATEWAY & SIGNAL MEDIA -->
    <g transform="translate(22, 574)">
      <rect width="680" height="44" rx="6" fill="#0c3831" stroke="#156e61" stroke-width="1.2"/>
      <text x="18" y="28" fill="#00f5d4" class="font-sans" font-size="17.5" font-weight="bold" letter-spacing="1.5">C : GATEWAY &amp; SIGNAL MEDIA</text>

      <!-- Items Container (5 items) -->
      <!-- Item B -->
      <g transform="translate(0, 52)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#044339" stroke="#00f5d4" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00f5d4" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">B</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Bridge (Air-Sea Gateway)</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Cross-medium relay: Satellite skyward + Acoustic UUV</text>
      </g>
      <!-- Item S -->
      <g transform="translate(0, 126)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#044339" stroke="#00f5d4" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00f5d4" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">S</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Satellite Mesh (LEO/GEO)</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Starlink / Oneweb / Mil-COMSAT phased-array antenna</text>
      </g>
      <!-- Item L -->
      <g transform="translate(0, 200)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#044339" stroke="#00f5d4" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00f5d4" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">L</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Line-of-Sight Mesh</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Tactical COFDM / directional high-bandwidth microwave radio</text>
      </g>
      <!-- Item F -->
      <g transform="translate(0, 274)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#044339" stroke="#00f5d4" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00f5d4" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">F</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Fiber-Optic Hard Tether</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Micro-spool physical fiber: 100% EW &amp; jamming immunity</text>
      </g>
      <!-- Item Q -->
      <g transform="translate(0, 348)">
        <rect width="680" height="66" rx="6" fill="#091f1c" stroke="#13473f" stroke-width="1.2"/>
        <rect x="12" y="9" width="48" height="48" rx="6" fill="#044339" stroke="#00f5d4" stroke-width="1.5"/>
        <text x="36" y="41" fill="#00f5d4" class="font-mono" font-size="24" font-weight="bold" text-anchor="middle">Q</text>
        <text x="72" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Quiet (Radio Silent)</text>
        <text x="72" y="53" fill="#cbd5e1" class="font-sans" font-size="16">Total EMCON emission control, autonomous inertial run</text>
      </g>
    </g>

    <!-- Tactical Architectural Card Note -->
    <g transform="translate(22, 1065)">
      <rect width="680" height="190" rx="8" fill="#082b26" stroke="#187a6b" stroke-width="1.3" stroke-dasharray="5 4"/>
      <text x="22" y="34" fill="#00f5d4" class="font-sans" font-size="16.5" font-weight="bold" letter-spacing="1">C2 ARCHITECTURAL REDUNDANCY NOTE</text>
      <text x="22" y="66" fill="#f1f5f9" class="font-sans" font-size="16">
        Resilient warfare demands multi-layer signal fallback:
      </text>
      <text x="22" y="92" fill="#a7d6ce" class="font-sans" font-size="16" font-weight="bold">
        Satellite Mesh (S) &#8594; Tactical LOS (L) &#8594; Micro-Fiber (F) &#8594; Autonomous EMCON (Q).
      </text>
      <text x="22" y="122" fill="#00f5d4" class="font-sans" font-size="15.5" font-weight="bold">
        Cross-domain bridging:
      </text>
      <text x="22" y="148" fill="#cbd5e1" class="font-sans" font-size="16">
        Gateway Bridge (B) relays acoustic signals from seabed UUVs up into the orbital constellation.
      </text>
    </g>
  </g>

  <!-- ==================== FOOTER SECTION ==================== -->
  <g transform="translate(80, 1615)">
    <line x1="0" y1="0" x2="2240" y2="0" stroke="#1f3652" stroke-width="1.5"/>
    <text x="0" y="26" fill="#64748b" class="font-sans" font-size="15" font-weight="700" letter-spacing="1.5">UNMANNED WARFARE ENGINE (UWE)</text>
    <text x="375" y="26" fill="#475569" class="font-sans" font-size="15">&#8226;</text>
    <text x="395" y="26" fill="#94a3b8" class="font-sans" font-size="15">ARTICLE 5: UNMANNED SURFACE VEHICLES (USV)</text>
    <text x="2240" y="26" fill="#00e5ff" class="font-sans" font-size="15" font-weight="700" text-anchor="end">SERHII KHYLEVYCH — SYSTEMS ARCHITECT &amp; MILTECH STRATEGIST</text>
  </g>
</svg>"""

with open('/home/hills/Documents/UWS/usv_taxonomy_matrix.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("Updated usv_taxonomy_matrix.svg written successfully.")
