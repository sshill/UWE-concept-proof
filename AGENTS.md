# AGENTS.md — Unmanned Warfare Engine (UWE) Project Instructions & Style Guide

> **Scope:** This rule file applies exclusively to tasks and conversations operating within the `/home/hills/Documents/UWS` directory and the **UWE (Unmanned Warfare Engine)** publication series.

---

## 1. Author Identity, Philosophy & Doctrinal Context

* **Author:** **Serhii Khylevych** — Systems Architect, MilTech strategist, and autonomous robotics engineer.
* **Context & Stakes:** Authored in Kyiv under real-world wartime conditions (air raid alerts, kinetic strikes, electronic warfare, grid disruptions). This is not Silicon Valley theoretical speculation; it is an existential doctrine born from the frontline of asymmetric warfare.
* **Core Mission:** Architecting a scalable, software-defined containment line and automated interdiction shield for the Free World (from the Scandinavian/Baltic littoral to the Black & Caspian Seas) that replaces human casualties with algorithmic, hardware-abstracted robotic fleets.
* **Philosophical Pillars:**
  1. **Rejection of "Wunderwaffen":** Single, bespoke, over-engineered "silver-bullet" platforms are dead-ends in attrition warfare. Supremacy belongs to standardized, modular, swarming components.
  2. **Rejection of Flat Commercial Metrics:** Discard amateur/marketing metrics like "hours of flight" or "takeoff weight" in favor of strict physical laws, aerodynamic/hydrodynamic envelopes, energy density, and cyber-physical limits.
  3. **Hardware Abstraction Layer (HAL):** Autonomous vehicles are programmable, object-oriented executors managed by a software-defined operational cloud (the "AWS for autonomous warfare").
  4. **The "First to See, First to Strike" Law:** The 6-character matrix provides a dual-read language (human commander + tactical AI edge processor) cutting cognitive load and GPU inference overhead to microseconds.

---

## 2. Terminology & Standardization Rules

* **Framework Acronym:** Always use **UWE (Unmanned Warfare Engine)**. 
  * *Strictly forbidden:* Do **NOT** use `UWS` (collides with *Urban Water Systems* and *Upper West Side*) or `UWF` in titles or public copy.
* **Matrix Standard:** Unified 6-character cyber-physical matrix.
* **Namespaces:** Domain prefixes isolate operational logic:
  * `UAV` — Unmanned Aerial Vehicles
  * `UCV` — Unmanned Combat Vehicles (strike multirotors / loitering munition)
  * `UGV` — Unmanned Ground Vehicles
  * `UUV` — Unmanned Underwater Vehicles
  * `USV` — Unmanned Surface Vehicles
* **Content Integrity:** NEVER truncate, compress, or re-interpret author comments, historical precedents (e.g., Ukrainian Cossack marine engineering: *Chaika*, *Pirnachka*), or physical mathematical formulations. All octet comments must remain unabridged.

---

## 3. The UWE Publication Cycle: History & Architecture

The UWE series transitions legacy military classifications into a software-defined matrix. The agent must maintain continuity with the full published cycle:

