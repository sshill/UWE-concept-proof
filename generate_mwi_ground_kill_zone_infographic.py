#!/usr/bin/env python3
"""
generate_mwi_ground_kill_zone_infographic.py

Generates a publication-grade 16:9 tactical architecture infographic:
- Core Layout:
  * Horizontal Module 1 (Top): UCV (Airborne Copter Echelon - Recon, Bomber, Attack, OWM)
  * Horizontal Module 2 (Center / Anchor): UGV (Terrestrial Convergence Node - 6-char [TK]-[DE]-[MC])
  * Horizontal Module 3 (Bottom): USV (Littoral & Amphibious Echelon - Beachhead & Riverine Handoff)
  * Vertical Spine (Full Height): UWE (Unmanned Warfare Engine) providing seamless vertical integration
    from UOV (Space / PWSA) through UCV, UGV, and USV down to hardware HAL/EAL and deterministic kill web.
- Outputs:
  1. mwi_ugv_ground_kill_zone.svg (2400 x 1350)
  2. mwi_ugv_ground_kill_zone.pdf (via LibreOffice)
  3. mwi_ugv_ground_kill_zone.png (high-res 2400 x 1350 via pdftoppm)
  4. mwi_ugv_ground_kill_zone_fitted.png (fitted 1000px for DOCX/HTML)
"""

import os
import subprocess

