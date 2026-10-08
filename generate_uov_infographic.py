#!/usr/bin/env python3
"""
Generates the LinkedIn Infographic for Unmanned Orbital Vehicles (UOV) Classification.
Aspect ratio: 1.91:1 (2400 x 1260 px - LinkedIn High-Res Landscape).
Layout: Left-to-Right progression from Earth Surface/Ocean to Deep Cislunar Space.
"""

import os
import subprocess

def create_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1260" width="2400" height="1260">
  <defs>
    <!-- Background Gradient: Earth Atmosphere Cyan to Deep Cosmic Black -->
    <linearGradient id="deepSpaceBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06192d"/>
      <stop offset="12%" stop-color="#081e36"/>
      <stop offset="28%" stop-color="#071526"/>
      <stop offset="50%" stop-color="#050d1a"/>
      <stop offset="75%" stop-color="#03070f"/>
      <stop offset="100%" stop-color="#010306"/>
    </linearGradient>

    <!-- Earth Limb Atmosphere Glow -->
    <radialGradient id="earthAtmosphere" cx="0%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#00d2ff" stop-opacity="0.35"/>
      <stop offset="40%" stop-color="#0077b6" stop-opacity="0.18"/>
      <stop offset="80%" stop-color="#023e8a" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <!-- Ocean Depth Gradient: Surface Cyan down to Abyss Dark Blue -->
    <linearGradient id="oceanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.95"/>
      <stop offset="18%" stop-color="#0369a1" stop-opacity="0.95"/>
      <stop offset="45%" stop-color="#075985" stop-opacity="0.98"/>
      <stop offset="75%" stop-color="#0c4a6e" stop-opacity="1"/>
      <stop offset="100%" stop-color="#082f49" stop-opacity="1"/>
    </linearGradient>

    <!-- Terrain Gradient -->
    <linearGradient id="terrainGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e3a2f"/>
      <stop offset="50%" stop-color="#152b22"/>
      <stop offset="100%" stop-color="#0d1b15"/>
    </linearGradient>

    <!-- Satellite Node Glow Filters -->
    <filter id="glowCyan" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowEmerald" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowAmber" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowPurple" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <!-- Gradients for Orbital Badges -->
    <linearGradient id="nodeGradV" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4"/><stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
    <linearGradient id="nodeGradL" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f5d4"/><stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="nodeGradM" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
    <linearGradient id="nodeGradG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="nodeGradE" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fb7185"/><stop offset="100%" stop-color="#e11d48"/>
    </linearGradient>
    <linearGradient id="nodeGradC" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc"/><stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>

    <!-- Moon Texture & Lighting -->
    <radialGradient id="moonGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="45%" stop-color="#cbd5e1"/>
      <stop offset="85%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#334155"/>
    </radialGradient>
    <radialGradient id="moonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="70%" stop-color="#c084fc" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
    </radialGradient>

    <!-- Tactical Grid Pattern -->
    <pattern id="tacGrid" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#172e48" stroke-width="0.7" stroke-opacity="0.35"/>
      <circle cx="60" cy="60" r="1.2" fill="#00d2ff" fill-opacity="0.25"/>
    </pattern>

    <!-- Van Allen Radiation Belt Pattern -->
    <linearGradient id="vanAllenGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0"/>
      <stop offset="50%" stop-color="#f59e0b" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Consolas', 'Courier New', monospace; }
  </style>

  <!-- ========================================================================= -->
  <!-- 1. MAIN BACKGROUND & TACTICAL GRID                                        -->
  <!-- ========================================================================= -->
  <rect width="2400" height="1260" fill="url(#deepSpaceBg)"/>
  <rect width="2400" height="1260" fill="url(#tacGrid)"/>

  <!-- Earth Atmospheric Radial Glow (Left Hemisphere) -->
  <circle cx="0" cy="630" r="850" fill="url(#earthAtmosphere)"/>

  <!-- Distant Stars in Deep Space (Right side) -->
  <g fill="#ffffff" opacity="0.6">
    <circle cx="1650" cy="180" r="1.2"/>
    <circle cx="1780" cy="320" r="1.5" opacity="0.8"/>
    <circle cx="1920" cy="140" r="1"/>
    <circle cx="2050" cy="280" r="1.8" opacity="0.9"/>
    <circle cx="2180" cy="190" r="1.3"/>
    <circle cx="2300" cy="350" r="1.6"/>
    <circle cx="1720" cy="740" r="1.2"/>
    <circle cx="1860" cy="820" r="1"/>
    <circle cx="2010" cy="690" r="1.4"/>
    <circle cx="2250" cy="800" r="1.7" opacity="0.85"/>
    <circle cx="2340" cy="620" r="1.1"/>
  </g>

  <!-- ========================================================================= -->
  <!-- 2. HEADER SECTION (LINKEDIN POST TITLE & BRANDING)                        -->
  <!-- ========================================================================= -->
  <g transform="translate(60, 40)">
    <!-- Top Meta Tag -->
    <rect x="0" y="0" width="310" height="26" rx="4" fill="#00e5ff" fill-opacity="0.12" stroke="#00e5ff" stroke-width="1.2"/>
    <text x="12" y="17" fill="#00e5ff" class="font-mono" font-size="11.5" font-weight="bold" letter-spacing="1.5">
      UWE ARCHITECTURAL FRAMEWORK • ARTICLE 6
    </text>

    <!-- Main Title -->
    <text x="0" y="66" fill="#f8fafc" class="font-sans" font-size="34" font-weight="900" letter-spacing="0.5">
      CLASSIFICATION OF UNMANNED ORBITAL VEHICLES (UOV)
    </text>
    <text x="0" y="98" fill="#94a3b8" class="font-sans" font-size="17" font-weight="500">
      Multi-Domain C4ISR Integration • Dynamic Physical Horizons [V, L, M, G, E, C] • The Kondratyuk Distributed Infrastructure
    </text>
  </g>

  <!-- Right Header Badge: Author / Strategy -->
  <g transform="translate(1920, 45)">
    <rect x="0" y="0" width="420" height="60" rx="8" fill="#0c1e33" stroke="#1e40af" stroke-width="1.2"/>
    <text x="20" y="26" fill="#38bdf8" class="font-sans" font-size="13" font-weight="bold" letter-spacing="1">
      SERHII KHYLEVYCH
    </text>
    <text x="20" y="46" fill="#94a3b8" class="font-sans" font-size="12">
      Systems Architect &amp; MilTech Strategist • UWE Series
    </text>
  </g>

  <!-- ========================================================================= -->
  <!-- 3. ORBITAL ARC GUIDE LINES & REGIONS                                      -->
  <!-- ========================================================================= -->
  <!-- Van Allen Radiation Belt Indicator between LEO and GEO (around MEO) -->
  <rect x="1050" y="130" width="280" height="920" fill="url(#vanAllenGrad)" rx="16"/>
  <text x="1190" y="170" fill="#f59e0b" opacity="0.65" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle" letter-spacing="2">
    VAN ALLEN RADIATION BELTS (MEO RAD-HARD HORIZON)
  </text>

  <!-- Vertical Orbit Separator Lines (Subtle Tactical Dotted Guides) -->
  <g stroke="#1e3a5f" stroke-width="1" stroke-dasharray="4 6" opacity="0.5">
    <line x1="580" y1="130" x2="580" y2="1050"/>  <!-- V (VLEO) -->
    <line x1="840" y1="130" x2="840" y2="1050"/>  <!-- L (LEO) -->
    <line x1="1190" y1="130" x2="1190" y2="1050"/> <!-- M (MEO) -->
    <line x1="1540" y1="130" x2="1540" y2="1050"/> <!-- G (GEO) -->
    <line x1="1840" y1="130" x2="1840" y2="1050"/> <!-- E (EEO) -->
    <line x1="2160" y1="130" x2="2160" y2="1050"/> <!-- C (Cislunar / Moon) -->
  </g>

  <!-- Highly Elliptical Orbit E Arc (Tundra/Molniya representation) -->
  <path d="M 840 540 C 1300 240, 1700 220, 1840 320" fill="none" stroke="#fb7185" stroke-width="1.8" stroke-dasharray="6 6" opacity="0.5"/>
  <text x="1420" y="270" fill="#fb7185" class="font-mono" font-size="11" opacity="0.8">
    EEO Elliptical Arc (Molniya / Tundra Dwell: Apogee ~40,000 km)
  </text>

  <!-- Cislunar Halo Transfer / Weak Stability Boundary Line to Moon -->
  <path d="M 1540 540 C 1750 480, 1950 420, 2140 430" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-dasharray="8 6" opacity="0.6"/>
  <text x="1800" y="475" fill="#c084fc" class="font-mono" font-size="11" opacity="0.8">
    Weak Stability Boundary (WSB) Transfer to L1/L2
  </text>

  <!-- ========================================================================= -->
  <!-- 4. LEFT SECTOR: EARTH SURFACE & OCEAN DEPTH (UGV, USV, UUV)               -->
  <!-- ========================================================================= -->
  <!-- Earth Curvature Limb / Boundary -->
  <path d="M 0 130 L 320 130 C 440 380, 440 820, 320 1060 L 0 1060 Z" fill="#0c233c" stroke="#00e5ff" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Upper Segment: Ground / Land Terrain for UGV -->
  <path d="M 0 130 L 320 130 C 375 250, 400 370, 405 450 L 0 450 Z" fill="url(#terrainGrad)"/>
  <path d="M 0 450 Q 200 450, 405 450" stroke="#10b981" stroke-width="3" fill="none"/>

  <!-- Lower Segment: Ocean Water Body for USV & UUV -->
  <path d="M 0 450 L 405 450 C 412 550, 410 700, 385 850 C 365 940, 345 1010, 320 1060 L 0 1060 Z" fill="url(#oceanGrad)"/>
  <!-- Sea Surface Waterline Waves -->
  <path d="M 0 450 Q 50 445, 100 450 T 200 450 T 300 450 T 405 450" fill="none" stroke="#38bdf8" stroke-width="2.5"/>

  <!-- Sector Labels: LAND & MARITIME DOMAINS -->
  <text x="25" y="165" fill="#34d399" class="font-mono" font-size="12" font-weight="bold" letter-spacing="1">
    TERRESTRIAL DOMAIN (LAND)
  </text>
  <text x="25" y="480" fill="#38bdf8" class="font-mono" font-size="12" font-weight="bold" letter-spacing="1">
    MARITIME DOMAIN (SURFACE &amp; BENTHIC DEPTH)
  </text>
  <text x="25" y="990" fill="#94a3b8" class="font-mono" font-size="10.5">
    Depth Strata: 0m → 200m (Shelf) → 1000m+ (Pelagic Abyss)
  </text>

  <!== ========================================================================= -->
  <!-- ICON 1: UGV (Ground Drone) - Strict RECTANGLE shape                       -->
  <!== ========================================================================= -->
  <g transform="translate(190, 310)">
    <!-- Base Glow -->
    <rect x="-6" y="-6" width="132" height="72" rx="6" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="1.2"/>
    <!-- UGV Rectangle -->
    <rect x="0" y="0" width="120" height="60" rx="3" fill="#062e24" stroke="#10b981" stroke-width="2.5"/>
    <!-- Treads / Wheels accents -->
    <rect x="10" y="48" width="100" height="8" rx="2" fill="#047857"/>
    <!-- Sensor mast -->
    <circle cx="35" cy="22" r="7" fill="#10b981"/>
    <text x="50" y="27" fill="#ffffff" class="font-mono" font-size="15" font-weight="bold">UGV</text>
    <text x="60" y="85" fill="#34d399" class="font-sans" font-size="12.5" font-weight="bold" text-anchor="middle">
      UGV Ground Drone
    </text>
  </g>

  <!== ========================================================================= -->
  <!-- ICON 2: USV (Surface Drone) - TRAPEZOID shape (shorter side to ground/water)-->
  <!== ========================================================================= -->
  <g transform="translate(180, 520)">
    <!-- Trapezoid Boat Hull: Top Deck is wider (140px), Bottom is shorter (90px) facing into water -->
    <polygon points="5,0 135,0 115,55 25,55" fill="#073b5c" stroke="#00e5ff" stroke-width="2.5"/>
    <!-- Upper Deck Superstructure / Radome -->
    <rect x="40" y="-14" width="60" height="14" rx="3" fill="#0c4a6e" stroke="#00e5ff" stroke-width="1.5"/>
    <circle cx="70" cy="-7" r="4" fill="#38bdf8"/>
    <!-- USV Label -->
    <text x="70" y="34" fill="#ffffff" class="font-mono" font-size="16" font-weight="bold" text-anchor="middle">USV</text>
    <text x="70" y="78" fill="#38bdf8" class="font-sans" font-size="12.5" font-weight="bold" text-anchor="middle">
      USV Surface Strike
    </text>
  </g>

  <!== ========================================================================= -->
  <!-- ICON 3: UUV (Undersea Benthic Drone) - OVAL shape submerged in water      -->
  <!== ========================================================================= -->
  <g transform="translate(180, 780)">
    <!-- Glow -->
    <ellipse cx="70" cy="30" rx="68" ry="34" fill="#0284c7" fill-opacity="0.12"/>
    <!-- UUV Oval Hull -->
    <ellipse cx="70" cy="30" rx="60" ry="28" fill="#082f49" stroke="#38bdf8" stroke-width="2.5"/>
    <!-- Rudder / Stern Thruster -->
    <path d="M 125 22 L 138 12 L 138 48 L 125 38 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.2"/>
    <!-- UUV Label -->
    <text x="70" y="36" fill="#ffffff" class="font-mono" font-size="16" font-weight="bold" text-anchor="middle">UUV</text>
    <text x="70" y="80" fill="#7dd3fc" class="font-sans" font-size="12.5" font-weight="bold" text-anchor="middle">
      UUV Subsea / Benthic
    </text>
  </g>

  <!== ========================================================================= -->
  <!-- LINK BETWEEN USV AND UUV (Acoustic / Tether / Buoy Gateway)               -->
  <!== ========================================================================= -->
  <g stroke="#00e5ff" stroke-width="2" stroke-dasharray="5 4">
    <line x1="250" y1="575" x2="250" y2="780"/>
  </g>
  <!-- Ping Wave Arcs -->
  <g fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.8">
    <path d="M 235 660 A 15 15 0 0 0 265 660"/>
    <path d="M 225 675 A 25 25 0 0 0 275 675"/>
    <path d="M 215 690 A 35 35 0 0 0 285 690"/>
  </g>
  <rect x="175" y="635" width="150" height="22" rx="4" fill="#022a44" stroke="#0284c7" stroke-width="1"/>
  <text x="250" y="650" fill="#38bdf8" class="font-mono" font-size="9.5" font-weight="bold" text-anchor="middle">
    SUBSEA GATEWAY LINK
  </text>

  <!-- ========================================================================= -->
  <!-- 5. ORBITAL SATELLITE NODES (CIRCLES WITH ORBIT LETTER IN CENTER)          -->
  <!-- ========================================================================= -->

  <!-- NODE 1: V (VLEO - Very Low Earth Orbit) -->
  <g transform="translate(580, 540)">
    <!-- Aerodynamic VLEO Wedge outline -->
    <path d="M -45 -18 L 45 0 L -45 18 Z" fill="#0891b2" fill-opacity="0.3" stroke="#06b6d4" stroke-width="1.2"/>
    <!-- Outer Glow & Crosshairs -->
    <circle cx="0" cy="0" r="48" fill="#083344" stroke="#06b6d4" stroke-width="2.8" filter="url(#glowCyan)"/>
    <circle cx="0" cy="0" r="38" fill="url(#nodeGradV)"/>
    <!-- Orbit Letter in Center -->
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">V</text>
    <!-- Card Info Callout -->
    <g transform="translate(0, 75)">
      <rect x="-85" y="0" width="170" height="52" rx="6" fill="#082333" stroke="#06b6d4" stroke-width="1.2"/>
      <text x="0" y="20" fill="#00e5ff" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">VLEO HORIZON</text>
      <text x="0" y="38" fill="#94a3b8" class="font-mono" font-size="11" text-anchor="middle">120 – 350 km (ABEP)</text>
    </g>
  </g>

  <!-- NODE 2: L (LEO - Low Earth Orbit) -->
  <g transform="translate(840, 540)">
    <!-- Solar Array Wings for Mega-Constellation Bus -->
    <rect x="-85" y="-12" width="40" height="24" rx="2" fill="#064e3b" stroke="#10b981" stroke-width="1.2"/>
    <rect x="45" y="-12" width="40" height="24" rx="2" fill="#064e3b" stroke="#10b981" stroke-width="1.2"/>
    <line x1="-85" y1="0" x2="85" y2="0" stroke="#34d399" stroke-width="1"/>
    <!-- Node Circle -->
    <circle cx="0" cy="0" r="48" fill="#062e24" stroke="#10b981" stroke-width="3" filter="url(#glowEmerald)"/>
    <circle cx="0" cy="0" r="38" fill="url(#nodeGradL)"/>
    <!-- Orbit Letter in Center -->
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">L</text>
    <!-- Card Info Callout -->
    <g transform="translate(0, 75)">
      <rect x="-85" y="0" width="170" height="52" rx="6" fill="#05251d" stroke="#10b981" stroke-width="1.2"/>
      <text x="0" y="20" fill="#34d399" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">LEO MEGA-SWARM</text>
      <text x="0" y="38" fill="#94a3b8" class="font-mono" font-size="11" text-anchor="middle">350 – 2,000 km (7.8 km/s)</text>
    </g>
  </g>

  <!-- NODE 3: M (MEO - Medium Earth Orbit) -->
  <g transform="translate(1190, 540)">
    <!-- Solar Panels -->
    <rect x="-95" y="-15" width="45" height="30" rx="3" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.2"/>
    <rect x="50" y="-15" width="45" height="30" rx="3" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.2"/>
    <!-- Node Circle -->
    <circle cx="0" cy="0" r="50" fill="#0c2340" stroke="#38bdf8" stroke-width="3" filter="url(#glowCyan)"/>
    <circle cx="0" cy="0" r="40" fill="url(#nodeGradM)"/>
    <!-- Orbit Letter in Center -->
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">M</text>
    <!-- Card Info Callout -->
    <g transform="translate(0, 80)">
      <rect x="-95" y="0" width="190" height="52" rx="6" fill="#081a2f" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="0" y="20" fill="#38bdf8" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">MEO REGIONAL ANCHOR</text>
      <text x="0" y="38" fill="#94a3b8" class="font-mono" font-size="11" text-anchor="middle">2,000 – 35,786 km (PNT/C2)</text>
    </g>
  </g>

  <!-- NODE 4: G (GEO - Geostationary Orbit) -->
  <g transform="translate(1540, 540)">
    <!-- Giant Deployable Mesh Antenna Reflector Graphic -->
    <ellipse cx="0" cy="-60" rx="45" ry="14" fill="#78350f" fill-opacity="0.3" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="0" y1="-46" x2="0" y2="-38" stroke="#f59e0b" stroke-width="2"/>
    <!-- Heavy Solar Wings -->
    <rect x="-105" y="-16" width="55" height="32" rx="3" fill="#451a03" stroke="#f59e0b" stroke-width="1.2"/>
    <rect x="50" y="-16" width="55" height="32" rx="3" fill="#451a03" stroke="#f59e0b" stroke-width="1.2"/>
    <!-- Node Circle -->
    <circle cx="0" cy="0" r="52" fill="#291404" stroke="#f59e0b" stroke-width="3" filter="url(#glowAmber)"/>
    <circle cx="0" cy="0" r="42" fill="url(#nodeGradG)"/>
    <!-- Orbit Letter in Center -->
    <text x="0" y="13" fill="#ffffff" class="font-sans" font-size="36" font-weight="900" text-anchor="middle">G</text>
    <!-- Card Info Callout -->
    <g transform="translate(0, 80)">
      <rect x="-95" y="0" width="190" height="52" rx="6" fill="#1c0f05" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="0" y="20" fill="#fbbf24" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">GEO STRATEGIC APEX</text>
      <text x="0" y="38" fill="#94a3b8" class="font-mono" font-size="11" text-anchor="middle">35,786 km (Zero Angular V)</text>
    </g>
  </g>

  <!-- NODE 5: E (EEO - Highly Elliptical Molniya / Tundra Orbit) -->
  <g transform="translate(1840, 320)">
    <!-- Specialized Apogee Sensor Pods -->
    <circle cx="-35" cy="-25" r="9" fill="#881337" stroke="#fb7185" stroke-width="1.2"/>
    <circle cx="35" cy="-25" r="9" fill="#881337" stroke="#fb7185" stroke-width="1.2"/>
    <!-- Node Circle -->
    <circle cx="0" cy="0" r="50" fill="#2d0612" stroke="#fb7185" stroke-width="3" filter="url(#glowPurple)"/>
    <circle cx="0" cy="0" r="40" fill="url(#nodeGradE)"/>
    <!-- Orbit Letter in Center -->
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">E</text>
    <!-- Card Info Callout -->
    <g transform="translate(0, 75)">
      <rect x="-95" y="0" width="190" height="52" rx="6" fill="#20040d" stroke="#fb7185" stroke-width="1.2"/>
      <text x="0" y="20" fill="#fb7185" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">EEO POLAR OVERWATCH</text>
      <text x="0" y="38" fill="#94a3b8" class="font-mono" font-size="11" text-anchor="middle">Apogee ~40,000 km (i=63.4°)</text>
    </g>
  </g>

  <!-- NODE 6: C (Cislunar / EMO Orbit at the threshold of the Moon) -->
  <g transform="translate(2160, 430)">
    <!-- Moon Visual Behind / Surrounding the Apogee -->
    <circle cx="0" cy="0" r="115" fill="url(#moonGlow)"/>
    <circle cx="65" cy="-25" r="60" fill="url(#moonGrad)" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Moon Craters -->
    <ellipse cx="50" cy="-35" rx="9" ry="6" fill="#475569" opacity="0.6"/>
    <ellipse cx="80" cy="-10" rx="14" ry="10" fill="#475569" opacity="0.5"/>
    <ellipse cx="40" cy="-10" rx="7" ry="5" fill="#475569" opacity="0.6"/>
    <ellipse cx="75" cy="-45" rx="6" ry="4" fill="#334155" opacity="0.7"/>

    <!-- Quantum Super-Bus Structure (Node C) -->
    <rect x="-35" y="-35" width="70" height="70" rx="10" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-dasharray="4 4"/>
    <!-- Node Circle -->
    <circle cx="0" cy="0" r="50" fill="#20093b" stroke="#c084fc" stroke-width="3" filter="url(#glowPurple)"/>
    <circle cx="0" cy="0" r="40" fill="url(#nodeGradC)"/>
    <!-- Orbit Letter in Center -->
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">C</text>
    <!-- Card Info Callout -->
    <g transform="translate(0, 80)">
      <rect x="-105" y="0" width="210" height="52" rx="6" fill="#17062a" stroke="#c084fc" stroke-width="1.2"/>
      <text x="0" y="20" fill="#c084fc" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">CISLUNAR QUANTUM NEXUS</text>
      <text x="0" y="38" fill="#94a3b8" class="font-mono" font-size="11" text-anchor="middle">~384,400 km (L1–L5 / NRHO)</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- 6. CROSS-DOMAIN COMMUNICATION NETWORK GRAPH (THE TACTICAL DATA LINKS)     -->
  <!-- ========================================================================= -->

  <!-- A. Direct Downlinks from V, L, M, G to UGV & USV (Cyan / Blue Dashed) -->
  <!-- V to UGV & USV -->
  <path d="M 580 540 Q 420 370, 310 340" fill="none" stroke="#00e5ff" stroke-width="2" stroke-dasharray="6 4" opacity="0.85"/>
  <path d="M 580 540 Q 430 520, 315 545" fill="none" stroke="#00e5ff" stroke-width="2" stroke-dasharray="6 4" opacity="0.85"/>

  <!-- L to UGV & USV (High-Bandwidth Direct-to-Cell / Starshield) -->
  <path d="M 840 540 Q 560 380, 310 340" fill="none" stroke="#10b981" stroke-width="2.2" stroke-dasharray="7 5" opacity="0.9"/>
  <path d="M 840 540 Q 580 560, 315 545" fill="none" stroke="#10b981" stroke-width="2.2" stroke-dasharray="7 5" opacity="0.9"/>

  <!-- M to UGV & USV (Regional Tactical PNT / Overwatch C2) -->
  <path d="M 1190 540 Q 750 420, 310 340" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="8 6" opacity="0.7"/>
  <path d="M 1190 540 Q 780 620, 315 545" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="8 6" opacity="0.7"/>

  <!-- G to UGV & USV (Strategic Wide-Area Theater Broadcast) -->
  <path d="M 1540 540 Q 940 450, 310 340" fill="none" stroke="#f59e0b" stroke-width="1.6" stroke-dasharray="10 6" opacity="0.6"/>
  <path d="M 1540 540 Q 960 670, 315 545" fill="none" stroke="#f59e0b" stroke-width="1.6" stroke-dasharray="10 6" opacity="0.6"/>

  <!-- B. Intra-Orbital Backbone Crosslinks: G and M communicate with L (Emerald Green) -->
  <!-- G <-> L Optical Laser Crosslink -->
  <path d="M 1540 515 Q 1190 440, 840 515" fill="none" stroke="#34d399" stroke-width="3" stroke-dasharray="8 4"/>
  <rect x="1115" y="445" width="150" height="22" rx="4" fill="#062e24" stroke="#34d399" stroke-width="1"/>
  <text x="1190" y="460" fill="#34d399" class="font-mono" font-size="10" font-weight="bold" text-anchor="middle">
    G ⇄ L LASER CROSSLINK
  </text>

  <!-- M <-> L Optical Laser Crosslink -->
  <path d="M 1190 565 Q 1015 620, 840 565" fill="none" stroke="#00e5ff" stroke-width="2.5" stroke-dasharray="6 4"/>
  <rect x="940" y="605" width="150" height="22" rx="4" fill="#082333" stroke="#00e5ff" stroke-width="1"/>
  <text x="1015" y="620" fill="#00e5ff" class="font-mono" font-size="10" font-weight="bold" text-anchor="middle">
    M ⇄ L RELAY MESH
  </text>

  <!-- C. High-Tier Crosslinks: E communicates with G, and C communicates with M -->
  <!-- E <-> G Tactical Strategic Early-Warning Link -->
  <path d="M 1840 370 Q 1700 480, 1540 515" fill="none" stroke="#fb7185" stroke-width="2.8" stroke-dasharray="7 5"/>
  <rect x="1630" y="410" width="160" height="22" rx="4" fill="#20040d" stroke="#fb7185" stroke-width="1"/>
  <text x="1710" y="425" fill="#fb7185" class="font-mono" font-size="10" font-weight="bold" text-anchor="middle">
    E ⇄ G STRATEGIC LINK
  </text>

  <!-- C <-> M Deep Cislunar Quantum / Laser Data Bridge -->
  <path d="M 2160 480 Q 1650 780, 1190 565" fill="none" stroke="#c084fc" stroke-width="3" stroke-dasharray="9 5"/>
  <rect x="1570" y="695" width="220" height="24" rx="4" fill="#17062a" stroke="#c084fc" stroke-width="1.2"/>
  <text x="1680" y="711" fill="#c084fc" class="font-mono" font-size="10.5" font-weight="bold" text-anchor="middle">
    C ⇄ M QUANTUM DATA BRIDGE
  </text>

  <!-- ========================================================================= -->
  <!-- 7. TACTICAL LEGEND BOX (CENTER-LEFT BOTTOM)                                -->
  <!-- ========================================================================= -->
  <g transform="translate(420, 890)">
    <rect width="660" height="135" rx="8" fill="#091829" stroke="#1f3d63" stroke-width="1.4"/>
    <text x="20" y="26" fill="#38bdf8" class="font-sans" font-size="14" font-weight="bold" letter-spacing="1">
      NETWORK TOPOLOGY &amp; LINK ROUTING LOGIC
    </text>

    <!-- Legend Items -->
    <g transform="translate(20, 42)">
      <!-- Line 1: Surface & Maritime Access -->
      <line x1="0" y1="12" x2="35" y2="12" stroke="#00e5ff" stroke-width="2.5" stroke-dasharray="5 3"/>
      <text x="45" y="16" fill="#f1f5f9" class="font-sans" font-size="12">
        <tspan font-weight="bold" fill="#00e5ff">V, L, M, G ➔ UGV &amp; USV:</tspan> Multi-tier direct-to-cell, SAR &amp; tactical C2 downlinks.
      </text>

      <!-- Line 2: Inter-Satellite Laser Mesh -->
      <line x1="0" y1="36" x2="35" y2="36" stroke="#34d399" stroke-width="3" stroke-dasharray="7 4"/>
      <text x="45" y="40" fill="#f1f5f9" class="font-sans" font-size="12">
        <tspan font-weight="bold" fill="#34d399">G, M ➔ L Routing:</tspan> Inter-satellite laser backbone (OISL) for theater data distribution.
      </text>

      <!-- Line 3: Deep Space & Polar Staging -->
      <line x1="0" y1="60" x2="35" y2="60" stroke="#c084fc" stroke-width="3" stroke-dasharray="8 4"/>
      <text x="45" y="64" fill="#f1f5f9" class="font-sans" font-size="12">
        <tspan font-weight="bold" fill="#c084fc">E ➔ G &amp; C ➔ M:</tspan> Polar high-apogee &amp; cislunar quantum supervisor bridges.
      </text>

      <!-- Line 4: Maritime Acoustic/Gateway -->
      <line x1="0" y1="84" x2="35" y2="84" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="4 4"/>
      <text x="45" y="88" fill="#f1f5f9" class="font-sans" font-size="12">
        <tspan font-weight="bold" fill="#38bdf8">USV ⇄ UUV:</tspan> Surface-to-benthic acoustic/tether gateway for seabed swarm stealth.
      </text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- 8. BOTTOM DISTANCE & METRIC SCALE BAR (0 km TO 384,400 km)                -->
  <!-- ========================================================================= -->
  <g transform="translate(60, 1070)">
    <!-- Scale Background Box -->
    <rect x="0" y="0" width="2280" height="115" rx="8" fill="#071322" stroke="#172e48" stroke-width="1.4"/>

    <!-- Scale Title -->
    <text x="20" y="24" fill="#38bdf8" class="font-mono" font-size="12" font-weight="bold" letter-spacing="1.5">
      PHYSICAL ORBITAL DISTANCE &amp; GRAVITATIONAL VELOCITY SPECTRUM (LOGARITHMIC EXPANSION)
    </text>

    <!-- Main Scale Baseline Line -->
    <line x1="20" y1="52" x2="2260" y2="52" stroke="#334155" stroke-width="2.5"/>

    <!-- Tick 0: Earth Surface -->
    <g transform="translate(200, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#00e5ff" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#00e5ff"/>
      <text x="0" y="30" fill="#f8fafc" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">EARTH</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">0 km (Sea Level)</text>
    </g>

    <!-- Tick 1: V (VLEO) -->
    <g transform="translate(520, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#06b6d4" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#06b6d4"/>
      <text x="0" y="30" fill="#00e5ff" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">V (VLEO)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">120 – 350 km</text>
    </g>

    <!-- Tick 2: L (LEO) -->
    <g transform="translate(780, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#10b981" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#10b981"/>
      <text x="0" y="30" fill="#34d399" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">L (LEO)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">350 – 2,000 km</text>
    </g>

    <!-- Tick 3: M (MEO) -->
    <g transform="translate(1130, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#38bdf8" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#38bdf8"/>
      <text x="0" y="30" fill="#38bdf8" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">M (MEO)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">2,000 – 35,786 km</text>
    </g>

    <!-- Tick 4: G (GEO) -->
    <g transform="translate(1480, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#f59e0b" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#f59e0b"/>
      <text x="0" y="30" fill="#fbbf24" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">G (GEO / GSO)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">~35,786 km</text>
    </g>

    <!-- Tick 5: E (EEO) -->
    <g transform="translate(1780, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#fb7185" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#fb7185"/>
      <text x="0" y="30" fill="#fb7185" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">E (EEO TUNDRA)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">Apogee ~40,000 km</text>
    </g>

    <!-- Tick 6: C (Cislunar / Moon Apogee) -->
    <g transform="translate(2100, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#c084fc" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#c084fc"/>
      <text x="0" y="30" fill="#c084fc" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">C (CISLUNAR / MOON)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">~384,400 km (Lagrange L1–L5)</text>
    </g>

    <!-- Horizontal Gradient Color Bar below scale -->
    <defs>
      <linearGradient id="spectrumBar" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00e5ff"/>
        <stop offset="18%" stop-color="#06b6d4"/>
        <stop offset="35%" stop-color="#10b981"/>
        <stop offset="55%" stop-color="#38bdf8"/>
        <stop offset="72%" stop-color="#f59e0b"/>
        <stop offset="85%" stop-color="#fb7185"/>
        <stop offset="100%" stop-color="#c084fc"/>
      </linearGradient>
    </defs>
    <rect x="20" y="50" width="2240" height="4" fill="url(#spectrumBar)"/>
  </g>

  <!-- ========================================================================= -->
  <!-- 9. FOOTER SECTION                                                         -->
  <!-- ========================================================================= -->
  <g transform="translate(60, 1220)">
    <text x="0" y="18" fill="#64748b" class="font-sans" font-size="13" font-weight="700" letter-spacing="1">
      UNMANNED WARFARE ENGINE (UWE)
    </text>
    <text x="260" y="18" fill="#475569" class="font-sans" font-size="13">•</text>
    <text x="275" y="18" fill="#94a3b8" class="font-sans" font-size="13">
      CLASSIFICATION OF UNMANNED ORBITAL VEHICLES (UOV) — CROSS-DOMAIN LINK GRAPH
    </text>
    <text x="2280" y="18" fill="#00e5ff" class="font-sans" font-size="13" font-weight="700" text-anchor="end">
      SERHII KHYLEVYCH — SYSTEMS ARCHITECT &amp; MILTECH STRATEGIST
    </text>
  </g>
