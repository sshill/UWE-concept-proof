#!/usr/bin/env python3
"""
Master Infographic Generator v2 for UWE Multi-Domain Cyber-Physical Architecture
Implements user feedback:
1. Significantly widened inter-column spacing (220px gutters) to expose rich background environments
2. Deep, vivid, highly expressive visual environmental backgrounds with domain-specific art:
   - Space: Curving glowing Earth limb, bright starfields, multi-altitude orbital tracks, constellation nodes
   - Air: Stratospheric sky gradient, supersonic streamlines, flight level altitude scale (FL600-FL050), pressure vectors
   - Land: Topographic contour lines with elevation labels, tactical trench profiles, soil strata & shear boundaries
   - Sea: Actual undulating ocean waves with foam, thermocline SVP acoustic channel, bathymetric abyss
   - METOC: Dynamic storm isobars, mud rasputitsa shear envelope, adversary RF jammer PSD curve, Anti-1812 warning
   - Cyber: High-tech neon PCB circuit traces, copper vias, CPS dual feedback loop, 48-bit MCU registers
3. Thick, bold, luminous arrows (3.5px - 5px width, large heads, glow effects)
4. Full cross-domain and diagonal links from the original PlantUML (Cyber -> EAL, Probes -> EAL, Feasibility -> CPS, Mesh <-> Token)
5. 3752 x 2658 pixel ultra-high resolution conforming to A4 landscape ratio (1.412:1)
"""

import os
import subprocess
import xml.etree.ElementTree as ET

def generate_svg():
    width = 2400
    height = 1700
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Master Deep Cosmic / Tactical Background -->
    <linearGradient id="masterDarkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#030611"/>
      <stop offset="50%" stop-color="#060b17"/>
      <stop offset="100%" stop-color="#02040a"/>
    </linearGradient>

    <!-- Glowing Filters -->
    <filter id="glowCyan" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowGreen" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowAmber" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowPurple" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <!-- Arrow Marker Definitions -->
    <marker id="arrowCyan" markerWidth="14" markerHeight="14" refX="10" refY="7" orient="auto">
      <polygon points="0 2, 12 7, 0 12, 3 7" fill="#00e5ff"/>
    </marker>
    <marker id="arrowBlue" markerWidth="14" markerHeight="14" refX="10" refY="7" orient="auto">
      <polygon points="0 2, 12 7, 0 12, 3 7" fill="#38bdf8"/>
    </marker>
    <marker id="arrowGreen" markerWidth="14" markerHeight="14" refX="10" refY="7" orient="auto">
      <polygon points="0 2, 12 7, 0 12, 3 7" fill="#22c55e"/>
    </marker>
    <marker id="arrowAmber" markerWidth="14" markerHeight="14" refX="10" refY="7" orient="auto">
      <polygon points="0 2, 12 7, 0 12, 3 7" fill="#f59e0b"/>
    </marker>
    <marker id="arrowPurple" markerWidth="14" markerHeight="14" refX="10" refY="7" orient="auto">
      <polygon points="0 2, 12 7, 0 12, 3 7" fill="#d946ef"/>
    </marker>

    <!-- Vivid Environment Background Gradients -->
    <!-- 1. Space: Deep Cosmic Indigo with Star Nebula -->
    <linearGradient id="vividSpace" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#05081a"/>
      <stop offset="30%" stop-color="#12103a"/>
      <stop offset="65%" stop-color="#1a124a"/>
      <stop offset="100%" stop-color="#080c24"/>
    </linearGradient>
    <radialGradient id="earthLimbGlow" cx="15%" cy="110%" r="90%">
      <stop offset="0%" stop-color="#00f5d4" stop-opacity="0.45"/>
      <stop offset="35%" stop-color="#0284c7" stop-opacity="0.3"/>
      <stop offset="70%" stop-color="#1e1b4b" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <!-- 2. Air: High-Altitude Stratospheric Azure to Aero Cyan -->
    <linearGradient id="vividAir" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#07223d"/>
      <stop offset="35%" stop-color="#0a3966"/>
      <stop offset="70%" stop-color="#0c4a85"/>
      <stop offset="100%" stop-color="#082b4f"/>
    </linearGradient>

    <!-- 3. Land: Rich Tactical Terrain Green with Earth Tones -->
    <linearGradient id="vividLand" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0d2410"/>
      <stop offset="35%" stop-color="#143d1a"/>
      <stop offset="70%" stop-color="#1a4d22"/>
      <stop offset="100%" stop-color="#0e2912"/>
    </linearGradient>

    <!-- 4. Sea: Luminous Marine Turquoise to Abyssal Navy -->
    <linearGradient id="vividSea" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#05263b"/>
      <stop offset="35%" stop-color="#084266"/>
      <stop offset="70%" stop-color="#0b5280"/>
      <stop offset="100%" stop-color="#052b42"/>
    </linearGradient>

    <!-- 5. METOC: Severe Weather, Viscous Mud Rasputitsa & Warning Ochre -->
    <linearGradient id="vividMetoc" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#381d06"/>
      <stop offset="35%" stop-color="#592e09"/>
      <stop offset="70%" stop-color="#6e370a"/>
      <stop offset="100%" stop-color="#3b1e06"/>
    </linearGradient>

    <!-- 6. Cyber: Neon Electric Circuit & Silicon Matrix -->
    <linearGradient id="vividCyber" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#24073d"/>
      <stop offset="35%" stop-color="#3d0b66"/>
      <stop offset="70%" stop-color="#4d0e82"/>
      <stop offset="100%" stop-color="#260740"/>
    </linearGradient>

    <!-- Solid High-Tech Card Backdrops -->
    <linearGradient id="cardMDO" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0b1324" stop-opacity="1.0"/>
      <stop offset="100%" stop-color="#070c18" stop-opacity="1.0"/>
    </linearGradient>
    <linearGradient id="cardUWE" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#041f33" stop-opacity="1.0"/>
      <stop offset="100%" stop-color="#021220" stop-opacity="1.0"/>
    </linearGradient>
    <linearGradient id="cardCPS" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#130e24" stop-opacity="1.0"/>
      <stop offset="100%" stop-color="#090614" stop-opacity="1.0"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans {{ font-family: 'Inter', 'Segoe UI', -apple-system, Arial, sans-serif; }}
    .font-mono {{ font-family: 'JetBrains Mono', 'Roboto Mono', 'SF Mono', Consolas, monospace; }}
  </style>

  <!-- Base Canvas Fill -->
  <rect width="{width}" height="{height}" fill="url(#masterDarkBg)"/>

  <!-- ========================================================================= -->
  <!-- 1. MASTER HEADER BANNER                                                   -->
  <!-- ========================================================================= -->
  <g transform="translate(50, 20)">
    <rect width="2300" height="115" rx="10" fill="#08101e" fill-opacity="0.94" stroke="#00e5ff" stroke-width="2" filter="url(#glowCyan)"/>
    <rect width="2300" height="115" rx="10" fill="#08101e" fill-opacity="0.94" stroke="#00e5ff" stroke-width="1.8"/>
    
    <!-- Corner Tech Brackets -->
    <path d="M 0 25 L 0 0 L 25 0" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
    <path d="M 2300 25 L 2300 0 L 2275 0" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
    <path d="M 0 90 L 0 115 L 25 115" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
    <path d="M 2300 90 L 2300 115 L 2275 115" fill="none" stroke="#38bdf8" stroke-width="3.5"/>

    <!-- Category Pill -->
    <rect x="25" y="16" width="340" height="25" rx="5" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="35" y="33" fill="#38bdf8" class="font-mono" font-size="11.5" font-weight="bold" letter-spacing="1.5">SOVEREIGN ARCHITECTURAL SPECIFICATION</text>

    <!-- Main Title -->
    <text x="25" y="74" fill="#ffffff" class="font-sans" font-size="27" font-weight="900" letter-spacing="0.5">
      UNMANNED WARFARE ENGINE (UWE) — MULTI-DOMAIN CYBER-PHYSICAL ARCHITECTURE
    </text>
    
    <!-- Subtitle -->
    <text x="25" y="98" fill="#94a3b8" class="font-sans" font-size="13.5" font-weight="600">
      Strategic Operational Chain: Multi-Domain Operations (MDO Doctrines) ──► Algorithmic Feasibility (UWE Platform) ──► Cyber-Physical Systems (CPS Execution)
    </text>

    <!-- Meta Information Cards -->
    <g transform="translate(1600, 22)">
      <rect width="320" height="72" rx="6" fill="#040c17" stroke="#1e293b" stroke-width="1.2"/>
      <text x="16" y="24" fill="#64748b" class="font-mono" font-size="10.5" font-weight="bold">SYSTEMS STRATEGIST &amp; ARCHITECT:</text>
      <text x="16" y="45" fill="#38bdf8" class="font-sans" font-size="14" font-weight="bold">Serhii Khylevych</text>
      <text x="16" y="62" fill="#94a3b8" class="font-mono" font-size="10">MilTech Architect &amp; Doctrine Author</text>
    </g>

    <g transform="translate(1940, 22)">
      <rect width="335" height="72" rx="6" fill="#040c17" stroke="#1e293b" stroke-width="1.2"/>
      <text x="16" y="24" fill="#64748b" class="font-mono" font-size="10.5" font-weight="bold">MANDATORY REGULATORY BASELINE:</text>
      <text x="16" y="44" fill="#a855f7" class="font-mono" font-size="11" font-weight="bold">MOSA 10 U.S.C. 4401 • STANAG 4754</text>
      <text x="16" y="62" fill="#10b981" class="font-mono" font-size="10.5">NIST SP 1500-201 (CPS) • IEEE 1451 • JP 3-59</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- 2. COLUMN HEADERS (Wider spacing: Col 1 w=520, Col 2 w=640, Col 3 w=680) -->
  <!-- Gutters: x: 580..800 (220px) and x: 1440..1660 (220px)                     -->
  <!-- ========================================================================= -->
  <!-- Column 1 Header: MDO -->
  <g transform="translate(60, 148)">
    <rect width="520" height="46" rx="6" fill="#0c1929" stroke="#3b82f6" stroke-width="2"/>
    <rect x="0" y="0" width="6" height="46" rx="3" fill="#3b82f6"/>
    <text x="18" y="28" fill="#ffffff" class="font-sans" font-size="14.5" font-weight="900" letter-spacing="0.8">COLUMN 1: MDO (OPERATIONS)</text>
    <text x="360" y="28" fill="#60a5fa" class="font-mono" font-size="11" font-weight="bold">[ STRATEGIC DOCTRINE ]</text>
  </g>

  <!-- Column 2 Header: UWE Platform -->
  <g transform="translate(800, 148)">
    <rect width="640" height="46" rx="6" fill="#042236" stroke="#00e5ff" stroke-width="2.2" filter="url(#glowCyan)"/>
    <rect width="640" height="46" rx="6" fill="#042236" stroke="#00e5ff" stroke-width="2"/>
    <rect x="0" y="0" width="6" height="46" rx="3" fill="#00e5ff"/>
    <text x="20" y="28" fill="#ffffff" class="font-sans" font-size="14.5" font-weight="900" letter-spacing="0.8">COLUMN 2: UWE CORE PLATFORM (ENGINE)</text>
    <text x="445" y="28" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold">[ ALGORITHMIC KERNEL ]</text>
  </g>

  <!-- Column 3 Header: CPS Execution -->
  <g transform="translate(1660, 148)">
    <rect width="680" height="46" rx="6" fill="#1b0e2b" stroke="#c026d3" stroke-width="2"/>
    <rect x="0" y="0" width="6" height="46" rx="3" fill="#c026d3"/>
    <text x="18" y="28" fill="#ffffff" class="font-sans" font-size="14.5" font-weight="900" letter-spacing="0.8">COLUMN 3: CPS (CYBER-PHYSICAL SYSTEMS)</text>
    <text x="450" y="28" fill="#e879f9" class="font-mono" font-size="11" font-weight="bold">[ HARDWARE &amp; ACTUATORS ]</text>
  </g>
