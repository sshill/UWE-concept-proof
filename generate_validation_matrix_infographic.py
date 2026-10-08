#!/usr/bin/env python3
import os
import subprocess
import html

def esc(text):
    """Safely escape text for XML/SVG rendering."""
    return html.escape(str(text), quote=False)

def create_svg():
    W = 2400
    H = 1350  # Exact 16:9 widescreen presentation canvas

    # Column x and widths (Total width = 2350, left margin = 25)
    # Column x and widths (Total width = 2350, left margin = 25)
    # Col 0: DOMAIN & CODE (165)
    # Col 1: REFERENCE PLATFORM (355)
    # Col 2: OEM / OPERATOR (300)
    # Col 3: HORIZON / MEDIUM (325)
    # Col 4: DIMENSIONS & MASS (365)
    # Col 5: POWERPLANT & ENERGY (410)
    # Col 6: COMMS & AUTONOMY (430)
    col_w = [165, 355, 300, 325, 365, 410, 430]
    col_x = [25, 190, 545, 845, 1170, 1535, 1945]

    headers = [
        "DOMAIN & CODE",
        "REFERENCE PLATFORM",
        "OEM / OPERATOR",
        "HORIZON / MEDIUM",
        "DIMENSIONS & MASS",
        "POWERPLANT & ENERGY",
        "COMMS & AUTONOMY"
    ]

    header_icons = ["🌐", "🎯", "🏭", "🌊", "⚖️", "⚡", "📡"]

    # 12 Rows across 6 Domains
    # (domain_tag, code, domain_icon, accent_col, bg_tint, [cells_data: 6 tuples of (line1, line2)])
    rows_data = [
        # UOV (Orbital Space)
        (
            "UOV", "LR-SL-MD", "🛰️", "#c084fc", "#1a0f2e",
            [
                ("Starshield / v2 Mini", "Direct-to-Cell Satellite"),
                ("SpaceX", "(USA)"),
                ("LEO (550 km)", "Exoatmospheric Orbit"),
                ("800 kg; 30 m wingspan", "30 m high-efficiency solar"),
                ("Solar + Krypton/Argon", "Hall Ion Electric Thruster"),
                ("Laser ISL + Ku/Ka AESA", "Direct-to-Cell cellular link")
            ]
        ),
        (
            "UOV", "CR-SP-DX", "🛰️", "#c084fc", "#1a0f2e",
            [
                ("CAPSTONE / Oracle", "Cislunar Nav Probe (CHPS)"),
                ("NASA / USSF / Adv. Space", "(USA)"),
                ("Cislunar NRHO, L1–L2", "Deep Space Gravity Wells"),
                ("25 kg total mass", "CubeSat 12U form-factor"),
                ("Solar Arrays + Chemical", "Micro-Hydrazine Thrusters"),
                ("Deep Space Network (DSN)", "Autonomous optical IMU nav")
            ]
        ),

        # UAV (Fixed-Wing Aviation)
        (
            "UAV", "AL-PE-HR", "✈️", "#38bdf8", "#061e33",
            [
                ("Bayraktar TB2 / Reaper", "Strategic MALE Picket"),
                ("Baykar / General Atomics", "(Turkey / USA)"),
                ("MALE (5–8 km)", "Tropospheric Wing Flight"),
                ("650 kg MTOW, 12 m span", "150 kg payload capacity"),
                ("Rotax 912 Piston ICE", "100 hp Avgas/Mogas engine"),
                ("Directional COFDM C2", "STANAG 4586 compliant link")
            ]
        ),
        (
            "UAV", "AL-CO-MO", "✈️", "#38bdf8", "#061e33",
            [
                ("Shahed-136 / Scalpel", "Long-Range Strike Wing"),
                ("Adversary OEM / MilTech", "(Global Threat)"),
                ("Low-Altitude Wing", "50–3,000 m Ingress"),
                ("200 kg gross, 2.5 m span", "50 kg PBX shaped warhead"),
                ("MD-550 50 hp 2-stroke ICE", "Solid rocket booster start"),
                ("Radio-Silent (Quiet Mode)", "CRPA GNSS + Optical OWM")
            ]
        ),

        # UCV (Tactical Multirotors)
        (
            "UCV", "CH-EA-MO", "🚁", "#00f5d4", "#032620",
            [
                ("Tactical Strike FPV", "Combat Quadcopter 7–10\""),
                ("Frontline Ecosystem", "(Ukraine / Global)"),
                ("Tactical Boundary Layer", "0–500 m AGL Envelope"),
                ("1.2–3.5 kg frame", "1.5 kg shaped-charge RPG"),
                ("6S2P Li-ion / LiPo pack", "4x Brushless FOC ESCs"),
                ("5.8 GHz Analog / FHSS", "Micro-Fiber-Optic spool tether")
            ]
        ),
        (
            "UCV", "CL-EL-DW", "🚁", "#00f5d4", "#032620",
            [
                ("Vampire (\"Baba Yaga\")", "Heavy Bomber / Relay"),
                ("SkyFall Ecosystem", "(Ukraine)"),
                ("Night Low-Altitude", "50–400 m AGL Operations"),
                ("25–40 kg hexacopter", "15 kg multi-drop bomb rack"),
                ("12S LiFePO4 battery bank", "High-torque brushless motors"),
                ("Encrypted FHSS Radio", "Thermal IR + Edge-AI lock")
            ]
        ),

        # UGV (Ground Robotics)
        (
            "UGV", "GL-EB-DW", "🚜", "#fbbf24", "#261a04",
            [
                ("THeMIS Combined Arms", "Logistic & Weapon Hub"),
                ("Milrem Robotics", "(Estonia)"),
                ("High-Obstacle Mud & Rubble", "Trenches, Off-Road Terrain"),
                ("1,630 kg; 2.4 × 2.0 m", "1,200 kg payload capacity"),
                ("Diesel-Electric Hybrid", "Li-ion pack + V2V power bus"),
                ("Encrypted MIMO Mesh", "3D LiDAR SLAM obstacle map")
            ]
        ),
        (
            "UGV", "GB-EA-HA", "🚜", "#fbbf24", "#261a04",
            [
                ("Shablya Remote Turret", "Automated Sleeper Bunker"),
                ("Brave1 Ecosystem", "(Ukraine)"),
                ("Static Hardened Position", "Trench / Bunker Parapet"),
                ("40–180 kg total mass", "7.62mm / 12.7mm weapon"),
                ("24V External Battery Pack", "Deep Sleep FSM (<5 mA standby)"),
                ("Hardwired Fiber / Wire", "Low-power secure Wi-Fi relay")
            ]
        ),

        # USV (Surface Marine)
        (
            "USV", "SL-PA-MO", "🚤", "#60a5fa", "#081d36",
            [
                ("Magura V5 / Sea Baby", "Wave-Piercing Strike USV"),
                ("Special Technotrade / SSU", "(Ukraine)"),
                ("Marine Littoral Waters", "Sea State 4–5 Waves"),
                ("1,000 kg; 5.5 m length", "450–850 kg shaped warhead"),
                ("Turbo Marine ICE / Diesel", "Low-cavitation tunnel waterjet"),
                ("Dual Starlink + Kymeta AESA", "Encrypted LoS mesh fallback")
            ]
        ),
        (
            "USV", "ST-EL-DR", "🚤", "#60a5fa", "#081d36",
            [
                ("Saildrone Voyager", "Autonomous Ocean Picket"),
                ("Saildrone Inc.", "(USA)"),
                ("Open Ocean Pelagic", "Sea State 6+ Endurance"),
                ("4,000 kg; 10.0 m length", "Multi-beam survey sonar"),
                ("Rigid Wing Sail + Solar", "Auxiliary diesel generator"),
                ("Iridium Certus + Inmarsat", "Optical AIS + autonomous nav")
            ]
        ),

        # UUV (Sub-Surface Marine)
        (
            "UUV", "UT-EB-SQ", "⚓", "#818cf8", "#121536",
            [
                ("HUGIN 6000", "Deep Benthic Survey Picket"),
                ("Kongsberg Maritime", "(Norway)"),
                ("Deep Benthic Seabed", "200–6,000 m Bathymetry"),
                ("2,200 kg; 6.5 m length", "High-resolution SAS sonar"),
                ("48 kWh Solid-State Li-ion", "Pressure-tolerant battery bank"),
                ("Acoustic HiPAP Modem", "Ring Laser Gyro (RLG) INS")
            ]
        ),
        (
            "UUV", "UB-EA-MA", "⚓", "#818cf8", "#121536",
            [
                ("Marichka Long-Range", "Strike Submersible UUV"),
                ("AMMO.UKRAINE / Brave1", "(Ukraine)"),
                ("Subsea Shelf & Pelagic", "0–100 m Operating Depth"),
                ("1,000 kg; 6.0 × 1.0 m", "450 kg PBX demolition charge"),
                ("100 kWh Custom LiFePO4", "Electric ring pod thruster"),
                ("Passive Sonar + INS", "Deployable fiber / RF mast")
            ]
        )
    ]

    table_top = 138
    hdr_h = 52
    row_h = 75
    same_domain_gap = 4
    diff_domain_gap = 10

    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#040811"/>
      <stop offset="40%" stop-color="#06111f"/>
      <stop offset="100%" stop-color="#091629"/>
    </linearGradient>
    <linearGradient id="hdrGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f223d"/>
      <stop offset="100%" stop-color="#081426"/>
    </linearGradient>
    <linearGradient id="accentCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="50%" stop-color="#00b4d8"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
    <pattern id="tacticalGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#13233a" stroke-width="0.6" stroke-opacity="0.35"/>
      <circle cx="36" cy="36" r="1" fill="#00d2ff" fill-opacity="0.12"/>
    </pattern>
  </defs>

  <style>
    .font-sans {{ font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif; }}
    .font-mono {{ font-family: 'Consolas', 'Roboto Mono', 'Courier New', monospace; }}
  </style>

  <!-- Background -->
  <rect width="{W}" height="{H}" fill="url(#bgGrad)"/>
  <rect width="{W}" height="{H}" fill="url(#tacticalGrid)"/>
  <rect x="0" y="0" width="{W}" height="5" fill="url(#accentCyan)"/>

  <!-- ==================== HEADER ==================== -->
  <g transform="translate(25, 22)">
    <rect x="0" y="0" width="240" height="26" rx="5" fill="#0c2340" stroke="#00a8e8" stroke-width="1.2"/>
    <text x="120" y="18" fill="#00f5d4" class="font-sans" font-size="13" font-weight="700" letter-spacing="1.8" text-anchor="middle">MILTECH ARCHITECTURE</text>
    
    <text x="0" y="62" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" letter-spacing="0.5">UNIFIED UWE CROSS-DOMAIN EMPIRICAL VALIDATION MATRIX</text>
    <text x="0" y="94" fill="#94a3b8" class="font-sans" font-size="18.5">
      Standardized 6-Character Cyber-Physical Benchmarks Across <tspan fill="#00f5d4" font-weight="700">Space, Air, Ground, Maritime &amp; Subsea Domains</tspan>
    </text>

    <!-- Top Right Meta Card -->
    <g transform="translate(1780, 2)">
      <rect x="0" y="0" width="570" height="96" rx="7" fill="#09182a" stroke="#1d385c" stroke-width="1.3"/>
      <text x="20" y="27" fill="#38bdf8" class="font-sans" font-size="14.5" font-weight="700" letter-spacing="0.8">HARDWARE ABSTRACTION LAYER (HAL) RIGOR</text>
      <text x="20" y="52" fill="#cbd5e1" class="font-sans" font-size="14.5">"Chassis is invariant HAL. Lethality &amp; OWM are runtime decorators."</text>
      <text x="20" y="78" fill="#94a3b8" class="font-sans" font-size="13.5">Full Traceability: Field Battle Tests ≡ Cyber-Physical Invariant Laws</text>
    </g>
  </g>
