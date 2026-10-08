#!/usr/bin/env python3
"""
Master Infographic Generator for UWE Multi-Domain Cyber-Physical Architecture
Creates a high-resolution, presentation-grade vector infographic (SVG) and raster (PNG)
Conforms to A4 landscape ratio (2400 x 1700), containing:
- 3 Distinct Vertical Columns: MDO (Left), UWE Platform (Center), CPS (Right)
- 6 Horizontal Environmental Bands representing specific operating media:
  1. Space Domain (Exoatmosphere / Orbit)
  2. Air Domain (Stratosphere / Low Airspace)
  3. Land Domain (Terrestrial Ground &amp; Trenches)
  4. Maritime Domain (Surface Littoral &amp; Subsea)
  5. METOC &amp; Physical Environment (The "Anti-1812" Reality)
  6. Cyberspace &amp; CPS (Electromagnetic Spectrum, Digital C2 &amp; Embedded Hardware)
- Authentic UOV, UAV, UCV, UGV, USV, UUV and standard CPS symbology
- Official normative indices (JP 3-59, JP 2-01.3, ATP 3-34.80, NIST SP 1500-201, IEEE 1451, STANAG 4754)
"""

import os
import subprocess
import xml.etree.ElementTree as ET

def generate_svg():
    width = 2400
    height = 1700
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Master Background Gradient -->
    <linearGradient id="masterBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="#070c18"/>
      <stop offset="100%" stop-color="#04060d"/>
    </linearGradient>

    <!-- Tactical Grid Pattern -->
    <pattern id="tacGrid" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#1e293b" stroke-width="0.7" stroke-opacity="0.35"/>
      <circle cx="60" cy="60" r="1.2" fill="#38bdf8" fill-opacity="0.25"/>
    </pattern>

    <!-- Circuit Trace Pattern for Cyber Band -->
    <pattern id="circuitPattern" width="80" height="80" patternUnits="userSpaceOnUse">
      <path d="M 10 10 L 40 10 L 50 20 L 70 20 M 20 40 L 20 60 L 30 70 M 60 50 L 75 50" fill="none" stroke="#c026d3" stroke-width="0.8" stroke-opacity="0.2"/>
      <circle cx="10" cy="10" r="2" fill="#c026d3" fill-opacity="0.3"/>
      <circle cx="70" cy="20" r="2" fill="#c026d3" fill-opacity="0.3"/>
      <circle cx="30" cy="70" r="2" fill="#c026d3" fill-opacity="0.3"/>
    </pattern>

    <!-- Topographic Contour Pattern for Land Band -->
    <pattern id="topoPattern" width="120" height="80" patternUnits="userSpaceOnUse">
      <path d="M 0 30 Q 30 10, 60 30 T 120 30 M 0 55 Q 30 40, 60 55 T 120 55 M 0 75 Q 40 65, 80 75 T 120 75" fill="none" stroke="#22c55e" stroke-width="0.7" stroke-opacity="0.15"/>
    </pattern>

    <!-- Wave Ripple Pattern for Sea Band -->
    <pattern id="wavePattern" width="100" height="40" patternUnits="userSpaceOnUse">
      <path d="M 0 20 Q 25 10, 50 20 T 100 20 M 0 35 Q 25 25, 50 35 T 100 35" fill="none" stroke="#06b6d4" stroke-width="0.8" stroke-opacity="0.18"/>
    </pattern>

    <!-- Horizontal Environment Gradients -->
    <!-- 1. Space Band -->
    <linearGradient id="bandSpace" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#040714"/>
      <stop offset="50%" stop-color="#0a102b"/>
      <stop offset="100%" stop-color="#050918"/>
    </linearGradient>

    <!-- 2. Air Band -->
    <linearGradient id="bandAir" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#051426"/>
      <stop offset="50%" stop-color="#0b2847"/>
      <stop offset="100%" stop-color="#07182e"/>
    </linearGradient>

    <!-- 3. Land Band -->
    <linearGradient id="bandLand" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#09170a"/>
      <stop offset="50%" stop-color="#122c16"/>
      <stop offset="100%" stop-color="#0a190b"/>
    </linearGradient>

    <!-- 4. Sea Band -->
    <linearGradient id="bandSea" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#041724"/>
      <stop offset="50%" stop-color="#07304d"/>
      <stop offset="100%" stop-color="#041a29"/>
    </linearGradient>

    <!-- 5. METOC / Anti-1812 Band -->
    <linearGradient id="bandMetoc" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1a0f05"/>
      <stop offset="50%" stop-color="#331e0a"/>
      <stop offset="100%" stop-color="#1c1106"/>
    </linearGradient>

    <!-- 6. Cyber / CPS Band -->
    <linearGradient id="bandCyber" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#120521"/>
      <stop offset="50%" stop-color="#240b42"/>
      <stop offset="100%" stop-color="#140624"/>
    </linearGradient>

    <!-- Glow Filters -->
    <filter id="glowCyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowGreen" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowAmber" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowPurple" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <!-- Card Background Fill -->
    <linearGradient id="cardBgMDO" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#0b1120" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="cardBgUWE" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0a1d2e" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#061320" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="cardBgCPS" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#111827" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#090d15" stop-opacity="0.96"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans {{ font-family: 'Inter', 'Segoe UI', -apple-system, Arial, sans-serif; }}
    .font-mono {{ font-family: 'JetBrains Mono', 'Roboto Mono', 'SF Mono', Consolas, monospace; }}
  </style>

  <!-- ========================================================================= -->
  <!-- 1. BASE BACKGROUND &amp; TACTICAL GRID                                        -->
  <!-- ========================================================================= -->
  <rect width="{width}" height="{height}" fill="url(#masterBg)"/>
  <rect width="{width}" height="{height}" fill="url(#tacGrid)"/>

  <!-- ========================================================================= -->
  <!-- 2. MASTER TITLE BANNER                                                    -->
  <!-- ========================================================================= -->
  <g transform="translate(50, 24)">
    <!-- Header Container Box -->
    <rect width="2300" height="110" rx="10" fill="#08101e" fill-opacity="0.92" stroke="#0284c7" stroke-width="1.8"/>
    <!-- Corner Tech Accents -->
    <path d="M 0 25 L 0 0 L 25 0" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <path d="M 2300 25 L 2300 0 L 2275 0" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <path d="M 0 85 L 0 110 L 25 110" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <path d="M 2300 85 L 2300 110 L 2275 110" fill="none" stroke="#38bdf8" stroke-width="3"/>

    <!-- Title Badge -->
    <rect x="25" y="16" width="310" height="24" rx="4" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="35" y="32" fill="#38bdf8" class="font-mono" font-size="11" font-weight="bold" letter-spacing="1.5">SOVEREIGN ARCHITECTURAL MATRIX</text>

    <!-- Main Title -->
    <text x="25" y="70" fill="#ffffff" class="font-sans" font-size="26" font-weight="900" letter-spacing="0.5">
      UNMANNED WARFARE ENGINE (UWE) — MULTI-DOMAIN CYBER-PHYSICAL ARCHITECTURE
    </text>
    
    <!-- Subtitle -->
    <text x="25" y="94" fill="#94a3b8" class="font-sans" font-size="13.5" font-weight="500">
      Strategic Convergence: Multi-Domain Operations (MDO Doctrines) ──► Algorithmic Feasibility (UWE Platform) ──► Cyber-Physical Systems (CPS Execution)
    </text>

    <!-- Metadata Badges on the right -->
    <g transform="translate(1620, 20)">
      <rect x="0" y="0" width="310" height="70" rx="6" fill="#040d1a" stroke="#1e293b" stroke-width="1"/>
      <text x="15" y="24" fill="#64748b" class="font-mono" font-size="10.5" font-weight="bold">FRAMEWORK ARCHITECT:</text>
      <text x="15" y="44" fill="#38bdf8" class="font-sans" font-size="13.5" font-weight="bold">Serhii Khylevych</text>
      <text x="15" y="60" fill="#94a3b8" class="font-mono" font-size="10">Systems Architect &amp; MilTech Strategist</text>
    </g>

    <g transform="translate(1950, 20)">
      <rect x="0" y="0" width="320" height="70" rx="6" fill="#040d1a" stroke="#1e293b" stroke-width="1"/>
      <text x="15" y="24" fill="#64748b" class="font-mono" font-size="10.5" font-weight="bold">GOVERNING STANDARDS:</text>
      <text x="15" y="43" fill="#a855f7" class="font-mono" font-size="11" font-weight="bold">MOSA • STANAG 4754 • IEEE 1451</text>
      <text x="15" y="60" fill="#10b981" class="font-mono" font-size="10.5">NIST SP 1500-201 • FM 3-0 • JP 3-59</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- 3. COLUMN HEADERS                                                         -->
  <!-- ========================================================================= -->
  <!-- Column 1 Header: MDO -->
  <g transform="translate(50, 146)">
    <rect width="710" height="46" rx="6" fill="#0c1929" stroke="#3b82f6" stroke-width="1.8"/>
    <rect x="0" y="0" width="6" height="46" rx="3" fill="#3b82f6"/>
    <text x="20" y="28" fill="#ffffff" class="font-sans" font-size="14.5" font-weight="900" letter-spacing="1">COLUMN 1: MDO (MULTI-DOMAIN OPERATIONS)</text>
    <text x="445" y="28" fill="#60a5fa" class="font-mono" font-size="11" font-weight="bold">[ STRATEGIC DOCTRINE ]</text>
  </g>

  <!-- Column 2 Header: UWE Platform -->
  <g transform="translate(810, 146)">
    <rect width="780" height="46" rx="6" fill="#062338" stroke="#00e5ff" stroke-width="2" filter="url(#glowCyan)"/>
    <rect width="780" height="46" rx="6" fill="#062338" stroke="#00e5ff" stroke-width="2"/>
    <rect x="0" y="0" width="6" height="46" rx="3" fill="#00e5ff"/>
    <text x="20" y="28" fill="#ffffff" class="font-sans" font-size="14.5" font-weight="900" letter-spacing="1">COLUMN 2: UWE CORE PLATFORM (ENGINE)</text>
    <text x="450" y="28" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold">[ CYBER-PHYSICAL KERNEL ]</text>
  </g>

  <!-- Column 3 Header: CPS Execution -->
  <g transform="translate(1640, 146)">
    <rect width="710" height="46" rx="6" fill="#181126" stroke="#c026d3" stroke-width="1.8"/>
    <rect x="0" y="0" width="6" height="46" rx="3" fill="#c026d3"/>
    <text x="20" y="28" fill="#ffffff" class="font-sans" font-size="14.5" font-weight="900" letter-spacing="1">COLUMN 3: CPS (CYBER-PHYSICAL SYSTEMS)</text>
    <text x="440" y="28" fill="#e879f9" class="font-mono" font-size="11" font-weight="bold">[ HARDWARE &amp; ACTUATORS ]</text>
  </g>