"""

    def generate_domain_row_v2(y_pos, height_row, domain_name, theme_color, bg_gradient,
                               bg_art_svg,
                               col1_data, col2_data, col3_data,
                               gutter1_content_svg, gutter2_content_svg):
        row_svg = f"""
  <!-- ========================================================================= -->
  <!-- DOMAIN ROW: {domain_name} (y={y_pos}, h={height_row}) -->
  <!-- ========================================================================= -->
  <!-- 1. FULL-WIDTH HORIZONTAL ENVIRONMENT BAND -->
  <g transform="translate(45, {y_pos})">
    <rect width="2310" height="{height_row}" rx="12" fill="{bg_gradient}" stroke="{theme_color}" stroke-width="1.4" stroke-opacity="0.7"/>
    {bg_art_svg}
    <g transform="translate(2290, 32)">
      <text x="0" y="0" fill="{theme_color}" fill-opacity="0.35" class="font-sans" font-size="28" font-weight="900" text-anchor="end" letter-spacing="2">
        {domain_name.upper().replace('&AMP;', '&amp;')}
      </text>
    </g>
  </g>

  <!-- 2. COLUMN 1 CARD: MDO (x=60, w=520) -->
  <g transform="translate(60, {y_pos + 10})">
    <rect width="520" height="{height_row - 20}" rx="8" fill="url(#cardMDO)" stroke="{theme_color}" stroke-width="1.8" stroke-opacity="0.85"/>
    <rect x="0" y="0" width="5" height="{height_row - 20}" rx="2" fill="{theme_color}"/>
    
    <rect x="14" y="12" width="492" height="26" rx="4" fill="{theme_color}" fill-opacity="0.18" stroke="{theme_color}" stroke-width="1"/>
    <text x="24" y="29" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">{col1_data['title']}</text>
    <text x="496" y="29" fill="{theme_color}" class="font-mono" font-size="10" font-weight="bold" text-anchor="end">{col1_data['doc']}</text>
    
    <g transform="translate(18, 48)">
      {col1_data['icon_svg']}
      <g transform="translate(75, 4)">
        {col1_data['body_svg']}
      </g>
    </g>
  </g>

  <!-- 3. GUTTER 1 CONNECTIONS & ENVIRONMENT (x: 580..800, width: 220px!) -->
  <g transform="translate(580, {y_pos})">
    {gutter1_content_svg}
  </g>

  <!-- 4. COLUMN 2 CARD: UWE CORE PLATFORM (x=800, w=640) -->
  <g transform="translate(800, {y_pos + 10})">
    <rect width="640" height="{height_row - 20}" rx="8" fill="url(#cardUWE)" stroke="#00e5ff" stroke-width="2.2" stroke-opacity="0.9" filter="url(#glowCyan)"/>
    <rect width="640" height="{height_row - 20}" rx="8" fill="url(#cardUWE)" stroke="#00e5ff" stroke-width="2"/>
    <rect x="0" y="0" width="6" height="{height_row - 20}" rx="3" fill="#00e5ff"/>
    
    <rect x="16" y="12" width="608" height="26" rx="4" fill="#00e5ff" fill-opacity="0.18" stroke="#00e5ff" stroke-width="1.2"/>
    <text x="26" y="29" fill="#ffffff" class="font-sans" font-size="13" font-weight="bold">{col2_data['title']}</text>
    <text x="614" y="29" fill="#00e5ff" class="font-mono" font-size="10.5" font-weight="bold" text-anchor="end">{col2_data['badge']}</text>
    
    <g transform="translate(18, 48)">
      {col2_data['icon_svg']}
      <g transform="translate(85, 4)">
        {col2_data['body_svg']}
      </g>
    </g>
  </g>

  <!-- 5. GUTTER 2 CONNECTIONS & ENVIRONMENT (x: 1440..1660, width: 220px!) -->
  <g transform="translate(1440, {y_pos})">
    {gutter2_content_svg}
  </g>

  <!-- 6. COLUMN 3 CARD: CPS EXECUTION (x=1660, w=680) -->
  <g transform="translate(1660, {y_pos + 10})">
    <rect width="680" height="{height_row - 20}" rx="8" fill="url(#cardCPS)" stroke="{theme_color}" stroke-width="1.8" stroke-opacity="0.85"/>
    <rect x="0" y="0" width="5" height="{height_row - 20}" rx="2" fill="{theme_color}"/>
    
    <rect x="14" y="12" width="652" height="26" rx="4" fill="{theme_color}" fill-opacity="0.18" stroke="{theme_color}" stroke-width="1"/>
    <text x="24" y="29" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">{col3_data['title']}</text>
    <text x="656" y="29" fill="{theme_color}" class="font-mono" font-size="10" font-weight="bold" text-anchor="end">{col3_data['standards']}</text>
    
    <g transform="translate(18, 48)">
      {col3_data['icon_svg']}
      <g transform="translate(85, 4)">
        {col3_data['body_svg']}
      </g>
    </g>
  </g>
