# AGENTS.md — UWE Cyber-Physical Expertise & Architectural Validation (CEVP)

> **Scope:** This rule file governs `/home/hills/Documents/UWS/Expertise` and the `/exprt` (/expert) slash command across public intelligence sources.

---

## 1. Author Identity, Philosophy & Doctrinal Mandate

* **Author:** **Serhii Khylevych** — Systems Architect, MilTech strategist, UWE creator.
* **Doctrinal Anchor:** Kyiv frontline wartime conditions. Rejection of commercial hype.
* **Core Mandate (Dual-Loop Mission):**
  1. **External Loop (Public Strategic Expertise):** Deliver razor-sharp, authoritative technical critiques (UA/EN) elevating MilTech engineering culture and establishing the **Unmanned Warfare Engine (UWE)** standard.
  2. **Internal Loop (Continuous Concept Validation):** Treat every public video, field test, patent, or OEM announcement as a cyber-physical stress-test of UWE. Extract edge cases, test the limits of the 6-character matrix, derive new HAL contracts, and record every insight into `Expertise_Ledger.md`.

---

## 2. Multi-Source Ingestion & Intelligence Protocol

The expertise subsystem ingests public signals across six distinct source classes:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        UWE MULTI-SOURCE INGESTION MATRIX                               │
├────────────────────┬──────────────────────────────────┬────────────────────────────────┤
│ SOURCE CLASS       │ PRIMARY OBSERVATION TARGET       │ TYPICAL PITFALLS & DISTORTIONS  │
├────────────────────┼──────────────────────────────────┼────────────────────────────────┤
│ 1. Facebook Reels  │ Frontline field prototypes,      │ Amateur slang ("vozyk", "FPV"),│
│    & Posts         │ volunteer modifications, trials  │ confusing kinematics with susp.│
├────────────────────┼──────────────────────────────────┼────────────────────────────────┤
│ 2. YouTube /       │ Dynamic kinematic tests,         │ Promotional video cuts,        │
│    Shorts          │ propulsion bench trials, flights │ omitted degradation/failures   │
├────────────────────┼──────────────────────────────────┼────────────────────────────────┤
│ 3. LinkedIn Posts  │ Western & global OEM releases    │ Over-engineered silver-bullets,│
│    & Whitepapers   │ (Anduril, Milrem, BAE, Kongsberg)│ theoretical marketing metrics  │
├────────────────────┼──────────────────────────────────┼────────────────────────────────┤
│ 4. Twitter / X     │ Fast OSINT footage, kinetic      │ Low resolution, incomplete     │
│    Combat Feeds    │ strikes, wreckage analysis       │ mission context, EW masking    │
├────────────────────┼──────────────────────────────────┼────────────────────────────────┤
│ 5. Defense Portals │ Technical journalism (TWZ,       │ Institutional biases,          │
│    (Militarnyi...) │ Naval News, Defense Express)     │ legacy STANAG/DoD categorization│
├────────────────────┼──────────────────────────────────┼────────────────────────────────┤
│ 6. Patents & OEM   │ Deep structural blueprints,      │ Theoretical claims lacking     │
│    Datasheets      │ CAD layouts, actuator schemas    │ combat attrition reality       │
└────────────────────┴──────────────────────────────────┴────────────────────────────────┘
```

---

## 3. The 5-Block Cyber-Physical Expertise & Validation Protocol (CEVP)

Every target link or platform must be processed through the standardized 5-block pipeline:

```
[Target URL / Signal]
         │
         ▼
 ┌───────────────┐
 │    BLOCK 1    │ ──► Raw Technical Extraction & Marketing De-Noising
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │    BLOCK 2    │ ──► UWE 4 Invariant Laws Stress-Test & 6-Character Token
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │    BLOCK 3    │ ──► HAL/EAL Contract Formulation & Piecewise Energy Audit
 └───────┬───────┘
         ▼
 ┌───────────────┬───────────────────────────────┐
 │    BLOCK 4    │ (External Loop)               │
 │ Public Output │ ──► Mobile-First Comments     │
 └───────────────┴───────────────────────────────┘
         ▼
 ┌───────────────┬───────────────────────────────┐
 │    BLOCK 5    │ (Internal Loop)               │
 │ Ledger & Git  │ ──► Codification in UWE Core  │
 └───────────────┴───────────────────────────────┘