"""

    # Helper function to generate an interconnected domain row with environmental background
    def generate_domain_row(y_pos, height_row, domain_name, theme_color, bg_gradient, pattern_id,
                            col1_data, col2_data, col3_data, bg_features_svg=""):
        row_svg = f"""
  <!-- ========================================================================= -->
  <!-- DOMAIN ROW: {domain_name} (y={y_pos}, h={height_row}) -->
  <!-- ========================================================================= -->
  <!-- Full-Width Horizontal Environment Background Band -->
  <g transform="translate(40, {y_pos})">
    <rect width="2320" height="{height_row}" rx="10" fill="{bg_gradient}" stroke="{theme_color}" stroke-width="0.8" stroke-opacity="0.4"/>
    {f'<rect width="2320" height="{height_row}" rx="10" fill="{pattern_id}"/>' if pattern_id else ''}
    {bg_features_svg}
    
    <!-- Environment Watermark Label on Far Right -->
    <text x="2300" y="32" fill="{theme_color}" fill-opacity="0.18" class="font-sans" font-size="32" font-weight="900" text-anchor="end" letter-spacing="2">
      {domain_name.upper().replace('&AMP;', '&amp;')}
    </text>
  </g>

  <!-- COLUMN 1 CARD (MDO) -->
  <g transform="translate(50, {y_pos + 8})">
    <rect width="710" height="{height_row - 16}" rx="8" fill="url(#cardBgMDO)" stroke="{theme_color}" stroke-width="1.5" stroke-opacity="0.75"/>
    <rect x="0" y="0" width="4" height="{height_row - 16}" rx="2" fill="{theme_color}"/>
    
    <!-- Header &amp; Standards Badge -->
    <rect x="18" y="14" width="674" height="28" rx="4" fill="{theme_color}" fill-opacity="0.12" stroke="{theme_color}" stroke-width="1" stroke-opacity="0.4"/>
    <text x="28" y="32" fill="#ffffff" class="font-sans" font-size="13" font-weight="bold">{col1_data['title']}</text>
    <text x="680" y="32" fill="{theme_color}" class="font-mono" font-size="10.5" font-weight="bold" text-anchor="end">{col1_data['doc']}</text>
    
    <!-- Visual Domain Icon + Details -->
    <g transform="translate(22, 54)">
      {col1_data['icon_svg']}
      <g transform="translate(85, 4)">
        {col1_data['body_svg']}
      </g>
    </g>
  </g>

  <!-- INTER-COLUMN BUS 1: MDO -> UWE -->
  <g transform="translate(760, {y_pos + height_row//2})">
    <line x1="5" y1="0" x2="45" y2="0" stroke="{theme_color}" stroke-width="2.5" stroke-dasharray="4 3"/>
    <polygon points="45,0 35,-5 35,5" fill="{theme_color}"/>
    <circle cx="25" cy="0" r="4" fill="{theme_color}"/>
  </g>

  <!-- COLUMN 2 CARD (UWE PLATFORM) -->
  <g transform="translate(810, {y_pos + 8})">
    <rect width="780" height="{height_row - 16}" rx="8" fill="url(#cardBgUWE)" stroke="#00e5ff" stroke-width="1.8" stroke-opacity="0.85"/>
    <rect x="0" y="0" width="5" height="{height_row - 16}" rx="2" fill="#00e5ff"/>
    
    <!-- Header &amp; Namespace Badge -->
    <rect x="18" y="14" width="744" height="28" rx="4" fill="#00e5ff" fill-opacity="0.14" stroke="#00e5ff" stroke-width="1.2" stroke-opacity="0.5"/>
    <text x="28" y="32" fill="#ffffff" class="font-sans" font-size="13.5" font-weight="bold">{col2_data['title']}</text>
    <text x="750" y="32" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold" text-anchor="end">{col2_data['badge']}</text>
    
    <!-- Visual UWE Engine Icon + Operational Specification -->
    <g transform="translate(22, 54)">
      {col2_data['icon_svg']}
      <g transform="translate(95, 4)">
        {col2_data['body_svg']}
      </g>
    </g>
  </g>

  <!-- INTER-COLUMN BUS 2: UWE <-> CPS (Bidirectional Control &amp; Telemetry) -->
  <g transform="translate(1590, {y_pos + height_row//2})">
    <!-- Forward Command Bus (UWE -> CPS) -->
    <line x1="5" y1="-8" x2="45" y2="-8" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="45,-8 35,-12 35,-4" fill="#38bdf8"/>
    
    <!-- Reverse Sensor Telemetry Bus (CPS -> UWE) -->
    <line x1="45" y1="8" x2="5" y2="8" stroke="#10b981" stroke-width="2" stroke-dasharray="3 2"/>
    <polygon points="5,8 15,4 15,12" fill="#10b981"/>
  </g>

  <!-- COLUMN 3 CARD (CPS HARDWARE EXECUTION) -->
  <g transform="translate(1640, {y_pos + 8})">
    <rect width="710" height="{height_row - 16}" rx="8" fill="url(#cardBgCPS)" stroke="{theme_color}" stroke-width="1.5" stroke-opacity="0.75"/>
    <rect x="0" y="0" width="4" height="{height_row - 16}" rx="2" fill="{theme_color}"/>
    
    <!-- Header &amp; Standards Badge -->
    <rect x="18" y="14" width="674" height="28" rx="4" fill="{theme_color}" fill-opacity="0.12" stroke="{theme_color}" stroke-width="1" stroke-opacity="0.4"/>
    <text x="28" y="32" fill="#ffffff" class="font-sans" font-size="13" font-weight="bold">{col3_data['title']}</text>
    <text x="680" y="32" fill="{theme_color}" class="font-mono" font-size="10.5" font-weight="bold" text-anchor="end">{col3_data['standards']}</text>
    
    <!-- Visual CPS Actuator / Driver Icon + Details -->
    <g transform="translate(22, 54)">
      {col3_data['icon_svg']}
      <g transform="translate(90, 4)">
        {col3_data['body_svg']}
      </g>
    </g>
  </g>
