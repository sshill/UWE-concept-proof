#!/usr/bin/env python3
import os
import subprocess

def create_compact_svg():
    W = 2400
    H = 880  # Optimized canvas: minimal padding, maximum text fill

    # Column x and widths (Total width = 2350, left margin = 25)
    # Col 0: TIER (120)
    # Col 1: LOGISTICAL CATEGORY (360)
    # Col 2: AIR (UAV / UCV) (375)
    # Col 3: GROUND (UGV) (370)
    # Col 4: MARITIME (USV) (380)
    # Col 5: SUB-SURFACE (UUV) (370)
    # Col 6: SPACE (UOV) (375)
    col_x = [25, 145, 505, 880, 1250, 1630, 2000]
    col_w = [120, 360, 375, 370, 380, 370, 375]
    
    headers = [
        "TIER",
        "LOGISTICAL CATEGORY",
        "AIR (UAV / UCV)",
        "GROUND (UGV)",
        "MARITIME (USV)",
        "SUB-SURFACE (UUV)",
        "SPACE (UOV)"
    ]
    
    domain_icons = ["⚙️", "📦", "✈️", "🚜", "🚤", "⚓", "🛰️"]

    rows_data = [
        (
            "C-0", "H", "#00f5d4", "#032621",
            [
                ("Handheld / Pocket", "Micro-Canister [H]"),
                ("Pocket micro-copter", "Black Hornet, tube"),
                ("Micro scout crawler", "in soldier pouch"),
                ("Inflatable micro-buoy", "fairway marker"),
                ("Diver sonar beacon", "micro-transponder"),
                ("ChipSat /", "Picosat 0.1U")
            ]
        ),
        (
            "C-1", "B", "#38bdf8", "#062236",
            [
                ("Crew-Served /", "Backpack [B]"),
                ("Operator backpack,", "pneumatic rail"),
                ("Squad litter,", "combat EOD crawler"),
                ("Small tactical RIB,", "commando inflatable"),
                ("Torpedo-tube launch", "(324 mm man-portable)"),
                ("CubeSat 1U–12U", "dispenser")
            ]
        ),
        (
            "C-2", "L", "#fbbf24", "#291d05",
            [
                ("Tactical Mobility /", "Light Carrier [L]"),
                ("Pickup rail launch,", "ATV tube cluster"),
                ("Light buggy trailer,", "pickup bed carrier"),
                ("4x4 trailer slipway,", "beach surf launch"),
                ("Davit crane on cutter,", "towed sonar cradle"),
                ("ESPA Ring,", "Rideshare")
            ]
        ),
        (
            "C-3", "T", "#fb923c", "#2d1606",
            [
                ("Operational Mobile /", "Heavy Container [T]"),
                ("6x6 Heavy truck,", "sealed launch canister"),
                ("Heavy lowboy trailer,", "armored recovery bay"),
                ("20-ft ISO container,", "stern launch slipway"),
                ("533 mm Torpedo Tube,", "deep mine canister"),
                ("Dedicated", "Falcon 9 FEU")
            ]
        ),
        (
            "C-4", "I", "#f43f5e", "#2e0912",
            [
                ("Strategic Fixed", "Infrastructure [I]"),
                ("Hardened runway, hangar,", "arresting cables"),
                ("Railhead ramp, arsenal,", "static repair bunker"),
                ("Naval base, drydock,", "shore boathouse, slipway"),
                ("Submarine pen, deep", "subsea cable terminal"),
                ("Fixed launch pad / silo,", "spaceport")
            ]
        )
    ]

    table_top = 142
    hdr_h = 56
    row_h = 98
    row_gap = 6

    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#040811"/>
      <stop offset="50%" stop-color="#06111f"/>
      <stop offset="100%" stop-color="#091629"/>
    </linearGradient>
    <linearGradient id="hdrGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f223d"/>
      <stop offset="100%" stop-color="#081426"/>
    </linearGradient>
    <linearGradient id="accentCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="50%" stop-color="#00b4d8"/>
      <stop offset="100%" stop-color="#0077b6"/>
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

  <!-- Canvas Background -->
  <rect width="{W}" height="{H}" fill="url(#bgGrad)"/>
  <rect width="{W}" height="{H}" fill="url(#tacticalGrid)"/>
  <rect x="0" y="0" width="{W}" height="5" fill="url(#accentCyan)"/>

  <!-- ==================== HEADER (ENLARGED) ==================== -->
  <g transform="translate(25, 24)">
    <rect x="0" y="0" width="240" height="26" rx="5" fill="#0c2340" stroke="#00a8e8" stroke-width="1.2"/>
    <text x="120" y="18" fill="#00f5d4" class="font-sans" font-size="13" font-weight="700" letter-spacing="1.8" text-anchor="middle">MILTECH ARCHITECTURE</text>
    
    <text x="0" y="62" fill="#ffffff" class="font-sans" font-size="34" font-weight="900" letter-spacing="0.5">THE UNIVERSAL UWE CONTAINERIZATION CONTINUUM</text>
    <text x="0" y="94" fill="#94a3b8" class="font-sans" font-size="19">
      Cross-Domain Logistical Footprint &amp; Deployment Regimes (<tspan fill="#00f5d4" font-weight="700">C0 to C4</tspan> across Space, Air, Ground, Maritime &amp; Subsea)
    </text>

    <!-- Top Right Doctrinal Box -->
    <g transform="translate(1780, 2)">
      <rect x="0" y="0" width="570" height="96" rx="7" fill="#09182a" stroke="#1d385c" stroke-width="1.3"/>
      <text x="20" y="28" fill="#38bdf8" class="font-sans" font-size="15" font-weight="700" letter-spacing="0.8">UWE DOCTRINAL INVARIANT LAW II</text>
      <text x="20" y="54" fill="#cbd5e1" class="font-sans" font-size="15.5">"Logistical friction scales from soldier pocket to strategic base."</text>
      <text x="20" y="80" fill="#94a3b8" class="font-sans" font-size="14.5">Runway (C4) ≡ Drydock (C4) ≡ Spaceport (C4) — Vulnerability Equivalence</text>
    </g>
  </g>
