#!/usr/bin/env python3
"""
generate_rusi_uk_maritime_infographic.py

Generates a publication-grade 16:9 tactical architecture infographic for RUSI Defence Systems:
- "The Royal Navy Maritime Dilemma & UWE Distributed Autonomous Solution"
- Architecture:
  * Panel 1 (Top Left): The UK Naval Paradox (Malloy T-150 logistics vs offensive void)
  * Panel 2 (Top Center): Escort Exhaustion in Choke Points (Red Sea / Hormuz, Aster 30 cost asymmetry)
  * Panel 3 (Top Right): North Sea Critical Undersea Infrastructure (Langeled, NSL vs Russian GUGI)
  * Central Core: The UWE Disaggregated Escort Formation (DEF) & "Silence Watch" (Inductive Parasitic Harvesting)
  * Lower Right: Modern "Endeavour" Hive (Converted commercial bulkers/tankers as Mothership Carriers)
  * Bottom Bar: Historical Precedents (Cook's Endeavour 1768, WWII MAC-ships, UWE 6-char Taxonomy)
- Outputs:
  1. rusi_uk_maritime_cui_architecture.svg (2400 x 1350)
  2. rusi_uk_maritime_cui_architecture.pdf
  3. rusi_uk_maritime_cui_architecture.png (high-res 2400 x 1350)
  4. rusi_uk_maritime_cui_architecture_fitted.png (fitted 1000px width)
"""

import os
import subprocess