"""
        return row_svg

    # ROW 1: SPACE DOMAIN
    bg_art_space = """
    <ellipse cx="250" cy="380" rx="600" ry="250" fill="url(#earthLimbGlow)"/>
    <path d="M 0 190 C 180 150, 360 160, 530 190" fill="none" stroke="#00e5ff" stroke-width="2.2" opacity="0.6"/>
    <text x="260" y="165" fill="#00e5ff" class="font-mono" font-size="10" opacity="0.8">KARMAN LINE: 100 km (ATMOSPHERIC BOUNDARY)</text>

    <circle cx="620" cy="50" r="2" fill="#ffffff" opacity="0.9"/>
    <circle cx="680" cy="120" r="1.5" fill="#818cf8" opacity="0.8"/>
    <circle cx="740" cy="40" r="2.5" fill="#38bdf8" opacity="0.9"/>
    <circle cx="770" cy="160" r="1.2" fill="#ffffff" opacity="0.7"/>

    <circle cx="1470" cy="45" r="1.8" fill="#ffffff" opacity="0.8"/>
    <circle cx="1520" cy="130" r="2.2" fill="#c084fc" opacity="0.9"/>
    <circle cx="1580" cy="65" r="1.5" fill="#38bdf8" opacity="0.7"/>
    <circle cx="1630" cy="155" r="2" fill="#ffffff" opacity="0.8"/>

    <path d="M 0 170 C 600 45, 1500 35, 2310 120" fill="none" stroke="#6366f1" stroke-width="2.8" stroke-dasharray="10 6" opacity="0.7"/>
    <circle cx="700" cy="88" r="4" fill="#00e5ff" filter="url(#glowCyan)"/>
    <text x="715" y="92" fill="#38bdf8" class="font-mono" font-size="10.5" font-weight="bold">LEO (v = 7.8 km/s)</text>
    <circle cx="1550" cy="62" r="4" fill="#a855f7" filter="url(#glowPurple)"/>
    <text x="1565" y="66" fill="#c084fc" class="font-mono" font-size="10.5" font-weight="bold">VLEO DECAY ZONE</text>
    """

    gutter1_space = """
    <g transform="translate(10, 107)">
      <line x1="15" y1="0" x2="185" y2="0" stroke="#6366f1" stroke-width="5" filter="url(#glowPurple)"/>
      <line x1="15" y1="0" x2="185" y2="0" stroke="#a5b4fc" stroke-width="3" marker-end="url(#arrowBlue)"/>
      <circle cx="15" cy="0" r="6" fill="#6366f1"/>
      <rect x="45" y="-18" width="115" height="18" rx="4" fill="#070d1e" stroke="#818cf8" stroke-width="1.2"/>
      <text x="102" y="-5" fill="#818cf8" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">MDO INTENT INGEST</text>
    </g>
    """

    gutter2_space = """
    <g transform="translate(10, 107)">
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#00e5ff" stroke-width="4.5" filter="url(#glowCyan)"/>
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#ffffff" stroke-width="2.5" marker-end="url(#arrowCyan)"/>
      <line x1="185" y1="14" x2="15" y2="14" stroke="#10b981" stroke-width="4" stroke-dasharray="6 4"/>
      <polygon points="15,14 27,9 27,19" fill="#10b981"/>
      <rect x="35" y="-34" width="130" height="16" rx="3" fill="#021a2c" stroke="#00e5ff" stroke-width="1"/>
      <text x="100" y="-22" fill="#00e5ff" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">REACTION TORQUE CMD</text>
      <rect x="35" y="20" width="130" height="16" rx="3" fill="#031e18" stroke="#10b981" stroke-width="1"/>
      <text x="100" y="32" fill="#10b981" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">TELEMETRY &amp; BUS STATUS</text>
    </g>
    """

    col1_space = {
        'title': 'MDO SPACE DOMAIN',
        'doc': 'JP 3-14 / SDP 1-0',
        'icon_svg': """
        <g transform="translate(28, 38)">
          <!-- Core celestial sphere -->
          <circle cx="0" cy="0" r="7" fill="#4338ca" stroke="#c7d2fe" stroke-width="1.5" filter="url(#glowPurple)"/>
          <circle cx="-2" cy="-2" r="2" fill="#c7d2fe" opacity="0.8"/>
          <!-- Orbital ellipse 1 (inclined -35 deg) -->
          <ellipse cx="0" cy="0" rx="25" ry="9" transform="rotate(-35)" fill="none" stroke="#818cf8" stroke-width="1.8"/>
          <circle cx="18" cy="-11" r="2.5" fill="#00e5ff" filter="url(#glowCyan)"/>
          <!-- Orbital ellipse 2 (inclined +35 deg) -->
          <ellipse cx="0" cy="0" rx="25" ry="9" transform="rotate(35)" fill="none" stroke="#a5b4fc" stroke-width="1.6" stroke-dasharray="5 2.5"/>
          <circle cx="-16" cy="-12" r="2" fill="#e0e7ff"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• Strategic Early Warning &amp; Deep Reconnaissance</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Resilient High-Throughput SATCOM Uplinks (SDR/Optical)</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Space Domain Awareness (SDA) &amp; PNT Constellations</text>
        <text y="72" fill="#818cf8" class="font-mono" font-size="10.5" font-weight="bold">Doctrinal Focus: Space Superiority &amp; Orbital C2</text>
        """
    }

    col2_space = {
        'title': 'UWE NAMESPACE UOV (SPACE HLD-1)',
        'badge': 'ORBITAL KINEMATICS',
        'icon_svg': """
        <g transform="translate(32, 38)">
          <rect x="-30" y="-10" width="16" height="20" rx="2" fill="#0891b2" stroke="#00e5ff" stroke-width="1.2"/>
          <rect x="14" y="-10" width="16" height="20" rx="2" fill="#0891b2" stroke="#00e5ff" stroke-width="1.2"/>
          <circle cx="0" cy="0" r="18" fill="#083344" stroke="#00e5ff" stroke-width="2.2" filter="url(#glowCyan)"/>
          <circle cx="0" cy="0" r="18" fill="#083344" stroke="#00e5ff" stroke-width="2"/>
          <text x="0" y="5" fill="#ffffff" class="font-mono" font-size="11" font-weight="900" text-anchor="middle">UOV</text>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Orbital Mechanics Ingestion &amp; VLEO Drag Profiling</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Autonomous Station-Keeping, Non-Keplerian Trajectory Shaping</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• C-4 Ground Infrastructure Coupling (Spaceports, Uplinks, Tracking)</text>
        <text y="72" fill="#00e5ff" class="font-mono" font-size="10.5" font-weight="bold">Kinematic Contract: Reaction Wheels, Cold-Gas, Micro-Impulse</text>
        """
    }

    col3_space = {
        'title': 'UOV-HAL DOMAIN DRIVERS',
        'standards': 'ECSS / CCSDS / IEEE 1451',
        'icon_svg': """
        <g transform="translate(30, 38)">
          <circle cx="0" cy="0" r="22" fill="#181126" stroke="#c084fc" stroke-width="2"/>
          <circle cx="0" cy="0" r="14" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="4 2"/>
          <rect x="-4" y="-4" width="8" height="8" fill="#e879f9"/>
          <path d="M 0 -22 L 0 -27 M 0 22 L 0 27 M -22 0 L -27 0 M 22 0 L 27 0" stroke="#c084fc" stroke-width="2"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• Reaction Wheels &amp; Cold-Gas Solenoid Drivers (LLD)</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Spacecraft Bus Decoupling Architecture &amp; Closed Thermal Loops</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Magnetorquer Earth Magnetic Dipole Actuation</text>
        <text y="72" fill="#c084fc" class="font-mono" font-size="10.5" font-weight="bold">Interface Contract: IKinematicDrive &amp; Spacecraft Bus</text>
        """
    }

    row1 = generate_domain_row_v2(
        205, 215, "Space Domain", "#6366f1", "url(#vividSpace)",
        bg_art_space, col1_space, col2_space, col3_space,
        gutter1_space, gutter2_space
    )

    # ROW 2: AIR DOMAIN
    bg_art_air = """
    <path d="M 0 90 Q 400 45, 800 85 T 1600 70 T 2310 95" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-opacity="0.6"/>
    <path d="M 0 135 Q 500 110, 1100 145 T 1900 120 T 2310 140" fill="none" stroke="#0ea5e9" stroke-width="1.8" stroke-dasharray="6 3" stroke-opacity="0.5"/>
    <path d="M 0 175 Q 600 155, 1400 180 T 2310 165" fill="none" stroke="#7dd3fc" stroke-width="1.2" stroke-opacity="0.4"/>
    
    <g transform="translate(620, 45)">
      <rect width="130" height="22" rx="4" fill="#032b49" stroke="#38bdf8" stroke-width="1"/>
      <text x="65" y="15" fill="#38bdf8" class="font-mono" font-size="10" font-weight="bold" text-anchor="middle">FL600 (HALE 20km)</text>
    </g>
    <g transform="translate(1480, 150)">
      <rect width="130" height="22" rx="4" fill="#032b49" stroke="#0ea5e9" stroke-width="1"/>
      <text x="65" y="15" fill="#7dd3fc" class="font-mono" font-size="10" font-weight="bold" text-anchor="middle">FL050 (TACTICAL COPTER)</text>
    </g>

    <polygon points="700,105 715,115 700,125 685,115" fill="none" stroke="#ffffff" stroke-width="1.5" opacity="0.6"/>
    <polygon points="1550,85 1565,95 1550,105 1535,95" fill="none" stroke="#ffffff" stroke-width="1.5" opacity="0.6"/>
    """

    gutter1_air = """
    <g transform="translate(10, 107)">
      <line x1="15" y1="0" x2="185" y2="0" stroke="#0284c7" stroke-width="5" filter="url(#glowCyan)"/>
      <line x1="15" y1="0" x2="185" y2="0" stroke="#bae6fd" stroke-width="3" marker-end="url(#arrowBlue)"/>
      <circle cx="15" cy="0" r="6" fill="#0284c7"/>
      <rect x="45" y="-18" width="115" height="18" rx="4" fill="#061c30" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="102" y="-5" fill="#38bdf8" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">AIR TASKING ORDER</text>
    </g>
    """

    gutter2_air = """
    <g transform="translate(10, 107)">
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#00e5ff" stroke-width="4.5" filter="url(#glowCyan)"/>
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#ffffff" stroke-width="2.5" marker-end="url(#arrowCyan)"/>
      <line x1="185" y1="14" x2="15" y2="14" stroke="#10b981" stroke-width="4" stroke-dasharray="6 4"/>
      <polygon points="15,14 27,9 27,19" fill="#10b981"/>
      <rect x="35" y="-34" width="130" height="16" rx="3" fill="#021a2c" stroke="#00e5ff" stroke-width="1"/>
      <text x="100" y="-22" fill="#00e5ff" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">FOC ESC SPEED / TORQUE</text>
      <rect x="35" y="20" width="130" height="16" rx="3" fill="#031e18" stroke="#10b981" stroke-width="1"/>
      <text x="100" y="32" fill="#10b981" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">15G OVERRIDE TRIGGER</text>
    </g>
    """

    col1_air = {
        'title': 'MDO AIR DOMAIN',
        'doc': 'FM 3-0 / JP 3-30',
        'icon_svg': """
        <g transform="translate(28, 38)">
          <!-- Dynamic Airflow Streamlines & Vectors -->
          <path d="M -24 -14 C -8 -18, 6 -8, 16 -12 C 22 -14, 25 -10, 20 -7" fill="none" stroke="#7dd3fc" stroke-width="2.2" stroke-linecap="round"/>
          <path d="M -26 0 C -10 -4, 8 6, 20 0 C 26 -3, 27 3, 21 5" fill="none" stroke="#00e5ff" stroke-width="2.6" stroke-linecap="round" filter="url(#glowCyan)"/>
          <path d="M -26 0 C -10 -4, 8 6, 20 0 C 26 -3, 27 3, 21 5" fill="none" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round"/>
          <path d="M -22 14 C -6 10, 10 18, 22 12" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
          <polygon points="23,0 17,-3 17,3" fill="#ffffff"/>
          <polygon points="23,12 17,9 17,15" fill="#38bdf8"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• Deep Fires Synchronization &amp; Offensive Counter-Air</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• High-Altitude Theater Persistent ISR (HALE / MALE)</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Collaborative Combat Aircraft (CCA) Swarm Penetration</text>
        <text y="72" fill="#38bdf8" class="font-mono" font-size="10.5" font-weight="bold">Doctrinal Focus: Theater Air Superiority &amp; Strike</text>
        """
    }

    col2_air = {
        'title': 'UWE NAMESPACES UAV &amp; UCV (AIR HLD-1)',
        'badge': 'AERO &amp; DISC DYNAMICS',
        'icon_svg': """
        <g transform="translate(32, 38)">
          <!-- UAV (Top) -->
          <g transform="translate(0, -18)">
            <polygon points="0,-13 22,7 11,7 0,3 -11,7 -22,7" fill="#073b5c" stroke="#00e5ff" stroke-width="1.8"/>
            <text x="0" y="3.5" fill="#ffffff" class="font-mono" font-size="8.5" font-weight="900" text-anchor="middle">UAV</text>
          </g>
          <!-- UCV (Bottom with vertical gap) -->
          <g transform="translate(0, 22)">
            <rect x="-14" y="-11" width="28" height="22" rx="3" fill="#08382c" stroke="#10b981" stroke-width="1.8"/>
            <circle cx="-14" cy="-11" r="3.5" fill="#10b981" stroke="#fff" stroke-width="0.8"/>
            <circle cx="14" cy="-11" r="3.5" fill="#10b981" stroke="#fff" stroke-width="0.8"/>
            <circle cx="14" cy="11" r="3.5" fill="#10b981" stroke="#fff" stroke-width="0.8"/>
            <circle cx="-14" cy="11" r="3.5" fill="#10b981" stroke="#fff" stroke-width="0.8"/>
            <text x="0" y="3" fill="#ffffff" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">UCV</text>
          </g>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Aerodynamic Glide Polars &amp; Disc-Loading Dynamic Limits</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Mothercraft Heavy Carrier Decoupling &amp; Swarm Deployment</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Tier C-4 Airfield Infrastructure (Paved Runways, Hangars, Arrester)</text>
        <text y="72" fill="#00e5ff" class="font-mono" font-size="10.5" font-weight="bold">Decoupled Lethality: Interchangeable Munitions / One-Way (OWM)</text>
        """
    }

    col3_air = {
        'title': 'UAV/UCV-HAL DOMAIN DRIVERS',
        'standards': 'STANAG 4586 / MOSA / ARINC 664',
        'icon_svg': """
        <g transform="translate(30, 38)">
          <circle cx="0" cy="0" r="22" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
          <path d="M -16 -16 L 16 16 M -16 16 L 16 -16" stroke="#0ea5e9" stroke-width="3"/>
          <circle cx="0" cy="0" r="7" fill="#38bdf8"/>
          <path d="M 14 -18 L 6 -6 L 14 -4 L 8 16" fill="none" stroke="#fbbf24" stroke-width="2"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• FOC ESC Inverter Drivers &amp; Dynamic Propeller Active Braking</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• 15G Limit Overrides on Terminal Impact (Thermal Safety Bypass)</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Multi-Rotor Torque Mixer &amp; Aerodynamic Elevon Servos</text>
        <text y="72" fill="#38bdf8" class="font-mono" font-size="10.5" font-weight="bold">Driver Interface: IFocEscController &amp; IActuatorAero</text>
        """
    }

    row2 = generate_domain_row_v2(
        428, 215, "Air Domain", "#0ea5e9", "url(#vividAir)",
        bg_art_air, col1_air, col2_air, col3_air,
        gutter1_air, gutter2_air
    )

    # ROW 3: LAND DOMAIN
    bg_art_land = """
    <path d="M 0 100 Q 300 70, 700 95 T 1400 80 T 2310 110" fill="none" stroke="#22c55e" stroke-width="1.8" stroke-opacity="0.6"/>
    <path d="M 0 140 Q 400 110, 800 135 T 1600 120 T 2310 150" fill="none" stroke="#16a34a" stroke-width="1.5" stroke-opacity="0.5"/>
    <text x="630" y="85" fill="#4ade80" class="font-mono" font-size="9" opacity="0.8">CONTOUR: 140m</text>
    <text x="1490" y="70" fill="#4ade80" class="font-mono" font-size="9" opacity="0.8">CONTOUR: 160m</text>

    <g transform="translate(630, 150)">
      <path d="M 0 0 L 30 0 L 40 25 L 80 25 L 90 0 L 140 0" fill="none" stroke="#4ade80" stroke-width="2"/>
      <text x="65" y="40" fill="#4ade80" class="font-mono" font-size="9" text-anchor="middle">TRENCH DEFENSE LINE</text>
    </g>
    <g transform="translate(1480, 150)">
      <path d="M 0 0 L 25 0 L 35 25 L 75 25 L 85 0 L 130 0" fill="none" stroke="#4ade80" stroke-width="2"/>
      <text x="60" y="40" fill="#4ade80" class="font-mono" font-size="9" text-anchor="middle">SOIL SATURATION LINE</text>
    </g>
    """

    gutter1_land = """
    <g transform="translate(10, 107)">
      <line x1="15" y1="0" x2="185" y2="0" stroke="#16a34a" stroke-width="5" filter="url(#glowGreen)"/>
      <line x1="15" y1="0" x2="185" y2="0" stroke="#86efac" stroke-width="3" marker-end="url(#arrowGreen)"/>
      <circle cx="15" cy="0" r="6" fill="#16a34a"/>
      <rect x="45" y="-18" width="115" height="18" rx="4" fill="#0a2110" stroke="#22c55e" stroke-width="1.2"/>
      <text x="102" y="-5" fill="#4ade80" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">GROUND CORRIDOR</text>
    </g>
    """

    gutter2_land = """
    <g transform="translate(10, 107)">
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#22c55e" stroke-width="4.5" filter="url(#glowGreen)"/>
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#ffffff" stroke-width="2.5" marker-end="url(#arrowGreen)"/>
      <line x1="185" y1="14" x2="15" y2="14" stroke="#10b981" stroke-width="4" stroke-dasharray="6 4"/>
      <polygon points="15,14 27,9 27,19" fill="#10b981"/>
      <rect x="35" y="-34" width="130" height="16" rx="3" fill="#04200c" stroke="#22c55e" stroke-width="1"/>
      <text x="100" y="-22" fill="#4ade80" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">SKID-STEER TORQUE</text>
      <rect x="35" y="20" width="130" height="16" rx="3" fill="#031e18" stroke="#10b981" stroke-width="1"/>
      <text x="100" y="32" fill="#10b981" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">V2V POWER SHARING</text>
    </g>
    """

    col1_land = {
        'title': 'MDO LAND DOMAIN',
        'doc': 'FM 3-0 / ATP 3-90',
        'icon_svg': """
        <g transform="translate(28, 38)">
          <rect x="-22" y="-12" width="44" height="20" rx="3" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
          <rect x="-18" y="8" width="36" height="8" rx="4" fill="#22c55e"/>
          <circle cx="-10" cy="12" r="3" fill="#14532d"/>
          <circle cx="0" cy="12" r="3" fill="#14532d"/>
          <circle cx="10" cy="12" r="3" fill="#14532d"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• Combined Arms Close Maneuver &amp; Breach Operations</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Dispersed Force Protection &amp; Autonomous Logistics Supply</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Forward Trench Penetration &amp; Static Area Fortification</text>
        <text y="72" fill="#22c55e" class="font-mono" font-size="10.5" font-weight="bold">Doctrinal Focus: Ground Combat Maneuver &amp; Hold</text>
        """
    }

    col2_land = {
        'title': 'UWE NAMESPACE UGV (GROUND HLD-1)',
        'badge': 'TERRAMECHANICS',
        'icon_svg': """
        <g transform="translate(32, 38)">
          <rect x="-24" y="-14" width="48" height="28" rx="4" fill="#062e24" stroke="#10b981" stroke-width="2.2"/>
          <rect x="-18" y="8" width="36" height="5" rx="2" fill="#047857"/>
          <text x="0" y="3" fill="#ffffff" class="font-mono" font-size="12" font-weight="900" text-anchor="middle">UGV</text>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Bekker-Wong Soil Mechanics &amp; Trafficability Verification</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Ground Pressure (kg/cm²) Pre-Flight Gating for Mud Rasputitsa</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Trench Gap Spanning &amp; Step Obstacle Climbing Feasibility</text>
        <text y="72" fill="#00e5ff" class="font-mono" font-size="10.5" font-weight="bold">Tabor Defense Service (LLD-3): Circular Perimeter Bastion</text>
        """
    }

    col3_land = {
        'title': 'UGV-HAL DOMAIN DRIVERS',
        'standards': 'STANAG 4754 (NGVA) / MIL-STD-810H',
        'icon_svg': """
        <g transform="translate(30, 38)">
          <circle cx="-10" cy="0" r="14" fill="#052e16" stroke="#22c55e" stroke-width="1.8"/>
          <circle cx="10" cy="0" r="14" fill="#052e16" stroke="#22c55e" stroke-width="1.8"/>
          <path d="M -10 -14 L 10 -14 M -10 14 L 10 14" stroke="#4ade80" stroke-width="2"/>
          <rect x="-4" y="-8" width="8" height="16" fill="#22c55e"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• Differential Skid-Steer Torque &amp; Dynamic Slip Sensing (LLD)</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Bidirectional V2V Charging BMS Bridge for Dismounted Infantry</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• High-Torque Planetary Planetary Hubs &amp; Trench Gearing</text>
        <text y="72" fill="#22c55e" class="font-mono" font-size="10.5" font-weight="bold">Driver Interface: IKinematicDrive &amp; IPowerEnergy (BMS)</text>
        """
    }

    row3 = generate_domain_row_v2(
        651, 215, "Land Domain", "#22c55e", "url(#vividLand)",
        bg_art_land, col1_land, col2_land, col3_land,
        gutter1_land, gutter2_land
    )

    # ROW 4: MARITIME DOMAIN
    bg_art_sea = """
    <path d="M 0 65 Q 150 40, 300 65 T 600 65 T 900 65 T 1200 65 T 1500 65 T 1800 65 T 2100 65 T 2310 65" fill="none" stroke="#00e5ff" stroke-width="2.8" opacity="0.8"/>
    <path d="M 0 75 Q 150 50, 300 75 T 600 75 T 900 75 T 1200 75 T 1500 75 T 1800 75 T 2100 75 T 2310 75" fill="none" stroke="#38bdf8" stroke-width="1.8" opacity="0.5"/>
    
    <line x1="0" y1="135" x2="2310" y2="135" stroke="#0284c7" stroke-width="2" stroke-dasharray="8 4" stroke-opacity="0.6"/>
    <g transform="translate(615, 125)">
      <rect width="140" height="20" rx="3" fill="#05273d" stroke="#0284c7" stroke-width="1"/>
      <text x="70" y="14" fill="#38bdf8" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">THERMOCLINE BOUNDARY</text>
    </g>
    <g transform="translate(1475, 125)">
      <rect width="140" height="20" rx="3" fill="#05273d" stroke="#0284c7" stroke-width="1"/>
      <text x="70" y="14" fill="#38bdf8" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">SOFAR DUCTING CHANNEL</text>
    </g>

    <g transform="translate(1550, 160)" fill="none" stroke="#38bdf8" stroke-width="1.8" opacity="0.8">
      <path d="M -15 0 A 15 15 0 0 1 15 0"/>
      <path d="M -25 0 A 25 25 0 0 1 25 0"/>
      <path d="M -35 0 A 35 35 0 0 1 35 0"/>
    </g>
    """

    gutter1_sea = """
    <g transform="translate(10, 107)">
      <line x1="15" y1="0" x2="185" y2="0" stroke="#0284c7" stroke-width="5" filter="url(#glowCyan)"/>
      <line x1="15" y1="0" x2="185" y2="0" stroke="#67e8f9" stroke-width="3" marker-end="url(#arrowCyan)"/>
      <circle cx="15" cy="0" r="6" fill="#0284c7"/>
      <rect x="45" y="-18" width="115" height="18" rx="4" fill="#052136" stroke="#00e5ff" stroke-width="1.2"/>
      <text x="102" y="-5" fill="#00e5ff" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">LITTORAL STRIKE ORDER</text>
    </g>
    """

    gutter2_sea = """
    <g transform="translate(10, 107)">
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#00e5ff" stroke-width="4.5" filter="url(#glowCyan)"/>
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#ffffff" stroke-width="2.5" marker-end="url(#arrowCyan)"/>
      <line x1="185" y1="14" x2="15" y2="14" stroke="#10b981" stroke-width="4" stroke-dasharray="6 4"/>
      <polygon points="15,14 27,9 27,19" fill="#10b981"/>
      <rect x="35" y="-34" width="130" height="16" rx="3" fill="#021a2c" stroke="#00e5ff" stroke-width="1"/>
      <text x="100" y="-22" fill="#00e5ff" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">WATERJET VECTOR THRUST</text>
      <rect x="35" y="20" width="130" height="16" rx="3" fill="#031e18" stroke="#10b981" stroke-width="1"/>
      <text x="100" y="32" fill="#10b981" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">BENTHIC DEPTH / SONAR</text>
    </g>
    """

    col1_sea = {
        'title': 'MDO MARITIME DOMAIN',
        'doc': 'JP 3-32 / NWP 3-0',
        'icon_svg': """
        <g transform="translate(28, 38)">
          <!-- Oceanic Sea Waves -->
          <path d="M -26 -10 Q -14 -22, -2 -10 T 22 -10" fill="none" stroke="#00e5ff" stroke-width="2.5" stroke-linecap="round" filter="url(#glowCyan)"/>
          <path d="M -26 -10 Q -14 -22, -2 -10 T 22 -10" fill="none" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
          <path d="M -22 4 Q -10 -8, 2 4 T 26 4" fill="none" stroke="#38bdf8" stroke-width="2.4" stroke-linecap="round"/>
          <path d="M -26 18 Q -14 6, -2 18 T 22 18" fill="none" stroke="#0891b2" stroke-width="2.2" stroke-linecap="round"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• Anti-Surface Warfare (ASuW) &amp; Littoral Choke-Point Denial</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Anti-Submarine Warfare (ASW) Multi-Static Acoustic Barriers</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Mine Countermeasures (MCM) &amp; Seabed Infrastructure Shield</text>
        <text y="72" fill="#06b6d4" class="font-mono" font-size="10.5" font-weight="bold">Doctrinal Focus: Sea Control &amp; Expeditionary Defense</text>
        """
    }

    col2_sea = {
        'title': 'UWE NAMESPACES USV &amp; UUV (MARITIME HLD-1)',
        'badge': 'HYDRODYNAMICS',
        'icon_svg': """
        <g transform="translate(32, 38)">
          <!-- USV (Top) -->
          <g transform="translate(0, -16)">
            <rect x="-5" y="-9" width="10" height="5" rx="1" fill="#00e5ff"/>
            <polygon points="-24,-4 24,-4 16,8 -16,8" fill="#073b5c" stroke="#00e5ff" stroke-width="1.8"/>
            <text x="0" y="4.5" fill="#ffffff" class="font-mono" font-size="8.5" font-weight="900" text-anchor="middle">USV</text>
          </g>
          <!-- UUV (Bottom with vertical gap) -->
          <g transform="translate(0, 22)">
            <ellipse cx="0" cy="0" rx="22" ry="9" fill="#082f49" stroke="#38bdf8" stroke-width="1.8"/>
            <polygon points="-22,0 -27,-4 -27,4" fill="#38bdf8"/>
            <text x="0" y="3.5" fill="#ffffff" class="font-mono" font-size="8.5" font-weight="900" text-anchor="middle">UUV</text>
          </g>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Wave Slamming Acceleration Limits (15G Gz at Sea State 6)</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Biomimetic Ribbon-Fin Crawling for Surf-Zone Minefield Breaching</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Variable Ballast Equilibrium &amp; Sound Velocity Profile (SVP) Routing</text>
        <text y="72" fill="#00e5ff" class="font-mono" font-size="10.5" font-weight="bold">Container Model: Port, Mothership Well-Deck &amp; Torpedo Tube (C0-C4)</text>
        """
    }

    col3_sea = {
        'title': 'USV/UUV-HAL DOMAIN DRIVERS',
        'standards': 'STANAG 4754 / MIL-STD-810H / IEEE 1451',
        'icon_svg': """
        <g transform="translate(30, 38)">
          <rect x="-18" y="-12" width="36" height="24" rx="3" fill="#083344" stroke="#06b6d4" stroke-width="1.8"/>
          <path d="M 18 -6 L 26 -10 L 26 10 L 18 6 Z" fill="#06b6d4"/>
          <path d="M 28 -8 Q 36 0, 28 8" fill="none" stroke="#38bdf8" stroke-width="2"/>
          <circle cx="-6" cy="0" r="5" fill="#38bdf8"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• Steerable Waterjets, Vector Thrust Servos &amp; Ribbon Fin Drivers</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• High-Pressure Variable Ballast Subsea Pump Controllers</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Deep-Water Acoustic Modems &amp; Hydrodynamic Pressure Sensor Ingest</text>
        <text y="72" fill="#06b6d4" class="font-mono" font-size="10.5" font-weight="bold">Driver Interface: IHydroDrive &amp; IAcousticTransceiver</text>
        """
    }

    row4 = generate_domain_row_v2(
        874, 215, "Maritime Domain", "#06b6d4", "url(#vividSea)",
        bg_art_sea, col1_sea, col2_sea, col3_sea,
        gutter1_sea, gutter2_sea
    )

    # ROW 5: METOC & OPERATIONAL ENVIRONMENT (THE "ANTI-1812" REALITY)
    bg_art_metoc = """
    <path d="M 0 70 Q 300 40, 700 80 T 1400 65 T 2310 90" fill="none" stroke="#f59e0b" stroke-width="2.5" opacity="0.7"/>
    <path d="M 0 110 Q 400 80, 900 120 T 1800 100 T 2310 130" fill="none" stroke="#fbbf24" stroke-width="1.8" stroke-dasharray="8 4" opacity="0.6"/>
    
    <g transform="translate(620, 140)">
      <rect width="140" height="24" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="70" y="16" fill="#fbbf24" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">MUD RASPUTITSA SHEAR</text>
    </g>
    <g transform="translate(1480, 140)">
      <rect width="140" height="24" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="70" y="16" fill="#fbbf24" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">RF JAMMING PSD FLOOR</text>
    </g>

    <g transform="translate(1550, 75)">
      <polygon points="0,30 -10,12 10,12" fill="#fbbf24"/>
      <line x1="0" y1="-10" x2="0" y2="12" stroke="#fbbf24" stroke-width="3"/>
      <text x="0" y="45" fill="#fbbf24" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">SOIL BEARING TEST</text>
    </g>
    """

    gutter1_metoc = """
    <g transform="translate(10, 112)">
      <!-- Horizontal MDO METOC -> UWE EAL -->
      <line x1="15" y1="0" x2="185" y2="0" stroke="#f59e0b" stroke-width="5" filter="url(#glowAmber)"/>
      <line x1="15" y1="0" x2="185" y2="0" stroke="#fef08a" stroke-width="3" marker-end="url(#arrowAmber)"/>
      <circle cx="15" cy="0" r="6" fill="#f59e0b"/>
      
      <rect x="45" y="-18" width="115" height="18" rx="4" fill="#2d1502" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="102" y="-5" fill="#fbbf24" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">METOC 4D TELEMETRY</text>

      <!-- Diagonal Link from Row 6 (MDO Cyber) up to UWE EAL! -->
      <path d="M 15 150 C 60 120, 120 40, 185 10" fill="none" stroke="#d946ef" stroke-width="3.5" stroke-dasharray="6 4" filter="url(#glowPurple)"/>
      <polygon points="185,10 172,12 176,2" fill="#d946ef"/>
      <rect x="55" y="65" width="125" height="16" rx="3" fill="#24073d" stroke="#d946ef" stroke-width="1"/>
      <text x="117" y="77" fill="#e879f9" class="font-mono" font-size="8" font-weight="bold" text-anchor="middle">MAPS SPECTRUM THREATS</text>
    </g>
    """

    gutter2_metoc = """
    <g transform="translate(10, 112)">
      <!-- Massive Reverse Ingest Arrow: Probes -> EAL World Model -->
      <line x1="185" y1="0" x2="15" y2="0" stroke="#f59e0b" stroke-width="5.5" filter="url(#glowAmber)"/>
      <line x1="185" y1="0" x2="15" y2="0" stroke="#ffffff" stroke-width="3.2"/>
      <polygon points="15,0 30,-6 24,0 30,6" fill="#ffffff"/>
      <circle cx="185" cy="0" r="6" fill="#f59e0b"/>

      <rect x="35" y="-24" width="135" height="18" rx="4" fill="#3b1d06" stroke="#fbbf24" stroke-width="1.2"/>
      <text x="102" y="-11" fill="#fbbf24" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">RAW SENSORY INGEST (EAL)</text>

      <!-- Downward Feasibility Validation Link into Row 6 Feasibility Engine! -->
      <path d="M 15 15 C 40 50, 60 100, 60 150" fill="none" stroke="#00e5ff" stroke-width="3.5" stroke-dasharray="6 4"/>
      <polygon points="60,150 55,138 65,138" fill="#00e5ff"/>
      <rect x="68" y="70" width="120" height="16" rx="3" fill="#042236" stroke="#00e5ff" stroke-width="1"/>
      <text x="128" y="82" fill="#00e5ff" class="font-mono" font-size="8" font-weight="bold" text-anchor="middle">GATES KINEMATICS (Phi)</text>
    </g>
    """

    col1_metoc = {
        'title': 'METOC &amp; OPERATIONAL ENVIRONMENT',
        'doc': 'JP 3-59 / JP 2-01.3 / ATP 3-34.80',
        'icon_svg': """
        <g transform="translate(28, 42)">
          <circle cx="0" cy="0" r="22" fill="#451a03" stroke="#f59e0b" stroke-width="2"/>
          <path d="M -12 -6 Q 0 -14, 12 -6 T 0 10" fill="none" stroke="#fbbf24" stroke-width="2"/>
          <circle cx="0" cy="0" r="3" fill="#f59e0b"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• JP 3-59: Meteorological &amp; Oceanographic Operations (METOC)</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• JP 2-01.3: Joint Intelligence Preparation of the Env. (JIPOE)</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• ATP 3-34.80: Military Terramechanics &amp; Trafficability Corridors</text>
        <text y="72" fill="#f59e0b" class="font-mono" font-size="10.5" font-weight="bold">The '1812' Trap: Doctrine without Physics = 100% Fleet Loss</text>
        """
    }

    col2_metoc = {
        'title': 'EAL: CYBER-PHYSICAL WORLD MODEL (HLD-0)',
        'badge': 'DYNAMIC 4D TENSOR',
        'icon_svg': """
        <g transform="translate(32, 42)">
          <rect x="-24" y="-20" width="48" height="40" rx="4" fill="#241405" stroke="#f59e0b" stroke-width="2"/>
          <line x1="-24" y1="0" x2="24" y2="0" stroke="#fbbf24" stroke-width="1.2"/>
          <line x1="0" y1="-20" x2="0" y2="20" stroke="#fbbf24" stroke-width="1.2"/>
          <circle cx="0" cy="0" r="5" fill="#00e5ff"/>
          <text x="0" y="27" fill="#f59e0b" class="font-mono" font-size="8" font-weight="bold" text-anchor="middle">EAL 4D</text>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Environmental Abstraction Layer (HLD-0) — CPS World Model</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Standards: NIST SP 1500-201 (CPS Framework) / ISO/IEC 21823</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Continuous Real-Time Ingest: Soil Shear, Wave Force (Gz), Icing, RF</text>
        <text y="72" fill="#00e5ff" class="font-mono" font-size="10.5" font-weight="bold">Pre-Flight Barrier: Blocks Kinematically Impossible Missions</text>
        """
    }

    col3_metoc = {
        'title': 'EAL PHYSICAL SENSORY PROBES (LLD-E0)',
        'standards': 'IEEE 1451 / STANAG 4754 / MIL-STD-810H',
        'icon_svg': """
        <g transform="translate(30, 42)">
          <circle cx="0" cy="0" r="22" fill="#291404" stroke="#f59e0b" stroke-width="1.8"/>
          <polygon points="0,18 -8,6 8,6" fill="#fbbf24"/>
          <line x1="0" y1="-14" x2="0" y2="6" stroke="#fbbf24" stroke-width="2.5"/>
          <path d="M -16 -4 Q 0 -12, 16 -4" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
          <path d="M -20 -10 Q 0 -18, 20 -10" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• Ground-Penetrating Radar (GPR) &amp; Cone Penetrometers (Soil Shear)</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• CTD Ocean Profilers &amp; Micro-LIDAR Wind Shear Scanners</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Frontline SDR Jamming Power Spectral Density (PSD) Telemetry</text>
        <text y="72" fill="#f59e0b" class="font-mono" font-size="10.5" font-weight="bold">Sensory Standard: IEEE 1451 Smart Transducer Standard / NGVA</text>
        """
    }

    row5 = generate_domain_row_v2(
        1097, 225, "METOC &amp; Environment", "#f59e0b", "url(#vividMetoc)",
        bg_art_metoc, col1_metoc, col2_metoc, col3_metoc,
        gutter1_metoc, gutter2_metoc
    )

    # ROW 6: CYBERSPACE & CPS
    bg_art_cyber = """
    <path d="M 0 100 L 500 100 L 560 60 L 1100 60 L 1160 100 L 1800 100 L 1860 140 L 2310 140" fill="none" stroke="#d946ef" stroke-width="2.2" stroke-opacity="0.7"/>
    <path d="M 0 140 L 400 140 L 450 170 L 1300 170 L 1350 140 L 2310 140" fill="none" stroke="#c026d3" stroke-width="1.8" stroke-dasharray="6 3" stroke-opacity="0.5"/>
    
    <circle cx="560" cy="60" r="4.5" fill="#f0abfc" filter="url(#glowPurple)"/>
    <circle cx="1160" cy="100" r="4.5" fill="#f0abfc" filter="url(#glowPurple)"/>
    <circle cx="1860" cy="140" r="4.5" fill="#f0abfc" filter="url(#glowPurple)"/>

    <!-- CPS Master Feedback Loop Icon in Gutter 2 -->
    <g transform="translate(1550, 105)">
      <path d="M -30 -10 A 30 30 0 0 1 30 -10" fill="none" stroke="#00e5ff" stroke-width="3" marker-end="url(#arrowCyan)"/>
      <path d="M 30 10 A 30 30 0 0 1 -30 10" fill="none" stroke="#d946ef" stroke-width="3" marker-end="url(#arrowPurple)"/>
      <text x="0" y="-35" fill="#00e5ff" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">CYBER</text>
      <text x="0" y="45" fill="#e879f9" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">PHYSICAL</text>
    </g>
    """

    gutter1_cyber = """
    <g transform="translate(10, 112)">
      <line x1="15" y1="0" x2="185" y2="0" stroke="#c026d3" stroke-width="5" filter="url(#glowPurple)"/>
      <line x1="15" y1="0" x2="185" y2="0" stroke="#f5d0fe" stroke-width="3" marker-end="url(#arrowPurple)"/>
      <circle cx="15" cy="0" r="6" fill="#c026d3"/>
      
      <rect x="45" y="-18" width="115" height="18" rx="4" fill="#200636" stroke="#d946ef" stroke-width="1.2"/>
      <text x="102" y="-5" fill="#f0abfc" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">ZERO TRUST MESH</text>
    </g>
    """

    gutter2_cyber = """
    <g transform="translate(10, 112)">
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#00e5ff" stroke-width="5" filter="url(#glowCyan)"/>
      <line x1="15" y1="-14" x2="185" y2="-14" stroke="#ffffff" stroke-width="3" marker-end="url(#arrowCyan)"/>
      
      <line x1="185" y1="14" x2="15" y2="14" stroke="#d946ef" stroke-width="4.5"/>
      <polygon points="15,14 27,9 27,19" fill="#d946ef"/>
      
      <rect x="35" y="-34" width="130" height="16" rx="3" fill="#021a2c" stroke="#00e5ff" stroke-width="1"/>
      <text x="100" y="-22" fill="#00e5ff" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">PRE-FLIGHT AUTH [Phi>0]</text>
      <rect x="35" y="20" width="130" height="16" rx="3" fill="#2b0840" stroke="#d946ef" stroke-width="1"/>
      <text x="100" y="32" fill="#f0abfc" class="font-mono" font-size="8.5" font-weight="bold" text-anchor="middle">48-BIT MCU REGISTER BUS</text>
    </g>
    """

    col1_cyber = {
        'title': 'MDO CYBERSPACE &amp; EW',
        'doc': 'JP 3-12 / NIST SP 800-160',
        'icon_svg': """
        <g transform="translate(28, 42)">
          <path d="M 0 -20 L 18 -10 L 18 10 C 18 20, 0 26, 0 26 C 0 26, -18 20, -18 10 L -18 -10 Z" fill="#3b0764" stroke="#c026d3" stroke-width="2"/>
          <circle cx="0" cy="0" r="5" fill="#e879f9"/>
          <line x1="0" y1="5" x2="0" y2="12" stroke="#e879f9" stroke-width="2"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• Offensive (OCO) &amp; Defensive (DCO) Cyberspace Operations</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Electromagnetic Warfare (EW) &amp; Spectrum Dominance (EMSO)</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Zero Trust High-Assurance C2 Architecture (NIST SP 800-160)</text>
        <text y="72" fill="#c026d3" class="font-mono" font-size="10.5" font-weight="bold">Doctrinal Focus: JP 3-12 / AJP-3.20 Cyber Defense</text>
        """
    }

    col2_cyber = {
        'title': 'UWE RESILIENT MESH &amp; FEASIBILITY (HLD-2/3)',
        'badge': 'MICROSECOND KILL WEB',
        'icon_svg': """
        <g transform="translate(32, 42)">
          <rect x="-26" y="-18" width="52" height="36" rx="4" fill="#1e0836" stroke="#c026d3" stroke-width="2"/>
          <text x="0" y="-3" fill="#00e5ff" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">[XX]-[YY]</text>
          <text x="0" y="10" fill="#e879f9" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">-[ZZ]</text>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Mission Feasibility Engine (HLD-3): Phi = F(K, L, E, C, T)</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• Cognitive Dual-Read Token: [XX]-[YY]-[ZZ] (Human / Edge-AI Parsed)</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• Self-Healing Cross-Network Mesh (Laser, COFDM, Acoustic, Fiber)</text>
        <text y="72" fill="#00e5ff" class="font-mono" font-size="10.5" font-weight="bold">Targeting Handoff: Zero-Latency Sensor-to-Shooter Web</text>
        """
    }

    col3_cyber = {
        'title': 'CPS UNIVERSAL CONTRACTS &amp; REGISTERS',
        'standards': 'NIST SP 1500-201 / STANAG 4754',
        'icon_svg': """
        <g transform="translate(30, 42)">
          <rect x="-16" y="-16" width="32" height="32" rx="3" fill="#2e1065" stroke="#e879f9" stroke-width="2"/>
          <rect x="-8" y="-8" width="16" height="16" rx="1" fill="#c026d3"/>
          <path d="M -16 -10 L -22 -10 M -16 0 L -22 0 M -16 10 L -22 10" stroke="#e879f9" stroke-width="2"/>
          <path d="M 16 -10 L 22 -10 M 16 0 L 22 0 M 16 10 L 22 10" stroke="#e879f9" stroke-width="2"/>
          <path d="M -10 -16 L -10 -22 M 0 -16 L 0 -22 M 10 -16 L 10 -22" stroke="#e879f9" stroke-width="2"/>
          <path d="M -10 16 L -10 22 M 0 16 L 0 22 M 10 16 L 10 22" stroke="#e879f9" stroke-width="2"/>
        </g>
        """,
        'body_svg': """
        <text y="14" fill="#ffffff" class="font-sans" font-size="12" font-weight="bold">• IPowerEnergy: Battery Management &amp; Deep Sleep 'Zhdun' (&lt;5mA)</text>
        <text y="33" fill="#cbd5e1" class="font-sans" font-size="11.5">• IPayloadAttachment: STANAG 4754 Pinout, OWM Crypto-Fuze Arming</text>
        <text y="52" fill="#cbd5e1" class="font-sans" font-size="11.5">• ITokenRegistry: 48-bit MCU Word Register, Single-Cycle Bitmask</text>
        <text y="72" fill="#e879f9" class="font-mono" font-size="10.5" font-weight="bold">Embedded Framework: Cyber-Physical Systems (CPS Execution)</text>
        """
    }

    row6 = generate_domain_row_v2(
        1330, 225, "Cyberspace &amp; CPS", "#c026d3", "url(#vividCyber)",
        bg_art_cyber, col1_cyber, col2_cyber, col3_cyber,
        gutter1_cyber, gutter2_cyber
    )

    # MASTER FOOTER
    footer = """
  <g transform="translate(50, 1572)">
    <rect width="2300" height="104" rx="8" fill="#060d1a" stroke="#00e5ff" stroke-width="1.8" filter="url(#glowCyan)"/>
    <rect width="2300" height="104" rx="8" fill="#060d1a" stroke="#00e5ff" stroke-width="1.5"/>
    <rect x="0" y="0" width="8" height="104" rx="4" fill="#00e5ff"/>
    
    <text x="25" y="28" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold" letter-spacing="1.5">
      THE FOUR INVARIANT LAWS OF THE UNMANNED WARFARE ENGINE (UWE)
    </text>
    <text x="750" y="28" fill="#94a3b8" class="font-sans" font-size="11.5">
      Cyber-Physical Principles for High-Attrition Autonomous Multi-Domain Warfare
    </text>
    
    <g transform="translate(25, 42)">
      <g transform="translate(0, 0)">
        <rect width="530" height="50" rx="5" fill="#09182a" stroke="#0284c7" stroke-width="1.4"/>
        <text x="14" y="20" fill="#38bdf8" class="font-sans" font-size="12" font-weight="bold">LAW I: KINEMATIC PRIMACY</text>
        <text x="14" y="38" fill="#cbd5e1" class="font-sans" font-size="11">Contact physics dictates software feasibility, never the reverse.</text>
      </g>
      
      <g transform="translate(550, 0)">
        <rect width="530" height="50" rx="5" fill="#091f18" stroke="#10b981" stroke-width="1.4"/>
        <text x="14" y="20" fill="#34d399" class="font-sans" font-size="12" font-weight="bold">LAW II: HIERARCHICAL CONTAINERIZATION</text>
        <text x="14" y="38" fill="#cbd5e1" class="font-sans" font-size="11">Scales friction from C0 man-pack up to C4 airfields &amp; naval ports.</text>
      </g>
      
      <g transform="translate(1100, 0)">
        <rect width="530" height="50" rx="5" fill="#241407" stroke="#f59e0b" stroke-width="1.4"/>
        <text x="14" y="20" fill="#fbbf24" class="font-sans" font-size="12" font-weight="bold">LAW III: HARDWARE ABSTRACTION &amp; OWM</text>
        <text x="14" y="38" fill="#cbd5e1" class="font-sans" font-size="11">Decoupled robotic chassis from mission payloads &amp; sacrificial fuzes.</text>
      </g>
      
      <g transform="translate(1650, 0)">
        <rect width="600" height="50" rx="5" fill="#1e092b" stroke="#c026d3" stroke-width="1.4"/>
        <text x="14" y="20" fill="#e879f9" class="font-sans" font-size="12" font-weight="bold">LAW IV: COGNITIVE SYNCHRONIZATION</text>
        <text x="14" y="38" fill="#cbd5e1" class="font-sans" font-size="11">[XX]-[YY]-[ZZ] dual-read tokens: human readable, edge-AI parsed.</text>
      </g>
    </g>
  </g>
