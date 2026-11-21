🏷️ CLASSIFICATION UNDER UWE STANDARD:
UAV: AL-HS-DR (Shift from UAV: AL-HR-DR)

• A (Atmospheric) — tactical horizon 0-5000m.
• L (Light Tactical) — 45 kg MTOW, 9 kg payload, class C2.
• H (Hybrid-Electric) — ICE generator + battery, >10h loiter.
• S (Strike) — bomber stores: 82mm mortar + 40mm grenades.
• D (Decoupled Lethality) — CCRP drop and standoff loiter.
• R (Radio Mesh) — 160 km link + dual Jetson Orin AI.

🟢 CYBER-PHYSICAL ADVANTAGES:
1. Aerodynamic L/D. Unlike multirotors (L/D ~ 0), Reliant achieves cruise L/D of 14-18, delivering 10+ h loiter and 160 km radius on hybrid power.
2. Recon-to-Bomber Shift. Quick swap from ISR gimbal to kinetic drop racks validates UWE Decoupled Lethality on an invariant airframe.
3. Runway-Independent eVTOL. Vertical launch eliminates runways and catapults (10x10m footprint).

🔴 CRITICAL ENGINEERING TRADE-OFFS:
1. Parasitic Drag. External munitions disrupt laminar flow, increasing C_d0 by 25-35%.
2. Asymmetric Release. Dropping a 3.5kg bomb triggers instant rolling moment requiring feedforward trim via IAsymmetricStoresRelease HAL.

⚡ VERDICT: Attrition warfare forces tactical UAS to evolve into software-defined strike bombers.
