import os
import subprocess

def generate_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1740" width="2400" height="1740">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="45%" stop-color="#08111e"/>
      <stop offset="100%" stop-color="#0a1526"/>
    </linearGradient>

    <!-- Column Card Backgrounds -->
    <linearGradient id="legacyCardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#180b0e" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#0f0608" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="uweCardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#091c2b" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#05121e" stop-opacity="0.95"/>
    </linearGradient>

    <!-- Visual Box Inner Gradients -->
    <linearGradient id="legacyVizBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#240c11"/>
      <stop offset="100%" stop-color="#120407"/>
    </linearGradient>
    <linearGradient id="uweVizBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#062233"/>
      <stop offset="100%" stop-color="#03111b"/>
    </linearGradient>

    <!-- Accent Gradients -->
    <linearGradient id="accentRed" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="accentCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e5ff"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="accentAmber" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="accentEmerald" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="100%" stop-color="#059669"/>
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
  <rect width="2400" height="1740" fill="url(#bgGrad)"/>
  <rect width="2400" height="1740" fill="url(#tacticalGrid)"/>

  <!-- Top Accent Bar: Half Red / Half Cyan -->
  <rect x="0" y="0" width="1200" height="7" fill="url(#accentRed)"/>
  <rect x="1200" y="0" width="1200" height="7" fill="url(#accentCyan)"/>

  <!-- ========================================================================= -->
  <!-- HEADER SECTION                                                            -->
  <!-- ========================================================================= -->
  <g transform="translate(70, 44)">
    <!-- Top Pill / Architecture Tag -->
    <rect x="0" y="0" width="340" height="32" rx="6" fill="#002b4d" stroke="#00a8e8" stroke-width="1.3"/>
    <text x="170" y="21" fill="#00e5ff" class="font-sans" font-size="13.5" font-weight="700" letter-spacing="2" text-anchor="middle">
      UWE DOCTRINAL ARCHITECTURE
    </text>

    <!-- Main Title -->
    <text x="0" y="74" fill="#ffffff" class="font-sans" font-size="38" font-weight="900" letter-spacing="0.5">
      LEGACY NAVALIST FALLACY <tspan fill="#64748b" font-weight="400">vs.</tspan> UWE CYBER-PHYSICAL REALITY
    </text>

    <!-- Subtitle -->
    <text x="0" y="112" fill="#94a3b8" class="font-sans" font-size="19.5">
      Why Bureaucratic Shipbuilding Collapses in Drone Combat — And How UWE Restores Fleet Tactics:
    </text>

    <!-- Formula / Doctrine Pill on Right -->
    <g transform="translate(1210, 80)">
      <rect x="0" y="0" width="1050" height="42" rx="8" fill="#0b1728" stroke="#1e3a5f" stroke-width="1.3"/>
      <text x="20" y="27" fill="#64748b" class="font-mono" font-size="13.5" font-weight="bold">SALVO DOCTRINE :</text>
      
      <text x="175" y="27" fill="#e2e8f0" class="font-mono" font-size="15" font-weight="bold">
        ΔP_kill ∝ [ 
        <tspan fill="#00e5ff">N_salvo</tspan> · <tspan fill="#00f5d4">P_hit</tspan> 
        ] / [ 
        <tspan fill="#ef4444">A_def</tspan> + <tspan fill="#f59e0b">S_intercept</tspan> 
        ]
      </text>

      <rect x="880" y="7" width="150" height="28" rx="5" fill="#003459" stroke="#00e5ff" stroke-width="1.2"/>
      <text x="955" y="26" fill="#00e5ff" class="font-mono" font-size="12.5" font-weight="bold" text-anchor="middle">HUGHES' LAW</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- COLUMN HEADERS                                                            -->
  <!-- ========================================================================= -->
  <!-- Left Header: Western Bureaucratic Model -->
  <g transform="translate(70, 175)">
    <rect width="1100" height="54" rx="10" fill="#2d0a10" stroke="#ef4444" stroke-width="1.6"/>
    <rect x="14" y="10" width="170" height="34" rx="6" fill="#450a12" stroke="#ef4444" stroke-width="1.2"/>
    <text x="99" y="32" fill="#fca5a5" class="font-mono" font-size="13.5" font-weight="bold" text-anchor="middle">LEGACY DOCTRINE</text>
    
    <text x="205" y="35" fill="#ffffff" class="font-sans" font-size="21" font-weight="bold" letter-spacing="0.5">
      WESTERN BUREAUCRATIC MODEL
    </text>
    <text x="1080" y="34" fill="#f87171" class="font-mono" font-size="14" font-weight="bold" text-anchor="end">
      [ MONOLITHIC &amp; VULNERABLE ]
    </text>
  </g>

  <!-- Center VS Divider -->
  <g transform="translate(1200, 202)">
    <circle cx="0" cy="0" r="22" fill="#0c1929" stroke="#38bdf8" stroke-width="2"/>
    <text x="0" y="6" fill="#00e5ff" class="font-sans" font-size="15" font-weight="900" text-anchor="middle">VS</text>
  </g>

  <!-- Right Header: UWE Operational Matrix -->
  <g transform="translate(1230, 175)">
    <rect width="1100" height="54" rx="10" fill="#062236" stroke="#00e5ff" stroke-width="1.6"/>
    <rect x="14" y="10" width="165" height="34" rx="6" fill="#003459" stroke="#00e5ff" stroke-width="1.2"/>
    <text x="96" y="32" fill="#38bdf8" class="font-mono" font-size="13.5" font-weight="bold" text-anchor="middle">UWE PARADIGM</text>
    
    <text x="200" y="35" fill="#ffffff" class="font-sans" font-size="21" font-weight="bold" letter-spacing="0.5">
      UWE OPERATIONAL MATRIX
    </text>
    <text x="1080" y="34" fill="#00f5d4" class="font-mono" font-size="14" font-weight="bold" text-anchor="end">
      [ SOFTWARE-DEFINED SWARM ]
    </text>
  </g>

  <!-- ========================================================================= -->
  <!-- ROW 1: TAXONOMY & PHYSICAL METRIC                                         -->
  <!-- ========================================================================= -->
  <!-- ROW 1 LEFT: Legacy Metric -->
  <g transform="translate(70, 248)">
    <rect width="1100" height="255" rx="12" fill="url(#legacyCardBg)" stroke="#4a151b" stroke-width="1.5"/>
    
    <!-- Header inside card -->
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#3b0f14" stroke="#7f1d1d" stroke-width="1.2"/>
    <text x="126" y="31" fill="#fca5a5" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">01 | TAXONOMY &amp; METRICS</text>

    <rect x="246" y="12" width="280" height="28" rx="5" fill="#2d0a0f" stroke="#ef4444" stroke-width="1"/>
    <text x="386" y="31" fill="#ef4444" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">CLASSIFIES BY LENGTH &amp; HULL WEIGHT</text>

    <!-- Main Content Left -->
    <g transform="translate(20, 52)">
      <text x="0" y="24" fill="#ffffff" class="font-sans" font-size="20.5" font-weight="bold">
        Classifies by Length &amp; Hull Weight
      </text>

      <!-- Bullet 1 -->
      <circle cx="8" cy="55" r="4" fill="#ef4444"/>
      <text x="22" y="60" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Bureaucratic Shipbuilding Tonnage Classes:
      </text>
      <text x="22" y="84" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Classifies USVs by physical length (Small &lt;7m, Medium 7–12m, Large &gt;12m)
      </text>
      <text x="22" y="106" fill="#cbd5e1" class="font-sans" font-size="15.5">
        and dry displacement, treating autonomous craft like scaled-down patrol boats.
      </text>

      <!-- Bullet 2 -->
      <circle cx="8" cy="138" r="4" fill="#ef4444"/>
      <text x="22" y="143" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Completely Blind to Environmental Ocean Physics:
      </text>
      <text x="22" y="167" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Ignores wave period resonance, wave slamming g-limits, and fresh/salt draft loss.
      </text>
      <text x="22" y="189" fill="#94a3b8" class="font-sans" font-size="15">
        A 10m monohull disintegrates in Sea State 4, while an 8m wave-piercer thrives.
      </text>
    </g>

    <!-- Right Graphic Box inside Card (width 390, height 195) -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#legacyVizBg)" stroke="#4a151b" stroke-width="1.2"/>
      <text x="18" y="26" fill="#fca5a5" class="font-mono" font-size="12" font-weight="bold">METRIC: ARBITRARY HULL LENGTH (LOA)</text>
      
      <!-- Ruler Graphic -->
      <g transform="translate(20, 48)">
        <line x1="0" y1="20" x2="355" y2="20" stroke="#7f1d1d" stroke-width="3"/>
        <line x1="0" y1="8" x2="0" y2="32" stroke="#ef4444" stroke-width="2"/>
        <line x1="110" y1="12" x2="110" y2="28" stroke="#ef4444" stroke-width="2"/>
        <line x1="230" y1="12" x2="230" y2="28" stroke="#ef4444" stroke-width="2"/>
        <line x1="355" y1="8" x2="355" y2="32" stroke="#ef4444" stroke-width="2"/>
        
        <text x="55" y="44" fill="#f87171" class="font-mono" font-size="12" text-anchor="middle">&lt; 7m (Small)</text>
        <text x="170" y="44" fill="#f87171" class="font-mono" font-size="12" text-anchor="middle">7–12m (Medium)</text>
        <text x="290" y="44" fill="#f87171" class="font-mono" font-size="12" text-anchor="middle">&gt; 12m (Large)</text>
      </g>

      <!-- Failure Alert Badge -->
      <g transform="translate(20, 115)">
        <rect width="355" height="62" rx="6" fill="#3b0f14" stroke="#ef4444" stroke-width="1.2"/>
        <circle cx="24" cy="31" r="10" fill="#7f1d1d"/>
        <text x="24" y="36" fill="#ffffff" class="font-mono" font-size="14" font-weight="bold" text-anchor="middle">✕</text>
        <text x="45" y="26" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">FATAL DOCTRINAL FLAW:</text>
        <text x="45" y="47" fill="#fca5a5" class="font-sans" font-size="12">
          Metric predicts neither wave survivability nor RCS stealth!
        </text>
      </g>
    </g>
  </g>

  <!-- ROW 1 RIGHT: UWE Domain Matrix -->
  <g transform="translate(1230, 248)">
    <rect width="1100" height="255" rx="12" fill="url(#uweCardBg)" stroke="#1a3d66" stroke-width="1.5"/>
    
    <!-- Header inside card -->
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#072b47" stroke="#0284c7" stroke-width="1.2"/>
    <text x="126" y="31" fill="#38bdf8" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">01 | TAXONOMY &amp; METRICS</text>

    <rect x="246" y="12" width="280" height="28" rx="5" fill="#003459" stroke="#00e5ff" stroke-width="1"/>
    <text x="386" y="31" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">CLASSIFIES BY AQUATIC DOMAIN (A)</text>

    <!-- Main Content Right -->
    <g transform="translate(20, 52)">
      <text x="0" y="24" fill="#ffffff" class="font-sans" font-size="20.5" font-weight="bold">
        Classifies by Aquatic Domain (A)
      </text>

      <!-- Bullet 1 -->
      <circle cx="8" cy="55" r="4" fill="#00e5ff"/>
      <text x="22" y="60" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        Multi-Physics Environmental Cost Tensor:
      </text>
      <text x="22" y="84" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Classifies by operational hydrodynamic regime: Fluvial (F), Littoral (L),
      </text>
      <text x="22" y="106" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Shelf Green-Water (S), Pelagic Deep-Sea (P), and Oceanic Blue-Water (O).
      </text>

      <!-- Bullet 2 -->
      <circle cx="8" cy="138" r="4" fill="#00e5ff"/>
      <text x="22" y="143" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        Directly Coupled to Survivability Envelopes:
      </text>
      <text x="22" y="167" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Locks maximum vertical g-shock (G_z ≤ 3.5g) and under-keel safety margin.
      </text>
      <text x="22" y="189" fill="#7dd3fc" class="font-sans" font-size="15">
        Guarantees hull survival and propulsion coupling before tasking mission route.
      </text>
    </g>

    <!-- Right Graphic Box inside Card -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#uweVizBg)" stroke="#133d5e" stroke-width="1.2"/>
      <text x="18" y="26" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold">TAXONOMY: MULTI-PHYSICS FLUID REGIMES</text>

      <!-- 5 Domain Badges in Row -->
      <g transform="translate(18, 45)">
        <!-- F -->
        <rect x="0" y="0" width="65" height="52" rx="6" fill="#002b4d" stroke="#00a8e8" stroke-width="1.3"/>
        <text x="32" y="25" fill="#00e5ff" class="font-mono" font-size="16" font-weight="bold" text-anchor="middle">F</text>
        <text x="32" y="42" fill="#7dd3fc" class="font-sans" font-size="10.5" text-anchor="middle">Fluvial</text>

        <!-- L -->
        <rect x="73" y="0" width="65" height="52" rx="6" fill="#002b4d" stroke="#00a8e8" stroke-width="1.3"/>
        <text x="105" y="25" fill="#00e5ff" class="font-mono" font-size="16" font-weight="bold" text-anchor="middle">L</text>
        <text x="105" y="42" fill="#7dd3fc" class="font-sans" font-size="10.5" text-anchor="middle">Littoral</text>

        <!-- S -->
        <rect x="146" y="0" width="65" height="52" rx="6" fill="#002b4d" stroke="#00a8e8" stroke-width="1.3"/>
        <text x="178" y="25" fill="#00e5ff" class="font-mono" font-size="16" font-weight="bold" text-anchor="middle">S</text>
        <text x="178" y="42" fill="#7dd3fc" class="font-sans" font-size="10.5" text-anchor="middle">Shelf</text>

        <!-- P -->
        <rect x="219" y="0" width="65" height="52" rx="6" fill="#002b4d" stroke="#00a8e8" stroke-width="1.3"/>
        <text x="251" y="25" fill="#00e5ff" class="font-mono" font-size="16" font-weight="bold" text-anchor="middle">P</text>
        <text x="251" y="42" fill="#7dd3fc" class="font-sans" font-size="10.5" text-anchor="middle">Pelagic</text>

        <!-- O -->
        <rect x="292" y="0" width="65" height="52" rx="6" fill="#002b4d" stroke="#00a8e8" stroke-width="1.3"/>
        <text x="324" y="25" fill="#00e5ff" class="font-mono" font-size="16" font-weight="bold" text-anchor="middle">O</text>
        <text x="324" y="42" fill="#7dd3fc" class="font-sans" font-size="10.5" text-anchor="middle">Oceanic</text>
      </g>

      <!-- Tensor Status Badge -->
      <g transform="translate(18, 115)">
        <rect width="358" height="62" rx="6" fill="#06324d" stroke="#00e5ff" stroke-width="1.2"/>
        <circle cx="24" cy="31" r="10" fill="#00a8e8"/>
        <text x="24" y="36" fill="#ffffff" class="font-mono" font-size="14" font-weight="bold" text-anchor="middle">✓</text>
        <text x="45" y="26" fill="#ffffff" class="font-sans" font-size="12.5" font-weight="bold">CYBER-PHYSICAL ADVANTAGE:</text>
        <text x="45" y="47" fill="#67e8f9" class="font-sans" font-size="12">
          Guarantees real-time 100Hz path planning across wave energy tensors!
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- ROW 2: ARCHITECTURAL PARADIGM & SWARMING                                  -->
  <!-- ========================================================================= -->
  <!-- ROW 2 LEFT: Mini-Frigate Fallacy -->
  <g transform="translate(70, 525)">
    <rect width="1100" height="255" rx="12" fill="url(#legacyCardBg)" stroke="#4a151b" stroke-width="1.5"/>
    
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#3b0f14" stroke="#7f1d1d" stroke-width="1.2"/>
    <text x="126" y="31" fill="#fca5a5" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">02 | SYSTEM PARADIGM</text>

    <rect x="246" y="12" width="245" height="28" rx="5" fill="#2d0a0f" stroke="#ef4444" stroke-width="1"/>
    <text x="368" y="31" fill="#ef4444" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">"MINIATURE FRIGATES" PARADIGM</text>

    <g transform="translate(20, 52)">
      <text x="0" y="24" fill="#ffffff" class="font-sans" font-size="20.5" font-weight="bold">
        "Miniature Frigates" Paradigm (Sensors + Arms)
      </text>

      <circle cx="8" cy="55" r="4" fill="#ef4444"/>
      <text x="22" y="60" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Cramming Multi-Mission Suites on a Single Hull:
      </text>
      <text x="22" y="84" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Tries to downscale 4,000-ton frigate capabilities onto a 10m hull: rotating radar,
      </text>
      <text x="22" y="106" fill="#cbd5e1" class="font-sans" font-size="15.5">
        heavy EO/IR turrets, 30mm remote weapon stations, and multi-mission bays.
      </text>

      <circle cx="8" cy="138" r="4" fill="#ef4444"/>
      <text x="22" y="143" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Fragile Singleton Electronic &amp; Kinetic Target:
      </text>
      <text x="22" y="167" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Overweight, electronically radiant, and impossible to service in austere field depots.
      </text>
      <text x="22" y="189" fill="#94a3b8" class="font-sans" font-size="15">
        Loss of a single platform forfeits the entire multi-mission sensor suite immediately.
      </text>
    </g>

    <!-- Right Graphic Box -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#legacyVizBg)" stroke="#4a151b" stroke-width="1.2"/>
      <text x="18" y="26" fill="#fca5a5" class="font-mono" font-size="12" font-weight="bold">PARADIGM: OVERLOADED SINGLETON</text>

      <!-- Overloaded Hull Silhouette Graphic -->
      <g transform="translate(45, 65)">
        <!-- Heavy Boat Silhouette -->
        <polygon points="0,40 230,40 270,10 0,10" fill="#3b0f15" stroke="#ef4444" stroke-width="2"/>
        <!-- Crowded Top Masts -->
        <rect x="50" y="-12" width="20" height="22" fill="#5c1d24" stroke="#f87171" stroke-width="1.2"/>
        <line x1="60" y1="-12" x2="60" y2="-28" stroke="#f87171" stroke-width="2"/>
        <circle cx="60" cy="-30" r="6" fill="#ef4444"/>
        
        <rect x="110" y="-8" width="35" height="18" fill="#5c1d24" stroke="#f87171" stroke-width="1.2"/>
        <line x1="127" y1="-8" x2="127" y2="-38" stroke="#f87171" stroke-width="2"/>
        <polygon points="120,-38 134,-38 127,-48" fill="#f59e0b"/>

        <rect x="175" y="0" width="25" height="10" fill="#7f1d1d"/>
        <line x1="195" y1="0" x2="215" y2="-12" stroke="#ef4444" stroke-width="3"/>

        <!-- Overweight Sinking Vectors -->
        <line x1="135" y1="45" x2="135" y2="65" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 2"/>
        <polygon points="131,65 139,65 135,72" fill="#ef4444"/>
        <text x="145" y="62" fill="#fca5a5" class="font-mono" font-size="11">OVERWEIGHT (LOW MARGIN)</text>
      </g>

      <g transform="translate(18, 148)">
        <rect width="358" height="34" rx="5" fill="#2d0a0f" stroke="#ef4444" stroke-width="1"/>
        <text x="179" y="22" fill="#f87171" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
          CRITICAL FAILURE: 1 SHOT DISABLES ENTIRE ASSET
        </text>
      </g>
    </g>
  </g>

  <!-- ROW 2 RIGHT: UWE Swarm Matrix -->
  <g transform="translate(1230, 525)">
    <rect width="1100" height="255" rx="12" fill="url(#uweCardBg)" stroke="#1a3d66" stroke-width="1.5"/>
    
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#072b47" stroke="#0284c7" stroke-width="1.2"/>
    <text x="126" y="31" fill="#38bdf8" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">02 | SYSTEM PARADIGM</text>

    <rect x="246" y="12" width="260" height="28" rx="5" fill="#003459" stroke="#00e5ff" stroke-width="1"/>
    <text x="376" y="31" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">SOFTWARE-DEFINED SWARM VECTORS</text>

    <g transform="translate(20, 52)">
      <text x="0" y="24" fill="#ffffff" class="font-sans" font-size="20.5" font-weight="bold">
        Software-Defined Swarming Vectors
      </text>

      <circle cx="8" cy="55" r="4" fill="#00e5ff"/>
      <text x="22" y="60" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        Functional Disaggregation Across Cheap Nodes:
      </text>
      <text x="22" y="84" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Splits mission roles across dedicated USVs: 1 Recon/EO Scout, 2 Radar Decoys,
      </text>
      <text x="22" y="106" fill="#cbd5e1" class="font-sans" font-size="15.5">
        and 6 Kinetic Strike Hulls linked via decentralized COFDM / Satellite mesh.
      </text>

      <circle cx="8" cy="138" r="4" fill="#00e5ff"/>
      <text x="22" y="143" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        Algorithmic Resilience &amp; Self-Healing Formation:
      </text>
      <text x="22" y="167" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Destroying any individual USV triggers instant algorithmic re-tasking.
      </text>
      <text x="22" y="189" fill="#7dd3fc" class="font-sans" font-size="15">
        The swarm maintains full lethality and target track even with 50% node loss.
      </text>
    </g>

    <!-- Right Graphic Box -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#uweVizBg)" stroke="#133d5e" stroke-width="1.2"/>
      <text x="18" y="26" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold">PARADIGM: DISAGGREGATED SWARM TOPOLOGY</text>

      <!-- Swarm Mesh Graphic -->
      <g transform="translate(30, 45)">
        <!-- Mesh Lines -->
        <line x1="50" y1="50" x2="165" y2="20" stroke="#00e5ff" stroke-width="1.5" stroke-opacity="0.6"/>
        <line x1="50" y1="50" x2="165" y2="80" stroke="#00e5ff" stroke-width="1.5" stroke-opacity="0.6"/>
        <line x1="165" y1="20" x2="280" y2="50" stroke="#00e5ff" stroke-width="1.5" stroke-opacity="0.6"/>
        <line x1="165" y1="80" x2="280" y2="50" stroke="#00e5ff" stroke-width="1.5" stroke-opacity="0.6"/>
        <line x1="165" y1="20" x2="165" y2="80" stroke="#00f5d4" stroke-width="1.5" stroke-dasharray="3 2"/>

        <!-- Nodes -->
        <!-- Node 1: Scout -->
        <circle cx="50" cy="50" r="14" fill="#003459" stroke="#00e5ff" stroke-width="2"/>
        <text x="50" y="54" fill="#00e5ff" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">EO</text>
        <text x="50" y="76" fill="#7dd3fc" class="font-mono" font-size="9.5" text-anchor="middle">SCOUT</text>

        <!-- Node 2: Decoy -->
        <circle cx="165" cy="20" r="14" fill="#3b0f34" stroke="#f72585" stroke-width="2"/>
        <text x="165" y="24" fill="#f72585" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">EW</text>
        <text x="165" y="6" fill="#f472b6" class="font-mono" font-size="9.5" text-anchor="middle">DECOY</text>

        <!-- Node 3: Kinetic -->
        <circle cx="165" cy="80" r="14" fill="#064e3b" stroke="#00f5d4" stroke-width="2"/>
        <text x="165" y="84" fill="#00f5d4" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">KT</text>
        <text x="165" y="104" fill="#34d399" class="font-mono" font-size="9.5" text-anchor="middle">STRIKE</text>

        <!-- Node 4: Kinetic -->
        <circle cx="280" cy="50" r="14" fill="#064e3b" stroke="#00f5d4" stroke-width="2"/>
        <text x="280" y="54" fill="#00f5d4" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">KT</text>
        <text x="280" y="76" fill="#34d399" class="font-mono" font-size="9.5" text-anchor="middle">STRIKE</text>
      </g>

      <g transform="translate(18, 148)">
        <rect width="358" height="34" rx="5" fill="#062e26" stroke="#00f5d4" stroke-width="1"/>
        <text x="179" y="22" fill="#34d399" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
          SELF-HEALING: RESILIENT ALGORITHMIC CONTINUITY
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- ROW 3: PLATFORM ECONOMICS & HARDWARE ABSTRACTION                         -->
  <!-- ========================================================================= -->
  <!-- ROW 3 LEFT: Expensive Boutique Hulls -->
  <g transform="translate(70, 802)">
    <rect width="1100" height="255" rx="12" fill="url(#legacyCardBg)" stroke="#4a151b" stroke-width="1.5"/>
    
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#3b0f14" stroke="#7f1d1d" stroke-width="1.2"/>
    <text x="126" y="31" fill="#fca5a5" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">03 | COST &amp; PROCUREMENT</text>

    <rect x="246" y="12" width="280" height="28" rx="5" fill="#2d0a0f" stroke="#ef4444" stroke-width="1"/>
    <text x="386" y="31" fill="#ef4444" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">EXPENSIVE MULTIPURPOSE PLATFORMS</text>

    <g transform="translate(20, 52)">
      <text x="0" y="24" fill="#ffffff" class="font-sans" font-size="20.5" font-weight="bold">
        Expensive Multipurpose Platforms ($15M–$50M)
      </text>

      <circle cx="8" cy="55" r="4" fill="#ef4444"/>
      <text x="22" y="60" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Bespoke Prime-Contractor Cost Structure:
      </text>
      <text x="22" y="84" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Prototypes built like luxury yachts with custom MIL-SPEC avionics, taking 5–7 years
      </text>
      <text x="22" y="106" fill="#cbd5e1" class="font-sans" font-size="15.5">
        from requirement to delivery at unsustainable unit costs of tens of millions.
      </text>

      <circle cx="8" cy="138" r="4" fill="#ef4444"/>
      <text x="22" y="143" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Tight Hardware/Software Coupling &amp; Vendor Lock-In:
      </text>
      <text x="22" y="167" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Changing a camera or propulsion motor requires full OEM system recertification.
      </text>
      <text x="22" y="189" fill="#94a3b8" class="font-sans" font-size="15">
        The high financial and reputational cost prevents platforms from being risked.
      </text>
    </g>

    <!-- Right Graphic Box -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#legacyVizBg)" stroke="#4a151b" stroke-width="1.2"/>
      <text x="18" y="26" fill="#fca5a5" class="font-mono" font-size="12" font-weight="bold">COST METRIC: CAPITAL ACQUISITION</text>

      <!-- Cost Graphic -->
      <g transform="translate(20, 42)">
        <rect width="355" height="48" rx="6" fill="#3b0f14" stroke="#ef4444" stroke-width="1.3"/>
        <text x="20" y="32" fill="#f87171" class="font-mono" font-size="18" font-weight="bold">
          $15,000,000 – $50,000,000
        </text>
        <rect x="275" y="12" width="70" height="24" rx="4" fill="#7f1d1d"/>
        <text x="310" y="28" fill="#ffffff" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">PER UNIT</text>

        <!-- Lifecycle timeline -->
        <g transform="translate(0, 60)">
          <text x="0" y="16" fill="#94a3b8" class="font-mono" font-size="11">PROCUREMENT TIMELINE: 6-8 YEARS</text>
          <rect x="0" y="22" width="355" height="12" rx="3" fill="#2d0a0f"/>
          <rect x="0" y="22" width="280" height="12" rx="3" fill="#ef4444"/>
        </g>
      </g>

      <g transform="translate(18, 148)">
        <rect width="358" height="34" rx="5" fill="#2d0a0f" stroke="#ef4444" stroke-width="1"/>
        <text x="179" y="22" fill="#f87171" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
          DOCTRINAL PARALYSIS: TOO EXPENSIVE TO LOSE
        </text>
      </g>
    </g>
  </g>

  <!-- ROW 3 RIGHT: UWE Decoupled HAL -->
  <g transform="translate(1230, 802)">
    <rect width="1100" height="255" rx="12" fill="url(#uweCardBg)" stroke="#1a3d66" stroke-width="1.5"/>
    
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#072b47" stroke="#0284c7" stroke-width="1.2"/>
    <text x="126" y="31" fill="#38bdf8" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">03 | COST &amp; PROCUREMENT</text>

    <rect x="246" y="12" width="280" height="28" rx="5" fill="#003459" stroke="#00e5ff" stroke-width="1"/>
    <text x="386" y="31" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">DECOUPLED HAL CHASSIS + MISSION</text>

    <g transform="translate(20, 52)">
      <text x="0" y="24" fill="#ffffff" class="font-sans" font-size="20.5" font-weight="bold">
        Decoupled HAL Chassis + Mission Modules
      </text>

      <circle cx="8" cy="55" r="4" fill="#00e5ff"/>
      <text x="22" y="60" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        Hydrodynamic Chassis Decoupled from Mission Software:
      </text>
      <text x="22" y="84" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Standard composite hulls ($45k–$150k) produced in non-shipyard industrial plants
      </text>
      <text x="22" y="106" fill="#cbd5e1" class="font-sans" font-size="15.5">
        with unified CAN-bus/Ethernet HAL interfaces for propulsion and steering.
      </text>

      <circle cx="8" cy="138" r="4" fill="#00e5ff"/>
      <text x="22" y="143" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        20-Minute Field Swap &amp; Consumable Attrition Math:
      </text>
      <text x="22" y="167" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Plug-and-play bays swap in minutes: 300kg warhead, ISR gimbal, or FPV relay.
      </text>
      <text x="22" y="189" fill="#7dd3fc" class="font-sans" font-size="15">
        Cost asymmetry: a $100k USV salvo destroys a $1.2B air-defense destroyer.
      </text>
    </g>

    <!-- Right Graphic Box -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#uweVizBg)" stroke="#133d5e" stroke-width="1.2"/>
      <text x="18" y="26" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold">ARCHITECTURE: MODULAR HAL HARDWARE</text>

      <!-- Modular Hull Diagram -->
      <g transform="translate(20, 42)">
        <!-- Base Chassis -->
        <rect width="355" height="38" rx="6" fill="#003459" stroke="#00a8e8" stroke-width="1.2"/>
        <text x="15" y="24" fill="#38bdf8" class="font-mono" font-size="13" font-weight="bold">BASE CHASSIS [HAL]: $65,000</text>
        <text x="340" y="24" fill="#00e5ff" class="font-mono" font-size="11" text-anchor="end">CONSUMABLE</text>

        <!-- 3 Quick Swap Bays -->
        <g transform="translate(0, 46)">
          <rect x="0" y="0" width="112" height="46" rx="4" fill="#06324d" stroke="#00f5d4" stroke-width="1"/>
          <text x="56" y="20" fill="#00f5d4" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">BAY 01: STRIKE</text>
          <text x="56" y="36" fill="#cbd5e1" class="font-sans" font-size="9.5" text-anchor="middle">300kg HE Warhead</text>

          <rect x="121" y="0" width="112" height="46" rx="4" fill="#06324d" stroke="#00f5d4" stroke-width="1"/>
          <text x="177" y="20" fill="#00f5d4" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">BAY 02: ISR</text>
          <text x="177" y="36" fill="#cbd5e1" class="font-sans" font-size="9.5" text-anchor="middle">EO/IR + Radar</text>

          <rect x="243" y="0" width="112" height="46" rx="4" fill="#06324d" stroke="#00f5d4" stroke-width="1"/>
          <text x="299" y="20" fill="#00f5d4" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">BAY 03: RELAY</text>
          <text x="299" y="36" fill="#cbd5e1" class="font-sans" font-size="9.5" text-anchor="middle">Starlink + Mesh</text>
        </g>
      </g>

      <g transform="translate(18, 148)">
        <rect width="358" height="34" rx="5" fill="#062e26" stroke="#00f5d4" stroke-width="1"/>
        <text x="179" y="22" fill="#34d399" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
          ASYMMETRIC MATH: 1:1,000 COST EXCHANGE RATIO
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- ROW 4: LOGISTICAL DEPLOYABILITY & BASING                                  -->
  <!-- ========================================================================= -->
  <!-- ROW 4 LEFT: Fixed Naval Ports -->
  <g transform="translate(70, 1079)">
    <rect width="1100" height="255" rx="12" fill="url(#legacyCardBg)" stroke="#4a151b" stroke-width="1.5"/>
    
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#3b0f14" stroke="#7f1d1d" stroke-width="1.2"/>
    <text x="126" y="31" fill="#fca5a5" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">04 | BASING &amp; LOGISTICS</text>

    <rect x="246" y="12" width="280" height="28" rx="5" fill="#2d0a0f" stroke="#ef4444" stroke-width="1"/>
    <text x="386" y="31" fill="#ef4444" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">TIED TO FIXED NAVAL BASES &amp; DOCKS</text>

    <g transform="translate(20, 52)">
      <text x="0" y="24" fill="#ffffff" class="font-sans" font-size="20.5" font-weight="bold">
        Tied to Fixed Naval Bases &amp; Docks
      </text>

      <circle cx="8" cy="55" r="4" fill="#ef4444"/>
      <text x="22" y="60" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Port Infrastructure &amp; Specialized Slipway Dependency:
      </text>
      <text x="22" y="84" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Heavy USVs demand deep harbors (&gt;2.5m draft), travel-lift cranes, certified
      </text>
      <text x="22" y="106" fill="#cbd5e1" class="font-sans" font-size="15.5">
        fueling docks, and shoreside maintenance sheds within static naval bases.
      </text>

      <circle cx="8" cy="138" r="4" fill="#ef4444"/>
      <text x="22" y="143" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Pre-Emptive Missile Strike Target Magnet:
      </text>
      <text x="22" y="167" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Concentrated in predictable geolocations, vulnerable to ballistic/cruise missiles.
      </text>
      <text x="22" y="189" fill="#94a3b8" class="font-sans" font-size="15">
        Destroying the pier crane or fuel depot traps the entire unmanned squadron.
      </text>
    </g>

    <!-- Right Graphic Box -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#legacyVizBg)" stroke="#4a151b" stroke-width="1.2"/>
      <text x="18" y="26" fill="#fca5a5" class="font-mono" font-size="12" font-weight="bold">LOGISTICS: STATIC TARGET EXPOSURE</text>

      <!-- Port Crane Target Graphic -->
      <g transform="translate(25, 45)">
        <!-- Concrete Pier -->
        <rect x="0" y="45" width="160" height="45" fill="#2d1c1a" stroke="#57534e" stroke-width="1.5"/>
        <text x="75" y="72" fill="#a8a29e" class="font-mono" font-size="11" text-anchor="middle">CONCRETE PIER</text>
        
        <!-- Crane Frame -->
        <line x1="40" y1="45" x2="40" y2="5" stroke="#f59e0b" stroke-width="3"/>
        <line x1="80" y1="45" x2="80" y2="5" stroke="#f59e0b" stroke-width="3"/>
        <line x1="30" y1="5" x2="130" y2="5" stroke="#f59e0b" stroke-width="3"/>
        <line x1="110" y1="5" x2="110" y2="25" stroke="#78716c" stroke-width="1.5"/>
        <polygon points="100,25 120,25 110,35" fill="#ef4444"/>

        <!-- Ballistic Missile Target Reticle -->
        <g transform="translate(260, 45)">
          <circle cx="0" cy="0" r="30" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4 2"/>
          <line x1="-38" y1="0" x2="38" y2="0" stroke="#ef4444" stroke-width="2"/>
          <line x1="0" y1="-38" x2="0" y2="38" stroke="#ef4444" stroke-width="2"/>
          <text x="0" y="48" fill="#fca5a5" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">BALLISTIC TARGET</text>
        </g>
      </g>

      <g transform="translate(18, 148)">
        <rect width="358" height="34" rx="5" fill="#2d0a0f" stroke="#ef4444" stroke-width="1"/>
        <text x="179" y="22" fill="#f87171" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
          CONCENTRATION RISK: ZERO DEPLOYMENT DISPERSAL
        </text>
      </g>
    </g>
  </g>

  <!-- ROW 4 RIGHT: UWE Beach-Trailer Launch -->
  <g transform="translate(1230, 1079)">
    <rect width="1100" height="255" rx="12" fill="url(#uweCardBg)" stroke="#1a3d66" stroke-width="1.5"/>
    
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#072b47" stroke="#0284c7" stroke-width="1.2"/>
    <text x="126" y="31" fill="#38bdf8" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">04 | BASING &amp; LOGISTICS</text>

    <rect x="246" y="12" width="275" height="28" rx="5" fill="#003459" stroke="#00e5ff" stroke-width="1"/>
    <text x="383" y="31" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">DISPERSED 4x4 BEACH-TRAILER LAUNCH</text>

    <g transform="translate(20, 52)">
      <text x="0" y="24" fill="#ffffff" class="font-sans" font-size="20.5" font-weight="bold">
        Dispersed 4x4 Beach-Trailer Launch
      </text>

      <circle cx="8" cy="55" r="4" fill="#00e5ff"/>
      <text x="22" y="60" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        Zero Port Dependence &amp; Civilian Highway Mobility:
      </text>
      <text x="22" y="84" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Class T (1.0–3.5 t) towed by standard civilian 4x4 pickups or utility trucks;
      </text>
      <text x="22" y="106" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Class M (≤100 kg) hand-portable 2-person launch from beaches or dinghies.
      </text>

      <circle cx="8" cy="138" r="4" fill="#00e5ff"/>
      <text x="22" y="143" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        15-Minute Unpaved Shoreline Deploy &amp; Disappear:
      </text>
      <text x="22" y="167" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Launches from muddy riverbanks, tidal surf zones, or concealed tree cover.
      </text>
      <text x="22" y="189" fill="#7dd3fc" class="font-sans" font-size="15">
        Vehicles vacate the launch coordinate in minutes, denying counter-battery fire.
      </text>
    </g>

    <!-- Right Graphic Box -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#uweVizBg)" stroke="#133d5e" stroke-width="1.2"/>
      <text x="18" y="26" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold">LOGISTICS: EXPEDITIONARY DISPERSAL</text>

      <!-- Pickup + Beach Trailer Graphic -->
      <g transform="translate(20, 50)">
        <!-- 4x4 Pickup Truck Silhouette -->
        <rect x="10" y="20" width="75" height="24" rx="4" fill="#003459" stroke="#00a8e8" stroke-width="1.2"/>
        <rect x="45" y="6" width="35" height="16" rx="3" fill="#00223d" stroke="#00a8e8" stroke-width="1"/>
        <circle cx="28" cy="44" r="8" fill="#1e293b" stroke="#00e5ff" stroke-width="1.5"/>
        <circle cx="70" cy="44" r="8" fill="#1e293b" stroke="#00e5ff" stroke-width="1.5"/>

        <!-- Tow Hitch -->
        <line x1="85" y1="36" x2="110" y2="36" stroke="#94a3b8" stroke-width="2"/>

        <!-- Trailer + USV -->
        <rect x="110" y="26" width="105" height="12" rx="2" fill="#0f172a" stroke="#00f5d4" stroke-width="1.2"/>
        <circle cx="160" cy="44" r="8" fill="#1e293b" stroke="#00f5d4" stroke-width="1.5"/>
        
        <!-- USV on Trailer -->
        <polygon points="105,24 195,24 215,10 120,10" fill="#064e3b" stroke="#00f5d4" stroke-width="1.3"/>

        <!-- Sand / Surf Ramp -->
        <path d="M 0 54 L 180 54 L 260 70 L 350 70" fill="none" stroke="#eab308" stroke-width="2" stroke-dasharray="4 2"/>
        <text x="300" y="62" fill="#38bdf8" class="font-mono" font-size="11">SURF ZONE</text>
      </g>

      <g transform="translate(18, 148)">
        <rect width="358" height="34" rx="5" fill="#062e26" stroke="#00f5d4" stroke-width="1"/>
        <text x="179" y="22" fill="#34d399" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
          TOTAL MOBILITY: 100% DISPERSED EXPEDITIONARY MASS
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- ROW 5: OPERATIONAL PHILOSOPHY & COMBAT DOCTRINE                           -->
  <!-- ========================================================================= -->
  <!-- ROW 5 LEFT: Mahanian Capital Ship Preservation -->
  <g transform="translate(70, 1356)">
    <rect width="1100" height="255" rx="12" fill="url(#legacyCardBg)" stroke="#4a151b" stroke-width="1.5"/>
    
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#3b0f14" stroke="#7f1d1d" stroke-width="1.2"/>
    <text x="126" y="31" fill="#fca5a5" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">05 | COMBAT DOCTRINE</text>

    <rect x="246" y="12" width="300" height="28" rx="5" fill="#2d0a0f" stroke="#ef4444" stroke-width="1"/>
    <text x="396" y="31" fill="#ef4444" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">MAHANIAN CAPITAL SHIP PRESERVATION</text>

    <g transform="translate(20, 50)">
      <text x="0" y="20" fill="#ffffff" class="font-sans" font-size="20" font-weight="bold">
        Mahanian Capital Ship Preservation
      </text>
      <text x="0" y="42" fill="#fca5a5" class="font-mono" font-size="13" font-weight="bold">
        [ WAYNE HUGHES' CRITIQUE: PARALYZED BY ATTRITION AVERSION ]
      </text>

      <circle cx="8" cy="68" r="4" fill="#ef4444"/>
      <text x="22" y="73" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Inherited 20th-Century Dreadnought Psychology:
      </text>
      <text x="22" y="95" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Treats autonomous craft with traditional capital-ship risk aversion. Platforms are
      </text>
      <text x="22" y="117" fill="#cbd5e1" class="font-sans" font-size="15.5">
        held back behind carrier strike screens to avoid negative headlines and loss metrics.
      </text>

      <circle cx="8" cy="144" r="4" fill="#ef4444"/>
      <text x="22" y="149" fill="#fca5a5" class="font-sans" font-size="16" font-weight="bold">
        Defensive Reactive Stance &amp; Paralysis:
      </text>
      <text x="22" y="171" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Forfeits the initiative: forces USVs into patrol loops where they wait to be engaged
      </text>
      <text x="22" y="193" fill="#94a3b8" class="font-sans" font-size="15">
        by coastal missiles, sea mines, and FPV drones without inflicting salvo shock.
      </text>
    </g>

    <!-- Right Graphic Box -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#legacyVizBg)" stroke="#4a151b" stroke-width="1.2"/>
      <text x="18" y="26" fill="#fca5a5" class="font-mono" font-size="12" font-weight="bold">DOCTRINE: ATTRITION FEAR &amp; DEFENSIVE SCREEN</text>

      <!-- Defensive Shield Standoff Graphic -->
      <g transform="translate(30, 48)">
        <!-- Defensive Bubble -->
        <circle cx="160" cy="40" r="45" fill="#3b0f14" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4 2"/>
        <text x="160" y="44" fill="#fca5a5" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">DEFENSIVE SCREEN</text>

        <!-- Capital Ship Inside -->
        <rect x="135" y="15" width="50" height="14" fill="#7f1d1d"/>

        <!-- Inactive Arrows Stalled -->
        <line x1="30" y1="40" x2="90" y2="40" stroke="#78716c" stroke-width="2" stroke-dasharray="4 3"/>
        <text x="60" y="32" fill="#78716c" class="font-mono" font-size="10" text-anchor="middle">STANDOFF</text>

        <text x="260" y="44" fill="#f87171" class="font-mono" font-size="11" font-weight="bold">PARALYZED</text>
      </g>

      <g transform="translate(18, 148)">
        <rect width="358" height="34" rx="5" fill="#2d0a0f" stroke="#ef4444" stroke-width="1"/>
        <text x="179" y="22" fill="#f87171" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
          TACTICAL DEADLOCK: DEFENSE NEVER WINS FLEET ACTIONS
        </text>
      </g>
    </g>
  </g>

  <!-- ROW 5 RIGHT: Hughes Law Attack Effectively First -->
  <g transform="translate(1230, 1356)">
    <rect width="1100" height="255" rx="12" fill="url(#uweCardBg)" stroke="#1a3d66" stroke-width="1.5"/>
    
    <rect x="16" y="12" width="220" height="28" rx="5" fill="#072b47" stroke="#0284c7" stroke-width="1.2"/>
    <text x="126" y="31" fill="#38bdf8" class="font-mono" font-size="13" font-weight="bold" text-anchor="middle">05 | COMBAT DOCTRINE</text>

    <rect x="246" y="12" width="275" height="28" rx="5" fill="#003459" stroke="#00e5ff" stroke-width="1"/>
    <text x="383" y="31" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold" text-anchor="middle">HUGHES' LAW: "ATTACK EFFECTIVELY FIRST"</text>

    <g transform="translate(20, 50)">
      <text x="0" y="20" fill="#ffffff" class="font-sans" font-size="20" font-weight="bold">
        Hughes Law: "Attack Effectively First"
      </text>
      <text x="0" y="42" fill="#38bdf8" class="font-mono" font-size="13" font-weight="bold">
        [ MASS TACTICS: CHEAP ALGORITHMIC CONVERGENCE ]
      </text>

      <circle cx="8" cy="68" r="4" fill="#00e5ff"/>
      <text x="22" y="73" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        Fleet Tactics Salvo Model Overcomes Point Defenses:
      </text>
      <text x="22" y="95" fill="#cbd5e1" class="font-sans" font-size="15.5">
        Capt. Wayne P. Hughes' foundational naval axiom: in missile &amp; drone warfare,
      </text>
      <text x="22" y="117" fill="#cbd5e1" class="font-sans" font-size="15.5">
        victory belongs to the salvo that saturates enemy defensive channels (A_def + S) first.
      </text>

      <circle cx="8" cy="144" r="4" fill="#00e5ff"/>
      <text x="22" y="149" fill="#38bdf8" class="font-sans" font-size="16" font-weight="bold">
        Cheap Algorithmic Mass Overwhelms Billion-Dollar Targets:
      </text>
      <text x="22" y="171" fill="#cbd5e1" class="font-sans" font-size="15.5">
        A coordinated salvo of 12 USVs exhausts CIWS ammunition and radar tracking gates.
      </text>
      <text x="22" y="193" fill="#7dd3fc" class="font-sans" font-size="15">
        Sacrificing 6 USVs to sink a 6,000-ton capital frigate is mathematically decisive victory.
      </text>
    </g>

    <!-- Right Graphic Box -->
    <g transform="translate(685, 45)">
      <rect width="395" height="195" rx="8" fill="url(#uweVizBg)" stroke="#133d5e" stroke-width="1.2"/>
      <text x="18" y="26" fill="#00e5ff" class="font-mono" font-size="12" font-weight="bold">DOCTRINE: WAYNE HUGHES SALVO CONVERGENCE</text>

      <!-- Converging Salvo Graphic -->
      <g transform="translate(30, 42)">
        <!-- Enemy Warship Target in Center -->
        <g transform="translate(160, 45)">
          <rect x="-35" y="-12" width="70" height="24" rx="4" fill="#3b0f14" stroke="#ef4444" stroke-width="1.5"/>
          <text x="0" y="4" fill="#fca5a5" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">CAPITAL TARGET</text>
        </g>

        <!-- Converging Salvo Arrows from 4 Quarters -->
        <g stroke="#00e5ff" stroke-width="2.5">
          <line x1="20" y1="10" x2="115" y2="35"/>
          <polygon points="112,30 125,38 116,42" fill="#00e5ff"/>

          <line x1="20" y1="80" x2="115" y2="55"/>
          <polygon points="116,48 125,52 112,60" fill="#00e5ff"/>

          <line x1="310" y1="10" x2="215" y2="35"/>
          <polygon points="214,42 205,38 218,30" fill="#00e5ff"/>

          <line x1="310" y1="80" x2="215" y2="55"/>
          <polygon points="218,60 205,52 214,48" fill="#00e5ff"/>
        </g>
        
        <text x="160" y="92" fill="#00f5d4" class="font-mono" font-size="11" font-weight="bold" text-anchor="middle">
          N_salvo &gt; CIWS TRACKING ENVELOPE
        </text>
      </g>

      <g transform="translate(18, 148)">
        <rect width="358" height="34" rx="5" fill="#062e26" stroke="#00f5d4" stroke-width="1"/>
        <text x="179" y="22" fill="#34d399" class="font-mono" font-size="11.5" font-weight="bold" text-anchor="middle">
          DECISIVE COMBAT: "ATTACK EFFECTIVELY FIRST"
        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- FOOTER SECTION                                                            -->
  <!-- ========================================================================= -->
  <g transform="translate(70, 1690)">
    <line x1="0" y1="0" x2="2260" y2="0" stroke="#1f3652" stroke-width="1.5"/>
    <text x="0" y="26" fill="#64748b" class="font-sans" font-size="15" font-weight="700" letter-spacing="1.5">
      UNMANNED WARFARE ENGINE (UWE)
    </text>
    <text x="375" y="26" fill="#475569" class="font-sans" font-size="15">&#8226;</text>
    <text x="395" y="26" fill="#94a3b8" class="font-sans" font-size="15">
      ARTICLE 5: UNMANNED SURFACE VEHICLES (USV) — DOCTRINAL COMPARISON
    </text>
    <text x="2260" y="26" fill="#00e5ff" class="font-sans" font-size="15" font-weight="700" text-anchor="end">
      SERHII KHYLEVYCH — SYSTEMS ARCHITECT &amp; MILTECH STRATEGIST
    </text>
  </g>
</svg>"""

    out_svg = "/home/hills/Documents/UWS/legacy_vs_uwe_doctrine.svg"
    with open(out_svg, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out_svg}")

if __name__ == "__main__":
    generate_svg()
