#!/usr/bin/env python3
"""
Refined UOV Architecture Infographic v2
- Adds UCV (square with bold rotor dots on corners) to the right of UGV
- Adds UAV (triangle) to the right of UCV
- Interconnects: UCV to UGV & USV; UAV to UGV, USV, & UCV
- Encapsulates all surface/air assets in a dedicated "SPACE-TO-SURFACE SEGMENT"
- Aggregates links from V, L, M, G into the Space-to-Surface Segment Gateway to eliminate visual clutter
- Maintains all orbital nodes: V, L, M, G, E, C (Moon at apogee)
- Bottom distance & speed spectrum scale
"""

import os
import subprocess
import xml.etree.ElementTree as ET

def generate_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1260" width="2400" height="1260">
  <defs>
    <!-- Background Gradient: Atmospheric Cyan to Deep Space Pitch Black -->
    <linearGradient id="deepSpaceBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#041525"/>
      <stop offset="12%" stop-color="#061a30"/>
      <stop offset="26%" stop-color="#051324"/>
      <stop offset="48%" stop-color="#030b17"/>
      <stop offset="72%" stop-color="#02060d"/>
      <stop offset="100%" stop-color="#000204"/>
    </linearGradient>

    <!-- Earth Atmosphere Limb Radial Glow -->
    <radialGradient id="earthAtmosphere" cx="0%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#00d2ff" stop-opacity="0.32"/>
      <stop offset="35%" stop-color="#0077b6" stop-opacity="0.16"/>
      <stop offset="75%" stop-color="#023e8a" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <!-- Space-to-Surface Segment Panel Background -->
    <linearGradient id="segmentPanelBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#071b2e" stop-opacity="0.92"/>
      <stop offset="100%" stop-color="#04101d" stop-opacity="0.92"/>
    </linearGradient>

    <!-- Terrain Gradient -->
    <linearGradient id="terrainGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#163826"/>
      <stop offset="50%" stop-color="#0f261a"/>
      <stop offset="100%" stop-color="#08140e"/>
    </linearGradient>

    <!-- Ocean Water Depth Gradient -->
    <linearGradient id="oceanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.9"/>
      <stop offset="25%" stop-color="#0369a1" stop-opacity="0.92"/>
      <stop offset="60%" stop-color="#075985" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#062e4a" stop-opacity="0.98"/>
    </linearGradient>

    <!-- Glow Filters -->
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

    <!-- Satellite Node Gradients -->
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

    <!-- Moon Gradients -->
    <radialGradient id="moonGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="40%" stop-color="#cbd5e1"/>
      <stop offset="80%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#334155"/>
    </radialGradient>
    <radialGradient id="moonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="65%" stop-color="#c084fc" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
    </radialGradient>

    <!-- Grid Pattern -->
    <pattern id="tacGrid" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#172e48" stroke-width="0.7" stroke-opacity="0.32"/>
      <circle cx="60" cy="60" r="1.2" fill="#00d2ff" fill-opacity="0.2"/>
    </pattern>

    <!-- Van Allen Radiation Belt Gradient -->
    <linearGradient id="vanAllenGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0"/>
      <stop offset="50%" stop-color="#f59e0b" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
    </linearGradient>

    <!-- Bottom Spectrum Bar Gradient -->
    <linearGradient id="spectrumBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e5ff"/>
      <stop offset="16%" stop-color="#06b6d4"/>
      <stop offset="34%" stop-color="#10b981"/>
      <stop offset="54%" stop-color="#38bdf8"/>
      <stop offset="72%" stop-color="#f59e0b"/>
      <stop offset="85%" stop-color="#fb7185"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Consolas', 'Courier New', monospace; }
  </style>

  <!-- 1. MAIN BACKGROUND & GRID -->
  <rect width="2400" height="1260" fill="url(#deepSpaceBg)"/>
  <rect width="2400" height="1260" fill="url(#tacGrid)"/>
  <circle cx="0" cy="630" r="950" fill="url(#earthAtmosphere)"/>

  <!-- Stars in Deep Space -->
  <g fill="#ffffff" opacity="0.6">
    <circle cx="1680" cy="160" r="1.3"/>
    <circle cx="1780" cy="220" r="1.6" opacity="0.8"/>
    <circle cx="1940" cy="140" r="1.1"/>
    <circle cx="2040" cy="200" r="1.8" opacity="0.9"/>
    <circle cx="2200" cy="160" r="1.3"/>
    <circle cx="2320" cy="240" r="1.6"/>
    <circle cx="1730" cy="820" r="1.2"/>
    <circle cx="1870" cy="870" r="1.1"/>
    <circle cx="2020" cy="760" r="1.4"/>
    <circle cx="2260" cy="850" r="1.7" opacity="0.85"/>
    <circle cx="2340" cy="710" r="1.1"/>
  </g>

  <!-- 2. HEADER SECTION -->
  <g transform="translate(60, 35)">
    <rect x="0" y="0" width="310" height="26" rx="4" fill="#00e5ff" fill-opacity="0.12" stroke="#00e5ff" stroke-width="1.2"/>
    <text x="12" y="17" fill="#00e5ff" class="font-mono" font-size="11.5" font-weight="bold" letter-spacing="1.5">
      UWE ARCHITECTURAL FRAMEWORK • ARTICLE 6
    </text>

    <text x="0" y="66" fill="#f8fafc" class="font-sans" font-size="34" font-weight="900" letter-spacing="0.5">
      CLASSIFICATION OF UNMANNED ORBITAL VEHICLES (UOV)
    </text>
    <text x="0" y="96" fill="#94a3b8" class="font-sans" font-size="16" font-weight="500">
      Multi-Domain C4ISR Integration • Space-to-Surface Segment • The Kondratyuk Distributed Infrastructure
    </text>
  </g>

  <!-- Right Header Author Badge -->
  <g transform="translate(1920, 35)">
    <rect x="0" y="0" width="420" height="60" rx="8" fill="#0c1e33" stroke="#1e40af" stroke-width="1.2"/>
    <text x="20" y="26" fill="#38bdf8" class="font-sans" font-size="13.5" font-weight="bold" letter-spacing="1">
      SERHII KHYLEVYCH
    </text>
    <text x="20" y="46" fill="#94a3b8" class="font-sans" font-size="12">
      Systems Architect &amp; MilTech Strategist • UWE Series
    </text>
  </g>

  <!-- 3. ORBITAL REGION GUIDES -->
  <!-- Van Allen Radiation Belt Indicator -->
  <rect x="1100" y="140" width="280" height="910" fill="url(#vanAllenGrad)" rx="16"/>
  <text x="1240" y="170" fill="#f59e0b" opacity="0.75" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle" letter-spacing="2">
    VAN ALLEN RADIATION BELTS (MEO RAD-HARD REGIME)
  </text>

  <!-- Vertical Orbit Separator Lines -->
  <g stroke="#1e3a5f" stroke-width="1" stroke-dasharray="4 6" opacity="0.45">
    <line x1="660" y1="140" x2="660" y2="1050"/>
    <line x1="910" y1="140" x2="910" y2="1050"/>
    <line x1="1240" y1="140" x2="1240" y2="1050"/>
    <line x1="1580" y1="140" x2="1580" y2="1050"/>
    <line x1="1870" y1="140" x2="1870" y2="1050"/>
    <line x1="2170" y1="140" x2="2170" y2="1050"/>
  </g>

  <!-- Highly Elliptical Orbit E Arc -->
  <path d="M 910 540 C 1350 230, 1750 210, 1870 310" fill="none" stroke="#fb7185" stroke-width="1.8" stroke-dasharray="6 6" opacity="0.55"/>
  <text x="1450" y="240" fill="#fb7185" class="font-mono" font-size="11" opacity="0.85">
    EEO Elliptical Arc (Molniya / Tundra Dwell: Apogee ~40,000 km)
  </text>

  <!-- Cislunar Halo Transfer WSB Line -->
  <path d="M 1580 540 C 1790 470, 1980 410, 2150 430" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-dasharray="8 6" opacity="0.65"/>
  <text x="1820" y="460" fill="#c084fc" class="font-mono" font-size="11" opacity="0.85">
    Weak Stability Boundary (WSB) Transfer to L1/L2
  </text>

  <!-- ========================================================================= -->
  <!-- 4. LEFT SECTOR: SPACE-TO-SURFACE SEGMENT (UGV, UCV, UAV, USV, UUV)        -->
  <!-- ========================================================================= -->

  <!-- Outer Boundary Container: Space-to-Surface Segment -->
  <g transform="translate(45, 140)">
    <!-- Container Card -->
    <rect width="470" height="910" rx="14" fill="url(#segmentPanelBg)" stroke="#00e5ff" stroke-width="1.8" stroke-opacity="0.55"/>

    <!-- Header Banner inside Segment -->
    <rect x="0" y="0" width="470" height="42" rx="14" fill="#0c2d4a" stroke="#00e5ff" stroke-width="1.2" stroke-opacity="0.7"/>
    <text x="235" y="26" fill="#00e5ff" class="font-mono" font-size="13" font-weight="bold" letter-spacing="1.5" text-anchor="middle">
      SPACE-TO-SURFACE SEGMENT (MULTI-DOMAIN)
    </text>

    <!-- Sub-zone 1: Terrestrial & Air Layer (Upper) -->
    <rect x="15" y="52" width="440" height="400" rx="8" fill="url(#terrainGrad)" stroke="#10b981" stroke-width="1" stroke-opacity="0.4"/>
    <text x="28" y="75" fill="#34d399" class="font-mono" font-size="11" font-weight="bold" letter-spacing="1">
      SURFACE &amp; AIR LAYER (GROUND + LOW / HIGH AIRSPACE)
    </text>

    <!-- Sub-zone 2: Maritime & Subsea Layer (Lower) -->
    <rect x="15" y="465" width="440" height="430" rx="8" fill="url(#oceanGrad)" stroke="#0284c7" stroke-width="1" stroke-opacity="0.4"/>
    <text x="28" y="488" fill="#38bdf8" class="font-mono" font-size="11" font-weight="bold" letter-spacing="1">
      MARITIME LAYER (SURFACE WATERLINE &amp; BENTHIC DEPTH)
    </text>
    <text x="28" y="878" fill="#94a3b8" class="font-mono" font-size="10">
      Depth Strata: 0m → 200m (Shelf) → 1000m+ (Pelagic Abyss)
    </text>

    <!-- ======================================================================= -->
    <!-- ASSET 1: UGV (Ground Drone) - RECTANGLE Shape                           -->
    <!-- ======================================================================= -->
    <g transform="translate(35, 270)">
      <rect x="-4" y="-4" width="98" height="58" rx="5" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="1"/>
      <rect x="0" y="0" width="90" height="50" rx="3" fill="#062e24" stroke="#10b981" stroke-width="2.5"/>
      <rect x="8" y="40" width="74" height="6" rx="2" fill="#047857"/>
      <circle cx="25" cy="18" r="6" fill="#10b981"/>
      <text x="42" y="24" fill="#ffffff" class="font-mono" font-size="14" font-weight="bold">UGV</text>
      <text x="45" y="72" fill="#34d399" class="font-sans" font-size="11.5" font-weight="bold" text-anchor="middle">
        UGV Ground
      </text>
    </g>

    <!-- ======================================================================= -->
    <!-- ASSET 2: UCV (Copter Drone) - SQUARE WITH BOLD ROTOR DOTS ON CORNERS    -->
    <!-- Positioned to the right of UGV                                          -->
    <!-- ======================================================================= -->
    <g transform="translate(195, 235)">
      <!-- Corner Rotor Arms -->
      <line x1="-12" y1="-12" x2="52" y2="52" stroke="#34d399" stroke-width="1.8"/>
      <line x1="52" y1="-12" x2="-12" y2="52" stroke="#34d399" stroke-width="1.8"/>
      <!-- Square Body -->
      <rect x="0" y="0" width="40" height="40" rx="3" fill="#08382c" stroke="#10b981" stroke-width="2.5"/>
      <!-- 4 BOLD ROTOR DOTS ON CORNERS -->
      <circle cx="-12" cy="-12" r="6.5" fill="#10b981" stroke="#ffffff" stroke-width="1.5"/>
      <circle cx="52" cy="-12" r="6.5" fill="#10b981" stroke="#ffffff" stroke-width="1.5"/>
      <circle cx="52" cy="52" r="6.5" fill="#10b981" stroke="#ffffff" stroke-width="1.5"/>
      <circle cx="-12" cy="52" r="6.5" fill="#10b981" stroke="#ffffff" stroke-width="1.5"/>
      <!-- Rotor blades spinning effect (subtle circles) -->
      <circle cx="-12" cy="-12" r="11" fill="none" stroke="#34d399" stroke-width="0.8" stroke-dasharray="2 2"/>
      <circle cx="52" cy="-12" r="11" fill="none" stroke="#34d399" stroke-width="0.8" stroke-dasharray="2 2"/>
      <circle cx="52" cy="52" r="11" fill="none" stroke="#34d399" stroke-width="0.8" stroke-dasharray="2 2"/>
      <circle cx="-12" cy="52" r="11" fill="none" stroke="#34d399" stroke-width="0.8" stroke-dasharray="2 2"/>
      <!-- Label in center -->
      <text x="20" y="25" fill="#ffffff" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">UCV</text>
      <text x="20" y="78" fill="#34d399" class="font-sans" font-size="11.5" font-weight="bold" text-anchor="middle">
        UCV Copter
      </text>
    </g>

    <!-- ======================================================================= -->
    <!-- ASSET 3: UAV (Winged Drone) - TRIANGLE Shape                            -->
    <!-- Positioned to the right of UCV in higher airspace                       -->
    <!-- ======================================================================= -->
    <g transform="translate(345, 175)">
      <polygon points="25,0 52,48 -2,48" fill="#0a3252" stroke="#00e5ff" stroke-width="2.5"/>
      <!-- Fuselage centerline & elevons -->
      <line x1="25" y1="0" x2="25" y2="48" stroke="#38bdf8" stroke-width="1.5"/>
      <polygon points="25,6 44,44 6,44" fill="#0284c7" fill-opacity="0.3"/>
      <!-- Label in center -->
      <text x="25" y="38" fill="#ffffff" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">UAV</text>
      <text x="25" y="72" fill="#38bdf8" class="font-sans" font-size="11.5" font-weight="bold" text-anchor="middle">
        UAV Winged
      </text>
    </g>

    <!-- ======================================================================= -->
    <!-- ASSET 4: USV (Surface Drone) - TRAPEZOID (shorter side facing down)     -->
    <!-- Floating on waterline                                                   -->
    <!-- ======================================================================= -->
    <g transform="translate(170, 520)">
      <!-- Waterline Wave -->
      <path d="M -50 0 Q -25 -4, 0 0 T 50 0 T 100 0 T 150 0" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Trapezoid Boat Hull: Top Deck = 100px wide, Bottom = 60px wide facing down -->
      <polygon points="0,0 100,0 80,42 20,42" fill="#073b5c" stroke="#00e5ff" stroke-width="2.5"/>
      <!-- Superstructure -->
      <rect x="30" y="-12" width="40" height="12" rx="2" fill="#0c4a6e" stroke="#00e5ff" stroke-width="1.2"/>
      <circle cx="50" cy="-6" r="3" fill="#38bdf8"/>
      <!-- Label in center -->
      <text x="50" y="27" fill="#ffffff" class="font-mono" font-size="14" font-weight="bold" text-anchor="middle">USV</text>
      <text x="50" y="66" fill="#38bdf8" class="font-sans" font-size="11.5" font-weight="bold" text-anchor="middle">
        USV Surface Strike
      </text>
    </g>

    <!-- ======================================================================= -->
    <!-- ASSET 5: UUV (Subsea Drone) - OVAL Shape in Water Depth                 -->
    <!-- Submerged in benthic water column                                       -->
    <!-- ======================================================================= -->
    <g transform="translate(170, 715)">
      <ellipse cx="50" cy="22" rx="55" ry="26" fill="#0284c7" fill-opacity="0.12"/>
      <ellipse cx="50" cy="22" rx="48" ry="22" fill="#082f49" stroke="#38bdf8" stroke-width="2.5"/>
      <!-- Rudder / Stern -->
      <path d="M 95 15 L 106 7 L 106 37 L 95 29 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.2"/>
      <!-- Label in center -->
      <text x="50" y="27" fill="#ffffff" class="font-mono" font-size="14" font-weight="bold" text-anchor="middle">UUV</text>
      <text x="50" y="66" fill="#7dd3fc" class="font-sans" font-size="11.5" font-weight="bold" text-anchor="middle">
        UUV Subsea / Benthic
      </text>
    </g>

    <!-- ======================================================================= -->
    <!-- INTERNAL CROSS-DOMAIN MESH LINKS (INSIDE SEGMENT)                       -->
    <!-- ======================================================================= -->
    <g stroke="#34d399" stroke-width="1.8" stroke-dasharray="4 3" opacity="0.8">
      <!-- UGV <-> UCV -->
      <line x1="125" y1="285" x2="195" y2="255"/>
      <!-- USV <-> UCV -->
      <line x1="210" y1="520" x2="215" y2="290"/>
    </g>

    <g stroke="#00e5ff" stroke-width="1.8" stroke-dasharray="4 3" opacity="0.85">
      <!-- UAV <-> UGV -->
      <line x1="345" y1="215" x2="125" y2="280"/>
      <!-- UAV <-> UCV -->
      <line x1="345" y1="205" x2="250" y2="245"/>
      <!-- UAV <-> USV -->
      <line x1="365" y1="225" x2="240" y2="520"/>
    </g>

    <!-- Subsea Gateway Acoustic Link: USV <-> UUV -->
    <g stroke="#38bdf8" stroke-width="2" stroke-dasharray="5 4">
      <line x1="220" y1="565" x2="220" y2="715"/>
    </g>
    <!-- Acoustic Ping Waves -->
    <g fill="none" stroke="#38bdf8" stroke-width="1.4" opacity="0.75">
      <path d="M 210 630 A 10 10 0 0 0 230 630"/>
      <path d="M 202 642 A 18 18 0 0 0 238 642"/>
      <path d="M 194 654 A 26 26 0 0 0 246 654"/>
    </g>
    <rect x="155" y="662" width="130" height="20" rx="4" fill="#031e33" stroke="#0284c7" stroke-width="1"/>
    <text x="220" y="676" fill="#38bdf8" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">
      SUBSEA ACOUSTIC
    </text>

    <!-- ======================================================================= -->
    <!-- AGGREGATED GATEWAY PORT (INTERFACING WITH ORBITAL ASSETS)               -->
    <!-- ======================================================================= -->
    <g transform="translate(450, 420)">
      <!-- Outer Pulsing Glow Border -->
      <rect x="-18" y="-45" width="36" height="90" rx="8" fill="#00e5ff" fill-opacity="0.2" stroke="#00e5ff" stroke-width="2"/>
      <rect x="-12" y="-38" width="24" height="76" rx="5" fill="#052538" stroke="#00e5ff" stroke-width="1.8"/>
      <circle cx="0" cy="-20" r="4" fill="#10b981"/>
      <circle cx="0" cy="0" r="5" fill="#00e5ff"/>
      <circle cx="0" cy="20" r="4" fill="#38bdf8"/>
      <!-- Label -->
      <g transform="translate(-160, -8)">
        <rect x="0" y="-12" width="140" height="24" rx="4" fill="#041a2c" stroke="#00e5ff" stroke-width="1"/>
        <text x="70" y="4" fill="#00e5ff" class="font-mono" font-size="9.5" font-weight="bold" text-anchor="middle">
          C4ISR AGGREGATOR
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- 5. ORBITAL SATELLITE NODES (CIRCLES WITH ORBIT LETTER IN CENTER)          -->
  <!-- ========================================================================= -->

  <!-- NODE 1: V (VLEO) -->
  <g transform="translate(660, 560)">
    <path d="M -45 -18 L 45 0 L -45 18 Z" fill="#0891b2" fill-opacity="0.3" stroke="#06b6d4" stroke-width="1.2"/>
    <circle cx="0" cy="0" r="48" fill="#083344" stroke="#06b6d4" stroke-width="2.8" filter="url(#glowCyan)"/>
    <circle cx="0" cy="0" r="38" fill="url(#nodeGradV)"/>
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">V</text>
    <g transform="translate(0, 75)">
      <rect x="-85" y="0" width="170" height="52" rx="6" fill="#082333" stroke="#06b6d4" stroke-width="1.2"/>
      <text x="0" y="20" fill="#00e5ff" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">VLEO HORIZON</text>
      <text x="0" y="38" fill="#94a3b8" class="font-mono" font-size="11" text-anchor="middle">120 – 350 km (ABEP)</text>
    </g>
  </g>

  <!-- NODE 2: L (LEO) -->
  <g transform="translate(910, 560)">
    <rect x="-85" y="-12" width="40" height="24" rx="2" fill="#064e3b" stroke="#10b981" stroke-width="1.2"/>
    <rect x="45" y="-12" width="40" height="24" rx="2" fill="#064e3b" stroke="#10b981" stroke-width="1.2"/>
    <line x1="-85" y1="0" x2="85" y2="0" stroke="#34d399" stroke-width="1"/>
    <circle cx="0" cy="0" r="48" fill="#062e24" stroke="#10b981" stroke-width="3" filter="url(#glowEmerald)"/>
    <circle cx="0" cy="0" r="38" fill="url(#nodeGradL)"/>
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">L</text>
    <g transform="translate(0, 75)">
      <rect x="-85" y="0" width="170" height="52" rx="6" fill="#05251d" stroke="#10b981" stroke-width="1.2"/>
      <text x="0" y="20" fill="#34d399" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">LEO MEGA-SWARM</text>
      <text x="0" y="38" fill="#94a3b8" class="font-mono" font-size="11" text-anchor="middle">350 – 2,000 km (7.8 km/s)</text>
    </g>
  </g>

  <!-- NODE 3: M (MEO) -->
  <g transform="translate(1240, 560)">
    <rect x="-95" y="-15" width="45" height="30" rx="3" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.2"/>
    <rect x="50" y="-15" width="45" height="30" rx="3" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.2"/>
    <circle cx="0" cy="0" r="50" fill="#0c2340" stroke="#38bdf8" stroke-width="3" filter="url(#glowCyan)"/>
    <circle cx="0" cy="0" r="40" fill="url(#nodeGradM)"/>
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">M</text>
    <g transform="translate(0, 80)">
      <rect x="-95" y="0" width="190" height="52" rx="6" fill="#081a2f" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="0" y="20" fill="#38bdf8" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">MEO REGIONAL ANCHOR</text>
      <text x="0" y="38" fill="#94a3b8" class="font-mono" font-size="11" text-anchor="middle">2,000 – 35,786 km (PNT/C2)</text>
    </g>
  </g>

  <!-- NODE 4: G (GEO) -->
  <g transform="translate(1580, 560)">
    <ellipse cx="0" cy="-60" rx="45" ry="14" fill="#78350f" fill-opacity="0.3" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="0" y1="-46" x2="0" y2="-38" stroke="#f59e0b" stroke-width="2"/>
    <rect x="-105" y="-16" width="55" height="32" rx="3" fill="#451a03" stroke="#f59e0b" stroke-width="1.2"/>
    <rect x="50" y="-16" width="55" height="32" rx="3" fill="#451a03" stroke="#f59e0b" stroke-width="1.2"/>
    <circle cx="0" cy="0" r="52" fill="#291404" stroke="#f59e0b" stroke-width="3" filter="url(#glowAmber)"/>
    <circle cx="0" cy="0" r="42" fill="url(#nodeGradG)"/>
    <text x="0" y="13" fill="#ffffff" class="font-sans" font-size="36" font-weight="900" text-anchor="middle">G</text>
    <g transform="translate(0, 80)">
      <rect x="-100" y="0" width="200" height="52" rx="6" fill="#1c0f05" stroke="#f59e0b" stroke-width="1.4"/>
      <text x="0" y="20" fill="#fbbf24" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">GEO STRATEGIC APEX</text>
      <text x="0" y="38" fill="#cbd5e1" class="font-mono" font-size="11" text-anchor="middle">35,786 km (Zero Angular V)</text>
    </g>
  </g>

  <!-- NODE 5: E (EEO Molniya / Tundra Orbit) -->
  <g transform="translate(1870, 310)">
    <circle cx="-35" cy="-25" r="9" fill="#881337" stroke="#fb7185" stroke-width="1.2"/>
    <circle cx="35" cy="-25" r="9" fill="#881337" stroke="#fb7185" stroke-width="1.2"/>
    <circle cx="0" cy="0" r="50" fill="#2d0612" stroke="#fb7185" stroke-width="3" filter="url(#glowPurple)"/>
    <circle cx="0" cy="0" r="40" fill="url(#nodeGradE)"/>
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">E</text>
    <!-- Card Info Callout Placed ABOVE node -->
    <g transform="translate(0, -90)">
      <rect x="-95" y="0" width="190" height="52" rx="6" fill="#20040d" stroke="#fb7185" stroke-width="1.4"/>
      <text x="0" y="20" fill="#fb7185" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">EEO POLAR OVERWATCH</text>
      <text x="0" y="38" fill="#cbd5e1" class="font-mono" font-size="11" text-anchor="middle">Apogee ~40,000 km (i=63.4°)</text>
    </g>
  </g>

  <!-- NODE 6: C (Cislunar / EMO Orbit at the threshold of the Moon) -->
  <g transform="translate(2170, 430)">
    <!-- Moon Visual Behind / Surrounding the Apogee -->
    <circle cx="0" cy="0" r="115" fill="url(#moonGlow)"/>
    <circle cx="70" cy="-30" r="62" fill="url(#moonGrad)" stroke="#94a3b8" stroke-width="1.5"/>
    <ellipse cx="55" cy="-40" rx="9" ry="6" fill="#475569" opacity="0.6"/>
    <ellipse cx="85" cy="-15" rx="14" ry="10" fill="#475569" opacity="0.5"/>
    <ellipse cx="45" cy="-15" rx="7" ry="5" fill="#475569" opacity="0.6"/>
    <ellipse cx="80" cy="-50" rx="6" ry="4" fill="#334155" opacity="0.7"/>

    <rect x="-35" y="-35" width="70" height="70" rx="10" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-dasharray="4 4"/>
    <circle cx="0" cy="0" r="50" fill="#20093b" stroke="#c084fc" stroke-width="3" filter="url(#glowPurple)"/>
    <circle cx="0" cy="0" r="40" fill="url(#nodeGradC)"/>
    <text x="0" y="12" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" text-anchor="middle">C</text>
    <g transform="translate(0, 85)">
      <rect x="-105" y="0" width="210" height="52" rx="6" fill="#17062a" stroke="#c084fc" stroke-width="1.4"/>
      <text x="0" y="20" fill="#c084fc" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">CISLUNAR QUANTUM NEXUS</text>
      <text x="0" y="38" fill="#cbd5e1" class="font-mono" font-size="11" text-anchor="middle">~384,400 km (L1–L5 / NRHO)</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- 6. AGGREGATED SPACE-TO-SURFACE & ORBITAL COMMUNICATIONS GRAPH             -->
  <!-- ========================================================================= -->

  <!-- A. CLEAN AGGREGATED LINKS: V, L, M, G converging onto Space-to-Surface Gateway -->
  <!-- V -> Gateway -->
  <path d="M 660 560 Q 560 560, 495 560" fill="none" stroke="#00e5ff" stroke-width="2.6" stroke-dasharray="6 4" opacity="0.9"/>
  <!-- L -> Gateway -->
  <path d="M 910 560 Q 700 560, 495 560" fill="none" stroke="#10b981" stroke-width="2.6" stroke-dasharray="7 5" opacity="0.95"/>
  <!-- M -> Gateway -->
  <path d="M 1240 560 Q 860 620, 495 560" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-dasharray="8 6" opacity="0.75"/>
  <!-- G -> Gateway -->
  <path d="M 1580 560 Q 1020 680, 495 560" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="10 6" opacity="0.65"/>

  <!-- Aggregated Gateway Badge -->
  <g transform="translate(505, 545)">
    <rect x="0" y="-12" width="130" height="24" rx="4" fill="#041a2c" stroke="#00e5ff" stroke-width="1.2"/>
    <text x="65" y="4" fill="#00e5ff" class="font-mono" font-size="10" font-weight="bold" text-anchor="middle">
      AGGREGATED LINK
    </text>
  </g>

  <!-- B. Intra-Orbital Backbone Crosslinks: G and M communicate with L -->
  <!-- G <-> L Optical Laser Crosslink -->
  <path d="M 1580 535 Q 1240 445, 910 535" fill="none" stroke="#34d399" stroke-width="3" stroke-dasharray="8 4"/>
  <rect x="1200" y="450" width="150" height="24" rx="4" fill="#062e24" stroke="#34d399" stroke-width="1.2"/>
  <text x="1275" y="466" fill="#34d399" class="font-mono" font-size="10.5" font-weight="bold" text-anchor="middle">
    G ⇄ L LASER CROSSLINK
  </text>

  <!-- M <-> L Optical Laser Crosslink -->
  <path d="M 1240 585 Q 1075 640, 910 585" fill="none" stroke="#00e5ff" stroke-width="2.5" stroke-dasharray="6 4"/>
  <rect x="1030" y="625" width="150" height="24" rx="4" fill="#082333" stroke="#00e5ff" stroke-width="1.2"/>
  <text x="1105" y="641" fill="#00e5ff" class="font-mono" font-size="10.5" font-weight="bold" text-anchor="middle">
    M ⇄ L RELAY MESH
  </text>

  <!-- C. High-Tier Crosslinks: E communicates with G, and C communicates with M -->
  <!-- E <-> G Strategic Early-Warning Link -->
  <path d="M 1870 350 Q 1720 430, 1580 535" fill="none" stroke="#fb7185" stroke-width="2.8" stroke-dasharray="7 5"/>
  <rect x="1670" y="415" width="160" height="24" rx="4" fill="#20040d" stroke="#fb7185" stroke-width="1.2"/>
  <text x="1750" y="431" fill="#fb7185" class="font-mono" font-size="10.5" font-weight="bold" text-anchor="middle">
    E ⇄ G STRATEGIC LINK
  </text>

  <!-- C <-> M Deep Cislunar Quantum / Laser Data Bridge -->
  <path d="M 2170 480 Q 1720 830, 1240 585" fill="none" stroke="#c084fc" stroke-width="3" stroke-dasharray="9 5"/>
  <rect x="1670" y="735" width="220" height="26" rx="4" fill="#17062a" stroke="#c084fc" stroke-width="1.2"/>
  <text x="1780" y="752" fill="#c084fc" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">
    C ⇄ M QUANTUM DATA BRIDGE
  </text>

  <!-- ========================================================================= -->
  <!-- 7. TACTICAL LEGEND BOX                                                     -->
  <!-- ========================================================================= -->
  <g transform="translate(540, 895)">
    <rect width="660" height="135" rx="8" fill="#091829" stroke="#1f3d63" stroke-width="1.4"/>
    <text x="20" y="26" fill="#38bdf8" class="font-sans" font-size="14" font-weight="bold" letter-spacing="1">
      NETWORK TOPOLOGY &amp; LINK ROUTING LOGIC
    </text>

    <g transform="translate(20, 42)">
      <line x1="0" y1="12" x2="35" y2="12" stroke="#00e5ff" stroke-width="2.5" stroke-dasharray="5 3"/>
      <text x="45" y="16" fill="#f1f5f9" class="font-sans" font-size="12">
        <tspan font-weight="bold" fill="#00e5ff">V, L, M, G ➔ Aggregated Segment:</tspan> Unified space-to-surface multi-domain C2 feed.
      </text>

      <line x1="0" y1="36" x2="35" y2="36" stroke="#34d399" stroke-width="3" stroke-dasharray="7 4"/>
      <text x="45" y="40" fill="#f1f5f9" class="font-sans" font-size="12">
        <tspan font-weight="bold" fill="#34d399">G, M ➔ L Routing:</tspan> Inter-satellite laser backbone (OISL) for high-bandwidth relay.
      </text>

      <line x1="0" y1="60" x2="35" y2="60" stroke="#c084fc" stroke-width="3" stroke-dasharray="8 4"/>
      <text x="45" y="64" fill="#f1f5f9" class="font-sans" font-size="12">
        <tspan font-weight="bold" fill="#c084fc">E ➔ G &amp; C ➔ M:</tspan> Polar high-apogee &amp; cislunar quantum supervisor bridges.
      </text>

      <line x1="0" y1="84" x2="35" y2="84" stroke="#00e5ff" stroke-width="2.5" stroke-dasharray="4 4"/>
      <text x="45" y="88" fill="#f1f5f9" class="font-sans" font-size="12">
        <tspan font-weight="bold" fill="#38bdf8">Surface/Air Mesh &amp; Subsea Link:</tspan> UGV, UCV, UAV, USV cross-links; USV ⇄ UUV acoustic.
      </text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- 8. BOTTOM DISTANCE & METRIC SCALE BAR (0 km TO 384,400 km)                -->
  <!-- ========================================================================= -->
  <g transform="translate(60, 1070)">
    <rect x="0" y="0" width="2280" height="115" rx="8" fill="#071322" stroke="#172e48" stroke-width="1.4"/>

    <text x="20" y="24" fill="#38bdf8" class="font-mono" font-size="12" font-weight="bold" letter-spacing="1.5">
      PHYSICAL ORBITAL DISTANCE &amp; GRAVITATIONAL VELOCITY SPECTRUM (LOGARITHMIC EXPANSION)
    </text>

    <line x1="20" y1="52" x2="2260" y2="52" stroke="#334155" stroke-width="2.5"/>

    <!-- Tick 0: Earth Surface -->
    <g transform="translate(260, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#00e5ff" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#00e5ff"/>
      <text x="0" y="30" fill="#f8fafc" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">EARTH (SURFACE)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">0 km (Sea Level)</text>
    </g>

    <!-- Tick 1: V (VLEO) -->
    <g transform="translate(610, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#06b6d4" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#06b6d4"/>
      <text x="0" y="30" fill="#00e5ff" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">V (VLEO)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">120 – 350 km</text>
    </g>

    <!-- Tick 2: L (LEO) -->
    <g transform="translate(860, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#10b981" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#10b981"/>
      <text x="0" y="30" fill="#34d399" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">L (LEO)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">350 – 2,000 km</text>
    </g>

    <!-- Tick 3: M (MEO) -->
    <g transform="translate(1180, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#38bdf8" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#38bdf8"/>
      <text x="0" y="30" fill="#38bdf8" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">M (MEO)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">2,000 – 35,786 km</text>
    </g>

    <!-- Tick 4: G (GEO) -->
    <g transform="translate(1520, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#f59e0b" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#f59e0b"/>
      <text x="0" y="30" fill="#fbbf24" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">G (GEO / GSO)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">~35,786 km</text>
    </g>

    <!-- Tick 5: E (EEO) -->
    <g transform="translate(1820, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#fb7185" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#fb7185"/>
      <text x="0" y="30" fill="#fb7185" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">E (EEO TUNDRA)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">Apogee ~40,000 km</text>
    </g>

    <!-- Tick 6: C (Cislunar / Moon Apogee) -->
    <g transform="translate(2120, 52)">
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#c084fc" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="4" fill="#c084fc"/>
      <text x="0" y="30" fill="#c084fc" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">C (CISLUNAR / MOON)</text>
      <text x="0" y="46" fill="#94a3b8" class="font-mono" font-size="10.5" text-anchor="middle">~384,400 km (Lagrange L1–L5)</text>
    </g>

    <!-- Spectrum Bar -->
    <rect x="20" y="50" width="2240" height="4" fill="url(#spectrumBar)"/>
  </g>

  <!-- 9. FOOTER SECTION -->
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

    # Validate XML
    ET.parse(out_svg)
    print("SVG generated and XML verified.")

    base_dir = "/home/hills/Documents/UWS"
    pdf_path = os.path.join(base_dir, "uov_orbital_architecture.pdf")

    # 1. Convert SVG to PDF
    cmd_pdf = [
        "libreoffice",
        "-env:UserInstallation=file:///home/hills/Documents/UWS/.lo_user",
        "--headless",
        "--convert-to", "pdf",
        out_svg,
        "--outdir", base_dir
    ]
    subprocess.run(cmd_pdf, check=True)
    print(f"Generated {pdf_path}")

    # 2. Convert PDF to PNG (150 DPI)
    cmd_png = [
        "pdftoppm",
        "-png",
        "-r", "150",
        pdf_path,
        os.path.join(base_dir, "uov_tmp")
    ]
    subprocess.run(cmd_png, check=True)
    os.rename(os.path.join(base_dir, "uov_tmp-1.png"), os.path.join(base_dir, "uov_orbital_architecture.png"))
    print("Generated uov_orbital_architecture.png")

    # 3. Convert PDF to JPEG
    cmd_jpg = [
        "pdftoppm",
        "-jpeg",
        "-r", "150",
        pdf_path,
        os.path.join(base_dir, "uov_tmp")
    ]
    subprocess.run(cmd_jpg, check=True)
    os.rename(os.path.join(base_dir, "uov_tmp-1.jpg"), os.path.join(base_dir, "uov_orbital_architecture.jpg"))
    print("Generated uov_orbital_architecture.jpg")

if __name__ == "__main__":
    generate_svg()
