EXPERT DECONSTRUCTION & CYBER-PHYSICAL ANALYSIS: NEBESA SUBORBITAL UNMANNED SPACEPLANE (CZECH REPUBLIC)

An article published by Militarnyi highlights the flagship aerospace project from Czech company Nebesa Aerospace (developed in collaboration with Czech Technical University in Prague and Czech IT Academy) — the NEBESA suborbital flight testbed, unveiled at Future Forces Forum 2026 in Prague.

The fundamental architectural disruption of the platform is the "Runway to Space" paradigm: horizontal takeoff and landing (HTOL) from conventional paved runways or highway stretches, performing a suborbital hop to an apogee of 110 km (crossing the Kármán line) and speeds up to Mach 3.5.

🏷️ CLASSIFICATION UNDER UWE STANDARD (Unmanned Warfare Engine):
UAV: HD-LR-PS

• H (Hypersonic / Suborbital Flight Horizon) — suborbital altitude ceiling up to 110 km (thermosphere / microgravity regime) and high-supersonic/near-hypersonic sprint velocity up to Mach 3.5 (3,700–4,300 km/h).
• D (Delta / Blended Wing Body Planform) — tailless delta wing with elongated sweepback, twin vertical fins on outer wing panels, and high internal propellant volume fraction.
• L (Light Dispersed Runway Logistics) — logistics tier C2/C3: horizontal takeoff and landing on standard civilian/military runways or straight road segments, eliminating heavy spaceport infrastructure.
• R (Rocket Liquid Propulsion) — 3D-printed metal liquid-propellant rocket engine RÁMUS I delivering 9 kN peak thrust with regenerative nozzle cooling, paired with turbojet airbreathing ascent.
• P (Passive Standoff Reconnaissance & Testbed Posture) — microgravity scientific research, materials and aerothermodynamic validation, high-altitude optical/electronic reconnaissance, and high-speed aerial target emulation for air defense systems.
• S (Space-to-Ground SATCOM & Space Telemetry) — resilient satellite constellation link and ultra-high-frequency telemetry immune to atmospheric plasma attenuation and Earth curvature at apogee.

🟢 PHYSICAL ADVANTAGES & KINEMATIC MERITS:

1. Spaceport Infrastructure Decoupling (UWE Law 2: C4 -> C2/C3):
Conventional vertical rocket launches require multibillion-dollar launch complexes whose fixed coordinates make them prime targets for preemptive strikes. NEBESA converts any 1,500–2,000 m runway or straight highway into a responsive suborbital launch pad, dispersing operations across standard airfield networks.

2. Dual-Regime Ascent Energetics (Airbreathing + Rocket Crossfade):
Leveraging turbojet propulsion in the dense troposphere allows the vehicle to climb to 10–12 km, preserving 30–40% of liquid oxidizer mass. Igniting the 9 kN liquid rocket engine RÁMUS I in rarefied air yields optimal specific impulse (Isp) due to drastically reduced ambient nozzle backpressure.

3. Responsive Suborbital Standoff & Attrition Immunity:
A modular 25 kg payload bay enables rapid-response strategic reconnaissance from an apogee of 110 km. At this altitude, the spaceplane operates far above the kinematic ceiling of conventional theater air-defense missiles (e.g., Patriot PAC-2, S-300, S-400), which lack exo-atmospheric kinetic kill vehicles (KKVs).

🔴 ENGINEERING VULNERABILITIES & TRADEOFFS:

1. Dynamic Pressure Collapse at Apogee (q -> 0 at 110 km):
At altitudes between 100 and 110 km, atmospheric density drops toward near-vacuum (rho -> 0). Conventional aerodynamic elevons and rudders lose all control authority. Attitude stabilization and orientation at the apex of the parabolic trajectory require a dedicated cold-gas or monopropellant Reaction Control System (RCS) or reaction wheels; any RCS failure causes catastrophic uncoordinated tumble upon atmospheric re-entry.

2. Aerothermodynamic Heating & Material Fatigue at Mach 3.5+:
Re-entering the upper atmosphere at Mach 3.5 generates intense shock-wave stagnation temperatures exceeding 500–700°C along wing leading edges and the nosecone. This mandates high-temperature titanium alloys, carbon-carbon composites, or specialized thermal barrier coatings (TBC), significantly elevating production costs and maintenance turnaround times.

3. Airspace Deconfliction in Shared Air Corridors:
A suborbital trajectory punches vertically through commercial flight levels (FL300–FL400) at extreme climb and descent velocities. Without real-time integration into military-civilian C4ISR air traffic management networks, rapid-response launches pose severe mid-air collision hazards.

⚙️ HAL CONTRACT OF THE ONBOARD OPERATING SYSTEM:
ISuborbitalTransitionDrive & IBlendedReactionAerodynamicControl

«Horizontal-takeoff suborbital spaceplanes require the ISuborbitalTransitionDrive and IBlendedReactionAerodynamicControl HAL contracts to dynamically orchestrate combined turbojet-to-rocket propulsion transitions, manage aerothermal heating loads during Mach 3.5 pull-up and re-entry, and continuously crossfade between aerodynamic elevons and exo-atmospheric reaction control systems (RCS) as dynamic pressure collapses to zero at 110 km apogee.»
