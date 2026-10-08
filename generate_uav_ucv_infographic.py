#!/usr/bin/env python3
"""
Generates the Defense One Infographic for UAV/UCV Air Domain Architecture.
Aspect ratio: 1.91:1 (2400 x 1260 px).
"""

import os
import subprocess

def create_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1260" width="2400" height="1260">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05101e"/>
      <stop offset="40%" stop-color="#0a192f"/>
      <stop offset="80%" stop-color="#071426"/>
      <stop offset="100%" stop-color="#020813"/>
    </linearGradient>

    <!-- Card Backgrounds -->
    <linearGradient id="cardGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f2744" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#08182b" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="cardGrad2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#142c3d" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#091b26" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="cardGrad3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2a1b14" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#180e0a" stop-opacity="0.95"/>
    </linearGradient>

    <!-- Glow & Shadow Filters -->
    <filter id="glowCyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowGold" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glowAmber" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- 1. Background -->
  <rect width="2400" height="1260" fill="url(#bgGrad)"/>

  <!-- Subtle Tactical Grid Lines -->
  <g stroke="#1e3a5f" stroke-width="1" opacity="0.3">
    <line x1="80" y1="200" x2="2320" y2="200"/>
    <line x1="80" y1="480" x2="2320" y2="480"/>
    <line x1="80" y1="780" x2="2320" y2="780"/>
    <line x1="80" y1="1080" x2="2320" y2="1080"/>
    <line x1="800" y1="200" x2="800" y2="1080"/>
    <line x1="1600" y1="200" x2="1600" y2="1080"/>
  </g>

  <!-- 2. Header Block -->
  <g id="header">
    <rect x="80" y="45" width="460" height="32" rx="6" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="310" y="66" fill="#38bdf8" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="bold" letter-spacing="2.5" text-anchor="middle">UNMANNED WARFARE ENGINE (UWE) • AIR DOCTRINE</text>

    <text x="80" y="125" fill="#f8fafc" font-family="'Segoe UI', Arial, sans-serif" font-size="36" font-weight="900" letter-spacing="1">STANDOFF C4ISR (UAV) TO ATTRITABLE KINETIC SWARM (UCV)</text>
    <text x="80" y="165" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="19" font-weight="400">Software-Defined Functional Segregation &amp; The Universal Six-Character Aerial Syntax</text>
  </g>

  <!-- 3. Top Banner: The Doctrinal Shift -->
  <g id="doctrinal-shift" transform="translate(80, 205)">
    <rect width="2240" height="85" rx="10" fill="#0c233c" stroke="#1e4976" stroke-width="2"/>
    <text x="40" y="38" fill="#38bdf8" font-family="'Segoe UI', Arial, sans-serif" font-size="17" font-weight="bold" letter-spacing="1.5">DOCTRINAL PIVOT:</text>
    <text x="210" y="38" fill="#e2e8f0" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="500">Why Legacy NATO STANAG 4670 (HALE/MALE/Tactical) and Consumer "FPV" Slang Paralyze Defense Procurement</text>
    <text x="40" y="66" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Static airframe weight and camera-goggle links ignore physical combat invariants: terminal kinematics, rotor disk loading, ECCM frequency agility, and Edge-AI Kill Web handoff.</text>
  </g>

  <!-- 4. Column 1: Standoff C4ISR Mesh (UAV Tier) -->
  <g id="col-uav" transform="translate(80, 315)">
    <rect width="720" height="660" rx="12" fill="url(#cardGrad1)" stroke="#0284c7" stroke-width="2"/>
    
    <!-- Tier Header -->
    <rect x="25" y="25" width="220" height="28" rx="4" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/>
    <text x="135" y="44" fill="#38bdf8" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="bold" letter-spacing="1.5" text-anchor="middle">TIER 1 • STANDOFF C4ISR</text>
    
    <text x="25" y="85" fill="#f8fafc" font-family="'Segoe UI', Arial, sans-serif" font-size="24" font-weight="bold">UAV: Winged High-Endurance</text>
    <text x="25" y="112" fill="#64748b" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-style="italic">Operating Altitude: 8,000 – 12,000 m (Outside Short-Range GBAD)</text>

    <!-- Syntax Badge -->
    <rect x="25" y="135" width="670" height="65" rx="8" fill="#041426" stroke="#0ea5e9" stroke-width="1.5"/>
    <text x="45" y="165" fill="#38bdf8" font-family="'Consolas', monospace" font-size="20" font-weight="bold" letter-spacing="2">UAV Profile: [ AL - PE - HR ]</text>
    <text x="45" y="188" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="13">Atmosphere • Runway Launch • Piston ICE • High-Loiter • Autonomous Patrol • Directional COFDM</text>

    <!-- Operational Core -->
    <g transform="translate(25, 225)">
      <rect width="670" height="400" rx="8" fill="#06182c" stroke="#173559" stroke-width="1"/>
      
      <text x="25" y="35" fill="#e2e8f0" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="bold">Core Operational Invariants:</text>
      
      <circle cx="35" cy="70" r="5" fill="#38bdf8"/>
      <text x="50" y="75" fill="#cbd5e1" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Standoff Survivability:</text>
      <text x="215" y="75" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Wings stay 40–80 km behind FLOT, using SAR radar</text>
      <text x="50" y="95" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">&amp; long-wave optronics to avoid S-300 / Buk air defense envelopes.</text>

      <circle cx="35" cy="130" r="5" fill="#38bdf8"/>
      <text x="50" y="135" fill="#cbd5e1" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Airborne C2 Router:</text>
      <text x="195" y="135" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Acts as an aerial gateway node, cross-linking laser</text>
      <text x="50" y="155" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">telemetry from LEO satellites (UOV) down to frontline mesh networks.</text>

      <circle cx="35" cy="190" r="5" fill="#38bdf8"/>
      <text x="50" y="195" fill="#cbd5e1" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Airborne Edge-AI Processor:</text>
      <text x="250" y="195" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Runs onboard neural networks to compute</text>
      <text x="50" y="215" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">firing solutions, generating microsecond vector handoffs to strike copters.</text>

      <line x1="25" y1="245" x2="645" y2="245" stroke="#1e3a5f" stroke-width="1"/>

      <text x="25" y="275" fill="#f59e0b" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Operational Benchmarks:</text>
      <text x="25" y="300" fill="#e2e8f0" font-family="'Segoe UI', Arial, sans-serif" font-size="13.5">• MQ-9 Reaper / Bayraktar TB2 (Classics, high-risk over contested frontline)</text>
      <text x="25" y="325" fill="#e2e8f0" font-family="'Segoe UI', Arial, sans-serif" font-size="13.5">• Collaborative Combat Aircraft (CCA) / Loyal Wingman (Next-Gen Penetrator)</text>
      <text x="25" y="350" fill="#e2e8f0" font-family="'Segoe UI', Arial, sans-serif" font-size="13.5">• Long-range Loitering Strike: [ AL - CO - MO ] (Shahed-136 / Switchblade 600)</text>
    </g>
  </g>

  <!-- 5. Column 2: Tactical Kinetic Swarm (UCV Tier) -->
  <g id="col-ucv" transform="translate(840, 315)">
    <rect width="720" height="660" rx="12" fill="url(#cardGrad3)" stroke="#f97316" stroke-width="2"/>
    
    <!-- Tier Header -->
    <rect x="25" y="25" width="260" height="28" rx="4" fill="#f97316" fill-opacity="0.25" stroke="#fb923c" stroke-width="1"/>
    <text x="155" y="44" fill="#fb923c" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="bold" letter-spacing="1.5" text-anchor="middle">TIER 2 • TACTICAL KINETIC SWARM</text>
    
    <text x="25" y="85" fill="#f8fafc" font-family="'Segoe UI', Arial, sans-serif" font-size="24" font-weight="bold">UCV: Unmanned Copter Vehicles</text>
    <text x="25" y="112" fill="#fdba74" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-style="italic">Operating Altitude: 0 – 500 m (Trench Line, Dense Electronic Warfare)</text>

    <!-- Syntax Badge -->
    <rect x="25" y="135" width="670" height="65" rx="8" fill="#1f110c" stroke="#f97316" stroke-width="1.5"/>
    <text x="45" y="165" fill="#fb923c" font-family="'Consolas', monospace" font-size="20" font-weight="bold" letter-spacing="2">UCV Profile: [ CH - EA - MO ]</text>
    <text x="45" y="188" fill="#fed7aa" font-family="'Segoe UI', Arial, sans-serif" font-size="13">Copter • Hand/Box Launch • High-Discharge Electric • Attack Vector • Auto Homing • Jam-Resistant</text>

    <!-- Operational Core -->
    <g transform="translate(25, 225)">
      <rect width="670" height="400" rx="8" fill="#170c08" stroke="#3b1d12" stroke-width="1"/>
      
      <text x="25" y="35" fill="#fed7aa" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="bold">The Combat UCV Standard (Retiring "FPV"):</text>
      
      <circle cx="35" cy="70" r="5" fill="#f97316"/>
      <text x="50" y="75" fill="#fed7aa" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Terminal Guidance Physics:</text>
      <text x="245" y="75" fill="#fdba74" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Calculates dive ballistics (120–160 km/h)</text>
      <text x="50" y="95" fill="#fdba74" font-family="'Segoe UI', Arial, sans-serif" font-size="14">with onboard optical flow tracking to defeat EW jamming in the last 100 meters.</text>

      <circle cx="35" cy="130" r="5" fill="#f97316"/>
      <text x="50" y="135" fill="#fed7aa" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Electronic Counter-Measures (ECCM):</text>
      <text x="315" y="135" fill="#fdba74" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Frequency-hopping C2 (FHSS),</text>
      <text x="50" y="155" fill="#fdba74" font-family="'Segoe UI', Arial, sans-serif" font-size="14">CRPA anti-jam GNSS antennas, and fiber-optic micro-tethers (jam-immune).</text>

      <circle cx="35" cy="190" r="5" fill="#f97316"/>
      <text x="50" y="195" fill="#fed7aa" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Modular Warhead Train (MIL-STD):</text>
      <text x="295" y="195" fill="#fdba74" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Standardized electronic safe &amp; arm,</text>
      <text x="50" y="215" fill="#fdba74" font-family="'Segoe UI', Arial, sans-serif" font-size="14">shaped-charge armor penetration, and impact/proximity fusing.</text>

      <line x1="25" y1="245" x2="645" y2="245" stroke="#431407" stroke-width="1"/>

      <text x="25" y="275" fill="#fb923c" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Operational Benchmarks:</text>
      <text x="25" y="300" fill="#fef08a" font-family="'Segoe UI', Arial, sans-serif" font-size="13.5">• Strike Copter: 7–10 inch tactical interceptor with shaped charge (Ukraine)</text>
      <text x="25" y="325" fill="#fef08a" font-family="'Segoe UI', Arial, sans-serif" font-size="13.5">• Heavy Bomber: [ CL - EL - DW ] (Vampire / "Baba Yaga" 15–25 kg payload)</text>
      <text x="25" y="350" fill="#fef08a" font-family="'Segoe UI', Arial, sans-serif" font-size="13.5">• Tethered Staging: Fiber-optic guided terminal strike (Immune to all trench EW)</text>
    </g>
  </g>

  <!-- 6. Column 3: The Cross-Domain Kill Web & DoD Replicator (HAL Tier) -->
  <g id="col-hal" transform="translate(1600, 315)">
    <rect width="720" height="660" rx="12" fill="url(#cardGrad2)" stroke="#10b981" stroke-width="2"/>
    
    <!-- Tier Header -->
    <rect x="25" y="25" width="280" height="28" rx="4" fill="#10b981" fill-opacity="0.25" stroke="#34d399" stroke-width="1"/>
    <text x="165" y="44" fill="#34d399" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="bold" letter-spacing="1.5" text-anchor="middle">CROSS-DOMAIN REPLICATOR KILL WEB</text>
    
    <text x="25" y="85" fill="#f8fafc" font-family="'Segoe UI', Arial, sans-serif" font-size="24" font-weight="bold">Hardware Abstraction Layer (HAL)</text>
    <text x="25" y="112" fill="#6ee7b7" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-style="italic">Decoupling Airframe Mass from Mission Logic (Microsecond Ingestion)</text>

    <!-- Syntax Badge -->
    <rect x="25" y="135" width="670" height="65" rx="8" fill="#041f17" stroke="#10b981" stroke-width="1.5"/>
    <text x="45" y="165" fill="#34d399" font-family="'Consolas', monospace" font-size="20" font-weight="bold" letter-spacing="2">UWE Kill Web Bridge: &lt; 1.8 s</text>
    <text x="45" y="188" fill="#a7f3d0" font-family="'Segoe UI', Arial, sans-serif" font-size="13">Space (UOV) → High-Altitude Air (UAV) → Low Copter (UCV) → Sea/Land (USV/UGV)</text>

    <!-- Operational Core -->
    <g transform="translate(25, 225)">
      <rect width="670" height="400" rx="8" fill="#061f18" stroke="#0e3d2e" stroke-width="1"/>
      
      <text x="25" y="35" fill="#a7f3d0" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="bold">Why HAL Solves the Replicator Dilemma:</text>
      
      <circle cx="35" cy="70" r="5" fill="#10b981"/>
      <text x="50" y="75" fill="#d1fae5" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Zero Vendor Lock-In:</text>
      <text x="205" y="75" fill="#a7f3d0" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Any commercial ESC, brushless motor, or composite</text>
      <text x="50" y="95" fill="#a7f3d0" font-family="'Segoe UI', Arial, sans-serif" font-size="14">frame is abstracted into standardized telemetry packets (CCSDS/POSIX).</text>

      <circle cx="35" cy="130" r="5" fill="#10b981"/>
      <text x="50" y="135" fill="#d1fae5" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Automated Target Handoff:</text>
      <text x="255" y="135" fill="#a7f3d0" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Target coordinates spotted by UAV</text>
      <text x="50" y="155" fill="#a7f3d0" font-family="'Segoe UI', Arial, sans-serif" font-size="14">are queued automatically into a swarm of 12 UCVs in 1.2 seconds.</text>

      <circle cx="35" cy="190" r="5" fill="#10b981"/>
      <text x="50" y="195" fill="#d1fae5" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Cross-Domain Micro-Carriers:</text>
      <text x="270" y="195" fill="#a7f3d0" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Maritime USVs and ground UGVs act as</text>
      <text x="50" y="215" fill="#a7f3d0" font-family="'Segoe UI', Arial, sans-serif" font-size="14">mobile recharge decks &amp; forward catapults, extending swarm reach by 600 km.</text>

      <line x1="25" y1="245" x2="645" y2="245" stroke="#047857" stroke-width="1"/>

      <text x="25" y="275" fill="#34d399" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="bold">Key Takeaways for Defense One:</text>
      <text x="25" y="300" fill="#ecfdf5" font-family="'Segoe UI', Arial, sans-serif" font-size="13.5">• Retire "FPV": Replace hobbyist slang with the rigorous UCV military standard.</text>
      <text x="25" y="325" fill="#ecfdf5" font-family="'Segoe UI', Arial, sans-serif" font-size="13.5">• Functional Segregation: Standoff wings (UAV) + Disposable swarms (UCV).</text>
      <text x="25" y="350" fill="#ecfdf5" font-family="'Segoe UI', Arial, sans-serif" font-size="13.5">• Software-Defined Mass: The only viable doctrine for Indo-Pacific attritability.</text>
    </g>
  </g>

  <!-- 7. Bottom Master Taxonomy Banner -->
  <g id="taxonomy-footer" transform="translate(80, 1005)">
    <rect width="2240" height="210" rx="10" fill="#061322" stroke="#0284c7" stroke-width="2"/>
    
    <text x="40" y="40" fill="#38bdf8" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="bold" letter-spacing="2">THE UNIVERSAL SIX-CHARACTER UWE SYNTAX MATRIX:</text>
    
    <!-- Code display -->
    <rect x="40" y="60" width="800" height="50" rx="6" fill="#030b14" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="440" y="93" fill="#f8fafc" font-family="'Consolas', monospace" font-size="22" font-weight="bold" letter-spacing="4" text-anchor="middle">[ Physical · Launch ] — [ Power · Mission ] — [ Autonomy · C2 ]</text>

    <!-- Detailed legend -->
    <text x="40" y="145" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">• <tspan fill="#38bdf8" font-weight="bold">Physical Regime:</tspan> A=Atmosphere Fixed-Wing, C=Copter/Multirotor, G=Ground, S=Surface Sea, U=Subsea, O=Orbit.</text>
    <text x="40" y="170" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">• <tspan fill="#38bdf8" font-weight="bold">Launch &amp; Recovery:</tspan> I=Infrastructure Runway, L=Mobile Rail/Flatbed, H=Hand/Pneumatic Box, V=Vertical VTOL.</text>
    <text x="40" y="195" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">• <tspan fill="#38bdf8" font-weight="bold">Power &amp; Vector:</tspan> P=Piston ICE, T=Turbine, E=Electric Battery, H=Hydrogen Fuel Cell | E=Endurance Loiter, A=Attack, O=One-Way.</text>

    <text x="1140" y="145" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">• <tspan fill="#10b981" font-weight="bold">Autonomy Level:</tspan> M=Manual Tele-op, H=Human-in-the-Loop Semi-Auto, D=Autonomous Patrol, S=Swarm Collective.</text>
    <text x="1140" y="170" fill="#94a3b8" font-family="'Segoe UI', Arial, sans-serif" font-size="14">• <tspan fill="#10b981" font-weight="bold">C2 Link Layer:</tspan> R=Directional RF, M=Tactical Mesh, F=Fiber-Optic Micro-Tether, Q=Radio-Silent Autonomous.</text>
    <text x="1140" y="195" fill="#f59e0b" font-family="'Segoe UI', Arial, sans-serif" font-size="14">Author: <tspan fill="#f8fafc" font-weight="bold">Serhii Khylevych</tspan>, Principal Systems Architect | Creator of the Unmanned Warfare Engine (UWE)</text>
  </g>
</svg>
"""
    base_dir = "/home/hills/Documents/UWS"
    svg_path = os.path.join(base_dir, "uav_ucv_architecture.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {svg_path}")
    return svg_path

def convert_to_raster(svg_path):
    base_dir = "/home/hills/Documents/UWS"
    pdf_path = os.path.join(base_dir, "uav_ucv_architecture.pdf")
    
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

    # 2. Convert PDF to PNG (150 DPI)
    cmd_png = [
        "pdftoppm",
        "-png",
        "-r", "150",
        pdf_path,
        os.path.join(base_dir, "uav_ucv_architecture_tmp")
    ]
    print(f"Running: {' '.join(cmd_png)}")
    res2 = subprocess.run(cmd_png, capture_output=True, text=True)
    if res2.returncode != 0:
        print("Error converting to PNG:", res2.stderr)
        return False

    tmp_png = os.path.join(base_dir, "uav_ucv_architecture_tmp-1.png")
    final_png = os.path.join(base_dir, "uav_ucv_architecture.png")
    if os.path.exists(tmp_png):
        os.rename(tmp_png, final_png)
        print(f"Generated {final_png}")

    return True

if __name__ == "__main__":
    svg_file = create_svg()
    convert_to_raster(svg_file)