</svg>
"""

    svg_content = svg + row1 + row2 + row3 + row4 + row5 + row6 + footer

    out_svg = "/home/hills/Documents/UWS/uwe_mdo_cps_infographic.svg"
    with open(out_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {out_svg}")
    return out_svg

def convert_to_raster(svg_path):
    base_dir = os.path.dirname(svg_path)
    pdf_path = os.path.join(base_dir, "uwe_mdo_cps_infographic.pdf")
    
    cmd_pdf = [
        "libreoffice",
        "-env:UserInstallation=file:///home/hills/Documents/UWS/.lo_user",
        "--headless",
        "--convert-to", "pdf",
        svg_path,
        "--outdir", base_dir
    ]
    subprocess.run(cmd_pdf, check=True)
    print(f"Generated {pdf_path}")

    cmd_png = [
        "pdftoppm",
        "-png",
        "-r", "150",
        pdf_path,
        os.path.join(base_dir, "uwe_infographic_tmp")
    ]
    subprocess.run(cmd_png, check=True)
    
    tmp_png = os.path.join(base_dir, "uwe_infographic_tmp-1.png")
    final_png = os.path.join(base_dir, "uwe_mdo_cps_infographic.png")
    if os.path.exists(tmp_png):
        if os.path.exists(final_png):
            os.remove(final_png)
        os.rename(tmp_png, final_png)
        print(f"Generated {final_png}")

    cmd_jpg = [
        "pdftoppm",
        "-jpeg",
        "-r", "150",
        pdf_path,
        os.path.join(base_dir, "uwe_infographic_tmp")
    ]
    subprocess.run(cmd_jpg, check=True)
    tmp_jpg = os.path.join(base_dir, "uwe_infographic_tmp-1.jpg")
    final_jpg = os.path.join(base_dir, "uwe_mdo_cps_infographic.jpg")
    if os.path.exists(tmp_jpg):
        if os.path.exists(final_jpg):
            os.remove(final_jpg)
        os.rename(tmp_jpg, final_jpg)
        print(f"Generated {final_jpg}")

if __name__ == "__main__":
    svg_file = generate_svg()
    convert_to_raster(svg_file)