def create_svg():
    width = 2400
    height = 1350

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #070b12; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;">
  <defs>
    <!-- Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="50%" stop-color="#0a101d"/>
      <stop offset="100%" stop-color="#05080f"/>
    </linearGradient>

    <linearGradient id="ucvGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#082f49" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0c1929" stop-opacity="0.9"/>
    </linearGradient>

    <linearGradient id="ugvGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#451a03" stop-opacity="0.95"/>
      <stop offset="50%" stop-color="#2a1205" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#140b05" stop-opacity="0.95"/>
    </linearGradient>

    <linearGradient id="usvGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#083344" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#081c24" stop-opacity="0.9"/>
    </linearGradient>

    <linearGradient id="uweSpineGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#064e3b" stop-opacity="0.95"/>
      <stop offset="50%" stop-color="#022c22" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#064e3b" stop-opacity="0.95"/>
    </linearGradient>

    <linearGradient id="spineAccent" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="50%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>

    <linearGradient id="goldAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>

    <!-- Filters & Glow -->
    <filter id="glowGreen" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="glowGold" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="shadowBox" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- Background Layer -->
  <rect width="{width}" height="{height}" fill="url(#bgGrad)"/>

  <!-- Subtle Tactical Grid Overlay -->
  <g opacity="0.04" stroke="#38bdf8" stroke-width="1">
    {"".join([f'<line x1="{x}" y1="0" x2="{x}" y2="{height}"/>' for x in range(0, width, 80)])}
    {"".join([f'<line x1="0" y1="{y}" x2="{width}" y2="{y}"/>' for y in range(0, height, 80)])}
  </g>

  <!-- ======================================================== -->
  <!-- HEADER BLOCK                                             -->
  <!-- ======================================================== -->
  <g transform="translate(60, 40)">
    <!-- Pill Tag -->
    <rect x="0" y="0" width="460" height="30" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>
    <text x="20" y="20" fill="#38bdf8" font-size="12" font-weight="700" letter-spacing="1.5">UNMANNED WARFARE ENGINE (UWE) · MULTI-DOMAIN DOCTRINE</text>

    <!-- Main Title -->
    <text x="0" y="68" fill="#f8fafc" font-size="34" font-weight="800" letter-spacing="0.5">THE TERRESTRIAL ANCHOR: UGV AS THE CENTRAL CONVERGENCE NODE</text>
    <text x="0" y="100" fill="#94a3b8" font-size="18" font-weight="400">Horizontal Domain Modular Echelons (UCV · UGV · USV) Synchronized by the Unified Vertical UWE Engine</text>

    <!-- Doctrinal Pivot Banner -->
    <rect x="0" y="118" width="2280" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
    <text x="18" y="144" fill="#38bdf8" font-size="13" font-weight="700">DOCTRINAL SYNTHESIS:</text>
    <text x="185" y="144" fill="#cbd5e1" font-size="13" font-weight="400">Overcoming 1-to-1 Teleoperation Vulnerability through Machine-Speed Multi-Agent Formations: UGV Provides Persistent Terrestrial Mass, Kilowatt Energy, and Swarm Staging</text>
  </g>

  <!-- ======================================================== -->
  <!-- HORIZONTAL MODULE 1 (TOP): AIRBORNE UCV ECHELON          -->
  <!-- ======================================================== -->
  <g transform="translate(60, 220)" filter="url(#shadowBox)">
    <!-- Card Outer Box -->
    <rect width="1580" height="260" rx="10" fill="url(#ucvGrad)" stroke="#0284c7" stroke-width="1.8"/>

    <!-- Top Badge -->
    <rect x="24" y="18" width="280" height="26" rx="4" fill="#0369a1" fill-opacity="0.4" stroke="#38bdf8" stroke-width="1"/>
    <text x="36" y="35" fill="#38bdf8" font-size="12" font-weight="700" letter-spacing="1">AIRBORNE COPTER ECHELON (UCV)</text>

    <text x="320" y="36" fill="#7dd3fc" font-size="13" font-weight="500">Operating Envelope: 0–300 m (Ground-Clutter Boundary · Trench Traversal · Direct Terminal Dive)</text>

    <!-- Subtitle / Title -->
    <text x="24" y="76" fill="#f0f9ff" font-size="22" font-weight="700">UCV Combat Formations: Recon, Strike &amp; Terminal Interception</text>

    <!-- 3 Internal Feature Columns -->
    <g transform="translate(24, 96)">
      <rect width="490" height="140" rx="6" fill="#0c1e33" stroke="#1e3a5f" stroke-width="1"/>
      <text x="16" y="26" fill="#38bdf8" font-size="14" font-weight="700">Tactical Formations vs. Legacy 'FPV' Slang</text>
      <text x="16" y="52" fill="#cbd5e1" font-size="12" font-weight="400">• Standardized functional classes: Recon (RC), Bomber (BC),</text>
      <text x="16" y="72" fill="#cbd5e1" font-size="12" font-weight="400">  Direct Attack (AC), and One-Way Kinetic Interceptors (OWM).</text>
      <text x="16" y="96" fill="#cbd5e1" font-size="12" font-weight="400">• Synchronized wave tactics replace uncoordinated single hobby drones;</text>
      <text x="16" y="116" fill="#cbd5e1" font-size="12" font-weight="400">  eliminates pilot goggles in favor of automated algorithmic kill cues.</text>
    </g>

    <g transform="translate(530, 96)">
      <rect width="490" height="140" rx="6" fill="#0c1e33" stroke="#1e3a5f" stroke-width="1"/>
      <text x="16" y="26" fill="#38bdf8" font-size="14" font-weight="700">Kinematic Limits &amp; The Battery Deficit</text>
      <text x="16" y="52" fill="#cbd5e1" font-size="12" font-weight="400">• Multirotor physics forces 75–85% battery burn just to transit 10 km;</text>
      <text x="16" y="72" fill="#cbd5e1" font-size="12" font-weight="400">  copters arrive at the target with critical reserve depletion.</text>
      <text x="16" y="96" fill="#38bdf8" font-size="12" font-weight="600">→ Solved by UGV Staging: Launching copters 400 m from objective</text>
      <text x="16" y="116" fill="#cbd5e1" font-size="12" font-weight="400">  reserves 100% capacity for 140 km/h terminal anti-armor dives.</text>
    </g>

    <g transform="translate(1036, 96)">
      <rect width="520" height="140" rx="6" fill="#0c1e33" stroke="#1e3a5f" stroke-width="1"/>
      <text x="16" y="26" fill="#38bdf8" font-size="14" font-weight="700">Universal Aerial Syntax Code: [CL] · [EB] · [AO]</text>
      <text x="16" y="52" fill="#94a3b8" font-size="12" font-weight="400">Copter Rotorcraft · Light Transport · Electric Battery · Attack/OWM</text>
      <text x="16" y="78" fill="#e2e8f0" font-size="12" font-weight="500">• Edge-AI optical tracking defeats final 100m trench jamming.</text>
      <text x="16" y="98" fill="#e2e8f0" font-size="12" font-weight="500">• Micro-spooled optical fiber lines grant 100% EW immunity.</text>
      <text x="16" y="118" fill="#38bdf8" font-size="12" font-weight="600">• Inductive landing pads enable automated ground turnaround.</text>
    </g>
  </g>

  <!-- INTER-MODULE FLOW ARROWS (UCV <-> UGV) -->
  <g transform="translate(850, 485)">
    <line x1="0" y1="0" x2="0" y2="40" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6,4"/>
    <polygon points="-6,36 6,36 0,46" fill="#f59e0b"/>
    <polygon points="-6,10 6,10 0,0" fill="#38bdf8"/>
    <rect x="-180" y="8" width="360" height="24" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="0" y="24" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">LAW II CONTAINERIZATION: UGV CARRIES &amp; LAUNCHES UCV SWARMS</text>
  </g>

  <!-- ======================================================== -->
  <!-- HORIZONTAL MODULE 2 (CENTER): TERRESTRIAL UGV ANCHOR      -->
  <!-- ======================================================== -->
  <g transform="translate(60, 535)" filter="url(#shadowBox)">
    <!-- Main Card Body with Glowing Gold Stroke -->
    <rect width="1580" height="360" rx="12" fill="url(#ugvGrad)" stroke="#f59e0b" stroke-width="2.5"/>

    <!-- Center Top Badge -->
    <rect x="24" y="20" width="370" height="28" rx="4" fill="#78350f" fill-opacity="0.6" stroke="#fbbf24" stroke-width="1.2"/>
    <text x="36" y="39" fill="#fde68a" font-size="13" font-weight="800" letter-spacing="1.5">TERRESTRIAL CONVERGENCE NODE (UGV)</text>

    <text x="410" y="39" fill="#fcd34d" font-size="14" font-weight="600">The Core Physical &amp; Energetic Anchor of the Multi-Domain Ecosystem</text>

    <!-- Main Title -->
    <text x="24" y="84" fill="#fffbeb" font-size="26" font-weight="800">UGV: Software-Defined Ground Fleet &amp; Persistent Combat Server</text>
    <text x="24" y="108" fill="#fed7aa" font-size="14" font-weight="400">Overcoming Human Biological Limits: Zero-Signature Sleeper Ambush, Kilowatt EW Generation &amp; Cross-Domain Handoff</text>

    <!-- 4 Structured Sub-Cards -->
    <g transform="translate(24, 126)">
      <rect width="360" height="210" rx="8" fill="#1c0f07" stroke="#78350f" stroke-width="1.2"/>
      <rect x="12" y="12" width="160" height="22" rx="4" fill="#b45309"/>
      <text x="20" y="27" fill="#fef3c7" font-size="11" font-weight="700">NEW 6-CHAR MATRIX</text>
      <text x="180" y="28" fill="#f59e0b" font-size="15" font-weight="800">[TK] · [DE] · [MC]</text>

      <text x="14" y="58" fill="#fed7aa" font-size="12" font-weight="700">T · Terrain Dynamics:</text>
      <text x="14" y="74" fill="#cbd5e1" font-size="11">R(Rigid), L(Loose), W(Wet), C(Coastal), A(All)</text>

      <text x="14" y="96" fill="#fed7aa" font-size="12" font-weight="700">K · Kinematics &amp; Suspension:</text>
      <text x="14" y="112" fill="#cbd5e1" font-size="11">H(Hard), F(Fast), E(Extended flippers), L(Legged)</text>

      <text x="14" y="134" fill="#fed7aa" font-size="12" font-weight="700">D · Deployment Logistics &amp; Mass:</text>
      <text x="14" y="150" fill="#cbd5e1" font-size="11">H(&lt;15t), T(&lt;3t), P(&lt;800kg), L(&lt;80kg), B(&lt;20kg)</text>

      <text x="14" y="172" fill="#fed7aa" font-size="12" font-weight="700">E · Powerplant Lifecycle:</text>
      <text x="14" y="188" fill="#cbd5e1" font-size="11">B(Battery/Sleeper), D(Diesel), H(Hybrid), T(Tether)</text>
    </g>

    <g transform="translate(400, 126)">
      <rect width="370" height="210" rx="8" fill="#1c0f07" stroke="#78350f" stroke-width="1.2"/>
      <text x="16" y="28" fill="#fbbf24" font-size="14" font-weight="700">The "Zhdun" (Sleeper) Physics</text>
      <text x="16" y="52" fill="#cbd5e1" font-size="12" font-weight="400">• Humans cannot lie motionless for 14 days</text>
      <text x="16" y="70" fill="#cbd5e1" font-size="12" font-weight="400">  in frozen mud without food, warmth, or carbon output.</text>
      <text x="16" y="94" fill="#fed7aa" font-size="12" font-weight="600">• Pure chemical battery architecture (Index B):</text>
      <text x="16" y="112" fill="#cbd5e1" font-size="12" font-weight="400">  Draws &lt; 10 mA in dormant standby state;</text>
      <text x="16" y="130" fill="#cbd5e1" font-size="12" font-weight="400">  zero acoustic, thermal, or radio signature.</text>
      <text x="16" y="154" fill="#fbbf24" font-size="12" font-weight="700">• Instant Wakeup (&lt; 1.5 seconds):</text>
      <text x="16" y="174" fill="#cbd5e1" font-size="12" font-weight="400">  Fires shaped-charge ambush into rear armor plates</text>
      <text x="16" y="192" fill="#cbd5e1" font-size="12" font-weight="400">  upon seismic sensor tripwire cue.</text>
    </g>

    <g transform="translate(786, 126)">
      <rect width="380" height="210" rx="8" fill="#1c0f07" stroke="#78350f" stroke-width="1.2"/>
      <text x="16" y="28" fill="#fbbf24" font-size="14" font-weight="700">Kilowatt Powerhouse in the Mud</text>
      <text x="16" y="52" fill="#cbd5e1" font-size="12" font-weight="400">• Air drones cannot lift heavy diesel-generators</text>
      <text x="16" y="70" fill="#cbd5e1" font-size="12" font-weight="400">  or 100 kg battery banks without stalling.</text>
      <text x="16" y="94" fill="#fed7aa" font-size="12" font-weight="600">• Continuous High-Power EW Shield:</text>
      <text x="16" y="112" fill="#cbd5e1" font-size="12" font-weight="400">  UGV generates steady kilowatts to power active</text>
      <text x="16" y="130" fill="#cbd5e1" font-size="12" font-weight="400">  700–1050 MHz jamming domes shielding infantry.</text>
      <text x="16" y="154" fill="#fed7aa" font-size="12" font-weight="600">• Telescopic Tactical Antenna Mast:</text>
      <text x="16" y="174" fill="#cbd5e1" font-size="12" font-weight="400">  Bridges non-line-of-sight dead zones in ravines;</text>
      <text x="16" y="192" fill="#cbd5e1" font-size="12" font-weight="400">  acts as the physical radio relay for UCV swarms.</text>
    </g>

    <g transform="translate(1182, 126)">
      <rect width="374" height="210" rx="8" fill="#1c0f07" stroke="#78350f" stroke-width="1.2"/>
      <text x="16" y="28" fill="#fbbf24" font-size="14" font-weight="700">Technical Validation vs. SMET/RCV</text>
      <text x="16" y="52" fill="#cbd5e1" font-size="12" font-weight="400">• Exposes the fatal flaw of GDLS SMET:</text>
      <text x="16" y="70" fill="#cbd5e1" font-size="12" font-weight="400">  "Follow-me" tether makes robot an artillery magnet</text>
      <text x="16" y="88" fill="#cbd5e1" font-size="12" font-weight="400">  destroying the squad walking beside it.</text>
      <text x="16" y="114" fill="#fed7aa" font-size="12" font-weight="600">• Debunks the $5M RCV "Mini-Tank" Fallacy:</text>
      <text x="16" y="132" fill="#cbd5e1" font-size="12" font-weight="400">  Expensive teleoperated turrets blind under EW.</text>
      <text x="16" y="158" fill="#fbbf24" font-size="12" font-weight="700">• The UWE Solution:</text>
      <text x="16" y="176" fill="#cbd5e1" font-size="12" font-weight="400">  Attritable modular chassis with Edge-AI autonomy,</text>
      <text x="16" y="194" fill="#cbd5e1" font-size="12" font-weight="400">  acting as kinetic mothership, not manned tank clone.</text>
    </g>
  </g>

  <!-- INTER-MODULE FLOW ARROWS (UGV <-> USV) -->
  <g transform="translate(850, 900)">
    <line x1="0" y1="0" x2="0" y2="40" stroke="#06b6d4" stroke-width="3" stroke-dasharray="6,4"/>
    <polygon points="-6,36 6,36 0,46" fill="#06b6d4"/>
    <polygon points="-6,10 6,10 0,0" fill="#f59e0b"/>
    <rect x="-190" y="8" width="380" height="24" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="0" y="24" fill="#06b6d4" font-size="11" font-weight="700" text-anchor="middle">LITTORAL HANDOFF (PROFILE C): USV INSERTS UGV ON BEACHHEAD</text>
  </g>

  <!-- ======================================================== -->
  <!-- HORIZONTAL MODULE 3 (BOTTOM): LITTORAL USV ECHELON       -->
  <!-- ======================================================== -->
  <g transform="translate(60, 950)" filter="url(#shadowBox)">
    <!-- Card Outer Box -->
    <rect width="1580" height="210" rx="10" fill="url(#usvGrad)" stroke="#0891b2" stroke-width="1.8"/>

    <!-- Top Badge -->
    <rect x="24" y="16" width="310" height="26" rx="4" fill="#0e7490" fill-opacity="0.4" stroke="#22d3ee" stroke-width="1"/>
    <text x="36" y="33" fill="#22d3ee" font-size="12" font-weight="700" letter-spacing="1">LITTORAL &amp; MARITIME ECHELON (USV)</text>

    <text x="350" y="34" fill="#67e8f9" font-size="13" font-weight="500">Hydrodynamic Envelope: Riverine Crossings · Coastal Infiltration · Island Flank Defense</text>

    <!-- Subtitle -->
    <text x="24" y="70" fill="#ecfeff" font-size="20" font-weight="700">Surface Fleet: High-Speed Littoral Insertion &amp; Amphibious Drone Mothercraft</text>

    <!-- 3 Internal Feature Columns -->
    <g transform="translate(24, 86)">
      <rect width="490" height="106" rx="6" fill="#061d26" stroke="#155e75" stroke-width="1"/>
      <text x="16" y="24" fill="#22d3ee" font-size="13" font-weight="700">Vector 7: Amphibious Infiltration &amp; Logistics</text>
      <text x="16" y="46" fill="#cbd5e1" font-size="12" font-weight="400">• Naval wars are won on the shoreline; USV transits coastal water</text>
      <text x="16" y="66" fill="#cbd5e1" font-size="12" font-weight="400">  to deploy coastal-profile (C) UGVs across surf and riverbanks.</text>
      <text x="16" y="88" fill="#cbd5e1" font-size="12" font-weight="400">• Ramp-discharge system facilitates unassisted ground beachhead capture.</text>
    </g>

    <g transform="translate(530, 86)">
      <rect width="490" height="106" rx="6" fill="#061d26" stroke="#155e75" stroke-width="1"/>
      <text x="16" y="24" fill="#22d3ee" font-size="13" font-weight="700">The USV-UGV Shared Telemetry Loop</text>
      <text x="16" y="46" fill="#cbd5e1" font-size="12" font-weight="400">• USVs provide maritime radar pickets and flank air defense screens</text>
      <text x="16" y="66" fill="#cbd5e1" font-size="12" font-weight="400">  protecting ground logistics nodes from sea-skimming threats.</text>
      <text x="16" y="88" fill="#22d3ee" font-size="12" font-weight="600">• UGV returns ground fire-control vectors to USV missile batteries.</text>
    </g>

    <g transform="translate(1036, 86)">
      <rect width="520" height="106" rx="6" fill="#061d26" stroke="#155e75" stroke-width="1"/>
      <text x="16" y="24" fill="#22d3ee" font-size="13" font-weight="700">Universal Surface Syntax: [AH] · [DE] · [PC]</text>
      <text x="16" y="46" fill="#94a3b8" font-size="11" font-weight="400">Aquatic Domain · Hydrodynamic Hull · Deploy Envelope · Power · Propulsor · Comms</text>
      <text x="16" y="70" fill="#e2e8f0" font-size="12" font-weight="500">• Planing wave-piercing hull delivers UGV payloads at 45+ knots.</text>
      <text x="16" y="90" fill="#22d3ee" font-size="12" font-weight="600">• Cross-domain gateway routes shore telemetry into satellite trunk.</text>
    </g>
  </g>

  <!-- ======================================================== -->
  <!-- VERTICAL INTEGRATION SPINE: UWE (FULL HEIGHT RIGHT)      -->
  <!-- ======================================================== -->
  <g transform="translate(1680, 220)" filter="url(#shadowBox)">
    <!-- Monolithic Spine Background -->
    <rect width="660" height="940" rx="12" fill="url(#uweSpineGrad)" stroke="#10b981" stroke-width="2.5"/>

    <!-- Spine Top Header -->
    <rect x="24" y="20" width="310" height="28" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="1.2"/>
    <text x="36" y="39" fill="#a7f3d0" font-size="13" font-weight="800" letter-spacing="1.2">VERTICAL INTEGRATION SPINE</text>

    <!-- Glowing Latency Metric -->
    <rect x="440" y="20" width="196" height="28" rx="4" fill="#047857" filter="url(#glowGreen)"/>
    <text x="538" y="39" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">KILL WEB: &lt; 1.2 s</text>

    <!-- Main Spine Title -->
    <text x="24" y="80" fill="#ffffff" font-size="24" font-weight="800">Unmanned Warfare Engine</text>
    <text x="24" y="104" fill="#6ee7b7" font-size="13" font-weight="500">Universal Meta-Operating System &amp; Hardware Abstraction Layer</text>

    <!-- ORBITAL UOV INTEGRATION CONNECTOR (TOP) -->
    <g transform="translate(24, 124)">
      <rect width="612" height="106" rx="8" fill="#022c22" stroke="#059669" stroke-width="1.2"/>
      <rect x="14" y="12" width="170" height="20" rx="4" fill="#047857"/>
      <text x="20" y="26" fill="#d1fae5" font-size="11" font-weight="700">UOV ORBITAL NEXUS</text>
      <text x="195" y="27" fill="#34d399" font-size="13" font-weight="700">LEO Tracking Layer · PWSA Direct Downlink</text>
      <text x="14" y="52" fill="#cbd5e1" font-size="12">• Bypasses radar horizon via Space Development Agency tracking layer.</text>
      <text x="14" y="72" fill="#cbd5e1" font-size="12">• Overhead ephemeris piped directly down into terrestrial UGV server.</text>
      <text x="14" y="92" fill="#6ee7b7" font-size="12" font-weight="600">→ UGV calibrates macro orbital data with micro ground-truth sensors.</text>
    </g>

    <!-- THE 4 INVARIANT LAWS OF UWE -->
    <g transform="translate(24, 246)">
      <rect width="612" height="236" rx="8" fill="#022c22" stroke="#059669" stroke-width="1.2"/>
      <text x="16" y="26" fill="#34d399" font-size="14" font-weight="800" letter-spacing="1">THE FOUR INVARIANT LAWS OF UWE</text>

      <!-- Law 1 -->
      <g transform="translate(16, 40)">
        <circle cx="10" cy="10" r="10" fill="#047857"/>
        <text x="10" y="14" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">I</text>
        <text x="30" y="14" fill="#a7f3d0" font-size="13" font-weight="700">Law of Kinematic Primacy (Physics Overrides Intent):</text>
        <text x="30" y="32" fill="#cbd5e1" font-size="11.5">No software can rescue a drone whose kinetic or thermal limits are violated.</text>
      </g>

      <!-- Law 2 -->
      <g transform="translate(16, 88)">
        <circle cx="10" cy="10" r="10" fill="#047857"/>
        <text x="10" y="14" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">II</text>
        <text x="30" y="14" fill="#a7f3d0" font-size="13" font-weight="700">Law of Hierarchical Containerization (Logistics Governs Survival):</text>
        <text x="30" y="32" fill="#cbd5e1" font-size="11.5">Robots carry robots: USV transports UGV; UGV transports &amp; stages UCV.</text>
      </g>

      <!-- Law 3 -->
      <g transform="translate(16, 136)">
        <circle cx="10" cy="10" r="10" fill="#047857"/>
        <text x="10" y="14" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">III</text>
        <text x="30" y="14" fill="#a7f3d0" font-size="13" font-weight="700">Law of Hardware Abstraction (Zero Vendor Lock-in):</text>
        <text x="30" y="32" fill="#cbd5e1" font-size="11.5">POSIX &amp; CCSDS protocol decoupling frees swarms from prime contractors.</text>
      </g>

      <!-- Law 4 -->
      <g transform="translate(16, 184)">
        <circle cx="10" cy="10" r="10" fill="#047857"/>
        <text x="10" y="14" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">IV</text>
        <text x="30" y="14" fill="#a7f3d0" font-size="13" font-weight="700">Law of Algorithmic Kill Web (Machine-Speed Fire Control):</text>
        <text x="30" y="32" fill="#cbd5e1" font-size="11.5">Humans authorize ROE rules; autonomous agents execute machine-to-machine.</text>
      </g>
    </g>

    <!-- HARDWARE ABSTRACTION LAYER (HAL / EAL) -->
    <g transform="translate(24, 498)">
      <rect width="612" height="150" rx="8" fill="#022c22" stroke="#059669" stroke-width="1.2"/>
      <text x="16" y="26" fill="#34d399" font-size="14" font-weight="800">HARDWARE ABSTRACTION LAYER (HAL &amp; EAL)</text>

      <text x="16" y="52" fill="#cbd5e1" font-size="12">• Decouples mission autonomy code from brushless ESCs, tracks, and servos.</text>
      <text x="16" y="74" fill="#cbd5e1" font-size="12">• Standardized microsecond telemetry bus handles 10,000 nodes simultaneously.</text>
      <text x="16" y="96" fill="#cbd5e1" font-size="12">• Eliminates the Replicator bottleneck: any commercial chassis can plug</text>
      <text x="16" y="116" fill="#cbd5e1" font-size="12">  into the UWE battle network and execute coordinated multi-domain fire.</text>
      <text x="16" y="138" fill="#6ee7b7" font-size="12" font-weight="600">→ Inter-Process Latency: Deterministic &lt; 1 ms on E/P-core POSIX architecture.</text>
    </g>

    <!-- CROSS-DOMAIN REAL-TIME ORCHESTRATION -->
    <g transform="translate(24, 664)">
      <rect width="612" height="252" rx="8" fill="#022c22" stroke="#059669" stroke-width="1.2"/>
      <text x="16" y="26" fill="#34d399" font-size="14" font-weight="800">WHY UWE IS VERTICALLY INVARIANT</text>

      <text x="16" y="52" fill="#a7f3d0" font-size="12.5" font-weight="700">1. Unified Sensor Fusion Matrix:</text>
      <text x="16" y="70" fill="#cbd5e1" font-size="11.5">Converts disparate data (LEO IR tracks, UCV optical flow, UGV ground lidar,</text>
      <text x="16" y="86" fill="#cbd5e1" font-size="11.5">USV navigation radar) into a single unified JSON/Protobuf tactical state vector.</text>

      <text x="16" y="112" fill="#a7f3d0" font-size="12.5" font-weight="700">2. Algorithmic ROE Compliance:</text>
      <text x="16" y="130" fill="#cbd5e1" font-size="11.5">Field commanders lock ROE boundaries on human terminals;</text>
      <text x="16" y="146" fill="#cbd5e1" font-size="11.5">UWE executes synchronized multi-domain strikes without cognitive lag.</text>

      <text x="16" y="172" fill="#a7f3d0" font-size="12.5" font-weight="700">3. Physical Domain Insulation (The UUV Exception):</text>
      <text x="16" y="190" fill="#cbd5e1" font-size="11.5">While Space, Air, Ground, and Surface communicate via RF/Optical/LEO,</text>
      <text x="16" y="206" fill="#cbd5e1" font-size="11.5">UUV operates in an isolated benthic acoustic domain, surfacing only to buoy nodes.</text>

      <rect x="16" y="222" width="580" height="20" rx="3" fill="#047857"/>
      <text x="306" y="236" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">CROSS-DOMAIN REPLICATOR READY · TRADOC &amp; AFC VALIDATED</text>
    </g>
  </g>

  <!-- ======================================================== -->
  <!-- HORIZONTAL DATA BUS CONNECTOR BEAMS                      -->
  <!-- ======================================================== -->
  <!-- Beam 1: UCV <-> UWE Spine -->
  <line x1="1640" y1="350" x2="1680" y2="350" stroke="#38bdf8" stroke-width="4" stroke-dasharray="4,2"/>
  <circle cx="1640" cy="350" r="5" fill="#38bdf8"/>
  <circle cx="1680" cy="350" r="5" fill="#34d399"/>

  <!-- Beam 2: UGV <-> UWE Spine (CENTRAL THICK HIGHLIGHT) -->
  <line x1="1640" y1="715" x2="1680" y2="715" stroke="#f59e0b" stroke-width="6"/>
  <circle cx="1640" cy="715" r="7" fill="#f59e0b" filter="url(#glowGold)"/>
  <circle cx="1680" cy="715" r="7" fill="#34d399" filter="url(#glowGreen)"/>

  <!-- Beam 3: USV <-> UWE Spine -->
  <line x1="1640" y1="1055" x2="1680" y2="1055" stroke="#06b6d4" stroke-width="4" stroke-dasharray="4,2"/>
  <circle cx="1640" cy="1055" r="5" fill="#06b6d4"/>
  <circle cx="1680" cy="1055" r="5" fill="#34d399"/>

  <!-- ======================================================== -->
  <!-- BOTTOM FOOTER & TAXONOMY SUMMARY BANNER                  -->
  <!-- ======================================================== -->
  <g transform="translate(60, 1180)">
    <rect width="2280" height="130" rx="8" fill="#0f172a" stroke="#1e293b" stroke-width="1.5"/>

    <!-- Left: Taxonomy Comparison -->
    <text x="24" y="30" fill="#38bdf8" font-size="13" font-weight="800" letter-spacing="1">THE UNIFIED MULTI-DOMAIN 6-CHARACTER TAXONOMY STANDARD:</text>

    <g transform="translate(24, 48)">
      <!-- UOV Code -->
      <rect x="0" y="0" width="370" height="36" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="12" y="23" fill="#a7f3d0" font-size="12" font-weight="700">🛰️ UOV (Space):</text>
      <text x="130" y="23" fill="#ffffff" font-size="13" font-weight="800">[OP] · [EM] · [TC]</text>

      <!-- UCV Code -->
      <rect x="390" y="0" width="370" height="36" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="402" y="23" fill="#7dd3fc" font-size="12" font-weight="700">🚁 UCV (Air Copter):</text>
      <text x="545" y="23" fill="#ffffff" font-size="13" font-weight="800">[CL] · [EB] · [AO]</text>

      <!-- UGV Code (HIGHLIGHTED GOLD) -->
      <rect x="780" y="0" width="410" height="36" rx="4" fill="#78350f" fill-opacity="0.8" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="792" y="23" fill="#fde68a" font-size="12" font-weight="800">🚜 UGV (Terrestrial):</text>
      <text x="945" y="23" fill="#ffffff" font-size="14" font-weight="900">[TK] · [DE] · [MC]</text>

      <!-- USV Code -->
      <rect x="1210" y="0" width="370" height="36" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="1222" y="23" fill="#67e8f9" font-size="12" font-weight="700">🚤 USV (Surface):</text>
      <text x="1355" y="23" fill="#ffffff" font-size="13" font-weight="800">[AH] · [DE] · [PC]</text>

      <!-- UUV Code -->
      <rect x="1600" y="0" width="370" height="36" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="1612" y="23" fill="#93c5fd" font-size="12" font-weight="700">⚓ UUV (Subsea):</text>
      <text x="1745" y="23" fill="#ffffff" font-size="13" font-weight="800">[DP] · [EM] · [TC]</text>
    </g>

    <!-- Bottom Attribution Line -->
    <text x="24" y="112" fill="#64748b" font-size="12">Doctrinal Concept &amp; System Architecture: </text>
    <text x="285" y="112" fill="#f8fafc" font-size="12" font-weight="700">Serhii Khylevych, Principal Systems Architect</text>
    <text x="560" y="112" fill="#64748b" font-size="12">| Modern War Institute at West Point Tactical Submission Asset | Unmanned Warfare Engine (UWE) v0.7.1</text>
    <text x="2256" y="112" fill="#10b981" font-size="12" font-weight="700" text-anchor="end">CLASSIFICATION: UNCLASSIFIED / OPEN ARCHITECTURE</text>
  </g>