### Article 1: UAV (Fixed-Wing Aviation)
* **Title:** *The Alt-Endurance Trap: Why Current UAV Classifications Fail*
* **Link:** [LinkedIn Pulse Article](https://www.linkedin.com/pulse/alt-endurance-trap-why-current-uav-classifications-fail-khylevych-wcebf)
* **Core Argument:** Legacy STANAG 4670 / DoD / EASA categories (HALE, MALE, LwA) rely on arbitrary altitude/endurance boxes. UWE breaks this into aerodynamic energy regimes, sensor spectral horizons, and structural payload ratios.

### Article 2: UCV (Combat Multirotors / Tactical Strike)
* **Title:** *Why "FPV" is a Nonsense Term: Shifting from Hobbyist Slang to Combat UCV Standard*
* **Link:** [LinkedIn Pulse Article](https://www.linkedin.com/pulse/why-fpv-nonsense-term-shifting-from-hobbyist-slang-uav-khylevych-ebcvf)
* **Core Argument:** "FPV" is a consumer piloting hobby term, meaningless for military doctrine. Established the UCV class: terminal guidance physics, electronic counter-countermeasures (ECCM), kinetic delivery dynamics, and modular explosive train integration.

### Article 3: UGV (Ground Robotics)
* **Title:** *Beyond the "Vozyk": The New 6-Character Standard for Combined Arms UGV*
* **Link:** [LinkedIn Pulse Article](https://www.linkedin.com/pulse/beyond-vozyk-new-6-character-standard-combined-arms-ugv-khylevych-j3r4f)
* **Core Argument:** Discarded slang ("vozyk", "cart") for a rigorous 6-character tactical standard: ground pressure / running gear physics (tracks vs. wheels), robotic autonomy levels, combat payload module, and hybrid powerplants.

### Article 4: UUV (Sub-surface Robotics) — *The Established Gold Standard*
* **Title:** *The Software-Defined Subsea Revolution: Why Autonomous Undersea Warfare Depends on Depth Horizons, Not Form Factors*
* **Link:** [LinkedIn Pulse Article](https://www.linkedin.com/pulse/software-defined-subsea-revolution-why-autonomous-depth-khylevych-kteaf/)
* **Benchmark Architecture (DPE-MTC):**
  * `D` — Depth Horizon (Surface 0-5m $\rightarrow$ Snorkel 15m $\rightarrow$ Shallow 100m $\rightarrow$ Shelf 200m $\rightarrow$ Pelagic 1000m $\rightarrow$ Abyssal 3000m $\rightarrow$ Hadal 6500m+).
  * `P` — Propulsion & Acoustic Signature.
  * `E` — Energy Storage & Subsea Endurance.
  * `M` — Mission Module & Payload Class.
  * `T` — Telemetry & Acoustic/Optical Tether.
  * `C` — Computational Autonomy & Edge Navigation.
* **Empirical Validation:** Rigorously cross-referenced with western and global OEM datasheets (SubSeaSail HORUS, BAE Systems Riptide, BeeX ALPHA/BETTA, Huntington Ingalls REMUS 600, Saab Sabertooth, WHOI Alvin).
* **Reference Artifacts:** 
  * [`Classification_of_UUV.md`](./Classification_of_UUV.md) (Full whitepaper)
  * [`Classification_of_UUV_LinkedIn.md`](./Classification_of_UUV_LinkedIn.md) (Mobile-optimized edition)
  * [`uuv_matrix_aligned.jpg`](./uuv_matrix_aligned.jpg) (16:9 tactical depth cutaway infographic)

---

## 4. LinkedIn Pulse Publishing Standards (Mobile-First)

LinkedIn's editor and mobile app severely distort standard Markdown or HTML tables. The agent must enforce the following formatting rules for all articles:

1. **Card Blocks over Tables:**
   * Never output wide comparison tables into the LinkedIn Pulse text.
   * Format matrix entries and horizons as structured vertical card blocks using bold headers, emojis, and clear bullet points:
     ```markdown
     🔹 **Horizon [Code]: [Name] ([Metric Range])**
     * **Physical Constraints:** [Pressure, hydrodynamics, acoustics]
     * **Tactical Mission:** [Mission profile]
     * **OEM Benchmark:** [Platform Name] ([Manufacturer]) — [Key spec]
     ```
2. **Visual Infographic Cover:**
   * Generate high-resolution 16:9 tactical infographics (Python matplotlib / SVG) with dark navy/slate theme, technical typography, and clear physical cutaway rulers.
   * Render vehicles and benchmarks along the physical gradient.
3. **Rich Text Formatting & Export Pipeline:**
   * Generate an intermediate clean HTML (`.html`) file with styled headings, bold text, and hyperlinks.
   * Convert HTML to `.docx` via LibreOffice headless:
     `libreoffice --headless --convert-to docx "<filename>.html"`
   * This enables the author to copy-paste directly into Google Docs or LinkedIn Pulse with 100% style, link, and font fidelity.

---

## 5. Technical Environment & Synchronization Tooling

* **Local Workspace:** `/home/hills/Documents/UWS`
* **Google Drive Sync:**
  * Remote Name: `GDdisk` (configured via `rclone` at `~/.config/rclone/rclone.conf`)
  * Target Folder ID: `10ICgE21Po26Tqo2KfxcqlFrIwnROFcx0`
  * Upload Command Example:
    `rclone copyto "<local_file.docx>" "GDdisk:UWS/<destination_filename.docx>"`
* **System Utilities:** Debian GNU/Linux 13 (trixie), LibreOffice, Python 3 (matplotlib, numpy, PIL), `pdftotext`.

---

## 6. Pipeline for Upcoming Publications (Remaining 3 in Series)

1. **Article 5: USV (Unmanned Surface Vehicles)**
   * **Domain:** Black Sea asymmetric naval war, littoral sea denial, automated straits interdiction.
   * **Physical Envelopes:** Planing vs. displacement vs. catamaran vs. semi-submersible, Sea State (Beaufort scale) survivability, hydrodynamics of high-speed wave impacts, RCS reduction, Starlink/COMSAT resilience, anti-air FPV interception.
   * **Benchmarks:** *Magura V5*, *Sea Baby*, *Saildrone Explorer/Surveyor*, *MARTAC MANTAS/Devil Ray*, *L3Harris MAST-13*, *Anduril Maritime*.
2. **Articles 6 & 7:** Cross-domain orchestration, C4ISR algorithmic clouds, electronic warfare & space resiliency.