''')

    # ==================== TABLE HEADERS (ENLARGED) ====================
    svg.append(f'  <g transform="translate(0, {table_top})">')
    for i in range(7):
        x = col_x[i]
        w = col_w[i]
        title = headers[i]
        icon = domain_icons[i]
        svg.append(f'    <rect x="{x}" y="0" width="{w}" height="{hdr_h}" rx="6" fill="url(#hdrGrad)" stroke="#1a3556" stroke-width="1.2"/>')
        svg.append(f'    <line x1="{x+4}" y1="{hdr_h-2}" x2="{x+w-4}" y2="{hdr_h-2}" stroke="#00b4d8" stroke-width="2"/>')
        if i == 0:
            svg.append(f'    <text x="{x + w/2}" y="35" fill="#00f5d4" class="font-sans" font-size="18" font-weight="800" letter-spacing="1.5" text-anchor="middle">{title}</text>')
        else:
            svg.append(f'    <text x="{x + 16}" y="35" fill="#f8fafc" class="font-sans" font-size="17.5" font-weight="800" letter-spacing="0.3">{icon}  {title}</text>')
    svg.append('  </g>')

    # ==================== DATA ROWS (SIGNIFICANTLY ENLARGED FONTS) ====================
    curr_y = table_top + hdr_h + row_gap
    for r_idx, row in enumerate(rows_data):
        tier_id, char_code, accent_col, bg_tint, cells = row
        svg.append(f'\n  <!-- Row {tier_id} -->')
        svg.append(f'  <g transform="translate(0, {curr_y})">')
        
        # Col 0: TIER Pill
        w0 = col_w[0]
        x0 = col_x[0]
        svg.append(f'''    <rect x="{x0}" y="0" width="{w0}" height="{row_h}" rx="6" fill="{bg_tint}" stroke="{accent_col}" stroke-width="1.5"/>
    <g transform="translate({x0 + w0/2}, 36)">
      <rect x="-42" y="-18" width="84" height="36" rx="6" fill="#061322" stroke="{accent_col}" stroke-width="1.6"/>
      <text x="0" y="7" fill="{accent_col}" class="font-mono" font-size="22" font-weight="900" text-anchor="middle">{tier_id}</text>
    </g>
    <text x="{x0 + w0/2}" y="78" fill="#94a3b8" class="font-mono" font-size="15.5" font-weight="700" text-anchor="middle">[{char_code}]</text>''')

        # Remaining 6 columns
        for c_idx in range(6):
            c_num = c_idx + 1
            xc = col_x[c_num]
            wc = col_w[c_num]
            line1, line2 = cells[c_idx]
            svg.append(f'''    <rect x="{xc}" y="0" width="{wc}" height="{row_h}" rx="6" fill="#091424" stroke="#15263d" stroke-width="1.1"/>
    <line x1="{xc}" y1="8" x2="{xc}" y2="{row_h-8}" stroke="{accent_col}" stroke-width="3.5" stroke-linecap="round"/>
    <g transform="translate({xc + 18}, 0)">
      <text x="0" y="41" fill="#ffffff" class="font-sans" font-size="22" font-weight="700" letter-spacing="0.1">{line1}</text>
      <text x="0" y="74" fill="{accent_col}" class="font-sans" font-size="19" font-weight="500">{line2}</text>
    </g>''')

        svg.append('  </g>')
        curr_y += row_h + row_gap

    # ==================== BOTTOM ARCHITECTURAL STRIP (ENLARGED) ====================
    legend_y = curr_y + 10
    svg.append(f'''
  <!-- Bottom Doctrinal Takeaway Strip -->
  <g transform="translate(25, {legend_y})">
    <rect x="0" y="0" width="2350" height="84" rx="7" fill="#081422" stroke="#182f4e" stroke-width="1.2"/>
    
    <g transform="translate(24, 20)">
      <circle cx="12" cy="12" r="7" fill="#00f5d4"/>
      <text x="30" y="17" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="700">C-0 &amp; C-1 (Dispersed Squad Echelon):</text>
      <text x="30" y="44" fill="#94a3b8" class="font-sans" font-size="15">Zero base footprint, soldier-portable, immune to runway / port strikes. Instant tactical mass.</text>
    </g>

    <g transform="translate(810, 20)">
      <circle cx="12" cy="12" r="7" fill="#fbbf24"/>
      <text x="30" y="17" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="700">C-2 (Tactical Mobility / Light Carrier):</text>
      <text x="30" y="44" fill="#94a3b8" class="font-sans" font-size="15">4x4 trailer &amp; pickup launch from mudbanks &amp; beaches. Key driver of Black Sea naval victory.</text>
    </g>

    <g transform="translate(1620, 20)">
      <circle cx="12" cy="12" r="7" fill="#f43f5e"/>
      <text x="30" y="17" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="700">C-3 &amp; C-4 (Operational Container / Fixed Base):</text>
      <text x="30" y="44" fill="#94a3b8" class="font-sans" font-size="15">ISO TEU mobile logistics vs. high-vulnerability static runways, drydocks, and space launchpads.</text>
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
    <text x="308" y="18" fill="#94a3b8" class="font-sans" font-size="13.5">SECTION 5.1: THE UNIVERSAL CONTAINERIZATION CONTINUUM</text>
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
    print("=== Generating Compact Continuum Table with Enlarged Fonts ===")
    compact_svg = create_compact_svg()
    export_file("uwe_containerization_continuum_compact", compact_svg)
    # Also update the primary file for consistency
    export_file("uwe_containerization_continuum", compact_svg)