''')

    # ==================== TABLE HEADERS ====================
    svg.append(f'  <g transform="translate(0, {table_top})">')
    for i in range(7):
        x = col_x[i]
        w = col_w[i]
        title = esc(headers[i])
        icon = header_icons[i]
        svg.append(f'    <rect x="{x}" y="0" width="{w}" height="{hdr_h}" rx="6" fill="url(#hdrGrad)" stroke="#1a3556" stroke-width="1.2"/>')
        svg.append(f'    <line x1="{x+4}" y1="{hdr_h-2}" x2="{x+w-4}" y2="{hdr_h-2}" stroke="#00b4d8" stroke-width="2"/>')
        if i == 0:
            svg.append(f'    <text x="{x + w/2}" y="33" fill="#00f5d4" class="font-sans" font-size="16.5" font-weight="800" letter-spacing="1.2" text-anchor="middle">{icon} {title}</text>')
        else:
            svg.append(f'    <text x="{x + 16}" y="33" fill="#f8fafc" class="font-sans" font-size="16.5" font-weight="800" letter-spacing="0.4">{icon}  {title}</text>')
    svg.append('  </g>')

    # ==================== DATA ROWS (12 ROWS) ====================
    curr_y = table_top + hdr_h + 6
    for r_idx, row in enumerate(rows_data):
        domain_tag, code, icon, accent_col, bg_tint, cells = row
        
        svg.append(f'\n  <!-- Row {r_idx+1}: {domain_tag} - {code} -->')
        svg.append(f'  <g transform="translate(0, {curr_y})">')
        
        # Col 0: DOMAIN & CODE Pill
        w0 = col_w[0]
        x0 = col_x[0]
        svg.append(f'''    <rect x="{x0}" y="0" width="{w0}" height="{row_h}" rx="6" fill="{bg_tint}" stroke="{accent_col}" stroke-width="1.3"/>
    <g transform="translate({x0 + 16}, 30)">
      <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="18" font-weight="800">{icon} {esc(domain_tag)}</text>
    </g>
    <g transform="translate({x0 + 14}, 54)">
      <rect x="0" y="-14" width="136" height="24" rx="4" fill="#061220" stroke="{accent_col}" stroke-width="1.2"/>
      <text x="68" y="3" fill="{accent_col}" class="font-mono" font-size="14.5" font-weight="800" text-anchor="middle">{esc(code)}</text>
    </g>''')

        # Remaining 6 columns
        for c_idx in range(6):
            c_num = c_idx + 1
            xc = col_x[c_num]
            wc = col_w[c_num]
            line1, line2 = cells[c_idx]
            
            svg.append(f'''    <rect x="{xc}" y="0" width="{wc}" height="{row_h}" rx="6" fill="#091424" stroke="#15263d" stroke-width="1.1"/>
    <line x1="{xc}" y1="8" x2="{xc}" y2="{row_h-8}" stroke="{accent_col}" stroke-width="3.5" stroke-linecap="round"/>
    <g transform="translate({xc + 16}, 0)">
      <text x="0" y="31" fill="#ffffff" class="font-sans" font-size="18" font-weight="700" letter-spacing="0.1">{esc(line1)}</text>
      <text x="0" y="57" fill="{accent_col}" class="font-sans" font-size="15.5" font-weight="500">{esc(line2)}</text>
    </g>''')

        svg.append('  </g>')
        
        # Decide gap
        gap = diff_domain_gap if (r_idx % 2 == 1) else same_domain_gap
        curr_y += row_h + gap

    # ==================== BOTTOM ARCHITECTURAL STRIP ====================
    legend_y = curr_y + 10
    svg.append(f'''
  <!-- Bottom Doctrinal Takeaway Strip -->
  <g transform="translate(25, {legend_y})">
    <rect x="0" y="0" width="2350" height="86" rx="7" fill="#081422" stroke="#182f4e" stroke-width="1.2"/>
    
    <g transform="translate(24, 21)">
      <circle cx="12" cy="12" r="7" fill="#c084fc"/>
      <text x="30" y="17" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="700">Space &amp; Air (UOV / UAV):</text>
      <text x="30" y="44" fill="#94a3b8" class="font-sans" font-size="15">Orbital laser mesh &amp; high-altitude C4ISR overwatch. Direct phone-to-drone command &amp; SAR mapping.</text>
    </g>

    <g transform="translate(810, 21)">
      <circle cx="12" cy="12" r="7" fill="#00f5d4"/>
      <text x="30" y="17" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="700">Tactical Air &amp; Ground (UCV / UGV):</text>
      <text x="30" y="44" fill="#94a3b8" class="font-sans" font-size="15">Massed fiber FPV strikes, automated robotic logistics, V2V powerbanks, and sub-5mA silent sleeper turrets.</text>
    </g>

    <g transform="translate(1620, 21)">
      <circle cx="12" cy="12" r="7" fill="#60a5fa"/>
      <text x="30" y="17" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="700">Maritime Surface &amp; Subsea (USV / UUV):</text>
      <text x="30" y="44" fill="#94a3b8" class="font-sans" font-size="15">Wave-piercing strike swarms &amp; benthic 30-day sleeper subs. Total littoral access denial at zero crew risk.</text>
    </g>
  </g>