</svg>"""

    base_dir = "/home/hills/Documents/UWS"
    svg_path = os.path.join(base_dir, "mwi_ugv_ground_kill_zone.svg")
    pdf_path = os.path.join(base_dir, "mwi_ugv_ground_kill_zone.pdf")
    png_path = os.path.join(base_dir, "mwi_ugv_ground_kill_zone.png")
    fitted_path = os.path.join(base_dir, "mwi_ugv_ground_kill_zone_fitted.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated SVG: {svg_path}")

    # Step 1: Convert SVG to PDF via LibreOffice
    print("Converting SVG to PDF via LibreOffice...")
    cmd_pdf = [
        "libreoffice",
        "-env:UserInstallation=file:///home/hills/Documents/UWS/.lo_user",
        "--headless",
        "--convert-to", "pdf:draw_pdf_Export",
        "--outdir", base_dir,
        svg_path
    ]
    subprocess.run(cmd_pdf, check=True)
    print(f"Generated PDF: {pdf_path}")

    # Step 2: Convert PDF to high-res PNG (2400 x 1350) via pdftoppm
    print("Converting PDF to high-res PNG...")
    cmd_png = [
        "pdftoppm",
        "-png",
        "-r", "150",
        pdf_path,
        os.path.join(base_dir, "mwi_ugv_tmp")
    ]
    subprocess.run(cmd_png, check=True)

    tmp_files = [f for f in os.listdir(base_dir) if f.startswith("mwi_ugv_tmp") and f.endswith(".png")]
    if tmp_files:
        tmp_file = os.path.join(base_dir, sorted(tmp_files)[0])
        os.rename(tmp_file, png_path)
        print(f"Generated high-res PNG: {png_path}")

    # Step 3: Convert PDF to fitted PNG (width 1000px) via pdftoppm
    print("Generating fitted PNG (width 1000 px)...")
    cmd_fit = [
        "pdftoppm",
        "-png",
        "-scale-to-x", "1000",
        "-scale-to-y", "-1",
        pdf_path,
        os.path.join(base_dir, "mwi_ugv_fit_tmp")
    ]
    subprocess.run(cmd_fit, check=True)

    tmp_fit_files = [f for f in os.listdir(base_dir) if f.startswith("mwi_ugv_fit_tmp") and f.endswith(".png")]
    if tmp_fit_files:
        tmp_fit_file = os.path.join(base_dir, sorted(tmp_fit_files)[0])
        os.rename(tmp_fit_file, fitted_path)
        print(f"Generated fitted PNG: {fitted_path}")

if __name__ == "__main__":
    create_svg()