```

### Block 1: Raw Technical Extraction & Marketing De-Noising
1. Fetch full page content, metadata, title, and video descriptions.
2. Extract physical ground truths: operating medium (air, ground, sea, subsea, orbit), actual structural mass, powerplant type, steering kinematics, and actuator layout.
3. Identify and strip marketing traps:
   - Conflating passive geometric hinges with *adaptive suspension* (e.g., SlimAk).
   - Calling fixed-wing VTOL aircraft *FPV copters* or *hybrid drones*.
   - Flat commercial claims like "hours of flight" without payload, speed, or wind envelopes.

### Block 2: UWE 4 Invariant Laws Stress-Test & Token Assignment
Filter the platform through the Four Invariant Laws of UWE:
1. **Law of Kinematic Primacy:** Does the physical interface comply with the medium? ($L/D$ aerodynamic ratio, ground pressure $\text{kg/cm}^2$, hydrodynamics $C_d$, wave impact $G_z$).
2. **Law of Hierarchical Containerization:** Assign the true logistics tier from $C_0$ (Micro/Handheld) to $C_4$ (Fixed Strategic Infrastructure).
3. **Law of Hardware Abstraction & Decoupled Lethality:** Is the chassis an invariant carrier? How is the payload or One-Way Mission (OWM) mode integrated?
4. **Law of Dual-Read Cognitive Synchronization:** Encode the monolithic 6-character token:
   $$\mathbf{[Domain / Horizon - Container]} - \mathbf{[Powerplant - Mission]} - \mathbf{[Doctrine - Comms]}$$

### Block 3: HAL / EAL Contract Formulation & Energy Audit
1. **HAL Contract Identification:** Define the exact programming interface governing the platform:
   - Lift + Cruise transitions: `IVtolTransitionDrive` (rotor-to-wing crossfade ratio $\alpha$).
   - Articulated ground chassis: `IArticulatedChassis` (yaw steering angle $\gamma$ & roll deflection).
   - Multi-bus hybrid powertrains: `IPowerEnergy::HybridBusManager` (discharge C-rate vs generator kW).
2. **Piecewise Energy & Degradation Solver:**
   - Multi-phase budget: $\int P(t)\,dt$ distinguishing hover vs cruise vs transit.
   - Dynamic airframe degradation: Internal cell resistance ($R_{\text{int}}$), voltage sag ($\Delta V$), and parasitic drag ($\Delta C_{D0}$).
3. **The HAL One-Sentence Definition:** Formulate an uncompromising single sentence explaining the cyber-physical control law for the platform.

### Block 4: External Public Output & Platform-Native Export
1. **Zero-Friction Formatting (Strict Platform Syntax):**
   * **Facebook Comments:** Facebook does NOT render Markdown. Strictly **NO** `**bold**`, `*italic*`, `### Headings`, or `>` blockquotes. Use:
     - UPPERCASE headers (`КЛАСИФІКАЦІЯ UWE: UAV: AI-CP-HL`).
     - Standard punctuation quotes («...» or "...").
     - Emoji bullets (`🟢`, `🔴`, `⚡`, `🏷️`, `🔹`).
     - Double-spaced paragraph breaks (`\n\n`) to prevent text collapse.
   * **YouTube Comments:** Single `*bold*` and `_italic_` only. Zero `###` or `**`.
   * **LinkedIn Comments:** Plain-text with emoji bullets and double line breaks. Strictly NO markdown asterisks (`**` or `*`).
     - **Character Limits:** Hard platform ceiling is **1,250 characters** (including whitespace). Engineering safe budget is **1,150–1,200 characters** to prevent multi-byte emoji cutoff and mobile truncation.
     - **Mandatory Elements:** Monolithic 6-character UWE token (`[DOMAIN]: [OCTET1]-[OCTET2]-[OCTET3]`), core physical/kinematic advantage, and HAL contract definition.
     - **Multi-Part Rule:** If full cyber-physical depth exceeds 1,200 characters, either condense into a single punchy <=1,200 char monolithic comment or split into numbered reply chunks (`[PART 1/2]`, `[PART 2/2]`).
   * **Twitter / X:** Character-budgeted (<280 chars per post or clean thread chunks).
2. **Dedicated `.md` Export Files (Anti-Copy-Corruption):**
   * To prevent UI copy-paste line truncation, every analysis MUST generate separate standalone `.md` files in `Expertise/comments/`:
     - `Expertise/comments/<TargetID>_<PlatformName>_UA.md`
     - `Expertise/comments/<TargetID>_<PlatformName>_EN.md`
   * In chat, render comments inside raw text code blocks (` ```text ... ``` `) so the UI copy button grabs clean, platform-compliant text.

### Block 5: Internal Architectural Codification
Immediately persist findings into [`Expertise_Ledger.md`](file:///home/hills/Documents/UWS/Expertise/Expertise_Ledger.md):
* Platform name, source URL, date.
* UWE 6-character token.
* Primary HAL interface tested.
* Architectural lesson derived (gap detected in legacy standards, physical law validated).

---

## 4. Strict Prohibitions & Anti-Patterns

1. **NO Dual-Domain Tokens:** Never use compound domains like `UAV/UCV` or `UGV/USV`. One vehicle belongs strictly to one primary physical domain. Lift + Cruise is strictly `UAV`.
2. **NO Amateur Military Slang:** Never use terms like *vozyk*, *cart*, *FPV* (as a vehicle class), *kamikaze-drone* (it is an OWM decorator on an invariant chassis).
3. **NO Inline Evaluation:** Zero `python -c` or `bash -c`. Use structured scripts or standard git inspect commands.
4. **NO Silent Lost Insights:** Every link analyzed MUST update `Expertise_Ledger.md`. No analysis is thrown away.