def create_svg():
    width = 2400
    height = 1350

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #070b14; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="#0b1222"/>
      <stop offset="100%" stop-color="#04060d"/>
    </linearGradient>

    <!-- Card Gradients -->
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141e33"/>
      <stop offset="100%" stop-color="#0d1424"/>
    </linearGradient>

    <linearGradient id="accentCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00d2ff"/>
      <stop offset="100%" stop-color="#0088cc"/>
    </linearGradient>

    <linearGradient id="accentAmber" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff9900"/>
      <stop offset="100%" stop-color="#cc6600"/>
    </linearGradient>

    <linearGradient id="accentRed" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff3344"/>
      <stop offset="100%" stop-color="#aa1122"/>
    </linearGradient>

    <linearGradient id="accentGreen" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e676"/>
      <stop offset="100%" stop-color="#00a152"/>
    </linearGradient>

    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="{width}" height="{height}" fill="url(#bgGrad)"/>

  <!-- Subtle Blueprint Grid -->
  <g opacity="0.05">
    {''.join([f'<line x1="{x}" y1="0" x2="{x}" y2="{height}" stroke="#00d2ff" stroke-width="1"/>' for x in range(0, width, 80)])}
    {''.join([f'<line x1="0" y1="{y}" x2="{width}" y2="{y}" stroke="#00d2ff" stroke-width="1"/>' for y in range(0, height, 80)])}
  </g>

  <!-- ==================== HEADER BAR ==================== -->
  <rect x="60" y="40" width="2280" height="90" rx="12" fill="#0e172a" stroke="#1e293b" stroke-width="2" filter="url(#shadow)"/>
  
  <!-- Header Title -->
  <text x="90" y="85" fill="#ffffff" font-size="28" font-weight="800" letter-spacing="1">THE ROYAL NAVY ESCORT CRISIS &amp; THE UWE AUTONOMOUS ARCHITECTURE</text>
  <text x="90" y="112" fill="#94a3b8" font-size="16" font-weight="500">RUSI Defence Systems Special Monograph | Disaggregated Formations, Silence Watch &amp; Commercial Mothership Hives</text>

  <!-- Author Badge -->
  <rect x="1860" y="55" width="450" height="60" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="1880" y="80" fill="#38bdf8" font-size="14" font-weight="700">AUTHOR &amp; ARCHITECT:</text>
  <text x="1880" y="102" fill="#f8fafc" font-size="16" font-weight="600">Serhii Khylevych | UWE Group</text>

  <!-- ==================== ROW 1: THE THREE STRATEGIC GAPS (Y: 150 to 450) ==================== -->

  <!-- GAP 1: LOGISTICS DRONE PARADOX -->
  <rect x="60" y="150" width="730" height="290" rx="14" fill="url(#cardGrad)" stroke="#ff9900" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="60" y="150" width="730" height="8" rx="4" fill="url(#accentAmber)"/>
  <text x="90" y="195" fill="#ffb74d" font-size="18" font-weight="800" letter-spacing="0.5">I. THE LOGISTICS UAV PARADOX</text>
  <text x="90" y="222" fill="#ffffff" font-size="20" font-weight="700">Flying Forklifts vs. Kinetic Striking Void</text>
  
  <text x="90" y="260" fill="#cbd5e1" font-size="15" font-weight="400">
    <tspan x="90" dy="0">• Heavy Lift Challenge (Malloy T-150 / T-600, Windracers ULTRA):</tspan>
    <tspan x="90" dy="24">  Heavy focus on ship-to-ship stores replenishment and CASEVAC.</tspan>
    <tspan x="90" dy="28">• The Doctrinal Vacuum: Royal Navy treats uncrewed platforms as</tspan>
    <tspan x="90" dy="24">  auxiliary logistics haulers, lacking offensive kinetic integration.</tspan>
    <tspan x="90" dy="28">• Vulnerability: Unarmed logistics drones cannot survive in contested</tspan>
    <tspan x="90" dy="24">  airspaces without organic escort and autonomous kinetic strike.</tspan>
  </text>

  <!-- GAP 2: CHOKE-POINT ESCORT EXHAUSTION -->
  <rect x="835" y="150" width="730" height="290" rx="14" fill="url(#cardGrad)" stroke="#ff3344" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="835" y="150" width="730" height="8" rx="4" fill="url(#accentRed)"/>
  <text x="865" y="195" fill="#ff6b81" font-size="18" font-weight="800" letter-spacing="0.5">II. CHOKE-POINT ESCORT EXHAUSTION</text>
  <text x="865" y="222" fill="#ffffff" font-size="20" font-weight="700">Red Sea / Hormuz &amp; Aster 30 Economic Defeat</text>
  
  <text x="865" y="260" fill="#cbd5e1" font-size="15" font-weight="400">
    <tspan x="865" dy="0">• Acute Fleet Attrition: Only 6 Type 45s and ~10 ageing Type 23s;</tspan>
    <tspan x="865" dy="24">  UK struggled to sustain a single destroyer (HMS Diamond) on station.</tspan>
    <tspan x="865" dy="28">• Economic Asymmetry: Firing £1.8M Aster 30 missiles against £15k</tspan>
    <tspan x="865" dy="24">  asymmetric drones guarantees rapid magazine and budget exhaustion.</tspan>
    <tspan x="865" dy="28">• Carrier Immobilization: £6.5B Queen Elizabeth class sidelined</tspan>
    <tspan x="865" dy="24">  due to lack of escort frigates and auxiliary support (RFA Fort Victoria).</tspan>
  </text>

  <!-- GAP 3: NORTH SEA CUI VULNERABILITY -->
  <rect x="1610" y="150" width="730" height="290" rx="14" fill="url(#cardGrad)" stroke="#00d2ff" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="1610" y="150" width="730" height="8" rx="4" fill="url(#accentCyan)"/>
  <text x="1640" y="195" fill="#38bdf8" font-size="18" font-weight="800" letter-spacing="0.5">III. NORTH SEA CRITICAL UNDERSEA INFRASTRUCTURE</text>
  <text x="1640" y="222" fill="#ffffff" font-size="20" font-weight="700">Langeled &amp; Power Cables vs. Russian GUGI</text>
  
  <text x="1640" y="260" fill="#cbd5e1" font-size="15" font-weight="400">
    <tspan x="1640" dy="0">• Vital Arteries: Langeled pipeline delivers &gt;20% of total UK gas;</tspan>
    <tspan x="1640" dy="24">  North Sea Link (720 km HVDC, 1400 MW) anchors national grid power.</tspan>
    <tspan x="1640" dy="28">• Russian Threat: GUGI specialized espionage motherships (Yantar)</tspan>
    <tspan x="1640" dy="24">  and titanium submersibles (Losharik) operate at 300–1200m depths.</tspan>
    <tspan x="1640" dy="28">• Inadequate Response: Repurposed RFA Proteus (MROS) is a single</tspan>
    <tspan x="1640" dy="24">  vessel that cannot police 4,000+ km of stormy North Sea seabed.</tspan>
  </text>

  <!-- ==================== ROW 2: THE UWE ARCHITECTURAL SOLUTION (Y: 470 to 920) ==================== -->

  <!-- CORE 1: DISAGGREGATED ESCORT FORMATION (DEF) -->
  <rect x="60" y="470" width="730" height="430" rx="14" fill="url(#cardGrad)" stroke="#38bdf8" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="90" y="515" fill="#38bdf8" font-size="18" font-weight="800">DISAGGREGATED ESCORT FORMATION (DEF)</text>
  <text x="90" y="542" fill="#ffffff" font-size="22" font-weight="700">Replacing the £1B Destroyer with 12 Nodes</text>

  <!-- Architecture Diagram Boxes -->
  <g transform="translate(90, 565)">
    <!-- Box 1 -->
    <rect x="0" y="0" width="670" height="85" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1"/>
    <text x="20" y="30" fill="#38bdf8" font-size="15" font-weight="700">FORWARD ISR SCREEN [AH-SP]-[DE-HE]-[PC-ISR]</text>
    <text x="20" y="55" fill="#94a3b8" font-size="13">Passive ESM / LPI Radar / Optronics Mast | 10–15 nm ahead of convoy</text>
    <text x="20" y="73" fill="#cbd5e1" font-size="12">Detects hostile surface craft &amp; low-altitude loitering munitions early</text>

    <!-- Box 2 -->
    <rect x="0" y="100" width="670" height="85" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="20" y="130" fill="#f87171" font-size="15" font-weight="700">KINETIC SHORAD / C-UAS USV [AH-P]-[DE-D]-[PC-K]</text>
    <text x="20" y="155" fill="#94a3b8" font-size="13">Stabilized 30mm Bushmaster II Airburst Cannon + Short-Range Missiles</text>
    <text x="20" y="173" fill="#4ade80" font-size="13" font-weight="700">Cost per intercept: £1,500 per burst (vs £1.8M Aster 30)</text>

    <!-- Box 3 -->
    <rect x="0" y="200" width="670" height="85" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="20" y="230" fill="#34d399" font-size="15" font-weight="700">SUBSEA ACOUSTIC SCREEN UUV [DP-EPI]-[EM-BG]-[TC-ASW]</text>
    <text x="20" y="255" fill="#94a3b8" font-size="13">Towed Thin-Line Passive Hydrophone Array | Under-layer Glider</text>
    <text x="20" y="273" fill="#cbd5e1" font-size="12">Monitors thermal layers for hostile torpedoes, SDVs and midget subs</text>
  </g>

  <!-- CORE 2: SILENCE WATCH & ENERGY HARVESTING -->
  <rect x="835" y="470" width="730" height="430" rx="14" fill="url(#cardGrad)" stroke="#10b981" stroke-width="2" filter="url(#shadow)"/>
  <text x="865" y="515" fill="#34d399" font-size="18" font-weight="800">"SILENCE WATCH" &amp; PARASITIC HARVESTING</text>
  <text x="865" y="542" fill="#ffffff" font-size="22" font-weight="700">Zero Hotel Load &amp; Perpetual Seabed Presence</text>

  <g transform="translate(865, 565)">
    <!-- Zero Hotel Load Box -->
    <rect x="0" y="0" width="670" height="90" rx="8" fill="#064e3b" stroke="#059669" stroke-width="1.5"/>
    <text x="20" y="32" fill="#a7f3d0" font-size="16" font-weight="800">ELIMINATION OF THE "HOTEL LOAD"</text>
    <text x="20" y="57" fill="#ffffff" font-size="14">Crewed Warship: 75% fuel &amp; power consumed by humans (HVAC, water, food).</text>
    <text x="20" y="77" fill="#6ee7b7" font-size="14" font-weight="700">UWE Formation: HOTEL LOAD = 0 kW. Zero human biology support.</text>

    <!-- Inductive Harvesting Box -->
    <rect x="0" y="105" width="670" height="180" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="20" y="135" fill="#34d399" font-size="16" font-weight="800">INDUCTIVE HARVESTING FROM SUBSEA INFRASTRUCTURE</text>
    
    <text x="20" y="165" fill="#cbd5e1" font-size="14">
      <tspan x="20" dy="0">• North Sea Link transmits 1,400 MW HVDC across 720 km seabed.</tspan>
      <tspan x="20" dy="25">• Langeled pipeline carries active cathodic corrosion currents.</tspan>
      <tspan x="20" dy="25">• Resident UUVs dock on cable berm via Inductive Coupling Collars,</tspan>
      <tspan x="20" dy="24">  trickle-charging battery banks DIRECTLY FROM THE POWER GRID.</tspan>
      <tspan x="20" dy="28" fill="#38bdf8" font-weight="700">Result: 180–360 days continuous subsea picket without surface ship.</tspan>
    </text>
  </g>

  <!-- CORE 3: AUTONOMOUS MOTHERSHIP CARRIER (AMC) -->
  <rect x="1610" y="470" width="730" height="430" rx="14" fill="url(#cardGrad)" stroke="#a855f7" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="1640" y="515" fill="#c084fc" font-size="18" font-weight="800">THE MODERN "ENDEAVOUR" HIVE</text>
  <text x="1640" y="542" fill="#ffffff" font-size="22" font-weight="700">Commercial Tanker &amp; Bulker Conversions</text>

  <g transform="translate(1640, 565)">
    <!-- Mothership Specs Box -->
    <rect x="0" y="0" width="670" height="150" rx="8" fill="#1e1b4b" stroke="#7e22ce" stroke-width="1.5"/>
    <text x="20" y="32" fill="#e9d5ff" font-size="16" font-weight="800">CONVERTED AFRAMAX / HANDYMAX BULKER HULL</text>
    <text x="20" y="60" fill="#cbd5e1" font-size="14">
      <tspan x="20" dy="0">• Acquisition &amp; Naval Refit: £120M total (vs £1.05B for 1 Type 45 destroyer)</tspan>
      <tspan x="20" dy="24">• Cavernous Capacity: Internal holds house 60–80 USVs + 30 UUVs</tspan>
      <tspan x="20" dy="24">• Automated LARS: Stern slipway &amp; overhead bridge gantry (Sea State 5)</tspan>
      <tspan x="20" dy="24">• Power Generation: 15–30 MW commercial diesel plant fast-charges fleet</tspan>
    </text>

    <!-- Double-Hull Box -->
    <rect x="0" y="165" width="670" height="120" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <text x="20" y="195" fill="#d8b4fe" font-size="15" font-weight="700">DOUBLE-HULL INDUSTRIAL RESILIENCE</text>
    <text x="20" y="222" fill="#94a3b8" font-size="13">Commercial double bottoms absorb multiple mine/missile strikes (1980s Tanker War).</text>
    <text x="20" y="244" fill="#cbd5e1" font-size="13">No delicate sensors on hull; operational survival far exceeds thin-skinned warships.</text>
    <text x="20" y="266" fill="#38bdf8" font-size="13" font-weight="700">Fleet Ratio: 7 Autonomous Motherships for the cost of 1 Type 45 Destroyer.</text>
  </g>

  <!-- ==================== ROW 3: HISTORICAL PROOF & TAXONOMY (Y: 920 to 1290) ==================== -->
  <rect x="60" y="920" width="2280" height="370" rx="14" fill="#0a0f1d" stroke="#1e293b" stroke-width="2" filter="url(#shadow)"/>
  
  <text x="90" y="965" fill="#f8fafc" font-size="20" font-weight="800">HISTORICAL PRECEDENTS &amp; CYBER-PHYSICAL TAXONOMIC REGIMES</text>

  <!-- Column 1: James Cook's Collier -->
  <g transform="translate(90, 995)">
    <rect x="0" y="0" width="700" height="260" rx="10" fill="#111827" stroke="#374151" stroke-width="1"/>
    <text x="25" y="35" fill="#fbbf24" font-size="17" font-weight="700">1768: JAMES COOK'S WHITBY COLLIER</text>
    <text x="25" y="60" fill="#9ca3af" font-size="14">Admiralty rejected fast rated frigates; bought coal bark Earl of Pembroke for £2,840.</text>
    <text x="25" y="95" fill="#e5e7eb" font-size="14">
      <tspan x="25" dy="0">• Broad beam, flat floor, shallow draft (14 ft) allowed careening on reef.</tspan>
      <tspan x="25" dy="25">• Sturdy merchant timbers survived Great Barrier Reef stranding in 1770.</tspan>
      <tspan x="25" dy="25">• Massive cargo hold sustained 3-year expedition without naval bases.</tspan>
      <tspan x="25" dy="30" fill="#fbbf24" font-weight="600">Proof: Working merchant hulls repeatedly solve Britain's strategic missions.</tspan>
    </text>
  </g>

  <!-- Column 2: WWII MAC-Ships -->
  <g transform="translate(850, 995)">
    <rect x="0" y="0" width="700" height="260" rx="10" fill="#111827" stroke="#374151" stroke-width="1"/>
    <text x="25" y="35" fill="#60a5fa" font-size="17" font-weight="700">1942: WWII MERCHANT AIRCRAFT CARRIERS</text>
    <text x="25" y="60" fill="#9ca3af" font-size="14">Royal Navy faced mid-Atlantic escort deficit against German U-boat wolfpacks.</text>
    <text x="25" y="95" fill="#e5e7eb" font-size="14">
      <tspan x="25" dy="0">• Converted 19 grain bulkers and oil tankers with simple wooden flight decks.</tspan>
      <tspan x="25" dy="25">• Operated Fairey Swordfish while carrying FULL CARGO of grain and fuel.</tspan>
      <tspan x="25" dy="25">• 100% Convoy Immunity: Zero merchant ships lost under MAC-ship escort.</tspan>
      <tspan x="25" dy="30" fill="#60a5fa" font-weight="600">Proof: Dual-use commercial carriers eliminate escort bottlenecks under fire.</tspan>
    </text>
  </g>

  <!-- Column 3: 6-Character UWE Taxonomy -->
  <g transform="translate(1610, 995)">
    <rect x="0" y="0" width="700" height="260" rx="10" fill="#111827" stroke="#374151" stroke-width="1"/>
    <text x="25" y="35" fill="#34d399" font-size="17" font-weight="700">2026: 6-CHARACTER UWE TAXONOMY</text>
    <text x="25" y="60" fill="#9ca3af" font-size="14">Replacing arbitrary displacement brackets with cyber-physical operating physics.</text>
    <text x="25" y="95" fill="#e5e7eb" font-size="14">
      <tspan x="25" dy="0">• USV Regimes [AH]-[DE]-[PC]: Hydrodynamic mode, energy topology, role.</tspan>
      <tspan x="25" dy="25">• UUV Horizons [DP]-[EM]-[TC]: Bathymetric depth, motive drive, mission.</tspan>
      <tspan x="25" dy="25">• Vector 6 &amp; 7 Integration: Mothership LARS &amp; Cross-domain deployment.</tspan>
      <tspan x="25" dy="30" fill="#34d399" font-weight="600">Outcome: Deterministic integration of scalable algorithmic mass for MoD UK.</tspan>
    </text>
  </g>

