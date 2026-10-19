# Case Study #6: USV vs. Semi-Submersible — Architectural Demarcation & Hydrodynamic Physics

> **Author:** Serhii Khylevych — Systems Architect, MilTech Strategist, UWE Creator  
> **Date:** October 19, 2026  
> **Source Signal:** [Naval News: Exail USVs Set for U.S. Navy and Coast Guard Evaluations (Euronaval 2026)](https://www.navalnews.com/event-news/euronaval-2026/2026/10/exail-usvs-set-for-u-s-navy-and-coast-guard-evaluations/)  
> **Framework:** Unmanned Warfare Engine (UWE) — Cyber-Physical Expertise & Architectural Validation (CEVP)  
> **Classification Tokens:**
> * **Exail DriX H-9:** `USV: SL-PA-DR`
> * **Exail Oryx O-16:** `USV: ST-PL-DD`

---

## 1. Executive Summary & The Problem Statement

During military evaluations by the U.S. Navy (Office of Naval Research Counter-UAS testbed) and U.S. Coast Guard (CG-781 autonomous maritime domain awareness), technical observers frequently misidentify slender wave-piercing platforms like **Exail DriX** and **Oryx O-16** as *semi-submersible craft* or *hybrid surface/subsurface vehicles*. 

This visual and operational confusion arises from two distinct physical features:
1. **Green Water on Deck (Wave Over-topping):** The extremely narrow, wave-piercing bow does not ride over swells like a traditional V-hull; it cuts through them. In Sea State 4+, the deck is perpetually washed by solid water, leaving only the composite mast visible above the surface.
2. **The Submerged Torpedo-Like Gondola:** Mounted 1.5 to 2.0 meters beneath the waterline on a hydrodynamic vertical foil, the drop-keel sensor pod visually mirrors an autonomous underwater vehicle (AUV/UUV) or a submarine lower hull.

This case study establishes the rigorous cyber-physical boundary separating **Unmanned Surface Vehicles (USVs)** from **Semi-Submersibles (SPSS)** and **Unmanned Underwater Vehicles (UUVs)** under the Four Invariant Laws of the **Unmanned Warfare Engine (UWE)**.

---

## 2. The 3 Physical Criteria of Architectural Demarcation

Under UWE doctrine, platform classification is governed by immutable physical laws and control degrees of freedom, never by visual appearance or marketing claims.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           UWE PHYSICAL DEMARCATION MATRIX                                        │
├──────────────────────────┬─────────────────────────────┬─────────────────────────────────────────┤
│ PHYSICAL CRITERION       │ SEMI-SUBMERSIBLE (SPSS/UUV) │ WAVE-PIERCING USV (DriX / Oryx)         │
├──────────────────────────┼─────────────────────────────┼─────────────────────────────────────────┤
│ 1. Buoyancy Distribution │ 90–95% of displacement is   │ >85% of buoyant volume is in the upper  │
│    & Reserve Buoyancy    │ submerged. Reserve buoyancy │ hull. Submerged gondola has neutral or  │
│                          │ is negligible (<5%).        │ negative buoyancy (acting as ballast).  │
├──────────────────────────┼─────────────────────────────┼─────────────────────────────────────────┤
│ 2. Depth Degree of       │ Vertical axis is controlled │ Vertical position is strictly tied to   │
│    Freedom (z-axis)      │ variable (z < 0). Capable   │ the surface plane (z = 0). Vehicle      │
│                          │ of depth trim/ballasting.   │ cannot submerge or trim depth.          │
├──────────────────────────┼─────────────────────────────┼─────────────────────────────────────────┤
│ 3. Internal Powerplant   │ Closed-loop or snorkel air; │ Atmospheric air-breathing IC diesel.    │
│    Thermodynamics        │ submersible battery/fuel    │ Ingestion of green water into mast intake│
│                          │ cell architecture.          │ induces catastrophic hydraulic lock.    │
└──────────────────────────┴─────────────────────────────┴─────────────────────────────────────────┘
```

### Criterion 1: Buoyancy Reserve & Displacement Equilibrium
In a genuine semi-submersible (such as the Ukrainian *Toloka* series or low-profile littoral pickets), the hull displacement volume is designed to sit almost entirely below the undisturbed water surface. Freeboard is measured in millimeters, and reserve buoyancy is tiny (<5%).

In contrast, the **Exail DriX and Oryx** have their primary buoyant hull, fuel tanks, propulsion engines, and control avionics housed entirely within the surface monohull. The lower gondola does **not** provide net positive buoyancy; it is a **pendulum ballast bulb** (identical in principle to the lead bulb on an ocean racing yacht) combined with an acoustic transducer housing.

### Criterion 2: Vertical Axis ($z$) Controllability
A vehicle transitions into the **UUV** domain when depth ($z$) becomes an actively controlled state variable:
$$\dot{z}(t) = f(\mathbf{u}_{\text{ballast}}, \mathbf{u}_{\text{planes}}, v_{\text{fwd}})$$
Exail USVs possess **zero** ballast control tanks and zero dive planes. The vehicle cannot dive, loiter at a subsurface depth, or execute an emergency descent. It is geometrically and hydrostatically constrained to the two-phase air-sea boundary ($z = 0$).

### Criterion 3: Atmospheric Air-Breathing Dynamics
The primary propulsion of both DriX H-9 and Oryx O-16 relies on marinized internal combustion diesel powerplants. Continuous combustion air and exhaust gases are ducted through the vertical mast. Any loss of positive freeboard resulting in mast submergence causes immediate diesel flameout and hydrodynamic swamp.

---

## 3. Hydrodynamic Physics: Slender Monohulls vs. Planing Sprint Hulls

Modern littoral naval drone combat (exemplified by the Black Sea campaign) has been dominated by **high-speed planing stepped monohulls** (*Magura V5*, *Sea Baby*). While ideal for sprint strikes in Sea State 1–3, planing hulls fail catastrophically in open-ocean endurance:

1. **Hydrodynamic Impact Acceleration ($G_z$):**
   * *Planing Hull:* At 40+ knots over 1.5-meter chop, repeated wave-slamming generates vertical peak shock loads exceeding $G_z > 5\text{--}8g$. This produces severe composite fatigue, delamination, and rapid gimbal saturation on gyro-stabilized sensor heads.
   * *Wave-Piercing Hull:* With a length-to-beam ratio ($L/B$) between $8:1$ and $10:1$, the wave-piercing bow slices through swells, slashing vertical accelerations to **$<1.5g$ in Sea State 5**.
2. **Acoustic Signal-to-Noise Ratio (SNR) in the Boundary Layer:**
   * Traditional hull-mounted transducers suffer massive acoustic degradation from near-surface wave breaking, bubble sweep-down, and hull boundary layer aeration.
   * By deploying the sensor payload into a **retractable drop-keel gondola at $z = -2.0\text{ m}$**, Exail isolates multibeam and USBL sonars from surface aeration. This delivers a **$+15\text{ to }20\text{ dB}$ SNR advantage**, enabling the passive acoustic detection of modern ultra-quiet AIP/diesel-electric submarines that would remain invisible to standard surface vessels.

---

## 4. Hardware Abstraction Layer (HAL) Contract Formulation

The distinction between USV and semi-submersible is codified at the code level within the UWE Hardware Abstraction Layer:

```rust
// ============================================================================
// UWE HAL Contract: Open-Ocean Wave-Piercing Surface Drive
// File: /uwe/hal/marine/drop_keel_surface_drive.rs
// ============================================================================

pub trait IHydrodynamicDropKeelDrive: ISurfaceVesselControl {
    /// Controls the mechanical extension, retraction, and locking of the submerged gondola.
    fn set_keel_deployment_state(&mut self, state: KeelPosition) -> Result<(), KeelError>;

    /// Dynamically trims active roll-damping fins mounted on the keel strut.
    fn update_active_roll_damping(&mut self, roll_angle_rad: f32, roll_rate_rad_s: f32);

    /// Monitors acoustic noise floor and adjusts vessel cruising rpm to optimize sensor SNR.
    fn optimize_acoustic_snr_profile(&self) -> AcousticNoiseFloorMetrics;
}
```

* **The HAL Single-Sentence Rule:**  
  *«Open-ocean unmanned surface platforms require the IHydrodynamicDropKeelDrive HAL contract, which dynamically deploys and trims a submerged sensor gondola below the near-surface cavitation and bubble sweep-down boundary layer, maximizing acoustic SNR for ASW picket loiter while dynamically damping the narrow wave-piercing displacement hull across Sea State 5+ environments.»*

If this platform were a semi-submersible, it would instead require `IBallastTrimControl` (managing ballast tank flood/blow solenoids and variable displacement pumps).

---

## 5. The 4-Tier Maritime Taxonomy for UWE Article 5 (USV)

To eliminate industry confusion, UWE Article 5 organizes the unmanned maritime surface/near-surface domain into four distinct hydro-mechanical classes:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        UWE MARITIME MOBILITY TAXONOMY (ARTICLE 5)                                │
├────────┬────────────────────────────────┬───────────────────────────────┬────────────────────────┤
│ TIER   │ ARCHITECTURAL REGIME           │ HYDRODYNAMIC PROFILE          │ BENCHMARK PLATFORMS    │
├────────┼────────────────────────────────┼───────────────────────────────┼────────────────────────┤
│ Tier 1 │ Planing Sprint Strike (USV)    │ High-speed lift (40–55 kts),  │ Magura V5, Sea Baby,   │
│        │                                │ severe wave shock (>5g),      │ MARTAC MANTAS T-12     │
│        │                                │ littoral sprint, short days.  │                        │
├────────┼────────────────────────────────┼───────────────────────────────┼────────────────────────┤
│ Tier 2 │ Wave-Piercing Displacement/    │ Slender monohull (10–18 kts), │ Exail DriX H-9,        │
│        │ Drop-Keel Picket (USV)         │ vertical shock <1.5g, months  │ Exail Oryx O-16        │
│        │                                │ at sea, max acoustic SNR.     │                        │
├────────┼────────────────────────────────┼───────────────────────────────┼────────────────────────┤
│ Tier 3 │ Self-Propelled Semi-           │ 90–95% submerged volume,      │ Toloka TLK-150 / 400,  │
│        │ Submersible (SPSS / USV-UUV)   │ near-zero radar/IR profile,   │ Low-Profile Pickets    │
│        │                                │ mast-dependent snorkeling.    │                        │
├────────┼────────────────────────────────┼───────────────────────────────┼────────────────────────┤
│ Tier 4 │ True Autonomous Undersea       │ Complete 3D fluid immersion,  │ REMUS 600, Marichka,   │
│        │ Vehicle (UUV)                  │ depth-controlled (10–6000m+), │ Saab Sabertooth        │
│        │                                │ independent of atmosphere.    │                        │
└────────┴────────────────────────────────┴───────────────────────────────┴────────────────────────┘
```

---

## 6. Strategic Takeaway & Architectural Codification

1. **Law of Decoupled Lethality Confirmed:** The Office of Naval Research's (ONR) deployment of a Counter-UAS payload onto the DriX H-9 demonstrates that the wave-piercing hull is an invariant cyber-physical carrier. Its superior platform stability ($<1.5g$) solves the naval gimbal-jitter problem, providing a cost-effective air-defense picket for carrier strike groups.
2. **Persistence Replaces Sprint:** High-speed planing drone boats won the Battle of the Black Sea by striking stationary or slow naval targets in calm littoral waters. However, securing vast ocean straits (the GIUK gap, Baltic littoral, South China Sea, and Taiwan Strait) requires **Tier 2 Wave-Piercing USVs** with multi-month endurance (90+ days at sea demonstrated by DriX in the Caribbean) and drop-keel sonars capable of detecting modern quiet submarines.

*Codified into the official UWE Knowledge Base and Expertise Ledger under Entry #6.*
