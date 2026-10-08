import os
import subprocess

def create_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1720" width="2400" height="1720">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050911"/>
      <stop offset="35%" stop-color="#08111e"/>
      <stop offset="100%" stop-color="#0b1728"/>
    </linearGradient>

    <!-- Card Backgrounds -->
    <linearGradient id="cardBgCyan" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0b1d30" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#071321" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="cardBgEmerald" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#092420" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#051714" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="cardBgAmber" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#241d0e" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#141007" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="cardBgMagenta" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#261022" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#140812" stop-opacity="0.96"/>
    </linearGradient>

    <!-- Visual Box Inner Gradients -->
    <linearGradient id="vizBoxCyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#061626"/>
      <stop offset="100%" stop-color="#030b14"/>
    </linearGradient>
    <linearGradient id="vizBoxEmerald" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#041a17"/>
      <stop offset="100%" stop-color="#020d0c"/>
    </linearGradient>
    <linearGradient id="vizBoxAmber" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1c1407"/>
      <stop offset="100%" stop-color="#0d0a03"/>
    </linearGradient>
    <linearGradient id="vizBoxMagenta" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1a0918"/>
      <stop offset="100%" stop-color="#0c040b"/>
    </linearGradient>

    <!-- Accent Bars -->
    <linearGradient id="accentCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e5ff"/>
      <stop offset="100%" stop-color="#0077ff"/>
    </linearGradient>
    <linearGradient id="accentEmerald" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="100%" stop-color="#00a878"/>
    </linearGradient>
    <linearGradient id="accentAmber" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffb703"/>
      <stop offset="100%" stop-color="#fb8500"/>
    </linearGradient>
    <linearGradient id="accentMagenta" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f72585"/>
      <stop offset="100%" stop-color="#7209b7"/>
    </linearGradient>

    <!-- Radar Ray Gradient -->
    <linearGradient id="radarBeam" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffb703" stop-opacity="0.4"/>
      <stop offset="70%" stop-color="#fb8500" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#fb8500" stop-opacity="0.0"/>
    </linearGradient>

    <!-- Water Density Gradient (Marine to Fresh) -->
    <linearGradient id="salinityGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0369a1" stop-opacity="0.85"/>
      <stop offset="55%" stop-color="#0d9488" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#15803d" stop-opacity="0.65"/>
    </linearGradient>

    <!-- Froude Curve Gradient -->
    <linearGradient id="froudeCurveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4cc9f0"/>
      <stop offset="45%" stop-color="#f72585"/>
      <stop offset="100%" stop-color="#ff0054"/>
    </linearGradient>

    <!-- Tactical Grid Pattern -->
    <pattern id="tacticalGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#162b45" stroke-width="0.6" stroke-opacity="0.3"/>
      <circle cx="40" cy="40" r="1.2" fill="#00d2ff" fill-opacity="0.18"/>
    </pattern>
  </defs>

  <style>
    .font-sans { font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Consolas', 'Roboto Mono', 'Courier New', monospace; }
  </style>

  <!-- Base Canvas Background -->
  <rect width="2400" height="1720" fill="url(#bgGrad)"/>
  <rect width="2400" height="1720" fill="url(#tacticalGrid)"/>

  <!-- Top Accent Neon Bar -->
  <rect x="0" y="0" width="2400" height="7" fill="url(#accentCyan)"/>

  <!-- ========================================================================= -->
  <!-- HEADER SECTION                                                            -->
  <!-- ========================================================================= -->
  <g transform="translate(70, 44)">
    <!-- Top Pill / Architecture Tag -->
    <rect x="0" y="0" width="390" height="32" rx="6" fill="#002b4d" stroke="#00a8e8" stroke-width="1.3"/>
    <text x="195" y="21" fill="#00e5ff" class="font-sans" font-size="13.5" font-weight="700" letter-spacing="2" text-anchor="middle">
      UWE AUTONOMOUS C2 &amp; TACTICAL PATHFINDING
    </text>

    <!-- Main Title -->
    <text x="0" y="74" fill="#ffffff" class="font-sans" font-size="40" font-weight="900" letter-spacing="0.5">
      THE 4-DIMENSIONAL ENVIRONMENTAL COST TENSOR
    </text>

    <!-- Subtitle -->
    <text x="0" y="112" fill="#94a3b8" class="font-sans" font-size="19">
      Ocean Multi-Physics, Bathymetry &amp; Tactical Radar Masking for Autonomous USVs:
    </text>

    <!-- Core Formula Widget -->
    <g transform="translate(1120, 80)">
      <rect x="0" y="0" width="1210" height="42" rx="8" fill="#0b1728" stroke="#1e3a5f" stroke-width="1.3"/>
      <text x="18" y="27" fill="#64748b" class="font-mono" font-size="13.5" font-weight="bold">OPTIMIZATION FORMULA :</text>
      
      <text x="215" y="27" fill="#e2e8f0" class="font-mono" font-size="15.5" font-weight="bold">
        min J = ∫ [
        <tspan fill="#00e5ff" font-weight="bold"> w₁·S_slamming </tspan> + 
        <tspan fill="#00f5d4" font-weight="bold"> w₂·B_draft </tspan> + 
        <tspan fill="#ffb703" font-weight="bold"> w₃·R_masking </tspan> + 
        <tspan fill="#f72585" font-weight="bold"> w₄·E_froude </tspan>
        ] dt
      </text>

      <rect x="1060" y="7" width="138" height="28" rx="5" fill="#003459" stroke="#00a8e8" stroke-width="1.2"/>
      <text x="1129" y="26" fill="#00e5ff" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">REAL-TIME 100Hz</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- QUADRANT 1: DYNAMIC WAVE SLAMMING TENSOR (Top-Left)                      -->
  <!-- ========================================================================= -->
  <g transform="translate(70, 190)">
    <!-- Card Outer Frame (width 1110, height 670) -->
    <rect width="1110" height="670" rx="14" fill="url(#cardBgCyan)" stroke="#1a3d66" stroke-width="2"/>
    <rect x="0" y="0" width="1110" height="58" rx="14" fill="#0a223a" stroke="#00a8e8" stroke-width="1.3"/>
    <path d="M 0 42 L 0 58 L 1110 58 L 1110 42 Z" fill="#0a223a"/>

    <!-- Header Content -->
    <rect x="18" y="12" width="125" height="34" rx="6" fill="#00e5ff" fill-opacity="0.18" stroke="#00e5ff" stroke-width="1.5"/>
    <text x="80" y="35" fill="#00e5ff" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">TENSOR 01</text>
    <text x="160" y="37" fill="#ffffff" class="font-sans" font-size="21" font-weight="bold" letter-spacing="0.5">
      1. DYNAMIC WAVE SLAMMING TENSOR
    </text>
    <text x="615" y="37" fill="#00e5ff" class="font-mono" font-size="19" font-weight="bold">(S_slamming)</text>

    <!-- ============ LEFT: GRAPHIC SCHEMATIC (525 x 580) ============ -->
    <g transform="translate(20, 72)">
      <!-- Visual Display Box -->
      <rect width="525" height="575" rx="10" fill="url(#vizBoxCyan)" stroke="#133352" stroke-width="1.2"/>
      
      <!-- Sub-headers -->
      <text x="18" y="30" fill="#00e5ff" class="font-mono" font-size="12.5" font-weight="bold">PHYSICS: WAVE SLAMMING &amp; DIAGONAL TACKING</text>
      <text x="508" y="30" fill="#64748b" class="font-mono" font-size="12" text-anchor="end">SEA STATE 4–5 (Hs = 2.5m)</text>

      <!-- Wave Train Crests -->
      <g opacity="0.85">
        <path d="M 25 125 Q 85 105, 145 125 T 265 125 T 385 125 T 495 125" fill="none" stroke="#0077b6" stroke-width="4"/>
        <path d="M 25 127 Q 85 107, 145 127 T 265 127 T 385 127 T 495 127" fill="none" stroke="#00e5ff" stroke-width="1.8" stroke-opacity="0.85"/>

        <path d="M 25 215 Q 85 195, 145 215 T 265 215 T 385 215 T 495 215" fill="none" stroke="#0077b6" stroke-width="4"/>
        <path d="M 25 217 Q 85 197, 145 217 T 265 217 T 385 217 T 495 217" fill="none" stroke="#00e5ff" stroke-width="1.8" stroke-opacity="0.85"/>

        <path d="M 25 305 Q 85 285, 145 305 T 265 305 T 385 305 T 495 305" fill="none" stroke="#0077b6" stroke-width="4"/>
        <path d="M 25 307 Q 85 287, 145 307 T 265 307 T 385 307 T 495 307" fill="none" stroke="#00e5ff" stroke-width="1.8" stroke-opacity="0.85"/>

        <path d="M 25 395 Q 85 375, 145 395 T 265 395 T 385 395 T 495 395" fill="none" stroke="#0077b6" stroke-width="4"/>
        <path d="M 25 397 Q 85 377, 145 397 T 265 397 T 385 397 T 495 397" fill="none" stroke="#00e5ff" stroke-width="1.8" stroke-opacity="0.85"/>
      </g>

      <!-- Wave Direction Indicator on far right edge -->
      <g transform="translate(490, 160)">
        <line x1="0" y1="0" x2="0" y2="180" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5 3"/>
        <polygon points="-6,180 6,180 0,195" fill="#38bdf8"/>
        <text x="-14" y="95" fill="#38bdf8" class="font-mono" font-size="11.5" font-weight="bold" transform="rotate(-90 -14,95)" text-anchor="middle">SWELL ADVANCE</text>
      </g>

      <!-- BAD PATH: Direct Head-on Slamming (Red Dashed Line) -->
      <g>
        <line x1="125" y1="475" x2="125" y2="85" stroke="#ef4444" stroke-width="3.5" stroke-dasharray="7 5"/>
        <polygon points="118,85 132,85 125,70" fill="#ef4444"/>
        <polygon points="125,350 116,376 134,376" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.6"/>
        
        <rect x="25" y="265" width="200" height="54" rx="6" fill="#3f0f15" stroke="#ef4444" stroke-width="1.4"/>
        <text x="125" y="287" fill="#fca5a5" class="font-sans" font-size="13" font-weight="bold" text-anchor="middle">HEAD-ON SLAMMING</text>
        <text x="125" y="307" fill="#f87171" class="font-mono" font-size="13.5" font-weight="bold" text-anchor="middle">G_z &gt; 8.5g (DELAMINATION)</text>
      </g>

      <!-- GOOD PATH: Autonomous Diagonal Zigzag Tacking (Cyan Solid Line) -->
      <g>
        <polyline points="250,480 365,360 245,230 375,100" fill="none" stroke="#00e5ff" stroke-width="4"/>
        <polygon points="368,92 388,104 378,118" fill="#00e5ff"/>
        
        <path d="M 250,480 L 250,390 A 90 90 0 0 1 325,405" fill="none" stroke="#ffb703" stroke-width="1.8" stroke-dasharray="4 3"/>
        <text x="290" y="424" fill="#ffb703" class="font-mono" font-size="15" font-weight="bold">θ ≈ 38°</text>

        <!-- USV Hull Models on Cyan Track -->
        <g transform="translate(308, 420) rotate(-40)">
          <polygon points="0,-18 -7,12 7,12" fill="#00e5ff" stroke="#ffffff" stroke-width="1.6"/>
        </g>
        <g transform="translate(305, 295) rotate(42)">
          <polygon points="0,-18 -7,12 7,12" fill="#00e5ff" stroke="#ffffff" stroke-width="1.6"/>
        </g>
        <g transform="translate(310, 165) rotate(-40)">
          <polygon points="0,-18 -7,12 7,12" fill="#00e5ff" stroke="#ffffff" stroke-width="1.6"/>
        </g>

        <!-- Success Callout Box -->
        <rect x="235" y="200" width="245" height="54" rx="6" fill="#003459" stroke="#00e5ff" stroke-width="1.5"/>
        <text x="357" y="222" fill="#67e8f9" class="font-sans" font-size="13.5" font-weight="bold" text-anchor="middle">OPTIMAL DIAGONAL TACKING</text>
        <text x="357" y="243" fill="#38bdf8" class="font-mono" font-size="14" font-weight="bold" text-anchor="middle">G_z ≤ 3.5g (HULL PRESERVED)</text>
      </g>

      <!-- Telemetry Bottom Bar inside Viz -->
      <g transform="translate(15, 508)">
        <rect width="495" height="50" rx="7" fill="#051c2f" stroke="#0d4670" stroke-width="1.2"/>
        <circle cx="28" cy="25" r="7" fill="#00e5ff"/>
        <text x="45" y="31" fill="#ffffff" class="font-sans" font-size="14" font-weight="bold">FEEDBACK LOOP:</text>
        <text x="170" y="31" fill="#7dd3fc" class="font-mono" font-size="14">Orbital Altimetry (SWOT/Jason) + 100Hz 6-DOF IMU</text>
      </g>
    </g>

    <!-- ============ RIGHT: TECHNICAL SPECS & BULLETS (535 x 580) ============ -->
    <g transform="translate(560, 72)">
      <!-- Formula Pill -->
      <rect width="530" height="46" rx="7" fill="#092036" stroke="#174978" stroke-width="1.2"/>
      <text x="20" y="29" fill="#38bdf8" class="font-mono" font-size="15" font-weight="bold">
        FORMULA: S_slamming = f(Hs, λ_wave, v_USV · k_wave, d²z/dt²)
      </text>

      <!-- Item 1 -->
      <g transform="translate(0, 58)">
        <rect width="530" height="114" rx="8" fill="#071828" stroke="#12385c" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#003459" stroke="#00e5ff" stroke-width="1.4"/>
        <text x="30" y="35" fill="#00e5ff" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">01</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Satellite Altimetry &amp; IMU Ingestion</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Continuous ingestion of orbital SAR wave altimetry data
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          fused with onboard 100 Hz 6-axis inertial sensors.
        </text>
      </g>

      <!-- Item 2 -->
      <g transform="translate(0, 184)">
        <rect width="530" height="114" rx="8" fill="#071828" stroke="#12385c" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#003459" stroke="#00e5ff" stroke-width="1.4"/>
        <text x="30" y="35" fill="#00e5ff" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">02</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Vertical G-Force Acceleration Clamping</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Restricts vertical shock: <tspan fill="#00e5ff" font-weight="bold"> G_z ≤ 3.5 – 4.0 g </tspan>. Eliminates
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          carbon-Kevlar delamination and shaft misalignment.
        </text>
      </g>

      <!-- Item 3 -->
      <g transform="translate(0, 310)">
        <rect width="530" height="114" rx="8" fill="#071828" stroke="#12385c" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#003459" stroke="#00e5ff" stroke-width="1.4"/>
        <text x="30" y="35" fill="#00e5ff" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">03</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Wave-Train Diagonal Tacking Trajectory</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Tacks diagonally across wave trains at 35°–45°,
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          turning violent slamming into controlled rolling heave.
        </text>
      </g>

      <!-- Tactical Value Banner -->
      <g transform="translate(0, 436)">
        <rect width="530" height="135" rx="8" fill="#032541" stroke="#00a8e8" stroke-width="1.4" stroke-dasharray="5 4"/>
        <text x="22" y="32" fill="#00e5ff" class="font-sans" font-size="15.5" font-weight="bold" letter-spacing="1">
          OPERATIONAL PAYOFF: HIGH-SEA COMBAT SURVIVAL
        </text>
        <text x="22" y="62" fill="#f1f5f9" class="font-sans" font-size="15.5">
          Sustains combat transit in Sea State 4+ where crewed craft
        </text>
        <text x="22" y="88" fill="#f1f5f9" class="font-sans" font-size="15.5">
          suffer incapacitating fatigue and unguided autopilots
        </text>
        <text x="22" y="114" fill="#38bdf8" class="font-sans" font-size="15.5" font-weight="bold">
          suffer catastrophic structural delamination.
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- QUADRANT 2: BATHYMETRIC DENSITY & BUOYANCY MATRIX (Top-Right)             -->
  <!-- ========================================================================= -->
  <g transform="translate(1220, 190)">
    <!-- Card Outer Frame -->
    <rect width="1110" height="670" rx="14" fill="url(#cardBgEmerald)" stroke="#114b40" stroke-width="2"/>
    <rect x="0" y="0" width="1110" height="58" rx="14" fill="#092923" stroke="#00f5d4" stroke-width="1.3"/>
    <path d="M 0 42 L 0 58 L 1110 58 L 1110 42 Z" fill="#092923"/>

    <!-- Header Content -->
    <rect x="18" y="12" width="125" height="34" rx="6" fill="#00f5d4" fill-opacity="0.18" stroke="#00f5d4" stroke-width="1.5"/>
    <text x="80" y="35" fill="#00f5d4" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">TENSOR 02</text>
    <text x="160" y="37" fill="#ffffff" class="font-sans" font-size="21" font-weight="bold" letter-spacing="0.5">
      2. BATHYMETRIC DENSITY &amp; BUOYANCY MATRIX
    </text>
    <text x="670" y="37" fill="#00f5d4" class="font-mono" font-size="19" font-weight="bold">(B_draft)</text>

    <!-- ============ LEFT: GRAPHIC SCHEMATIC (525 x 580) ============ -->
    <g transform="translate(20, 72)">
      <!-- Visual Display Box -->
      <rect width="525" height="575" rx="10" fill="url(#vizBoxEmerald)" stroke="#13473e" stroke-width="1.2"/>

      <text x="18" y="30" fill="#00f5d4" class="font-mono" font-size="12.5" font-weight="bold">HYDROSTATICS: SALINITY &amp; SHOAL ROUTING</text>
      <text x="508" y="30" fill="#64748b" class="font-mono" font-size="12" text-anchor="end">ESTUARY (0–35 PSU)</text>

      <!-- Salinity & Bathymetry Schematic -->
      <g transform="translate(18, 50)">
        <!-- Top Salinity Labels -->
        <rect x="0" y="0" width="220" height="26" rx="4" fill="#032b45" stroke="#0284c7" stroke-width="1.2"/>
        <text x="110" y="18" fill="#38bdf8" class="font-mono" font-size="12.5" font-weight="bold" text-anchor="middle">
          BASIN: 35 PSU (ρ=1.025)
        </text>

        <rect x="268" y="0" width="220" height="26" rx="4" fill="#063e26" stroke="#059669" stroke-width="1.2"/>
        <text x="378" y="18" fill="#4ade80" class="font-mono" font-size="12.5" font-weight="bold" text-anchor="middle">
          ESTUARY: 0 PSU (-2.5% LIFT)
        </text>

        <!-- Water Body Rect -->
        <rect x="0" y="34" width="488" height="275" rx="6" fill="url(#salinityGrad)"/>
        
        <!-- Depth Scale Markers on Left Edge -->
        <line x1="0" y1="75" x2="488" y2="75" stroke="#ffffff" stroke-opacity="0.15" stroke-dasharray="4 4"/>
        <text x="10" y="70" fill="#e2e8f0" class="font-mono" font-size="12" font-weight="bold">DEPTH: 1.0m</text>
        
        <line x1="0" y1="130" x2="488" y2="130" stroke="#ffffff" stroke-opacity="0.15" stroke-dasharray="4 4"/>
        <text x="10" y="125" fill="#e2e8f0" class="font-mono" font-size="12" font-weight="bold">SHOAL: 2.2m</text>
        
        <line x1="0" y1="215" x2="488" y2="215" stroke="#ffffff" stroke-opacity="0.15" stroke-dasharray="4 4"/>
        <text x="10" y="210" fill="#e2e8f0" class="font-mono" font-size="12" font-weight="bold">DRAFT: 5.8m</text>

        <!-- Seabed Profile -->
        <path d="M 0 285 Q 140 270, 220 150 T 360 110 Q 425 130, 488 95 L 488 309 L 0 309 Z" fill="#1c1917" stroke="#78716c" stroke-width="2"/>
        
        <!-- Sandbar / Shoal Label -->
        <rect x="245" y="152" width="170" height="28" rx="4" fill="#292524" stroke="#a8a29e" stroke-width="1.2"/>
        <text x="330" y="171" fill="#facc15" class="font-mono" font-size="12.5" font-weight="bold" text-anchor="middle">SHALLOW SHOAL: 1.8m</text>

        <!-- USV Model Crossing Shoal (Draft = 0.75m) -->
        <g transform="translate(360, 48)">
          <polygon points="-26,0 20,0 28,-9 -26,-9" fill="#00f5d4" stroke="#ffffff" stroke-width="1.8"/>
          <rect x="-9" y="-18" width="18" height="9" rx="2" fill="#092923" stroke="#00f5d4" stroke-width="1.2"/>
          <line x1="0" y1="0" x2="0" y2="28" stroke="#00f5d4" stroke-width="2.5"/>
          <line x1="-8" y1="28" x2="8" y2="28" stroke="#00f5d4" stroke-width="2.5"/>
          <rect x="-55" y="34" width="110" height="22" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="1.2"/>
          <text x="0" y="50" fill="#34d399" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">CLEARANCE: +1.0m</text>
        </g>

        <!-- ENEMY FRIGATE Model Blocked by Shoal (Lowered to y=65 to avoid basin label) -->
        <g transform="translate(135, 68)">
          <polygon points="-55,0 55,0 75,-22 -55,-22" fill="#475569" stroke="#94a3b8" stroke-width="1.8"/>
          <rect x="-26" y="-38" width="36" height="16" rx="2" fill="#334155" stroke="#94a3b8" stroke-width="1.2"/>
          <line x1="0" y1="-38" x2="0" y2="-52" stroke="#94a3b8" stroke-width="2.2"/>
          <line x1="12" y1="0" x2="12" y2="125" stroke="#ef4444" stroke-width="3" stroke-dasharray="5 3"/>
          <line x1="-8" y1="125" x2="30" y2="125" stroke="#ef4444" stroke-width="3"/>
          
          <rect x="-65" y="132" width="155" height="34" rx="4" fill="#450a0a" stroke="#ef4444" stroke-width="1.3"/>
          <text x="12" y="148" fill="#fca5a5" class="font-sans" font-size="12" font-weight="bold" text-anchor="middle">ENEMY FRIGATE (5.8m)</text>
          <text x="12" y="161" fill="#ef4444" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">GROUNDING BARRIER</text>
        </g>
      </g>

      <!-- Buoyancy Mathematical Note inside visual box -->
      <g transform="translate(18, 395)">
        <rect width="488" height="98" rx="7" fill="#04201a" stroke="#0e6553" stroke-width="1.2"/>
        <text x="18" y="27" fill="#00f5d4" class="font-sans" font-size="14.5" font-weight="bold">BUOYANCY &amp; SINKAGE RE-CALCULATION:</text>
        <text x="18" y="54" fill="#e2e8f0" class="font-mono" font-size="14">
          Δ Lift = (ρ_estuary - ρ_marine)/ρ_marine = (1000 - 1025)/1025 ≈ <tspan fill="#facc15" font-weight="bold"> -2.44% </tspan>
        </text>
        <text x="18" y="80" fill="#a7f3d0" class="font-sans" font-size="13.5">
          USV draft increases +3.2cm in fresh water — tensor guarantees safe keel clearance.
        </text>
      </g>

      <!-- Bottom Status Pill -->
      <g transform="translate(18, 508)">
        <rect width="488" height="50" rx="7" fill="#062e26" stroke="#059669" stroke-width="1.2"/>
        <text x="244" y="31" fill="#34d399" class="font-mono" font-size="14.5" font-weight="bold" text-anchor="middle">
          ASYMMETRIC LITTORAL SANCTUARY: NAVIGATION VERIFIED
        </text>
      </g>
    </g>

    <!-- ============ RIGHT: TECHNICAL SPECS & BULLETS (535 x 580) ============ -->
    <g transform="translate(560, 72)">
      <!-- Formula Pill -->
      <rect width="530" height="46" rx="7" fill="#062822" stroke="#105e4f" stroke-width="1.2"/>
      <text x="20" y="29" fill="#34d399" class="font-mono" font-size="15" font-weight="bold">
        FORMULA: B_draft = m_USV / [ ρ(Salinity, Temp) · ∇_hull ]
      </text>

      <!-- Item 1 -->
      <g transform="translate(0, 58)">
        <rect width="530" height="114" rx="8" fill="#051c17" stroke="#0e473b" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#064e3b" stroke="#00f5d4" stroke-width="1.4"/>
        <text x="30" y="35" fill="#00f5d4" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">01</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Salinity Drop &amp; Lift Loss Compensation</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Accounts for steep density drops from marine basins (35 PSU)
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          to estuaries (0 PSU), anticipating <tspan fill="#00f5d4" font-weight="bold"> -2.5% buoyancy drop </tspan>.
        </text>
      </g>

      <!-- Item 2 -->
      <g transform="translate(0, 184)">
        <rect width="530" height="114" rx="8" fill="#051c17" stroke="#0e473b" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#064e3b" stroke="#00f5d4" stroke-width="1.4"/>
        <text x="30" y="35" fill="#00f5d4" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">02</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Dynamic Keel Clearance &amp; Tidal Fusion</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Cross-references bathymetric charts with live astronomical tide
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          and dynamic wave drawdown for safe under-keel margin.
        </text>
      </g>

      <!-- Item 3 -->
      <g transform="translate(0, 310)">
        <rect width="530" height="114" rx="8" fill="#051c17" stroke="#0e473b" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#064e3b" stroke="#00f5d4" stroke-width="1.4"/>
        <text x="30" y="35" fill="#00f5d4" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">03</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Shoal Routing Asymmetry vs Capital Ships</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Routes heavily armed strike USVs through 1.2–2.0 m shallows
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          and sandbars completely impassable to deep-draft frigates.
        </text>
      </g>

      <!-- Tactical Value Banner -->
      <g transform="translate(0, 436)">
        <rect width="530" height="135" rx="8" fill="#043229" stroke="#00f5d4" stroke-width="1.4" stroke-dasharray="5 4"/>
        <text x="22" y="32" fill="#00f5d4" class="font-sans" font-size="15.5" font-weight="bold" letter-spacing="1">
          OPERATIONAL PAYOFF: ASYMMETRIC LITTORAL DOMINANCE
        </text>
        <text x="22" y="62" fill="#f1f5f9" class="font-sans" font-size="15.5">
          Transforms shallow coastal barriers into lethal strike corridors.
        </text>
        <text x="22" y="88" fill="#f1f5f9" class="font-sans" font-size="15.5">
          USVs bypass blue-water pickets and infiltrate vectors
        </text>
        <text x="22" y="114" fill="#34d399" class="font-sans" font-size="15.5" font-weight="bold">
          where major surface combatants cannot enter or defend.
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- QUADRANT 3: RADAR HORIZON & CLUTTER MASKING (Bottom-Left)                 -->
  <!-- ========================================================================= -->
  <g transform="translate(70, 890)">
    <!-- Card Outer Frame -->
    <rect width="1110" height="670" rx="14" fill="url(#cardBgAmber)" stroke="#523912" stroke-width="2"/>
    <rect x="0" y="0" width="1110" height="58" rx="14" fill="#332208" stroke="#ffb703" stroke-width="1.3"/>
    <path d="M 0 42 L 0 58 L 1110 58 L 1110 42 Z" fill="#332208"/>

    <!-- Header Content -->
    <rect x="18" y="12" width="125" height="34" rx="6" fill="#ffb703" fill-opacity="0.18" stroke="#ffb703" stroke-width="1.5"/>
    <text x="80" y="35" fill="#ffb703" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">TENSOR 03</text>
    <text x="160" y="37" fill="#ffffff" class="font-sans" font-size="21" font-weight="bold" letter-spacing="0.5">
      3. RADAR HORIZON &amp; CLUTTER MASKING
    </text>
    <text x="615" y="37" fill="#ffb703" class="font-mono" font-size="19" font-weight="bold">(R_masking)</text>

    <!-- ============ LEFT: GRAPHIC SCHEMATIC (525 x 580) ============ -->
    <g transform="translate(20, 72)">
      <!-- Visual Display Box -->
      <rect width="525" height="575" rx="10" fill="url(#vizBoxAmber)" stroke="#4d320a" stroke-width="1.2"/>

      <text x="18" y="30" fill="#ffb703" class="font-mono" font-size="12.5" font-weight="bold">EW MODEL: HORIZON GEOMETRY &amp; CLUTTER MASKING</text>
      <text x="508" y="30" fill="#64748b" class="font-mono" font-size="12" text-anchor="end">EMCON DOMAIN</text>

      <!-- Schematic Cross-Section -->
      <g transform="translate(15, 50)">
        <!-- Earth Curved Sea Surface Arc -->
        <path d="M 0 310 Q 240 280, 495 310 L 495 390 L 0 390 Z" fill="#081b2c" stroke="#1e3a5f" stroke-width="1.6"/>
        <text x="247" y="355" fill="#64748b" class="font-mono" font-size="12.5" font-weight="bold" text-anchor="middle">CURVED SEA SURFACE (R = 6,371 km)</text>

        <!-- Coastal Mountain/Cliff -->
        <path d="M 0 160 L 60 160 L 90 310 L 0 310 Z" fill="#292524" stroke="#57534e" stroke-width="1.6"/>
        <!-- Radar Tower on Cliff -->
        <line x1="45" y1="160" x2="45" y2="80" stroke="#f59e0b" stroke-width="3.5"/>
        <circle cx="45" cy="75" r="8" fill="#78350f" stroke="#fbbf24" stroke-width="2.2"/>
        <path d="M 37 67 A 11 11 0 0 1 53 67" fill="none" stroke="#fbbf24" stroke-width="2.2"/>
        <text x="45" y="58" fill="#fcd34d" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">COASTAL RADAR (h=45m)</text>

        <!-- Radar Beam Emission Cone -->
        <polygon points="45,75 495,125 495,265 200,290" fill="url(#radarBeam)"/>

        <!-- Radar Line-of-Sight Horizon Line -->
        <line x1="45" y1="75" x2="215" y2="292" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6 3"/>
        <circle cx="215" cy="292" r="5" fill="#ef4444"/>
        
        <!-- Horizon Callout clearly placed -->
        <g transform="translate(145, 238)">
          <rect width="145" height="26" rx="4" fill="#450a0a" stroke="#ef4444" stroke-width="1.2"/>
          <text x="72" y="18" fill="#fca5a5" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">RADAR HORIZON</text>
        </g>

        <!-- Atmospheric Ducting Layer -->
        <rect x="0" y="110" width="495" height="28" fill="#ffb703" fill-opacity="0.12" stroke="#ffb703" stroke-opacity="0.45" stroke-dasharray="5 3"/>
        <text x="247" y="129" fill="#fbbf24" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">
          ATMOSPHERIC DUCTING LAYER (TROPOSPHERIC WAVEGUIDE)
        </text>

        <!-- Radar Shadow Zone Label placed higher -->
        <g transform="translate(290, 175)">
          <rect width="190" height="28" rx="4" fill="#0c233c" stroke="#38bdf8" stroke-width="1.2"/>
          <text x="95" y="19" fill="#38bdf8" class="font-mono" font-size="12.5" font-weight="bold" text-anchor="middle">RADAR SHADOW ZONE</text>
        </g>

        <!-- Coastal Sea Clutter Noise Layer on Surface -->
        <g transform="translate(75, 270)">
          <path d="M 0 16 L 14 7 L 28 17 L 42 8 L 56 18 L 70 8 L 84 17 L 98 8 L 112 18 L 126 8 L 140 16" fill="none" stroke="#ffb703" stroke-width="2.2"/>
          <text x="70" y="35" fill="#fbbf24" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">
            COASTAL SEA CLUTTER (DOPPLER NOISE)
          </text>
        </g>

        <!-- Stealth USV Model in Horizon Shadow Zone -->
        <g transform="translate(385, 295)">
          <!-- Faceted Silhouette -->
          <polygon points="-28,5 18,5 28,-6 -24,-6" fill="#0f172a" stroke="#00e5ff" stroke-width="2.2"/>
          <polygon points="-12,-6 10,-6 5,-13 -7,-13" fill="#1e293b" stroke="#00e5ff" stroke-width="1.4"/>
          
          <!-- Low-RCS Tag above -->
          <rect x="-72" y="-38" width="144" height="24" rx="4" fill="#002b4d" stroke="#00e5ff" stroke-width="1.3"/>
          <text x="0" y="-22" fill="#00e5ff" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
            LOW-RCS USV (σ &lt; 0.01 m²)
          </text>
          
          <!-- Masked Status below -->
          <rect x="-78" y="16" width="156" height="24" rx="4" fill="#052e16" stroke="#22c55e" stroke-width="1.2"/>
          <text x="0" y="32" fill="#4ade80" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
            CLUTTER-MASKED (SNR &lt; NOISE)
          </text>
        </g>
      </g>

      <!-- Bottom Status Pill -->
      <g transform="translate(18, 508)">
        <rect width="488" height="50" rx="7" fill="#2d1c04" stroke="#d97706" stroke-width="1.2"/>
        <text x="244" y="31" fill="#fbbf24" class="font-mono" font-size="14.5" font-weight="bold" text-anchor="middle">
          RADAR DETECTION RANGE REDUCED BY UP TO 80%
        </text>
      </g>
    </g>

    <!-- ============ RIGHT: TECHNICAL SPECS & BULLETS (535 x 580) ============ -->
    <g transform="translate(560, 72)">
      <!-- Formula Pill -->
      <rect width="530" height="46" rx="7" fill="#2b1a04" stroke="#78470a" stroke-width="1.2"/>
      <text x="20" y="29" fill="#fbbf24" class="font-mono" font-size="15" font-weight="bold">
        FORMULA: R_masking = SNR_radar ∝ σ_RCS / [ R⁴ · σ⁰_clutter(θ, SS) ]
      </text>

      <!-- Item 1 -->
      <g transform="translate(0, 58)">
        <rect width="530" height="114" rx="8" fill="#1c1203" stroke="#4a2e06" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#451a03" stroke="#ffb703" stroke-width="1.4"/>
        <text x="30" y="35" fill="#ffb703" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">01</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Earth Curvature &amp; Evaporation Ducting</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Calculates enemy radar horizon based on antenna mast height,
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          Earth curvature, and tropospheric evaporation duct traps.
        </text>
      </g>

      <!-- Item 2 -->
      <g transform="translate(0, 184)">
        <rect width="530" height="114" rx="8" fill="#1c1203" stroke="#4a2e06" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#451a03" stroke="#ffb703" stroke-width="1.4"/>
        <text x="30" y="35" fill="#ffb703" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">02</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Coastal Sea-Chop Clutter Masking</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Hugs coastal wave chop and surf zones where chaotic radar
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          sea clutter completely swamps the <tspan fill="#ffb703" font-weight="bold"> low-RCS signature </tspan>.
        </text>
      </g>

      <!-- Item 3 -->
      <g transform="translate(0, 310)">
        <rect width="530" height="114" rx="8" fill="#1c1203" stroke="#4a2e06" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#451a03" stroke="#ffb703" stroke-width="1.4"/>
        <text x="30" y="35" fill="#ffb703" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">03</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Dynamic Knife-Edge Aspect Evasion</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Dynamically points stealth faceted hull aspects toward
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          active radar emitters, eliminating broadside reflection spikes.
        </text>
      </g>

      <!-- Tactical Value Banner -->
      <g transform="translate(0, 436)">
        <rect width="530" height="135" rx="8" fill="#381d03" stroke="#ffb703" stroke-width="1.4" stroke-dasharray="5 4"/>
        <text x="22" y="32" fill="#ffb703" class="font-sans" font-size="15.5" font-weight="bold" letter-spacing="1">
          OPERATIONAL PAYOFF: INVISIBLE COMBAT PENETRATION
        </text>
        <text x="22" y="62" fill="#f1f5f9" class="font-sans" font-size="15.5">
          Eliminates surface vehicle vulnerability to shore radar.
        </text>
        <text x="22" y="88" fill="#f1f5f9" class="font-sans" font-size="15.5">
          USVs penetrate high-threat A2/AD perimeters undetected
        </text>
        <text x="22" y="114" fill="#fcd34d" class="font-sans" font-size="15.5" font-weight="bold">
          until visual acquisition occurs inside the terminal kill-zone.
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- QUADRANT 4: FROUDE NUMBER HYDRODYNAMIC OPTIMIZATION (Bottom-Right)        -->
  <!-- ========================================================================= -->
  <g transform="translate(1220, 890)">
    <!-- Card Outer Frame -->
    <rect width="1110" height="670" rx="14" fill="url(#cardBgMagenta)" stroke="#5e144a" stroke-width="2"/>
    <rect x="0" y="0" width="1110" height="58" rx="14" fill="#3b0a2e" stroke="#f72585" stroke-width="1.3"/>
    <path d="M 0 42 L 0 58 L 1110 58 L 1110 42 Z" fill="#3b0a2e"/>

    <!-- Header Content -->
    <rect x="18" y="12" width="125" height="34" rx="6" fill="#f72585" fill-opacity="0.18" stroke="#f72585" stroke-width="1.5"/>
    <text x="80" y="35" fill="#f72585" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">TENSOR 04</text>
    <text x="160" y="37" fill="#ffffff" class="font-sans" font-size="21" font-weight="bold" letter-spacing="0.5">
      4. FROUDE HYDRODYNAMIC OPTIMIZATION
    </text>
    <text x="640" y="37" fill="#f72585" class="font-mono" font-size="19" font-weight="bold">(E_froude)</text>

    <!-- ============ LEFT: GRAPHIC SCHEMATIC (525 x 580) ============ -->
    <g transform="translate(20, 72)">
      <!-- Visual Display Box -->
      <rect width="525" height="575" rx="10" fill="url(#vizBoxMagenta)" stroke="#4d0f3e" stroke-width="1.2"/>

      <text x="18" y="30" fill="#f72585" class="font-mono" font-size="12.5" font-weight="bold">HYDRODYNAMICS: DUAL REGIME RESISTANCE</text>
      <text x="508" y="30" fill="#64748b" class="font-mono" font-size="12" text-anchor="end">RANGE VS VELOCITY</text>

      <!-- Resistance vs Froude Number Plot -->
      <g transform="translate(30, 48)">
        <!-- Axes -->
        <line x1="50" y1="265" x2="455" y2="265" stroke="#94a3b8" stroke-width="1.8"/>
        <line x1="50" y1="265" x2="50" y2="25" stroke="#94a3b8" stroke-width="1.8"/>
        <polygon points="455,261 465,265 455,269" fill="#94a3b8"/>
        <polygon points="46,25 50,15 54,25" fill="#94a3b8"/>
        
        <!-- Axis Labels -->
        <text x="450" y="286" fill="#94a3b8" class="font-mono" font-size="12" font-weight="bold">Fn (Froude)</text>
        <text x="50" y="14" fill="#94a3b8" class="font-mono" font-size="12" font-weight="bold">Specific Resistance (R / Δ)</text>

        <!-- Resistance Curve -->
        <path d="M 50 255 C 100 250, 130 210, 175 100 C 215 65, 255 120, 305 155 C 365 175, 415 185, 450 190" 
              fill="none" stroke="url(#froudeCurveGrad)" stroke-width="4"/>

        <!-- Phase 1 Shaded Area (Transit) -->
        <rect x="50" y="25" width="115" height="240" fill="#4cc9f0" fill-opacity="0.08"/>
        <line x1="165" y1="25" x2="165" y2="265" stroke="#4cc9f0" stroke-width="1.2" stroke-dasharray="4 3"/>
        <text x="107" y="48" fill="#4cc9f0" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">TRANSIT</text>
        <text x="107" y="66" fill="#38bdf8" class="font-mono" font-size="12" text-anchor="middle">Fn &lt; 1.0</text>
        <text x="107" y="83" fill="#cbd5e1" class="font-sans" font-size="11.5" text-anchor="middle">Displacement</text>

        <!-- Resistance Hump Barrier -->
        <rect x="165" y="25" width="125" height="240" fill="#ffb703" fill-opacity="0.08"/>
        <line x1="290" y1="25" x2="290" y2="265" stroke="#ffb703" stroke-width="1.2" stroke-dasharray="4 3"/>
        <text x="227" y="48" fill="#ffb703" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">HUMP BARRIER</text>
        <text x="227" y="66" fill="#f59e0b" class="font-mono" font-size="12" text-anchor="middle">1.0 &lt; Fn &lt; 2.5</text>
        <text x="227" y="83" fill="#cbd5e1" class="font-sans" font-size="11.5" text-anchor="middle">Severe Wave Drag</text>

        <!-- Phase 2 Shaded Area (Terminal Sprint) -->
        <rect x="290" y="25" width="165" height="240" fill="#f72585" fill-opacity="0.08"/>
        <text x="372" y="48" fill="#f72585" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">TERMINAL SPRINT</text>
        <text x="372" y="66" fill="#f43f5e" class="font-mono" font-size="12" text-anchor="middle">Fn &gt; 3.0</text>
        <text x="372" y="83" fill="#cbd5e1" class="font-sans" font-size="11.5" text-anchor="middle">Full Planing Sprint</text>

        <!-- Points on Curve -->
        <circle cx="95" cy="252" r="6" fill="#4cc9f0" stroke="#ffffff" stroke-width="1.8"/>
        <text x="95" y="238" fill="#4cc9f0" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">ECO CRUISE</text>

        <circle cx="410" cy="183" r="6" fill="#f72585" stroke="#ffffff" stroke-width="1.8"/>
        <text x="410" y="167" fill="#f72585" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">55+ KTS SPRINT</text>
      </g>

      <!-- Dual Profile Diagrams (Boats) -->
      <g transform="translate(20, 360)">
        <!-- Mode 1: Low-Speed Displacement Cruise -->
        <rect width="235" height="110" rx="7" fill="#140924" stroke="#4a1854" stroke-width="1.2"/>
        <text x="14" y="24" fill="#4cc9f0" class="font-mono" font-size="12" font-weight="bold">1. TRANSIT PHASE (Fn &lt; 1.0)</text>
        <line x1="15" y1="75" x2="220" y2="75" stroke="#0284c7" stroke-width="1.8"/>
        <polygon points="40,75 145,75 168,55 40,55" fill="#1e293b" stroke="#38bdf8" stroke-width="1.4"/>
        <text x="14" y="98" fill="#94a3b8" class="font-mono" font-size="11.5">800+ km Range • Minimal Wake</text>

        <!-- Mode 2: Terminal Sprint Wave-Piercing -->
        <g transform="translate(250, 0)">
          <rect width="235" height="110" rx="7" fill="#24071c" stroke="#66103e" stroke-width="1.2"/>
          <text x="14" y="24" fill="#f72585" class="font-mono" font-size="12" font-weight="bold">2. TERMINAL SPRINT (Fn &gt; 3.0)</text>
          <path d="M 15 78 Q 60 62, 120 82 T 220 74" fill="none" stroke="#f43f5e" stroke-width="1.8"/>
          <g transform="translate(52, 48) rotate(-14)">
            <polygon points="0,22 105,22 126,5 0,5" fill="#3f0f29" stroke="#f72585" stroke-width="1.4"/>
            <path d="M -6 20 L -38 13 L -6 27 Z" fill="#f72585" fill-opacity="0.6"/>
          </g>
          <text x="14" y="98" fill="#fca5a5" class="font-mono" font-size="11.5">45–55+ kts Sprint • Overcomes CIWS</text>
        </g>
      </g>

      <!-- Bottom Status Pill -->
      <g transform="translate(18, 508)">
        <rect width="488" height="50" rx="7" fill="#380926" stroke="#db2777" stroke-width="1.2"/>
        <text x="244" y="31" fill="#f472b6" class="font-mono" font-size="14.5" font-weight="bold" text-anchor="middle">
          ENERGY EFFICIENCY OPTIMIZATION: 3.8X RANGE MULTIPLIER
        </text>
      </g>
    </g>

    <!-- ============ RIGHT: TECHNICAL SPECS & BULLETS (535 x 580) ============ -->
    <g transform="translate(560, 72)">
      <!-- Formula Pill -->
      <rect width="530" height="46" rx="7" fill="#330b26" stroke="#831853" stroke-width="1.2"/>
      <text x="20" y="29" fill="#f472b6" class="font-mono" font-size="14" font-weight="bold">
        FORMULA: Fn = v / √(g · L_wl) &amp; E_froude = η_prop(Fn) · P_kw
      </text>

      <!-- Item 1 -->
      <g transform="translate(0, 58)">
        <rect width="530" height="114" rx="8" fill="#1f0718" stroke="#54123c" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#500724" stroke="#f72585" stroke-width="1.4"/>
        <text x="30" y="35" fill="#f72585" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">01</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Transit Phase: Frugal Displacement (Fn &lt; 1.0)</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Maintains sub-critical speed minimizing wave drag,
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          maximizing efficiency &amp; extending radius to <tspan fill="#f72585" font-weight="bold"> 800–1,200 km </tspan>.
        </text>
      </g>

      <!-- Item 2 -->
      <g transform="translate(0, 184)">
        <rect width="530" height="114" rx="8" fill="#1f0718" stroke="#54123c" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#500724" stroke="#f72585" stroke-width="1.4"/>
        <text x="30" y="35" fill="#f72585" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">02</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Resistance Hump Barrier Punch-Through</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Pre-programs hydrodynamic power reserve to rapidly punch
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          through wave drag hump (1.0 &lt; Fn &lt; 2.5) without stalling.
        </text>
      </g>

      <!-- Item 3 -->
      <g transform="translate(0, 310)">
        <rect width="530" height="114" rx="8" fill="#1f0718" stroke="#54123c" stroke-width="1.2"/>
        <circle cx="30" cy="30" r="14" fill="#500724" stroke="#f72585" stroke-width="1.4"/>
        <text x="30" y="35" fill="#f72585" class="font-mono" font-size="15" font-weight="bold" text-anchor="middle">03</text>
        <text x="56" y="33" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="bold">Terminal Intercept: Planing Sprint (Fn &gt; 3.0)</text>
        <text x="56" y="62" fill="#cbd5e1" class="font-sans" font-size="16">
          Triggers maximum waterjet output upon terminal cueing,
        </text>
        <text x="56" y="86" fill="#cbd5e1" class="font-sans" font-size="16">
          unleashing 45–55+ kts sprint to defeat point-defense guns.
        </text>
      </g>

      <!-- Tactical Value Banner -->
      <g transform="translate(0, 436)">
        <rect width="530" height="135" rx="8" fill="#4a0833" stroke="#f72585" stroke-width="1.4" stroke-dasharray="5 4"/>
        <text x="22" y="32" fill="#f72585" class="font-sans" font-size="15.5" font-weight="bold" letter-spacing="1">
          OPERATIONAL PAYOFF: RESOLVING RANGE VS SPRINT
        </text>
        <text x="22" y="62" fill="#f1f5f9" class="font-sans" font-size="15.5">
          Bypasses traditional naval trade-off by scheduling energy:
        </text>
        <text x="22" y="88" fill="#f1f5f9" class="font-sans" font-size="15.5">
          90% mission duration is spent in frugal displacement, while
        </text>
        <text x="22" y="114" fill="#f472b6" class="font-sans" font-size="15.5" font-weight="bold">
          100% power is unleashed for terminal kinetic penetration.
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- FOOTER SECTION                                                            -->
  <!-- ========================================================================= -->
  <g transform="translate(70, 1675)">
    <line x1="0" y1="0" x2="2260" y2="0" stroke="#1f3652" stroke-width="1.5"/>
    <text x="0" y="26" fill="#64748b" class="font-sans" font-size="15" font-weight="700" letter-spacing="1.5">
      UNMANNED WARFARE ENGINE (UWE)
    </text>
    <text x="375" y="26" fill="#475569" class="font-sans" font-size="15">&#8226;</text>
    <text x="395" y="26" fill="#94a3b8" class="font-sans" font-size="15">
      ARTICLE 5: UNMANNED SURFACE VEHICLES (USV) — 4D ENVIRONMENTAL COST TENSOR
    </text>
    <text x="2260" y="26" fill="#00e5ff" class="font-sans" font-size="15" font-weight="700" text-anchor="end">
      SERHII KHYLEVYCH — SYSTEMS ARCHITECT &amp; MILTECH STRATEGIST
    </text>
  </g>
</svg>"""

    out_svg = "/home/hills/Documents/UWS/environmental_cost_tensor.svg"
    with open(out_svg, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out_svg}")

if __name__ == "__main__":
    create_svg()
