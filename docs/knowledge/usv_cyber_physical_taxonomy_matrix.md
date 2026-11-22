# USV Cyber-Physical Taxonomy Matrix Specification
## Monolithic 6-Character Standard: `[ H K ] - [ E M ] - [ D C ]`

> **Document Type:** Canonical UWE Knowledge Base Reference  
> **Domain:** Unmanned Surface Vehicles (USV)  
> **Author:** Serhii Khylevych (Kyiv Baseline)

---

## 1. Architectural Foundation & Marine Physics

The ocean air-sea boundary layer is dictated by:
1. **Vertical Wave Slamming ($G_z$):** $G_z \propto V^2 / B$ under Savitsky formulation. Planing craft in Sea State 4+ suffer destructive shocks (>6-8g).
2. **Decoupled Lethality:** Hull is an invariant carrier; payload (OWM warhead, C-UAS rail, sonar, cargo) is a modular kit.
3. **EW Resiliency:** Multi-bearer fallback (SATCOM $\rightarrow$ Mesh RF $\rightarrow$ Quiet ATR $\rightarrow$ Fiber).

---

## 2. Matrix Structure: `[ H K ] - [ E M ] - [ D C ]`

```
[ H K ]  -  [ E M ]  -  [ D C ]
   │            │            │
   │            │            └─ OCTET 3: Tactical Doctrine & Comms
   │            └────────────── OCTET 2: Powerplant & Mission Mode
   └─────────────────────────── OCTET 1: Hydrodynamics & Container
```

---

## 3. Detailed Character Definitions

### OCTET 1: Hydrodynamic Form & Containerization `[ H K ]`

#### Character 1: Hull Hydrodynamic Form (`H`)
* **P (Planing Monohull):** V-shaped hard-chine monohull ($\beta > 18^\circ$, $Fn > 1.0$), sprint 50–70+ kts. High shock accelerations in waves.
* **W (Wave-Piercing Slender):** Ultra-narrow displacement monohull, knife bow. Stable in Sea State 5+ ($G_z < 1.5g$), low wave signature.
* **S (Semi-Submersible / Low-Freeboard):** Ballast-flooded hull, near-zero freeboard. Low optical/radar cross-section, reduced wave slam.
* **C (Catamaran / Multihull):** Multi-hull platform with high transverse metacentric height ($GM_T$). Stable droneport or weapon mount.
* **F (Hydrofoil / SES):** Hydrofoils or surface effect air cavity. Extreme dash (>70 kts) decoupling hull from wave impacts.

#### Character 2: Carrier Class & Containerization (`K`)
* **P (Portable / Squad $C_1$):** Ultralight hull (<4m, <300 kg), beach slipway, inflatable craft (RIB) launch.
* **T (Trailer / Slipway $C_2$):** Standard road trailer or coastal slipway (5–8m, 1–3t, Magura/Sea Baby tier).
* **V (Vessel Davit / Crane $C_3$):** Mothership launch via crane/davit from frigates, corvettes, or tenders.
* **W (Well-Deck / Amphibious Dock $C_3/C_4$):** Autonomous underway ingress into flooded warship well-decks (LHD/LPD).
* **B (Bunker / Coastal Pen $C_4$):** Hardened rock pens, underground maritime tunnels, concrete coastal installations.

---

### OCTET 2: Powerplant Propulsion & Operational Mission `[ E M ]`

#### Character 3: Powerplant Architecture (`E`)
* **P (Petrol ICE + Waterjet):** Marine gasoline ICE with waterjet and reversing bucket. Max sprint, shallow water agility.
* **D (Marine Diesel Inboard):** Heavy fuel diesel inboard. Extreme range (600–2000 nmi), high continuous duty.
* **E (Battery Electric):** Pure electrochemical storage. Thermal/acoustic silence, stealth ingress (10–30 nmi).
* **H (Hybrid Diesel-Electric):** Diesel generator + battery buffer. Silent loiter + high-speed transit.
* **T (Gas Turbine):** Marine gas turbine. Extreme power-to-weight for ultra-high-speed sprint.
* **S (Solar / Wave Harvesting):** Unpowered renewable harvesting (Saildrone, months of persistent patrol).

#### Character 4: Operational Mission Kit (`M`)
* **K (Kinetic Impact / OWM):** One-Way Mission with shaped charge/HE warhead (250–850 kg) against capital ships.
* **A (Anti-Air / C-UAS Platform):** Air defense payload with SAM rails (R-73, Mistral) or FPV anti-air interceptors.
* **S (Sensor ASW / ISR):** Dipping sonars, towed acoustic arrays, magnetometers, surface search radar.
* **L (Logistics / UNREP):** Autonomous cargo, ammo resupply, and underway well-deck replenishment.
* **M (Mine Countermeasures / MCM):** Acoustic/magnetic mine sweepers, minehunting ROV/AUV deployment.
* **C (Carrier Mothership):** Deployment platform and charging hub for aerial drone swarms (UAV/UCV).

---

### OCTET 3: Tactical Doctrine & Signal Backbone `[ D C ]`

#### Character 5: Autonomous Doctrine (`D`)
* **W (Wolfpack Coordinated Swarm):** Decentralized multi-agent swarm logic, multi-axis pincer strikes.
* **H (Hunter Solo):** Fully autonomous predatory trackline search and engagement without human commands.
* **A (Autonomous Precision Docking):** Closed-loop relative velocity matching and underway docking.
* **R (Remote Teleoperation):** Operator-in-the-loop low-latency video teleoperation.
* **P (Patrol / Loitering Sentry):** Low-power anchor/drift loiter (*Zhdun*) awaiting target acoustic trigger.

#### Character 6: Communications Media (`C`)
* **S (LEO Multi-SATCOM):** Dual Starlink/OneWeb/Kymeta phased array terminals.
* **M (Mesh Tactical RF SDR):** Tactical MIMO/COFDM SDR datalinks (Silvus, Doodle Labs).
* **Q (Quiet / RF-Silent):** Absolute radio silence. Pure optical ATR, LiDAR, and INS dead-reckoning.
* **L (Laser Crosslink):** Line-of-sight laser transceivers between vessels or coastal nodes.
* **F (Fiber-Optic Tether):** Micro-fiber optic spool for EW-immune close-range operations.

---

## 4. Empirical Benchmark Validation

| Platform | Domain Token | Verified Architecture & Mission |
|---|---|---|
| **Magura V5** | `USV: PT-PK-WS` | Planing, Trailer, Petrol ICE waterjet, Kinetic OWM, Wolfpack swarm, LEO SATCOM |
| **Sea Baby** | `USV: ST-PK-WS` | Semi-submersible low-freeboard, Trailer, Petrol waterjet, Kinetic, Wolfpack, SATCOM |
| **Exail DriX** | `USV: WV-DS-HA` | Wave-piercing slender, Vessel crane, Diesel, ASW sensor, Hunter, Autonomous/SATCOM |
| **Typhoon USV (Splash)** | `USV: PW-PL-AQ` | Planing, Well-deck dock, Petrol waterjet, Logistics UNREP, Autonomous docking, Quiet |
| **Saildrone Explorer** | `USV: WT-SS-PS` | Wave-piercing, Trailer/harbor, Solar/wind, Sensor ISR, Patrol sentry, LEO SATCOM |






