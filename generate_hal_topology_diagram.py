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

    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#030712"/>
      <stop offset="40%" stop-color="#051224"/>
      <stop offset="100%" stop-color="#08182f"/>
    </linearGradient>
    <linearGradient id="hdrGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f2544"/>
      <stop offset="100%" stop-color="#081528"/>
    </linearGradient>
    <linearGradient id="accentCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="35%" stop-color="#00b4d8"/>
      <stop offset="70%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
    <linearGradient id="busEthernetGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#00b4d8"/>
    </linearGradient>
    <linearGradient id="cardGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#091b30"/>
      <stop offset="100%" stop-color="#05101d"/>
    </linearGradient>
    <linearGradient id="cardGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c223c"/>
      <stop offset="100%" stop-color="#061220"/>
    </linearGradient>
    <pattern id="tacticalGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#10253d" stroke-width="0.6" stroke-opacity="0.4"/>
      <circle cx="36" cy="36" r="1" fill="#00d2ff" fill-opacity="0.12"/>
    </pattern>
    <marker id="arrowCyan" markerWidth="9" markerHeight="9" refX="5" refY="4.5" orient="auto">
      <polygon points="0 0, 9 4.5, 0 9, 3 4.5" fill="#00f5d4"/>
    </marker>
    <marker id="arrowSky" markerWidth="9" markerHeight="9" refX="5" refY="4.5" orient="auto">
      <polygon points="0 0, 9 4.5, 0 9, 3 4.5" fill="#38bdf8"/>
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="9" refX="5" refY="4.5" orient="auto">
      <polygon points="0 0, 9 4.5, 0 9, 3 4.5" fill="#fbbf24"/>
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="9" refX="5" refY="4.5" orient="auto">
      <polygon points="0 0, 9 4.5, 0 9, 3 4.5" fill="#f43f5e"/>
    </marker>
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
  <g transform="translate(25, 20)">
    <rect x="0" y="0" width="310" height="26" rx="5" fill="#0c2340" stroke="#00a8e8" stroke-width="1.2"/>
    <text x="155" y="18" fill="#00f5d4" class="font-sans" font-size="12.5" font-weight="700" letter-spacing="1.8" text-anchor="middle">MILTECH HARDWARE ABSTRACTION</text>
    
    <text x="0" y="60" fill="#ffffff" class="font-sans" font-size="33" font-weight="900" letter-spacing="0.5">HAL LLD: SYSTEM BUS &amp; DRIVER TOPOLOGY</text>
    <text x="0" y="92" fill="#94a3b8" class="font-sans" font-size="18">
      Deterministic Edge-to-Actuator Decoupling: <tspan fill="#00f5d4" font-weight="700">Mission Microservices</tspan>, <tspan fill="#38bdf8" font-weight="700">MCU/FPGA Gateway</tspan> &amp; <tspan fill="#fbbf24" font-weight="700">Isolated Physical Buses</tspan>
    </text>

    <!-- Top Right Meta Card -->
    <g transform="translate(1720, 2)">
      <rect x="0" y="0" width="630" height="96" rx="7" fill="#09182a" stroke="#1d385c" stroke-width="1.3"/>
      <text x="20" y="27" fill="#38bdf8" class="font-sans" font-size="14.5" font-weight="700" letter-spacing="0.8">HAL INVARIANT FAULT-ISOLATION LAW</text>
      <text x="20" y="52" fill="#cbd5e1" class="font-sans" font-size="14.5">"Mission OS crash must never cause physical loss of control or misfire."</text>
      <text x="20" y="78" fill="#94a3b8" class="font-sans" font-size="13.5">MCU/FPGA hardware safety FSM operates fully autonomous from Linux/ROS2.</text>
    </g>
  </g>

  <!-- ==================== OUTER SYSTEM CHASSIS FRAME ==================== -->
  <rect x="25" y="130" width="2350" height="1005" rx="10" fill="#050d1a" stroke="#142842" stroke-width="1.3"/>

  <!-- Tactical Corner Crosshairs -->
  <path d="M 40 145 L 55 145 M 40 145 L 40 160" stroke="#00f5d4" stroke-width="2" fill="none"/>
  <path d="M 2360 145 L 2345 145 M 2360 145 L 2360 160" stroke="#00f5d4" stroke-width="2" fill="none"/>
  <path d="M 40 1120 L 55 1120 M 40 1120 L 40 1105" stroke="#00f5d4" stroke-width="2" fill="none"/>
  <path d="M 2360 1120 L 2345 1120 M 2360 1120 L 2360 1105" stroke="#00f5d4" stroke-width="2" fill="none"/>


  <!-- ====================================================================== -->
  <!-- TIER 1: MISSION COMPUTER (EDGE AI / OS)                                -->
  <!-- ====================================================================== -->
  <g transform="translate(55, 150)">
    <!-- Container -->
    <rect x="0" y="0" width="2290" height="160" rx="8" fill="url(#cardGrad1)" stroke="#00a8e8" stroke-width="1.5"/>
    <line x1="0" y1="0" x2="2290" y2="0" stroke="#00f5d4" stroke-width="3.5"/>

    <!-- Left Header Section -->
    <g transform="translate(24, 24)">
      <rect x="0" y="0" width="230" height="24" rx="4" fill="#08223d" stroke="#00b4d8" stroke-width="1.1"/>
      <text x="115" y="17" fill="#00f5d4" class="font-sans" font-size="11.5" font-weight="800" letter-spacing="1.4" text-anchor="middle">TIER 1 • NON-DETERMINISTIC OS</text>
      
      <text x="0" y="58" fill="#ffffff" class="font-sans" font-size="24" font-weight="900" letter-spacing="0.5">🧠 MISSION COMPUTER (EDGE AI / OS)</text>
      <text x="0" y="86" fill="#94a3b8" class="font-sans" font-size="15">NVIDIA Jetson AGX Orin / Rockchip RK3588 • Ubuntu Linux / ROS2 Node Architecture</text>
      <text x="0" y="112" fill="#38bdf8" class="font-sans" font-size="14" font-weight="600">Runtime Decorators: Lethality, OWM Nav, Target Classification &amp; Swarm Consensus</text>
    </g>

    <!-- 4 Combat Microservice Cards -->
    <!-- Available width from x=760 to 2266 (width = 1506). 4 cards of width 362, gap = 19 -->
    <!-- Card 1: Kill Web -->
    <g transform="translate(760, 20)">
      <rect x="0" y="0" width="362" height="120" rx="6" fill="#091729" stroke="#1d3c63" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="120" rx="2" fill="#f43f5e"/>
      <g transform="translate(16, 26)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="800">🎯 Kill Web Microservice</text>
        <text x="0" y="25" fill="#f87171" class="font-mono" font-size="12.5" font-weight="700">SERVICE_UID: 0x01_KILLWEB</text>
        <text x="0" y="49" fill="#cbd5e1" class="font-sans" font-size="13.5">Terminal target track &amp; lock</text>
        <text x="0" y="70" fill="#94a3b8" class="font-sans" font-size="12.5">Kinematic trajectory generation</text>
      </g>
    </g>

    <!-- Card 2: EVAC -->
    <g transform="translate(1141, 20)">
      <rect x="0" y="0" width="362" height="120" rx="6" fill="#091729" stroke="#1d3c63" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="120" rx="2" fill="#00f5d4"/>
      <g transform="translate(16, 26)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="800">🚑 EVAC &amp; Logistic Service</text>
        <text x="0" y="25" fill="#2dd4bf" class="font-mono" font-size="12.5" font-weight="700">SERVICE_UID: 0x02_EVAC_LOG</text>
        <text x="0" y="49" fill="#cbd5e1" class="font-sans" font-size="13.5">Casualty waypoint navigation</text>
        <text x="0" y="70" fill="#94a3b8" class="font-sans" font-size="12.5">Safe corridor return-to-base</text>
      </g>
    </g>

    <!-- Card 3: Tabor -->
    <g transform="translate(1522, 20)">
      <rect x="0" y="0" width="362" height="120" rx="6" fill="#091729" stroke="#1d3c63" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="120" rx="2" fill="#38bdf8"/>
      <g transform="translate(16, 26)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="800">🛡️ Tabor Autonomous Swarm</text>
        <text x="0" y="25" fill="#38bdf8" class="font-mono" font-size="12.5" font-weight="700">SERVICE_UID: 0x03_TABOR_C2</text>
        <text x="0" y="49" fill="#cbd5e1" class="font-sans" font-size="13.5">Distributed mesh consensus</text>
        <text x="0" y="70" fill="#94a3b8" class="font-sans" font-size="12.5">Collaborative picket &amp; relay</text>
      </g>
    </g>

    <!-- Card 4: Breaching -->
    <g transform="translate(1903, 20)">
      <rect x="0" y="0" width="362" height="120" rx="6" fill="#091729" stroke="#1d3c63" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="120" rx="2" fill="#fbbf24"/>
      <g transform="translate(16, 26)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="800">💥 Breaching &amp; Assault</text>
        <text x="0" y="25" fill="#fbbf24" class="font-mono" font-size="12.5" font-weight="700">SERVICE_UID: 0x04_BREACH</text>
        <text x="0" y="49" fill="#cbd5e1" class="font-sans" font-size="13.5">Barrier / mine clearing FSM</text>
        <text x="0" y="70" fill="#94a3b8" class="font-sans" font-size="12.5">Multi-vector kinetic strike</text>
      </g>
    </g>
  </g>


  <!-- ====================================================================== -->
  <!-- BUS 1: HIGH-SPEED ETHERNET 100BASE-T1 / TSN CONDUIT                    -->
  <!-- ====================================================================== -->
  <!-- Vertical Bus Conduit Lines -->
  <g transform="translate(0, 0)">
    <!-- Main spine left & right pipelines -->
    <line x1="1185" y1="310" x2="1185" y2="430" stroke="#00f5d4" stroke-width="3" stroke-dasharray="8 4"/>
    <line x1="1215" y1="310" x2="1215" y2="430" stroke="#00f5d4" stroke-width="3" stroke-dasharray="8 4"/>
    
    <!-- Central Data Highway Pipe Badge -->
    <g transform="translate(760, 335)">
      <rect x="0" y="0" width="880" height="70" rx="8" fill="#061626" stroke="#00f5d4" stroke-width="1.8"/>
      
      <!-- Connector Port Dots -->
      <circle cx="16" cy="35" r="5" fill="#00f5d4"/>
      <circle cx="864" cy="35" r="5" fill="#00f5d4"/>

      <!-- Content -->
      <g transform="translate(35, 27)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="900" letter-spacing="0.5">⚡ HIGH-SPEED ETHERNET 100BASE-T1 / TSN (TIME-SENSITIVE NETWORKING)</text>
        <text x="0" y="26" fill="#94a3b8" class="font-sans" font-size="14.5">
          IEEE 802.1Qbv Deterministic Traffic Shaper • Real-Time C2 Telemetry &amp; Payload Routing • <tspan fill="#00f5d4" font-weight="700">&lt;500 µs Bounded Latency</tspan>
        </text>
      </g>
    </g>

    <!-- Downward Arrow Indicator into Tier 2 -->
    <polygon points="1200,430 1192,416 1208,416" fill="#00f5d4"/>
  </g>


  <!-- ====================================================================== -->
  <!-- TIER 2: HAL CONTROLLER GATEWAY (MCU / FPGA CORE)                       -->
  <!-- ====================================================================== -->
  <g transform="translate(55, 430)">
    <!-- Container -->
    <rect x="0" y="0" width="2290" height="240" rx="8" fill="url(#cardGrad2)" stroke="#38bdf8" stroke-width="1.6"/>
    <line x1="0" y1="0" x2="2290" y2="0" stroke="#38bdf8" stroke-width="3.5"/>

    <!-- Header / Banner Section inside Tier 2 -->
    <g transform="translate(24, 20)">
      <rect x="0" y="0" width="330" height="24" rx="4" fill="#08223d" stroke="#38bdf8" stroke-width="1.1"/>
      <text x="165" y="17" fill="#38bdf8" class="font-sans" font-size="11.5" font-weight="800" letter-spacing="1.4" text-anchor="middle">TIER 2 • HARD REAL-TIME DETERMINISTIC GATEWAY</text>

      <text x="350" y="18" fill="#ffffff" class="font-sans" font-size="22" font-weight="900">🎛️ HAL CONTROLLER GATEWAY (MCU / FPGA CORE)</text>
      <text x="960" y="18" fill="#94a3b8" class="font-sans" font-size="15">Lockstep ARM Cortex-M7 (STM32H7) / Xilinx Zynq FPGA • Bare-Metal FreeRTOS • 100% Invariant Safety Loops</text>
    </g>

    <!-- 3 Subsystem Controller FSM Cards -->
    <!-- Total width 2240 inside (left=25, gap=20). 3 cards: (2240 - 40) / 3 = 733 px each -->
    
    <!-- Card 1: Kinematics Driver -->
    <g transform="translate(25, 56)">
      <rect x="0" y="0" width="733" height="164" rx="7" fill="#091b2c" stroke="#00f5d4" stroke-width="1.4"/>
      <rect x="0" y="0" width="5" height="164" rx="2" fill="#00f5d4"/>
      
      <g transform="translate(22, 28)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="20" font-weight="800">⚙️ Kinematics Driver &amp; Motion FSM</text>
        <text x="0" y="27" fill="#00f5d4" class="font-mono" font-size="13.5" font-weight="700">LOOP_RATE: 1,000 Hz (1 ms) • HARD REAL-TIME</text>
        
        <text x="0" y="55" fill="#e2e8f0" class="font-sans" font-size="14.5">• Closed-loop attitude, yaw/pitch rate &amp; vector kinematics</text>
        <text x="0" y="78" fill="#cbd5e1" class="font-sans" font-size="14">• Hardware DShot600 / PWM pulse generator &amp; ESC telemetry</text>
        <text x="0" y="101" fill="#94a3b8" class="font-sans" font-size="14">• Invariant anti-stall, altitude-floor &amp; obstacle avoidance FSM</text>
      </g>
    </g>

    <!-- Card 2: BMS / Power FSM -->
    <g transform="translate(778, 56)">
      <rect x="0" y="0" width="733" height="164" rx="7" fill="#091b2c" stroke="#fbbf24" stroke-width="1.4"/>
      <rect x="0" y="0" width="5" height="164" rx="2" fill="#fbbf24"/>
      
      <g transform="translate(22, 28)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="20" font-weight="800">🔋 BMS / Power Management FSM</text>
        <text x="0" y="27" fill="#fbbf24" class="font-mono" font-size="13.5" font-weight="700">LOOP_RATE: 100 Hz (10 ms) • THERMAL &amp; RAIL SAFETY</text>
        
        <text x="0" y="55" fill="#e2e8f0" class="font-sans" font-size="14.5">• Dynamic load shedding &amp; prioritized brownout prevention</text>
        <text x="0" y="78" fill="#cbd5e1" class="font-sans" font-size="14">• Multi-pack Li-ion/LiFePO4 cell balancing &amp; thermals monitoring</text>
        <text x="0" y="101" fill="#94a3b8" class="font-sans" font-size="14">• Ultra-low power sleeper mode FSM (&lt;5 mA deep sleep standby)</text>
      </g>
    </g>

    <!-- Card 3: Payload & Detonation FSM -->
    <g transform="translate(1531, 56)">
      <rect x="0" y="0" width="734" height="164" rx="7" fill="#091b2c" stroke="#f43f5e" stroke-width="1.4"/>
      <rect x="0" y="0" width="5" height="164" rx="2" fill="#f43f5e"/>
      
      <g transform="translate(22, 28)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="20" font-weight="800">🎯 Payload &amp; Detonation FSM</text>
        <text x="0" y="27" fill="#f87171" class="font-mono" font-size="13.5" font-weight="700">STANAG 4754 (NGVA) • DUAL-KEY HARDWARE ARMING</text>
        
        <text x="0" y="55" fill="#e2e8f0" class="font-sans" font-size="14.5">• Hardware Safety &amp; Arming Device (ESAD) dual-switch logic</text>
        <text x="0" y="78" fill="#cbd5e1" class="font-sans" font-size="14">• Independent mechanical &amp; optocoupler detonation interlocks</text>
        <text x="0" y="101" fill="#94a3b8" class="font-sans" font-size="14">• EO/IR thermal gimbal stabilization &amp; laser target illuminator C2</text>
      </g>
    </g>
  </g>


  <!-- ====================================================================== -->
  <!-- BUS 2: THREE ISOLATED DETERMINISTIC FIELD BUS CONDUITS                 -->
  <!-- ====================================================================== -->
  <!-- Branch 1 (CAN-FD Bus) -->
  <g transform="translate(0, 0)">
    <!-- Vertical Data Pipes -->
    <line x1="446" y1="670" x2="446" y2="780" stroke="#00f5d4" stroke-width="2.5" stroke-dasharray="6 3"/>
    
    <!-- Bus Badge -->
    <g transform="translate(160, 692)">
      <rect x="0" y="0" width="573" height="66" rx="7" fill="#071828" stroke="#00f5d4" stroke-width="1.4"/>
      <g transform="translate(20, 26)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="800">⚡ CAN-FD BUS (ISO 11898-1)</text>
        <text x="0" y="24" fill="#00f5d4" class="font-sans" font-size="13.5">5 Mbps High-Speed • Cyclic CRC-17 • High-EMC Motion Bus</text>
      </g>
    </g>
    <!-- Downward Arrow into Pod 1 -->
    <polygon points="446,780 438,768 454,768" fill="#00f5d4"/>
  </g>

  <!-- Branch 2 (PMBus / I2C / SPI Bus) -->
  <g transform="translate(0, 0)">
    <!-- Vertical Data Pipes -->
    <line x1="1200" y1="670" x2="1200" y2="780" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6 3"/>
    
    <!-- Bus Badge -->
    <g transform="translate(913, 692)">
      <rect x="0" y="0" width="574" height="66" rx="7" fill="#071828" stroke="#fbbf24" stroke-width="1.4"/>
      <g transform="translate(20, 26)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="800">⚡ PMBus / I2C / SPI SYSTEM BUS</text>
        <text x="0" y="24" fill="#fbbf24" class="font-sans" font-size="13.5">SMBus 1.3 • Direct Sensor Telemetry &amp; Power Rail Control</text>
      </g>
    </g>
    <!-- Downward Arrow into Pod 2 -->
    <polygon points="1200,780 1192,768 1208,768" fill="#fbbf24"/>
  </g>

  <!-- Branch 3 (STANAG 4754 / RS-485 Bus) -->
  <g transform="translate(0, 0)">
    <!-- Vertical Data Pipes -->
    <line x1="1953" y1="670" x2="1953" y2="780" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6 3"/>
    
    <!-- Bus Badge -->
    <g transform="translate(1666, 692)">
      <rect x="0" y="0" width="574" height="66" rx="7" fill="#071828" stroke="#f43f5e" stroke-width="1.4"/>
      <g transform="translate(20, 26)">
        <text x="0" y="0" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="800">⚡ STANAG 4754 / RS-485 BUS</text>
        <text x="0" y="24" fill="#f87171" class="font-sans" font-size="13.5">NATO Generic Vehicle Architecture • Differential Weapon &amp; Gimbal C2</text>
      </g>
    </g>
    <!-- Downward Arrow into Pod 3 -->
    <polygon points="1953,780 1945,768 1961,768" fill="#f43f5e"/>
  </g>


  <!-- ====================================================================== -->
  <!-- TIER 3: PHYSICAL ACTUATORS & HARDWARE PAYLOADS                         -->
  <!-- ====================================================================== -->
  <!-- Pod 1: Motor ESCs & Servo Actuators -->
  <g transform="translate(80, 780)">
    <rect x="0" y="0" width="733" height="330" rx="8" fill="#081726" stroke="#00f5d4" stroke-width="1.5"/>
    <rect x="0" y="0" width="733" height="46" rx="8" fill="#0a2538"/>
    <line x1="0" y1="46" x2="733" y2="46" stroke="#00f5d4" stroke-width="1.5"/>
    
    <text x="22" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="900">🔩 MOTOR ESCs &amp; SERVO ACTUATORS</text>
    <text x="710" y="30" fill="#00f5d4" class="font-mono" font-size="13" font-weight="800" text-anchor="end">PROPULSION / DRIVE</text>

    <!-- Sub-elements list -->
    <g transform="translate(24, 76)">
      <!-- Item 1 -->
      <rect x="0" y="0" width="685" height="52" rx="5" fill="#061220" stroke="#13334d" stroke-width="1"/>
      <text x="16" y="24" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Multi-Axis BLDC Electronic Speed Controllers (ESCs)</text>
      <text x="16" y="43" fill="#00f5d4" class="font-sans" font-size="13">FOC 32-bit MCU per motor • RPM feedback • Phase current sensing</text>

      <!-- Item 2 -->
      <rect x="0" y="60" width="685" height="52" rx="5" fill="#061220" stroke="#13334d" stroke-width="1"/>
      <text x="16" y="84" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Digital CAN-FD Flight &amp; Steering Servos</text>
      <text x="16" y="103" fill="#94a3b8" class="font-sans" font-size="13">Titanium gearboxes • Brushless core • Deflection angle telemetry</text>

      <!-- Item 3 -->
      <rect x="0" y="120" width="685" height="52" rx="5" fill="#061220" stroke="#13334d" stroke-width="1"/>
      <text x="16" y="144" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Domain Physical Effectors</text>
      <text x="16" y="163" fill="#94a3b8" class="font-sans" font-size="13">UAV prop rotors • USV tunnel waterjets • UGV track motors • UUV thruster pods</text>

      <!-- Item 4 -->
      <rect x="0" y="180" width="685" height="52" rx="5" fill="#061220" stroke="#13334d" stroke-width="1"/>
      <text x="16" y="204" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Hardware Telemetry Bus Return</text>
      <text x="16" y="223" fill="#94a3b8" class="font-sans" font-size="13">Real-time thermal monitoring • Motor vibration • ESC health diagnostics</text>
    </g>
  </g>

  <!-- Pod 2: Bidirectional Power Rail BMS -->
  <g transform="translate(833, 780)">
    <rect x="0" y="0" width="733" height="330" rx="8" fill="#081726" stroke="#fbbf24" stroke-width="1.5"/>
    <rect x="0" y="0" width="733" height="46" rx="8" fill="#2d2208"/>
    <line x1="0" y1="46" x2="733" y2="46" stroke="#fbbf24" stroke-width="1.5"/>
    
    <text x="22" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="900">⚡ BIDIRECTIONAL POWER RAIL BMS</text>
    <text x="710" y="30" fill="#fbbf24" class="font-mono" font-size="13" font-weight="800" text-anchor="end">ENERGY / POWER</text>

    <!-- Sub-elements list -->
    <g transform="translate(24, 76)">
      <!-- Item 1 -->
      <rect x="0" y="0" width="685" height="52" rx="5" fill="#061220" stroke="#3d3013" stroke-width="1"/>
      <text x="16" y="24" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Smart Battery Management System (BMS)</text>
      <text x="16" y="43" fill="#fbbf24" class="font-sans" font-size="13">Multi-cell Li-ion / LiFePO4 / Solid-State packs • Active cell balancing</text>

      <!-- Item 2 -->
      <rect x="0" y="60" width="685" height="52" rx="5" fill="#061220" stroke="#3d3013" stroke-width="1"/>
      <text x="16" y="84" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Isolated DC-DC Regulated Rails (3.3V / 5V / 12V / 24V)</text>
      <text x="16" y="103" fill="#94a3b8" class="font-sans" font-size="13">Low-noise avionics supply • Solid-state e-fuses with microsecond trip</text>

      <!-- Item 3 -->
      <rect x="0" y="120" width="685" height="52" rx="5" fill="#061220" stroke="#3d3013" stroke-width="1"/>
      <text x="16" y="144" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">V2V Bidirectional Charging &amp; Power Bus</text>
      <text x="16" y="163" fill="#94a3b8" class="font-sans" font-size="13">Tethered drone power supply • Vehicle-to-vehicle field energy donation</text>

      <!-- Item 4 -->
      <rect x="0" y="180" width="685" height="52" rx="5" fill="#061220" stroke="#3d3013" stroke-width="1"/>
      <text x="16" y="204" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Fail-Safe Hardware Energy Isolation</text>
      <text x="16" y="223" fill="#94a3b8" class="font-sans" font-size="13">Thermal runaway containment • Reverse polarity protection • Sleep FSM</text>
    </g>
  </g>

  <!-- Pod 3: Modular Weapon & Sensor Payloads -->
  <g transform="translate(1586, 780)">
    <rect x="0" y="0" width="734" height="330" rx="8" fill="#081726" stroke="#f43f5e" stroke-width="1.5"/>
    <rect x="0" y="0" width="734" height="46" rx="8" fill="#300d16"/>
    <line x1="0" y1="46" x2="734" y2="46" stroke="#f43f5e" stroke-width="1.5"/>
    
    <text x="22" y="30" fill="#ffffff" class="font-sans" font-size="18.5" font-weight="900">🎯 MODULAR WEAPON / SENSOR PAYLOADS</text>
    <text x="710" y="30" fill="#f87171" class="font-mono" font-size="13" font-weight="800" text-anchor="end">LETHALITY / ISR</text>

    <!-- Sub-elements list -->
    <g transform="translate(24, 76)">
      <!-- Item 1 -->
      <rect x="0" y="0" width="685" height="52" rx="5" fill="#061220" stroke="#4d1624" stroke-width="1"/>
      <text x="16" y="24" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Electronic Safety &amp; Arming Device (ESAD)</text>
      <text x="16" y="43" fill="#f87171" class="font-sans" font-size="13">Dual-key optical/electronic arming • Invariant fuze safety &amp; detonation</text>

      <!-- Item 2 -->
      <rect x="0" y="60" width="685" height="52" rx="5" fill="#061220" stroke="#4d1624" stroke-width="1"/>
      <text x="16" y="84" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Precision Kinetic Warheads &amp; Munitions</text>
      <text x="16" y="103" fill="#94a3b8" class="font-sans" font-size="13">Shaped-charge RPG / PBX demolition blocks / Automated turret breech</text>

      <!-- Item 3 -->
      <rect x="0" y="120" width="685" height="52" rx="5" fill="#061220" stroke="#4d1624" stroke-width="1"/>
      <text x="16" y="144" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Multi-Spectral Stabilized EO/IR Gimbals</text>
      <text x="16" y="163" fill="#94a3b8" class="font-sans" font-size="13">Thermal LWIR / MWIR uncooled cores • Laser rangefinder / target pointer</text>

      <!-- Item 4 -->
      <rect x="0" y="180" width="685" height="52" rx="5" fill="#061220" stroke="#4d1624" stroke-width="1"/>
      <text x="16" y="204" fill="#ffffff" class="font-sans" font-size="15" font-weight="700">Special EW &amp; Acoustic Payloads</text>
      <text x="16" y="223" fill="#94a3b8" class="font-sans" font-size="13">RF jamming pods • Dipping active/passive sonar buoys • Fiber optic spools</text>
    </g>
  </g>


  <!-- ==================== BOTTOM ARCHITECTURAL STRIP ==================== -->
  <g transform="translate(25, 1150)">
    <rect x="0" y="0" width="2350" height="92" rx="7" fill="#081422" stroke="#182f4e" stroke-width="1.2"/>
    
    <g transform="translate(24, 18)">
      <circle cx="12" cy="12" r="7" fill="#00f5d4"/>
      <text x="30" y="17" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="700">Hardware Fail-Safe Decoupling:</text>
      <text x="30" y="42" fill="#94a3b8" class="font-sans" font-size="14">Bare-metal MCU/FPGA maintains flight stabilization &amp; safety envelopes</text>
      <text x="30" y="62" fill="#94a3b8" class="font-sans" font-size="14">even during total Mission Linux / ROS2 crash or kernel panic.</text>
    </g>

    <g transform="translate(810, 18)">
      <circle cx="12" cy="12" r="7" fill="#38bdf8"/>
      <text x="30" y="17" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="700">Deterministic Time-Sensitive Bus (TSN):</text>
      <text x="30" y="42" fill="#94a3b8" class="font-sans" font-size="14">High-bandwidth vision &amp; AI streams (100BASE-T1) are strictly isolated</text>
      <text x="30" y="62" fill="#94a3b8" class="font-sans" font-size="14">from microsecond actuator commands &amp; motion loops (CAN-FD).</text>
    </g>

    <g transform="translate(1620, 18)">
      <circle cx="12" cy="12" r="7" fill="#fbbf24"/>
      <text x="30" y="17" fill="#ffffff" class="font-sans" font-size="16.5" font-weight="700">Universal Cross-Domain Interoperability:</text>
      <text x="30" y="42" fill="#94a3b8" class="font-sans" font-size="14">Identical 3-tier HAL topology runs without modification across Space (UOV),</text>
      <text x="30" y="62" fill="#94a3b8" class="font-sans" font-size="14">Air (UAV/UCV), Ground (UGV), Maritime Surface (USV) &amp; Subsea (UUV).</text>
    </g>
  </g>


  <!-- ==================== FOOTER ==================== -->
  <g transform="translate(25, 1324)">
    <line x1="0" y1="0" x2="2350" y2="0" stroke="#14263b" stroke-width="1.2"/>
    <text x="0" y="18" fill="#64748b" class="font-sans" font-size="13.5" font-weight="700" letter-spacing="1.2">UNMANNED WARFARE ENGINE (UWE)</text>
    <text x="290" y="18" fill="#334155" class="font-sans" font-size="13.5">•</text>
    <text x="308" y="18" fill="#94a3b8" class="font-sans" font-size="13.5">SECTION 4.2: HAL LLD SYSTEM BUS &amp; DRIVER TOPOLOGY</text>
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
    print("=== Generating HAL LLD System Bus & Driver Topology Diagram ===")
    svg_content = create_svg()
    export_file("uwe_hal_lld_topology", svg_content)