</svg>"""

    out_svg = "/home/hills/Documents/UWS/uov_orbital_architecture.svg"
    with open(out_svg, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out_svg}")
    return out_svg

def convert_to_raster(svg_path):
    base_dir = os.path.dirname(svg_path)
    pdf_path = os.path.join(base_dir, "uov_orbital_architecture.pdf")
    
    # 1. Convert SVG to PDF via LibreOffice Draw
    cmd_pdf = [
        "libreoffice",
        "-env:UserInstallation=file:///home/hills/Documents/UWS/.lo_user",
        "--headless",
        "--convert-to", "pdf",
        svg_path,
        "--outdir", base_dir
    ]
    print(f"Running: {' '.join(cmd_pdf)}")
    res1 = subprocess.run(cmd_pdf, capture_output=True, text=True)
    if res1.returncode != 0:
        print("Error converting to PDF:", res1.stderr)
        return False
    print(f"Generated {pdf_path}")

    # 2. Convert PDF to PNG (150 DPI for super crisp LinkedIn high-res)
    cmd_png = [
        "pdftoppm",
        "-png",
        "-r", "150",
        pdf_path,
        os.path.join(base_dir, "uov_orbital_architecture_tmp")
    ]
    print(f"Running: {' '.join(cmd_png)}")
    res2 = subprocess.run(cmd_png, capture_output=True, text=True)
    if res2.returncode != 0:
        print("Error converting to PNG:", res2.stderr)
        return False

    tmp_png = os.path.join(base_dir, "uov_orbital_architecture_tmp-1.png")
    final_png = os.path.join(base_dir, "uov_orbital_architecture.png")
    if os.path.exists(tmp_png):
        os.rename(tmp_png, final_png)
        print(f"Generated {final_png}")

    # 3. Convert PDF to JPEG
    cmd_jpg = [
        "pdftoppm",
        "-jpeg",
        "-r", "150",
        pdf_path,
        os.path.join(base_dir, "uov_orbital_architecture_tmp")
    ]
    print(f"Running: {' '.join(cmd_jpg)}")
    res3 = subprocess.run(cmd_jpg, capture_output=True, text=True)
    tmp_jpg = os.path.join(base_dir, "uov_orbital_architecture_tmp-1.jpg")
    final_jpg = os.path.join(base_dir, "uov_orbital_architecture.jpg")
    if os.path.exists(tmp_jpg):
        os.rename(tmp_jpg, final_jpg)
        print(f"Generated {final_jpg}")

    return True

if __name__ == "__main__":
    svg_file = create_svg()
    convert_to_raster(svg_file)