''')

    # ==================== FOOTER ====================
    footer_y = H - 26
    svg.append(f'''
  <g transform="translate(25, {footer_y})">
    <line x1="0" y1="0" x2="2350" y2="0" stroke="#14263b" stroke-width="1.2"/>
    <text x="0" y="18" fill="#64748b" class="font-sans" font-size="13.5" font-weight="700" letter-spacing="1.2">UNMANNED WARFARE ENGINE (UWE)</text>
    <text x="290" y="18" fill="#334155" class="font-sans" font-size="13.5">•</text>
    <text x="308" y="18" fill="#94a3b8" class="font-sans" font-size="13.5">SECTION 6.1: UNIFIED CROSS-DOMAIN EMPIRICAL VALIDATION MATRIX</text>
    <text x="2350" y="18" fill="#00e5ff" class="font-sans" font-size="13.5" font-weight="700" text-anchor="end">SERHII KHYLEVYCH — SYSTEMS ARCHITECT &amp; MILTECH STRATEGIST</text>
  </g>
</svg>''')

    return "".join(svg)

def export_file(base_name, svg_content):
    work_dir = "/home/hills/Documents/UWS"
    svg_path = os.path.join(work_dir, f"{base_name}.svg")
    pdf_path = os.path.join(work_dir, f"{base_name}.pdf")
    png_path = os.path.join(work_dir, f"{base_name}.png")
    jpg_path = os.path.join(work_dir, f"{base_name}.jpg")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated SVG: {svg_path}")

    lo_profile = "file:///home/hills/Documents/UWS/.lo_user"
    cmd_pdf = [
        "libreoffice",
        f"-env:UserInstallation={lo_profile}",
        "--headless",
        "--convert-to", "pdf",
        svg_path,
        "--outdir", work_dir
    ]
    subprocess.run(cmd_pdf, check=True)
    print(f"Generated PDF: {pdf_path}")

    tmp_prefix = os.path.join(work_dir, f"{base_name}_render")
    cmd_png = [
        "pdftoppm",
        "-png",
        "-r", "150",
        pdf_path,
        tmp_prefix
    ]
    subprocess.run(cmd_png, check=True)
    rendered_png = f"{tmp_prefix}-1.png"
    if os.path.exists(rendered_png):
        if os.path.exists(png_path):
            os.remove(png_path)
        os.rename(rendered_png, png_path)
        print(f"Generated PNG: {png_path}")

    cmd_jpg = [
        "pdftoppm",
        "-jpeg",
        "-r", "150",
        pdf_path,
        tmp_prefix
    ]
    subprocess.run(cmd_jpg, check=True)
    rendered_jpg = f"{tmp_prefix}-1.jpg"
    if os.path.exists(rendered_jpg):
        if os.path.exists(jpg_path):
            os.remove(jpg_path)
        os.rename(rendered_jpg, jpg_path)
        print(f"Generated JPG: {jpg_path}")

if __name__ == "__main__":
    print("=== Generating Empirical Validation Matrix Infographic ===")
    svg_content = create_svg()
    export_file("uwe_empirical_validation_matrix", svg_content)