"""
        return row_svg

    # =========================================================================
    # ROW 1: SPACE DOMAIN
    # =========================================================================
    bg_space = """
    <!-- Atmospheric limb and stars -->
    <circle cx="120" cy="90" r="1.5" fill="#ffffff" opacity="0.6"/>
    <circle cx="450" cy="40" r="2" fill="#818cf8" opacity="0.8"/>
    <circle cx="980" cy="120" r="1" fill="#ffffff" opacity="0.4"/>
    <circle cx="1450" cy="70" r="1.8" fill="#38bdf8" opacity="0.7"/>
    <circle cx="1920" cy="150" r="2.2" fill="#ffffff" opacity="0.6"/>
    <!-- Orbital Curvature Trajectory Arc -->
    <path d="M 0 170 C 600 40, 1600 30, 2320 140" fill="none" stroke="#6366f1" stroke-width="1.8" stroke-dasharray="8 6" opacity="0.45"/>
    <text x="1200" y="60" fill="#818cf8" class="font-mono" font-size="11" opacity="0.6">LEO / VLEO ORBITAL TRAJECTORY (v = 7.8 km/s)</text>
    """
    
    icon_mdo_space = """
    <circle cx="32" cy="40" r="28" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.8"/>
    <!-- Orbiting Satellite Icon -->
    <ellipse cx="32" cy="40" rx="22" ry="8" fill="none" stroke="#6366f1" stroke-width="1" stroke-dasharray="3 2"/>
    <rect x="25" y="34" width="14" height="12" rx="2" fill="#c7d2fe"/>
    <rect x="8" y="37" width="14" height="6" rx="1" fill="#6366f1"/>
    <rect x="42" y="37" width="14" height="6" rx="1" fill="#6366f1"/>
    """
    
    body_mdo_space = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Strategic Early Warning &amp; Deep Reconnaissance</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Resilient High-Throughput SATCOM Uplinks (SDR/Optical)</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• Space Domain Awareness (SDA) &amp; PNT Constellations</text>
    <text y="74" fill="#818cf8" class="font-mono" font-size="11" font-weight="bold">Doctrinal Focus: JP 3-14 / SDP 1-0 Space Superiority</text>
    """

    icon_uwe_space = """
    <!-- UOV Satellite Node from UOV architecture -->
    <g transform="translate(35, 42)">
      <rect x="-32" y="-10" width="18" height="20" rx="2" fill="#0891b2" stroke="#00e5ff" stroke-width="1"/>
      <rect x="14" y="-10" width="18" height="20" rx="2" fill="#0891b2" stroke="#00e5ff" stroke-width="1"/>
      <circle cx="0" cy="0" r="20" fill="#042f40" stroke="#00e5ff" stroke-width="2"/>
      <text x="0" y="6" fill="#ffffff" class="font-sans" font-size="14" font-weight="900" text-anchor="middle">UOV</text>
    </g>
    """

    body_uwe_space = """
    <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Namespace UOV (Space HLD-1) — Orbital Kinematics</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12">• Orbital Ephemeris Ingestion &amp; VLEO Atmospheric Drag Models</text>
    <text y="54" fill="#cbd5e1" class="font-sans" font-size="12">• Autonomous Station-Keeping, Non-Keplerian Orbit Maneuvers</text>
    <text y="74" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold">Kinematic Contract: Reaction Wheels, Cold-Gas, Micro-Impulse Thrusters</text>
    """

    icon_cps_space = """
    <!-- Reaction Wheel &amp; Cold Gas Thruster Solenoid -->
    <g transform="translate(32, 42)">
      <circle cx="0" cy="0" r="22" fill="#181126" stroke="#c084fc" stroke-width="2"/>
      <circle cx="0" cy="0" r="14" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="4 2"/>
      <rect x="-4" y="-4" width="8" height="8" fill="#e879f9"/>
      <!-- Cold Gas Jets -->
      <path d="M 0 -22 L 0 -28 M 0 22 L 0 28 M -22 0 L -28 0 M 22 0 L 28 0" stroke="#c084fc" stroke-width="1.8"/>
    </g>
    """

    body_cps_space = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Reaction Wheels &amp; Cold-Gas Solenoid Drivers (LLD)</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Spacecraft Bus Decoupling &amp; Closed Thermal Loops</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• Magnetorquer Earth Magnetic Dipole Actuation</text>
    <text y="74" fill="#c084fc" class="font-mono" font-size="11" font-weight="bold">Driver Interface: IKinematicDrive &amp; Spacecraft Power Bus</text>
    """

    row1 = generate_domain_row(
        205, 215, "Space Domain", "#6366f1", "url(#bandSpace)", None,
        {'title': 'MDO SPACE DOMAIN', 'doc': 'JP 3-14 / SDP 1-0', 'icon_svg': icon_mdo_space, 'body_svg': body_mdo_space},
        {'title': 'UWE NAMESPACE UOV (SPACE HLD-1)', 'badge': 'ORBITAL SOVEREIGNTY', 'icon_svg': icon_uwe_space, 'body_svg': body_uwe_space},
        {'title': 'UOV-HAL DOMAIN DRIVERS', 'standards': 'ECSS / CCSDS / IEEE 1451', 'icon_svg': icon_cps_space, 'body_svg': body_cps_space},
        bg_space
    )

    # =========================================================================
    # ROW 2: AIR DOMAIN
    # =========================================================================
    bg_air = """
    <!-- Streamlines and Air Pressure Vectors -->
    <path d="M 0 110 Q 500 70, 1100 110 T 2320 90" fill="none" stroke="#0ea5e9" stroke-width="1" stroke-opacity="0.3"/>
    <path d="M 0 145 Q 600 120, 1400 150 T 2320 130" fill="none" stroke="#0ea5e9" stroke-width="1" stroke-opacity="0.2"/>
    <text x="1200" y="55" fill="#38bdf8" class="font-mono" font-size="11" opacity="0.6">FLIGHT MEDIA BOUNDARY: FL600 (HALE) ──► FL100 (TACTICAL COPTER DIVE)</text>
    """

    icon_mdo_air = """
    <!-- Fixed Wing + Air Interdiction Icon -->
    <g transform="translate(32, 42)">
      <polygon points="0,-22 24,18 -24,18" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
      <line x1="0" y1="-22" x2="0" y2="18" stroke="#ffffff" stroke-width="1.5"/>
      <line x1="-16" y1="10" x2="16" y2="10" stroke="#bae6fd" stroke-width="1.5"/>
    </g>
    """

    body_mdo_air = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Deep Fires Synchronization &amp; Offensive Counter-Air</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• High-Altitude Theater Persistent ISR (HALE / MALE)</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• Collaborative Combat Aircraft (CCA) Swarm Penetration</text>
    <text y="74" fill="#38bdf8" class="font-mono" font-size="11" font-weight="bold">Doctrinal Focus: FM 3-0 / JP 3-30 Joint Air Operations</text>
    """

    icon_uwe_air = """
    <!-- Combined UAV (Wing) and UCV (Copter) from UOV architecture -->
    <g transform="translate(35, 42)">
      <!-- Copter Body &amp; Rotors -->
      <rect x="-16" y="-16" width="32" height="32" rx="3" fill="#08382c" stroke="#10b981" stroke-width="2"/>
      <circle cx="-16" cy="-16" r="4.5" fill="#10b981" stroke="#fff" stroke-width="1"/>
      <circle cx="16" cy="-16" r="4.5" fill="#10b981" stroke="#fff" stroke-width="1"/>
      <circle cx="16" cy="16" r="4.5" fill="#10b981" stroke="#fff" stroke-width="1"/>
      <circle cx="-16" cy="16" r="4.5" fill="#10b981" stroke="#fff" stroke-width="1"/>
      <text x="0" y="5" fill="#ffffff" class="font-mono" font-size="10" font-weight="bold" text-anchor="middle">UCV</text>
    </g>
    """

    body_uwe_air = """
    <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Namespaces UAV &amp; UCV (Air HLD-1) — Flight Physics</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12">• Aerodynamic Glide Polars &amp; Disc-Loading Dynamic Limits</text>
    <text y="54" fill="#cbd5e1" class="font-sans" font-size="12">• Tier C-4 Airfield Infrastructure (Paved Runways, Hangars, Arrester)</text>
    <text y="74" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold">Container Model: Mothercraft Carrier Decoupling &amp; Swarm Release</text>
    """

    icon_cps_air = """
    <!-- FOC ESC / Inverter &amp; Brushless Motor Icon -->
    <g transform="translate(32, 42)">
      <circle cx="0" cy="0" r="22" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
      <!-- Rotor blades -->
      <path d="M -16 -16 L 16 16 M -16 16 L 16 -16" stroke="#0ea5e9" stroke-width="3"/>
      <circle cx="0" cy="0" r="7" fill="#38bdf8"/>
      <!-- Terminal Override Lightning Badge -->
      <path d="M 14 -18 L 6 -6 L 14 -4 L 8 16" fill="none" stroke="#fbbf24" stroke-width="2"/>
    </g>
    """

    body_cps_air = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• FOC ESC Inverter Drivers &amp; Dynamic Propeller Active Braking</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Terminal 15G Limit Overrides on Terminal Kinetic Impact</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• Multi-Rotor Torque Mixer &amp; Aerodynamic Elevon Servos</text>
    <text y="74" fill="#38bdf8" class="font-mono" font-size="11" font-weight="bold">Driver Interface: IFocEscController &amp; IActuatorAero</text>
    """

    row2 = generate_domain_row(
        428, 215, "Air Domain", "#0ea5e9", "url(#bandAir)", None,
        {'title': 'MDO AIR DOMAIN', 'doc': 'FM 3-0 / JP 3-30', 'icon_svg': icon_mdo_air, 'body_svg': body_mdo_air},
        {'title': 'UWE NAMESPACES UAV &amp; UCV (AIR HLD-1)', 'badge': 'AERO &amp; DISC DYNAMICS', 'icon_svg': icon_uwe_air, 'body_svg': body_uwe_air},
        {'title': 'UAV/UCV-HAL DOMAIN DRIVERS', 'standards': 'STANAG 4586 / MOSA / ARINC 664', 'icon_svg': icon_cps_air, 'body_svg': body_cps_air},
        bg_air
    )

    # =========================================================================
    # ROW 3: LAND DOMAIN
    # =========================================================================
    bg_land = """
    <!-- Topographic contour lines and trench baseline -->
    <path d="M 0 160 L 500 160 L 530 185 L 620 185 L 650 160 L 2320 160" fill="none" stroke="#22c55e" stroke-width="1.8" stroke-opacity="0.35"/>
    <text x="580" y="178" fill="#4ade80" class="font-mono" font-size="10" opacity="0.7">TACTICAL TRENCH PROFILE</text>
    <text x="1200" y="55" fill="#4ade80" class="font-mono" font-size="11" opacity="0.6">TERRESTRIAL GROUND INTERFACE: CLAY, MUD, CONCRETE &amp; URBAN RUBBLE</text>
    """

    icon_mdo_land = """
    <!-- Armored Tracked Profile Icon -->
    <g transform="translate(32, 42)">
      <rect x="-24" y="-12" width="48" height="20" rx="3" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
      <rect x="-20" y="8" width="40" height="8" rx="4" fill="#22c55e"/>
      <circle cx="-12" cy="12" r="3" fill="#14532d"/>
      <circle cx="0" cy="12" r="3" fill="#14532d"/>
      <circle cx="12" cy="12" r="3" fill="#14532d"/>
    </g>
    """

    body_mdo_land = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Combined Arms Close Maneuver &amp; Breach Operations</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Dispersed Force Protection &amp; Autonomous Logistics Lines</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• High-Attrition Forward Trench Penetration &amp; Static Defense</text>
    <text y="74" fill="#22c55e" class="font-mono" font-size="11" font-weight="bold">Doctrinal Focus: FM 3-0 / ATP 3-90 Maneuver &amp; Assault</text>
    """

    icon_uwe_land = """
    <!-- UGV Icon from UOV architecture -->
    <g transform="translate(35, 42)">
      <rect x="-26" y="-16" width="52" height="32" rx="4" fill="#062e24" stroke="#10b981" stroke-width="2.5"/>
      <rect x="-20" y="10" width="40" height="6" rx="2" fill="#047857"/>
      <circle cx="-12" cy="-4" r="4" fill="#10b981"/>
      <text x="6" y="2" fill="#ffffff" class="font-mono" font-size="12" font-weight="bold">UGV</text>
    </g>
    """

    body_uwe_land = """
    <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Namespace UGV (Ground HLD-1) — Terramechanics</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12">• Bekker-Wong Soil Sinking &amp; Shear Failure Pre-Calculation</text>
    <text y="54" fill="#cbd5e1" class="font-sans" font-size="12">• Ground Pressure (kg/cm²) Validation for Spring Rasputitsa</text>
    <text y="74" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold">Tabor Defense Service (LLD-3): Cossack-Style Autonomous Perimeter</text>
    """

    icon_cps_land = """
    <!-- Differential Skid-Steer Drive &amp; Track Sprocket -->
    <g transform="translate(32, 42)">
      <circle cx="-10" cy="0" r="14" fill="#052e16" stroke="#22c55e" stroke-width="1.8"/>
      <circle cx="10" cy="0" r="14" fill="#052e16" stroke="#22c55e" stroke-width="1.8"/>
      <path d="M -10 -14 L 10 -14 M -10 14 L 10 14" stroke="#4ade80" stroke-width="2"/>
      <rect x="-4" y="-8" width="8" height="16" fill="#22c55e"/>
    </g>
    """

    body_cps_land = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Differential Skid-Steer Torque Control &amp; Dynamic Slip Sensing</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Bidirectional V2V Charging BMS for Forward Infantry Squads</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• High-Torque Planetary Gearboxes &amp; Obstacle Climbing Servos</text>
    <text y="74" fill="#22c55e" class="font-mono" font-size="11" font-weight="bold">Driver Interface: IKinematicDrive &amp; IPowerEnergy (V2V BMS)</text>
    """

    row3 = generate_domain_row(
        651, 215, "Land Domain", "#22c55e", "url(#bandLand)", "url(#topoPattern)",
        {'title': 'MDO LAND DOMAIN', 'doc': 'FM 3-0 / ATP 3-90', 'icon_svg': icon_mdo_land, 'body_svg': body_mdo_land},
        {'title': 'UWE NAMESPACE UGV (GROUND HLD-1)', 'badge': 'TERRAMECHANICS &amp; MOBILITY', 'icon_svg': icon_uwe_land, 'body_svg': body_uwe_land},
        {'title': 'UGV-HAL DOMAIN DRIVERS', 'standards': 'STANAG 4754 (NGVA) / MIL-STD-810H', 'icon_svg': icon_cps_land, 'body_svg': body_cps_land},
        bg_land
    )

    # =========================================================================
    # ROW 4: MARITIME DOMAIN
    # =========================================================================
    bg_sea = """
    <!-- Hydrodynamic surface wave and thermocline depth boundary -->
    <path d="M 0 85 Q 200 65, 400 85 T 800 85 T 1200 85 T 1600 85 T 2000 85 T 2320 85" fill="none" stroke="#06b6d4" stroke-width="2" stroke-opacity="0.45"/>
    <line x1="0" y1="140" x2="2320" y2="140" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="6 4" stroke-opacity="0.35"/>
    <text x="1200" y="55" fill="#38bdf8" class="font-mono" font-size="11" opacity="0.6">MARITIME LAYER: SURFACE LITTORAL ──► THERMOCLINE BARRIER ──► BENTHIC ABYSS</text>
    <text x="2100" y="132" fill="#0284c7" class="font-mono" font-size="9.5" opacity="0.7">SVP THERMOCLINE BOUNDARY</text>
    """

    icon_mdo_sea = """
    <!-- Naval Surface Hull + Subsea Torpedo Shape -->
    <g transform="translate(32, 42)">
      <!-- Surface Boat -->
      <polygon points="-22,-4 22,-4 14,8 -14,8" fill="#0e7490" stroke="#06b6d4" stroke-width="1.8"/>
      <rect x="-6" y="-12" width="12" height="8" rx="1" fill="#06b6d4"/>
      <!-- Subsea Submarine -->
      <ellipse cx="0" cy="18" rx="18" ry="6" fill="#155e75" stroke="#38bdf8" stroke-width="1.5"/>
    </g>
    """

    body_mdo_sea = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Anti-Surface Warfare (ASuW) &amp; Littoral Choke-Point Denial</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Anti-Submarine Warfare (ASW) Multi-Static Sonar Shields</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• Mine Countermeasures (MCM) &amp; Seabed Infrastructure Guard</text>
    <text y="74" fill="#06b6d4" class="font-mono" font-size="11" font-weight="bold">Doctrinal Focus: JP 3-32 / NWP 3-0 Maritime Joint Operations</text>
    """

    icon_uwe_sea = """
    <!-- USV + UUV from UOV architecture -->
    <g transform="translate(35, 42)">
      <!-- USV Trapezoid -->
      <polygon points="-24,-12 24,-12 16,4 -16,4" fill="#073b5c" stroke="#00e5ff" stroke-width="2"/>
      <rect x="-6" y="-18" width="12" height="6" fill="#00e5ff"/>
      <!-- UUV Oval below -->
      <ellipse cx="0" cy="16" rx="20" ry="8" fill="#082f49" stroke="#38bdf8" stroke-width="1.8"/>
      <text x="0" y="-2" fill="#ffffff" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">USV/UUV</text>
    </g>
    """

    body_uwe_sea = """
    <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Namespaces USV &amp; UUV (Maritime HLD-1) — Hydrodynamics</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12">• Hydrodynamic Wave Slamming Spectra (15G Gz Limits at Sea State 6)</text>
    <text y="54" fill="#cbd5e1" class="font-sans" font-size="12">• Biomimetic Ribbon-Fin Propulsion for Surf-Zone Minefield Breaching</text>
    <text y="74" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold">Variable Ballast Trim &amp; Acoustic Sound Velocity Profile (SVP) Routing</text>
    """

    icon_cps_sea = """
    <!-- Steerable Waterjet &amp; Ribbon-Fin Servo -->
    <g transform="translate(32, 42)">
      <rect x="-18" y="-12" width="36" height="24" rx="3" fill="#083344" stroke="#06b6d4" stroke-width="1.8"/>
      <!-- Waterjet Nozzle -->
      <path d="M 18 -6 L 26 -10 L 26 10 L 18 6 Z" fill="#06b6d4"/>
      <!-- Water Thrust Stream -->
      <path d="M 28 -8 Q 36 0, 28 8" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <!-- Acoustic Modem Transducer -->
      <circle cx="-6" cy="0" r="5" fill="#38bdf8"/>
    </g>
    """

    body_cps_sea = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Vector Thrusters, Waterjet Servos &amp; Ribbon-Fin Flex Drivers</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• High-Pressure Variable Ballast Subsea Pump Controllers</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• Deep-Water Acoustic Modems &amp; Hydrodynamic Pressure Sensors</text>
    <text y="74" fill="#06b6d4" class="font-mono" font-size="11" font-weight="bold">Driver Interface: IHydroDrive &amp; IAcousticTransceiver</text>
    """

    row4 = generate_domain_row(
        874, 215, "Maritime Domain", "#06b6d4", "url(#bandSea)", "url(#wavePattern)",
        {'title': 'MDO MARITIME DOMAIN', 'doc': 'JP 3-32 / NWP 3-0', 'icon_svg': icon_mdo_sea, 'body_svg': body_mdo_sea},
        {'title': 'UWE NAMESPACES USV &amp; UUV (MARITIME HLD-1)', 'badge': 'HYDRODYNAMICS &amp; BUOYANCY', 'icon_svg': icon_uwe_sea, 'body_svg': body_uwe_sea},
        {'title': 'USV/UUV-HAL DOMAIN DRIVERS', 'standards': 'STANAG 4754 / MIL-STD-810H / IEEE 1451', 'icon_svg': icon_cps_sea, 'body_svg': body_cps_sea},
        bg_sea
    )

    # =========================================================================
    # ROW 5: METOC &amp; OPERATIONAL ENVIRONMENT (THE "ANTI-1812" REALITY)
    # =========================================================================
    bg_metoc = """
    <!-- Soil shear failure envelope and weather front lines -->
    <path d="M 0 150 Q 300 120, 700 155 T 1400 140 T 2320 160" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="5 3" opacity="0.4"/>
    <text x="1200" y="55" fill="#fbbf24" class="font-mono" font-size="11" opacity="0.7">PHYSICAL REALITY (THE 'ANTI-1812' ENGINE): TERRAMECHANICS • OCEANOGRAPHY • MICRO-MET • RF FLOOR</text>
    """

    icon_mdo_metoc = """
    <!-- Weather Front, Soil Strata &amp; Barometer -->
    <g transform="translate(32, 42)">
      <circle cx="0" cy="0" r="22" fill="#451a03" stroke="#f59e0b" stroke-width="2"/>
      <!-- Wind / Weather Swirl -->
      <path d="M -12 -6 Q 0 -14, 12 -6 T 0 10" fill="none" stroke="#fbbf24" stroke-width="2"/>
      <circle cx="0" cy="0" r="3" fill="#f59e0b"/>
    </g>
    """

    body_mdo_metoc = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="bold">• JP 3-59: Meteorological &amp; Oceanographic Operations (METOC)</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="bold">• JP 2-01.3: Joint Intelligence Preparation of the Env. (JIPOE)</text>
    <text y="54" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="bold">• ATP 3-34.80: Military Terramechanics &amp; Trafficability Corridors</text>
    <text y="74" fill="#f59e0b" class="font-mono" font-size="11" font-weight="bold">The '1812' Trap: Doctrine without Physics = 100% Fleet Attrition</text>
    """

    icon_uwe_metoc = """
    <!-- Dynamic 4D Tensor / World Model Icon -->
    <g transform="translate(35, 42)">
      <rect x="-24" y="-20" width="48" height="40" rx="4" fill="#241405" stroke="#f59e0b" stroke-width="2"/>
      <!-- Tensor Grid Coordinate Lines -->
      <line x1="-24" y1="0" x2="24" y2="0" stroke="#fbbf24" stroke-width="1.2"/>
      <line x1="0" y1="-20" x2="0" y2="20" stroke="#fbbf24" stroke-width="1.2"/>
      <circle cx="0" cy="0" r="5" fill="#00e5ff"/>
      <text x="0" y="27" fill="#f59e0b" class="font-mono" font-size="8" font-weight="bold" text-anchor="middle">EAL 4D</text>
    </g>
    """

    body_uwe_metoc = """
    <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">EAL: Environmental Abstraction Layer (HLD-0) — CPS World Model</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12">• Real-time Ingestion: Soil Shear (c, phi), Wave Force (Gz), Icing, Jamming (J/S)</text>
    <text y="54" fill="#cbd5e1" class="font-sans" font-size="12">• Deterministic Feasibility Engine (HLD-3): Phi = F(K, L, E, C, T)</text>
    <text y="74" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold">Algorithmic Barrier: Blocks Kinematically Impossible Missions Pre-Flight</text>
    """

    icon_cps_metoc = """
    <!-- Physical Sensing Probes: GPR, Penetrometer &amp; SDR Antenna -->
    <g transform="translate(32, 42)">
      <circle cx="0" cy="0" r="22" fill="#291404" stroke="#f59e0b" stroke-width="1.8"/>
      <!-- Penetrometer Cone Pointing Down -->
      <polygon points="0,18 -8,6 8,6" fill="#fbbf24"/>
      <line x1="0" y1="-14" x2="0" y2="6" stroke="#fbbf24" stroke-width="2.5"/>
      <!-- Emitted Radar / Sensing Waves -->
      <path d="M -16 -4 Q 0 -12, 16 -4" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
      <path d="M -20 -10 Q 0 -18, 20 -10" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
    </g>
    """

    body_cps_metoc = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Ground-Penetrating Radar (GPR) &amp; Cone Soil Penetrometers</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• CTD Ocean Buoyancy Profilers &amp; Micro-LIDAR Wind Shear Scanners</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• Frontline SDR Jamming Power Spectral Density (PSD) Telemetry</text>
    <text y="74" fill="#f59e0b" class="font-mono" font-size="11" font-weight="bold">Sensory Architecture: IEEE 1451 Smart Transducer Standard / NGVA</text>
    """

    row5 = generate_domain_row(
        1097, 225, "METOC &amp; Environment", "#f59e0b", "url(#bandMetoc)", None,
        {'title': 'METOC &amp; OPERATIONAL ENVIRONMENT', 'doc': 'JP 3-59 / JP 2-01.3 / ATP 3-34.80', 'icon_svg': icon_mdo_metoc, 'body_svg': body_mdo_metoc},
        {'title': 'EAL: CYBER-PHYSICAL WORLD MODEL (HLD-0)', 'badge': 'DYNAMIC 4D TENSOR', 'icon_svg': icon_uwe_metoc, 'body_svg': body_uwe_metoc},
        {'title': 'EAL PHYSICAL SENSORY PROBES (LLD-E0)', 'standards': 'IEEE 1451 / STANAG 4754 / MIL-STD-810H', 'icon_svg': icon_cps_metoc, 'body_svg': body_cps_metoc},
        bg_metoc
    )

    # =========================================================================
    # ROW 6: CYBERSPACE &amp; CPS EXECUTION
    # =========================================================================
    bg_cyber = """
    <!-- Binary data nodes, circuit lines and crypto mesh -->
    <path d="M 0 170 L 400 170 L 460 130 L 1200 130 L 1260 170 L 2320 170" fill="none" stroke="#c026d3" stroke-width="1.5" stroke-opacity="0.4"/>
    <text x="1200" y="55" fill="#e879f9" class="font-mono" font-size="11" opacity="0.7">CYBER-PHYSICAL SYNAPSE: SECURE DATA FABRIC ──► 48-BIT MCU REGISTER ──► ACTUATOR DYNAMICS</text>
    """

    icon_mdo_cyber = """
    <!-- Shield / Zero Trust Cyber Lock -->
    <g transform="translate(32, 42)">
      <path d="M 0 -20 L 18 -10 L 18 10 C 18 20, 0 26, 0 26 C 0 26, -18 20, -18 10 L -18 -10 Z" fill="#3b0764" stroke="#c026d3" stroke-width="2"/>
      <circle cx="0" cy="0" r="5" fill="#e879f9"/>
      <line x1="0" y1="5" x2="0" y2="12" stroke="#e879f9" stroke-width="2"/>
    </g>
    """

    body_mdo_cyber = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Offensive (OCO) &amp; Defensive (DCO) Cyberspace Operations</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• Electromagnetic Warfare (EW) &amp; Spectrum Dominance (EMSO)</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• High-Assurance Zero Trust C2 Architecture (NIST SP 800-160)</text>
    <text y="74" fill="#c026d3" class="font-mono" font-size="11" font-weight="bold">Doctrinal Focus: JP 3-12 / AJP-3.20 Allied Cyber Doctrine</text>
    """

    icon_uwe_cyber = """
    <!-- 48-bit Dual Read Token Matrix Icon -->
    <g transform="translate(35, 42)">
      <rect x="-26" y="-18" width="52" height="36" rx="4" fill="#1e0836" stroke="#c026d3" stroke-width="2"/>
      <text x="0" y="-3" fill="#00e5ff" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">[XX]-[YY]</text>
      <text x="0" y="10" fill="#e879f9" class="font-mono" font-size="9" font-weight="bold" text-anchor="middle">-[ZZ]</text>
    </g>
    """

    body_uwe_cyber = """
    <text y="14" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">Resilient Transport Mesh &amp; Feasibility Engine (HLD-2 / 3)</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12">• Cognitive Dual-Read Token: [XX]-[YY]-[ZZ] (Human Readable / Edge-AI Parsed)</text>
    <text y="54" fill="#cbd5e1" class="font-sans" font-size="12">• Self-Healing Multi-Medium Mesh (Laser, COFDM, Acoustic, Fiber)</text>
    <text y="74" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold">Kill Web Latency: Sub-10ms Targeting Handoff without Staff Friction</text>
    """

    icon_cps_cyber = """
    <!-- CPS Microcontroller Chip with Pins &amp; Bus Lines -->
    <g transform="translate(32, 42)">
      <rect x="-16" y="-16" width="32" height="32" rx="3" fill="#2e1065" stroke="#e879f9" stroke-width="2"/>
      <!-- Silicon Core -->
      <rect x="-8" y="-8" width="16" height="16" rx="1" fill="#c026d3"/>
      <!-- Outer Metal IC Pins -->
      <path d="M -16 -10 L -22 -10 M -16 0 L -22 0 M -16 10 L -22 10" stroke="#e879f9" stroke-width="1.8"/>
      <path d="M 16 -10 L 22 -10 M 16 0 L 22 0 M 16 10 L 22 10" stroke="#e879f9" stroke-width="1.8"/>
      <path d="M -10 -16 L -10 -22 M 0 -16 L 0 -22 M 10 -16 L 10 -22" stroke="#e879f9" stroke-width="1.8"/>
      <path d="M -10 16 L -10 22 M 0 16 L 0 22 M 10 16 L 10 22" stroke="#e879f9" stroke-width="1.8"/>
    </g>
    """

    body_cps_cyber = """
    <text y="14" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• IPowerEnergy: Battery Management &amp; Deep Sleep 'Zhdun' (&lt;5mA)</text>
    <text y="34" fill="#cbd5e1" class="font-sans" font-size="12" font-weight="600">• IPayloadAttachment: STANAG 4754 Pinout, OWM Crypto-Fuze Arming</text>
    <text y="54" fill="#94a3b8" class="font-sans" font-size="11.5">• ITokenRegistry: 48-bit MCU Word Register, Single-Cycle Bitmask Filter</text>
    <text y="74" fill="#e879f9" class="font-mono" font-size="11" font-weight="bold">Framework Standard: NIST SP 1500-201 Cyber-Physical Systems (CPS)</text>
    """

    row6 = generate_domain_row(
        1330, 225, "Cyberspace &amp; CPS", "#c026d3", "url(#bandCyber)", "url(#circuitPattern)",
        {'title': 'MDO CYBERSPACE &amp; EW', 'doc': 'JP 3-12 / NIST SP 800-160', 'icon_svg': icon_mdo_cyber, 'body_svg': body_mdo_cyber},
        {'title': 'UWE RESILIENT MESH &amp; FEASIBILITY (HLD-2/3)', 'badge': 'MICROSECOND KILL WEB', 'icon_svg': icon_uwe_cyber, 'body_svg': body_uwe_cyber},
        {'title': 'CPS UNIVERSAL CONTRACTS &amp; REGISTERS', 'standards': 'NIST SP 1500-201 / STANAG 4754', 'icon_svg': icon_cps_cyber, 'body_svg': body_cps_cyber},
        bg_cyber
    )

    # =========================================================================
    # MASTER FOOTER BAR: THE FOUR INVARIANT LAWS &amp; ANTI-1812 PRINCIPLE
    # =========================================================================
    footer = """
  <!-- Master Footer Summary Bar -->
  <g transform="translate(50, 1572)">
    <rect width="2300" height="100" rx="8" fill="#060d1a" stroke="#1e293b" stroke-width="1.5"/>
    
    <!-- Left Accent Tag -->
    <rect x="0" y="0" width="8" height="100" rx="4" fill="#00e5ff"/>
    
    <!-- Title -->
    <text x="25" y="28" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold" letter-spacing="1.5">
      THE FOUR INVARIANT LAWS OF THE UNMANNED WARFARE ENGINE (UWE)
    </text>
    
    <!-- 4 Law Columns -->
    <g transform="translate(25, 42)">
      <!-- Law 1 -->
      <g transform="translate(0, 0)">
        <rect width="530" height="46" rx="4" fill="#0a1728" stroke="#0284c7" stroke-width="1"/>
        <text x="12" y="18" fill="#38bdf8" class="font-sans" font-size="11.5" font-weight="bold">LAW I: KINEMATIC PRIMACY</text>
        <text x="12" y="34" fill="#94a3b8" class="font-sans" font-size="10.5">Contact physics dictates mission feasibility, never the reverse.</text>
      </g>
      
      <!-- Law 2 -->
      <g transform="translate(550, 0)">
        <rect width="530" height="46" rx="4" fill="#0a1728" stroke="#10b981" stroke-width="1"/>
        <text x="12" y="18" fill="#34d399" class="font-sans" font-size="11.5" font-weight="bold">LAW II: HIERARCHICAL CONTAINERIZATION</text>
        <text x="12" y="34" fill="#94a3b8" class="font-sans" font-size="10.5">Scales friction from C0 man-pack to C4 strategic airfields &amp; ports.</text>
      </g>
      
      <!-- Law 3 -->
      <g transform="translate(1100, 0)">
        <rect width="530" height="46" rx="4" fill="#0a1728" stroke="#f59e0b" stroke-width="1"/>
        <text x="12" y="18" fill="#fbbf24" class="font-sans" font-size="11.5" font-weight="bold">LAW III: HARDWARE ABSTRACTION &amp; OWM</text>
        <text x="12" y="34" fill="#94a3b8" class="font-sans" font-size="10.5">Decoupled robotic chassis from payloads &amp; sacrificial modes.</text>
      </g>
      
      <!-- Law 4 -->
      <g transform="translate(1650, 0)">
        <rect width="600" height="46" rx="4" fill="#0a1728" stroke="#c026d3" stroke-width="1"/>
        <text x="12" y="18" fill="#e879f9" class="font-sans" font-size="11.5" font-weight="bold">LAW IV: COGNITIVE SYNCHRONIZATION</text>
        <text x="12" y="34" fill="#94a3b8" class="font-sans" font-size="10.5">[XX]-[YY]-[ZZ] tokens: human readable, microsecond edge-AI parsed.</text>
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
    
    # 1. Convert SVG to PDF using LibreOffice
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

    # 2. Convert PDF to high-resolution PNG (150 DPI)
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

    # 3. Convert PDF to high-resolution JPEG (150 DPI)
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