</svg>
"""

    base_dir = "/home/hills/Documents/UWS"
    svg_path = os.path.join(base_dir, "rusi_uk_maritime_cui_architecture.svg")
    pdf_path = os.path.join(base_dir, "rusi_uk_maritime_cui_architecture.pdf")
    png_path = os.path.join(base_dir, "rusi_uk_maritime_cui_architecture.png")
    fitted_path = os.path.join(base_dir, "rusi_uk_maritime_cui_architecture_fitted.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated SVG: {svg_path}")

    # Step 1: Convert SVG to PDF via LibreOffice
    print("Converting SVG to PDF via LibreOffice...")
    cmd_pdf = [
        "libreoffice",
        "--headless",
        "--convert-to", "pdf:draw_pdf_Export",
        "--outdir", base_dir,
        svg_path
    ]
    subprocess.run(cmd_pdf, check=True)
    print(f"Generated PDF: {pdf_path}")

    # Step 2: Convert PDF to high-res PNG (2400 x 1350) via pdftoppm
    print("Converting PDF to high-res PNG (2400x1350)...")
    cmd_png = [
        "pdftoppm",
        "-png",
        "-r", "150",
        pdf_path,
        os.path.join(base_dir, "rusi_tmp")
    ]
    subprocess.run(cmd_png, check=True)

    tmp_files = [f for f in os.listdir(base_dir) if f.startswith("rusi_tmp") and f.endswith(".png")]
    if tmp_files:
        tmp_file = os.path.join(base_dir, sorted(tmp_files)[0])
        os.rename(tmp_file, png_path)
        print(f"Generated high-res PNG: {png_path}")

    # Step 3: Convert PDF to fitted PNG (width 1000px) via pdftoppm
    print("Generating fitted PNG (width 1000px)...")
    cmd_fit = [
        "pdftoppm",
        "-png",
        "-scale-to-x", "1000",
        "-scale-to-y", "-1",
        pdf_path,
        os.path.join(base_dir, "rusi_fit_tmp")
    ]
    subprocess.run(cmd_fit, check=True)

    tmp_fit_files = [f for f in os.listdir(base_dir) if f.startswith("rusi_fit_tmp") and f.endswith(".png")]
    if tmp_fit_files:
        tmp_fit_file = os.path.join(base_dir, sorted(tmp_fit_files)[0])
        os.rename(tmp_fit_file, fitted_path)
        print(f"Generated fitted PNG: {fitted_path}")

if __name__ == "__main__":
    create_svg()
