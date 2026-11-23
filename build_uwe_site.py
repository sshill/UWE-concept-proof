#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# [AI_PROVENANCE: TIER_2_GROQ | MODEL: openai/gpt-oss-120b]
import sys
import html as html_mod
import re
import json
import shutil
from pathlib import Path

sys.dont_write_bytecode = True

WORKSPACE = Path(__file__).resolve().parent
DOCS = WORKSPACE / "docs"
BASE_URL = "https://sshill.github.io/UWE-concept-proof"
C2_ARTICLE_PATH = "c2/joint-unmanned-operation.html"

# 32 Empirical Platform Benchmarks Metadata & Deep Cyber-Physical Content
CASES_DATA = [
    {
        "id": "01",
        "slug": "01-honda-evtol",
        "domain": "UAV",
        "name": "Honda eVTOL (GT-HEV Lift+Cruise)",
        "token": "UAV: AL-TL-HR",
        "token_full": "UAV: Atmospheric Lift • C2 Light Logistics (5-8 pax) • GT-HEV Gas Turbine Hybrid • Loiter/Cruise Transit • High Survivability Reserve • Redundant MESH/SATCOM",
        "hal": "IVtolTransitionDrive",
        "hal_def": "Lift+Cruise eVTOL architectures mandate IVtolTransitionDrive to dynamically crossfade rotor lift to aerodynamic wing loading (rotor throttle α: 1.0 -> 0.0) without mechanical tiltrotor pitch instability.",
        "vendor": "Honda Aircraft Company",
        "vendor_slug": "honda",
        "date": "2026-10-19",
        "source_name": "Facebook Reel / Honda Aviation Field Test",
        "source_url": "https://www.facebook.com/reel/1409577227898837",
        "advantages": [
            "Decoupled Lift+Cruise eliminates tiltrotor single-point mechanical failure by isolating hover props from horizontal cruise pusher.",
            "Gas turbine hybrid-electric powertrain (GT-HEV) breaks the chemical battery energy density bottleneck (12,000 Wh/kg vs 250 Wh/kg).",
            "Piecewise energy budget proves hover power drain is ~6x cruise power (P_hover ≈ 6 * P_cruise), allowing small cruise engines."
        ],
        "vulnerabilities": [
            "Internal cell resistance voltage sag (ΔV = I * R_int) on terminal hover descent under degraded battery state of health.",
            "Airframe parasitic drag penalty (ΔC_D0) from eight locked vertical lift rotors during high-speed cruise.",
            "Dual-system thermal and acoustic signature from gas turbine exhaust reducing acoustic stealth."
        ],
        "lesson": "Validates the Law of Decoupled Powerplants in UWE: pure battery VTOL is kinetically unviable for theater logistics; hybrid turbine generation is mandatory.",
        "related": ["03-stealth-ucav", "09-capstone-coaxial", "12-mq25-stingray"]
    },
    {
        "id": "02",
        "slug": "02-slimak-ugv",
        "domain": "UGV",
        "name": "НРК SlimAk (Articulated Chassis UGV)",
        "token": "UGV: GL-EP-WR",
        "token_full": "UGV: Ground Land • C1 Hand-Deployable / Man-Portable • Electric Battery • Patrol / Forward Recon • All-Terrain Wheeled • Redundant RF Mesh",
        "hal": "IArticulatedChassis",
        "hal_def": "Articulated off-road robotic chassis require the IArticulatedChassis HAL contract to decouple central joint roll compliance from active yaw steering, eliminating tire slip scrub in deep mud.",
        "vendor": "Ukrainian Frontline Engineering",
        "vendor_slug": "frontline-ua",
        "date": "2026-10-19",
        "source_name": "Facebook Reel / Frontline Field Prototype",
        "source_url": "https://www.facebook.com/reel/1572864870891828",
        "advantages": [
            "Articulated two-section frame provides passive mechanical roll conformity across rugged shell craters and trenches.",
            "Eliminates skid-steer scrubbing in viscous mud, reducing drivetrain electrical energy consumption by 30-40%.",
            "Continuous 4-wheel soil contact maximizes normal force and Bekker soil traction adhesion."
        ],
        "vulnerabilities": [
            "Central articulating hinge is a primary mechanical stress concentrator and single-point-of-failure under blast shocks.",
            "High exposure of steering hydraulic/linear electric actuators to small-arms fire and soil grit ingress.",
            "Zero active roll suspension damping: passive geometric hinge is not adaptive suspension."
        ],
        "lesson": "Demolishes marketing confusion: a passive articulating mechanical hinge is a chassis topology, NOT an adaptive suspension system.",
        "related": ["08-unex-artillery"]
    },
    {
        "id": "03",
        "slug": "03-stealth-ucav",
        "domain": "UAV",
        "name": "Transonic / Supersonic Stealth UCAV",
        "token": "UAV: AH-PA-HO",
        "token_full": "UAV: Atmospheric High-Altitude • C3 Strategic Runway • Jet Propulsion • Air Superiority • Heavy Payload Strike • Optical/Laser Resilient",
        "hal": "IAerodynamicTrim",
        "hal_def": "Supersonic tailless unmanned combat airframes mandate IAerodynamicTrim to dynamically bias elevon reflex angles against boundary-layer separation and shock-induced pitching moments.",
        "vendor": "Defense Aerospace Research",
        "vendor_slug": "global-aerospace",
        "date": "2026-10-19",
        "source_name": "Facebook Reel / Aerodynamic Wind Tunnel Model",
        "source_url": "https://www.facebook.com/reel/1625827525885877",
        "advantages": [
            "Tailless blended wing-body yields ultra-low radar cross-section (RCS < -30 dBsm) across VHF to X-band radar frequencies.",
            "Internal conformal weapons bay prevents weapon drag divergence and maintains stealth during supersonic cruise.",
            "High structural fuel fraction enables extended unrefueled combat radius (>1,500 km)."
        ],
        "vulnerabilities": [
            "Prominent roof bubble canopy creates transonic wave drag divergence (ΔC_D0) and distorts boundary layer entering dorsal intake.",
            "Severe total pressure recovery loss in serpentine S-duct engine inlet under high angles of attack.",
            "High yaw divergence sensitivity at supersonic speeds due to absence of vertical stabilizing fins."
        ],
        "lesson": "Confirms the Law of Kinematic Primacy: cosmetic design tropes (bubble cockpits on unmanned airframes) destroy transonic aerodynamic efficiency.",
        "related": ["04-waverider-corvus", "05-sickle-wing", "13-fury-ghostbat"]
    },
    {
        "id": "04",
        "slug": "04-waverider-corvus",
        "domain": "UAV",
        "name": "Mach 6 Hypersonic Waverider (Corvus)",
        "token": "UAV: AI-CP-HL",
        "token_full": "UAV: Atmospheric Interceptor / Hypersonic • C4 Strategic Launch • Scramjet / Rocket Boost • Deep Penetration Strike • High-Altitude • Laser ISL Link",
        "hal": "IThermalPlasmaLink",
        "hal_def": "Hypersonic waverider vehicles require the IThermalPlasmaLink HAL contract to command aft-directed laser optical links to orbital relay satellites, bypassing the Mach 6 plasma blackout sheath.",
        "vendor": "DARPA / Skunk Works Experimental",
        "vendor_slug": "darpa",
        "date": "2026-10-19",
        "source_name": "Defense OSINT / Theoretical Mach 6 Aerothermal Benchmark",
        "source_url": "https://www.facebook.com/reel/1625827525885877",
        "advantages": [
            "Compression lift generation: rides its own shockwave yielding high hypersonic lift-to-drag ratio (L/D > 4.5 at Mach 6).",
            "Kinetic survivability: Mach 6 velocity and 30 km altitude render all current short/medium-range SAM interceptors kinematically obsolete.",
            "Near-instantaneous time-critical strike capability across intercontinental theater arcs."
        ],
        "vulnerabilities": [
            "Stagnation point aerothermal heating exceeding 1,850°C blinds forward optical and infrared imaging sensors.",
            "Ionized plasma sheath (electron density ω_p > 30 GHz) completely blocks RF communications, GPS, and radar altimeters.",
            "Extremely narrow scramjet unstart margins during rapid dynamic maneuvering."
        ],
        "lesson": "Proves the necessity of cross-domain orbital integration: hypersonic atmospheric vehicles cannot communicate via terrestrial RF and must link to orbital UOV anchors.",
        "related": ["05-sickle-wing", "10-orbital-guardian"]
    },
    {
        "id": "05",
        "slug": "05-sickle-wing",
        "domain": "UAV",
        "name": "Autonomous Sickle Wing (Tailless Hypersonic)",
        "token": "UAV: AI-CP-HL",
        "token_full": "UAV: Atmospheric Interceptor • C3 Dispersed Base • Scramjet Cruise • High-Altitude Interdiction • Stealth Penetration • Laser Link",
        "hal": "IActiveFlowControlDrive",
        "hal_def": "Tailless hypersonic sickle-wing configurations mandate IActiveFlowControlDrive to generate dynamic yaw and roll control moments via supersonic bleed-air blowing, replacing mechanical control surfaces.",
        "vendor": "Next-Gen Hypersonic Consortium",
        "vendor_slug": "hypersonic-consortium",
        "date": "2026-10-19",
        "source_name": "Facebook Reel / Hypersonic Aerodynamic Planform",
        "source_url": "https://www.facebook.com/reel/1818239552508775",
        "advantages": [
            "Crescent sickle leading-edge geometry delays supersonic shock detachment and reduces wave drag across Mach 3 to Mach 6.",
            "Total absence of vertical empennage slashes side-aspect radar cross-section (RCS).",
            "Fluidic Thrust Vectoring (FTV) eliminates mechanical hinge gaps that cause boundary layer trip and extreme localized heating."
        ],
        "vulnerabilities": [
            "Complex pneumatic bleed-air ducting adds internal mass and parasitic engine compressor power loss.",
            "High aerothermal ablation along sharp leading edges requires carbon-carbon composite matrix refurbishing.",
            "Severe directional stability instability at low takeoff and landing approach speeds."
        ],
        "lesson": "Validates the UWE Law of Kinematic Primacy: mechanical control surfaces fail under hypersonic aerothermal loads; flight control becomes fluidic and software-driven.",
        "related": ["03-stealth-ucav", "04-waverider-corvus"]
    },
    {
        "id": "06",
        "slug": "06-exail-usv",
        "domain": "USV",
        "name": "Exail DriX H-9 & Oryx O-16 USVs",
        "token": "USV: SL-PA-DR",
        "token_full": "USV: Surface Marine • C2 Light 9m / C3 Heavy 16m • Diesel-Electric • Counter-UAS Escort / ASW Loiter • Persistent Picket • Dual MESH/SATCOM",
        "hal": "IHydrodynamicDropKeelDrive",
        "hal_def": "Open-ocean unmanned surface platforms require IHydrodynamicDropKeelDrive to dynamically lower sonar payloads 2m below surface cavitation and bubble sweep-down noise, enabling ASW acoustic SNR > 20 dB in Sea State 5.",
        "vendor": "Exail Marine & U.S. Navy Evaluations",
        "vendor_slug": "exail",
        "date": "2026-10-19",
        "source_name": "Naval News Euronaval 2026 / U.S. Navy & Coast Guard Trials",
        "source_url": "https://www.navalnews.com/event-news/euronaval-2026/2026/10/exail-usvs-set-for-u-s-navy-and-coast-guard-evaluations/",
        "advantages": [
            "Slender wave-piercing displacement monohull slashes vertical heave accelerations (<1.5g in Sea State 5 vs >6g for planing hulls).",
            "2-meter drop keel isolates sonars and acoustic sensors from hull surface bubble sweep-down, yielding +15-20 dB SNR for submarine tracking.",
            "Extreme endurance: 90 consecutive days on station demonstrated in U.S. 4th Fleet operations."
        ],
        "vulnerabilities": [
            "Narrow beam (L/B ≈ 9) causes low transverse metacentric height (GM_T), making roll stability dependent on active pendulum ballast.",
            "Submerged gondola draft prevents shallow littoral navigation unless actively retracted.",
            "Displacement hull limits maximum sprint speed to 15-20 knots, making it vulnerable to high-speed interceptor swarms."
        ],
        "lesson": "Establishes the hydrodynamic boundary for UWE Article 5 (USV): sprint planing hulls belong to kamikaze strike, while persistent ocean denial belongs strictly to wave-piercing displacement forms.",
        "related": ["07-ghostshark-auv"]
    },
    {
        "id": "07",
        "slug": "07-ghostshark-auv",
        "domain": "UUV",
        "name": "Anduril Ghost Shark XL-AUV & Ocius BlueBottle USV",
        "token": "UUV: PT-RM-DA",
        "token_full": "UUV: Pelagic 1000m Depth • C3 Heavy Slipway • Battery Electric • Multi-Payload: 12 Naval Mines + ALTIUS UAV Launch • Strategic Denial • Acoustic/RF",
        "hal": "ISubseaLaunchController",
        "hal_def": "Heterogeneous subsea architectures require ISubseaLaunchController to dynamically manage buoyancy transients (ΔB = -∑m_payload) during mine salvo release and submerged capsule UAV launch.",
        "vendor": "Anduril Industries & Ocius Technology (AUKUS)",
        "vendor_slug": "anduril",
        "date": "2026-10-19",
        "source_name": "Naval News / Royal Australian Navy AUKUS Milestone",
        "source_url": "https://lnkd.in/p/dd2v4jnD",
        "advantages": [
            "Decoupled Lethality: invariant pelagic hull converts between laying 12 naval mines, tube-launching ALTIUS UAVs, and covert SOF delivery.",
            "Persistent solar/sail/wave harvesting on companion BlueBottle USV provides infinite station-keeping acoustic gateway to orbital SATCOM.",
            "Deep ocean shelf transit (1,000m depth) completely bypasses shallow surface ASW acoustic barriers."
        ],
        "vulnerabilities": [
            "Rapid positive buoyancy spike upon salvo mine drop threatens accidental depth broaching if ballast flooding lags.",
            "Submerged UAV launch requires surface broaching and rocket booster ignition without compromising carrier acoustic stealth.",
            "Battery endurance constraints for high-speed underwater sprints without nuclear/parasitic assistance."
        ],
        "lesson": "Validates UWE Cross-Domain Orchestration: subsea combat supremacy is achieved by heterogeneous UUV (subsea carrier) + USV (energy gateway) + UAV (airborne effector) teams.",
        "related": ["06-exail-usv", "11-lockheed-lamprey"]
    },
    {
        "id": "08",
        "slug": "08-unex-artillery",
        "domain": "UGV",
        "name": "UNEX Amphibious Prime Mover (ABRIS)",
        "token": "UGV: GH-ET-DL",
        "token_full": "UGV: Ground Heavy / Amphibious • C3 Heavy Flatbed • Electric Battery • Artillery Towing & Ammo Replenishment • Rear/Forward Logistics • Starlink/RF",
        "hal": "IDrawbarTractionController",
        "hal_def": "Robotic prime movers require IDrawbarTractionController to govern wheel torque to Bekker soil slip ratios (s < 0.2) and actively pulse anti-jackknife braking against unbraked towed artillery loads.",
        "vendor": "UNEX (Tim De Zitter / Militarnyi)",
        "vendor_slug": "unex",
        "date": "2026-10-19",
        "source_name": "LinkedIn / Technical Analysis / Militarnyi",
        "source_url": "https://lnkd.in/p/dvJEuUV5",
        "advantages": [
            "Instant 0-RPM electric motor torque overcomes static breakaway friction on 3.2-tonne D-30 howitzer without clutch burn.",
            "Carrying 1.2 tonnes of onboard ammunition adds critical ballast to prime mover wheels, boosting normal tractive force.",
            "Zero acoustic and thermal exhaust signature during covert artillery displacement under drone surveillance."
        ],
        "vulnerabilities": [
            "Trailing unbraked mass: on muddy downhills, 3.2 tonnes of trailing artillery creates forward inertial thrust, jackknifing the UGV.",
            "Soil adhesion bounds: off-road drawbar pull is strictly limited by soil shear strength (F = μ * m * g), invalidating 10-tonne asphalt claims.",
            "Heavy battery pack mass limits amphibious freeboard and waterjet swimming velocity in river crossings."
        ],
        "lesson": "Demolishes marketing motor claims: towing capacity in war is dictated by Bekker soil mechanics and tractor ballast, not electric motor kilowatts.",
        "related": ["02-slimak-ugv"]
    },
    {
        "id": "09",
        "slug": "09-capstone-coaxial",
        "domain": "UCV",
        "name": "CAPSTONE Coaxial Heavy-Lift UCV",
        "token": "UCV: CL-PM-DR",
        "token_full": "UCV: Copter Lift (Coaxial) • C2 Light Mobile Footprint • Piston Heavy-Fuel • Multi-Payload 300kg / ASW / Logistics • Escort/Denial • MESH/SATCOM",
        "hal": "ICoaxialRotorDrive",
        "hal_def": "Heavy coaxial rotorcraft UCVs mandate ICoaxialRotorDrive to govern differential collective yaw while algorithmically clamping cyclic pitch rate limits to prevent catastrophic blade clashing under high-G gusts.",
        "vendor": "Certo Aerospace & BAE FalconWorks",
        "vendor_slug": "bae-falconworks",
        "date": "2026-10-19",
        "source_name": "Facebook Reel / Flight Testing Demonstration",
        "source_url": "https://www.facebook.com/reel/4404808966462700",
        "advantages": [
            "100% Useful Lift Power: eliminating the tail rotor recovers 12-15% of engine shaft power, directly enabling a 50% structural payload fraction (300kg on 600kg MTOW).",
            "Compact footprint: contra-rotating blades yield ~35% smaller rotor disc diameter compared to single-rotor helicopters, enabling confined deck landings.",
            "Symmetrical high-speed lift: retreating blade stall on one rotor is balanced by advancing blade of opposing rotor, eliminating roll divergence at >100 kts."
        ],
        "vulnerabilities": [
            "Catastrophic Blade Clashing: severe cyclic inputs cause dynamic blade flapping; if flapping exceeds mast separation, top and bottom blades collide.",
            "Complex coaxial swashplate hub: dual counter-rotating swashplates and concentric shafts increase maintenance and dust vulnerability.",
            "Severe rotor-induced downwash turbulence during cargo sling hooking operations."
        ],
        "lesson": "Validates the Law of Kinematic Primacy: without fixed wings or stall speed, all rotor disc-loaded vertical lift systems belong strictly to UCV (Unmanned Copter Vehicles).",
        "related": ["01-honda-evtol", "13-fury-ghostbat"]
    },
    {
        "id": "10",
        "slug": "10-orbital-guardian",
        "domain": "UOV",
        "name": "Orbital Guardian ADR Satellite Hunter",
        "token": "UOV: LM-CA-HR",
        "token_full": "UOV: Low Earth Orbit (350-1000km) • ESPA Class 150-300kg • Chemical Stored Thrusters • Active Rendezvous & Grappling • Solo Hunter • Phased Array RF",
        "hal": "ITumblingTargetCapture",
        "hal_def": "Autonomous orbital proximity and interception platforms require ITumblingTargetCapture to solve Clohessy-Wiltshire kinematics, match target 3-axis tumble momentum via CMGs, and execute impedance grappling without kinetic fragmentation.",
        "vendor": "NextGen Arsenal",
        "vendor_slug": "nextgen-arsenal",
        "date": "2026-10-19",
        "source_name": "Facebook Reel / Orbital Proximity Docking Animation",
        "source_url": "https://www.facebook.com/reel/2177636083099811",
        "advantages": [
            "Standardized robotic grappling transforms passive orbital space into an active interception and debris removal domain.",
            "Dual-use operational convergence: Active Debris Removal (ADR) and offensive anti-satellite (ASAT/OSC) share 100% identical hardware contracts.",
            "Direct Keplerian Clohessy-Wiltshire navigation enables micro-impulse station keeping."
        ],
        "vulnerabilities": [
            "The Tsiolkovsky ΔV Attrition Trap: orbital plane changes cost ~2,000 m/s for a 15° inclination shift at LEO; chemical chasers are restricted to single targets.",
            "Angular momentum transfer: latching onto an uncooperative tumbling satellite violently transfers spin, risking mechanical shear.",
            "Secondary Kessler syndrome: relative docking impacts >0.1 m/s risk shattering solar panels and generating clouds of hypervelocity shrapnel."
        ],
        "lesson": "Demolishes sci-fi free-flight orbital tropes: multi-target orbital sweepers require high-power nuclear-electric propulsion; chemical platforms remain single-mission effectors.",
        "related": ["04-waverider-corvus"]
    },
    {
        "id": "11",
        "slug": "11-lockheed-lamprey",
        "domain": "UUV",
        "name": "Lockheed Martin Lamprey MMAUV",
        "token": "UUV: CV-IS-HQ",
        "token_full": "UUV: Continental Shelf 0-500m • Vessel-Attached / Hull Hitchhiker • Hydrokinetic Harvesting • Seabed Ambush (Zhdun Posture) • Solo Hunter • Silent Acoustic",
        "hal": "IParasiticAttachmentDrive",
        "hal_def": "Parasitic undersea autonomous platforms require IParasiticAttachmentDrive and IHydrokineticHarvesting to govern hull boundary-layer suction, harvest power from 20-knot flow, and command positive separation into seabed resting sentinel posture.",
        "vendor": "Lockheed Martin Skunk Works",
        "vendor_slug": "lockheed-martin",
        "date": "2026-10-19",
        "source_name": "Facebook Reel / Undersea Modular Subsystem Concept",
        "source_url": "https://www.facebook.com/reel/2203326470200241",
        "advantages": [
            "Zero Transit Battery Drain: hitchhikes on host submarine/warship hulls; in-transit hydrokinetic turbines arrive on station with 100% battery state-of-charge.",
            "Seabed Ambush (Zhdun Posture): rests on continental shelf with all propulsion off, yielding zero acoustic and thermal signature for weeks of passive listening.",
            "Decoupled Lethality: 24 cu ft modular bay accommodates torpedoes, mine layers, EW jammers, or air-defense UAV launchers."
        ],
        "vulnerabilities": [
            "Boundary layer shear stress: 20-25 knot transit creates massive hydrodynamic drag, risking clamp detachment or acoustic cavitation revealing host sub.",
            "Bernoulli Suction Hazard: separating from moving hull induces low-pressure suction toward host screw propellers, requiring pyrotechnic positive ejection.",
            "Seafloor silt fouling: direct resting on silt risks clogging waterjet impellers and acoustic sonar transducers."
        ],
        "lesson": "Codifies Parasitic Maritime Logistics in UWE: host platform mobility and autonomous robotic effector lethality operate under completely independent energy cycles.",
        "related": ["06-exail-usv", "07-ghostshark-auv"]
    },
    {
        "id": "12",
        "slug": "12-mq25-stingray",
        "domain": "UAV",
        "name": "Boeing MQ-25 Stingray CBARS",
        "token": "UAV: AI-TF-DR",
        "token_full": "UAV: Atmospheric Winged • C4 CATOBAR Carrier Base • Turbofan AE 3007N • Airborne Fuel Tanker (Cobham ARS) • Fleet Escort & Persistent Shield • MESH/COMSAT",
        "hal": "IAerialRefuelingHoseDrogueDrive",
        "hal_def": "Carrier-borne tanker UAVs require IAerialRefuelingHoseDrogueDrive to actively damp drogue basket whip against receiver supersonic bow wave displacement while compensating center-of-gravity shifts during 15,000-lb fuel offloads.",
        "vendor": "Boeing Defense & U.S. Navy",
        "vendor_slug": "boeing",
        "date": "2026-10-20",
        "source_name": "U.S. Navy / NAVAIR Carrier Demonstration Video",
        "source_url": "https://www.facebook.com/SecretaryoftheNavy/videos/1123057570114063/",
        "advantages": [
            "Eliminates carrier air wing fatigue: relieves F/A-18 Super Hornets from wasting 25% of combat flight hours on wasteful buddy-tanking sorties.",
            "Doubles strike radius: pushes F-35C and CCA strike reach from 450 to >900 nmi, allowing carrier strike groups to operate outside DF-21D A2/AD envelopes.",
            "Airborne energy backbone: forms the continuous in-flight refueling lifeline for autonomous Collaborative Combat Aircraft (CCA) along containment lines."
        ],
        "vulnerabilities": [
            "Aerodynamic bow wave whip: receiver aircraft nose pressure wave pushes drogue basket off-center, causing probe strikes and canopy impacts.",
            "Flight deck taxi density: autonomous taxi among tractors and catapults under 120 dB acoustic noise requires robust computer vision wand failsafes.",
            "4G carrier cable trap deceleration creates violent internal fuel slosh, requiring active internal baffles and reinforced gear."
        ],
        "lesson": "Proves UWE Strategic Doctrine: autonomous interdiction shields and containment lines depend fundamentally on distributed aerial refueling infrastructure, not bespoke single-sortie ranges.",
        "related": ["01-honda-evtol", "13-fury-ghostbat"]
    },
    {
        "id": "13",
        "slug": "13-fury-ghostbat",
        "domain": "UAV",
        "name": "Anduril Fury & Boeing MQ-28 Ghost Bat (CCA Triad)",
        "token": "UAV: AL-TC-DR",
        "token_full": "UAV: Atmospheric Transonic M 0.95 • C2 Dispersed Runway • Turbofan FJ44 • Air-to-Air Interceptor (AIM-120 Conformal Bay) • Escort Air Superiority • Lattice OS / MESH",
        "hal": "IHighGEvasiveManeuverDrive",
        "hal_def": "Autonomous air-to-air Collaborative Combat Aircraft mandate IHighGEvasiveManeuverDrive and IAutonomousWeaponSeparation to execute machine-speed 9G intercepts and command >40G positive ejection to suppress transonic cavity resonance (Rossiter modes).",
        "vendor": "Anduril Industries & Boeing Australia",
        "vendor_slug": "anduril",
        "date": "2026-10-20",
        "source_name": "CBS 60 Minutes (Palmer Luckey) & Australian MoD Test Flight",
        "source_url": "https://www.cbsnews.com/news/anduril-ceo-unveils-the-fury-unmanned-fighter-jet-60-minutes/",
        "advantages": [
            "Transonic 9G Kinetic Agility: carbon-composite monocoque construction eliminates pilot G-limits, sustaining 9G evasive missile-breakaway maneuvers.",
            "Low-Observable Conformal Weapons Carriage: internal bays carry AIM-120 and AIM-9X missiles while preserving very-low-observable (VLO) radar signature.",
            "Lattice OS Edge Autonomy: distributed sensor-fusion enables machine-speed radar triangulation, pincer intercepts, and silent forward scouting."
        ],
        "vulnerabilities": [
            "Weapons Bay Cavity Resonance (Rossiter Modes): opening doors at Mach 0.95 creates severe acoustic pressure waves; requires high-force positive ejection.",
            "Internal fuel deficit: compact 9G airframe loiter is limited to <1.5h without aerial refueling, creating an operational dependency on MQ-25 Stingray.",
            "High unit attritability threshold compared to mass-produced FPV multirotors."
        ],
        "lesson": "Validates the Closed UWE Aerial Containment Triad: 1) Kinetic Dogfighter (Fury), 2) Modular Sensor Anchor (MQ-28), 3) Persistent Energy Hub (MQ-25 Tanker) sustaining 24/7 robotic borders.",
        "related": ["03-stealth-ucav", "04-waverider-corvus", "12-mq25-stingray"]
    },
    {
        "id": "14",
        "slug": "14-knds-centurio",
        "domain": "UGV",
        "name": "KNDS CENTURIO Tactical UGV",
        "token": "UGV: GL-DC-DR",
        "token_full": "UGV: Ground Land • C2 Light Tactical (2.8t trailer) • Diesel Hydrostatic Drive (60 kW) • ARX20/30 Autocannon RWS • Combined Arms Fire Support • Resilient LOS RF & Fiber-Optic Spool",
        "hal": "IAllWheelSteeringKinematics",
        "hal_def": "Tactical all-wheel-steer robotic platforms require IAllWheelSteeringKinematics and IHydrostaticTractionControl to coordinate independent four-wheel angles and hydraulic displacement, eliminating skid-steer scrubbing losses and holding 60% slopes, while IRemoteWeaponStationStabilization isolates 20mm/30mm autocannon recoil impulses.",
        "vendor": "KNDS France & Germany",
        "vendor_slug": "knds",
        "date": "2026-10-20",
        "source_name": "Facebook Reel / Defense Advancement",
        "source_url": "https://www.facebook.com/reel/945299761633386",
        "advantages": [
            "4WS Kinematic Primacy: 4-wheel independent steering eliminates lateral tire scrubbing, saving 35–40% traction energy during turns and enabling diagonal crab-crawling.",
            "Hydrostatic Crawl Torque: 60 kW diesel hydrostatic drive provides high low-speed torque without mechanical clutch wear, climbing 60% grades with intrinsic hydrostatic braking.",
            "Zero-Line Fiber-Optic Tethering: deployable optical spool provides unjammable, high-bandwidth telemetry and instant weapon trigger control in dense EW environments."
        ],
        "vulnerabilities": [
            "Hydrostatic Line Shrapnel Sensitivity: 250–350 bar centralized hydraulic circuits risk instant systemic pressure collapse upon fragment penetration; requires ballistic skirts.",
            "Prominent Acoustic and Thermal IR Profile: 60 kW diesel engine exhaust and oil cooling radiators create elevated infrared and acoustic signatures.",
            "High Gross Weight: at 2.8 tonnes, extraction requires dedicated recovery prime movers if immobilized."
        ],
        "lesson": "Validates the Law of Decoupled Lethality in ground combat: the invariant 2.8t 4WS chassis serves as a mobile carrier decoupled from kinetic autocannon or sapper payloads.",
        "related": ["02-slimak-ugv", "08-unex-artillery", "17-frodo-ugv"]
    },
    {
        "id": "15",
        "slug": "15-tekever-ar6",
        "domain": "UCV",
        "name": "TEKEVER AR6 Heavy-Lift UAS",
        "token": "UCV: CL-PL-DR",
        "token_full": "UCV: Rotorcraft Disc-Loaded • C2 Light Tactical (600kg MTOW) • Piston Engine Digital Displacement Fluid Power • Heavy Logistics (200kg / 500km) • Forward Force Support • Anti-Jam & GNSS-Denied",
        "hal": "IDigitalDisplacementHydraulicDrive",
        "hal_def": "Heavy-lift fluid-power multirotor platforms require IDigitalDisplacementHydraulicDrive to execute sub-20ms digital valve sequencing across distributed hydraulic rotor hubs, converting liquid fuel energy density into microsecond differential thrust while decoupling heavy cargo dynamics under GNSS denial.",
        "vendor": "TEKEVER",
        "vendor_slug": "tekever",
        "date": "2026-10-20",
        "source_name": "LinkedIn / German Army Logistics Validation",
        "source_url": "https://lnkd.in/p/d9Ztc8D8",
        "advantages": [
            "Breaking the Multirotor Specific Energy Bottleneck: liquid fuel (12,000 Wh/kg) driving digital hydraulics delivers 200+ kg payload over 500 km range in a pure VTOL footprint.",
            "Digital Fluid Power Simplicity: eliminates failure-prone mechanical transmissions, swashplates, and pitch pushrods in favor of high-speed digital hydraulic valves.",
            "Frontline GLOC Resupply: enables non-line-of-sight autonomous artillery shell, ammunition, and battery delivery across interdicted frontline corridors without crew exposure."
        ],
        "vulnerabilities": [
            "Continuous Acoustic and Thermal Profile: internal combustion engine creates a continuous acoustic signature and thermal exhaust plume vulnerable to SHORAD.",
            "Hydraulic Water Hammer Fatigue: rapid digital valve cycling induces hydraulic pressure transients in flexible hoses, demanding pulsation dampers and telemetry monitoring.",
            "High Rotor Disc Downwash: heavy disc loading creates violent dust and debris downwash during forward unprepared site landings."
        ],
        "lesson": "Establishes the fluid-power heavy-lift standard within UCV: pure battery power is restricted to tactical micro-strike, while operational sustainment mandates fluid-power density.",
        "related": ["01-honda-evtol", "09-capstone-coaxial"]
    },
    {
        "id": "16",
        "slug": "16-rq81-diana",
        "domain": "UAV",
        "name": "'RQ-81 Diana' / Solar HAPS Architecture",
        "token": "UAV: AL-ER-DO",
        "token_full": "UAV: Atmospheric Stratospheric (20km) • C2 Modular Wing-Box • Solar Photovoltaic + Secondary Battery • Persistent C4ISR Overwatch • Strategic Defense • Optical Laser ISL & MESH",
        "hal": "ISolarDiurnalEnergyManagement",
        "hal_def": "Stratospheric solar pseudo-satellite platforms require ISolarDiurnalEnergyManagement and IAeroelasticFlutterSuppression to balance solar harvesting against nocturnal gravitational descent while actively damping aerodynamic gust-induced limit-cycle flutter across flexible wings.",
        "vendor": "Stratospheric Defense & HAPS Aerospace",
        "vendor_slug": "haps-consortium",
        "date": "2026-10-20",
        "source_name": "Facebook Reel / US NextGen Airpower (Unverified Spec)",
        "source_url": "https://www.facebook.com/reel/1080077671497853",
        "advantages": [
            "Persistent Stratospheric Station-Keeping: operating at 65,000 ft (20 km) in the stratospheric wind minimum allows unattenuated solar harvesting and multi-month persistence.",
            "Stationary Regional Persistence: provides stationary persistence over tactical theaters with microsecond optical/RF ground latency and zero rocket launch costs.",
            "Laser Cross-Link Gateway: serves as a high-bandwidth optical laser relay bridging terrestrial drone swarms directly to orbital defense constellations."
        ],
        "vulnerabilities": [
            "Physics Debunking: optical line-of-sight horizon at 20 km is ~505 km (maximum theoretical area ~800,000 km², less than 8% of the US landmass, debunking viral clickbait claims).",
            "Nocturnal Energy Deficit: low 7% air density requires climbing to 70,000 ft during daylight and descending to 50,000 ft at night to trade potential energy for aerodynamic lift.",
            "Tropospheric Jet Stream Flutter: ultra-high-aspect-ratio flexible wings risk catastrophic limit-cycle flutter when traversing turbulent 35,000 ft jet streams."
        ],
        "lesson": "Demarcates the boundary between aerodynamic pseudo-satellites (UAV: AL-ER-DO) and true orbital platforms (UOV); enforces physical rigor over CGI military entertainment tropes.",
        "related": ["03-stealth-ucav", "04-waverider-corvus", "10-orbital-guardian"]
    },
    {
        "id": "17",
        "slug": "17-frodo-ugv",
        "domain": "UGV",
        "name": "НРК «Фродо» 6x6 Universal Tactical UGV",
        "token": "UGV: GL-EM-DR",
        "token_full": "UGV: Ground Land • C2 Tactical (500-700kg gross) • Electric Quick-Swap Battery • Multi-Mission (200-400kg / CASEVAC / Buriya Turret) • Tactical Force Support • Multi-Bearer Starlink/Silvus/ELRS",
        "hal": "IIndependent6x6TractionControl",
        "hal_def": "High-speed tactical ground robotics platforms require IIndependent6x6TractionControl and IAdaptiveClearanceSuspension to redistribute torque under single-wheel loss (N-1) and modulate ground clearance (170-330mm) for 40 km/h FPV evasion, while IMultiBearerTacticalGateway manages seamless C2 failover under dense EW.",
        "vendor": "Ukrainian Frontline Defense-Tech & Robotics",
        "vendor_slug": "frontline-ua",
        "date": "2026-10-24",
        "source_name": "Facebook Reel / Taurus UGV Company, 5th Assault Brigade",
        "source_url": "https://www.facebook.com/reel/2263655697790308",
        "advantages": [
            "40 km/h Sprint Velocity as Kinetic Active Defense: cuts open-ground kill zone exposure time by 70% and breaks the terminal guidance intercept angle of enemy FPV strike drones.",
            "6x6 Wheel Mesh with N-1 Redundancy: independent suspension across all 6 wheels provides mobility across shell craters and allows mission completion even after single-wheel combat loss.",
            "Adaptive Clearance & Quick-Swap Battery: modulates height (170–330 mm) for terrain concealment or obstacle clearing; modular batteries swap in minutes supporting 150 km range."
        ],
        "vulnerabilities": [
            "High-Speed Dynamic Suspension Fatigue: rough terrain sprint at 40 km/h induces extreme dynamic shock loads (G_z > 4–6g) requiring continuous vibration telemetry.",
            "Visual Silhouette at Max Clearance: full 330 mm elevation raises center of gravity and increases side visual detection profile.",
            "Battery Mass vs Ballistic Armor Trade-off: preserving 40 km/h agility limits passive armor thickness, making dynamic speed the primary defensive shield."
        ],
        "lesson": "Codifies Kinetic Evasion as the frontline survivability standard in UGV:GL; demonstrates the value of co-designing tactical robotics with combat units (5th Assault Brigade).",
"related": ["02-slimak-ugv", "08-unex-artillery", "14-knds-centurio"]
    },
    {
        "id": "18",
        "slug": "18-vantage-tacitframe",
        "domain": "UAV",
        "name": "Vantage Tacitframe / 'The Whale' (Tacit Blue Legacy)",
        "token": "UAV: AL-TR-DR",
        "token_full": "UAV: Atmospheric Low-Observable • C2 Light Tactical / Dispersed • Turbofan Powerplant • Reconnaissance & C4ISR • Resilient Defense • Low Probability of Intercept MESH/AESA",
        "hal": "IContinuousCurvatureStealthDynamics",
        "hal_def": "Unmanned continuous-curvature low-observable airframes mandate IContinuousCurvatureStealthDynamics to eliminate cockpit canopy radar cavity reflections and govern digital fly-by-wire stability across unstable faceted-curvature planforms.",
        "vendor": "Vantage Aerospace / Northrop Grumman Legacy",
        "vendor_slug": "vantage-aerospace",
        "date": "2026-10-25",
        "source_name": "Facebook Reel / Tactical Low-Observable Aerodynamics",
        "source_url": "https://www.facebook.com/reel/1092850673159459",
        "advantages": [
            "Continuous-Curvature Gaussian Shaping: eliminates pilot cockpit canopy, removing radar cavity retro-reflection and freeing 30% airframe internal volume for fuel and AESA apertures.",
            "360° All-Aspect Low RCS: faceted-curvature shielding minimizes radar return across VHF to Ku bands, enabling survivable loiter over hostile airspace.",
            "Conformal Sensor Integration: replaces bulky drag-inducing spherical chin gimbals with flush conformal sapphire apertures and side-looking radar tiles."
        ],
        "vulnerabilities": [
            "Aerodynamic Brick Instability: low lift-to-drag ratio and unstable yaw/pitch dynamics require continuous high-cadence (>80 Hz) digital fly-by-wire corrections.",
            "Internal Volume Packaging Constraints: thermal buildup in tightly packed composite payload bays demands active heat exchangers.",
            "High Unit Production Complexity: complex compound curves elevate tooling and composite curing costs compared to tubular airframes."
        ],
        "lesson": "Validates Law of Kinematic Primacy: eliminating the human pilot allows pure continuous-curvature aerodynamic stealth, decoupling carrier survival from external pods.",
        "related": ["03-stealth-ucav", "04-waverider-corvus", "13-fury-ghostbat"]
    },
    {
        "id": "19",
        "slug": "19-petrel-aero-sky",
        "domain": "UAV",
        "name": "Petrel Technologies AERO Sky Drone Mothership",
        "token": "UAV: AL-TH-DR",
        "token_full": "UAV: Atmospheric Lift • C2 Light Airfield • Turboprop / Heavy Fuel • Mothership Carrier & FPV Air-Drop • Tactical Escort & Deep Penetration • Airborne MESH Relay",
        "hal": "IAirborneMothershipCarrier",
        "hal_def": "Airborne drone mothership carriers mandate IAirborneMothershipCarrier and IAirborneMeshRelayGateway to manage dynamic center-of-gravity shifts during multi-UAV drop salvos while maintaining high-altitude COFDM data routing to deployed sub-munitions.",
        "vendor": "Petrel Technologies & Sustainable Skylines",
        "vendor_slug": "petrel-tech",
        "date": "2026-10-25",
        "source_name": "Facebook Reel / Mothership Air-Drop Demonstration",
        "source_url": "https://www.facebook.com/reel/4466377780286509",
        "advantages": [
            "Endurance Multiplier: fixed-wing cruise (L/D ≈ 12-15) transports tactical strike copters 40-60 km deep, overcoming multirotor battery limits.",
            "High-Altitude Relay Node: loitering mothership acts as a line-of-sight RF relay, eliminating terrain masking and low-altitude EW shadow zones.",
            "Rapid Air-Drop Deployment: internal payload bay dispenses strike swarms at high altitude with zero launch battery consumption."
        ],
        "vulnerabilities": [
            "Single Point of Failure: loss or electronic blinding of the mothership severs C2 links for all tethered strike drones simultaneously.",
            "Acoustic and Radar Vulnerability: loitering at 2-3 km altitude exposes the mothership to medium-range air defense systems.",
            "Drop Separation Turbulence: wake turbulence from mothership wings risks destabilizing lightweight copters during ejection."
        ],
        "lesson": "Validates Law of Hierarchical Containerization: nested carrier-subcarrier architectures extend tactical strike depth without expensive heavy strategic airframes.",
        "related": ["01-honda-evtol", "13-fury-ghostbat", "21-tactical-ucv-spectrum"]
    },
    {
        "id": "20",
        "slug": "20-tusas-aksungur",
        "domain": "UAV",
        "name": "TUSAŞ Aksungur Maritime ASW UCAV (aselBUOY Gateway)",
        "token": "UAV: AT-PS-DS",
        "token_full": "UAV: Atmospheric Medium-Altitude • C3 Heavy Runway • Twin Turbodiesel • ASW Subsea Sonobuoy Drop & Acoustic Gateway • Maritime Border Screen • Multi-Band SATCOM & Tactical Line-of-Sight",
        "hal": "IAswSonobuoyAcousticGateway",
        "hal_def": "Maritime patrol UCAVs acting as cross-domain acoustic nodes require IAswSonobuoyAcousticGateway and ISubseaAcousticDataFusion to deploy sonobuoy fields, maintain low-latency hydroacoustic telemetry, and calculate target depth horizons.",
        "vendor": "Turkish Aerospace (TUSAŞ) & ASELSAN",
        "vendor_slug": "tusas-aselsan",
        "date": "2026-10-25",
        "source_name": "LinkedIn / Naval News ASW Sonobuoy Drop",
        "source_url": "https://lnkd.in/p/dW53c44c",
        "advantages": [
            "Cross-Domain Air-to-Subsea Gateway: deploys aselBUOY 100P sonobuoys, bridging pelagic acoustic signals directly into the theater air C2 mesh.",
            "50+ Hour Diurnal Patrol Persistence: twin PD-170 turbodiesel engines burn kerosene/heavy fuel efficiently, providing continuous maritime choke-point coverage.",
            "750 kg Multi-Mission Payload Bay: simultaneously carries sonobuoy launcher pods, maritime search radar, and lightweight ASW torpedoes."
        ],
        "vulnerabilities": [
            "Acoustic Horizon Transmission Loss: shallow surface thermoclines can distort and attenuate sonobuoy acoustic signals in coastal waters.",
            "Radar Cross-Section Vulnerability: large 24m straight-wing planform is detectable by naval air defense radars at 100+ km range.",
            "Turbodiesel Cold-Soak Ceiling Limits: operating near 30,000 ft in icing conditions risks fuel freezing and turbocharger intercooler clogging."
        ],
        "lesson": "Validates Cross-Domain Heterogeneous Kill Web: persistent fixed-wing UAS serve as indispensable acoustic relay anchors for undersea warfare.",
        "related": ["07-ghostshark-auv", "11-lockheed-lamprey", "12-mq25-stingray"]
    },
    {
        "id": "21",
        "slug": "21-tactical-ucv-spectrum",
        "domain": "UCV",
        "name": "Ukrainian Tactical Strike UCV Fleet Spectrum",
        "token": "UCV: HQ-TE-IR",
        "token_full": "UCV: High-Speed Multirotor Munition • C1 Hand/Tube Deployable • High C-Rate Lithium Electric • Terminal Kinetic Strike & Fiber-Guided Interception • Attritable Frontline Assault • Zero-RF Fiber / Edge-AI Optical",
        "hal": "ITerminalOpticalFiberGuidance",
        "hal_def": "Tactical combat copters operating in contested EW environments require ITerminalOpticalFiberGuidance and IHighGTerminalSprint to execute 450 km/h kinematic dives and optical contrast terminal locks without RF emission.",
        "vendor": "Ukrainian Drone Coalition & DefPulse",
        "vendor_slug": "defpulse-coalition",
        "date": "2026-10-26",
        "source_name": "LinkedIn / Frontline UCV Spectrum Analysis",
        "source_url": "https://lnkd.in/p/d9d2z_V8",
        "advantages": [
            "Kinetic Sprint Sprint Interception: sprint speeds reaching 450 km/h (P1-Sun) break the evasive maneuvers of fixed-wing reconnaissance drones.",
            "Zero-RF Fiber Munition: 10-25 km fiber-optic spools (Zhakh/Khyzhak) bypass intense EW and radar jammer umbrellas completely.",
            "Edge-AI Optical Terminal Lock: auto-tracking algorithms (Vyriy PRO) execute terminal homing without pilot RF tether."
        ],
        "vulnerabilities": [
            "Extreme C-Rate Discharge: high-speed dash pulls 40-60C from lithium cells, causing voltage drop and short 3-5 minute flight times.",
            "Fiber Spool Snag Risk: unspooling wire can shear on tree branches, wire obstacles, or vehicle sharp edges during low-level transit.",
            "Aerodynamic Parasitic Drag: exposed quadcopter arms and payloads cause severe parasite drag power scaling at speeds >200 km/h."
        ],
        "lesson": "Demolishes 'FPV' slang: copter munitions are specialized cyber-physical UCVs differentiated by kinetic intercept velocity, fiber resilience, and edge autonomy.",
        "related": ["09-capstone-coaxial", "15-tekever-ar6", "23-lpp-jwi4000"]
    },
    {
        "id": "22",
        "slug": "22-stratonex-varan",
        "domain": "UGV",
        "name": "Stratonex VARAN Heavy Attrition UGV",
        "token": "UGV: WM-LE-PQ",
        "token_full": "UGV: Wheeled Medium • C2 Light Transport • Low-Cost Electric • Towing & Frontline Logistics (500kg/1t) • Attritable Mass • Passive Optical/RF",
        "hal": "IActiveGeometrySuspension",
        "hal_def": "Low-cost high-payload ground robotics require IActiveGeometrySuspension and IPassiveVisualOdometry to adjust chassis ground clearance over mud and ruts while navigating without active ELINT-emitting sensors.",
        "vendor": "Stratonex Robotics",
        "vendor_slug": "stratonex",
        "date": "2026-10-26",
        "source_name": "Defence Blog / Industrial Prototype",
        "source_url": "https://lnkd.in/p/dDrYcfbn",
        "advantages": [
            "Extreme Attritable Economy: built with commodity components and structural timber/sheet metal to ensure cheap replacement under mass artillery.",
            "Passive Stealth Navigation: replaces active LIDAR and radar emitters with passive stereoscopic optical odometry to avoid enemy radio reconnaissance.",
            "High Towing Ratio: 500 kg onboard payload plus 1,000 kg towing drawbar allows remote ammunition supply to forward firing trenches."
        ],
        "vulnerabilities": [
            "Quasi-Static Geometry Linkage: motorized lever arm suspension increases mechanical stress points in viscous clay/black soil.",
            "Unarmored Hull Vulnerability: commodity construction offers zero protection against mortar shell fragments and FPV shaped charges.",
            "Open-Loop Actuator Torque Stalls: deep soil ruts stall low-voltage electric gearboxes without closed-loop current monitoring."
        ],
        "lesson": "Validates Law of Attritable Mass: frontline ground combat requires disposable, software-governed transport carriers costing less than single precision munitions.",
"related": ["02-slimak-ugv", "08-unex-artillery", "17-frodo-ugv"]
    },
    {
        "id": "23",
        "slug": "23-lpp-jwi4000",
        "domain": "UAV",
        "name": "LPP JWI-4000 High-Ceiling C-UAS Interceptor",
        "token": "UAV: AC-RE-AQ",
        "token_full": "UAV: Atmospheric C-UAS Interceptor • C1 Hand-Deployable / Tube • Rocket/Electric Hybrid • Kinetic & Blast Interception • Point Air Defense • ASTERIX Radar Cueing & Optical Lock",
        "hal": "IAirborneInterceptionDynamics",
        "hal_def": "Dedicated vertical-launch C-UAS interceptors mandate IAirborneInterceptionDynamics and IAsterixRadarCueingGateway to execute 35 m/s vertical sprints to 4,000m ceiling and govern terminal blast fragmentation at 130+ m/s closure rates.",
        "vendor": "LPP Praha",
        "vendor_slug": "lpp-praha",
        "date": "2026-10-26",
        "source_name": "LinkedIn / LPP Technical Specification",
        "source_url": "https://lnkd.in/p/d6DutPRP",
        "advantages": [
            "4,000m Vertical Interception Ceiling: reaches high-altitude Orlan/Supercam reconnaissance drones far above handheld MANPADS envelopes.",
            "ASTERIX Protocol Integration: directly ingests NATO standard radar tracks for autonomous midcourse flight vectoring.",
            "Thermobaric Blast Expansion: 1.8 kg thermobaric warhead compensates for sensor latency and terminal miss distance at high closure velocities."
        ],
        "vulnerabilities": [
            "V^3 Aerodynamic Power Penalty: drag power scales cubically with velocity, exhausting battery reserves within 3-4 minutes of high-speed climb.",
            "Terminal Optical Glint: direct sun alignment or low-contrast cloud horizons can temporarily blind the forward optical tracker.",
            "High Acceleration G-Forces: rapid climb and pull-up impose high structural loads on composite control fins."
        ],
        "lesson": "Validates Kinetic Interception Physics: defeating strategic reconnaissance drones requires dedicated vertical sprint interceptors rather than retrofitted quadcopters.",
        "related": ["03-stealth-ucav", "13-fury-ghostbat", "21-tactical-ucv-spectrum"]
    },
    {
        "id": "24",
        "slug": "24-lurtz-kill-zone",
        "domain": "UGV",
        "name": "Autonomous Kill Zone & HMT Architecture (Patrick Lurtz)",
        "token": "UGV: GL-DC-DR",
        "token_full": "UGV: Ground Land • C2 Tactical Footprint • Hybrid Powertrain • Combined Arms Kinetic Defense • Deep Kill-Web Integration • Low-Cadence Human Intent Link",
        "hal": "IHumanMachineIntentGateway",
        "hal_def": "Combined arms human-machine teaming architectures require IHumanMachineIntentGateway and IDynamicKillWebRouting to decouple high-frequency 300+ APM robotic vehicle reflexes from low-cadence (2-3 CPM) human commander lethal authorizations.",
        "vendor": "Patrick Lurtz / European MilTech Architecture",
        "vendor_slug": "lurtz-hmt",
        "date": "2026-11-01",
        "source_name": "LinkedIn / Tactical Kill Zone Doctrine",
        "source_url": "https://lnkd.in/p/d7ptMX9P",
        "advantages": [
            "Cognitive Bandwidth Decoupling: human operators provide mission rules of engagement (ROE) while edge AI executes microsecond pathfinding and weapon stabilization.",
            "Kill Zone Depth Multiplication: dispersed UGVs form 5-10 km autonomous screen lines, absorbing enemy reconnaissance without risking crewed armor.",
            "Heterogeneous Sensor Fusion: merges acoustic gunfire detectors, seismic sensors, and thermal vision into unified target queues."
        ],
        "vulnerabilities": [
            "RF Interception in Electronic Contested Zones: high-bandwidth video backhauls broadcast vehicle positions to enemy SIGINT.",
            "Adversarial Visual Deception: smoke screens, decoy thermal flares, and camouflage netting can spoof edge object-detection models.",
            "Mechanical Logistics Strain: multi-axle tracked and wheeled robotic fleets require high spare parts and field recovery capacity."
        ],
        "lesson": "Establishes HMT Control Layer in UWE: humans command intent at doctrinal cadence; machines execute physics at microsecond edge loops.",
        "related": ["02-slimak-ugv", "14-knds-centurio", "17-frodo-ugv"]
    },
    {
        "id": "25",
        "slug": "25-stat-caylus-b2lt",
        "domain": "UAV",
        "name": "French Army STAT Caylus C-UAS B2LT",
        "token": "UAV: AC-RE-AQ",
        "token_full": "UAV: Atmospheric C-UAS • C1 Hand-Deployable • Rocket/Turbine Hybrid • Hard-Kill Kinetic Interception • Urban & Littoral Defense • Local Radar & Acoustic Cueing",
        "hal": "IKineticHitToKillAutonomy",
        "hal_def": "Tube-launched anti-drone interceptors require IKineticHitToKillAutonomy and IAcousticVectorGuidance to execute terminal 30G intercept burns, colliding directly with agile maneuvering copters at microsecond control loops.",
        "vendor": "French Army STAT & Caylus Urban Combat Center",
        "vendor_slug": "stat-caylus",
        "date": "2026-11-01",
        "source_name": "LinkedIn / STAT B2LT Urban Field Trials",
        "source_url": "https://lnkd.in/p/d6h_9H4B",
        "advantages": [
            "Zero Collateral Damage Hard-Kill: direct kinetic body-to-body impact destroys hostile multirotors without explosive fragmentation in populated areas.",
            "Rapid Tube Deployment: pneumatic cold-gas launch clears container in <0.2s before rocket motor ignition.",
            "Omnidirectional Threat Response: 360° launch capability with zero turret slew latency protects forward command posts."
        ],
        "vulnerabilities": [
            "Miss Distance Zero-Tolerance: kinetic impact requires sub-10 cm guidance accuracy; any aerodynamic buffeting causes complete miss.",
            "Single-Target Engagement: each tube intercepts exactly one drone, making defensive salvos vulnerable to mass swarm saturation.",
            "Propellant Smoke Trail: solid rocket motor exhaust provides optical back-azimuth revealing launcher position."
        ],
        "lesson": "Validates Point Defense Kinematics: defeating saturation multirotor raids mandates tube-launched kinetic interceptors integrated into local acoustic cueing grids.",
        "related": ["13-fury-ghostbat", "21-tactical-ucv-spectrum", "23-lpp-jwi4000"]
    },
    {
        "id": "26",
        "slug": "26-kashmir-sentinel",
        "domain": "UAV",
        "name": "Kashmir Border Swarm Sentinel AESA",
        "token": "UAV: AM-TD-RA",
        "token_full": "UAV: Atmospheric Mountainous • C2 Short Takeoff • Turboprop / Heavy Fuel • Forward Radar Picket & Swarm Interdiction • Mountain Border Defense • Active AESA Radar & MESH Gateway",
        "hal": "IMountainousAesaOverwatch",
        "hal_def": "Mountain border surveillance UAS require IMountainousAesaOverwatch and ITerrainMaskingClutterRejection to isolate micro-UAV radar cross-sections (<0.01 m²) against steep alpine ground clutter while maintaining MESH links through deep valleys.",
        "vendor": "Choudhary Tactical / Border Surveillance Consortium",
        "vendor_slug": "kashmir-sentinel",
        "date": "2026-11-02",
        "source_name": "LinkedIn / Tactical Mountain Border Defense",
        "source_url": "https://lnkd.in/p/dMhG2277",
        "advantages": [
            "Alpine Clutter Suppression: pulse-Doppler AESA radar filters mountain face ground reflections, detecting low-flying stealth copters.",
            "Valley MESH Repeater: airborne loiter altitude provides line-of-sight communications over steep ridgelines, un-masking isolated border outposts.",
            "High-Density Swarm Cueing: tracks up to 128 individual airborne contacts simultaneously and directs defensive interceptors."
        ],
        "vulnerabilities": [
            "Severe High-Altitude Density Altitude: thin mountain air at 4,000-5,000m degrades propeller thrust and increases stall speeds.",
            "Extreme Katabatic Wind Turbulence: violent mountain downdrafts challenge airframe structural margins and gimbal stabilization.",
            "RF Radiation Vulnerability: active AESA radar emissions illuminate the picket platform to enemy anti-radiation missiles."
        ],
        "lesson": "Enforces Kinematic Primacy in Alpine medium: border interdiction in rugged relief requires elevated radar picket nodes to eliminate valley radar shadows.",
        "related": ["03-stealth-ucav", "15-tekever-ar6", "20-tusas-aksungur"]
    },
    {
        "id": "27",
        "slug": "27-rusi-rasputitsa",
        "domain": "UGV",
        "name": "RUSI Frontline Rasputitsa Ground Dynamics",
        "token": "UGV: GL-EM-DR",
        "token_full": "UGV: Ground Land • C2 Heavy Transport • Hybrid Diesel-Electric • Logistics Sustainment & Mine Breaching • Frontline Environmental Survival • Wideband Starlink/COFDM",
        "hal": "IBekkerViscousSoilAdhesion",
        "hal_def": "Heavy autonomous ground logistics vehicles require IBekkerViscousSoilAdhesion and IDifferentialTorqueVectoring to dynamically modulate wheel slip between 15% and 25%, preventing sinkage and catastrophic soil shear failure in deep rasputitsa mud.",
        "vendor": "RUSI & Frontline Operational Analysis",
        "vendor_slug": "rusi-analysis",
        "date": "2026-11-02",
        "source_name": "RUSI / Frontline Rasputitsa Operational Assessment",
        "source_url": "https://lnkd.in/p/dr6p8uU9",
        "advantages": [
            "Continuous Mud Mobility: algorithmic traction control prevents wheel spin-down, maintaining forward momentum through 50 cm clay ruts.",
            "Distributed All-Wheel Power: independent electric hub motors deliver instant micro-torque adjustments across 6 or 8 traction contact patches.",
            "Autonomous Convoy Tethering: leader-follower visual tracking allows single manned lead vehicles to guide multiple robotic supply platforms."
        ],
        "vulnerabilities": [
            "Belly Drag Immobilization: soft mud buildup under flat hull belly plates creates vacuum suction, neutralizing wheel normal force.",
            "Radiator & Intake Clay Clogging: viscous soil spray clogs hybrid engine cooling radiators, inducing thermal overheating shutdowns.",
            "Extreme Mechanical Attrition: abrasive quartz sand and clay slurry destroy axle bearings, seals, and brake pads within 100-200 operating hours."
        ],
"lesson": "Confirms Environmental Abstraction Layer (EAL): frontline robotic supremacy is determined by soil shear mechanics and environmental durability, not laboratory autonomy software.",
        "related": ["02-slimak-ugv", "08-unex-artillery", "17-frodo-ugv"]
    },
    {
        "id": "28",
        "slug": "28-south-china-reef",
        "domain": "USV",
        "name": "South China Sea Artificial Reef Interdiction USV",
        "token": "USV: PM-DE-AR",
        "token_full": "USV: Planing/Semi-Displacement Maritime • C3 Heavy Slipway • Diesel Waterjet • Littoral Interdiction & Harbor Defense • Asymmetric Sea Denial • Anti-Jam Satellite & Line-of-Sight MESH",
        "hal": "IShallowReefHydrodynamics",
        "hal_def": "Littoral strike and patrol surface robotics require IShallowReefHydrodynamics and IWaveImpactDamping to execute 45+ knot high-speed sprints across shallow coral atolls while damping 5G wave slap shocks on sensitive mast optronics.",
        "vendor": "PLAN / Indo-Pacific Strategic Analysis",
        "vendor_slug": "south-china-reef",
        "date": "2026-11-03",
        "source_name": "Defense One / Indo-Pacific Littoral Analysis",
        "source_url": "https://lnkd.in/p/d9d2z_V8",
        "advantages": [
            "Shallow-Draft Atoll Navigation: waterjet propulsion draws under 0.8m of water, navigating shallow lagoons impassable to frigates.",
            "High-Speed Wave Impact Attenuation: carbon-reinforced stepped hull planes efficiently at Sea State 3, providing rapid reaction to island incursions.",
            "Integrated Kinetic Defense: mounts remote weapon stations with dual anti-air FPV interceptors and anti-ship missile canisters."
        ],
        "vulnerabilities": [
            "Waterjet Coral Ingestion: suspended coral rubble and seaweed in shallow lagoons risk clogging waterjet intake grates, causing impeller cavitation.",
            "Extreme Tropical Saline Corrosion: 35°C water and 90% humidity accelerate salt crystallization and galvanization in composite-aluminum joints.",
            "Satellite Jamming Vulnerability: open-ocean operations depend heavily on satellite downlinks, making vessels vulnerable to regional GNSS/COMSAT spoofing."
        ],
        "lesson": "Validates Littoral Hydrodynamic Primacy: shallow-water maritime denial demands shallow-draft waterjet hulls with robust shock-mounted sensor masts.",
        "related": ["06-exail-usv", "29-fitburg-sentinel", "30-philippine-carrier"]
    },
    {
        "id": "29",
        "slug": "29-fitburg-sentinel",
        "domain": "UUV",
        "name": "Fitburg Anchor Drag Critical Undersea Infrastructure Defense",
        "token": "UUV: CV-IS-HQ",
        "token_full": "UUV: Continental Shelf Seabed • C2 Autonomous Deployment • Battery & Fuel Cell • Seabed Infrastructure Defense & Cable Picket • Strategic Deterrence • Acoustic Underwater Modem & Optical Link",
        "hal": "ISeabedAnchorMonitoring",
        "hal_def": "Seabed critical infrastructure defense robotics require ISeabedAnchorMonitoring and IHydroacousticInterceptionArray to detect and localize hostile commercial anchor-dragging attacks on subsea telecommunication cables and gas pipelines in real time.",
        "vendor": "Fitburg Marine & Subsea Infrastructure Defense",
        "vendor_slug": "fitburg",
        "date": "2026-11-03",
        "source_name": "Naval News / Critical Undersea Infrastructure Picket",
        "source_url": "https://lnkd.in/p/d6h_9H4B",
        "advantages": [
            "Continuous Infrastructure Overwatch: autonomous crawling and loitering on the continental shelf provides 24/7 acoustic listening along fiber corridors.",
            "Non-Attributable Threat Attribution: records acoustic signatures of dragging vessel anchors, proving deliberate sabotage vs maritime accidents.",
            "Modular Seabed Interdiction: capable of releasing warning acoustic beacons, deploying cable-repair anchors, or marking sabotage platforms."
        ],
        "vulnerabilities": [
            "Extreme Hydrostatic Silt Sinking: prolonged stationary posture on loose seabed silt causes chassis subsidence, requiring buoyant ejection tanks.",
            "Acoustic Communication Bandwidth: underwater acoustic modems provide under 10 kbps throughput, requiring onboard AI to process raw sonar contacts.",
            "Commercial Trawler Snag Hazard: heavy bottom-trawling fishing nets can ensnare or displace the sentinel vehicle."
        ],
        "lesson": "Codifies Subsea Critical Infrastructure Protection (CUI) in UWE: defending democratic digital subsea cables requires stationary, autonomous seabed sentinels.",
        "related": ["07-ghostshark-auv", "11-lockheed-lamprey", "28-south-china-reef"]
    },
    {
        "id": "30",
        "slug": "30-philippine-carrier",
        "domain": "USV",
        "name": "Philippine Dual-Carrier Chokepoint Saturation USV",
        "token": "USV: SM-DE-AR",
        "token_full": "USV: Surface Marine • C2 Tactical Footprint • Twin Diesel / Surface Piercing • Chokepoint Interdiction & Swarm Strike • Asymmetric Strait Defense • Redundant SATCOM & High-Speed Optical MESH",
        "hal": "IChokepointSwarmSaturation",
        "hal_def": "Maritime chokepoint interdiction USVs mandate IChokepointSwarmSaturation and ICoordinatedPincerAttack to synchronize high-speed multi-axis swarm strikes across narrow island straits, overwhelming warship close-in weapons systems (CIWS).",
        "vendor": "Philippine Armed Forces / Littoral Defense",
        "vendor_slug": "philippine-carrier",
        "date": "2026-11-04",
        "source_name": "USNI News / Philippine Maritime Littoral Defense",
        "source_url": "https://lnkd.in/p/dMhG2277",
        "advantages": [
            "Narrow Strait Geographic Multiplier: operating within island straits (Luzon/Mindoro) eliminates open-ocean transit penalties, concentrating mass.",
            "Multi-Axis Pincer Saturation: coordinates 12-24 surface strike drones to attack large capital ships simultaneously from 360° azimuths.",
            "Low Radar Cross-Section Stealth: wave-piercing low-freeboard hull reflects radar beams upward, delaying optical/radar detection until 3-4 km range."
        ],
        "vulnerabilities": [
            "Close-In Autocannon Degradation: 30mm naval autocannons and helicopter-fired rockets can destroy lead surface drones in clear daylight.",
            "Island Terrain RF Masking: steep coastal mountains block line-of-sight command relays, requiring airborne UAV or high-elevation repeaters.",
            "Surface Sea State Limits: Sea State 4+ waves (>2.5m) significantly reduce maximum sprint speed and risk capsizing small 6-8m hulls."
        ],
        "lesson": "Proves the Law of Asymmetric Chokepoint Denial: small autonomous surface fleets operating in archipelagic straits can neutralize multimillion-dollar naval strike groups.",
        "related": ["06-exail-usv", "28-south-china-reef", "29-fitburg-sentinel"]
    },
    {
        "id": "31",
        "slug": "31-spm-kondratyuk",
        "domain": "UOV",
        "name": "SPM Group Kondratyuk 1.0 FEU LEO ADR Hunter",
        "token": "UOV: LM-CA-HR",
        "token_full": "UOV: Low Earth Orbit (LEO 400-800km) • C2 SmallSat / ESPA Ring • Chemical Monopropellant & Reaction Wheels • Active Debris Removal & Co-Planar Intercept • Orbital Shield & Counter-Space • Radiation-Hardened Laser Cross-Link",
        "hal": "IRendezvousProximityOperations",
        "hal_def": "Unmanned orbital vehicles require IRendezvousProximityOperations and INonCooperativeDockingCapture to compute Clohessy-Wiltshire relative trajectory burns within sub-centimeter tolerances and grapple tumbling non-cooperative orbital targets without creating debris clouds.",
        "vendor": "SPM Group & Ukrainian Space Cluster",
        "vendor_slug": "spm-group",
        "date": "2026-11-05",
        "source_name": "SPM Group Technical Whitepaper / Orbital Demonstration",
        "source_url": "https://lnkd.in/p/d9d2z_V8",
        "advantages": [
            "Non-Cooperative Tumbling Capture: robotic tentacles and visual LIDAR track tumbling spent rocket stages, securing latch without docking ports.",
            "Dual-Use Counter-Space Capability: identical proximity flight laws enable peaceful debris de-orbiting and neutralization of hostile reconnaissance satellites.",
            "Precision Micro-Thruster Pulse: cold-gas / monopropellant thrusters deliver millinewton impulse bits for safe close-in orbital approach."
        ],
        "vulnerabilities": [
            "Finite Delta-V Budget: 350-500 m/s total ΔV restricts missions to 1-2 major co-planar targets; inclination changes are impossible without refueling.",
            "Space Radiation Single-Event Upsets: intense cosmic rays and solar flares can flip memory bits in commercial grade edge processors.",
            "Collision Cascade Risk (Kessler Syndrome): any guidance thruster failure during docking risks generating thousands of high-velocity debris fragments."
        ],
        "lesson": "Establishes Orbital Regime in UWE: space vehicles (UOV) operate strictly under orbital mechanics laws (Kepler, Clohessy-Wiltshire) where altitude and inclination dictate energy, not aerodynamic endurance.",
        "related": ["10-orbital-guardian", "04-waverider-corvus", "16-rq81-diana"]
    },
    {
        "id": "32",
        "slug": "32-izzy-fried-c2",
        "domain": "C2",
        "name": "Izzy Fried & Fox2Sierra Joint Multi-Domain C2",
        "token": "C2: MB-HR-GW",
        "token_full": "C2: Multi-Domain Orchestration • C4 Operational Cloud & Tactical Edge • Distributed Cloud Compute & Battery Pack • Joint Operation Mission Commander & Target Handoff • Human-Machine Swarm Shield • Resilient Wideband MESH / Starlink / COFDM Gateway",
        "hal": "IMultiDomainSwarmOrchestration",
        "hal_def": "Operational command-and-control clouds require IMultiDomainSwarmOrchestration and IAlgorithmicTargetHandoff to synchronize heterogeneous robotic platforms (UAV air cover + UGV ground screen + USV naval picket) while enforcing human-in-the-loop lethal weapon fire authorization.",
        "vendor": "Fox2Sierra & Tactical Edge Command",
        "vendor_slug": "fox2sierra",
        "date": "2026-11-06",
        "source_name": "LinkedIn / Joint Autonomous Force Operation Analysis",
        "source_url": "https://lnkd.in/p/dMhG2277",
        "advantages": [
            "Cross-Domain Kill-Chain Compression: compresses sensor-to-shooter latency from 15-20 minutes to under 5 seconds across Air, Ground, and Naval robotic units.",
            "Dynamic Task Allocation: edge AI dynamically reassigns missions when individual drones are shot down or jammed, maintaining continuous perimeter defense.",
            "Human Commander Scalability: single human officer commands 50-100 heterogeneous autonomous vehicles through declarative high-level intent."
        ],
        "vulnerabilities": [
            "Network Disruption Susceptibility: catastrophic C4ISR collapse occurs if all wideband satellite and terrestrial MESH relays are simultaneously jammed.",
            "Algorithmic Exploitation: adversarial machine learning attacks (optical decoys, ghost targets) can saturate C2 target allocation queues.",
            "Bandwidth Chokepoints: real-time streaming of dozens of high-definition video feeds saturates tactical radio links in contested frontline sectors."
],
        "lesson": "Codifies the Ultimate UWE Synthesis: autonomous warfare supremacy is achieved not by individual platforms, but by the software-defined C2 cloud binding heterogeneous robotic domains into a unified algorithmic shield.",
        "related": ["13-fury-ghostbat", "17-frodo-ugv", "21-tactical-ucv-spectrum", "24-lurtz-kill-zone"]
    },
    {
        "id": "34",
        "slug": "34-regent-seaglider",
        "domain": "USV",
        "name": "REGENT Seaglider (Viceroy Tri-Modal WIG)",
        "token": "USV: LG-VB-AS",
        "token_full": "USV: Littoral Ground-Effect • High-Speed Glider Hull • Distributed Electric Vectoring • Maritime High-Speed Transport • Autonomous Coastal Infiltration • Satellite & Coastal AIS / Mesh",
        "hal": "ITriModalSeagliderTransitionDrive",
        "hal_def": "Tri-modal ground-effect seagliders require ITriModalSeagliderTransitionDrive to crossfade hydrodynamic foil lift to aerodynamic wing ground-effect lift, coordinating distributed propeller blown-flap angles to neutralize violent pitch trim divergence and prevent height instability during foil retraction at 100+ km/h.",
        "vendor": "REGENT Craft",
        "vendor_slug": "regent-craft",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / REGENT Craft",
        "source_url": "https://www.facebook.com/reel/1091309223663639",
        "advantages": [
            "Ground-Effect Induced Drag Halving: flying in close ground effect (h/c < 0.5) eliminates downwash and tip vortices, boosting cruise L/D > 22-25 and reaching 300 km/h on battery power.",
            "Hydrofoil R_hump Solution: deployable hydrofoils lift the hull cleanly at 30-75 km/h, slashing water drag by 70-80% and eliminating wave-slamming accelerations in Sea State 3.",
            "Distributed Electric Propulsion (DEP): 8-12 wing-mounted electric propellers blow directly across full-span flaps, preventing stall and providing robust low-speed control authority."
        ],
        "vulnerabilities": [
            "Center-of-Pressure Transition Shift: withdrawing hydrofoils transfers vehicle support from water struts to wings, triggering pitching moment divergence that requires microsecond blown-flap torque arbitration.",
            "Ground Effect Pitch-Height Coupling: aerodynamic pitch instability close to water demands continuous (>100 Hz) radar/lidar surface-tracking to prevent porpoising.",
            "Saline Corrosion & Cavitation: operating distributed nacelles in high-velocity sea spray accelerates leading-edge erosion, demanding hermetic IP68 motor sealing."
        ],
        "lesson": "Regulatory & Physical Decoupling: classifying high-speed coastal transit under maritime WIG standards (IMO MSC/Circ.1054) rather than FAA aviation codes bypasses airport infrastructure, while tri-modal hydrofoil-WIG physics conquers the hydrodynamic power barrier.",
        "related": ["06-exail-usv", "28-south-china-reef", "30-philippine-carrier"]
    },
    {
        "id": "35",
        "slug": "35-hopaero-rook",
        "domain": "UAV",
        "name": "Hop Aero ROOK (Container-Launched Hypersonic Cargo Rocket)",
        "token": "UAV: HC-CR-AS",
        "token_full": "UAV: Hypersonic Suborbital Trajectory • Containerized Vertical-Launch Airframe • Chemical Rocket Engine • Tactical High-Priority Cargo Delivery • Autonomous Terminal Decoupling • Satellite & Terrain-Relative Guidance",
        "hal": "ISuborbitalVtvlCargoDrive",
        "hal_def": "Autonomous containerized suborbital cargo rockets require ISuborbitalVtvlCargoDrive to coordinate supersonic aerodynamic re-entry deceleration and deep-throttling gimbaled thrust vectoring in real time, executing terrain-relative navigation for zero-runway touchdown on unprepared ground within CEP < 5 meters.",
        "vendor": "Hop Aero",
        "vendor_slug": "hop-aero",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / Hop Aero",
        "source_url": "https://www.facebook.com/reel/972173385834214",
        "advantages": [
            "Containerized Decoupled Infrastructure (C4 to C3): packaging launch rail and erection hydraulics into a 40-ft ISO container decouples rocket operations from spaceports and runways, turning container ships or clearings into instant launchpads.",
            "Compressed Temporal Attrition: 750 km delivery in 900 seconds compresses operational latency from hours to minutes, bypassing maritime blockades, A2/AD bubbles, and ground choke points.",
            "Decoupled Payload Integration: modular 250 kg payload bay supports rapid swapping between medical resupply, loitering munition dispenser cartridges, or EW packages without propulsion redesign."
        ],
        "vulnerabilities": [
            "The Hoverslam Throttling Trap: liquid rocket engines have hard lower throttle limits (30-40%); in a nearly dry vehicle, minimum thrust exceeds landing weight, forcing a millisecond suicide burn with zero hover margin.",
            "Rocket Plume Excavation: impinging a multi-ton supersonic rocket plume (>2500 m/s, >2500°C) onto raw dirt or sand blasts craters and debris back into the engine bell and TVC actuators.",
            "Strategic Early-Warning Ambiguity: high-altitude suborbital ballistic arcs emit massive infrared plumes identical to IRBMs, risking false alarms in early-warning constellations."
        ],
        "lesson": "Law 2 Microcosm & Terminal Physics: military rocket logistics succeed only when freed from C4 strategic bases into standard C3 intermodal logistics, though terminal landing physics dictates survivability.",
        "related": ["04-waverider-corvus", "10-orbital-guardian", "31-spm-kondratyuk"]
    },
    {
        "id": "36",
        "slug": "36-avidrone-tandem",
        "domain": "UCV",
        "name": "Avidrone Aerospace Tandem-Rotor Cargo UCV (740T & 210TL)",
        "token": "UCV: TL-TH-MS",
        "token_full": "UCV: Tactical Tandem-Rotor Disc • Heavy Logistics Airframe • Turboshaft Heavy-Fuel Engine • Heavy Tactical Cargo Resupply • Semi-Autonomous Mission Flight • MESH & Satellite Command Link",
        "hal": "ITandemRotorDynamics",
        "hal_def": "Autonomous tandem-rotor copter systems require ITandemRotorDynamics to continuously arbitrate differential collective pitch across counter-rotating rotor discs, compensating for rapid center-of-gravity shifts during autonomous pickup and release of 227-kg tactical payloads on unprepared forward terrain.",
        "vendor": "Avidrone Aerospace",
        "vendor_slug": "avidrone-aerospace",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / Defense Advancement",
        "source_url": "https://www.facebook.com/reel/3237345289784878",
        "advantages": [
            "100% Useful Lift Power Conversion: counter-rotating tandem rotors cancel net torque aerodynamically, eliminating the tail rotor that wastes 12-15% of engine shaft power.",
            "Lower Disc Loading vs Multirotors: two large-diameter rotor discs drastically reduce induced power losses vs multirotor propellers, delivering the hover efficiency needed to lift 227 kg payloads.",
            "Longitudinal Center-of-Gravity Invariance: shifting sling loads or sloshing liquid cargo is trimmed via differential collective pitch between rotors rather than parasite trim tabs.",
            "Heavy Fuel Frontline Logistics: the 740T gas turbine operates on standard battlefield Jet A / JP-8 / Diesel, eliminating forward battery charging bottlenecks."
        ],
        "vulnerabilities": [
            "Mechanical Complexity & Maintenance: dual swashplates, collective pushrods, synchronization cross-shafting, and gearboxes introduce mechanical wear points in dusty frontline conditions.",
            "Rotor Wake Intermeshing Vibrations: forward flight pushes front rotor wake into the rear disc, creating periodic aerodynamic interference and dynamic blade stress."
        ],
        "lesson": "Kinematic Primacy of Rotorcraft in UCV: confirms that vertical lift platforms governed by disc loading belong strictly to UCV; when cargo exceeds 50-200 kg, multirotors fail due to induced power scaling, mandating large disc-loaded rotorcraft.",
        "related": ["09-capstone-coaxial", "15-tekever-ar6", "21-tactical-ucv-spectrum"]
    },
    {
        "id": "37",
        "slug": "37-oshen-cstar",
        "domain": "USV",
        "name": "Oshen C-Star PC13 (Micro-USV Transatlantic Wingsail)",
        "token": "USV: SW-MS-IS",
        "token_full": "USV: Surface Wave Boundary • Micro-Scale Wingsail Hull • Wind Propulsion & Solar Buffer • Persistent Ocean Sensor Picket • Persistent Autonomous Station-Keeping • Satellite Iridium IoT & AIS Link",
        "hal": "IAutonomousWingsailNavigation",
        "hal_def": "Autonomous micro-wingsail surface vessels mandate IAutonomousWingsailNavigation to dynamically coordinate rigid wingsail angle-of-attack and rudder deflection against local wind polars, enabling perpetual wind-propelled ocean transit and virtual-tether station-holding across extreme sea states with zero fuel expenditure.",
        "vendor": "Oshen Ltd",
        "vendor_slug": "oshen-ltd",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / Interesting Engineering",
        "source_url": "https://www.facebook.com/reel/1459370292730982",
        "advantages": [
            "Zero Wave-Bending Damage (L^3 Scale Invariance): at 1.3m length and 56 kg mass, structural bending moments under cresting waves are virtually negligible, riding 9-meter breaking swells where large displacement ships suffer fatigue.",
            "Decoupled Kinetic vs Electrical Energy Harvesting: wind thrust powers infinite hydrodynamic propulsion, while a 52.5W solar array independently charges a 100Ah battery for compute and telemetry.",
            "Persistent Low-Cost Maritime Picketing: acts as an ultra-low-cost, distributed acoustic and meteorological ocean sentry, bridging latency gaps between satellite passes and providing gateway relays for subsurface UUVs."
        ],
        "vulnerabilities": [
            "Low Tactical Velocity (1.2-1.5 kts): speed is strictly bounded by ambient trade winds; incapable of tactical sprint, rapid evasive maneuvers, or fast intercept missions.",
            "Severe Marine Biofouling: multi-month deployments (127 days) allow barnacles and algae to foul hydrodynamic hull surfaces and submerged acoustic sensor faces.",
            "Commercial Shipping Collision Hazard: ultra-low radar cross-section renders the micro-hull invisible to commercial ship radars without continuous active AIS transponders."
        ],
        "lesson": "Micro-Scale Hydrodynamic Invariance in USV: validates the C0 tier within the USV continuum; micro-wingsail vessels provide sovereign distributed oceanic endurance (>100 days), proving extreme miniaturization defeats open-ocean attrition at near-zero unit cost.",
        "related": ["06-exail-usv", "28-south-china-reef", "30-philippine-carrier"]
    },
    {
        "id": "38",
        "slug": "38-preneu-tactical",
        "domain": "UAV",
        "name": "PRENEU Tactical UAS (MILVUS T400 Lift+Cruise & PANDION Q1200)",
        "token": "UAV: AL-EB-MS",
        "token_full": "UAV: Atmospheric Low-Altitude • Lift+Cruise Hybrid Airframe • Electric Battery Storage • Tactical ISR & Forward Screening • Autonomous Mission Autopilot • Encrypted Tactical MESH & Satellite Link",
        "hal": "IVtolTransitionDrive",
        "hal_def": "Lift+Cruise tactical UAS architectures require IVtolTransitionDrive to arbitrate progressive aerodynamic handoff between vertical-lift quad rotors and fixed-wing pusher propulsion across the stall transition envelope, preventing roll-yaw cross-coupling during wing loading.",
        "vendor": "PRENEU",
        "vendor_slug": "preneu",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / Defense Advancement",
        "source_url": "https://www.facebook.com/reel/2008703892980995",
        "advantages": [
            "Decoupled Lift+Cruise Transition Safety: quad vertical-lift rotors isolate hover lift from horizontal cruise pusher propulsion, eliminating tiltrotor mechanical swashplate/nacelle failure modes.",
            "High Aspect Ratio Battery Endurance: 4.15m fixed-wing airframe delivers 180 min (3 h) loiter endurance and 50+ km operational radius on pure chemical battery storage.",
            "Closed-Loop Ballistic Drop Compensation: dedicated ultrasonic wind sensor feeds dynamic crossflow drift into the flight controller, achieving <5m CEP from 150m AGL without dive maneuvers."
        ],
        "vulnerabilities": [
            "Parasitic Lift-Boom Drag Tax: in horizontal cruise, the 4 inactive vertical motors and carbon boom structures generate a 15-20% parasitic drag penalty, restricting cruise velocity.",
            "Chemical Storage Payload Bottleneck: with a 9 kg battery pack on a 25 kg MTOW, the 1.5 kg payload strictly bounds sensor optics to lightweight gimbals.",
            "Hover Exposure of Strike Multirotor: hovering at 150m AGL for 30+ seconds to stabilize wind-compensated drops exposes the multirotor to acoustic detection and small-arms fire."
        ],
        "lesson": "Law of Decoupled Lethality across Heterogeneous Teams: pairing high-efficiency aerodynamic lift (UAV: AL-EB-MS) for persistent ISR screening with compact disc-loaded rotorcraft (UCV: CQ-EB-DR) for kinetic delivery outperforms all-in-one compromises.",
        "related": ["01-honda-evtol", "13-fury-ghostbat", "19-petrel-aero-sky"]
    },
    {
        "id": "39",
        "slug": "39-airbus-flexrotor",
        "domain": "UAV",
        "name": "Airbus Flexrotor (Aerovel Tailsitter VTOL)",
        "token": "UAV: AL-IC-SL",
        "token_full": "UAV: Atmospheric Low-Altitude • Tailsitter VTOL Fixed-Wing Airframe • Internal Combustion Heavy Fuel Engine • Expeditionary Tactical ISR & Screening • Autonomous Transition & Flight Control • Line-of-Sight & Satellite Comms",
        "hal": "ITailsitterTransitionDynamics",
        "hal_def": "Tailsitter VTOL UAS architectures mandate ITailsitterTransitionDynamics to seamlessly arbitrate the continuous 90-degree pitch transition by blending proprotor cyclic pitch with wing elevon aerodynamic deflections, actively decoupling gyroscopic precession moments across the stall boundary.",
        "vendor": "Airbus & Aerovel",
        "vendor_slug": "airbus-aerovel",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / Defense Advancement",
        "source_url": "https://www.facebook.com/reel/1495653508676587",
        "advantages": [
            "Zero Parasite Boom Drag Tax: unlike Lift+Cruise craft carrying inactive lift motors, the tailsitter utilizes 100% of its single 2.2m proprotor for hover and cruise, achieving clean glide efficiency (L/D > 16).",
            "Hydrocarbon Energy Density: powered by a 28cc two-stroke engine running on heavy fuel or gasoline, the 25-kg airframe achieves 12 to 15 hours standard endurance and up to 32+ hours world-record loiter.",
            "Exceptional Useful Payload Fraction (32% of MTOW): lifts up to 8 kg of stabilized EO/IR gimbal, EW, or radar sensors on a 25 kg airframe.",
            "Expeditionary Runway-Independence: vertical launch and recovery directly from a 3.7x3.7m footprint eliminates catapults or nets, allowing operations from small naval vessels and austere posts."
        ],
        "vulnerabilities": [
            "Hover Wing Sail Effect: standing vertically on its tail, the 3.0-meter fixed wing acts as a sail in crosswinds, demanding high cyclic pitch authority and active elevon trim in propwash.",
            "Gyroscopic Precession in Transition: rapidly pitching the spinning 2.2m proprotor through 90 degrees generates cross-axis gyroscopic yaw torque that flight computers must decouple.",
            "Vibrational Stress on Geared Swashplate: single two-stroke cylinder torque pulses impose high vibrational loads on proprotor gearbox and cyclic pitch swashplates."
        ],
        "lesson": "The Tailsitter Aerodynamic Frontier: single-proprotor tailsitters powered by internal combustion radically outperform electric Lift+Cruise multi-motor platforms by eliminating dead-weight boom drag, governed by software-defined transition HALs.",
        "related": ["01-honda-evtol", "18-vantage-tacitframe", "20-tusas-aksungur"]
    },
    {
        "id": "40",
        "slug": "40-solaris-one",
        "domain": "UOV",
        "name": "Solaris One (Titan-Scale GEO Surveillance Satellite Benchmark)",
        "token": "UOV: GS-SL-MD",
        "token_full": "UOV: Geostationary Orbit (35,786 km) • Strategic Structural Platform • Solar Photovoltaic & Electric Propulsion • Hemispheric Optical & RF Surveillance • Autonomous Multi-Aperture Coordination • Deep-Space Laser Inter-Satellite Gateway",
        "hal": "ISparseApertureInterferometryDrive",
        "hal_def": "Geostationary strategic orbital surveillance architectures mandate ISparseApertureInterferometryDrive to synthesize multi-aperture optical wavefronts across distributed structural segments, enabling coherent image reconstruction while compensating for inter-segment optical path differences.",
        "vendor": "World Titan Forces Research",
        "vendor_slug": "world-titan-forces",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / World Titan Forces",
        "source_url": "https://www.facebook.com/reel/1085319637452189",
        "advantages": [
            "Continuous Hemispheric Persistence: orbiting at GEO (35,786 km), a single platform maintains uninterrupted optical and RF line-of-sight across ~42% of the globe, eliminating handover latency.",
            "Diffraction-Limited Aperture Thresholds: under the Rayleigh criterion, an effective aperture of D ~21.8m yields 1.0m ground resolution, while D ~436m provides 0.05m tactical resolution."
        ],
        "vulnerabilities": [
            "Structural Impossibility of Monolithic 20 km Disc: differential gravity gradient torques across a 20-km monolithic disc and severe thermal expansion gradients destroy optical diffraction coherence.",
            "Solar Radiation Pressure Torques: a 20-km disc catches over 1.4 kN of continuous solar radiation pressure, overwhelming traditional reaction wheels and thrusters.",
            "Prohibitive Delta-V for Maneuvering: relocating or re-inclining an ultra-massive structure incurs astronomical propellant mass ratios, leaving the megastructure an unmaneuverable target for ASAT effectors."
        ],
        "lesson": "Kondratyuk SPM Paradigm vs Monolithic CGI: monolithic orbital megastructures are an engineering and survivability dead end; resilient strategic surveillance demands a distributed sparse-aperture array of synchronized, disaggregated nodes across GEO, MEO, and LEO.",
        "related": ["10-orbital-guardian", "31-spm-kondratyuk"]
    },
    {
        "id": "41",
        "slug": "41-chaklun-uav",
        "domain": "UAV",
        "name": "Chaklun (Tactical Reconnaissance Fixed-Wing UAS)",
        "token": "UAV: AH-EB-AR",
        "token_full": "UAV: Atmospheric Low-Altitude • Hand-Launched EPP Flying Wing Airframe • Electric Battery Storage • Tactical Forward Reconnaissance • Autonomous Radio-Silent Dead-Reckoning • Autonomous Optical Navigation & RF Silence",
        "hal": "IRadioSilentDeadReckoningNav",
        "hal_def": "Tactical reconnaissance fixed-wing UAS operating under complete GNSS and RF datalink denial mandate IRadioSilentDeadReckoningNav to maintain 3D trajectory tracking and autonomous return-to-base via Pitot-static airspeed and 6-DoF inertial sensor fusion without emitting radio-frequency signatures.",
        "vendor": "Chaklun Aviation Frontline Cluster",
        "vendor_slug": "chaklun-aviation",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / Defense Advancement & Ukraine Defense Portal",
        "source_url": "https://www.facebook.com/reel/2318493582236910",
        "advantages": [
            "Ultra-Low Radar Cross Section (RCS): monolithic expanded polypropylene (EPP) construction with minimal metallic internal structure yields exceptionally low radar signature, evading tactical air defenses at operational altitudes.",
            "Zero Logistics Footprint: hand-launch capability eliminates catapults or cleared runways; belly landing on unpaved ground eliminates nets and parachutes, enabling instantaneous frontline redeployment.",
            "Aerodynamic Glide Efficiency: fixed-wing high-wing pusher architecture achieves 60-120 min endurance and 50-100+ km operational mission routes on battery power alone."
        ],
        "vulnerabilities": [
            "Dead-Reckoning Wind Drift Accumulation: long-duration flight under GNSS denial accumulates position drift from unmeasured crosswind gusts, requiring periodic optical flow corrections.",
            "Belly Landing Abrasion: repeated landings on frozen soil, gravel, or asphalt degrade the lower EPP fuselage skin and camera ports.",
            "Lightweight Sensor Limitations: compact backpack footprint limits payload to micro-gimbals or fixed cameras, relying on airframe banking for off-axis coverage."
        ],
        "lesson": "The Attrition-Resistant Tactical Scout Archetype: in dense EW environments, survivability does not stem from complex frequency-hopping alone, but from the physical ability to cut all transmissions, navigate purely on onboard physics-based sensor fusion, and absorb physical punishment.",
        "related": ["16-rq81-diana", "18-vantage-tacitframe", "26-kashmir-sentinel"]
    },
    {
        "id": "42",
        "slug": "42-intelligent-energy-soar",
        "domain": "UAV",
        "name": "Intelligent Energy IE-SOAR (Hydrogen Fuel Cell UAV Systems)",
        "token": "UAV: AL-HL-DR",
        "token_full": "UAV: Atmospheric Low-Altitude • Fixed-Wing / Multirotor Airframe • Hydrogen Fuel Cell Hybrid Powerplant • Long-Endurance Tactical Standoff ISR • Autonomous Powerpath Arbitration • Line-of-Sight & Direct Radio Datalink",
        "hal": "IPemFuelCellHybridDrive",
        "hal_def": "Lightweight hydrogen fuel cell hybrid UAV powerplants mandate IPemFuelCellHybridDrive to dynamically arbitrate microsecond transient power sharing between steady-state PEM fuel cell stack and high-C-rate lithium buffer batteries, preventing cathode starvation during peak VTOL and gust loads while regulating airflow stoichiometry.",
        "vendor": "Intelligent Energy",
        "vendor_slug": "intelligent-energy",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / Defense Advancement",
        "source_url": "https://www.facebook.com/reel/1033114216185690",
        "advantages": [
            "Gravimetric Energy Density Multiplier (700-1000 Wh/kg): integrated PEM stack with 350-bar carbon cylinder yields 3-4x usable specific energy of lithium batteries, extending multirotor hover to 2-3+ hours and fixed-wing loiter to 8-15+ hours.",
            "Rapid Operational Turnaround (< 3 min): swapping or quick-filling the 350-bar cylinder takes under 3 minutes, eliminating 60-120 minute forward battery charging downtime.",
            "Acoustic & Thermal Stealth Invariance: near-silent electric motors with warm water vapor exhaust (55-65°C) rather than 400-600°C ICE exhaust, drastically degrading detection by IRST and MANPADS thermal seekers."
        ],
        "vulnerabilities": [
            "Low Volumetric Energy Density & Parasite Drag: gaseous hydrogen at 350 bar has low density (~24 g/L); storing adequate fuel mass requires bulky cylinders that expand fuselage diameter and parasite drag.",
            "Transient Response Throttle Lag: PEM fuel cells cannot match millisecond transient spikes (up to 8 kW) demanded by VTOL transitions or gust stabilization, making a lithium buffer pack strictly mandatory.",
            "Frontline H2 Supply Chain Bottleneck: ultra-pure hydrogen (Grade 5.0, 99.999%) compressed to 350-500 bar is entirely absent from frontline tactical logistics, requiring dedicated base infrastructure."
        ],
        "lesson": "The Standoff C4ISR Niche vs Zero-Line Attrition: hydrogen fuel cells deliver unmatched silent endurance for standoff C4ISR orbits and maritime pickets, but the logistical burden of 350-bar hydrogen leaves lithium batteries and heavy-fuel ICE generators as the primary frontline tactical powerpaths.",
        "related": ["01-honda-evtol", "16-rq81-diana", "20-tusas-aksungur"]
    },
    {
        "id": "43",
        "slug": "43-avilus-grille",
        "domain": "UCV",
        "name": "Avilus Grille (Heavy-Lift Autonomous MEDEVAC eVTOL)",
        "token": "UCV: CL-EB-DR",
        "token_full": "UCV: Coaxial Heavy-Lift Multirotor • Heavy Airframe / Stretcher Capsule • Electric Battery Storage • Autonomous Combat CASEVAC & Extraction • Autonomous Flight & Attitude Clamping • Encrypted Direct Radio Datalink",
        "hal": "ICoaxialRotorFailureTolerantDynamics",
        "hal_def": "Heavy-lift autonomous medical evacuation rotorcraft mandate ICoaxialRotorFailureTolerantDynamics and IAutonomousCasEvacAttitudeControl to dynamically redistribute coaxial motor thrust during motor/ESC failures while enforcing physiological acceleration limits (G_z, G_y <= 1.2g) and attitude clamping to preserve casualty hemodynamics.",
        "vendor": "Avilus GmbH",
        "vendor_slug": "avilus-gmbh",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / Defense Advancement",
        "source_url": "https://www.facebook.com/reel/1812626446539196",
        "advantages": [
            "Zero-Risk Battlefield Extraction in the Golden Hour: eliminates human flight crew risk in hostile low-altitude air defense bubbles; extracts wounded within the critical 60-minute window across minefields and severed ground lines.",
            "Coaxial Hexacopter Thrust Redundancy: 12 rotors configured in 6 coaxial pairs with independent inverters provide N-1 and N-2 failure tolerance, allowing safe recovery upon rotor or ESC failure.",
            "Enclosed Climate-Controlled Capsule with Biometric Telemetry: protects casualties from fragments, rotor downwash, and hypothermia while live biometric transmission enables pre-arrival triage by rear surgeons.",
            "Intermodal C3 ISO Container Logistics: disassembles to fit inside a standard 20-ft ISO container; two soldiers can assemble the drone tool-free in under 15 minutes."
        ],
        "vulnerabilities": [
            "Severe Battery Energy Density & Range Ceiling: pure battery storage limits operational radius to ~25 km outbound + ~25 km return and 20-45 min flight time at 750 kg MTOW.",
            "Acoustic & Radar Cross-Section Signature: 7.8-meter diameter rotorcraft with 12 spinning blades generates a massive acoustic footprint (audible from 2-3 km) and prominent radar micro-Doppler modulation.",
            "Downwash Hazards in Unprepared LZs: 750 kg MTOW on a high-disc-loading footprint generates intense downwash winds (>20 m/s), creating brownout conditions that blind sensors and endanger ground crews."
        ],
        "lesson": "The Autonomous CASEVAC Archetype & Disc Loading Limits: validates replacing crewed helicopters with attritable heavy-lift rotorcraft for tactical evacuation, but exposes the limits of lithium chemistry; scaling medevac beyond 25 km demands hybrid turbogenerators or fixed wings.",
        "related": ["09-capstone-coaxial", "15-tekever-ar6", "21-tactical-ucv-spectrum"]
    },
    {
        "id": "44",
        "slug": "44-ziyan-greywhale-g1",
        "domain": "UCV",
        "name": "ZIYAN Grey Whale G1 (Modular Heavy-Load Cargo Unmanned Helicopter)",
        "token": "UCV: HL-EB-DR",
        "token_full": "UCV: Single-Rotor Helicopter Disc • Heavy Cargo Fuselage • Electric Battery Storage • Autonomous Standoff Winch Resupply • Autonomous Pendulum-Damped Flight • Encrypted Direct Radio Datalink",
        "hal": "IAutonomousCargoWinchDrive",
        "hal_def": "Tactical unmanned cargo helicopters deploying slung loads require IAutonomousCargoWinchDrive and IHelicopterRotorDynamics to feed forward cable pendulum oscillation vectors into cyclic swashplate trim, active-damping swinging loads during 6,000m high-altitude hover while autonomously managing crosswind yaw compensation.",
        "vendor": "ZIYAN Technology",
        "vendor_slug": "ziyan-technology",
        "date": "2026-11-16",
        "source_name": "Facebook Reel / ZIYAN Technology",
        "source_url": "https://www.facebook.com/reel/1773414080378754",
        "advantages": [
            "Aerodynamic Figure of Merit (FM >= 0.72): single 2.18m 4-blade rotor disc generates drastically lower disc loading (~12 kg/m^2) than multirotors, lifting 15-21 kg payloads on battery power.",
            "High-Altitude Mountain Envelope (6,000 m Ceiling): high blade area ratio and variable collective pitch maintain air density lift at extreme altitudes where fixed-pitch multirotors stall.",
            "Modular C2 Logistics Footprint: tool-free quick-release rotor blades, detachable tail boom, and folding gear collapse airframe into an ultra-compact package for pickup transport and 10-minute field assembly.",
            "Precision Standoff Winch Delivery: automated winch hoist delivers supplies directly to jagged mountain terrain, tree canopies, or trenches without landing."
        ],
        "vulnerabilities": [
            "Mechanical Single Points of Failure: swashplate linkages, cyclic pitch bearings, reduction gearing, and tail rotor drive shaft introduce mechanical wear with zero redundancy.",
            "Tail Rotor Power Tax & Obstacle Risk: tail rotor expends 10-15% of battery power purely on anti-torque counteraction and is vulnerable to brush or ground strikes during low hover.",
            "Battery Operational Radius (~20 km): 13 kg lithium battery pack restricts full-load radius to ~20 km, requiring frequent battery swapping in forward logistics loops."
        ],
        "lesson": "Kinematic Primacy of Single-Rotor Helicopters in Tactical Logistics: for vertical cargo lift between 15-50 kg in high-altitude mountain environments, single-rotor variable-pitch helicopters dramatically outperform multirotors in aerodynamic efficiency and ceiling.",
        "related": ["09-capstone-coaxial", "15-tekever-ar6", "36-avidrone-tandem"]
    },
    {
        "id": "45",
        "slug": "45-tencore-mat1lda",
        "domain": "UGV",
        "name": "TENCORE MAT1LDA 8x8 & TerMIT 2.0 (Amphibious Carrier & Combat UGV)",
        "token": "UGV: GM-IT-AR",
        "token_full": "UGV: Terrestrial & Water Amphibious • Medium 8x8 Armored Hull • Internal Combustion Petrol Engine • Tactical Robotic Carrier / Minelaying • Autonomous Route Autopilot • Anti-Jam Radio & MESH Gateway",
        "hal": "IAmphibiousTransitionDrive",
        "hal_def": "Amphibious robotic mother-carriers require IAmphibiousTransitionDrive and IMotherChildDeploymentGateway to dynamically trim all-wheel 8x8 skid-steer torque against loss of ground normal force during water entry and muddy riverbank egress, while coordinating automated deck latching and roll-pitch stabilization during deployment of tracked combat effectors.",
        "vendor": "TENCORE",
        "vendor_slug": "tencore",
        "date": "2026-11-16",
        "source_name": "Facebook Post / Defender Media",
        "source_url": "https://www.facebook.com/DefenderMediaUA/posts/pfbid027psMxGoouoi9zz1qTHi8PeRkb8ncYocy1LerB4Z1xTbhAWh9ks4DuWWBpqNMo1ekl",
        "advantages": [
            "Decoupled Operational vs Tactical Energy: MAT1LDA uses an internal combustion engine to deliver high energy density and 160 km land / 50 km water range, while TerMIT 2.0 uses electric battery drive for silent, low-thermal assault and minelaying.",
            "Amphibious Riverine & Wetland Access: 8x8 all-wheel drive with sealed buoyancy hull and side pontoons allows crossing rivers, estuaries, and bogs where conventional UGVs sink or require combat engineering bridges.",
            "Mothership-Parasite Doctrine: transports tracked combat unit across contested water barriers without risking human crews, deploying TerMIT 2.0 directly onto enemy shores for assault or minelaying.",
            "AI Autopilot for EW Navigation: onboard AI cruise control with visual/inertial odometry enables TerMIT and MAT1LDA to complete mission routes even under total GPS and RF jamming."
        ],
        "vulnerabilities": [
            "Riverbank Egress Traction Collapse: buoyancy sharply reduces wheel downforce during water-to-mud transition, creating severe wheel slip and beaching hazards on steep clay banks.",
            "ICE Acoustic & Infrared Plume: petrol combustion engine generates significant acoustic noise and an exhaust thermal plume, exposing water crossings to thermal sensor detection and ATGM strikes.",
            "Skid-Steer Tire Scrub & Drive Train Stress: non-steered 8x8 layout induces massive lateral tire scrub and torque spikes on dry paved terrain."
        ],
        "lesson": "The Hierarchical Mother-Child Archetype in Unmanned Ground Warfare: single universal ground robots are a doctrinal failure; combining an amphibious carrier (UGV: GM-IT-AR) with a tracked strike parasite (UGV: GL-EC-DR) proves combined-arms robotic superiority requires layered hierarchies.",
        "related": ["02-slimak-ugv", "08-unex-artillery", "17-frodo-ugv"]
    },
    {
        "id": "46",
        "slug": "46-nodrics-mat1lda",
        "domain": "UGV",
        "name": "NODRICS MAT1LDA 8x8 (Amphibious Tactical Logistics & CASEVAC UGV)",
        "token": "UGV: GM-IL-AR",
        "token_full": "UGV: Terrestrial & Water Amphibious • Medium 8x8 Sealed Hull • Internal Combustion Petrol Engine • Frontline Amphibious Logistics & CASEVAC • Autonomous Waypoint Navigation • Encrypted Anti-Jam RF & MESH",
        "hal": "IAmphibiousLogisticsDrive",
        "hal_def": "Amphibious logistics and CASEVAC UGVs require IAmphibiousLogisticsDrive and ICasEvacStabilityController to crossfade 8x8 wheel torque into buoyancy during water-bank transitions, clamping pitch/roll shocks to preserve casualty hemodynamic stability.",
        "vendor": "NODRICS",
        "vendor_slug": "nodrics",
        "date": "2026-11-17",
        "source_name": "Facebook Reel / Mezha.net",
        "source_url": "https://www.facebook.com/reel/904767382590697",
        "advantages": [
            "Hydrocarbon Energy Density (12,000 Wh/kg vs 250 Wh/kg): petrol ICE eliminates battery exhaustion under severe water-drag resistance power, delivering 160 km land / 50 km water range without battery charging delays.",
            "8x8 Sealed Displacement Hull & Pontoons: all-wheel drive combined with side pontoon buoyancy enables swimming with 400 kg cargo across rivers, lakes, and marshes without pontoon bridges.",
            "Modular Payload Decoupling: open-frame chassis accepts quick-swap cargo containers for 500 kg ammunition/supplies or casualty evacuation litters for crossing water barriers within the Golden Hour.",
            "TENCORE AI KIT Autonomous Navigation: onboard visual-inertial odometry executes pre-planned routes and return-to-base maneuvers under total GNSS denial and wideband RF jamming."
        ],
        "vulnerabilities": [
            "Riverbank Egress Traction Deficit: water buoyancy severely reduces wheel normal downforce during water-to-mud transition, creating wheel slip and beaching risks on steep clay banks.",
            "ICE Acoustic & Thermal Signature: internal combustion engine produces acoustic noise and a hot exhaust plume (>200°C), elevating detection risks from thermal reconnaissance drones.",
            "Skid-Steer Drivetrain Scrubbing & Deck Jerk: non-steered 8x8 layout induces lateral tire scrub and abrupt yaw angular jerks that jeopardize wounded stabilization unless smoothed by HAL acceleration filtering."
        ],
        "lesson": "The Amphibious Logistics-Energy Paradigm: in contested riverine corridors, electric UGVs suffer range collapse due to water-drag resistance; liquid hydrocarbon powertrains remain mandatory for operational-depth amphibious logistics (>50 km water / 150+ km land).",
        "related": ["02-slimak-ugv", "08-unex-artillery", "45-tencore-mat1lda"]
    },
    {
        "id": "47",
        "slug": "47-navalgroup-ucuv",
        "domain": "UUV",
        "name": "Naval Group UCUV Combat Demonstrator (France DGA)",
        "token": "UUV: CB-RA-HQ",
        "token_full": "UUV: Continental Shelf (100-200m) • Large Displacement Submersible Hull • Rechargeable Electric Battery Storage • Anti-Submarine & Surface Torpedo Strike • Autonomous Acoustic Tracking & Target Attack • Acoustic Modem & Low-Probability Intercept RF",
        "hal": "ISubseaCombatTrimmingDrive",
        "hal_def": "Uncrewed Combat Underwater Vehicles require ISubseaCombatTrimmingDrive and IVariableBallastTrimController to crossfade control-surface hydrodynamics with high-rate variable ballast compensation upon kinetic weapon ejection, counteracting pitch transients while micro-throttling Steeris hotel loads to preserve multi-day acoustic stealth loiter.",
        "vendor": "Naval Group",
        "vendor_slug": "naval-group",
        "date": "2026-11-18",
        "source_name": "LinkedIn / Tim De Zitter",
        "source_url": "https://lnkd.in/p/dMKGwNFp",
        "advantages": [
            "Continental Shelf Mass Optimization: limiting maximum depth to 150m dramatically reduces hull wall thickness and pressure hull mass fraction vs 1000m+ pelagic drones, freeing internal volume and mass for weapon modules.",
            "Closed-Cycle Acoustic Stealth: pure electrical battery storage eliminates diesel snorting, heat plumes, and acoustic cavitation, sustaining continuous low-speed (3 kts) stealth loiter.",
            "Decoupled Combat Payload: open modular payload bay allows configuring the invariant 11.7m hull for anti-submarine strike (MU90 torpedoes), offensive sea denial (mine laying), or long-range ISR.",
            "Steeris Autonomous Edge Command: onboard mission autonomy executes acoustic signature classification and tactical maneuvers without vulnerable surface RF or tether links."
        ],
        "vulnerabilities": [
            "Weapon Ejection Buoyancy Transient: discharging a 300kg torpedo or mine salvo instantly generates positive buoyancy; without high-rate variable ballast flooding, the vehicle suffers pitch-up and surface broaching.",
            "Hotel Load Parasitic Drain: at 3 kts, propulsion power is low, but hotel loads (sonar processing, compute, pumps) consume 50%+ of energy, collapsing 10-day endurance if sensors run at full duty cycles.",
            "Hydrodynamic Drag Asymmetry: external weapon shutters or mine hatches introduce parasitic drag, shifting trim across speed variations."
        ],
        "lesson": "The Subsea Lethality-Displacement Envelope: autonomous subsea combat assets cannot be evaluated by commercial endurance metrics alone; weapon separation physics and hotel loads dictate actual combat radius, with continental shelf specialization optimizing littoral sea denial.",
        "related": ["07-ghostshark-auv", "11-lockheed-lamprey", "29-fitburg-sentinel"]
    },
    {
        "id": "48",
        "slug": "48-sentinel-corebreak",
        "domain": "UAV",
        "name": "Sentinel Corebreak (Directed-Energy Air Superiority Platform)",
        "token": "UAV: AL-TD-HR",
        "token_full": "UAV: Atmospheric Low-Altitude • High-Aspect Tactical Airframe • Turbofan / Heavy Generator Powerplant • Directed-Energy Tactical Interception • Autonomous Swarm Interceptor / Hunter • High-Bandwidth Resilient Tactical Datalink",
        "hal": "IDirectedEnergyAeroOpticsDrive",
        "hal_def": "Airborne directed-energy airframes require IDirectedEnergyAeroOpticsDrive and IThermalEnergyLoadManager to dynamically compensate for transonic aero-optical boundary layer wavefront distortion around rotating beam turrets while micro-regulating engine bleed-air and phase-change thermal sinks to dump megawatts of laser waste heat without violating drag envelopes.",
        "vendor": "US NextGen Airpower Research",
        "vendor_slug": "nextgen-airpower",
        "date": "2026-11-18",
        "source_name": "Facebook Reel / US NextGen Airpower",
        "source_url": "https://www.facebook.com/reel/1424523013068659",
        "advantages": [
            "Speed-of-Light Interception: zero time-of-flight at tactical ranges negates kinematic evasion of high-G hostile missiles and loitering munitions.",
            "VLO Profile Preservation: replacing external/bay kinetic missile racks with internal fiber laser emitters maintains an uncompromised radar cross-section without weapons-bay radar blooming."
        ],
        "vulnerabilities": [
            "Thermal Saturation & Reload Physics: 30-35% electrical efficiency for a 150 kW beam dumps ~300 kW waste heat; once phase-change material heat sinks saturate, weapons cease firing until regeneration completes.",
            "Transonic Aero-Optics Jitter: protruding rotating turrets create supersonic shock waves and turbulent boundary layers, inducing Optical Path Difference aberrations that degrade focal intensity.",
            "Radiator Parasitic Drag: deploying external heat exchangers or ram-air scoops imposes severe parasitic drag spikes, degrading cruise speed and combat radius."
        ],
        "lesson": "The Thermodynamic-Optic Interdiction Limit: directed energy weapons eliminate ammunition logistics mass but transfer physical constraints entirely into thermodynamics and aero-optics; combat persistence is strictly bounded by waste heat dissipation and wavefront correction.",
        "related": ["03-stealth-ucav", "13-fury-ghostbat", "23-lpp-jwi4000"]
    },
    {
        "id": "49",
        "slug": "49-xq45-fibertailor",
        "domain": "UAV",
        "name": "XQ-45 Fibertailor & French Valkyrie (Dassault Rafale F5 UCAV Benchmark)",
        "token": "UAV: AL-TK-WR",
        "token_full": "UAV: Atmospheric Low-Altitude • Tailless Supersonic Stealth Airframe • Turbofan Jet Engine • Kinetic Strike & SEAD / DEAD • Wingman Manned-Unmanned Teaming • Wideband Resilient Tactical MESH Link",
        "hal": "IAeroelasticLoadLimiter",
        "hal_def": "Autonomous supersonic CCAs require IAeroelasticLoadLimiter and ILoyalWingmanFormationDrive to clamp control deflections against catastrophic wing root bending moments during extreme G-transients, preserving Boyd Ps to prevent energy bleeding and stall during maneuvering.",
        "vendor": "Dassault Aviation & French Air Force",
        "vendor_slug": "dassault-aviation",
        "date": "2026-11-18",
        "source_name": "Facebook Reel / US NextGen Airpower",
        "source_url": "https://www.facebook.com/reel/4065861937048538",
        "advantages": [
            "Omitting the Biological Envelope: removing cockpit and life support saves 1.5-2.0 tons empty mass for fuel and sensors, unlocking agile maneuvers free from human G-LOC (~9G).",
            "French Sovereign CCA Benchmark: France officially launched its sovereign loyal wingman program for Rafale F5, inheriting nEUROn stealth flight heritage for A2/AD penetration, SEAD/DEAD, and nuclear strike escort."
        ],
        "vulnerabilities": [
            "The 15-G Induced Drag Collapse: pulling 15-G demands high C_L, causing induced drag to spike quadratically (C_Di ~ C_L^2 ~ 225) and plunging specific excess power negative, bleeding Mach 1.4 into a stall within seconds.",
            "15-G Wing Root Bending Structural Fracture: a 4-ton airframe pulling 15-G experiences a 60-ton normal load (600 kN); composite wings under 200 kg cannot withstand this bending moment, fracturing under interlaminar shear.",
            "Supersonic Fuel Mass Contradiction: a 1,500-mile range at Mach 1.4 requires a fuel mass fraction of >=50%, physically precluding ultra-light wing structures."
        ],
        "lesson": "The Energy-Maneuverability Boundary in Autonomous Air Combat: removing human physiology does not abolish aerodynamic energy conservation (P_s) or aeroelastic structural boundaries (M_b); France's doctrine wisely prioritizes survivability, stealth, and sensor fusion over unviable 15-G marketing claims.",
        "related": ["03-stealth-ucav", "05-sickle-wing", "13-fury-ghostbat"]
    },
    {
        "id": "50",
        "slug": "50-vyriy-slavic",
        "domain": "UCV",
        "name": "Vyriy SLAVIC (Tactical Reconnaissance Copter / Sovereign Mavic Alternative)",
        "token": "UCV: CB-ER-DR",
        "token_full": "UCV: Compact Quadrotor Multirotor • Backpack Tactical Airframe • Solid-State Electric Battery Pack • Tactical Forward Reconnaissance • Dead-Reckoning & Optical Odometry • Directional Encrypted Tactical RF Link",
        "hal": "IVisualInertialOdometryNav",
        "hal_def": "Tactical reconnaissance multirotors require IVisualInertialOdometryNav and ISolidStateBatteryManagement to sustain drift-free visual-inertial hover in GNSS-denied corridors while optimizing solid-state battery thermal discharge to break the 90-minute endurance barrier and protect crews from kill-zone counter-battery tracking.",
        "vendor": "Vyriy Industries Frontline Cluster",
        "vendor_slug": "vyriy-industries",
        "date": "2026-11-18",
        "source_name": "Facebook Reel / Гаряча Зона / Vyriy Industries",
        "source_url": "https://www.facebook.com/reel/2607037159801948",
        "advantages": [
            "Kill-Zone Expansion Standoff: 30 km radius and 90-120 min endurance allow crews to launch from 15-20 km behind the contact line, escaping the lethal forward kill-zone that endangered Mavic 3 pilots.",
            "Solid-State Chemistry (350-400 Wh/kg): 40,000 mAh pack yields 3x loiter duration of standard Li-Ion pouch cells, stable winter discharge, and puncture fire resilience.",
            "Anti-AeroScope Sovereign Security: eliminates DJI DroneID telemetry leakage, preventing pilot coordinate interception and post-crash flight-log extraction."
        ],
        "vulnerabilities": [
            "Logistics Footprint of Directional Tracker Mast: sustaining 30 km telemetry requires an elevated ground station with pan-tilt directional antennas, increasing deployment time and position profile.",
            "Visual-Inertial Odometry Night Drift: featureless terrain in zero-illumination nights or dense fog causes optical flow integration drift, requiring radio beacon triangulation to maintain station.",
            "Component Sourcing Dependencies: while frame, firmware, and controllers are sovereign, core motors and optical zoom sensors remain dependent on external supply chains."
        ],
        "lesson": "The Kill-Zone Standoff Principle: frontline tactical reconnaissance cannot rely on consumer toy metrics or unencrypted protocols; when the lethal envelope expands, tactical multirotors must transition from handheld toys to squad-level endurance tools powered by solid-state chemistry and optical odometry.",
        "related": ["09-capstone-coaxial", "21-tactical-ucv-spectrum", "41-chaklun-uav"]
    },
    {
        "id": "51",
        "slug": "51-canister-arrow",
        "domain": "UAV",
        "name": "Canister Arrow (Tube-Launched Micro-UAV)",
        "token": "UAV: AC-CE-AR",
        "token_full": "UAV: Atmospheric Low-Altitude • Canister Tube-Launched Folding Airframe • Cold-Gas Pneumatic & Electric Propulsion • Precision Loitering Strike Munition • Autonomous Launch Decoupling & Terminal Lock • Encrypted Anti-Jam Radio Link",
        "hal": "ITubeLaunchTransitionDrive",
        "hal_def": "Tube-launched canister micro-UAVs require ITubeLaunchTransitionDrive and IFoldingWingAerodynamicControl to orchestrate the sub-second transition from tube ejection to closed-loop aerodynamic control.",
        "vendor": "Energy Book Tactical Systems",
        "vendor_slug": "energy-book",
        "date": "2026-11-18",
        "source_name": "Facebook Reel / Energy Book",
        "source_url": "https://www.facebook.com/reel/1614862140287826",
        "advantages": [
            "Canister Rapid Ejection (5-10s Launch Readiness): eliminates prolonged frontline exposure of FPV crews, allowing deployment directly from trenches or armored vehicles.",
            "Fixed-Wing Aerodynamic Efficiency: fixed-wing glide breaks multirotor battery exhaustion, extending loiter time and strike radius.",
            "Protected Pusher Architecture: rear folding propeller protects blades during tube transit, leaving nose bay free for modular payloads."
        ],
        "vulnerabilities": [
            "Wing Deployment Dynamic Shock: requires microsecond mechanical latching upon tube exit; asymmetrical wing lock triggers instant aerodynamic roll departure.",
            "Pusher Aeroacoustic BPF Signature: operating in the turbulent wake behind the cylindrical fuselage creates discrete acoustic harmonics.",
            "Payload Caliber Limit (50-60mm): hard geometric constraints limit shaped-charge jet diameter, restricting lethality primarily to unarmored targets."
        ],
        "lesson": "The Canister Deployment Invariant: frontline loitering strike platforms benefit exponentially from modular tube containerization, decoupling operator survival from launch setup time and replacing open-air multirotor vulnerability with instant pneumatic ejection.",
        "related": ["23-lpp-jwi4000", "25-stat-caylus-b2lt", "41-chaklun-uav"]
    },
    {
        "id": "52",
        "slug": "52-rovertech-zmiy",
        "domain": "UGV",
        "name": "RoverTech ZMIY Droid 12.7 (Combat UGV / Elevating RCWS)",
        "token": "UGV: GL-EC-DR",
        "token_full": "UGV: Terrestrial Ground Mud • Light 4x4 Armored Wheeled Chassis • Electric Battery Drive • Combat Heavy Machine Gun Fire Support • Defilade Pantograph Engagement • Digital Encrypted Direct Radio Datalink",
        "hal": "IElevatingWeaponStation",
        "hal_def": "Combat ground robotic platforms require IElevatingWeaponStation and ISkidSteerRecoilCompensator to coordinate pantograph elevation for defilade firing while crossfading wheel brake torques to absorb 12.7mm recoil without chassis pitching.",
        "vendor": "RoverTech Frontline Cluster",
        "vendor_slug": "rovertech",
        "date": "2026-11-18",
        "source_name": "Facebook Reel / Defense Advancement",
        "source_url": "https://www.facebook.com/reel/1614141370078662",
        "advantages": [
            "Defilade Pantograph Geometry: elevating mast keeps the armored chassis hidden behind trenches and berms, exposing only barrel and optics, cutting visual/radar cross-section by 70%.",
            "12.7x99mm Heavy Firepower: delivers up to 18 kJ muzzle energy for counter-material defeat through field fortifications at 1,500m standoff.",
            "AI Ballistic Auto-Tracking: Stronghold AI automated target acquisition eliminates human hand-tremor under combat stress."
        ],
        "vulnerabilities": [
            "Recoil Tipping Moments: burst-firing 12.7mm (.50 BMG) generates 35 N*s impulse; elevated pantograph creates high tipping leverage requiring dynamic wheel lock.",
            "Skid-Steer Tire Scrubbing: chevron lugs provide extreme mud bite but induce severe lateral scrubbing, consuming up to 45% power on hard-pack turns.",
            "Elevated Mast Vulnerability: raised sensor and gun assembly presents a high-priority vertical profile for hostile snipers and FPV counter-attacks."
        ],
        "lesson": "The Defilade Fire Superiority Law: static trench combat is lethal for manned crews; robotic weapon stations must exploit mechanical articulation (elevating pantographs) to achieve asymmetric defilade engagement, decoupling weapon line-of-sight from hull exposure.",
        "related": ["02-slimak-ugv", "14-knds-centurio", "17-frodo-ugv"]
    },
    {
        "id": "53",
        "slug": "53-nebesa-spaceplane",
        "domain": "UAV",
        "name": "Nebesa Aerospace NEBESA Suborbital Spaceplane",
        "token": "UAV: HD-LR-PS",
        "token_full": "UAV: High-Altitude Suborbital • Delta-Wing Spaceplane Airframe • Liquid Rocket & Airbreathing Turbojet Hybrid • Reconnaissance & Fast Re-Entry Interceptor • Pre-Planned Ballistic Orbit • Autonomous Inertial Space Tracking",
        "hal": "ISuborbitalTransitionDrive",
        "hal_def": "Horizontal-takeoff suborbital spaceplanes require ISuborbitalTransitionDrive and IBlendedReactionAerodynamicControl to orchestrate combined turbojet-to-rocket ascent and crossfade elevons with reaction thrusters at 110 km apogee.",
        "vendor": "Nebesa Aerospace",
        "vendor_slug": "nebesa-aerospace",
        "date": "2026-11-18",
        "source_name": "Militarnyi / Future Forces Forum 2026 Prague",
        "source_url": "https://militarnyi.com/uk/news/predstavyly-suborbitalny-bezpilotnyk-nebesa/",
        "advantages": [
            "Runway to Space Infrastructure Decoupling: replaces fixed vertical spaceports with standard 1,500-2,000 m paved runways or highways, dispersing suborbital operations across standard military and civilian airfields.",
            "Dual-Regime Combined Propulsion: airbreathing turbojet climb to 10-12 km saves up to 35% oxidizer mass; 9 kN 3D-printed liquid rocket engine ignites in rarefied atmosphere, achieving optimal specific impulse.",
            "Suborbital Reconnaissance Standoff: 110 km apogee and Mach 3.5 velocity exceed kinematic engagement ceilings of theater air-defense systems, ensuring survivable high-altitude observation."
        ],
        "vulnerabilities": [
            "Dynamic Pressure Collapse (q -> 0): in the 100-110 km exo-atmospheric apex, aerodynamic elevons lose control authority; stabilization relies strictly on reaction control thrusters or reaction wheels.",
            "Aerothermodynamic Heat Loads at Mach 3.5+: re-entry shock stagnation temperatures exceed 500-700°C on wing leading edges and nosecone, requiring specialized titanium/carbon-carbon thermal barrier composites.",
            "Airspace Deconfliction: high vertical climb and dive rates punch through civil flight corridors, mandating real-time C4ISR coordination to prevent mid-air hazards."
        ],
        "lesson": "The Suborbital Runway-Decoupling Law: decoupling exo-atmospheric access from multibillion-dollar vertical launch infrastructure through winged horizontal ascent transforms suborbital flight into an agile, survivable tactical asset.",
        "related": ["04-waverider-corvus", "05-sickle-wing", "35-hopaero-rook"]
    },
    {
        "id": "54",
        "slug": "54-skyx-flyingfish",
        "domain": "UAV",
        "name": "Changsha Nighthawk SkyX Triphibious Bionic Flying Fish Drone",
        "token": "UAV: AC-LE-SR",
        "token_full": "UAV: Atmospheric Low-Altitude • Convertible Triphibious Biomimetic Airframe • Liquid/Electric Dual-Regime Power • Subsea Loiter & Fast Aerial Reconnaissance • Submerged Infiltration & Aerial Sprint • Acoustic / RF Dual-Medium Comms",
        "hal": "ITransMediumTransitionDrive",
        "hal_def": "Trans-medium triphibious robotic vehicles mandate ITransMediumTransitionDrive and IBiomimeticMorphingWingControl to crossfade motor torque across the 800:1 water-air density ratio, lock morphing wings in 2.0s during surface breach, and compensate for water-shedding trim shifts.",
        "vendor": "Changsha Nighthawk Technology",
        "vendor_slug": "changsha-nighthawk",
        "date": "2026-11-18",
        "source_name": "Facebook Reel / CGTN Europe / Changsha Nighthawk",
        "source_url": "https://www.facebook.com/reel/1433213258697820",
        "advantages": [
            "800:1 Density Ratio Wing Morphing: folding wings flush against hydrodynamic fuselage slashes underwater drag, enabling 50 km/h subsea dash; 2.0s deployment restores full aerodynamic cruise in air.",
            "Triphibious Mission Continuity: bridges 3 domains with 60 min aerial flight (96 km/h), 30 min subsea loitering, and indefinite zero-power surface floating.",
            "Stealthy Submerged Sleeper Posture: lurking submerged beneath surface chop completely defeats airborne counter-UAS radars, thermal imaging pods, and visual tracking."
        ],
        "vulnerabilities": [
            "Water Breach Adhesion & Pitch Trim Shift: surface tension adhesion and water clingage add 10-15% deadweight during breach; wing lock delays exceeding 2.0s induce fatal aerodynamic stalls into the water.",
            "Subsurface RF Blackout & Inertial Drift: GHz radio frequencies attenuate to zero in seawater; submerged navigation relies on dead-reckoning which accumulates position errors without GNSS fixes.",
            "Rotary Wing Seal Degradation: articulated wing morphing hinges face cyclic hydrostatic pressure, marine biofouling, and abrasive sand, risking catastrophic short-circuits upon seal failure."
        ],
        "lesson": "The Cross-Medium Trans-Density Law: single invariant airframes cannot bridge the 800:1 water-air density ratio without mechanical shape transformation; triphibious supremacy requires active kinematic morphing and dedicated dual-regime propulsion.",
        "related": ["07-ghostshark-auv", "34-regent-seaglider", "37-oshen-cstar"]
    },
    {
        "id": "55",
        "slug": "55-bair-arkhan",
        "domain": "UGV",
        "name": "BAIR ARKHAN Autonomous Defense System (Mothership-Parasite Concept)",
        "token": "UGV: GT-DC-MR",
        "token_full": "UGV: Terrestrial Heavy Tracked • Armored Tracked Carrier / Base • Heavy Diesel Generator & Electric Drive • Multi-Domain Robotic Docking & Mother Base • Multi-Domain Heterogeneous Swarm Coordination • Encrypted Tactical MESH & Satellite Gateway",
        "hal": "IMothershipSwarmCarrier",
        "hal_def": "Integrated air-ground defense ecosystems require IMothershipSwarmCarrier and IHeterogeneousDockingManager to coordinate precision autonomous docking, automated battery hot-swapping or high-current charging, and distributed sensor fusion across heterogeneous carrier, quadrupedal, and aerial nodes in GNSS-denied environments.",
        "vendor": "BAIR MilTech Architecture",
        "vendor_slug": "bair-miltech",
        "date": "2026-11-18",
        "source_name": "Facebook Reel / BAIR MilTech",
        "source_url": "https://www.facebook.com/reel/1654555996099911",
        "advantages": [
            "Hierarchical Containerization (UWE Law 2): division into a protected heavy tracked mothership (C3) and attritable parasites (C1) protects generators and servers, moving light robots without depleting small batteries on march.",
            "Omnidirectional Tri-Domain Sensor Fusion: aerial drone provides high-altitude look-down C4ISR across 5-10 km; quadruped scouts blind corners and trenches; tracked carrier provides kinetic armor and long-range comms.",
            "Automated Force Multiplication: decouples human operators from the front line, transforming a single ground vehicle into an autonomous reconnaissance and perimeter interdiction hub."
        ],
        "vulnerabilities": [
            "Legged Robotics Energy Trap (CoT 1.5-3.0): quadruped robots burn excessive power maintaining balance even at standstill; operational radius rarely exceeds 3-5 km, making carrier battery recharge latency a critical bottleneck.",
            "Rotor Downwash Interference on Mobile Carrier: launching multirotors directly from carrier roof induces severe ground-effect turbulence and hull reflection, requiring mechanical guide cradles or magnetic locks.",
            "Open RF Jamming Vulnerability: unhardened 2.4/5.8 GHz communication links between carrier and parasites are easily severed under front-line EW, mandating optical tether or edge VIO/SLAM navigation."
        ],
        "lesson": "The Heterogeneous Carrier-Parasite Symbiosis Law: in attrition warfare, disparate kinematic nodes (tracks, legs, rotors) are viable only when bound into an integrated symbiosis where the heavy carrier absorbs logistical overhead, freeing lightweight edge nodes to execute specialized tactical actions.",
        "related": ["02-slimak-ugv", "14-knds-centurio", "45-tencore-mat1lda"]
    }
]

VENDORS_DATA = [
    {"slug": "anduril", "name": "Anduril Industries", "origin": "USA", "type": "OEM", "platforms": ["Anduril Fury (CCA)", "Ghost Shark XL-AUV", "ALTIUS Series"], "focus": "Autonomous defense-tech, Lattice OS, Collaborative Combat Aircraft, attritable robotic mass."},
    {"slug": "boeing", "name": "Boeing Defense, Space & Security", "origin": "USA / Australia", "type": "OEM", "platforms": ["MQ-25 Stingray CBARS", "MQ-28 Ghost Bat"], "focus": "Carrier-based unmanned aviation, aerial refueling infrastructure, modular CCA airframes."},
    {"slug": "lockheed-martin", "name": "Lockheed Martin (Skunk Works)", "origin": "USA", "type": "OEM", "platforms": ["Lamprey MMAUV", "U-2 / RQ-170 Heritage"], "focus": "Parasitic subsea autonomous systems, advanced stealth aerostructures, low-observable naval technologies."},
    {"slug": "exail", "name": "Exail Marine", "origin": "France", "type": "OEM", "platforms": ["DriX H-9 USV", "Oryx O-16 USV"], "focus": "Slender wave-piercing displacement unmanned surface vessels, drop-keel ASW hydrography, Sea State 5 endurance."},
    {"slug": "bae-falconworks", "name": "BAE Systems & Certo Aerospace", "origin": "UK", "type": "OEM", "platforms": ["CAPSTONE Coaxial Heavy-Lift UCV"], "focus": "Coaxial rotorcraft disc loading, 50% structural payload fraction, naval frigate deck operations."},
    {"slug": "unex", "name": "UNEX Automation", "origin": "Belgium / Ukraine", "type": "OEM", "platforms": ["ABRIS Amphibious Prime Mover"], "focus": "Heavy electric all-terrain logistics, robotic artillery towing, Bekker soil traction management."},
    {"slug": "honda", "name": "Honda Aircraft Company", "origin": "Japan / USA", "type": "OEM", "platforms": ["Honda eVTOL (GT-HEV)"], "focus": "Decoupled Lift+Cruise aerodynamics, gas turbine hybrid-electric powertrains, inter-city logistics."},
    {"slug": "frontline-ua", "name": "Ukrainian Frontline Defense-Tech & Robotics", "origin": "Ukraine", "type": "Frontline Cluster", "platforms": ["НРК SlimAk UGV", "НРК «Фродо» 6x6 UGV", "Buriya Stabilized Turret", "Black Sea USVs"], "focus": "Asymmetric robotic warfare, articulated mud-conforming chassis, 40 km/h kinetic evasion, multi-bearer C2, electronic warfare resilience."},
    {"slug": "knds", "name": "KNDS France & Germany", "origin": "France / Germany", "type": "OEM", "platforms": ["CENTURIO Tactical UGV", "PHOBOS Chassis", "ARX20/30 RWS"], "focus": "Tactical all-wheel-steer combat robotics, hydrostatic traction drives, high-recoil remote weapon stations, zero-line fiber-optic telemetry."},
    {"slug": "tekever", "name": "TEKEVER", "origin": "Portugal / UK", "type": "OEM", "platforms": ["AR6 Heavy-Lift UAS", "AR5 Life Ray", "AR4 Evolution"], "focus": "Fluid-power multirotors, digital displacement hydraulics, long-range maritime and tactical logistics UAS."},
    {"slug": "haps-consortium", "name": "Stratospheric Defense & HAPS Aerospace", "origin": "USA / International", "type": "Research Source", "platforms": ["'RQ-81 Diana' HAPS", "Solar Stratospheric Relays", "Laser Cross-Link Nodes"], "focus": "High-altitude pseudo-satellites (HAPS), solar diurnal energy balancing, aeroelastic flutter suppression, non-orbital persistence."},
    {"slug": "nextgen-arsenal", "name": "NextGen Arsenal", "origin": "International", "type": "Research Source", "platforms": ["Orbital Guardian ADR Hunter"], "focus": "Active Debris Removal, proximity operations (RPO), non-cooperative tumbling target capture, dual-use counter-space."},
    {"slug": "darpa", "name": "DARPA & Skunk Works Experimental", "origin": "USA", "type": "Research Source", "platforms": ["Mach 6 Hypersonic Waverider (Corvus)"], "focus": "Hypersonic aerothermodynamics, compression lift waveriders, laser communications through plasma sheaths."},
    {"slug": "global-aerospace", "name": "Defense Aerospace Research", "origin": "USA / Global", "type": "Research Source", "platforms": ["Transonic / Supersonic Stealth UCAV"], "focus": "Tailless blended wing-body stealth, internal weapons bays, aerothermal boundary layer dynamics."},
    {"slug": "hypersonic-consortium", "name": "Next-Gen Hypersonic Consortium", "origin": "International", "type": "Research Source", "platforms": ["Autonomous Sickle Wing"], "focus": "Tailless sickle wing planforms, fluidic thrust vectoring (FTV), supersonic active flow control."},
    {"slug": "vantage-aerospace", "name": "Vantage Aerospace / Northrop Grumman Legacy", "origin": "USA", "type": "Research Source", "platforms": ["Vantage Tacitframe ('The Whale')", "Tacit Blue Heritage"], "focus": "Continuous-curvature Gaussian stealth airframes, pilotless radar cavity elimination, 360-degree all-aspect low observability."},
    {"slug": "petrel-tech", "name": "Petrel Technologies & Sustainable Skylines", "origin": "USA", "type": "OEM", "platforms": ["AERO Sky Drone Mothership", "SkyDrop Systems"], "focus": "Fixed-wing airborne mothership carriers, dynamic center-of-gravity release management, tactical strike copter air-drop."},
    {"slug": "tusas-aselsan", "name": "Turkish Aerospace (TUSAŞ) & ASELSAN", "origin": "Turkey", "type": "OEM", "platforms": ["Aksungur MALE UCAV", "aselBUOY 100P Sonobuoy", "ANKA Series"], "focus": "Long-endurance maritime ASW patrol, air-to-subsea acoustic sonobuoy gateways, twin turbodiesel powerplants."},
    {"slug": "defpulse-coalition", "name": "Ukrainian Drone Coalition & DefPulse", "origin": "Ukraine", "type": "Frontline Cluster", "platforms": ["P1-Sun 450km/h Interceptor", "Zhakh/Khyzhak Fiber Munition", "Vyriy PRO Optical Terminal"], "focus": "Frontline combat multirotors, 450 km/h kinetic sprint interception, zero-RF fiber-optic guidance, edge-AI terminal lock."},
    {"slug": "stratonex", "name": "Stratonex Robotics", "origin": "Ukraine / UK", "type": "OEM", "platforms": ["VARAN Heavy Attrition UGV", "Ground Towing Systems"], "focus": "High-attrition disposable robotic transport, quasi-static geometry suspension, passive stereoscopic optical odometry."},
    {"slug": "lpp-praha", "name": "LPP Praha", "origin": "Czech Republic", "type": "OEM", "platforms": ["JWI-4000 C-UAS Interceptor", "ASTERIX Flight Directors"], "focus": "Dedicated vertical sprint C-UAS interceptors, 4,000m altitude ceilings, NATO ASTERIX radar track integration."},
    {"slug": "lurtz-hmt", "name": "Patrick Lurtz / European MilTech Architecture", "origin": "Germany / Europe", "type": "Strategic Architect", "platforms": ["Autonomous Kill Zone Architecture", "HMT Screen Line Networks"], "focus": "Human-machine teaming (HMT), cognitive bandwidth decoupling, combined arms robotic screens, intent-based lethal control."},
    {"slug": "stat-caylus", "name": "French Army STAT & Caylus Urban Combat Center", "origin": "France", "type": "Military Trial Center", "platforms": ["B2LT C-UAS Interceptor", "Tube-Launched Kinetic Modules"], "focus": "Zero-collateral hard-kill drone interception, tube-launched cold gas pneumatic systems, urban perimeter protection."},
    {"slug": "kashmir-sentinel", "name": "Choudhary Tactical / Border Surveillance Consortium", "origin": "India / International", "type": "Research Source", "platforms": ["Border Swarm Sentinel UAS", "Alpine AESA Nodes"], "focus": "Alpine radar picket UAS, pulse-Doppler mountain face clutter suppression, valley RF MESH repeaters."},
    {"slug": "rusi-analysis", "name": "RUSI & Frontline Operational Analysis", "origin": "UK / Ukraine", "type": "Defense Think-Tank", "platforms": ["Rasputitsa Ground Assessment", "All-Wheel Traction Models"], "focus": "Environmental Abstraction Layer (EAL), Bekker-Wong viscous soil mechanics, mud mobility telemetry, abrasive wear modeling."},
    {"slug": "south-china-reef", "name": "PLAN / Indo-Pacific Strategic Analysis", "origin": "International / Indo-Pacific", "type": "Strategic Source", "platforms": ["Atoll Interdiction USV", "Shallow Reef Vessels"], "focus": "Shallow-water lagoon waterjets, high-speed stepped hull hydrodynamics, tropical corrosion mitigation, coral reef navigation."},
    {"slug": "fitburg", "name": "Fitburg Marine & Subsea Infrastructure Defense", "origin": "Europe / Baltic", "type": "OEM", "platforms": ["Critical Undersea Infrastructure Sentinel", "Seabed Cable Picketers"], "focus": "Continental shelf infrastructure defense, anchor-drag acoustic sabotage detection, stationary seabed sentinels."},
    {"slug": "philippine-carrier", "name": "Philippine Armed Forces / Littoral Defense", "origin": "Philippines", "type": "Defense Force Source", "platforms": ["Chokepoint Saturation USV", "Archipelagic Strike Swarms"], "focus": "Asymmetric chokepoint interdiction, archipelagic strait defense, 360-degree multi-axis swarm saturation, low-RCS wave-piercing hulls."},
    {"slug": "spm-group", "name": "SPM Group & Ukrainian Space Cluster", "origin": "Ukraine", "type": "OEM", "platforms": ["Kondratyuk 1.0 FEU ADR Hunter", "RPO Orbital Platforms"], "focus": "Active Debris Removal (ADR), Low Earth Orbit rendezvous and proximity operations (RPO), non-cooperative tumbling target capture."},
{"slug": "fox2sierra", "name": "Fox2Sierra & Tactical Edge Command", "origin": "USA / International", "type": "Strategic Architect", "platforms": ["Joint Multi-Domain C2 Cloud", "Edge Mission Commander"], "focus": "Cross-domain kill-chain orchestration, Air-Ground-Sea heterogeneous swarm fusion, microsecond sensor-to-shooter handoffs."},
    {"slug": "regent-craft", "name": "REGENT Craft", "origin": "USA", "type": "OEM", "platforms": ["REGENT Viceroy Seaglider"], "focus": "Tri-modal wing-in-ground-effect craft, deployable hydrofoils, distributed electric propulsion blown flaps."},
    {"slug": "hop-aero", "name": "Hop Aero", "origin": "USA", "type": "OEM", "platforms": ["Hop Aero ROOK Cargo Rocket"], "focus": "Container-launched suborbital cargo rockets, supersonic VTVL re-entry, terrain-relative terminal touchdown."},
    {"slug": "avidrone-aerospace", "name": "Avidrone Aerospace", "origin": "Canada / USA", "type": "OEM", "platforms": ["Avidrone 740T", "Avidrone 210TL"], "focus": "Tandem-rotor disc dynamics, gas turbine heavy-fuel cargo rotorcraft, automated slung-load pickup."},
    {"slug": "oshen-ltd", "name": "Oshen Ltd", "origin": "UK", "type": "OEM", "platforms": ["Oshen C-Star PC13"], "focus": "Micro-scale autonomous wingsail USVs, perpetual wind-propelled ocean transit, distributed acoustic sentinels."},
    {"slug": "preneu", "name": "PRENEU", "origin": "South Korea", "type": "OEM", "platforms": ["MILVUS T400", "PANDION Q1200"], "focus": "Lift+Cruise tactical hybrid UAS, closed-loop wind-compensated ballistic munition drops, sovereign flight controllers."},
    {"slug": "airbus-aerovel", "name": "Airbus & Aerovel", "origin": "France / USA", "type": "OEM", "platforms": ["Airbus Flexrotor VTOL"], "focus": "Single-proprotor tailsitter VTOL UAS, two-stroke heavy-fuel endurance, small shipboard automated recovery."},
    {"slug": "world-titan-forces", "name": "World Titan Forces Research", "origin": "International", "type": "Research Source", "platforms": ["Solaris One GEO Platform"], "focus": "Theoretical geostationary megastructures, sparse-aperture optical interferometry, solar radiation pressure dynamics."},
    {"slug": "chaklun-aviation", "name": "Chaklun Aviation Frontline Cluster", "origin": "Ukraine", "type": "Frontline Cluster", "platforms": ["Chaklun Tactical Reconnaissance UAV"], "focus": "Hand-launched EPP flying wings, complete radio-silent dead-reckoning navigation, low-RCS front-line scouting."},
    {"slug": "intelligent-energy", "name": "Intelligent Energy", "origin": "UK", "type": "OEM", "platforms": ["IE-SOAR Hydrogen Fuel Cell Modules"], "focus": "Lightweight open-cathode PEM fuel cells, 350-bar composite hydrogen storage, hybrid battery power arbitration."},
    {"slug": "avilus-gmbh", "name": "Avilus GmbH", "origin": "Germany", "type": "OEM", "platforms": ["Avilus Grille MEDEVAC eVTOL"], "focus": "Autonomous heavy-lift CASEVAC coaxial hexacopters, physiological G-clamping, ISO container field deployment."},
    {"slug": "ziyan-technology", "name": "ZIYAN Technology", "origin": "China / International", "type": "OEM", "platforms": ["Grey Whale G1 Cargo Helicopter"], "focus": "Modular single-rotor electric cargo helicopters, automated standoff winch hoisting, high-altitude mountain envelopes."},
    {"slug": "tencore", "name": "TENCORE", "origin": "Ukraine", "type": "OEM", "platforms": ["MAT1LDA 8x8 Amphibious Carrier", "TerMIT 2.0 Tracked UGV"], "focus": "Amphibious all-wheel-drive mothership carriers, mother-parasite tactical deployment, riverine combat engineering."},
    {"slug": "nodrics", "name": "NODRICS", "origin": "Ukraine", "type": "OEM", "platforms": ["NODRICS MAT1LDA 8x8 Logistics UGV"], "focus": "Internal combustion amphibious tactical supply, heavy water-drag propulsion, stabilized casualty evacuation."},
    {"slug": "naval-group", "name": "Naval Group", "origin": "France", "type": "OEM", "platforms": ["Naval Group UCUV Demonstrator"], "focus": "Uncrewed combat underwater vehicles, continental shelf sea denial, heavy torpedo ejection ballast trim control."},
    {"slug": "nextgen-airpower", "name": "US NextGen Airpower Research", "origin": "USA", "type": "Research Source", "platforms": ["Sentinel Corebreak Directed-Energy Platform"], "focus": "Airborne high-energy laser interdiction, transonic aero-optical boundary layer correction, phase-change thermal management."},
    {"slug": "dassault-aviation", "name": "Dassault Aviation & French Air Force", "origin": "France", "type": "OEM", "platforms": ["Rafale F5 Loyal Wingman UCAV"], "focus": "Supersonic tailless stealth CCAs, nEUROn flight heritage, manned-unmanned teaming, aeroelastic load limiting."},
    {"slug": "vyriy-industries", "name": "Vyriy Industries Frontline Cluster", "origin": "Ukraine", "type": "Frontline Cluster", "platforms": ["Vyriy SLAVIC Tactical Reconnaissance Copter"], "focus": "Solid-state battery multirotors, sovereign encrypted digital datalinks, anti-AeroScope pilot security."},
    {"slug": "energy-book", "name": "Energy Book Tactical Systems", "origin": "International", "type": "Research Source", "platforms": ["Canister Arrow Tube-Launched Micro-UAV"], "focus": "Pneumatic canister tube-launch, sub-second folding-wing deployment, protected pusher propeller loitering munitions."},
    {"slug": "rovertech", "name": "RoverTech Frontline Cluster", "origin": "Ukraine", "type": "Frontline Cluster", "platforms": ["ZMIY Droid 12.7 Combat UGV"], "focus": "Elevating pantograph remote weapon stations, defilade 12.7mm heavy fire support, skid-steer recoil compensation."},
    {"slug": "nebesa-aerospace", "name": "Nebesa Aerospace", "origin": "Czech Republic / Ukraine", "type": "OEM", "platforms": ["NEBESA Suborbital Spaceplane"], "focus": "Horizontal-takeoff suborbital spaceplanes, combined turbojet-rocket propulsion, blended aerodynamic/reaction controls."},
    {"slug": "changsha-nighthawk", "name": "Changsha Nighthawk Technology", "origin": "China", "type": "OEM", "platforms": ["SkyX Bionic Flying Fish Triphibious Drone"], "focus": "Trans-medium triphibious morphing wing robotics, 800:1 water-air density transition, stealth subsea loitering."},
    {"slug": "bair-miltech", "name": "BAIR MilTech Architecture", "origin": "International", "type": "Research Source", "platforms": ["BAIR ARKHAN Autonomous Defense System"], "focus": "Heterogeneous carrier-parasite defense symbiosis, autonomous docking/charging stations, multi-domain edge AI fusion."}
]

DOMAINS_DATA = [
    {
        "code": "UAV",
        "name": "Unmanned Aerial Vehicles (Fixed-Wing & Hypersonic)",
        "medium": "Atmospheric Airspace (0 to 30 km)",
        "governing_laws": "Aerodynamic Lift-to-Drag (L/D), Mach number shock detachment, boundary-layer aerothermodynamics, wing loading.",
        "legacy_trap": "STANAG 4670 & DoD MTOW/HALE/MALE classifications rely on arbitrary weight and altitude boxes, ignoring kinetic threat omission limits and FPV interceptor speeds.",
        "cases": [
            "01-honda-evtol", "03-stealth-ucav", "04-waverider-corvus", "05-sickle-wing",
            "12-mq25-stingray", "13-fury-ghostbat", "16-rq81-diana", "18-vantage-tacitframe",
            "19-petrel-aero-sky", "20-tusas-aksungur", "23-lpp-jwi4000", "25-stat-caylus-b2lt",
            "26-kashmir-sentinel", "35-hopaero-rook", "38-preneu-tactical", "39-airbus-flexrotor",
            "41-chaklun-uav", "42-intelligent-energy-soar", "48-sentinel-corebreak",
            "49-xq45-fibertailor", "51-canister-arrow", "53-nebesa-spaceplane", "54-skyx-flyingfish"
        ]
    },
    {
        "code": "UCV",
        "name": "Unmanned Copter Vehicles (Combat Multirotors, Coaxials & Fluid-Power Heavy-Lift)",
        "medium": "Low-Altitude Disc-Loaded Aerodynamics & Fluid Power",
        "governing_laws": "Rotor disc loading (T/A), zero stall speed (V_stall = 0), momentum theory, advancing/retreating blade flapping dynamics, digital displacement fluid power.",
        "legacy_trap": "Conflating combat rotorcraft with hobbyist slang ('FPV'). FPV is a pilot screen mode, not a cyber-physical combat aircraft category.",
        "cases": [
            "09-capstone-coaxial", "15-tekever-ar6", "21-tactical-ucv-spectrum",
            "36-avidrone-tandem", "43-avilus-grille", "44-ziyan-greywhale-g1", "50-vyriy-slavic"
        ]
    },
    {
        "code": "UGV",
        "name": "Unmanned Ground Vehicles (Tactical Robotics & Prime Movers)",
        "medium": "Terrestrial & Amphibious Terrain",
        "governing_laws": "Bekker-Wong soil mechanics, drawbar pull (F_pull = μ * m * g), ground pressure (kg/cm²), rolling resistance, steering slip ratios, kinetic evasion velocity.",
        "legacy_trap": "Amateur slang ('vozyk', 'cart') and marketing claims of 10-tonne towing based on electric motor kW while ignoring soil shear failure in mud.",
        "cases": [
            "02-slimak-ugv", "08-unex-artillery", "14-knds-centurio", "17-frodo-ugv",
            "22-stratonex-varan", "24-lurtz-kill-zone", "27-rusi-rasputitsa",
            "45-tencore-mat1lda", "46-nodrics-mat1lda", "52-rovertech-zmiy", "55-bair-arkhan"
        ]
    },
    {
        "code": "UUV",
        "name": "Unmanned Undersea Vehicles (Sub-Surface Robotics)",
        "medium": "Sub-surface Hydrospace (0 to 11,000m)",
        "governing_laws": "Hydrostatic pressure gradient (1 atm / 10m), acoustic transmission loss, acoustic cavitation, boundary-layer drag, parasitic energy harvesting.",
        "legacy_trap": "Classifying submersibles by geometric hull form factors (torpedo vs box) rather than physical Depth Horizons (D0 to D5) and acoustic signatures.",
        "cases": [
            "07-ghostshark-auv", "11-lockheed-lamprey", "29-fitburg-sentinel", "47-navalgroup-ucuv"
        ]
    },
    {
        "code": "USV",
        "name": "Unmanned Surface Vehicles (Littoral & Marine Vessels)",
        "medium": "Ocean Surface Boundary Layer (Air-Sea Interface)",
        "governing_laws": "Froude number, wave-piercing slender hull dynamics, Sea State (Beaufort scale) vertical g-shock limits, transverse metacentric height (GM_T).",
        "legacy_trap": "Using fragile recreational planing speedboats for open-ocean missions; high vertical g-shocks (>6g) destroy gimbal sensors and break hulls in Sea State 4+.",
        "cases": [
            "06-exail-usv", "28-south-china-reef", "30-philippine-carrier",
            "34-regent-seaglider", "37-oshen-cstar"
        ]
    },
    {
        "code": "UOV",
        "name": "Unmanned Orbital Vehicles (Counter-Space & Interceptors)",
        "medium": "Low Earth Orbit & Cislunar Space (160 to 36,000 km)",
        "governing_laws": "Keplerian two-body celestial mechanics, Clohessy-Wiltshire relative equations, Tsiolkovsky rocket equation ΔV limits, solar radiation pressure.",
        "legacy_trap": "Sci-fi free-flight orbital tropes: changing orbital inclination by 15° at LEO costs ~2,000 m/s ΔV, locking chemical hunters into narrow co-planar targets.",
        "cases": ["10-orbital-guardian", "31-spm-kondratyuk", "40-solaris-one"],
        "axis_legend": {
            "octet_1": "Orbital Regime & Container Tier (L: Low Earth Orbit / M: Medium Tactical / S: Sun-Synchronous / G: Geostationary Orbit)",
            "octet_2": "Propulsion & Mission (C: Chemical Reaction Thruster / S: Solar Photovoltaic / A: Active Debris Removal / RPO)",
            "octet_3": "Doctrine & Comms (H: High-Survivability Space Shield / M: Multi-Aperture Coordination / R: Radiation-Hardened / D: Deep-Space Gateway)"
        }
    }
]
CASE_CATEGORIES = [domain["code"] for domain in DOMAINS_DATA] + ["C2"]

VALIDATION_DATA = {
    "summary": {
        "total_laws": 4,
        "confirmed_laws": 4,
        "total_postulates": 5,
        "confirmed_postulates": 5,
        "total_rules": 9,
        "confirmed_rules": 9,
        "percentage": 100
    },
    "laws": [
        {
            "id": "LAW-1",
            "name": "Law of Kinematic Primacy",
            "statement": "The physical interface with the operating medium (air, ground, sea, space) strictly dictates platform physics and domain. Cosmetic shapes and commercial marketing terms cannot violate aerodynamic L/D, Bekker soil mechanics, or hydrodynamics.",
            "status": "CONFIRMED",
            "proof_cases": [
                {"id": "02", "slug": "02-slimak-ugv", "name": "SlimAk UGV", "insight": "Passive mechanical hinge is chassis articulation, not adaptive suspension."},
                {"id": "03", "slug": "03-stealth-ucav", "name": "Stealth UCAV", "insight": "Cockpit bubble canopies destroy transonic wave drag and inlet pressure recovery."},
                {"id": "05", "slug": "05-sickle-wing", "name": "Sickle Wing", "insight": "Hypersonic flight eliminates mechanical hinges in favor of fluidic thrust vectoring."},
                {"id": "06", "slug": "06-exail-usv", "name": "Exail USV", "insight": "Persistent ocean denial demands wave-piercing displacement, not fragile planing."},
                {"id": "08", "slug": "08-unex-artillery", "name": "UNEX ABRIS", "insight": "Towing capacity in mud is bounded by Bekker soil shear, not motor kW."},
                {"id": "09", "slug": "09-capstone-coaxial", "name": "CAPSTONE Coaxial", "insight": "Zero stall speed and disc loading strictly define UCV copter physics."},
                {"id": "14", "slug": "14-knds-centurio", "name": "KNDS CENTURIO UGV", "insight": "4WS steering kinematics eliminate lateral tire scrubbing, conserving 35-40% traction energy."},
                {"id": "17", "slug": "17-frodo-ugv", "name": "НРК «Фродо» 6x6 UGV", "insight": "40 km/h sprint velocity acts as active kinetic defense breaking FPV intercept angles."}
            ]
        },
        {
            "id": "LAW-2",
            "name": "Law of Hierarchical Containerization (C0–C4)",
            "statement": "Logistics deployment footprints strictly govern robotic vehicle mass, range, and operational tempo. Platforms are partitioned into C0 (Handheld), C1 (Man-Portable), C2 (Light/Dispersed), C3 (Heavy/Slipway), and C4 (Strategic/CATOBAR).",
            "status": "CONFIRMED",
            "proof_cases": [
                {"id": "01", "slug": "01-honda-evtol", "name": "Honda eVTOL", "insight": "C2 dispersed theater logistics requires GT-HEV to avoid C4 infrastructure lock."},
                {"id": "06", "slug": "06-exail-usv", "name": "Exail DriX/Oryx", "insight": "C2 (9m) vs C3 (16m) modular logistics dictate harbor slipway vs ocean crane handling."},
                {"id": "07", "slug": "07-ghostshark-auv", "name": "Ghost Shark XL-AUV", "insight": "C3 heavy slipway footprint allows 12-mine capacity without strategic nuclear docks."},
                {"id": "10", "slug": "10-orbital-guardian", "name": "Orbital Guardian", "insight": "C2 ESPA rideshare class (150-300kg) dictates upper-stage dispenser interfaces."},
                {"id": "12", "slug": "12-mq25-stingray", "name": "MQ-25 Stingray", "insight": "C4 CATOBAR carrier-basing requires arresting gear and bow catapult compatibility."},
                {"id": "13", "slug": "13-fury-ghostbat", "name": "Anduril Fury / MQ-28", "insight": "C2 dispersed runway operations enable distributed survivable air combat mass."},
                {"id": "15", "slug": "15-tekever-ar6", "name": "TEKEVER AR6 UAS", "insight": "C2 tactical footprint delivers 200kg cargo over 500km without C3/C4 strategic runway lock."},
                {"id": "17", "slug": "17-frodo-ugv", "name": "НРК «Фродо» 6x6", "insight": "C2 tactical trailer footprint enables 6x6 crater mobility and quick-swap battery logistics."}
            ]
        },
        {
            "id": "LAW-3",
            "name": "Law of Hardware Abstraction & Decoupled Lethality",
            "statement": "The physical chassis operates as an invariant robotic carrier with standardized HAL contracts, completely decoupled from modular payloads and mission profiles (ISR, EW, Strike, or One-Way Mission / Kamikaze decorator).",
            "status": "CONFIRMED",
            "proof_cases": [
                {"id": "06", "slug": "06-exail-usv", "name": "Exail USV", "insight": "Dynamic drop-keel gondola decouples ASW/hydrographic sensors from hull motions."},
                {"id": "07", "slug": "07-ghostshark-auv", "name": "Ghost Shark", "insight": "Invariant subsea hull interchanges 12 naval mines, ALTIUS UAVs, or SOF modules."},
                {"id": "10", "slug": "10-orbital-guardian", "name": "Orbital Guardian", "insight": "Dual-use hardware: ADR debris capture and offensive ASAT use identical HAL contracts."},
                {"id": "11", "slug": "11-lockheed-lamprey", "name": "Lamprey MMAUV", "insight": "24 cu ft modular bay separates effector lethality from host vehicle transport."},
                {"id": "12", "slug": "12-mq25-stingray", "name": "MQ-25 Tanker", "insight": "Decoupled Cobham ARS pod transforms carrier strike aircraft into persistent refuelers."},
                {"id": "13", "slug": "13-fury-ghostbat", "name": "Fury CCA", "insight": "Conformal bay decouples kinetic airframe from AIM-120/AIM-9X munitions."},
                {"id": "14", "slug": "14-knds-centurio", "name": "KNDS CENTURIO", "insight": "Invariant 2.8t 4WS PHOBOS chassis decouples from ARX20/30 autocannon or sapper modules."},
                {"id": "15", "slug": "15-tekever-ar6", "name": "TEKEVER AR6 UAS", "insight": "Invariant fluid-power rotorcraft platform decouples heavy cargo from flight control stabilization."},
                {"id": "17", "slug": "17-frodo-ugv", "name": "НРК «Фродо» UGV", "insight": "Invariant 6x6 chassis decouples from 'Buriya' stabilized turret or CASEVAC payloads."}
            ]
        },
        {
            "id": "LAW-4",
            "name": "Law of Dual-Read Cognitive Synchronization",
            "statement": "Autonomous warfare demands a unified 6-character cyber-physical token ([Domain/Horizon-Container]-[Powerplant-Mission]-[Doctrine-Comms]) decipherable simultaneously by human commanders and edge tactical AI microkernels in microseconds.",
            "status": "CONFIRMED",
            "proof_cases": [
                {"id": "01", "slug": "01-honda-evtol", "name": "Honda eVTOL", "insight": "Token UAV: AL-TL-HR parsed by commander and mission router instantly."},
                {"id": "02", "slug": "02-slimak-ugv", "name": "SlimAk UGV", "insight": "Token UGV: GL-EP-WR establishes mobility and mesh comms profile in 6 chars."},
                {"id": "06", "slug": "06-exail-usv", "name": "Exail USV", "insight": "Token USV: SL-PA-DR governs drop-keel telemetry and endurance constraints."},
                {"id": "07", "slug": "07-ghostshark-auv", "name": "Ghost Shark", "insight": "Token UUV: PT-RM-DA encodes 1000m pelagic depth and multi-mine salvo mission."},
                {"id": "10", "slug": "10-orbital-guardian", "name": "Orbital Guardian", "insight": "Token UOV: LM-CA-HR sets LEO orbit, chemical propulsion, and RPO grappling."},
                {"id": "12", "slug": "12-mq25-stingray", "name": "MQ-25 Stingray", "insight": "Token UAV: AI-TF-DR defines CATOBAR tanker escort doctrine microsecond routing."},
                {"id": "13", "slug": "13-fury-ghostbat", "name": "Fury CCA", "insight": "Token UAV: AL-TC-DR establishes transonic air superiority and Lattice OS edge mesh."},
                {"id": "14", "slug": "14-knds-centurio", "name": "KNDS CENTURIO", "insight": "Token UGV: GL-DC-DR encodes diesel hydrostatic drive and fiber-optic tether link."},
                {"id": "15", "slug": "15-tekever-ar6", "name": "TEKEVER AR6", "insight": "Token UCV: CL-PL-DR establishes fluid-power heavy logistics and anti-jam profile."},
                {"id": "16", "slug": "16-rq81-diana", "name": "Solar HAPS", "insight": "Token UAV: AL-ER-DO defines stratospheric diurnal solar persistence and laser cross-links."},
                {"id": "17", "slug": "17-frodo-ugv", "name": "НРК «Фродо»", "insight": "Token UGV: GL-EM-DR sets 6x6 electric quick-swap logistics and multi-bearer C2."}
            ]
        }
    ],
    "postulates": [
        {
            "id": "POSTULATE-1",
            "name": "Environmental Abstraction Layer (Anti-1812 Engine)",
            "statement": "Autonomous vehicles must absorb and overcome brutal environmental degradation (viscous mud, aerothermal plasma blackout, Sea State 5, hydrostatic depth, and space vacuum) at the hardware-software HAL boundary.",
            "status": "CONFIRMED",
            "proof_cases": [
                {"id": "02", "slug": "02-slimak-ugv", "name": "SlimAk UGV", "insight": "Articulated chassis eliminates wheel scrubbing in deep frontline viscous mud."},
                {"id": "04", "slug": "04-waverider-corvus", "name": "Mach 6 Waverider", "insight": "IThermalPlasmaLink commands aft laser to bypass Mach 6 RF plasma blackout."},
                {"id": "06", "slug": "06-exail-usv", "name": "Exail DriX USV", "insight": "Drop-keel lowers acoustic payload below surface aeration in Sea State 5."},
                {"id": "08", "slug": "08-unex-artillery", "name": "UNEX ABRIS", "insight": "Bekker soil slip traction controller prevents wheel spin-down in clay soils."},
                {"id": "16", "slug": "16-rq81-diana", "name": "Solar HAPS", "insight": "Gravitational battery maneuver trades potential energy for lift during diurnal solar deficit."},
                {"id": "17", "slug": "17-frodo-ugv", "name": "НРК «Фродо» 6x6", "insight": "Variable 170-330mm ground clearance and N-1 wheel tolerance negotiate shell craters."}
            ]
        },
        {
            "id": "POSTULATE-2",
            "name": "Parasitic Energy Harvesting & Tanker Lifelines",
            "statement": "True continuous theater persistence cannot rely on individual battery capacities; it mandates distributed parasitic energy harvesting from host platforms, natural flows, or specialized airborne refueling tankers.",
            "status": "CONFIRMED",
            "proof_cases": [
                {"id": "11", "slug": "11-lockheed-lamprey", "name": "Lockheed Lamprey", "insight": "Hydrokinetic in-transit harvesting recharges battery to 100% SoC on host sub hulls."},
                {"id": "12", "slug": "12-mq25-stingray", "name": "MQ-25 Stingray", "insight": "Carrier tanker refuels CCA fighter swarms, doubling combat reach to 900+ nmi."}
            ]
        },
        {
            "id": "POSTULATE-3",
            "name": "Sleeper / Sentinel Posture ('Zhdun' State)",
            "statement": "To survive ubiquitous ISR surveillance, autonomous robotic units must execute ultra-low-power zero-acoustic sentinel postures, lying dormant until triggered by acoustic, seismic, or RF tripwires.",
            "status": "CONFIRMED",
            "proof_cases": [
                {"id": "07", "slug": "07-ghostshark-auv", "name": "Ghost Shark XL-AUV", "insight": "Rests on continental shelf for weeks with zero acoustic output awaiting choke-point targets."},
                {"id": "11", "slug": "11-lockheed-lamprey", "name": "Lockheed Lamprey", "insight": "Executes seabed anchor posture with all thrusters unpowered for covert minefield ambush."}
            ]
        },
        {
            "id": "POSTULATE-4",
            "name": "Cross-Domain Heterogeneous Kill Web",
            "statement": "No single domain operates in isolation. Theater containment lines function as a cross-domain web linking Subsea (UUV) + Surface (USV) + Air (UAV/UCV) + Orbit (UOV) with microsecond latency.",
            "status": "CONFIRMED",
            "proof_cases": [
                {"id": "04", "slug": "04-waverider-corvus", "name": "Hypersonic Corvus", "insight": "Direct laser uplink to Low Earth Orbit satellites enables Mach 6 target handoff."},
                {"id": "07", "slug": "07-ghostshark-auv", "name": "Ghost Shark + BlueBottle", "insight": "Subsea UUV + surface wave-harvesting USV + air ALTIUS UAV form heterogeneous triad."},
                {"id": "13", "slug": "13-fury-ghostbat", "name": "Anduril CCA Triad", "insight": "Fury interceptor + Ghost Bat sensor node + MQ-25 fuel tanker form continuous aerial line."}
            ]
        },
        {
            "id": "POSTULATE-5",
            "name": "Rejection of 'Wunderwaffen' for Attritable Mass",
            "statement": "Single, bespoke, billionaire-class exquisite weapon systems are mathematically defeated in attrition warfare. Algorithmic software superiority coupled with COTS engines and attritable composite mass dictates victory.",
            "status": "CONFIRMED",
            "proof_cases": [
                {"id": "12", "slug": "12-mq25-stingray", "name": "MQ-25 Stingray", "insight": "Standardized turbofan airframe relieves 25% of costly manned fighter sorties."},
                {"id": "13", "slug": "13-fury-ghostbat", "name": "Anduril Fury (CCA)", "insight": "Commercial FJ44 engine + carbon monocoque yields mass-producible 9G dogfighters."}
            ]
        }
    ]
}

def write_file(rel_path, content):
    dest = DOCS / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"  [PAGE WRITTEN] docs/{rel_path}")

def copy_asset_binary(src_name, rel_dest):
    src = WORKSPACE / src_name
    dest = DOCS / rel_dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    if src.exists():
        shutil.copy2(src, dest)
        print(f"  [ASSET COPIED] {src_name} -> docs/{rel_dest}")
    else:
        print(f"  [ASSET MISSING] {src_name} not found in workspace root")

def generate_css():
    css = """/* UWE Scientific-Practical Reddit/ArXiv Technical Dark Theme */
:root {
  --bg-dark: #0d1117;
  --surface: #161b22;
  --surface-alt: #21262d;
  --border: #30363d;
  --border-light: #484f58;
  --text-main: #e6edf3;
  --text-muted: #8b949e;
  --accent: #58a6ff;
  --accent-hover: #1f6feb;
  --green: #2ea043;
  --green-bg: #122616;
  --red: #f85149;
  --red-bg: #2d1617;
  --amber: #d29922;
  --amber-bg: #2d2206;
  --purple: #bc8cff;
  --purple-bg: #27173e;
  --cyan: #38bdf8;
  --cyan-bg: #07273d;
  --code-font: "JetBrains Mono", "SF Mono", "Fira Code", monospace;
  --sans-font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 0;
  background-color: var(--bg-dark);
  color: var(--text-main);
  font-family: var(--sans-font);
  line-height: 1.6;
  font-size: 15px;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
header.top-nav {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0.75rem 1.5rem;
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.nav-brand { font-weight: 700; font-size: 1.1rem; color: #fff; display: flex; align-items: center; gap: 0.5rem; }
.nav-links { display: flex; gap: 1.25rem; font-size: 0.9rem; align-items: center; }
.nav-links a { color: var(--text-muted); }
.nav-links a:hover, .nav-links a.active { color: var(--text-main); }
.container { max-width: 1150px; margin: 0 auto; padding: 2rem 1.25rem; }
.hero-box {
  background: linear-gradient(180deg, var(--surface) 0%, rgba(22,27,34,0.4) 100%);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 2.5rem 2rem;
  margin-bottom: 2rem;
}
.hero-title { font-size: 2.2rem; margin: 0 0 0.5rem 0; line-height: 1.2; color: #fff; }
.hero-subtitle { font-size: 1.15rem; color: var(--text-muted); margin: 0 0 1.5rem 0; }
.author-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  padding: 0.35rem 0.85rem;
  border-radius: 20px;
  font-size: 0.85rem;
  color: var(--text-muted);
}
.author-pill strong { color: var(--text-main); }
.badge {
  display: inline-block;
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
  font-family: var(--code-font);
  border: 1px solid transparent;
}
.badge-uav { background: var(--green-bg); color: #3fb950; border-color: var(--green); }
.badge-ucv { background: var(--amber-bg); color: var(--amber); border-color: #9e6a03; }
.badge-ugv { background: var(--purple-bg); color: var(--purple); border-color: #8957e5; }
.badge-uuv { background: #0c2340; color: #58a6ff; border-color: #1f6feb; }
.badge-usv { background: var(--cyan-bg); color: var(--cyan); border-color: #0284c7; }
.badge-uov { background: #361608; color: #ff7b72; border-color: #d03801; }
.badge-c2 { background: rgba(99, 102, 241, 0.2); color: #a5b4fc; border-color: rgba(99, 102, 241, 0.4); }
.badge-vendor { background: var(--surface-alt); color: var(--text-muted); border-color: var(--border); }
.badge-hal { background: #161b22; color: #a5d6ff; border-color: #388bfd; font-family: var(--code-font); }

/* Top KPI Telemetry Ribbon */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}
.kpi-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.25rem 1rem;
  text-align: center;
  transition: transform 0.15s ease, border-color 0.15s ease;
}
.kpi-card:hover {
  transform: translateY(-2px);
  border-color: var(--border-light);
}
.kpi-card.highlight {
  border-color: #2ea043;
  background: linear-gradient(180deg, #122616 0%, var(--surface) 100%);
}
.kpi-num {
  font-size: 2.2rem;
  font-weight: 800;
  font-family: var(--code-font);
  color: #fff;
  line-height: 1;
}
.kpi-card.highlight .kpi-num {
  color: #3fb950;
}
.kpi-label {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-top: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}
.kpi-sub {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 0.25rem;
}

/* Domain Spectrum Bar */
.spectrum-wrap {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.25rem;
  margin: 1.5rem 0;
}
.spectrum-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.spectrum-bar {
  display: flex;
  height: 16px;
  border-radius: 8px;
  overflow: hidden;
  gap: 2px;
  background: #0d1117;
  padding: 2px;
  border: 1px solid var(--border);
}
.spec-seg {
  height: 100%;
  transition: opacity 0.2s, transform 0.2s;
  cursor: pointer;
  border-radius: 4px;
}
.spec-seg:hover {
  opacity: 0.85;
  filter: brightness(1.2);
}
.spectrum-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 0.85rem;
  font-size: 0.8rem;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: var(--text-muted);
}
.legend-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  display: inline-block;
}

/* Concept Validation Dashboard */
.val-dashboard {
  background: linear-gradient(180deg, #101726 0%, var(--surface) 100%);
  border: 1px solid #1f3a5f;
  border-radius: 8px;
  padding: 1.75rem;
  margin: 2rem 0;
}
.progress-meter {
  background: #0d1117;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.25rem;
  margin: 1rem 0 1.5rem 0;
}
.progress-labels {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.6rem;
  font-family: var(--code-font);
}
.progress-track {
  height: 20px;
  background: var(--surface-alt);
  border-radius: 10px;
  overflow: hidden;
  position: relative;
  border: 1px solid #30363d;
}
.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #2ea043 0%, #38bdf8 100%);
  border-radius: 10px;
  box-shadow: 0 0 14px rgba(56, 189, 248, 0.5);
  transition: width 0.5s ease-in-out;
}
.val-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.25rem;
  margin-bottom: 1rem;
}
.val-card.law {
  border-left: 4px solid var(--green);
}
.val-card.postulate {
  border-left: 4px solid var(--cyan);
}
.val-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 0.5rem;
  flex-wrap: wrap;
}
.val-card-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #fff;
  margin: 0;
}
.val-card-statement {
  font-size: 0.88rem;
  color: var(--text-muted);
  line-height: 1.5;
  margin: 0.5rem 0;
}
.val-proofs {
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px dashed var(--border);
}
.proof-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  font-size: 0.78rem;
  margin-right: 0.4rem;
  margin-bottom: 0.4rem;
  color: #e6edf3;
  transition: border-color 0.15s, background-color 0.15s;
}
.proof-tag:hover {
  border-color: var(--accent);
  background: #1f2937;
  text-decoration: none;
}

/* Reddit/ArXiv Post Card */
.reddit-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  transition: border-color 0.15s ease;
}
.reddit-card:hover { border-color: var(--border-light); }
.card-meta {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
}
.card-title { font-size: 1.35rem; margin: 0 0 0.75rem 0; color: #fff; }
.card-title a { color: #fff; }
.card-title a:hover { color: var(--accent); }
.token-banner {
  background: #0d1117;
  border: 1px solid var(--border);
  border-left: 4px solid var(--accent);
  padding: 0.75rem 1rem;
  border-radius: 4px;
  margin: 1rem 0;
  font-family: var(--code-font);
  font-size: 0.9rem;
}
.token-banner strong { color: #58a6ff; }
.hal-box {
  background: #111827;
  border: 1px solid #1f2937;
  padding: 0.85rem 1rem;
  border-radius: 6px;
  margin: 1rem 0;
  font-size: 0.88rem;
}
.hal-box .hal-title { font-family: var(--code-font); color: #60a5fa; font-weight: 600; margin-bottom: 0.35rem; }
.pros-cons-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.25rem 0; }
@media (max-width: 768px) { .pros-cons-grid { grid-template-columns: 1fr; } }
.col-pro { background: var(--green-bg); border: 1px solid #1b4724; border-radius: 6px; padding: 1rem; }
.col-con { background: var(--red-bg); border: 1px solid #571b1d; border-radius: 6px; padding: 1rem; }
.col-pro h4 { color: #3fb950; margin: 0 0 0.5rem 0; font-size: 0.9rem; }
.col-con h4 { color: #f85149; margin: 0 0 0.5rem 0; font-size: 0.9rem; }
ul.points { margin: 0; padding-left: 1.25rem; font-size: 0.88rem; }
ul.points li { margin-bottom: 0.4rem; }
.lesson-box {
  background: var(--surface-alt);
  border-left: 4px solid var(--amber);
  padding: 0.85rem 1rem;
  border-radius: 0 6px 6px 0;
  margin: 1rem 0;
  font-size: 0.9rem;
}
.citation-box {
  background: #0d1117;
  border: 1px solid var(--border);
  padding: 0.75rem 1rem;
  border-radius: 6px;
  font-size: 0.85rem;
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.search-bar { width: 100%; padding: 0.75rem 1rem; background: var(--surface); border: 1px solid var(--border); color: #fff; border-radius: 6px; font-size: 1rem; margin-bottom: 1rem; }
.search-bar:focus { outline: none; border-color: var(--accent); }
.filter-group-label { font-size: 0.78rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700; margin-bottom: 0.4rem; letter-spacing: 0.5px; }
.filter-pills { display: flex; gap: 0.5rem; margin-bottom: 1rem; flex-wrap: wrap; }
.filter-pill { background: var(--surface); border: 1px solid var(--border); padding: 0.35rem 0.8rem; border-radius: 20px; font-size: 0.82rem; color: var(--text-muted); cursor: pointer; transition: all 0.15s ease; }
.filter-pill:hover, .filter-pill.active { background: var(--surface-alt); color: #fff; border-color: var(--accent); }
.filter-pill.active { background: #1f2937; color: var(--accent); font-weight: 600; }
.nav-links a.active-cta { color: #58a6ff; font-weight: 600; border: 1px solid rgba(88, 166, 255, 0.4); padding: 0.25rem 0.65rem; border-radius: 4px; background: rgba(88, 166, 255, 0.08); transition: all 0.15s ease; }
.nav-links a.active-cta:hover, .nav-links a.active-cta.active { background: rgba(88, 166, 255, 0.2); border-color: #58a6ff; color: #fff; text-decoration: none; }
.btn { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.65rem 1.25rem; font-size: 0.95rem; font-weight: 600; border-radius: 6px; text-decoration: none; transition: all 0.15s ease; cursor: pointer; }
.btn-primary { background: #238636; color: #fff; border: 1px solid rgba(240, 246, 252, 0.1); }
.btn-primary:hover { background: #2ea043; color: #fff; text-decoration: none; }
.btn-secondary { background: var(--surface-alt); color: var(--text-main); border: 1px solid var(--border); }
.btn-secondary:hover { background: #30363d; color: #fff; border-color: var(--border-light); text-decoration: none; }
.service-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 1.5rem 0; }
.service-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; transition: border-color 0.15s ease, transform 0.15s ease; }
.service-card:hover { border-color: var(--accent); transform: translateY(-2px); }
.service-header { border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1rem; }
.service-title { font-size: 1.2rem; font-weight: 700; color: #fff; margin: 0.25rem 0; }
.service-scope { font-size: 0.9rem; color: #c9d1d9; line-height: 1.5; margin-bottom: 1rem; }
.service-deliverables { background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; padding: 0.75rem 1rem; font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem; }
.service-deliverables strong { color: var(--text-main); }
.service-format { border-top: 1px dashed var(--border); padding-top: 0.75rem; font-size: 0.85rem; color: #58a6ff; font-weight: 600; font-family: var(--code-font); }
.gov-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.25rem; margin: 1.5rem 0; }
.gov-card { background: var(--surface); border: 1px solid var(--border); border-left: 4px solid #58a6ff; border-radius: 6px; padding: 1.25rem; }
.gov-card h4 { margin: 0 0 0.5rem 0; font-size: 1.05rem; color: #fff; }
.gov-card p { margin: 0; font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; }
.workflow-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1.5rem 0; }
.workflow-step { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; position: relative; }
.step-num { font-family: var(--code-font); font-size: 0.85rem; color: #3fb950; font-weight: 700; text-transform: uppercase; margin-bottom: 0.35rem; }
.step-title { font-size: 1rem; font-weight: 700; color: #fff; margin: 0 0 0.5rem 0; }
.step-desc { font-size: 0.85rem; color: var(--text-muted); line-height: 1.5; margin: 0; }
.inquiry-box { background: linear-gradient(135deg, rgba(31, 111, 235, 0.1) 0%, rgba(22, 27, 34, 0.95) 100%); border: 1px solid #1f6feb; border-radius: 8px; padding: 2rem; margin: 2rem 0; }
.legal-card { background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; padding: 1.25rem; margin-top: 1.5rem; font-size: 0.85rem; color: var(--text-muted); line-height: 1.6; }
.tag-pill { display: inline-flex; align-items: center; gap: 0.35rem; background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3); color: #38bdf8; padding: 0.25rem 0.65rem; border-radius: 20px; font-size: 0.8rem; font-weight: 500; }
footer.page-footer { background: var(--surface); border-top: 1px solid var(--border); padding: 2rem 1.5rem; text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-top: 3rem; }
"""
    write_file("assets/css/style.css", css)

def generate_js():
    js = """// Instant Client-Side Filter & Dual Search for UWE Cases
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('case-search');
  const cards = document.querySelectorAll('.case-item');
  const domainPills = document.querySelectorAll('.domain-pill');
  const vendorPills = document.querySelectorAll('.vendor-pill');
  const specSegs = document.querySelectorAll('.spec-seg');
  
  let activeDomain = 'ALL';
  let activeVendor = 'ALL';

  function applyFilter() {
    const q = (searchInput ? searchInput.value : '').toLowerCase().trim();
    let visibleCount = 0;

    cards.forEach(card => {
      const text = card.textContent.toLowerCase();
      const domain = card.getAttribute('data-domain') || '';
      const vendor = card.getAttribute('data-vendor') || '';

      const domainMatch = (activeDomain === 'ALL' || domain === activeDomain);
      const vendorMatch = (activeVendor === 'ALL' || vendor === activeVendor);
      const textMatch = !q || text.includes(q);

      if (domainMatch && vendorMatch && textMatch) {
        card.style.display = 'block';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    const countDisplay = document.getElementById('visible-count');
    if (countDisplay) {
      countDisplay.textContent = visibleCount;
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', applyFilter);
  }

  domainPills.forEach(pill => {
    pill.addEventListener('click', () => {
      domainPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeDomain = pill.getAttribute('data-domain-filter') || 'ALL';
      applyFilter();
    });
  });

  vendorPills.forEach(pill => {
    pill.addEventListener('click', () => {
      vendorPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeVendor = pill.getAttribute('data-vendor-filter') || 'ALL';
      applyFilter();
    });
  });

  specSegs.forEach(seg => {
    seg.addEventListener('click', () => {
      const targetDomain = seg.getAttribute('data-domain-filter') || 'ALL';
      domainPills.forEach(p => {
        if (p.getAttribute('data-domain-filter') === targetDomain) {
          p.classList.add('active');
        } else {
          p.classList.remove('active');
        }
      });
      activeDomain = targetDomain;
      applyFilter();
    });
  });
});
"""
    write_file("assets/js/search.js", js)

def render_header(active_nav="home", depth=0):
    rel = "../" * depth
    return f"""<header class="top-nav">
  <div class="nav-brand">
    <a href="{rel}index.html" style="color:#fff; font-weight:700;">⚡ UWE Standard</a>
  </div>
  <nav class="nav-links">
    <a href="{rel}index.html" class="{'active' if active_nav=='home' else ''}">Hub</a>
    <a href="{rel}domains/index.html" class="{'active' if active_nav=='domains' else ''}">Taxonomy & Domains</a>
    <a href="{rel}cases/index.html" class="{'active' if active_nav=='cases' else ''}">{len(CASES_DATA)} Benchmarks</a>
    <a href="{rel}c2/index.html" class="{'active' if active_nav=='c2' else ''}">C2 &amp; Articles</a>
    <a href="{rel}vendors/index.html" class="{'active' if active_nav=='vendors' else ''}">Vendors & OEMs</a>
<a href="{rel}hal/index.html" class="{'active' if active_nav=='hal' else ''}">HAL Registry</a>
    <a href="{rel}consulting.html" class="{'active active-cta' if active_nav=='consulting' else 'active-cta'}">Advisory &amp; Consulting</a>
    <a href="https://ua.linkedin.com/in/serhii-khylevych-aa152322" target="_blank" rel="noopener">Author Profile ↗</a>
  </nav>
</header>"""

def render_footer(is_consulting=False):
    if is_consulting:
        return """<footer class="page-footer">
  <div class="container">
    <p><strong>UWE Systems Architecture &amp; Advisory</strong> — Authored by <strong>Serhii Khylevych</strong>, Systems Architect.</p>
    <p style="margin-top:0.5rem; font-size:0.8rem; color:#8b949e;">
      Independent Systems Architecture, Hardware Abstraction Layers (HAL), and Engineering Advisory.<br>
      Strict adherence to physical laws, deterministic control contracts, and intellectual property protection.
    </p>
  </div>
</footer>"""
    return """<footer class="page-footer">
  <div class="container">
    <p><strong>Unmanned Warfare Engine (UWE)</strong> — Authored by <strong>Serhii Khylevych</strong>, Systems Architect.</p>
    <p style="margin-top:0.5rem; font-size:0.8rem; color:#8b949e;">
      Architecting a software-defined containment line and automated interdiction shield for the Free World.<br>
      Strict adherence to physical laws, hardware abstraction, and cyber-physical matrices. Local Kyiv wartime conditions.
    </p>
  </div>
</footer>"""

def render_spectrum_bar():
    colors = {
        "UAV": "#3fb950",
        "UCV": "#d29922",
        "UGV": "#bc8cff",
        "UUV": "#58a6ff",
        "USV": "#38bdf8",
        "UOV": "#ff7b72",
        "C2": "#ec4899",
    }
    domain_names = {
        "UAV": "Air",
        "UCV": "Copter",
        "UGV": "Ground",
        "UUV": "Subsea",
        "USV": "Surface",
        "UOV": "Orbital",
        "C2": "C2/Cloud",
    }
    total = len(CASES_DATA)
    if total == 0:
        return ""

    counts = [len([c for c in CASES_DATA if c["domain"] == code]) for code in CASE_CATEGORIES]
    raw_pcts = [(cnt / total) * 100.0 for cnt in counts]
    base_pcts = [int(p) for p in raw_pcts]
    remainders = [(raw_pcts[i] - base_pcts[i], i) for i in range(len(CASE_CATEGORIES))]
    remainders.sort(key=lambda x: (-x[0], x[1]))
    shortfall = 100 - sum(base_pcts)
    alloc_pcts = list(base_pcts)
    for k in range(shortfall):
        idx = remainders[k][1]
        alloc_pcts[idx] += 1

    segs = []
    legends = []
    for i, code in enumerate(CASE_CATEGORIES):
        cnt = counts[i]
        pct = raw_pcts[i]
        bar_w = alloc_pcts[i]
        color = colors.get(code, "#8b949e")
        short_name = domain_names.get(code, code)
        segs.append(f'<div class="spec-seg" data-domain-filter="{code}" style="width:{bar_w}%; background:{color};" title="{code} {short_name}: {cnt} cases ({pct:.1f}%)"></div>')
        legends.append(f'<span class="legend-item"><span class="legend-dot" style="background:{color};"></span> {code} {short_name} ({pct:.1f}%)</span>')
    
    return f"""<div class="spectrum-wrap">
      <div class="spectrum-head">
        <strong style="font-size:0.95rem; color:#fff;">📊 Cross-Domain Operational Spectrum ({total} Empirical Benchmarks)</strong>
        <span style="font-size:0.8rem; color:var(--text-muted);">Click bar segment to filter cases</span>
      </div>
      <div class="spectrum-bar">
        {"".join(segs)}
      </div>
      <div class="spectrum-legend">
        {"".join(legends)}
      </div>
    </div>"""

def render_filter_pills():
    total = len(CASES_DATA)
    total_vendors = len(VENDORS_DATA)
    domain_names = {
        "UAV": "Air",
        "UCV": "Copter",
        "UGV": "Ground",
        "UUV": "Subsea",
        "USV": "Surface",
        "UOV": "Orbital",
        "C2": "C2/Cloud",
    }
    d_pills = [f'<span class="filter-pill domain-pill active" data-domain-filter="ALL">All Categories ({total})</span>']
    for code in CASE_CATEGORIES:
        cnt = len([c for c in CASES_DATA if c["domain"] == code])
        short_name = domain_names.get(code, code)
        d_pills.append(f'<span class="filter-pill domain-pill" data-domain-filter="{code}">{code} {short_name} ({cnt})</span>')
    
    v_pills = [f'<span class="filter-pill vendor-pill active" data-vendor-filter="ALL">All Vendors ({total_vendors})</span>']
    for v in VENDORS_DATA:
        slug = v["slug"]
        cnt = len([c for c in CASES_DATA if c["vendor_slug"] == slug])
        v_pills.append(f'<span class="filter-pill vendor-pill" data-vendor-filter="{slug}">{v["name"]} ({cnt})</span>')
        
    return "".join(d_pills), "".join(v_pills)

def classification_path(code):
    return "c2/index.html" if code == "C2" else f"domains/{code.lower()}.html"


def render_case_card(case, depth=0):
    rel = "../" * depth
    pros_li = "".join(f"<li>{p}</li>" for p in case["advantages"])
    cons_li = "".join(f"<li>{c}</li>" for c in case["vulnerabilities"])
    related_badges = "".join(f'<a href="{rel}cases/{r}.html" class="badge badge-hal" style="margin-right:0.35rem;">🔗 Case #{r[:2]}</a>' for r in case.get("related", []))
    
    return f"""<article class="reddit-card case-item" data-domain="{case['domain']}" data-vendor="{case['vendor_slug']}" id="case-{case['id']}">
  <div class="card-meta">
    <span>Posted by <strong>Serhii Khylevych</strong> (Systems Architect)</span>
    <span>•</span>
    <span>{case['date']}</span>
    <span>•</span>
    <a href="{rel}{classification_path(case['domain'])}" class="badge badge-{case['domain'].lower()}">{case['domain']}</a>
    <a href="{rel}vendors/index.html#{case['vendor_slug']}" class="badge badge-vendor">{case['vendor']}</a>
  </div>
  <h2 class="card-title">
    <a href="{rel}cases/{case['slug']}.html">Case #{case['id']}: {case['name']}</a>
  </h2>
  
  <div class="token-banner">
    <div><strong>UWE Token:</strong> <code>{case['token']}</code></div>
    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:0.25rem;">{case['token_full']}</div>
  </div>

  <div class="hal-box">
    <div class="hal-title">⚙️ Tested HAL Contract: <a href="{rel}hal/index.html#{case['hal']}"><code>{case['hal']}</code></a></div>
    <div><em>"{case['hal_def']}"</em></div>
  </div>

  <div class="pros-cons-grid">
    <div class="col-pro">
      <h4>🟢 Physical Superiority (Compliance with Law of Kinematics)</h4>
      <ul class="points">{pros_li}</ul>
    </div>
    <div class="col-con">
      <h4>🔴 Engineering Vulnerabilities & Cyber-Physical Limits</h4>
      <ul class="points">{cons_li}</ul>
    </div>
  </div>

  <div class="lesson-box">
    <strong>💡 Architectural Lesson for UWE:</strong> {case['lesson']}
  </div>

  <div class="citation-box">
    <div>
      <strong>OSINT Source:</strong> <a href="{case['source_url']}" target="_blank" rel="noopener">{case['source_name']} ↗</a>
    </div>
    <div style="display:flex; align-items:center; gap:0.5rem;">
      <span style="font-size:0.8rem; color:var(--text-muted);">Related Triad:</span>
      {related_badges}
      <a href="{rel}cases/{case['slug']}.html" class="badge" style="background:var(--accent); color:#fff;">Full Study →</a>
    </div>
  </div>
</article>"""
def build_index():
    cases_html = "\n".join(render_case_card(c, depth=0) for c in CASES_DATA)
    domain_pills_html, vendor_pills_html = render_filter_pills()
    spectrum_bar_html = render_spectrum_bar()
    
    # Generate Laws HTML
    laws_html = ""
    for law in VALIDATION_DATA["laws"]:
        proof_tags = "".join(
            f'<a href="cases/{p["slug"]}.html" class="proof-tag">'
            f'<span>Case #{p["id"]} ({p["name"]})</span>'
            f'<span style="color:var(--text-muted);">• {p["insight"]}</span>'
            f'</a>'
            for p in law["proof_cases"]
        )
        laws_html += f"""<div class="val-card law">
  <div class="val-card-header">
    <div class="val-card-title">⚖️ {law['id']}: {law['name']}</div>
    <span class="badge badge-uav" style="font-size:0.75rem;">🟢 {law['status']} (100%)</span>
  </div>
  <p class="val-card-statement">"{law['statement']}"</p>
  <div class="val-proofs">
    <div style="font-size:0.8rem; font-weight:700; color:var(--text-muted); margin-bottom:0.4rem;">EMPIRICAL PROOF PLATFORMS ({len(law['proof_cases'])} Cases):</div>
    <div>{proof_tags}</div>
  </div>
</div>"""

    # Generate Postulates HTML
    postulates_html = ""
    for post in VALIDATION_DATA["postulates"]:
        proof_tags = "".join(
            f'<a href="cases/{p["slug"]}.html" class="proof-tag">'
            f'<span>Case #{p["id"]} ({p["name"]})</span>'
            f'<span style="color:var(--text-muted);">• {p["insight"]}</span>'
            f'</a>'
            for p in post["proof_cases"]
        )
        postulates_html += f"""<div class="val-card postulate">
  <div class="val-card-header">
    <div class="val-card-title">🛡️ {post['id']}: {post['name']}</div>
    <span class="badge badge-usv" style="font-size:0.75rem;">🟢 {post['status']} (100%)</span>
  </div>
  <p class="val-card-statement">"{post['statement']}"</p>
  <div class="val-proofs">
    <div style="font-size:0.8rem; font-weight:700; color:var(--text-muted); margin-bottom:0.4rem;">EMPIRICAL PROOF PLATFORMS ({len(post['proof_cases'])} Cases):</div>
    <div>{proof_tags}</div>
  </div>
</div>"""

    jsonld = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": "Unmanned Warfare Engine (UWE) — Cyber-Physical Matrix & Autonomous Defense Standard",
        "description": "Standardizing autonomous robotic fleets across air, copter, ground, subsea, surface, and orbital domains. Replaces obsolete STANAG 4670 with 4 Invariant Laws and Hardware Abstraction Layer (HAL).",
        "author": {
            "@type": "Person",
            "name": "Serhii Khylevych",
            "jobTitle": "Systems Architect",
            "url": "https://ua.linkedin.com/in/serhii-khylevych-aa152322"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Unmanned Warfare Engine Initiative"
        },
        "datePublished": "2026-10-19",
        "dateModified": "2026-10-20",
        "mainEntityOfPage": f"{BASE_URL}/index.html"
    }

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Unmanned Warfare Engine (UWE) — Cyber-Physical Robotics Standard</title>
  <meta name="description" content="Autonomous warfare doctrine, 6-character cyber-physical matrix, and {len(CASES_DATA)} empirical platform benchmarks replacing legacy STANAG 4670. Authored by Serhii Khylevych.">
  <link rel="canonical" href="{BASE_URL}/index.html">
  <link rel="stylesheet" href="assets/css/style.css">
  <script type="application/ld+json">
{json.dumps(jsonld, indent=2)}
  </script>
</head>
<body>
  {render_header("home", depth=0)}
  <div class="container">
    <div class="hero-box">
      <div class="author-pill">
        <span>Architect:</span> <strong>Serhii Khylevych</strong> <span>• Kyiv Wartime Operational Context</span>
      </div>
      <h1 class="hero-title" style="margin-top:1rem;">Unmanned Warfare Engine (UWE)</h1>
      <p class="hero-subtitle">
        The Unified Cyber-Physical Framework for Software-Defined Robotic Fleets.<br>
        Replacing human casualties and single bespoke "Wunderwaffen" with an algorithmic, hardware-abstracted containment line.
      </p>
      
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:1rem; margin-top:1.5rem;">
        <div style="background:var(--surface-alt); padding:1rem; border-radius:6px; border:1px solid var(--border);">
          <strong style="color:#58a6ff;">1. Law of Kinematic Primacy</strong>
          <p style="margin:0.25rem 0 0 0; font-size:0.82rem; color:var(--text-muted);">Physical interface strictly dictates domain (L/D, ground pressure, hydrodynamics). No hybrid marketing tropes.</p>
        </div>
        <div style="background:var(--surface-alt); padding:1rem; border-radius:6px; border:1px solid var(--border);">
          <strong style="color:#58a6ff;">2. Law of Hierarchical Containerization</strong>
          <p style="margin:0.25rem 0 0 0; font-size:0.82rem; color:var(--text-muted);">Strict logistics tiers from C0 (Micro/Handheld) to C4 (Strategic Base/CATOBAR). Logistics limits dictate mass.</p>
        </div>
        <div style="background:var(--surface-alt); padding:1rem; border-radius:6px; border:1px solid var(--border);">
          <strong style="color:#58a6ff;">3. Law of Decoupled Lethality</strong>
          <p style="margin:0.25rem 0 0 0; font-size:0.82rem; color:var(--text-muted);">Invariant chassis decoupled from interchangeable payloads and One-Way Mission (OWM) decorators.</p>
        </div>
        <div style="background:var(--surface-alt); padding:1rem; border-radius:6px; border:1px solid var(--border);">
          <strong style="color:#58a6ff;">4. Dual-Read Cognitive Synchronization</strong>
          <p style="margin:0.25rem 0 0 0; font-size:0.82rem; color:var(--text-muted);">Monolithic 6-character token dual-read by human commander and tactical edge AI in microseconds.</p>
        </div>
      </div>
    </div>

    <!-- Top Telemetry KPI Counters Ribbon -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-num">{len(CASES_DATA)}</div>
        <div class="kpi-label">Empirical Benchmarks</div>
        <div class="kpi-sub">Flight & field tests analyzed</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-num">6</div>
        <div class="kpi-label">Physical Domains</div>
        <div class="kpi-sub">Air, Copter, Ground, Sea, Subsea, Orbit</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-num">{len(VENDORS_DATA)}</div>
        <div class="kpi-label">Defense Primes & Labs</div>
        <div class="kpi-sub">Western OEMs & frontline developers</div>
      </div>
      <div class="kpi-card highlight">
        <div class="kpi-num">100%</div>
        <div class="kpi-label">Concept Validation</div>
        <div class="kpi-sub">9 of 9 Laws & Postulates Confirmed</div>
      </div>
    </div>

    <!-- Cross-Domain Operational Spectrum Bar -->
    {spectrum_bar_html}

    <!-- C2 Cyber-Physical Officer Spotlight Banner -->
    <section class="reddit-card" style="border:1px solid #1f6feb; background:linear-gradient(135deg, rgba(31, 111, 235, 0.12) 0%, rgba(22, 27, 34, 0.95) 100%); margin-bottom:2rem; padding:1.5rem;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.75rem;">
        <span class="badge" style="background:#1f6feb; color:#fff; font-size:0.8rem; font-weight:700;">🌟 NEW DOCTRINAL MILESTONE</span>
        <span style="font-size:0.85rem; color:#8b949e;">Multi-Domain C2 Architecture • Kyiv Wartime Baseline</span>
      </div>
      <h2 style="margin:0 0 0.5rem 0; font-size:1.4rem; color:#fff;">
        <a href="c2/officer.html" style="color:#58a6ff; text-decoration:none;">The Cyber-Physical Officer: Human-Machine Symbiosis in UWE</a>
      </h2>
      <p style="margin:0 0 1rem 0; color:#c9d1d9; font-size:0.95rem; line-height:1.6;">
        Beyond "twitch-reflexes": The <strong>Moore-Plumley paradigm</strong>, <strong>APM (300–400)</strong> motor control vs. <strong>CPM (2–3)</strong> sovereign lethal will, the <strong>STDFUA</strong> real-time biometric fail-safe, and the <em>"I Shoot As I Think"</em> zero translation latency doctrine.
      </p>
<div style="display:flex; gap:0.75rem; flex-wrap:wrap; align-items:center;">
        <a href="c2/officer.html" class="badge badge-uav" style="font-size:0.88rem; padding:0.45rem 0.9rem; text-decoration:none;">Read C2 Symbiosis Whitepaper →</a>
        <a href="https://www.linkedin.com/pulse/cyber-physical-officer-human-machine-symbiosis-engine-khylevych-pkjff" target="_blank" rel="noopener" style="color:#8b949e; font-size:0.85rem; text-decoration:none;">View Official Pulse Article ↗</a>
      </div>
    </section>

    <!-- B2B Advisory Callout Banner -->
    <section class="advisory-callout" style="border:1px solid rgba(88, 166, 255, 0.3); background:rgba(13, 17, 23, 0.8); border-radius:8px; padding:1.25rem 1.5rem; margin-bottom:2rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
      <div style="max-width:720px;">
        <span class="badge badge-uav" style="font-size:0.75rem; margin-bottom:0.4rem;">ENGINEERING ADVISORY &amp; ARCHITECTURE AUDIT</span>
        <h3 style="margin:0.25rem 0 0.4rem 0; font-size:1.15rem; color:#fff;">
          Developing an Autonomous Platform or Scaling Production?
        </h3>
        <p style="margin:0; font-size:0.9rem; color:var(--text-muted); line-height:1.5;">
          Get independent systems architecture review, Hardware Abstraction Layer (HAL) design, and cyber-physical stress-testing under strict NDA.
        </p>
      </div>
      <div>
        <a href="consulting.html#contact" class="btn btn-primary" style="font-size:0.9rem; padding:0.6rem 1.2rem; text-decoration:none; display:inline-flex; align-items:center; gap:0.5rem; white-space:nowrap;">
          Request Architecture Briefing →
        </a>
      </div>
    </section>

    <!-- Concept & Laws Empirical Validation Dashboard -->
    <section class="val-dashboard" id="validation-dashboard">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
        <div>
          <h2 style="margin:0; font-size:1.45rem; color:#fff;">📐 Concept & Architectural Laws Empirical Validation Matrix</h2>
          <p style="margin:0.25rem 0 0 0; color:var(--text-muted); font-size:0.9rem;">
            Rigorous verification of UWE theoretical axioms against field telemetry, flight test footage, and Western/Ukrainian OEM datasheets.
          </p>
        </div>
        <div class="badge" style="background:#122616; border-color:#2ea043; color:#3fb950; font-size:0.85rem; padding:0.4rem 0.8rem;">
          STATUS: ALL 9 AXIOMS CONFIRMED (100%)
        </div>
      </div>

      <div class="progress-meter">
        <div class="progress-labels">
          <span style="color:#58a6ff; font-weight:700;">EMPIRICAL VALIDATION PROGRESS</span>
          <span style="color:#3fb950; font-weight:700;">9 OF 9 VERIFIED (100.0%)</span>
        </div>
        <div class="progress-track">
          <div class="progress-fill" style="width: 100%;"></div>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:0.5rem; font-size:0.78rem; color:var(--text-muted);">
          <span>4 Invariant Physical Laws: 4/4 Verified (100%)</span>
          <span>5 Operational Postulates: 5/5 Verified (100%)</span>
        </div>
      </div>

      <h3 style="font-size:1.1rem; color:#58a6ff; margin:1.5rem 0 0.75rem 0; text-transform:uppercase; letter-spacing:0.5px;">
        ⚖️ Part 1: The Four Invariant Laws of UWE (4/4 Confirmed)
      </h3>
      {laws_html}

      <h3 style="font-size:1.1rem; color:#38bdf8; margin:1.5rem 0 0.75rem 0; text-transform:uppercase; letter-spacing:0.5px;">
        🛡️ Part 2: The Five Operational Postulates of Autonomous Warfare (5/5 Confirmed)
      </h3>
      {postulates_html}
    </section>

<!-- Empirical Case Studies Section -->
    <div id="benchmarks" style="margin-bottom:2rem;">
      <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--border); padding-bottom:0.5rem; margin-bottom:1rem;">
        <h2 style="font-size:1.4rem; margin:0;">
          🔬 {len(CASES_DATA)} Empirical Platform Benchmarks & Architectural Mapping
        </h2>
        <span style="font-size:0.85rem; color:var(--text-muted);">Showing <strong id="visible-count" style="color:#fff;">{len(CASES_DATA)}</strong> of {len(CASES_DATA)} platforms</span>
      </div>
      <p style="color:var(--text-muted); font-size:0.95rem; margin-bottom:1.25rem;">
        Scientific-practical stress-testing of western OEMs, Ukrainian frontline prototypes, and global aerospace systems against the 4 Invariant Laws of UWE.
      </p>

      <input type="text" id="case-search" class="search-bar" placeholder="Search {len(CASES_DATA)} benchmarks by platform, token, HAL contract, or vendor (e.g., 'Anduril', 'coaxial', 'MQ-25', 'IVtol')...">
      
      <div class="filter-group-label">Filter by Physical Medium Domain:</div>
      <div class="filter-pills">
        {domain_pills_html}
      </div>

      <div class="filter-group-label">Filter by Defense-Tech OEM / Developer:</div>
      <div class="filter-pills">
        {vendor_pills_html}
      </div>

      <div id="cases-feed">
        {cases_html}
      </div>
    </div>
  </div>
  {render_footer()}
  <script src="assets/js/search.js"></script>
</body>
</html>"""
    write_file("index.html", html)

def build_case_pages():
    for case in CASES_DATA:
        pros_li = "".join(f"<li>{p}</li>" for p in case["advantages"])
        cons_li = "".join(f"<li>{c}</li>" for c in case["vulnerabilities"])
        related_links = "".join(f'<p style="margin:0.25rem 0;"><a href="{r}.html" class="badge badge-hal">Case #{r[:2]} Study →</a></p>' for r in case.get("related", []))
        c2_notice = ""
        if case["domain"] == "C2":
            c2_notice = f"""<div class="lesson-box">
        This benchmark concerns cross-domain orchestration, not a seventh physical domain.
        <a href="../{C2_ARTICLE_PATH}">Read the Joint Cross-Domain Unmanned Operation article →</a>
      </div>"""

        jsonld = {
            "@context": "https://schema.org",
            "@type": "TechArticle",
            "headline": f"UWE Case #{case['id']}: {case['name']} — Cyber-Physical Architectural Analysis",
            "description": f"Empirical evaluation of {case['name']} ({case['token']}) under Hardware Abstraction Layer {case['hal']}. {case['lesson']}",
            "author": {
                "@type": "Person",
                "name": "Serhii Khylevych",
                "jobTitle": "Systems Architect",
                "url": "https://ua.linkedin.com/in/serhii-khylevych-aa152322"
            },
            "datePublished": case["date"],
            "url": f"{BASE_URL}/cases/{case['slug']}.html",
            "keywords": [case['domain'], case['token'], case['hal'], case['vendor'], "UWE Standard", "STANAG 4670 replacement"]
        }

        html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Case #{case['id']}: {html_mod.escape(case['name'])} | UWE Architectural Benchmark</title>
  <meta name="description" content="Technical audit of {case['name']} ({case['token']}). Physical advantages, failure modes, and HAL contract {case['hal']}.">
  <link rel="canonical" href="{BASE_URL}/cases/{case['slug']}.html">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script type="application/ld+json">
{json.dumps(jsonld, indent=2)}
  </script>
</head>
<body>
  {render_header("cases", depth=1)}
  <div class="container" style="max-width:900px;">
    <div style="margin-bottom:1.5rem;">
      <a href="index.html" style="font-size:0.9rem;">← Back to All {len(CASES_DATA)} Benchmarks</a>
    </div>

    <article class="reddit-card">
      <div class="card-meta">
        <span>Author: <strong>Serhii Khylevych</strong></span>
        <span>•</span>
        <span>Date: {case['date']}</span>
        <span>•</span>
        <a href="../{classification_path(case['domain'])}" class="badge badge-{case['domain'].lower()}">{case['domain']}</a>
        <a href="../vendors/index.html#{case['vendor_slug']}" class="badge badge-vendor">{case['vendor']}</a>
      </div>
      <h1 class="hero-title" style="font-size:1.85rem; margin-bottom:1rem;">
        Case #{case['id']}: {case['name']}
      </h1>
      {c2_notice}

      <div class="token-banner">
        <div><strong>Monolithic 6-Character UWE Token:</strong> <code>{case['token']}</code></div>
        <div style="font-size:0.85rem; color:var(--text-muted); margin-top:0.35rem;">{case['token_full']}</div>
      </div>

      <div class="hal-box">
        <div class="hal-title">⚙️ Tested Hardware Abstraction Layer (HAL) Contract: <a href="../hal/index.html#{case['hal']}"><code>{case['hal']}</code></a></div>
        <div style="line-height:1.5;"><em>"{case['hal_def']}"</em></div>
      </div>

      <h3 style="color:#58a6ff; margin-top:1.5rem;">1. Cyber-Physical Kinematic & Energy Analysis</h3>
      <div class="pros-cons-grid">
        <div class="col-pro">
          <h4>🟢 Physical Superiority (Compliance with Law of Kinematics)</h4>
          <ul class="points">{pros_li}</ul>
        </div>
        <div class="col-con">
          <h4>🔴 Engineering Vulnerabilities & Cyber-Physical Limits</h4>
          <ul class="points">{cons_li}</ul>
        </div>
      </div>

      <h3 style="color:#58a6ff; margin-top:1.5rem;">2. Doctrinal Takeaway for Unmanned Warfare</h3>
      <div class="lesson-box">
        <strong>💡 Architectural Lesson for UWE:</strong> {case['lesson']}
      </div>

      <h3 style="color:#58a6ff; margin-top:1.5rem;">3. Primary Proofs & OSINT Verification</h3>
      <div class="citation-box" style="margin-bottom:1.5rem;">
        <div>
          <div><strong>Primary OSINT Evidence:</strong> <a href="{case['source_url']}" target="_blank" rel="noopener">{case['source_name']} ↗</a></div>
          <div style="margin-top:0.35rem; font-size:0.8rem; color:var(--text-muted);">Hardware Platform Manufacturer: <strong>{case['vendor']}</strong></div>
        </div>
        <div>
          <a href="{case['source_url']}" target="_blank" rel="noopener" class="badge badge-hal">Open External Source ↗</a>
        </div>
      </div>

<div style="background:var(--surface-alt); padding:1rem; border-radius:6px; border:1px solid var(--border);">
        <h4 style="margin:0 0 0.5rem 0; color:#fff; font-size:0.9rem;">Cross-Domain Ecosystem Pairings:</h4>
        {related_links}
      </div>

      <!-- Advisory / Architecture Briefing Callout -->
      <div style="margin-top:2rem; padding:1.25rem 1.5rem; background:linear-gradient(135deg, rgba(88, 166, 255, 0.08) 0%, rgba(22, 27, 34, 0.95) 100%); border:1px solid rgba(88, 166, 255, 0.3); border-radius:6px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
        <div style="max-width:680px;">
          <div style="font-size:0.75rem; font-weight:700; color:var(--accent-blue, #58a6ff); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.25rem;">Systems Architecture &amp; HAL Advisory</div>
          <div style="font-size:1.05rem; font-weight:700; color:#fff;">Developing a similar platform or integrating autonomous subsystems?</div>
          <p style="margin:0.25rem 0 0 0; font-size:0.85rem; color:var(--text-muted); line-height:1.4;">
            Engage Principal Systems Architect <strong>Serhii Khylevych</strong> for independent kinematic validation, HAL interface design, and cyber-physical stress-testing under mutual NDA.
          </p>
        </div>
        <div>
          <a href="../consulting.html#contact" class="btn btn-primary" style="font-size:0.88rem; padding:0.55rem 1.1rem; text-decoration:none; white-space:nowrap; display:inline-block;">
            Request Architecture Briefing →
          </a>
        </div>
      </div>
    </article>
  </div>
  {render_footer()}
</body>
</html>"""
        write_file(f"cases/{case['slug']}.html", html)

def build_cases_index():
    cases_html = "\n".join(render_case_card(c, depth=1) for c in CASES_DATA)
    domain_pills_html, vendor_pills_html = render_filter_pills()
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Empirical Case Studies Registry ({len(CASES_DATA)} Validated Platforms) | UWE</title>
  <meta name="description" content="Cumulative registry of all {len(CASES_DATA)} empirical defense-tech systems analyzed under the Unmanned Warfare Engine (UWE) framework.">
  <link rel="canonical" href="{BASE_URL}/cases/index.html">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
  {render_header("cases", depth=1)}
  <div class="container">
    <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--border); padding-bottom:0.5rem; margin-bottom:1rem;">
      <h1 class="hero-title" style="font-size:1.85rem; margin:0;">Empirical Platform Benchmarks ({len(CASES_DATA)} Cases)</h1>
      <span style="font-size:0.85rem; color:var(--text-muted);">Showing <strong id="visible-count" style="color:#fff;">{len(CASES_DATA)}</strong> of {len(CASES_DATA)} platforms</span>
    </div>
    <p style="color:var(--text-muted); margin-bottom:1.5rem;">
      Cross-referencing western OEMs, frontline Ukrainian prototypes, and aerospace systems against the 4 Invariant Laws of UWE.
    </p>

    <input type="text" id="case-search" class="search-bar" placeholder="Search {len(CASES_DATA)} benchmarks by platform, token, HAL contract, or vendor...">
    
    <div class="filter-group-label">Filter by Physical Medium Domain:</div>
    <div class="filter-pills">
      {domain_pills_html}
    </div>

    <div class="filter-group-label">Filter by Defense-Tech OEM / Developer:</div>
    <div class="filter-pills">
      {vendor_pills_html}
    </div>

    <div id="cases-feed">
      {cases_html}
    </div>
  </div>
  {render_footer()}
  <script src="../assets/js/search.js"></script>
</body>
</html>"""
    write_file("cases/index.html", html)

def render_domain_taxonomy_section(code):
    tax = DOMAINS_TAXONOMY.get(code, {})
    if not tax:
        return ""
    
    # 1. Historical Doctrine
    hist_html = f"""
    <section class="reddit-card" style="border-left:4px solid var(--accent);">
      <h3 style="color:#58a6ff; margin-top:0;">1. The Historical Doctrine: Conceptual Precedent & Lineage</h3>
      <p style="font-size:0.95rem; line-height:1.6; color:#e6edf3;"><strong>{tax['history_title']}</strong></p>
      <div style="font-size:0.9rem; line-height:1.6; color:var(--text-muted);">{tax['history_body']}</div>
    </section>
    """

    # 2. Bureaucratic Trap
    trap_html = f"""
    <section class="reddit-card" style="border-left:4px solid var(--red);">
      <h3 style="color:#f85149; margin-top:0;">2. The Bureaucratic Trap & Empirical De-Noising</h3>
      <p style="font-size:0.95rem; line-height:1.6; color:#e6edf3;"><strong>{tax['trap_title']}</strong></p>
      <div style="font-size:0.9rem; line-height:1.6; color:var(--text-muted);">{tax['trap_body']}</div>
    </section>
    """

    # 3. 7 Universal Vectors
    vectors_li = "".join(f"<li style='margin-bottom:0.75rem;'><strong style='color:#58a6ff;'>{v['code']}: {v['name']}</strong><br><span style='color:var(--text-muted); font-size:0.88rem;'>{v['desc']}</span></li>" for v in tax['vectors'])
    vectors_html = f"""
    <section class="reddit-card" style="border-left:4px solid var(--green);">
      <h3 style="color:#3fb950; margin-top:0;">3. The 7 Universal Operational Vectors</h3>
      <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:1rem;">Universal mission profiles decoupling airframe/hull kinematics from tactical payload kits:</p>
      <ul style="padding-left:1.25rem; font-size:0.92rem;">
        {vectors_li}
      </ul>
      <div style="background:#0d1117; border:1px dashed var(--border); padding:0.85rem 1rem; border-radius:6px; margin-top:1rem;">
        <strong style="color:#e6edf3; font-size:0.88rem;">⚡ 300-Second Multi-Domain Combat Loop:</strong>
        <p style="color:var(--text-muted); font-size:0.85rem; margin:0.35rem 0 0 0; line-height:1.5;">{tax['combat_loop']}</p>
      </div>
    </section>
    """

    # 4. Monolithic 6-Character Matrix
    matrix_html = f"""
    <section class="reddit-card" style="border-left:4px solid var(--purple);">
      <h3 style="color:#d2a8ff; margin-top:0;">4. The 6-Character Cyber-Physical Matrix: <code>{tax['matrix_token']}</code></h3>
      <div class="token-banner" style="font-size:1.05rem;">
        <strong>Monolithic UWE Standard Token:</strong> <code>{tax['matrix_token']}</code>
      </div>
      <div style="overflow-x:auto; margin-top:1rem;">
        <table style="width:100%; border-collapse:collapse; font-size:0.85rem; text-align:left;">
          <thead>
            <tr style="border-bottom:2px solid var(--border); color:#58a6ff;">
              <th style="padding:0.5rem 0.75rem;">Octet 1: {tax['octet1_title']}</th>
              <th style="padding:0.5rem 0.75rem;">Octet 2: {tax['octet2_title']}</th>
              <th style="padding:0.5rem 0.75rem;">Octet 3: {tax['octet3_title']}</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border); vertical-align:top; color:var(--text-muted);">
              <td style="padding:0.6rem 0.75rem;">{tax['octet1_content']}</td>
              <td style="padding:0.6rem 0.75rem;">{tax['octet2_content']}</td>
              <td style="padding:0.6rem 0.75rem;">{tax['octet3_content']}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
    """

    # 5. Mobile Benchmark Cards
    cards_html = ""
    for b in tax['benchmarks']:
        cards_html += f"""
        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1rem; margin-bottom:1rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem; flex-wrap:wrap; gap:0.5rem;">
            <strong style="color:#fff; font-size:1rem;">{b['role']}</strong>
            <span class="badge badge-hal" style="font-family:var(--code-font); font-size:0.85rem;">{b['token']}</span>
          </div>
          <p style="margin:0.25rem 0; font-size:0.85rem; color:#58a6ff;"><strong>OEM Platform:</strong> {b['platform']}</p>
          <p style="margin:0.25rem 0; font-size:0.85rem; color:var(--text-muted);"><strong>Kinematics & Envelope:</strong> {b['kinematics']}</p>
          <p style="margin:0.25rem 0; font-size:0.85rem; color:var(--text-muted);"><strong>Logistics & Power:</strong> {b['logistics']}</p>
          <p style="margin:0.25rem 0; font-size:0.85rem; color:var(--text-muted);"><strong>Autonomy & C2:</strong> {b['autonomy']}</p>
          <div style="margin-top:0.5rem; font-size:0.83rem; color:#3fb950;"><strong>Kill Web Function:</strong> {b['kill_web']}</div>
        </div>
        """
    benchmarks_section = f"""
    <section class="reddit-card" style="border-left:4px solid var(--cyan);">
      <h3 style="color:#7ee787; margin-top:0;">5. Mobile-First Benchmark Cards</h3>
      <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:1rem;">Structured vertical cards benchmarked against frontline combat systems and global defense primes:</p>
      {cards_html}
    </section>
    """

    # 6. HAL Contract & Governing Physics
    hal_section = f"""
    <section class="reddit-card" style="border-left:4px solid var(--amber);">
      <h3 style="color:#e3b341; margin-top:0;">6. Hardware Abstraction Layer (HAL) & Governing Physics</h3>
      <div class="hal-box">
        <div class="hal-title">⚙️ Primary HAL Contract: <code>{tax['hal_contract']}</code></div>
        <p style="margin:0.35rem 0; font-size:0.88rem; line-height:1.5;">{tax['hal_contract_desc']}</p>
      </div>
      <div style="background:#0d1117; border:1px solid var(--border); padding:1rem; border-radius:6px; margin-top:1rem;">
        <strong style="color:#58a6ff; font-size:0.9rem;">📐 Cyber-Physical Governing Formula:</strong>
        <p style="font-family:var(--code-font); color:#fff; font-size:0.95rem; margin:0.5rem 0; background:#161b22; padding:0.5rem 0.75rem; border-radius:4px; overflow-x:auto;">{tax['governing_formula']}</p>
        <p style="font-size:0.85rem; color:var(--text-muted); margin:0.35rem 0 0 0; line-height:1.5;">{tax['formula_desc']}</p>
      </div>
    </section>
    """

    # 7. Cross-Domain C2 Officer Integration
    c2_section = f"""
    <section class="reddit-card" style="border-left:4px solid var(--accent); background:rgba(31, 111, 235, 0.05);">
      <h3 style="color:#58a6ff; margin-top:0;">7. C2 Officer Symbiosis & Autonomous Kill Web Integration</h3>
      <p style="font-size:0.92rem; line-height:1.6; color:#e6edf3; margin-bottom:0.75rem;">
        How <strong>{code}</strong> autonomous fleets integrate into the human-machine command loop under the 
        <a href="../c2/officer.html" style="color:#58a6ff; font-weight:600;">Moore-Plumley Doctrine</a>:
      </p>
      <div style="display:flex; gap:0.5rem; flex-wrap:wrap; align-items:center; margin-bottom:0.75rem;">
        <span class="badge" style="background:#161b22; border:1px solid var(--border); color:#d2a8ff;">ED25519 CPM Fire Release</span>
        <span class="badge" style="background:#161b22; border:1px solid var(--border); color:#7ee787;">300-400 APM Motor Control</span>
        <span class="badge" style="background:#161b22; border:1px solid var(--border); color:#ffa657;">STDFUA Biometric Sentinel</span>
      </div>
      <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.5; margin:0;">
        Kinematic optimization and inter-platform target handoffs are managed by the engine at machine speed, while lethal authorization remains strictly anchored to the sovereign human commander under the <em>"I Shoot As I Think"</em> zero translation latency doctrine.
        <a href="../c2/officer.html" style="color:#58a6ff; margin-left:0.5rem; font-weight:600;">Explore C2 Officer Doctrine →</a>
      </p>
    </section>
    """

    return hist_html + trap_html + vectors_html + matrix_html + benchmarks_section + hal_section + c2_section

DOMAINS_TAXONOMY = {
    "UAV": {
        "history_title": "Cossack Beket Signal Pyramids & Steppe Rocket Batteries (16th–18th Century)",
        "history_body": "The Zaporozhian Sich defended a 1,000-km open steppe frontier without stone fortresses by constructing an automated, distributed optical early-warning network ('Figury'). Trihedral tar-soaked beacons on burial mounds transmitted alarm signals from the Black Sea to Kyiv in 20-30 minutes—a deterministic zero-latency optical relay mesh centuries before LEO satellites. Offensively, Cossacks deployed mobile rocket stanchions and multi-barrel 'organky', prioritizing dispersion and fire rate over static artillery armor.",
        "trap_title": "The 'Alt-Endurance' Trap (STANAG 4670) & The Heavy Gimbal Paradox",
        "trap_body": "NATO STANAG 4670 / DoD Class I-III categories rely on altitude and endurance—metrics that create massive radar beacons (Bayraktar TB2, MQ-9) easily engaged by S-300V4, Buk-M3, and low-cost loitering SAMs (Project 358). Furthermore, observing from 60-80 km standoff requires 50-kg optical turrets (Wescam MX-15/20) under Johnson criteria (f = 800-1200 mm), inflating MTOW to 1,500-5,000 kg and cost to $20M+. UWE shifts mass to the ground-clutter layer (0-300 m) beneath the radar horizon (R_radar ≈ 4.12(√hr + √ht)), replacing heavy glass with 35-50mm lenses and onboard Edge-AI computer vision (ATR).",
        "vectors": [
            {"code": "AL-PE-HR", "name": "Standoff C4ISR & Tactical Airborne Relay", "desc": "Orbiting 60-100 km behind friendly lines; directional phased RF and LEO satellite gateway unifying the tactical frontline mesh."},
            {"code": "AH-EE-MO", "name": "Active Emitter Stimulator / Stand-in Decoy", "desc": "High-speed airframe emulating cruise missile RCS; forces SAM radars (9S18 Kupol, 9S36) to radiate and expend interceptors."},
            {"code": "AH-EA-MO", "name": "Ground-Clutter Low-Altitude Loitering Strike", "desc": "Terrain-following cruise (30-150 m) under the radar horizon with terminal optical ATR dive onto high-value armor and air defense."},
            {"code": "AL-EA-MA", "name": "Extended-Range Tactical Interdiction", "desc": "High-efficiency gliding (100-180 km/h) over 100-300 km depths; interdicting logistics convoys and ammunition nodes."},
            {"code": "AL-JA-TA", "name": "Deep Strategic Kinetic Penetration", "desc": "Long-range (500-1,500+ km) one-way strike against refineries, defense plants, and airbases with anti-jam CRPA-GNSS and TERCOM."},
            {"code": "AL-TH-HR", "name": "Autonomous Aerial Tanker & Power Lifeline", "desc": "Dispersed airborne refueling and battery-swapping orbit multiplying loiter time without forward strip turnaround."},
            {"code": "AS-CM-HR", "name": "Collaborative Combat Aircraft (Loyal Wingman)", "desc": "Transonic Mach 0.95, 9G escort for crewed fighters; carrying forward AESA sensors and internal missile bays (Fury, MQ-28)."}
        ],
        "combat_loop": "T+000s: Standoff Relay (AL-PE-HR) detects radar emitter. T+045s: Decoys (AH-EE-MO) bait SAM illumination. T+180s: Low-altitude strike UAVs (AH-EA-MO) pop up under radar horizon. T+260s: Edge-AI ATR initiates radio-silent dive. T+300s: Target destroyed.",
        "matrix_token": "[ A H ]  -  [ D E ]  -  [ T C ]",
        "octet1_title": "Aerodynamic Horizon & Wing Regime [AH]",
        "octet1_content": "<b>A: Horizon</b><br>• A: Atmospheric (0-3 km)<br>• S: Stratospheric (12-25 km)<br>• T: Transonic (M 0.7-0.98)<br>• H: Hypersonic (M 5.0+)<br><br><b>H: Wing Planform</b><br>• L: High-Aspect (AR≥20)<br>• D: Delta / BWB<br>• S: Swept High-Speed<br>• F: Tailless Flying Wing<br>• C: Canard / Foldable<br>• V: VTOL Crossfade",
        "octet2_title": "Containerization & Powerplant [DE]",
        "octet2_content": "<b>D: Deployment</b><br>• H: Hand / Bungee<br>• C: Canister / Pneumatic<br>• R: Rail / JATO Boost<br>• L: Light Dispersed Runway<br>• I: Fixed Infrastructure<br><br><b>E: Powerplant</b><br>• E: Battery Electric<br>• P: Piston ICE (Rotax)<br>• T: Turbojet / Turbofan<br>• H: Hybrid Electric/Gas<br>• R: Rocket Solid/Liquid",
        "octet3_title": "Tactical Autonomy & Comms [TC]",
        "octet3_content": "<b>T: Tactical Posture</b><br>• P: Passive Orbit / Relay<br>• A: Active Attack / Strike<br>• M: Mass Swarm Mesh<br>• S: Sleeper / Standby<br>• D: Decoy / Penetrator<br>• H: Collaborative Manned<br><br><b>C: Comms Gateway</b><br>• R: Directional Phased RF<br>• S: LEO Satellite (Starlink)<br>• F: Fiber-Optic Tether<br>• Q: Radio-Silent Optical ATR<br>• L: Laser Free-Space Link",
        "benchmarks": [
            {"role": "Standoff Airborne C4ISR & Relay Orbit", "token": "UAV: AL-PE-HR", "platform": "TEKEVER AR5 / MQ-9 Reaper", "kinematics": "High-aspect glider (AR≥20) | Ceiling 8,000-12,000m | L/D > 22", "logistics": "Dispersed/Fixed Runway (D: I) | Turbocharged ICE (E: P, 24-30h)", "autonomy": "Autonomous waypoint patrol | Directional Ku/Ka SATCOM & SDR", "kill_web": "Vector 1: Primary C4ISR backbone and EW gateway outside SAM reach."},
            {"role": "Ground-Clutter Low-Altitude Strike", "token": "UAV: AH-EA-MO", "platform": "WB Group Warmate / Switchblade 600", "kinematics": "Canard folding wing | Cruise 120-150 km/h, terminal dive 220 km/h", "logistics": "Pneumatic canister tube (D: C) | Li-ion electric motor (E: E)", "autonomy": "Edge-AI ATR terminal lock | Radio-silent terminal flight (C: Q)", "kill_web": "Vector 3: Surgical destruction of radars and armor at 0-300m altitude."},
            {"role": "Collaborative Combat Aircraft (Loyal Wingman)", "token": "UAV: AS-CM-HR", "platform": "Anduril Fury (YFQ-44A) / Boeing MQ-28", "kinematics": "Stealth swept wing | Transonic Mach 0.95 | Ceiling 15,000m | 9G sustained", "logistics": "Dispersed runway / rocket rail | Williams turbofan (E: T)", "autonomy": "Lattice OS autonomous teaming | AESA phased array & MADL bus", "kill_web": "Vector 7: Escort strike packages, absorb missile salvos, forward missile magazine."}
        ],
        "hal_contract": "IVtolTransitionDrive / IFixedWingKinematics",
        "hal_contract_desc": "Governs dynamic crossfade transition from vertical hover to aerodynamic wing lift (SetTransitionRatio(α)) and validates boundary layer flight envelopes under nap-of-the-earth radar clutter.",
        "governing_formula": "E_total = ∫ P_hover dt + ∫ [½ ρ V³ S (C_D0 + C_L² / (π·AR·e))] dt + ∫ P_dash dt",
        "formula_desc": "Piecewise multi-phase aerodynamic energy equation: hover disc power scales with (T/A)^0.5, while cruise power is minimized at high aspect ratio AR and low zero-lift drag C_D0."
    },
    "UCV": {
        "history_title": "Cossack Pikash Darts & Hand Caltrops ('Rogulky')",
        "history_body": "Zaporozhian Cossacks mastered close-quarters kinetic harassment through lightweight, hand-thrown armor-piercing iron darts ('pikash') and multi-spiked area-denial caltrops ('rogulky'). These weapons converted individual soldier agility into lethal kinetic breaches against heavy cavalry armor—the exact historical precursor to modern high-acceleration multirotor kinetic strikes.",
        "trap_title": "Conflating Combat Rotorcraft with Hobbyist Slang ('FPV')",
        "trap_body": "'FPV' (First Person View) describes a consumer analog video headset, NOT a combat vehicle class. Conflating terminal kinetic interceptors with commercial hobby toys blinds defense procurement to essential cyber-physical laws: rotor disc loading (T/A), advance ratio (μ = V / (Ω·R)), retreating blade stall, and electronic counter-countermeasures (ECCM).",
        "vectors": [
            {"code": "CH-EE-AR", "name": "Terminal Precision Kinetic Interceptor", "desc": "High-acceleration 7-10\" frame; Mach 0.15-0.20 terminal dive with modular shaped charge."},
            {"code": "CL-EE-AR", "name": "Over-the-Horizon Indirect Strike", "desc": "Ballistic pitch delivery from behind tree lines using automated terminal guidance."},
            {"code": "CM-EE-AQ", "name": "Heavy Armor Breacher / Top-Attack Munition", "desc": "Heavy octocopter dropping thermobaric and tandem anti-tank ordnance on engine decks."},
            {"code": "CH-EE-AF", "name": "Fiber-Optic Electronic-Warfare Immune Penetrator", "desc": "Spooled micro-optical glass fiber (5-20 km); 100% immune to EW jammers, zero RF footprint."},
            {"code": "CT-GE-PR", "name": "Tethered Persistent Airborne Sentry", "desc": "Ground-powered micro-rotorcraft hovering 100m for 72+ hours as persistent radar/EW mast."},
            {"code": "CS-EE-SR", "name": "Perch-and-Listen Ambush Sleeper", "desc": "Dormant rooftop or tree-branch perching; activates motors only upon acoustic acoustic trigger."},
            {"code": "CH-EE-MA", "name": "Autonomous Anti-Air Drone Hunter", "desc": "Machine-vision high-speed interceptor engaging hostile reconnaissance UAVs at 180+ km/h."}
        ],
        "combat_loop": "T+000s: Ground acoustic sensor trips. T+015s: Sleeper UCV (CS-EE-SR) awakens. T+040s: Fiber-optic strike UCV (CH-EE-AF) launched. T+090s: Target armor acquired visually. T+110s: Kinetic breach confirmed.",
        "matrix_token": "[ C H ]  -  [ D E ]  -  [ T C ]",
        "octet1_title": "Copter Horizon & Rotor Architecture [CH]",
        "octet1_content": "<b>C: Horizon</b><br>• C: Micro-Tactical (0-50m)<br>• L: Low-Altitude (0-300m)<br>• M: Medium Urban (0-1 km)<br>• H: High-Ceiling (up to 4 km)<br><br><b>H: Rotor Layout</b><br>• Q: Quadrotor Standard<br>• X: Coaxial High-Density<br>• O: Octocopter Heavy-Lift<br>• H: Hexacopter Redundant",
        "octet2_title": "Deployment & Battery C-Rate [DE]",
        "octet2_content": "<b>D: Container</b><br>• H: Hand-Thrown / Backpack<br>• T: Tube / Vehicle Rack<br>• M: Mobile Mothership<br><br><b>E: Energy Bus</b><br>• E: High-Rate LiPo (60-120C)<br>• S: Solid-State Battery<br>• H: Micro-Hybrid Generator<br>• T: Tethered Ground Line",
        "octet3_title": "Guidance Autonomy & Comms [TC]",
        "octet3_content": "<b>T: Tactical Mode</b><br>• A: Direct Kinetic Impact<br>• D: Bomb Drop / Retrievable<br>• P: Persistent Orbit<br>• S: Perched Sleeper<br><br><b>C: Link Security</b><br>• R: Analog/Digital SDR<br>• F: Spooled Glass Fiber<br>• Q: Radio-Silent Optical ATR<br>• M: Swarm Mesh Relay",
        "benchmarks": [
            {"role": "Precision Kinetic Interceptor", "token": "UCV: CH-EE-AR", "platform": "Frontline 10\" Tactical Strike Quad", "kinematics": "Thrust-to-weight > 8:1 | Terminal speed 180 km/h | Zero stall speed", "logistics": "Soldier backpack (D: H) | 6S Li-ion/LiPo (E: E, 15 min flight)", "autonomy": "Optical ATR lock-on | Frequency-hopping SDR 700-1000 MHz", "kill_web": "Vector 1: Precision armor and trench breach at 5-15 km radius."},
            {"role": "EW-Immune Fiber Penetrator", "token": "UCV: CH-EE-AF", "platform": "Frontline Fiber-Optic Guided Copter", "kinematics": "Rigid carbon frame | 15 km glass-fiber spool | Zero telemetry lag", "logistics": "Dispersed soldier launch (D: H) | High-drain LiPo (E: E)", "autonomy": "Human-in-the-loop 4K video | Zero RF emission, jammer-proof", "kill_web": "Vector 4: Defeating EW-protected electronic warfare domes."},
            {"role": "Heavy Coaxial Maritime/Land Carrier", "token": "UCV: CL-PE-HR", "platform": "BAE / Certo CAPSTONE Coaxial", "kinematics": "Dual contra-rotating coaxial rotors | Disc loading T/A > 35 kg/m²", "logistics": "Deck davit / truck bed | Heavy fuel piston generator (E: P)", "autonomy": "Autonomous precision shipboard landing | Encrypted mesh SDR", "kill_web": "Vector 3: Logistics resupply and heavy torpedo/sensor carriage."}
        ],
        "hal_contract": "IFastInterdictor / IRotorcraftDynamics",
        "hal_contract_desc": "Controls high-rate motor ESC telemetry (DShot1200), computes aerodynamic advance ratio μ to prevent retreating blade stall during 50 m/s terminal sprints.",
        "governing_formula": "P_rotor = [T^{3/2} / (2 ρ A)^{1/2}] · (1 / η_figure_of_merit) + ½ ρ V³ S_fuselage C_D_parasitic",
        "formula_desc": "Rotor momentum theory: induced hover power requires maximizing disc area A, while high-speed forward dashes are limited by fuselage parasitic drag and motor C-rate limits."
    },
    "UGV": {
        "history_title": "Chumak Tabor (Wagenburg) & Cossack Mobile Field Fortresses",
        "history_body": "15th-18th century Ukrainian Chumaks and Cossacks organized heavy trade and military convoys into 'Tabors'—interconnected wooden freight wagons forming an impenetrable, self-defending mobile perimeter. In open terrain, the Tabor functioned as a modular, terrain-conforming armored ring capable of dynamic repositioning, defending against cavalry charges without static castle walls.",
        "trap_title": "Amateur Slang ('Vozyk') & Motor kW vs Bekker Soil Mechanics",
        "trap_body": "Calling military ground robotics 'vozyky' (carts) reduces MilTech to hobby gardening. Marketing claims boast '10-tonne towing' based on electric motor kilowatt ratings while completely ignoring Bekker-Wong soil mechanics: drawbar pull is bounded by soil shear strength (F_pull = A·c + W·tanφ), not motor torque. Without adequate ground contact area, high-torque electric motors merely dig wheels into viscous Ukrainian black soil (chernozem).",
        "vectors": [
            {"code": "WL-EE-PR", "name": "High-Threat Casualty Evacuation (CASEVAC)", "desc": "Low-profile armored litter carrier evacuating wounded under direct fire without exposing personnel."},
            {"code": "WL-HE-PR", "name": "Forward Munition & Energy Resupply Lifeline", "desc": "Autonomous payload delivery traversing artillery-cratered mud corridors at 15-25 km/h."},
            {"code": "WT-EE-AR", "name": "Remote Kinetic Turret / Ambush Platform", "desc": "Stabilized heavy machine gun (12.7mm) or anti-tank missile carrier with low acoustic signature."},
            {"code": "TP-DE-MR", "name": "Combat Breaching & Route Clearance", "desc": "Tracked heavy chassis with flails, rollers, and explosive line charges clearing minefields."},
            {"code": "WP-DE-TR", "name": "Heavy Artillery Prime Mover", "desc": "High drawbar-pull amphibious tractor towing 155mm howitzers across swamp and deep snow."},
            {"code": "WS-EE-SR", "name": "Ground Sensor Emplacement & Picket", "desc": "Camouflaged seismic, acoustic, and thermal sensor anchor loitering for weeks in dormant posture."},
            {"code": "WL-EE-MR", "name": "Distributed Anti-Armor Minelayer", "desc": "Rapid autonomous dispersal of anti-tank bottom mines across anticipated enemy assault axes."}
        ],
        "combat_loop": "T+000s: Seismic sensor detects tank column. T+030s: Ambush UGV (WT-EE-AR) raises mast camera. T+075s: Anti-tank guided missile launched. T+120s: Minelayer UGV (WL-EE-MR) deploys flank barrier. T+240s: Withdrawal under smoke.",
        "matrix_token": "[ W P ]  -  [ D E ]  -  [ T C ]",
        "octet1_title": "Running Gear & Ground Pressure [WP]",
        "octet1_content": "<b>W: Running Gear</b><br>• W: All-Terrain Wheeled (4x4, 6x6)<br>• T: Continuous Tracked (Rubber/Steel)<br>• A: Articulated Two-Section<br>• L: Quadruped Legged / Bio<br><br><b>P: Ground Pressure</b><br>• L: Ultra-Low (<0.2 kg/cm²)<br>• M: Medium Tactical (0.2-0.5 kg/cm²)<br>• H: Heavy Armored (>0.5 kg/cm²)",
        "octet2_title": "Logistics Tier & Powerplant [DE]",
        "octet2_content": "<b>D: Carrier Class</b><br>• C1: Man-Portable (<100 kg)<br>• C2: Light Tactical (100-1,000 kg)<br>• C3: Heavy Operational (1-5 tonnes)<br>• C4: Strategic Prime Mover (>5t)<br><br><b>E: Powerplant</b><br>• E: Pure Electric (Battery)<br>• H: Diesel-Electric Hybrid<br>• D: Heavy Fuel Diesel ICE",
        "octet3_title": "Autonomy Doctrine & Signal [TC]",
        "octet3_content": "<b>T: Tactical Posture</b><br>• P: Patrol & Transport<br>• A: Active Kinetic Combat<br>• M: Breaching / Demining<br>• S: Dormant Surveillance<br><br><b>C: Signal Backbone</b><br>• R: Mesh Radio SDR<br>• F: Spooled Fiber-Optic Cable<br>• S: LEO Satellite (Starlink)<br>• Q: Optical Visual Odometry",
        "benchmarks": [
            {"role": "Articulated Off-Road Scout & Carrier", "token": "UGV: GL-EP-WR", "platform": "Frontline НРК SlimAk", "kinematics": "Articulated 2-section frame | Passive roll compliance | Eliminates skid-steer scrubbing", "logistics": "Trailer / pickup bed (D: C1) | Electric battery (E: E, 6h autonomy)", "autonomy": "Mesh RF remote drive | Low acoustic and thermal signature", "kill_web": "Vector 2: Silent CASEVAC and ammo delivery through trenches and craters."},
            {"role": "Heavy Amphibious Prime Mover", "token": "UGV: WL-DE-TR", "platform": "UNEX ABRIS Amphibious Tractor", "kinematics": "8x8 high-displacement wheels | Ground pressure 0.18 kg/cm² | Amphibious swim", "logistics": "Heavy flatbed transport (D: C3) | Turbocharged diesel-electric hybrid (E: H)", "autonomy": "Autonomous convoy follow-me | High drawbar pull for 155mm howitzers", "kill_web": "Vector 5: Artillery displacement and heavy recovery through muddy floodplains."},
            {"role": "Tracked Combat Weapon Carrier", "token": "UGV: TL-HE-AR", "platform": "Milrem Robotics THeMIS", "kinematics": "Dual low-profile rubber tracks | Low ground pressure 0.25 kg/cm²", "logistics": "Air-transportable / truck (D: C2) | Diesel-electric hybrid bus (E: H)", "autonomy": "MIFIK autonomous waypoint navigation | 12.7mm stabilized turret", "kill_web": "Vector 3: Mobile ambush line and automated perimeter defense."}
        ],
        "hal_contract": "IArticulatedChassis / IGroundMobility",
        "hal_contract_desc": "Decouples passive central roll conformity from active yaw steering hydraulics, computing dynamic wheel slip ratios across Bekker soil sinkage gradients.",
        "governing_formula": "F_drawbar = A · c + W · tan(φ) - [k_c/b + k_φ] · (z^{n+1} / (n + 1))",
        "formula_desc": "Bekker-Wong soil mechanics: traction force is governed by cohesive shear c and internal friction angle φ, minus compaction resistance scaling with sinkage depth z and wheel width b."
    },
    "USV": {
        "history_title": "Zaporozhian Chaika (Lapstrake Clinker) & The Monitor Warning (1862)",
        "history_body": "16th-17th century Cossack naval fleets operated clinker-built 'Chaikas' (60 ft, 50-70 crew) constructed with overlapping oak and linden planks. Chaikas featured bundles of reeds strapped along the gunwales ('remi') providing reserve buoyancy, roll dampening, and unsinkability in heavy Black Sea waves while maintaining a razor-thin visual freeboard that evaded Ottoman galleys. In 1862, the Battle of Hampton Roads proved that small, low-freeboard armored craft render high-sided wooden fleet flagships obsolete overnight.",
        "trap_title": "The British Admiralty Rating Trap & Speedboat Conversion Myth",
        "trap_body": "Traditional navies categorize surface ships by displacement tonnage, armor thickness, and gun caliber—a colonial fleet dogma that paralyzed the Russian Black Sea Fleet. Conversely, converting civilian fiberglass planing speedboats into military drones fails in open seas: high-speed planing into Sea State 4+ generates extreme vertical accelerations (G_z > 6-8g), snapping composite stringers and destroying optical gimbal gyros. UWE mandates slender, wave-piercing displacement or semi-submersible hulls.",
        "vectors": [
            {"code": "AH-PE-AQ", "name": "Littoral Long-Range Kinetic Interdictor", "desc": "Low-RCS wave-piercing surface hull delivering 300-500 kg shaped warheads against capital ships."},
            {"code": "AL-HE-MR", "name": "Anti-Air Drone Carrier & Mothership", "desc": "Deploying short-range air-defense missile rails or FPV interceptors to neutralize attack helicopters."},
            {"code": "AW-DE-PS", "name": "Slender Wave-Piercing Hydrographic Sentry", "desc": "High-efficiency slender monohull with drop keel maintaining persistent ASW sonar patrol for 30+ days."},
            {"code": "AH-PE-MA", "name": "Autonomous Straits Interdiction Gate", "desc": "Swarming surface interceptors executing automated chokepoint blockades in contested maritime narrows."},
            {"code": "AL-DE-PR", "name": "Anti-Submarine Warfare (ASW) Dipping Node", "desc": "Deploying active/passive dipping sonars and lightweight torpedoes against hostile submersibles."},
            {"code": "AM-EE-MR", "name": "Mine Countermeasures (MCM) Shallow Sweeper", "desc": "Acoustic and magnetic signature sweeper detonating seabed mines without risking manned minesweepers."},
            {"code": "AL-DE-TR", "name": "Dispersed Blockade-Running Logistics Transporter", "desc": "High-speed night transit delivering ammunition, fuel, and batteries to besieged coastal islands."}
        ],
        "combat_loop": "T+000s: Satellite radar detects enemy frigate. T+060s: Surface wolfpack (AH-PE-AQ) disperses. T+180s: Pincer convergence initiated. T+240s: Anti-air drone (AL-HE-MR) counters naval helicopter. T+300s: Synchronized hull breach confirmed.",
        "matrix_token": "[ A H ]  -  [ D E ]  -  [ P C ]",
        "octet1_title": "Architecture & Hull Hydrodynamics [AH]",
        "octet1_content": "<b>A: Architecture</b><br>• P: High-Speed Planing<br>• W: Wave-Piercing Slender<br>• S: Semi-Submersible Low-Freeboard<br>• C: Hydrofoil Catamaran<br><br><b>H: Sea State Survivability</b><br>• 1: Sea State 1-2 (Calm)<br>• 3: Sea State 3-4 (Moderate, 1.5m)<br>• 5: Sea State 5-6 (Rough, 3-4m)<br>• 7: Sea State 7+ (Survival)",
        "octet2_title": "Containerization & Powerplant [DE]",
        "octet2_content": "<b>D: Carrier Class</b><br>• T: Trailer / Beach Launch<br>• V: Vessel Davit / Crane<br>• B: Bunker Coastal Pen<br><br><b>E: Powerplant</b><br>• P: Gasoline Waterjet ICE<br>• D: Marine Diesel Inboard<br>• H: Diesel-Electric Hybrid<br>• S: Solar-Wind Auxiliary",
        "octet3_title": "Mission Posture & Signal Backbone [PC]",
        "octet3_content": "<b>P: Operational Posture</b><br>• A: Direct Kinetic Impact (OWM)<br>• R: Reusable Sensor / Weapon Launch<br>• S: Persistent Sleeper Loiter<br><br><b>C: Communications Media</b><br>• S: LEO Satellite (Starlink/Kymeta)<br>• R: High-Bandwidth RF SDR<br>• Q: Optical Visual Horizon ATR<br>• L: Laser Coastal Crosslink",
        "benchmarks": [
            {"role": "Littoral Kinetic Interdictor", "token": "USV: AH-PE-AQ", "platform": "Magura V5 / Sea Baby", "kinematics": "Low-freeboard wave-cleaving hull | Speed 40+ knots | Range > 800 km", "logistics": "Trailer beach slipway (D: T) | High-output marine gasoline engine (E: P)", "autonomy": "Dual Starlink SATCOM + optical backup | Redundant electro-hydraulic steering", "kill_web": "Vector 1: Strategic maritime sea-denial and capital warship sinking."},
            {"role": "Slender Wave-Piercing Hydrographic Sentry", "token": "USV: AW-DE-PS", "platform": "Exail DriX H-9 / Oryx O-16", "kinematics": "Slender wave-piercing keel | Sea State 5 stable | Roll-damping fin ballast", "logistics": "Davit crane / mothership (D: V) | Marine diesel inboard (E: D, 10-30 days)", "autonomy": "Gondola drop-keel sonar bus | Anti-collision radar and Starlink mesh", "kill_web": "Vector 3: High-resolution ASW hydrography and acoustic submarine tracking."}
        ],
        "hal_contract": "ISurfacePlanner / IMarineKinematics",
        "hal_contract_desc": "Computes dynamic vertical slam acceleration G_z across incoming wave spectra, automatically trimming interceptor pitch to prevent slamming structural delamination.",
        "governing_formula": "G_z = c · [V² / B] · [tan(β) / (1 + H_w / L)]",
        "formula_desc": "Savitsky planing impact formula: vertical g-shock scales with velocity squared V² and deadrise angle β, inversely proportional to beam B and hull length ratio."
    },
    "UUV": {
        "history_title": "Cossack 'Pirnachka' Paradigm (Zhelekhivskyi, 1886) & Renaissance Engineering",
        "history_body": "Documented in Yevhen Zhelekhivskyi's 1886 Ukrainian-German Dictionary as 'Kalbsmagen' (calf's stomach), the Cossack Pirnachka was an open Chaika hull completely enclosed with fat-treated, watertight leather. The craft managed internal pressure and fluid ballast like an organic bladder, submerging to reed snorkel depth to evade Ottoman shore artillery—synchronous with William Bourne (1578) and Cornelis Drebbel (1620) Thames submarine trials.",
        "trap_title": "Hull Form-Factor Dogma vs Hydrostatic Depth Horizons",
        "trap_body": "Classifying submersibles by geometric shape (torpedo tube vs box) misses the central physical reality: operational depth horizon dictates everything. Hydrostatic pressure scales at 1 atm per 10m depth (P = ρgh), demanding exponentially thicker titanium, steel, or ceramic pressure vessels that consume internal payload volume and restrict battery capacity. UWE classifies submersibles strictly by depth layers (D0 Surface to D6 Hadal).",
        "vectors": [
            {"code": "DA-RE-AQ", "name": "Dynamic Kinetic Interdictor / Undersea Strike", "desc": "Sub-surface torpedo-delivered kinetic penetrator neutralizing naval hulls from beneath."},
            {"code": "DC-GE-PS", "name": "Benthic Infrastructure Sentry & Pipeline Guard", "desc": "Seafloor-crawling rover inspecting and defending gas conduits and fiber cables."},
            {"code": "DK-IE-PR", "name": "Sub-Surface C4ISR & Acoustic Relay Anchor", "desc": "Snorkel-horizon gateway relaying acoustic seabed signals to tactical LEO satellite clouds."},
            {"code": "DC-RE-SQ", "name": "Coastal Chokepoint Ambush Sleeper ('Zhdun')", "desc": "Resting silent on shallow seabed shelf for weeks; awakens upon acoustic warship signature."},
            {"code": "DA-IE-MR", "name": "Anti-Submarine Acoustic Barrier & Tracker", "desc": "Autonomous acoustic listening array tracking hostile nuclear and diesel submarines."},
            {"code": "DH-GE-MS", "name": "Seabed Robotic Intervenor & Heavy Manipulator", "desc": "Heavy robotic tool arm executing micron-level sabotage or repair at 3,000-6,000m depths."},
            {"code": "DK-IE-MR", "name": "Cross-Domain Littoral Aerial Staging Base", "desc": "Submerged stealth platform surfacing to launch FPV and UAV swarms into enemy rear littoral."}
        ],
        "combat_loop": "T+000s: Seabed sleeper (DC-RE-SQ) detects acoustic propeller signature. T+045s: Ballast released; silent ascent to strike depth. T+120s: Hydroacoustic terminal homing active. T+180s: Keel torpedo impact confirmed.",
        "matrix_token": "[ D P ]  -  [ E M ]  -  [ T C ]",
        "octet1_title": "Depth Horizon & Deployment Class [DP]",
        "octet1_content": "<b>D: Depth Horizon</b><br>• S: Surface (0m)<br>• K: Snorkel (0-15m)<br>• Z: Surf Zone (0-50m)<br>• W: Shallow Water (up to 100m)<br>• C: Continental Shelf (up to 500m)<br>• A: Abyssal (500-6,000m)<br>• H: Hadal (6,000-11,000m)<br><br><b>P: Deployment Class</b><br>• D: Diver-Deployed (<50 kg)<br>• V: Vessel Davit / Slipway<br>• T: 533mm Torpedo Tube<br>• L: Large Carrier Well-Deck<br>• B: Coastal Bunker Pen",
        "octet2_title": "Power Regeneration & Mission Mode [EM]",
        "octet2_content": "<b>E: Powerplant</b><br>• R: Rapid Chemical (Li-Ion, 12h)<br>• I: Intermittent Snorkel AIP<br>• G: Seabed Umbilical Anchor Grid<br>• N: Nuclear Micro-Reactor<br><br><b>M: Mission Mode</b><br>• D: Direct Kinetic Attack<br>• S: Stationary Sentry ('Zhdun')<br>• B: Benthic Crawler Ground-Contact<br>• L: Cross-Domain Aerial Launcher",
        "octet3_title": "Tactical Control & Acoustic Comms [TC]",
        "octet3_content": "<b>T: Autonomy Doctrine</b><br>• P: Passive Waypoint Navigation<br>• A: Active Acoustic Tracking<br>• M: Distributed Seabed Mesh<br>• S: Dormant Seabed Sleep<br><br><b>C: Comms Gateway</b><br>• A: Hydroacoustic Modem<br>• F: Spooled Glass Fiber Tether<br>• S: Floating Mast SATCOM<br>• Q: Radio-Silent Inertial/Terrain",
        "benchmarks": [
            {"role": "Extra-Large Autonomous Undersea Vehicle (XL-AUV)", "token": "UUV: DC-IE-MR", "platform": "Anduril Ghost Shark / Boeing Orca", "kinematics": "Hydrodynamic modular hull | Depth 500m+ | 100+ days subsea endurance", "logistics": "Shore slipway / well deck (D: L) | Heavy AIP / Li-ion hybrid bus (E: I)", "autonomy": "Autonomous acoustic pathfinding | Floating antenna buoy SATCOM", "kill_web": "Vector 1 & 5: Deep maritime interdiction and persistent choke-point mining."},
            {"role": "Parasitic Hull-Attached Stealth Vehicle", "token": "UUV: DC-RE-PR", "platform": "Lockheed Martin Lamprey MMAUV", "kinematics": "Slender conformal suction profile | Attaches directly to submarine hull", "logistics": "Host submarine external pylon (D: T) | Chemical solid-state cells (E: R)", "autonomy": "Autonomous parasitic detachment and return | Radio-silent acoustic ATR", "kill_web": "Vector 4: Forward acoustic screening and clandestine harbor penetration."}
        ],
        "hal_contract": "ISubseaAcoustic / IBenthicKinematics",
        "hal_contract_desc": "Governs buoyancy engine fluid trim, computes acoustic transmission loss TL across thermoclines, and controls caterpillar benthic seabed traction.",
        "governing_formula": "P_hydro = ρ · g · h  |  TL = 20 · log₁₀(R) + α · R",
        "formula_desc": "Hydrostatic pressure scales linearly with depth h, while acoustic transmission loss TL governs hydroacoustic modem communications and sonar detection limits."
    },
    "UOV": {
        "history_title": "Yuriy Kondratyuk (1929, LOR & Orbital Fuel Depots) Paradigm",
        "history_body": "In his seminal 1929 work 'The Conquest of Interplanetary Spaces', Ukrainian aerospace pioneer Yuriy Kondratyuk (Oleksandr Shargei) formulated the Lunar Orbit Rendezvous (LOR) trajectory chosen by NASA for the Apollo program. Crucially, Kondratyuk established the concept of distributed orbital fuel depots and modular spacecraft decoupling, proving that space dominance relies on rendezvous logistics and staging nodes rather than single giant rockets.",
        "trap_title": "Sci-Fi Free-Flight Tropes vs Keplerian Celestial Mechanics",
        "trap_body": "Popular culture envisions space warfare as dogfights with free directional maneuvering. In physical reality, spacecraft are prisoners of gravity: orbital velocity at LEO is 7.8 km/s. Changing orbital inclination by just 15° costs ~2,000 m/s of ΔV—equivalent to burning 50-70% of total satellite mass in chemical propellant. Space combat is governed strictly by Keplerian two-body celestial mechanics and Clohessy-Wiltshire relative equations.",
        "vectors": [
            {"code": "OL-RE-AQ", "name": "Co-Orbital Kinetic Interceptor & Hunter", "desc": "Maneuvering into matching orbital planes to execute machine-speed kinetic impact or fragmentation."},
            {"code": "OC-EE-PR", "name": "Rendezvous & Proximity Operations (RPO) Inspector", "desc": "Autonomous close-range fly-around imaging and electronic signals eavesdropping on adversary satellites."},
            {"code": "OM-CE-PS", "name": "Orbital Refueling Depot & Life Extension Tug", "desc": "Autonomous docking and propellant transfer extending the combat lifecycle of reconnaissance platforms."},
            {"code": "OC-EE-MA", "name": "Active Debris Removal (ADR) & Counter-Space", "desc": "Deploying harpoons, nets, and robotic clamps to capture and de-orbit hostile space assets."},
            {"code": "OL-EE-PS", "name": "Resilient LEO Distributed Mesh Constellation", "desc": "Mass-produced SmallSats providing jam-resistant optical crosslinks and optical/SAR surveillance."},
            {"code": "OG-HE-AR", "name": "High-Orbit Directed Energy & EW Neutralizer", "desc": "High-power radiofrequency and optical laser dazzler disabling sensor optics at geostationary altitudes."},
            {"code": "OD-RE-AQ", "name": "Cislunar & Deep Space Kinetic Interdictor", "desc": "Operating in Lagrange point halo orbits to police cislunar transit corridors."}
        ],
        "combat_loop": "T+000s: Ground space-tracking radar detects hostile maneuver. T+120s: Hunter (OL-RE-AQ) calculates Clohessy-Wiltshire intercept burn. T+360s: Cold-gas thruster firing. T+600s: Non-cooperative proximity lock. T+720s: Target neutralized.",
        "matrix_token": "[ O P ]  -  [ E M ]  -  [ T C ]",
        "octet1_title": "Orbital Horizon & Planar Alignment [OP]",
        "octet1_content": "<b>O: Orbital Horizon</b><br>• L: Low Earth Orbit (LEO, 160-2,000 km)<br>• M: Medium Earth Orbit (MEO, 2,000-35,786 km)<br>• G: Geostationary Orbit (GEO, 35,786 km)<br>• H: Highly Elliptical Orbit (HEO / Molniya)<br>• C: Cislunar / Lagrange Points (L1-L5)<br><br><b>P: Planar Alignment</b><br>• C: Co-Planar Shared Inclination<br>• N: Non-Co-Planar Crossing Orbit<br>• R: Retrograde High-Velocity Intercept",
        "octet2_title": "Propellant Architecture & Mode [EM]",
        "octet2_content": "<b>E: Powerplant & ISP</b><br>• C: Cold-Gas RCS (<75s ISP)<br>• M: Hypergolic Monoprop / Biprop (220-310s ISP)<br>• I: Ion Electric Hall-Effect (1,500-3,000s ISP)<br>• N: Nuclear Thermal Rocket (NTR, 850-1,000s ISP)<br><br><b>M: Dynamic Mission Mode</b><br>• K: Kinetic Kill (One-Way Impact)<br>• R: Rendezvous & Proximity (RPO)<br>• H: Harpoon / Net Debris Capture<br>• D: Refueling & Servicing Dock",
        "octet3_title": "Autonomy Doctrine & Signal Gateway [TC]",
        "octet3_content": "<b>T: Tactical Posture</b><br>• P: Persistent Orbit Surveillance<br>• A: Active Kinetic Attack<br>• M: Swarm Constellation Flocking<br>• S: Dormant Zombie Satellite<br><br><b>C: Communications Media</b><br>• L: Inter-Satellite Laser Crosslink (OISL)<br>• R: Space-to-Ground Phased S/X-Band<br>• Q: Autonomous Star-Tracker / Inertial<br>• S: Deep Space Relay Mesh",
        "benchmarks": [
            {"role": "Active Debris Removal & Counter-Space Hunter", "token": "UOV: OC-EE-MA", "platform": "NextGen Arsenal Orbital Guardian / Astroscale", "kinematics": "LEO sun-synchronous orbit | Cold-gas + electric propulsion | Multi-DoF robotic clamp", "logistics": "Rideshare fairing deployment (D: C) | Solar array + chemical RCS (E: M)", "autonomy": "Clohessy-Wiltshire relative navigation | Star-tracker + LiDAR rendezvous", "kill_web": "Vector 4: Non-cooperative orbital capture and targeted de-orbiting."},
            {"role": "Geostationary Mission Extension Tug", "token": "UOV: OG-CE-PS", "platform": "Northrop Grumman MEV (Mission Extension Vehicle)", "kinematics": "GEO drift orbit | High-ISP Hall thruster propulsion | Apogee kick motor", "logistics": "Heavy launch vehicle (D: I) | Solar-electric bus (E: I, 15+ years)", "autonomy": "Autonomous mechanical docking to target liquid apogee engine nozzle", "kill_web": "Vector 3: Life-extension, orbital attitude control, and satellite relocation."}
        ],
        "hal_contract": "IOrbitalInterceptor / ICelestialMechanics",
        "hal_contract_desc": "Solves Clohessy-Wiltshire relative equations for close proximity operations (RPO) and manages Tsiolkovsky delta-V budgets under non-linear orbital perturbations.",
        "governing_formula": "ΔV = I_sp · g_0 · ln(m_0 / m_f)  |  δr̈ + 2ω × δṙ + ω × (ω × δr) = F_thrust / m",
        "formula_desc": "Tsiolkovsky rocket equation defines maximum kinematic velocity change ΔV, while Clohessy-Wiltshire equations govern relative motion between interceptor and target spacecraft."
    }
}

def build_domains():
    # 1. Domains Master Index
    domains_cards = ""
    for d in DOMAINS_DATA:
        case_pills = "".join(f'<a href="../cases/{c}.html" class="badge badge-{d["code"].lower()}" style="margin-right:0.35rem; margin-bottom:0.35rem;">Case #{c[:2]}</a>' for c in d["cases"])
        domains_cards += f"""<div class="reddit-card">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
    <h2 style="margin:0;"><a href="{d['code'].lower()}.html">{d['name']}</a></h2>
    <span class="badge badge-{d['code'].lower()}" style="font-size:0.85rem;">{d['code']}</span>
  </div>
  <p><strong>Physical Medium:</strong> {d['medium']}</p>
  <p><strong>Governing Equations:</strong> {d['governing_laws']}</p>
  <div class="lesson-box" style="margin:0.75rem 0;">
    <strong>Legacy Classification Failure:</strong> {d['legacy_trap']}
  </div>
  <div style="margin-top:1rem;">
    <strong style="font-size:0.85rem; color:var(--text-muted);">Empirical Benchmarks in this Domain:</strong>
    <div style="margin-top:0.35rem;">{case_pills}</div>
  </div>
  <div style="margin-top:1rem;">
    <a href="{d['code'].lower()}.html" class="badge badge-hal" style="font-size:0.9rem; padding:0.4rem 0.8rem;">Explore Full 6-Block Taxonomy for {d['code']} →</a>
  </div>
</div>"""

    index_html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UWE Domain Taxonomy &amp; Cyber-Physical Horizons</title>
  <meta name="description" content="The 6 physical operational domains of UWE: UAV, UCV, UGV, UUV, USV, and UOV. Physical laws and taxonomy boundaries.">
  <link rel="canonical" href="{BASE_URL}/domains/index.html">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
  {render_header("domains", depth=1)}
  <div class="container">
    <h1 class="hero-title" style="font-size:1.85rem;">UWE Cross-Domain Taxonomy</h1>
    <p style="color:var(--text-muted); margin-bottom:2rem;">
      Replacing fragmented single-medium labels with unified cyber-physical horizons governed by the Law of Kinematic Primacy.
    </p>
    {domains_cards}
    <div class="lesson-box">
      <strong>Cross-domain orchestration is a separate layer, not a seventh physical domain.</strong>
      <a href="../c2/index.html">Explore C2 articles and Case #32 →</a>
    </div>
  </div>
  {render_footer()}
</body>
</html>"""
    write_file("domains/index.html", index_html)

    # 2. Individual Domain Pages
    for d in DOMAINS_DATA:
        dom_cases = [c for c in CASES_DATA if c["slug"] in d["cases"]]
        dom_cases_cards = "\n".join(render_case_card(c, depth=1) for c in dom_cases)
        deep_content = render_domain_taxonomy_section(d['code'])

        dom_page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{d['code']} Domain Taxonomy | Unmanned Warfare Engine</title>
  <meta name="description" content="{d['name']} — physical boundaries, equations of motion, 6-character matrix, and empirical benchmarks.">
  <link rel="canonical" href="{BASE_URL}/domains/{d['code'].lower()}.html">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
  {render_header("domains", depth=1)}
  <div class="container" style="max-width:960px;">
    <div style="margin-bottom:1rem;"><a href="index.html">← Back to All Domains</a></div>
    
    <div class="hero-box" style="margin-bottom:1.5rem;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
        <span class="badge badge-{d['code'].lower()}" style="font-size:1rem; padding:0.35rem 0.75rem;">Domain: {d['code']}</span>
        <span style="font-size:0.85rem; color:var(--text-muted);">Architect: <strong style="color:#fff;">Serhii Khylevych</strong> (Kyiv Baseline)</span>
      </div>
      <h1 class="hero-title" style="margin-top:0.75rem; margin-bottom:0.5rem;">{d['name']}</h1>
      <p style="color:var(--text-muted); font-size:1.05rem; margin-bottom:1rem;">{d['medium']}</p>
      
      <div style="background:var(--surface-alt); padding:1rem; border-radius:6px; border:1px solid var(--border);">
        <strong>Cyber-Physical Governing Laws:</strong>
        <p style="margin:0.25rem 0 0 0; font-size:0.9rem; color:#e6edf3;">{d['governing_laws']}</p>
      </div>

      <div class="lesson-box" style="margin-top:1rem;">
        <strong>The Legacy Classification Trap:</strong> {d['legacy_trap']}
      </div>
    </div>

    {deep_content}

    <div style="margin-top:2.5rem; border-top:2px solid var(--border); padding-top:1.5rem;">
      <h2 style="font-size:1.35rem; margin-bottom:1rem;">🔬 Empirical Benchmarks in {d['code']} ({len(dom_cases)} Cases)</h2>
      <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:1rem;">Empirical validation of platforms operating within the {d['code']} physical envelope:</p>
      <div>
        {dom_cases_cards}
      </div>
    </div>
  </div>
  {render_footer()}
</body>
</html>"""
        write_file(f"domains/{d['code'].lower()}.html", dom_page)


def build_vendors():
    vendor_cards = ""
    for v in VENDORS_DATA:
        v_cases = [c for c in CASES_DATA if c["vendor_slug"] == v["slug"]]
        case_links = "".join(f'<a href="../cases/{c["slug"]}.html" class="badge badge-{c["domain"].lower()}" style="margin-right:0.35rem;">Case #{c["id"]} ({c["name"]}) →</a>' for c in v_cases)
        plat_li = "".join(f"<li>{p}</li>" for p in v["platforms"])

        vendor_cards += f"""<div class="reddit-card" id="{v['slug']}">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
    <h2 style="margin:0; font-size:1.35rem;">{v['name']}</h2>
    <span class="badge badge-vendor">{v['origin']}</span>
  </div>
  <p style="color:var(--text-muted); font-size:0.9rem;">{v['focus']}</p>
  <div style="margin:0.75rem 0;">
    <strong>Key Autonomous Programs:</strong>
    <ul class="points">{plat_li}</ul>
  </div>
  <div style="margin-top:0.75rem; background:var(--surface-alt); padding:0.75rem; border-radius:6px;">
    <strong style="font-size:0.85rem; color:#58a6ff;">Evaluated in UWE Benchmarks:</strong>
    <div style="margin-top:0.35rem;">{case_links}</div>
  </div>
</div>"""

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vendor &amp; OEM Defense-Tech Mapping | UWE</title>
  <meta name="description" content="Mapping global MilTech manufacturers and frontline developers to UWE cyber-physical contracts.">
  <link rel="canonical" href="{BASE_URL}/vendors/index.html">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
  {render_header("vendors", depth=1)}
  <div class="container">
    <h1 class="hero-title" style="font-size:1.85rem;">Defense-Tech Vendors & OEM Mapping</h1>
    <p style="color:var(--text-muted); margin-bottom:2rem;">
      Analyzing how global defense primes (Anduril, Boeing, Lockheed Martin, Exail, BAE Systems) and frontline Ukrainian innovators align with the UWE Hardware Abstraction Layer.
    </p>
    {vendor_cards}
  </div>
  {render_footer()}
</body>
</html>"""
    write_file("vendors/index.html", html)

def build_hal():
    hal_rows = ""
    for c in CASES_DATA:
        hal_rows += f"""<div class="reddit-card" id="{c['hal']}">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
    <h3 style="margin:0; font-family:var(--code-font); color:#58a6ff;"><code>{c['hal']}</code></h3>
    <a href="../cases/{c['slug']}.html" class="badge badge-{c['domain'].lower()}">Case #{c['id']} ({c['domain']})</a>
  </div>
  <div style="background:#111827; padding:0.85rem; border-radius:6px; margin:0.75rem 0; border:1px solid #1f2937;">
    <strong>One-Sentence Control Law:</strong>
    <p style="margin:0.25rem 0 0 0; font-style:italic; font-size:0.9rem;">"{c['hal_def']}"</p>
  </div>
  <div style="font-size:0.85rem; color:var(--text-muted);">
    Tested Platform: <strong>{c['name']}</strong> ({c['vendor']}) • Token: <code>{c['token']}</code>
  </div>
</div>"""

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hardware Abstraction Layer (HAL) Contract Registry | UWE</title>
  <meta name="description" content="Deterministic cyber-physical interfaces and control law contracts governing robotic fleets under UWE.">
  <link rel="canonical" href="{BASE_URL}/hal/index.html">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
  {render_header("hal", depth=1)}
  <div class="container">
    <h1 class="hero-title" style="font-size:1.85rem;">Hardware Abstraction Layer (HAL) Registry</h1>
    <p style="color:var(--text-muted); margin-bottom:2rem;">
      Autonomous vehicles are object-oriented executors. The HAL contracts standardize control laws across disparate airframes, hulls, and chassis.
    </p>
    {hal_rows}
  </div>
  {render_footer()}
</body>
</html>"""
    write_file("hal/index.html", html)

def build_consulting():
    print("\n🔹 Generating B2B Advisory & Consulting Landing Page...")
    jsonld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "B2B Systems Architecture & Engineering Advisory",
        "provider": {
            "@type": "Person",
            "name": "Serhii Khylevych",
            "jobTitle": "Principal Systems Architect",
            "url": "https://ua.linkedin.com/in/serhii-khylevych-aa152322"
        },
        "description": "End-to-end systems architecture, multi-tier Hardware Abstraction Layer (HAL) design, and operational rollout consulting for autonomous platforms across air, ground, maritime, and orbital domains.",
        "areaServed": ["US", "EU", "UK", "NATO Allied Markets"],
        "serviceType": "Autonomous Cyber-Physical Systems Architecture",
        "url": f"{BASE_URL}/consulting.html"
    }

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Advisory &amp; Consulting | Systems Architecture &amp; HAL Design | UWE</title>
  <meta name="description" content="End-to-end B2B systems architecture, Hardware Abstraction Layer (HAL) design, and MVP-to-industrial rollout advisory for autonomous defense robotics by Serhii Khylevych.">
  <link rel="canonical" href="{BASE_URL}/consulting.html">
  <link rel="stylesheet" href="assets/css/style.css">
  <script type="application/ld+json">
{json.dumps(jsonld, indent=2)}
  </script>
</head>
<body>
  {render_header("consulting", depth=0)}
  <div class="container">
    <!-- Block 1: Hero Section -->
    <div class="hero-box">
      <div style="margin-bottom:1rem;">
        <span class="tag-pill" style="border-color:#58a6ff; color:#58a6ff; background:rgba(88, 166, 255, 0.1); font-weight:700; text-transform:uppercase; letter-spacing:0.5px;">
          🛡️ B2B SYSTEMS ARCHITECTURE &amp; ENGINEERING ADVISORY
        </span>
      </div>
      <h1 class="hero-title" style="margin-top:0.5rem; font-size:2.3rem;">
        From Physics-Validated Prototypes to Industrial-Scale Autonomous Systems
      </h1>
      <p class="hero-subtitle" style="font-size:1.15rem; line-height:1.6; max-width:960px;">
        End-to-end systems architecture, multi-tier Hardware Abstraction Layer (HAL) design, and operational rollout consulting for autonomous platforms across air, ground, maritime, and orbital domains.
      </p>
      
      <div style="display:flex; flex-wrap:wrap; gap:0.6rem; margin:1.25rem 0 1.75rem 0;">
        <span class="tag-pill">🔒 Strict NDA Compliance</span>
        <span class="tag-pill">📊 Open-Source &amp; Client Data Only</span>
        <span class="tag-pill">⚡ 20+ Years Principal Architecture</span>
      </div>

      <div style="display:flex; flex-wrap:wrap; gap:1rem; align-items:center;">
        <a href="#contact" class="btn btn-primary" style="font-size:1rem; padding:0.75rem 1.4rem;">Request Architecture Briefing →</a>
        <a href="index.html#benchmarks" class="btn btn-secondary" style="font-size:1rem; padding:0.75rem 1.4rem;">Explore Empirical Benchmarks</a>
      </div>
    </div>

    <!-- Block 2: Track Record & Trust Metrics -->
    <div class="kpi-grid">
      <div class="kpi-card highlight">
        <div class="kpi-num" style="color:#58a6ff;">20+ Years</div>
        <div class="kpi-label">Mission-Critical Architecture</div>
        <div class="kpi-sub">Enterprise telecom, NTN/LEO satellite networks, SDR/MANET &amp; autonomous cyber-physical systems</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-num">$45M+</div>
        <div class="kpi-label">Portfolios Delivered &amp; Scaled</div>
        <div class="kpi-sub">Proven track record in scaling complex engineering from initial concept to multi-site industrial replication</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-num">{len(CASES_DATA)}</div>
        <div class="kpi-label">Empirically Benchmarked</div>
        <div class="kpi-sub">Physics-based stress-testing across 6 physical domains against kinematic, thermodynamic &amp; EW limits</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-num" style="color:#3fb950;">100%</div>
        <div class="kpi-label">IP Protection &amp; Zero Classified Data</div>
        <div class="kpi-sub">Strict mutual NDA execution using Client proprietary specifications and public scientific/OSINT benchmarks</div>
      </div>
    </div>

    <!-- Block 3: Core Advisory & Engineering Services -->
    <div style="margin:3rem 0 2rem 0;">
      <div style="border-bottom:1px solid var(--border); padding-bottom:0.75rem; margin-bottom:1.5rem;">
        <h2 style="font-size:1.6rem; color:#fff; margin:0 0 0.4rem 0;">Full-Lifecycle Architectural &amp; Rollout Capabilities</h2>
        <p style="color:var(--text-muted); font-size:1rem; margin:0;">
          Practical systems engineering designed to eliminate kinematic bottlenecks, prevent costly hardware redesigns, and ensure survivability in contested environments.
        </p>
      </div>

      <div class="service-grid">
        <div class="service-card">
          <div>
            <div class="service-header">
              <span class="badge badge-uav">TIER 1 ARCHITECTURE</span>
              <h3 class="service-title">Multi-Tier Systems Architecture &amp; HAL Design</h3>
            </div>
            <p class="service-scope">
              End-to-end architectural blueprint across all system layers—from physical chassis kinematics and Hardware Abstraction Layers (HAL) to onboard Edge-AI, resilient SDR/MANET communications, and multi-domain C2 orchestration.
            </p>
            <div class="service-deliverables">
              <strong>Deliverables:</strong> System Architecture Document (SAD), HAL interface contracts, telemetry &amp; control loop latency budgets, failure-mode isolation matrices.
            </div>
          </div>
          <div class="service-format">
            Fixed-Scope Project (2–4 weeks) • Starting from $4,000
          </div>
        </div>

        <div class="service-card">
          <div>
            <div class="service-header">
              <span class="badge badge-ucv">TIER 2 INDUSTRIALIZATION</span>
              <h3 class="service-title">MVP-to-Industrial Rollout Roadmap</h3>
            </div>
            <p class="service-scope">
              Bridging the gap between a working field prototype (MVP) and repeatable industrial mass production. Eliminating fragile bespoke dependencies, standardizing modular payloads, and structuring scalable software-hardware pipelines.
            </p>
            <div class="service-deliverables">
              <strong>Deliverables:</strong> Industrialization &amp; Scaling Roadmap, Bill-of-Materials (BoM) architectural optimization, modular containerization strategy (C0–C4 logistics alignment).
            </div>
          </div>
          <div class="service-format">
            Phased Milestone Delivery • Starting from $5,000
          </div>
        </div>

        <div class="service-card">
          <div>
            <div class="service-header">
              <span class="badge badge-usv">TIER 3 ENVIRONMENT ADAPTATION</span>
              <h3 class="service-title">Market &amp; Tactical Environment Adaptation</h3>
            </div>
            <p class="service-scope">
              Stress-testing and adapting commercial or dual-purpose platforms for harsh, denied, degraded, intermittent, and limited-bandwidth (DDIL) operational environments, as well as commercial market viability.
            </p>
            <div class="service-deliverables">
              <strong>Deliverables:</strong> Environmental Abstraction Layer (EAL) specification, EW/GNSS-denied resilience audit, kinematic trade-off study, and regulatory/market fit assessment.
            </div>
          </div>
          <div class="service-format">
            Targeted Audit / Trade-Off Study • Starting from $3,500
          </div>
        </div>

        <div class="service-card">
          <div>
            <div class="service-header">
              <span class="badge badge-ugv">TIER 4 EXECUTIVE GOVERNANCE</span>
              <h3 class="service-title">Fractional Principal Systems Architect</h3>
            </div>
            <p class="service-scope">
              Ongoing executive-level technical governance for R&amp;D teams, OEMs, and venture-backed engineering startups. Direct participation in design reviews, vendor evaluations, and architectural decision-making.
            </p>
            <div class="service-deliverables">
              <strong>Deliverables:</strong> Weekly architecture review sessions, continuous technical due diligence, direct advisory access for CTOs and lead engineers.
            </div>
          </div>
          <div class="service-format">
            Monthly Advisory Retainer • $4,000 – $7,500 / month
          </div>
        </div>
      </div>
    </div>

    <!-- Block 4: Methodology & Data Governance -->
    <div style="margin:3rem 0 2rem 0;">
      <div style="border-bottom:1px solid var(--border); padding-bottom:0.75rem; margin-bottom:1.5rem;">
        <h2 style="font-size:1.6rem; color:#fff; margin:0 0 0.4rem 0;">Data Governance, NDA &amp; Export Control Compliance</h2>
        <p style="color:var(--text-muted); font-size:1rem; margin:0;">
          Engineered for seamless legal and financial onboarding with international corporations across the US, EU, UK, and allied markets.
        </p>
      </div>

      <div class="gov-grid">
        <div class="gov-card">
          <h4>1. Strict Information Boundaries</h4>
          <p>
            All analytical modeling, simulations, and architectural recommendations are derived exclusively from Client-provided confidential specifications (under NDA) and publicly available physics, academic literature, and OSINT benchmarks. No restricted or classified third-party data is ever accessed or utilized.
          </p>
        </div>
        <div class="gov-card" style="border-left-color:#3fb950;">
          <h4>2. Client IP Ownership</h4>
          <p>
            Upon milestone completion, 100% of custom architectural specifications, HAL schemas, and mathematical models produced during the engagement transfer unconditionally to the Client.
          </p>
        </div>
        <div class="gov-card" style="border-left-color:#bc8cff;">
          <h4>3. Transparent B2B Contracting</h4>
          <p>
            Engagements are executed under standard Master Services Agreements (MSA) and Mutual NDAs, supported by milestone-based invoicing (SWIFT USD / SEPA EUR) and formal Certificates of Completion.
          </p>
        </div>
      </div>
    </div>

    <!-- Block 5: Engagement Workflow -->
    <div style="margin:3rem 0 2rem 0;">
      <div style="border-bottom:1px solid var(--border); padding-bottom:0.75rem; margin-bottom:1.5rem;">
        <h2 style="font-size:1.6rem; color:#fff; margin:0 0 0.4rem 0;">Engagement Workflow</h2>
        <p style="color:var(--text-muted); font-size:1rem; margin:0;">
          A deterministic, low-overhead four-step process from initial discovery to validated architectural handover.
        </p>
      </div>

      <div class="workflow-grid">
        <div class="workflow-step">
          <div class="step-num">Step 01</div>
          <h4 class="step-title">Initial Discovery &amp; Mutual NDA</h4>
          <p class="step-desc">
            30-minute technical scoping call to align on system objectives, physical domain constraints, and sign a Mutual Non-Disclosure Agreement.
          </p>
        </div>
        <div class="workflow-step">
          <div class="step-num">Step 02</div>
          <h4 class="step-title">Architectural Scoping &amp; Plan</h4>
          <p class="step-desc">
            Definition of exact engineering deliverables, timeline, and fixed-price milestones (with standard 50% upfront / 50% upon delivery billing).
          </p>
        </div>
        <div class="workflow-step">
          <div class="step-num">Step 03</div>
          <h4 class="step-title">Deep-Dive Modeling &amp; Design</h4>
          <p class="step-desc">
            Execution of kinematic/cyber-physical analysis, HAL contract specification, or rollout architecture based on your team's inputs.
          </p>
        </div>
        <div class="workflow-step">
          <div class="step-num">Step 04</div>
          <h4 class="step-title">Handover &amp; Engineering Briefing</h4>
          <p class="step-desc">
            Delivery of comprehensive technical documentation, simulation matrices, and a live Q&amp;A walkthrough with your R&amp;D leadership.
          </p>
        </div>
      </div>
    </div>

    <!-- Block 6: Direct Inquiry & Legal Footer -->
    <div id="contact" class="inquiry-box">
      <div style="max-width:800px;">
        <span class="badge badge-uav" style="font-size:0.8rem; margin-bottom:0.5rem;">DIRECT ARCHITECTURAL ENGAGEMENT</span>
        <h2 style="font-size:1.85rem; color:#fff; margin:0.5rem 0 0.75rem 0;">
          Ready to Stress-Test or Scale Your System Architecture?
        </h2>
        <p style="color:#c9d1d9; font-size:1.05rem; line-height:1.6; margin-bottom:1.5rem;">
          Direct communication with Principal Systems Architect <strong>Serhii Khylevych</strong>. No sales intermediaries or business-development overhead.
        </p>

<div style="display:flex; flex-wrap:wrap; gap:1rem; align-items:center; margin-bottom:1rem;">
          <a href="mailto:hillmtz@gmail.com?subject=UWE%20Architecture%20Briefing%20Inquiry" class="btn btn-primary" style="font-size:1rem; padding:0.75rem 1.5rem;">
            ✉️ Schedule Briefing via Email
          </a>
          <a href="https://ua.linkedin.com/in/serhii-khylevych-aa152322" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size:1rem; padding:0.75rem 1.5rem;">
            Connect on LinkedIn ↗
          </a>
        </div>

        <div style="display:inline-flex; align-items:center; gap:0.5rem; background:rgba(255,255,255,0.05); border:1px solid var(--border-color); padding:0.5rem 0.85rem; border-radius:6px; font-family:monospace; font-size:0.95rem; color:#fff; margin-bottom:1.5rem;">
          <span style="color:var(--text-muted); font-family:sans-serif; font-size:0.85rem;">Direct Email:</span>
          <strong id="contact-email">hillmtz@gmail.com</strong>
          <button type="button" onclick="navigator.clipboard.writeText('hillmtz@gmail.com'); this.innerText='✓ Copied'; setTimeout(()=>this.innerText='Copy', 2000);" style="background:var(--accent-blue, #58a6ff); border:none; color:#fff; padding:0.25rem 0.6rem; border-radius:4px; cursor:pointer; font-size:0.8rem; margin-left:0.5rem; font-family:sans-serif;">Copy</button>
        </div>

        <div class="legal-card">
          <div style="font-weight:700; color:#fff; margin-bottom:0.4rem; font-size:0.95rem;">
            🏢 Legal &amp; Billing Entity (International Banking Compliance)
          </div>
          <div><strong>Service Provider:</strong> Private Entrepreneur (PE) Serhii Khylevych (Ukraine, Group 3 Tax Entity — Export of Engineering &amp; IT Consulting Services)</div>
          <div><strong>Accepted Currencies:</strong> USD (SWIFT wire transfer), EUR (SEPA wire transfer)</div>
          <div style="margin-top:0.4rem; color:var(--text-muted); font-size:0.8rem;">
            <em>Compliance Statement:</em> All advisory services constitute intellectual systems engineering and non-classified architectural consulting. Engagements operate strictly on non-restricted technical and open-source data under mutual NDA.
          </div>
        </div>
      </div>
    </div>

  </div>
  {render_footer(is_consulting=True)}
</body>
</html>"""
    write_file("consulting.html", html)

def build_c2_officer():
    print("\n🔹 Generating C2 Officer Human-Machine Symbiosis Whitepaper Page...")
    
    # 1. Copy Master High-Resolution Visual Assets to docs/assets/img/
    copy_asset_binary("uwe_officer_trinity_collage.jpg", "assets/img/uwe_officer_trinity_collage.jpg")
    copy_asset_binary("hal_moore_shoot_as_think.png", "assets/img/hal_moore_shoot_as_think.png")
    copy_asset_binary("jordan_oneil_coastal_rescue.jpg", "assets/img/jordan_oneil_coastal_rescue.jpg")
    copy_asset_binary("maverick_dagger_dogfight.png", "assets/img/maverick_dagger_dogfight.png")

    # 2. Build HTML Page
    jsonld = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": "The Cyber-Physical Officer: Human-Machine Symbiosis in the Unmanned Warfare Engine (UWE)",
        "description": "Multi-domain C2 command doctrine, Moore-Plumley paradigm, APM vs. CPM discrimination, Fallout 4-STDFUA biometric fail-safe, and 'I Shoot As I Think' zero translation latency.",
        "author": {
            "@type": "Person",
            "name": "Serhii Khylevych",
            "jobTitle": "Systems Architect",
            "url": "https://ua.linkedin.com/in/serhii-khylevych-aa152322"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Unmanned Warfare Engine Initiative"
        },
        "datePublished": "2026-10-24",
        "mainEntityOfPage": f"{BASE_URL}/c2/officer.html"
    }

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Cyber-Physical Officer: Human-Machine Symbiosis | UWE Standard</title>
  <meta name="description" content="Autonomous warfare command doctrine: The Moore-Plumley paradigm, APM (300-400) vs CPM (2-3) discrimination, STDFUA biometric fail-safe, and 'I Shoot As I Think' zero translation latency. Authored by Serhii Khylevych.">
  <link rel="canonical" href="{BASE_URL}/c2/officer.html">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script type="application/ld+json">
  {json.dumps(jsonld, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>
  {render_header("c2", depth=1)}
  <div class="container">
    <div style="margin-bottom:1rem; font-size:0.85rem; color:var(--text-muted);">
      <a href="../index.html">Hub</a> &gt; <span style="color:#fff;">C2 Officer Symbiosis</span>
    </div>

    <!-- Hero Card -->
    <div class="hero-box">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
        <span class="badge" style="background:#1f6feb; color:#fff; font-size:0.85rem; font-weight:700;">COMMAND & COGNITIVE SYMBIOSIS DOCTRINE</span>
        <span style="font-size:0.85rem; color:#8b949e;">Kyiv Wartime Baseline • 2026</span>
      </div>
      <h1 class="hero-title" style="font-size:2.1rem;">The Cyber-Physical Officer: Human-Machine Symbiosis in UWE</h1>
      <p class="hero-subtitle" style="font-size:1.15rem; color:#c9d1d9;">
        Beyond "Twitch-Reflexes": The Moore-Plumley Paradigm, APM vs. CPM Discrimination, and the <em>"I Shoot As I Think"</em> Doctrine
      </p>
      
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; border-top:1px solid var(--border); padding-top:1rem; margin-top:1rem;">
        <div>
          <span style="color:#fff; font-weight:600;">Author:</span> Serhii Khylevych — <em>Systems Architect & MilTech Strategist</em>
        </div>
        <div>
          <a href="https://www.linkedin.com/pulse/cyber-physical-officer-human-machine-symbiosis-engine-khylevych-pkjff" target="_blank" rel="noopener" class="badge badge-uav" style="font-size:0.85rem; padding:0.4rem 0.8rem; text-decoration:none;">Read Live on LinkedIn Pulse ↗</a>
        </div>
      </div>

      <!-- Master Title Infographic Cover -->
      <div style="margin-top:2rem; text-align:center;">
        <img src="../assets/img/uwe_officer_trinity_collage.jpg" alt="UWE Tactical Officer Trinity & Invariant HAL" style="width:100%; max-width:1000px; height:auto; border-radius:8px; border:1px solid var(--border); box-shadow: 0 8px 30px rgba(0,0,0,0.6);">
        <p style="font-size:0.85rem; color:var(--text-muted); margin-top:0.6rem;">
          <em>Figure 1: Master Title Infographic Cover (2400×1350) — The Command Trinity (Hal Moore, Jordan O'Neil, Pete Maverick) orbiting the Invariant HAL Anchor (CSM Basil Plumley) across the 6-Domain Saturated Gauge.</em>
        </p>
      </div>

      <!-- Epistemological Disclaimer -->
      <div style="background:#161b22; border-left:4px solid var(--amber); padding:1rem; border-radius:6px; margin-top:1.5rem; font-size:0.88rem; line-height:1.6; color:#c9d1d9;">
        <strong style="color:#d29922;">⚠️ EPISTEMOLOGICAL DISCLAIMER & SYSTEM BOUNDARIES:</strong><br>
        The author of this architecture does not hold authorization to cite classified operational after-action reports (AARs) or restricted multi-domain tactical telemetry datasets of sovereign states. Consequently, the cinematic case studies referenced herein (<em>We Were Soldiers</em>, <em>G.I. Jane</em>, <em>Top Gun: Maverick</em>, <em>Lie to Me</em>) are utilized strictly as non-linear conceptual metaphors and qualitative cognitive models to evaluate the extreme limits of human-machine interaction, reflex synchronization, and real-time cybernetic fail-safes under high-intensity kinematic stress.
      </div>
    </div>

    <!-- Dedications & Tactical Phenotypes -->
    <section class="reddit-card" style="border-left:4px solid #e3b341; background:rgba(227, 179, 65, 0.04);">
      <h2 style="color:#f2cc60; margin-top:0;">🌟 Dedications &amp; Deep Gratitude</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        This architectural model was forged in Kyiv amidst the existential realities of multi-domain asymmetric warfare. The cognitive framework detailed here would have been impossible without the profound inspiration of legendary actors and the dialogue of international peers.
      </p>

      <h3 style="color:#fff; font-size:1.1rem; margin-top:1.25rem;">🎖️ The Legendary Actors &amp; Their Tactical Phenotypes</h3>
      <p style="color:var(--text-muted); font-size:0.9rem;">
        We extend our deepest gratitude for the extraordinary motivation, character archetypes, and cultural grounding provided by:
      </p>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:1rem; margin:1rem 0;">
        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="color:#bc8cff; font-size:1.05rem;">Sam Elliott</strong>
            <span class="badge" style="background:#2d1b4e; color:#d2a8ff;">INVARIANT HAL ENGINE</span>
          </div>
          <div style="font-size:0.85rem; color:#8b949e; margin-bottom:0.5rem;">
            <em>CSM Basil Plumley</em> in <a href="https://www.imdb.com/title/tt0277434/" target="_blank" rel="noopener">We Were Soldiers (2002)</a> &amp; <em>Gen. Ross</em> in <a href="https://www.imdb.com/title/tt0286716/" target="_blank" rel="noopener">Hulk (2003)</a>
          </div>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5; margin:0;">
            The archetype of the unyielding, predatory Master Sergeant. His legendary "Old Iron Jaw" calm under artillery fire provided the behavioral baseline for the <strong>UWE Engine itself</strong> — a tireless, incorruptible cyber-physical executor maintaining logistical and tactical order across battlefield friction. (<a href="https://www.imdb.com/name/nm0000385/" target="_blank" rel="noopener">Sam Elliott IMDb</a>)
          </p>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="color:#58a6ff; font-size:1.05rem;">Mel Gibson</strong>
            <span class="badge" style="background:#12283a; color:#58a6ff;">CPM MORAL SOVEREIGNTY</span>
          </div>
          <div style="font-size:0.85rem; color:#8b949e; margin-bottom:0.5rem;">
            <em>Lt. Col. Harold G. "Hal" Moore</em> in <a href="https://www.imdb.com/title/tt0277434/" target="_blank" rel="noopener">We Were Soldiers (2002)</a>
          </div>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5; margin:0;">
            The personification of the sovereign moral core, battlefield empathy, and the sacred military oath ("First on the ground, last to leave"). His leadership model underpins our doctrine of <strong>CPM Sovereignty</strong>, guaranteeing that while machines optimize kinematics, only a human commander carries the moral and legal weight of lethal authority. (<a href="https://www.imdb.com/name/nm0000154/" target="_blank" rel="noopener">Mel Gibson IMDb</a>)
          </p>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="color:#38bdf8; font-size:1.05rem;">Demi Moore</strong>
            <span class="badge" style="background:#0d2d3a; color:#38bdf8;">ANTIFRAGILE SYSTEM GUARDIAN</span>
          </div>
          <div style="font-size:0.85rem; color:#8b949e; margin-bottom:0.5rem;">
            <em>Lt. Jordan O'Neil</em> in <a href="https://www.imdb.com/title/tt0119173/" target="_blank" rel="noopener">G.I. Jane (1997)</a>
          </div>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5; margin:0;">
            The ultimate benchmark for high-bandwidth spatial scanning, predictive synchronization, and unyielding fortitude. Her coastal extraction planning demonstrated the compressed OODA loop required of an officer managing multi-domain Kill Webs, rescuing the system when automation fractures under stress. (<a href="https://www.instagram.com/demimoore/" target="_blank" rel="noopener">Demi Moore Instagram</a> / <a href="https://www.imdb.com/name/nm0000193/" target="_blank" rel="noopener">IMDb</a>)
          </p>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="color:#ff7b72; font-size:1.05rem;">Tom Cruise</strong>
            <span class="badge" style="background:#3a1818; color:#ff7b72;">9G KINEMATIC BOUNDARY</span>
          </div>
          <div style="font-size:0.85rem; color:#8b949e; margin-bottom:0.5rem;">
            <em>Capt. Pete "Maverick" Mitchell</em> in <a href="https://www.imdb.com/title/tt1745960/" target="_blank" rel="noopener">Top Gun: Maverick (2022)</a>
          </div>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5; margin:0;">
            The benchmark for non-linear crisis adaptation, testing kinematic boundaries (UWE Law I), and shattering bureaucratic dogma through physical execution. His 9G flight test provided the foundation for our core tactical creed: <strong>"I Shoot As I Think."</strong> (<a href="https://www.imdb.com/name/nm0000129/" target="_blank" rel="noopener">Tom Cruise Profile</a>)
          </p>
        </div>
      </div>

      <div style="background:#161b22; border-left:4px solid #38bdf8; padding:1rem; border-radius:6px; margin-top:1.25rem;">
        <strong style="color:#38bdf8;">🤝 Special Strategic Acknowledgement: <a href="https://www.linkedin.com/in/kjchoo/" target="_blank" rel="noopener" style="color:#58a6ff;">KJ Choo</a></strong><br>
        <p style="font-size:0.88rem; color:#c9d1d9; margin:0.35rem 0 0 0; line-height:1.6;">
          Systems strategist and international technology leader. Without his continuous analytical support, rigorous sounding-board evaluations, and deep perspective on autonomous systems integration, this cross-domain human-cybernetic synthesis would have remained incomplete. His engagement exemplifies the international coalition of forward-thinking minds building the automated shield for the Free World.
        </p>
      </div>
    </section>

    <!-- Section 1: Foundational Analogy -->
    <section class="reddit-card" style="border-left:4px solid var(--accent);">
      <h2 style="color:#58a6ff; margin-top:0;">1. The Foundational Analogy: Naval Fleet Scaling across 6 Domains</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        In classical land warfare, command revolves around directing human bodies. In <strong>UWE</strong>, command shifts to orchestrating high-density cyber-physical fleets across six operating domains: 
        <strong>Space (<a href="../domains/uov.html">UOV</a>)</strong>, 
        <strong>Air (<a href="../domains/uav.html">UAV</a>)</strong>, 
        <strong>Copter (<a href="../domains/ucv.html">UCV</a>)</strong>, 
        <strong>Ground (<a href="../domains/ugv.html">UGV</a>)</strong>, 
        <strong>Surface (<a href="../domains/usv.html">USV</a>)</strong>, and 
        <strong>Subsea (<a href="../domains/uuv.html">UUV</a>)</strong>.
      </p>
      <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6;">
        This operational paradigm directly mirrors <strong>Naval Fleet Operations (ВМФ)</strong>: autonomous robotic fleets operate with high technological density per unit, navigate hostile physical fluids, and execute coordinated strikes under strict electronic silence (EMCON). Command authority scales across three maritime tiers:
      </p>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:1rem; margin-top:1.25rem;">
        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="color:#fff; font-size:1.05rem;">Tier 1: Ship Captain / Corvette</strong>
            <span class="badge badge-uav" style="font-size:0.75rem;">TACTICAL ORDER</span>
          </div>
          <p style="font-size:0.85rem; color:#58a6ff; margin:0.25rem 0;"><strong>Command Unit:</strong> Single heavy platform (<code>SL-PA-MO</code>, <code>GL-EB-DW</code>) or tactical cluster.</p>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5;"><strong>Operational Scope:</strong> Total autonomy under electronic blackout. The officer functions as a ship captain: managing hull damage, local power budgets, and executing terminal strikes without waiting for satellite pings.</p>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="color:#fff; font-size:1.05rem;">Tier 2: Division Commander</strong>
            <span class="badge badge-usv" style="font-size:0.75rem;">KILL WEB COORDINATOR</span>
          </div>
          <p style="font-size:0.85rem; color:#38bdf8; margin:0.25rem 0;"><strong>Command Unit:</strong> Multi-asset strike groups (Air-Surface-Subsea).</p>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5;"><strong>Operational Scope:</strong> Dynamic Kill Web allocation and rapid intermodal deployment (C0-C2 Containerization) from off-road beach trailers before adversary counter-battery locks on.</p>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="color:#fff; font-size:1.05rem;">Tier 3: Fleet Admiral</strong>
            <span class="badge badge-uov" style="font-size:0.75rem;">STRATEGIC ARCHITECT</span>
          </div>
          <p style="font-size:0.85rem; color:#ff7b72; margin:0.25rem 0;"><strong>Command Unit:</strong> Entire 6-domain theater containment shield.</p>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5;"><strong>Operational Scope:</strong> Full theater orchestration, balancing the <strong>Cost-Exchange Ratio (attrition calculus)</strong>, and integrating open-architecture APIs to out-scale adversary industrial output.</p>
        </div>
      </div>
    </section>

    <!-- Section 2: Moore-Plumley Symbiosis -->
    <section class="reddit-card" style="border-left:4px solid var(--purple);">
      <h2 style="color:#bc8cff; margin-top:0;">2. The Hal Moore &amp; CSM Basil Plumley Symbiosis (E2E Combat Lifecycle)</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        The primary anxiety of military commanders regarding AI is the <em>"loss of control"</em> — the fear of opaque algorithms usurping command or executing unauthorized escalations.
      </p>
      <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6;">
        UWE resolves this by adopting the historical command dynamic of <strong>Lt. Col. Hal Moore and CSM Basil Plumley</strong> (Battle of Ia Drang, 1965):
      </p>
      
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1rem; margin:1rem 0;">
        <div style="background:#161b22; border:1px solid var(--border); border-radius:6px; padding:1rem;">
          <h4 style="margin:0 0 0.5rem 0; color:#58a6ff;">🎖️ The Commander (Hal Moore)</h4>
          <p style="font-size:0.88rem; color:#e6edf3; margin:0;">Holds the <strong>"Why" and "What"</strong> — strategic intent, ethical stewardship, sovereign authority under the Law of Armed Conflict, and cryptographic lethal release.</p>
        </div>
        <div style="background:#161b22; border:1px solid var(--border); border-radius:6px; padding:1rem;">
          <h4 style="margin:0 0 0.5rem 0; color:#d2a8ff;">⚙️ The UWE Engine (CSM Basil Plumley)</h4>
          <p style="font-size:0.88rem; color:#e6edf3; margin:0;">Holds the <strong>"How"</strong> — tireless discipline, terramechanics, aerodynamic drag solving, logistical containerization, and microsecond Kill Web routing.</p>
        </div>
      </div>

      <h3 style="color:#fff; font-size:1.1rem; margin-top:1.5rem;">The Five Phases of the Combat Lifecycle</h3>
      <div style="display:flex; flex-direction:column; gap:0.75rem; font-size:0.9rem;">
        <div style="background:#111827; padding:0.85rem 1rem; border-radius:6px; border:1px solid #1f2937;">
          <strong style="color:#58a6ff;">Phase 1: Planning &amp; Intent vs. Physical Reality:</strong> The Commander dictates operational vectors. UWE calculates the dynamic feasibility index against terramechanics, waves, and jamming. Like Plumley, UWE grumbles in cold numbers: <em>"Sir, your vector is 82% viable; shift deployment to C2 mobile rails for 100%."</em>
        </div>
        <div style="background:#111827; padding:0.85rem 1rem; border-radius:6px; border:1px solid #1f2937;">
          <strong style="color:#58a6ff;">Phase 2: Decentralized Logistics &amp; Sustainment:</strong> The Commander focuses on operational geometry. UWE automatically manages the supply continuum (Law II): monitoring battery SOC, routing <a href="../domains/ugv.html">UGV</a> mobile powerbanks (LLD-2), and pre-positioning munition pods.
        </div>
        <div style="background:#111827; padding:0.85rem 1rem; border-radius:6px; border:1px solid #1f2937;">
          <strong style="color:#58a6ff;">Phase 3: The Kinetic Kill Web (LLD-1):</strong> The Commander tracks operational tempo. UWE binds orbital sensors (<a href="../domains/uov.html">UOV</a>) to tactical multirotors (<a href="../domains/ucv.html">UCV</a>) and surface interceptors (<a href="../domains/usv.html">USV</a>) at machine speed, resolving microsecond target handoffs without human cognitive lag.
        </div>
        <div style="background:#111827; padding:0.85rem 1rem; border-radius:6px; border:1px solid #1f2937;">
          <strong style="color:#f85149;">Phase 4: Critical States &amp; "Broken Arrow" (Law III Decoupled Lethality):</strong> When defense lines are breached, the Commander authorizes the cybernetic equivalent of "Broken Arrow." UWE activates runtime One-Way Mission (OWM / LLD-5) decorators: uncapping thermal limits, commanding 15G defensive turns, and transforming recon platforms into sacrificial kinetic rams to save human lives.
        </div>
        <div style="background:#111827; padding:0.85rem 1rem; border-radius:6px; border:1px solid #1f2937;">
          <strong style="color:#3fb950;">Phase 5: Post-Engagement Recovery &amp; Sleeper Fortresses:</strong> UWE coordinates autonomous CASEVAC, schedules 15-minute fast charging, and settles subsea nodes back into the seabed in low-power "Zhdun" sleeper mode (LLD-3). Master Sergeant UWE reports: <em>"Fleet re-armed, defensive pickets silent, awaiting orders, Sir."</em>
        </div>
      </div>
    </section>

    <!-- Section 3: APM vs CPM -->
    <section class="reddit-card" style="border-left:4px solid var(--green);">
      <h2 style="color:#3fb950; margin-top:0;">3. Cognitive Discrimination: APM vs. CPM</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        Military leaders rightly fear the <em>"twitch-panic"</em> scenario — the fear that an overstimulated operator will panic-click and trigger an unintended kinetic escalation. UWE neutralizes this through a strict architectural separation:
      </p>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1rem; margin:1.25rem 0;">
        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="color:#3fb950; font-size:1.1rem;">APM: 300–400 Actions/min</strong>
            <span class="badge" style="background:#122616; color:#3fb950;">MOTOR REALM</span>
          </div>
          <p style="font-size:0.88rem; color:#e6edf3; margin:0.25rem 0;"><strong>Function:</strong> Spatial maneuvering, sensory orientation, EW frequency hopping, re-grouping orders, and platform survival.</p>
          <p style="font-size:0.88rem; color:var(--text-muted); margin:0.25rem 0;"><strong>Mechanism:</strong> Fluid muscle memory, hotkeys, and precision manipulator inputs.</p>
          <div style="margin-top:0.75rem; font-size:0.85rem; color:#3fb950; font-weight:600;">🛡️ ZERO LETHAL DANGER: High APM manipulates kinematics and telemetry; it cannot authorize an explosive train.</div>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="color:#f85149; font-size:1.1rem;">CPM: 2–3 Commands/min</strong>
            <span class="badge" style="background:#2d1617; color:#f85149;">SOVEREIGN WILL</span>
          </div>
          <p style="font-size:0.88rem; color:#e6edf3; margin:0.25rem 0;"><strong>Function:</strong> Legally binding lethal authorization and strategic state shifts (OWM activation).</p>
          <p style="font-size:0.88rem; color:var(--text-muted); margin:0.25rem 0;"><strong>Mechanism:</strong> Deliberate, conscious execution signed via individual cryptographic tokens (<strong>STANAG 4754 / ED25519</strong>).</p>
          <div style="margin-top:0.75rem; font-size:0.85rem; color:#f85149; font-weight:600;">⚖️ SOVEREIGN ACCOUNTABILITY: Each command carries the weight of international law and sovereign defense.</div>
        </div>
      </div>

      <div style="background:#161b22; border:1px solid var(--border); border-radius:6px; padding:1rem; margin-top:1rem;">
        <h4 style="color:#fff; margin:0 0 0.5rem 0;">✈️ The "Nuclear Pilot" Standard &amp; Why Pure Gamers Fail</h4>
        <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin:0;">
          This standard mirrors a <strong>fighter pilot carrying tactical nuclear munitions</strong>: possessing superhuman subconscious motor control at 9G, paired with icy moral clarity regarding the weapon release switch. Pure esports gamers fail as combat commanders because tournaments occur in risk-free environments where defeat is merely a lost match; under kinetic artillery fire, unconditioned psychology fractures. In UWE doctrine, gamers serve strictly as <strong>Technical Instructors for ARM-SRM Simulators</strong> to drill muscle memory, while the combat seat is held exclusively by a commissioned officer bound by military oath.
        </p>
      </div>
    </section>

    <!-- Section 4: Reflex Loop & Shoot As Think -->
    <section class="reddit-card" style="border-left:4px solid var(--cyan);">
      <h2 style="color:#38bdf8; margin-top:0;">4. The Cyber-Physical Reflex Loop &amp; "I Shoot As I Think"</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        The transition from command intent to kinetic execution requires an indivisible three-stage <strong>Cyber-Physical Reflex Loop</strong>:
      </p>

      <div style="display:flex; flex-direction:column; gap:1rem; margin:1.25rem 0;">
        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <h4 style="color:#38bdf8; margin:0 0 0.35rem 0;">🔹 Stage I: Ergonomics of Intent — Why the Mechanical Manipulator Wins</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.5; margin:0 0 0.75rem 0;">
            Futuristic concepts often push gesture control or eye-tracking. In high-intensity combat, UWE rejects these gimmicks in favor of precision mechanical manipulators (mouse or trackball) for two definitive reasons:
          </p>
          <ul style="font-size:0.86rem; color:#c9d1d9; padding-left:1.2rem; margin:0; line-height:1.5;">
            <li><strong>Kinematic Precision of Hand-Arm Positioning:</strong> No interface matches the sub-pixel velocity and spatial vector navigation of a mechanical mouse or trackball. Eye-tracking suffers from involuntary saccadic jumps (10–30 ms micro-glances), while touchscreens block visual telemetry and lack tactile feedback under mechanical vibration.</li>
            <li><strong>The Manipulator as Proof of Conscious Intent:</strong> An eye flicker or gesture can occur reflexively due to flash, acoustic shock, or startle. Conversely, a physical cursor trajectory plus an intentional tactile click with resistance requires coordinated motor-cortex activation — the ultimate biological indicator of conscious intent.</li>
          </ul>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <h4 style="color:#d2a8ff; margin:0 0 0.35rem 0;">🔹 Stage II: The Biometric Sentinel — Fallout 4-STDFUA Protocol</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.5; margin:0 0 0.75rem 0;">
            Drawing on the real-time cybernetic feedback loops proven in the author's technical project <strong>Fallout 4-STDFUA</strong>, UWE implements an automated multimodal biometric fail-safe:
          </p>
          <ul style="font-size:0.86rem; color:#c9d1d9; padding-left:1.2rem; margin:0 0 0.75rem 0; line-height:1.5;">
            <li><strong>Metabolic &amp; Autonomic Monitoring:</strong> Continuous blood glucose monitoring prevents micro-tremors and tunnel vision from sudden glycemic drops during prolonged combat; HRV tensors detect physiological shock or cognitive stupor.</li>
            <li><strong>Somatic &amp; Acoustic Profiling ("Lie to Me" Effect):</strong> Vocal micro-tremor parsing distinguishes tactical commands from panic; real-time Facial Action Coding (FACS) detects catatonic freeze or shrapnel shock.</li>
          </ul>
          <div style="background:#161b22; border-left:3px solid #f85149; padding:0.75rem 1rem; border-radius:4px; font-size:0.85rem; color:#ff7b72;">
            <strong>🛡️ Automated Lethality Isolation:</strong> If acute trauma, shock, or panic is detected, erratic mouse movement is identified as an involuntary muscle spasm: <strong>the system immediately locks the lethal command line (CPM)</strong>, preventing accidental detonation, while Master Sergeant UWE takes the fleet into defensive station-keeping and transfers command up-chain.
          </div>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <h4 style="color:#7ee787; margin:0 0 0.35rem 0;">🔹 Stage III: The Operational Creed — "I Shoot As I Think" (Zero Translation Latency)</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.5; margin:0 0 1rem 0;">
            In the microsecond domain of Dagger Dogfights where closing speeds reach km/s and EW pulses blind standard radios, linear decision cycles are fatal: <em>"Shoot, then think"</em> leads to fratricide; <em>"Think, then shoot"</em> leads to destruction via adversary Edge-AI translation latency. The UWE Officer operates under the creed: <strong>"I Shoot As I Think" (Стріляю, як думаю)</strong>.
          </p>
          
          <div style="text-align:center;">
            <img src="../assets/img/hal_moore_shoot_as_think.png" alt="Lt. Col. Hal Moore executing command and kinetic fire simultaneously" style="width:100%; max-width:850px; height:auto; border-radius:6px; border:1px solid var(--border); box-shadow:0 4px 20px rgba(0,0,0,0.5);">
            <p style="font-size:0.83rem; color:var(--text-muted); margin-top:0.5rem;">
              <em>Figure 2: The Physical Embodiment of "I Shoot As I Think" — Lt. Col. Hal Moore in the Ia Drang firefight. Handset to ear coordinating sovereign multi-domain fires (CPM), while his rifle simultaneously engages charging assault waves (APM). Zero translation latency between thought, command, and kinetic delivery.</em>
            </p>
          </div>

          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:0.75rem; margin-top:1rem;">
            <div style="background:#161b22; padding:0.85rem; border-radius:4px; font-size:0.85rem; color:var(--text-muted);">
              <strong style="color:#58a6ff;">Dual-Channel Synchronization:</strong> Left hand on the tactical radio (Sovereign CPM Channel), right hand firing rifle into smoke (Kinematic APM Execution).
            </div>
            <div style="background:#161b22; padding:0.85rem; border-radius:4px; font-size:0.85rem; color:var(--text-muted);">
              <strong style="color:#3fb950;">Elimination of the Pause:</strong> No pausing to deliberate. Tactical assessment, strategic command, and kinetic defense merge into a single physiological act.
            </div>
            <div style="background:#161b22; padding:0.85rem; border-radius:4px; font-size:0.85rem; color:var(--text-muted);">
              <strong style="color:#38bdf8;">Direct Kill-Web Driving:</strong> The mind directs the swarm via sovereign intent; fingers immediately engage threats. Zero menu navigation lag.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Coastal Extraction & System Rescue -->
    <section class="reddit-card" style="border-left:4px solid var(--amber);">
      <h2 style="color:#d29922; margin-top:0;">5. The Coastal Extraction: Jane's Cold-State Topology &amp; System Rescue</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        The climax on the hostile coast in <em>G.I. Jane</em> anchors <strong>Lt. Jordan O'Neil</strong> in our human triad orbiting the <strong>Plumley Anchor (UWE Engine)</strong>:
      </p>

      <div style="text-align:center; margin:1.5rem 0;">
        <img src="../assets/img/jordan_oneil_coastal_rescue.jpg" alt="Lt. Jordan O'Neil on the Hostile Coast" style="width:100%; max-width:850px; height:auto; border-radius:6px; border:1px solid var(--border); box-shadow:0 4px 20px rgba(0,0,0,0.5);">
        <p style="font-size:0.85rem; color:var(--text-muted); margin-top:0.5rem;">
          <em>Figure 3: Lt. Jordan O'Neil on the Coastline — Shaved head, grime, comms headset active. Cold calculation under mortal stress: emotional responses cut, functioning as a pure tactical processor rescuing the system when automation fractures.</em>
        </p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:1rem; margin-top:1.25rem;">
        <div style="background:#111827; padding:1.2rem; border-radius:6px; border:1px solid #1f2937;">
          <h4 style="color:#fff; margin:0 0 0.5rem 0; font-size:1rem;">🔹 1. Firmness &amp; Calculation under Pressure (Твердість та Розрахунок)</h4>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Here on the coast her character is fully forged. Emotional noise is severed: her mind operates as a <strong>pure tactical processor</strong>, evaluating terrain vectors and hostile firing positions with algorithmic detachment.
          </p>
        </div>

        <div style="background:#111827; padding:1.2rem; border-radius:6px; border:1px solid #1f2937;">
          <h4 style="color:#38bdf8; margin:0 0 0.5rem 0; font-size:1rem;">🔹 2. Real-Time Interaction with Master Sergeant UWE (Взаємодія з UWE)</h4>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Her gaze on the collage, directed toward Master Sergeant UWE, represents <strong>absolute tactical synchronization</strong>. She does not ask the machine for advice; she commands at the speed UWE links orbital satellites (<code>UOV</code>) and strike drones (<code>UCV</code>) into a unified Kill Web.
          </p>
        </div>

        <div style="background:#111827; padding:1.2rem; border-radius:6px; border:1px solid #1f2937;">
          <h4 style="color:#e3b341; margin:0 0 0.5rem 0; font-size:1rem;">🔹 3. System Rescue: Overriding Crippled Automation (Рятування системи)</h4>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Her mission on that coast is the rescue of Master Chief. In UWE doctrine, this carries vital architectural meaning: a human with this mindset <strong>saves the cyber-physical system itself</strong> when automation (the AI Sergeant) is damaged, blinded by EW strikes, or trapped in an algorithmic deadlock.
          </p>
        </div>

        <div style="background:#111827; padding:1.2rem; border-radius:6px; border:1px solid #1f2937;">
          <h4 style="color:#3fb950; margin:0 0 0.5rem 0; font-size:1rem;">🔹 4. The Antifragile Human Guardian</h4>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5; margin:0;">
            This episode provides the definitive proof: a UWE Fleet Officer forged with Jane's character <strong>never fractures before supercritical challenges on the real-world battlefield</strong>.
          </p>
        </div>
      </div>
    </section>

    <!-- Section 6: Character Synthesis & Maverick Kinematic Boundary -->
    <section class="reddit-card" style="border-left:4px solid var(--red);">
      <h2 style="color:#ff7b72; margin-top:0;">6. The Trinity of Command: Character Synthesis &amp; Maverick at 9G</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        Neither Maverick, Moore, nor O'Neil is a ready-made UWE Officer. What unites them is <strong>acceptance of the physical reality of combat (Law I)</strong> and non-linear decision-making. The UWE Officer is an engineered psychological alloy:
      </p>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:1rem; margin:1.25rem 0;">
        <div style="background:#161b22; border:1px solid var(--border); border-radius:6px; padding:1.2rem;">
          <h4 style="color:#58a6ff; margin:0 0 0.5rem 0;">🎖️ The Hal Moore Component</h4>
          <div style="font-size:0.82rem; color:#3fb950; font-weight:700; margin-bottom:0.4rem;">MORAL SOVEREIGNTY &amp; CPM ANCHOR</div>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Absolute fidelity to the military oath, ethical command, and human stewardship. The officer never views robotic fleets as a video game; they carry sovereign accountability under the Law of Armed Conflict, holding the cryptographic key that authorizes lethal force.
          </p>
        </div>

        <div style="background:#161b22; border:1px solid var(--border); border-radius:6px; padding:1.2rem;">
          <h4 style="color:#38bdf8; margin:0 0 0.5rem 0;">🌊 The Jordan O'Neil Component</h4>
          <div style="font-size:0.82rem; color:#38bdf8; font-weight:700; margin-bottom:0.4rem;">SPATIAL TELEMETRY &amp; PREDICTIVE OODA</div>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Compressed situational awareness and total elimination of panic under extreme stress. Reads compressed 6-character tokens across 6 operating domains simultaneously, anticipating edge-AI maneuvers before network bottlenecks register.
          </p>
        </div>

        <div style="background:#161b22; border:1px solid var(--border); border-radius:6px; padding:1.2rem;">
          <h4 style="color:#ff7b72; margin:0 0 0.5rem 0;">⚡ The Pete Maverick Component</h4>
          <div style="font-size:0.82rem; color:#ff7b72; font-weight:700; margin-bottom:0.4rem;">KINEMATIC PRIMACY &amp; 9G ADAPTATION</div>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Rejection of administrative dogma in favor of immutable physical laws. In high-G crises (Dagger Dogfights), pushes platforms to structural limits, overriding peacetime limiters because they know the metal will hold.
          </p>
        </div>
      </div>

      <!-- Maverick 9G Kinematic Boundary Embedded Focus -->
      <div style="background:#111827; border:1px solid #372020; border-radius:8px; padding:1.5rem; margin-top:1.5rem;">
        <h3 style="color:#ff7b72; margin-top:0; font-size:1.2rem;">✈️ Capt. Pete Maverick: Kinematic Boundary Testing &amp; Dagger Dogfights</h3>
        <p style="color:#e6edf3; font-size:0.92rem; line-height:1.6;">
          In autonomous warfare, tactical failure stems from peacetime doctrinal dogma — believing that simulation boundaries and safety interlocks represent the absolute limit of the physical platform. Maverick demonstrates the core tenet of <strong>UWE Law I (Kinematic Primacy)</strong>: when the mission hangs in the balance, physical dynamics take absolute precedence over bureaucratic constraints.
        </p>

        <div style="text-align:center; margin:1.5rem 0;">
          <img src="../assets/img/maverick_dagger_dogfight.png" alt="Capt. Pete Maverick Mitchell executing 9G Dagger Dogfight maneuvers" style="width:100%; max-width:850px; height:auto; border-radius:6px; border:1px solid #7f1d1d; box-shadow:0 4px 20px rgba(0,0,0,0.6);">
          <p style="font-size:0.85rem; color:var(--text-muted); margin-top:0.5rem;">
            <em>Figure 4: Capt. Pete "Maverick" Mitchell at 9G in Dagger Dogfight — Soft tissue deformed under massive kinematic pressure, executing supercritical maneuvers outside peacetime NATO doctrine. Proving that when physical metal holds, human cognitive and motor will pushes autonomous interceptors to the theoretical edge of the aerodynamic envelope.</em>
          </p>
        </div>

        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1rem; margin-top:1rem;">
          <div style="background:#161b22; padding:1rem; border-radius:6px; border:1px solid var(--border);">
            <strong style="color:#ff7b72;">Shattering Peacetime Limiters:</strong>
            <p style="font-size:0.85rem; color:var(--text-muted); margin:0.3rem 0 0 0; line-height:1.5;">
              Standard flight computers enforce conservative G-limiters to preserve airframe service life. In Dagger Dogfights where adversary loitering munitions and interceptors close at supersonic speeds, the UWE Officer overrides peacetime envelopes, commanding 12G–15G terminal turns because the kinetic imperative demands victory.
            </p>
          </div>
          <div style="background:#161b22; padding:1rem; border-radius:6px; border:1px solid var(--border);">
            <strong style="color:#3fb950;">Physical Envelope Primacy:</strong>
            <p style="font-size:0.85rem; color:var(--text-muted); margin:0.3rem 0 0 0; line-height:1.5;">
              Software cannot alter lift curves or energy dissipation. Maverick’s mindset roots autonomous C2 in pure physics: the pilot does not negotiate with the interface; they execute at the structural bleeding edge where fluid dynamics, wing loading, and thrust vectors meet.
            </p>
          </div>
        </div>
      </div>

      <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1rem; margin-top:1.25rem;">
        <strong style="color:#bc8cff;">⚙️ The Basil Plumley Anchor (The Cyber-Physical Engine):</strong>
        <p style="font-size:0.88rem; color:var(--text-muted); margin:0.35rem 0 0 0; line-height:1.5;">
          These three human dimensions converge around the <strong>Plumley Anchor (UWE Engine)</strong>: a tireless, objective master sergeant executing kinematics, containerization, and fail-safe supervision. The machine protects the human from physiological errors; the human infuses the machine with sovereign moral intent.
        </p>
      </div>
    </section>

    <!-- Section 7: Visual Strategy -->
    <section class="reddit-card" style="border-left:4px solid var(--purple);">
      <h2 style="color:#d2a8ff; margin-top:0;">7. Visual Strategy: Parade Dress Title vs. Combat Grime Reality</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        To communicate this architecture to defense leaders without triggering bureaucratic resistance, the visual series establishes an intentional cognitive progression across two distinct visual registers:
      </p>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.25rem; margin:1.25rem 0;">
        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <h3 style="color:#58a6ff; font-size:1.1rem; margin-top:0;">🎖️ Level I: The Title Collage (Parade Uniforms &amp; Sovereign Legitimacy)</h3>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5;">
            The cover image (<strong>Figure 1</strong>) presents the <strong>Command Trinity in Service Dress Uniforms</strong>, radiating constitutional legitimacy, tradition, and discipline:
          </p>
          <ul style="font-size:0.84rem; color:#c9d1d9; padding-left:1.2rem; margin:0.5rem 0; line-height:1.6;">
            <li><strong style="color:#58a6ff;">Top Canopy (Lt. Col. Hal Moore):</strong> In field helmet and cavalry blue ascot, gazing with paternal resolve (<em>"I will leave no man behind"</em>).</li>
            <li><strong style="color:#bc8cff;">Central Anchor (CSM Basil Plumley / Sam Elliott):</strong> General dress uniform with a predatory squint and faint, knowing smile — the confident, unflinching engine ready for battle.</li>
            <li><strong style="color:#38bdf8;">Left Wing (Lt. Jordan O'Neil):</strong> Immaculate USN service dress white uniform and cover, radiating cold analytical precision.</li>
            <li><strong style="color:#ff7b72;">Right Wing (Capt. Pete Mitchell):</strong> USN service dress blue uniform, executing a sharp, formal hand salute with focused intensity.</li>
          </ul>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1.2rem;">
          <h3 style="color:#ff7b72; font-size:1.1rem; margin-top:0;">⚡ Level II: In-Text Kinetic Realism (The Dagger Dogfight Climax)</h3>
          <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.5;">
            As the reader transitions into the kinetic mechanics of autonomous warfare, the visual series pivots into raw, unadorned combat reality:
          </p>
          <ul style="font-size:0.84rem; color:#c9d1d9; padding-left:1.2rem; margin:0.5rem 0; line-height:1.6;">
            <li><strong style="color:#58a6ff;">Moore in Ia Drang (Figure 2):</strong> Tactical radio handset to ear directing multi-domain fires while his rifle engages charging assault waves — the raw physical embodiment of <em>"I Shoot As I Think."</em></li>
            <li><strong style="color:#38bdf8;">O'Neil on Hostile Coast (Figure 3):</strong> Shaved head, grime-streaked face, headset keyed, scanning terrain contours to rescue her wounded Master Chief / save the system.</li>
            <li><strong style="color:#ff7b72;">Maverick at 9G (Figure 4):</strong> Soft tissue deformed under massive kinematic pressure, executing supercritical maneuvers outside peacetime NATO doctrine.</li>
          </ul>
        </div>
      </div>

      <h3 style="color:#fff; font-size:1.1rem; margin-top:1.5rem;">📐 Complete Lexicon &amp; Architectural Mapping of the UWE Master Infographic</h3>
      <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.5;">
        Every visual badge, vector, and arc on the master infographic corresponds to an exact cyber-physical subsystem:
      </p>

      <div style="display:flex; flex-direction:column; gap:0.75rem; font-size:0.88rem; margin-top:1rem;">
        <div style="background:#161b22; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
          <strong style="color:#fff;">1. Central Anchor (Sam Elliott / Plumley):</strong> 
          <code style="color:#58a6ff;">[INVARIANT HAL ANCHOR | FALLOUT 4-STDFUA MULTIMODAL SUITE]</code> — The machine executor managing the 44px pressure gauge dial across 6 saturated domains (<code>UOV • SPACE</code>, <code>UAV • AIR</code>, <code>UCV • STRIKE</code>, <code>UGV • GROUND</code>, <code>USV • SURFACE</code>, <code>UUV • SUBSEA</code>).
        </div>
        <div style="background:#161b22; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
          <strong style="color:#fff;">2. Top Apex Node (Mel Gibson / Moore):</strong> 
          <code style="color:#3fb950;">[2-3 CPM | IA DRANG DOCTRINE | 'FIRST ON GROUND, LAST TO LEAVE']</code> — Sovereign moral core and lethal authorization token holder.
        </div>
        <div style="background:#161b22; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
          <strong style="color:#fff;">3. Left Wing Node (Demi Moore / O'Neil):</strong> 
          <code style="color:#38bdf8;">[ANTIFRAGILE COGNITIVE TOPOLOGY | PREDICTIVE SYNTHESIS]</code> — Spatial telemetry, extraction coordination, and multi-domain OODA loop.
        </div>
        <div style="background:#161b22; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
          <strong style="color:#fff;">4. Right Wing Node (Tom Cruise / Maverick):</strong> 
          <code style="color:#ff7b72;">[300-400 APM | TERMINAL INTERCEPTION | ZERO LATENCY]</code> — Tactical motor reflex and supercritical vectoring under extreme physical stress.
        </div>
      </div>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1rem; margin-top:1rem;">
        <div style="background:#161b22; padding:1rem; border-radius:6px; border:1px solid var(--border);">
          <h4 style="color:#fff; margin:0 0 0.5rem 0;">Connecting Arcs &amp; Subordination Conduits</h4>
          <ul style="font-size:0.82rem; color:var(--text-muted); padding-left:1.2rem; margin:0; line-height:1.5;">
            <li><code>DOCTRINAL INTENT &lt;---&gt; SPATIAL SITUATIONAL AWARENESS</code>: Binds Moore's moral mandate to O'Neil's spatial telemetry.</li>
            <li><code>6-DOMAIN KILL-WEB &lt;---&gt; KINEMATIC INTERCEPTION</code>: Binds O'Neil's predictive sensor synthesis to Maverick's interceptors.</li>
            <li><code>HIGH-G KINETIC FEEDBACK &lt;---&gt; SOVEREIGN LETHAL OATH</code>: Feeds real-time kinetic results back into sovereign command.</li>
            <li><code>CPM SOVEREIGN FIRE ORDER ---&gt; HAL INVARIANT</code>: Cryptographic release of lethal authorization.</li>
          </ul>
        </div>

        <div style="background:#161b22; padding:1rem; border-radius:6px; border:1px solid var(--border);">
          <h4 style="color:#fff; margin:0 0 0.5rem 0;">Radial Echelon Hierarchy &amp; Environmental Horizons</h4>
          <ul style="font-size:0.82rem; color:var(--text-muted); padding-left:1.2rem; margin:0; line-height:1.5;">
            <li><strong>Concentric Radar Rings (Echelons I–VIII):</strong> Scaling from single platform (Echelon I) to Multi-Kill-Web (Echelon IV, 30–50 nodes), Battalion (Echelon V, 150–200 nodes), up to Theater 6-Domain C4ISR (Echelon VIII).</li>
            <li><strong>4 Environmental Horizons:</strong> Exoatmosphere/Orbital (<code>UOV</code>), Air-Ground Troposphere (<code>UAV</code>/<code>UCV</code>), Terrestrial/Littoral (<code>UGV</code>), Subsea Pelagic/Abyssal (<code>USV</code>/<code>UUV</code>).</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Section 8: Conclusion -->
    <section class="reddit-card" style="border-left:4px solid var(--green); background:rgba(63, 185, 80, 0.04);">
      <h2 style="color:#3fb950; margin-top:0;">8. Conclusion: The Sovereign Shield</h2>
      <p style="color:#e6edf3; font-size:1.05rem; line-height:1.7; font-weight:500;">
        The <strong>Unmanned Warfare Engine (UWE)</strong> does not build robotic toys, nor does it displace human responsibility. It builds the software-defined shield that will protect the Free World from Scandinavian fjords to the Black Sea.
      </p>
      <p style="color:#c9d1d9; font-size:0.95rem; line-height:1.6;">
        By combining tournament-grade mechanical APM with sovereign moral CPM, anchored by the <strong>Fallout 4-STDFUA</strong> real-time fail-safe and grounded in immutable physical laws, we forge an officer capable of winning the wars of tomorrow.
      </p>
      <div style="margin-top:1.25rem; font-size:0.9rem; color:#8b949e; text-align:right; font-style:italic;">
        — Serhii Khylevych, Kyiv, 2026
      </div>
    </section>

    <!-- Section 9: Deep Crosslink Matrix -->
    <section class="reddit-card" style="border-left:4px solid var(--accent); background:rgba(31, 111, 235, 0.04);">
      <h2 style="color:#58a6ff; margin-top:0;">9. Deep Cross-Domain &amp; Empirical Benchmark Topology</h2>
      <p style="color:var(--text-muted); font-size:0.92rem; margin-bottom:1.25rem;">
        The Cyber-Physical Officer orchestrates across the full spectrum of UWE physical domains, empirical benchmarks, and HAL contracts:
      </p>

      <h3 style="font-size:1.05rem; color:#fff; margin-bottom:0.75rem;">🌐 Six Operating Physical Medium Domains</h3>
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap:0.75rem; margin-bottom:1.5rem;">
        <a href="../domains/uav.html" class="badge badge-uav" style="padding:0.6rem; font-size:0.85rem; text-align:center; text-decoration:none;">UAV • Air Troposphere</a>
        <a href="../domains/ucv.html" class="badge badge-ucv" style="padding:0.6rem; font-size:0.85rem; text-align:center; text-decoration:none;">UCV • Combat Strike</a>
        <a href="../domains/ugv.html" class="badge badge-ugv" style="padding:0.6rem; font-size:0.85rem; text-align:center; text-decoration:none;">UGV • Ground Terrain</a>
        <a href="../domains/usv.html" class="badge badge-usv" style="padding:0.6rem; font-size:0.85rem; text-align:center; text-decoration:none;">USV • Surface Vessels</a>
        <a href="../domains/uuv.html" class="badge badge-uuv" style="padding:0.6rem; font-size:0.85rem; text-align:center; text-decoration:none;">UUV • Subsea Depths</a>
        <a href="../domains/uov.html" class="badge badge-uov" style="padding:0.6rem; font-size:0.85rem; text-align:center; text-decoration:none;">UOV • Orbital Space</a>
      </div>

      <h3 style="font-size:1.05rem; color:#fff; margin-bottom:0.75rem;">🔬 Key Empirical Benchmarks Governing C2 Symbiosis</h3>
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:0.75rem; margin-bottom:1.5rem;">
        <a href="../cases/13-fury-ghostbat.html" style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:0.75rem; text-decoration:none; color:inherit; display:block;">
          <strong style="color:#58a6ff; font-size:0.9rem;">Case #13: Anduril Fury / Ghost Bat</strong>
          <p style="font-size:0.8rem; color:var(--text-muted); margin:0.25rem 0 0 0;">Loyal Wingman collaborative combat aircraft validating the APM/CPM pilot handshake.</p>
        </a>
        <a href="../cases/01-honda-evtol.html" style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:0.75rem; text-decoration:none; color:inherit; display:block;">
          <strong style="color:#58a6ff; font-size:0.9rem;">Case #01: Honda eVTOL GT-HEV</strong>
          <p style="font-size:0.8rem; color:var(--text-muted); margin:0.25rem 0 0 0;">Piecewise energy budget proving hover vs cruise power limits during transition.</p>
        </a>
        <a href="../cases/02-slimak-ugv.html" style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:0.75rem; text-decoration:none; color:inherit; display:block;">
          <strong style="color:#bc8cff; font-size:0.9rem;">Case #02: НРК SlimAk UGV</strong>
          <p style="font-size:0.8rem; color:var(--text-muted); margin:0.25rem 0 0 0;">Articulated ground chassis kinematics vs marketing myths of adaptive suspension.</p>
        </a>
        <a href="../cases/06-exail-usv.html" style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:0.75rem; text-decoration:none; color:inherit; display:block;">
          <strong style="color:#38bdf8; font-size:0.9rem;">Case #06: Exail DriX USV</strong>
          <p style="font-size:0.8rem; color:var(--text-muted); margin:0.25rem 0 0 0;">Wave-piercing surface hull hydrodynamics and acoustic silent station-keeping.</p>
        </a>
        <a href="../cases/07-ghostshark-auv.html" style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:0.75rem; text-decoration:none; color:inherit; display:block;">
          <strong style="color:#58a6ff; font-size:0.9rem;">Case #07: Ghost Shark XL-AUV</strong>
          <p style="font-size:0.8rem; color:var(--text-muted); margin:0.25rem 0 0 0;">Autonomous subsea sleeper fortress resting on the continental shelf awaiting C2 activation.</p>
        </a>
      </div>

      <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1rem;">
        <strong style="color:#d29922;">⚙️ Hardware Abstraction Layer Registry:</strong>
        <p style="font-size:0.85rem; color:var(--text-muted); margin:0.25rem 0 0 0;">
          Explore the deterministic control contracts governing lift transition (<code>IVtolTransitionDrive</code>), articulated steering (<code>IArticulatedChassis</code>), and surface sea-keeping (<code>ISurfacePlanner</code>): 
          <a href="../hal/index.html" style="color:#58a6ff; margin-left:0.5rem;">View Complete HAL Registry →</a>
        </p>
      </div>
    </section>
  </div>
  {render_footer()}
</body>
</html>"""
    write_file("c2/officer.html", html)

def build_c2_articles():
    case = next(c for c in CASES_DATA if c["slug"] == "32-izzy-fried-c2")
    title = "Joint Cross-Domain Unmanned Operation"
    jsonld = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": title,
        "author": {"@type": "Person", "name": "Serhii Khylevych"},
        "datePublished": "2026-11-07",
        "citation": "https://lnkd.in/p/d9qXKrmm",
        "mainEntityOfPage": f"{BASE_URL}/{C2_ARTICLE_PATH}",
    }
    article = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html_mod.escape(title)} | UWE C2 Articles</title>
  <meta name="description" content="Case #32: Izzy Fried / Fox2Sierra and UWE multi-layer stratification across air, ground, and maritime domains.">
  <link rel="canonical" href="{BASE_URL}/{C2_ARTICLE_PATH}">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script type="application/ld+json">
{json.dumps(jsonld, indent=2)}
  </script>
</head>
<body>
  {render_header("c2", depth=1)}
  <main class="container" style="max-width:960px;">
    <p><a href="index.html">← C2 Articles</a></p>
    <article class="reddit-card">
      <div class="card-meta">Serhii Khylevych · Expertise Ledger record: 2026-11-07 · Case #32</div>
      <h1 class="hero-title">{title}</h1>
      <p>Izzy Fried / Fox2Sierra</p>
      <div class="lesson-box">C2 is the cross-domain orchestration layer. Its taxonomy is not yet defined; this article does not introduce a seventh physical domain.</div>
      <p><strong>Ledger source:</strong> <a href="https://lnkd.in/p/d9qXKrmm" target="_blank" rel="noopener">Izzy Fried — LinkedIn Post ↗</a></p>
      <p><strong>UWE Tokens:</strong> <code>C2: MB-HR-GW</code>, <code>UAV: AL-TC-DR</code>, <code>UGV: GL-EM-DR</code>, <code>USV: SL-PA-DR</code></p>
      <h2>HAL Contract</h2>
      <p><code>ICrossDomainKillWebRouter</code> &amp; <code>IMultiBearerCommsGateway</code></p>
      <blockquote>Joint cross-domain autonomy requires ICrossDomainKillWebRouter and IMultiBearerCommsGateway to resolve heterogeneous telemetry into unified execution APIs.</blockquote>
      <h2>Validation</h2>
      <p>Confirms UWE 3-Tier Multi-Layer Architecture (MDO Strategic Intent ➔ UWE Meta-Layer Operational Engine ➔ CPS: HAL/EAL Execution) across air, ground, and maritime domains.</p>
      <h2>Vulnerability</h2>
      <p>Proprietary point-to-point command links create vendor lock-in and collapse under multi-domain EW.</p>
      <h2>Architectural Lesson</h2>
      <p>Validates UWE Multi-Layer Stratification; heterogeneous swarms require unified HAL abstraction rather than bespoke C2 integration.</p>
      <p><a href="../cases/{case['slug']}.html">Case #32: existing benchmark analysis →</a></p>
      <p>The benchmark record retains its original source, date, and interface terminology; the ledger-derived summary above is identified separately.</p>
      <p><a href="officer.html">Related article: The Cyber-Physical Officer — Human-Machine Symbiosis →</a></p>
    </article>
  </main>
  {render_footer()}
</body>
</html>"""
    write_file(C2_ARTICLE_PATH, article)
    index = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>C2 Articles &amp; Cross-Domain Orchestration | UWE</title>
  <meta name="description" content="UWE C2 articles: human-machine symbiosis and joint cross-domain unmanned operations, separate from the six physical-domain taxonomies.">
  <link rel="canonical" href="{BASE_URL}/c2/index.html">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
  {render_header("c2", depth=1)}
  <main class="container">
    <h1 class="hero-title">C2 Articles &amp; Cross-Domain Orchestration</h1>
    <p>C2 taxonomy is not yet defined. These articles address orchestration across the <a href="../domains/index.html">six physical domains</a>, not a seventh physical domain.</p>
    <article class="reddit-card">
      <h2><a href="officer.html">The Cyber-Physical Officer: Human-Machine Symbiosis in UWE</a></h2>
      <p>The existing Officer Symbiosis whitepaper and its human-machine command doctrine.</p>
    </article>
    <article class="reddit-card">
      <h2><a href="{Path(C2_ARTICLE_PATH).name}">{title}</a></h2>
      <p>Case #32 — Izzy Fried / Fox2Sierra. Existing benchmark analysis and the Expertise Ledger record of UWE multi-layer stratification.</p>
      <a href="../cases/{case['slug']}.html">View benchmark record →</a>
    </article>
  </main>
  {render_footer()}
</body>
</html>"""
    write_file("c2/index.html", index)


def build_seo_assets():
    # 1. Sitemap.xml
    urls = [
        f"{BASE_URL}/index.html",
        f"{BASE_URL}/domains/index.html",
        f"{BASE_URL}/cases/index.html",
        f"{BASE_URL}/c2/index.html",
        f"{BASE_URL}/c2/officer.html",
        f"{BASE_URL}/{C2_ARTICLE_PATH}",
f"{BASE_URL}/vendors/index.html",
        f"{BASE_URL}/hal/index.html",
        f"{BASE_URL}/consulting.html",
    ]
    for d in DOMAINS_DATA:
        urls.append(f"{BASE_URL}/domains/{d['code'].lower()}.html")
    for c in CASES_DATA:
        urls.append(f"{BASE_URL}/cases/{c['slug']}.html")

    sitemap_entries = "\n".join(f"""  <url>
    <loc>{u}</loc>
<lastmod>2026-11-23</lastmod>
    <changefreq>weekly</changefreq>
<priority>{'1.0' if u.endswith('index.html') and 'cases/' not in u and 'domains/' not in u else ('0.9' if 'c2/' in u or 'consulting.html' in u else '0.8')}</priority>
  </url>""" for u in urls)

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}
</urlset>"""
    write_file("sitemap.xml", sitemap_xml)

    # 2. Robots.txt
    robots = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    write_file("robots.txt", robots)

def purge_stale_cases(docs_root):
    cases_dir = (Path(docs_root) / "cases").resolve()
    if cases_dir.exists():
        for p in cases_dir.glob("[0-9][0-9]-*.html"):
            rp = p.resolve()
            if rp.is_relative_to(cases_dir) and not p.is_symlink() and p.name != "index.html":
                try:
                    p.unlink()
                except OSError as e:
                    raise ValueError(f"Failed to purge stale case file {p}: {e}")

TOKEN_RE = re.compile(r"^[A-Z][A-Z0-9]{1,2}: [A-Z]{2}-[A-Z]{2}-[A-Z]{2}$")
UW_SF_RE = re.compile(r"\bUW[SF]\b")
ALLOWED_TYPES = {
    "OEM", "Frontline Cluster", "Research Source", "Strategic Architect",
    "Military Trial Center", "Defense Think-Tank", "Strategic Source", "Defense Force Source"
}
ALLOWED_DOMAINS = {"UAV", "UCV", "UGV", "USV", "UUV", "UOV", "C2"}
ALLOWED_COLLISIONS = {
    "UAV: AI-CP-HL": {"04-waverider-corvus", "05-sickle-wing"},
    "UOV: LM-CA-HR": {"10-orbital-guardian", "31-spm-kondratyuk"},
    "UUV: CV-IS-HQ": {"11-lockheed-lamprey", "29-fitburg-sentinel"},
    "UGV: GL-DC-DR": {"14-knds-centurio", "24-lurtz-kill-zone"},
    "UGV: GL-EM-DR": {"17-frodo-ugv", "27-rusi-rasputitsa"},
    "UAV: AC-RE-AQ": {"23-lpp-jwi4000", "25-stat-caylus-b2lt"},
}

def validate_uwe_integrity(cases, vendors, domains, docs_root):
    if len(cases) != 54:
        raise ValueError(f"Expected 54 cases, found {len(cases)}")
    if len({c["slug"] for c in cases}) != 54:
        raise ValueError("Duplicate case slug detected")
    if len(vendors) != 52:
        raise ValueError(f"Expected 52 vendors, found {len(vendors)}")
    if len({v["slug"] for v in vendors}) != 52:
        raise ValueError("Duplicate vendor slug detected")
    if len(domains) != 6 or {d["code"] for d in domains} != ALLOWED_DOMAINS - {"C2"}:
        raise ValueError("Expected the six physical domains, with C2 classified separately")

    domain_members = [slug for d in domains for slug in d["cases"]]
    physical_cases = {c["slug"] for c in cases if c["domain"] != "C2"}
    if set(domain_members) != physical_cases or len(domain_members) != len(physical_cases):
        raise ValueError("Physical-domain membership must cover each physical case exactly once")
    case_domains = {c["slug"]: c["domain"] for c in cases}
    for d in domains:
        if any(case_domains[slug] != d["code"] for slug in d["cases"]):
            raise ValueError(f"Incorrect case assignment in domain {d['code']}")

    for c in cases:
        prefix = f"{c['id']}-"
        if not c["slug"].startswith(prefix):
            raise ValueError(f"""Case {c["slug"]} does not start with ID prefix {prefix}""")

    vendor_slugs = {v["slug"] for v in vendors}
    for v in vendors:
        v_type = v.get("type")
        if v_type not in ALLOWED_TYPES:
            raise ValueError(f"""Vendor {v["slug"]} has invalid type: {v_type}""")

    used_vendors = set()
    token_to_slugs = {}
    for c in cases:
        v_slug = c.get("vendor_slug")
        if v_slug not in vendor_slugs:
            raise ValueError(f"""Case {c["slug"]} references unknown vendor {v_slug}""")
        used_vendors.add(v_slug)

        if c["domain"] not in ALLOWED_DOMAINS:
            raise ValueError(f"""Case {c["slug"]} has invalid domain: {c["domain"]}""")

        tok = c.get("token", "")
        if not TOKEN_RE.match(tok):
            raise ValueError(f"""Case {c["slug"]} has malformed token: {tok}""")
        if tok.split(":")[0] != c["domain"]:
            raise ValueError(f"""Case {c["slug"]} token prefix {tok.split(":")[0]} != domain {c["domain"]}""")

        if tok not in token_to_slugs:
            token_to_slugs[tok] = []
        token_to_slugs[tok].append(c["slug"])

    orphan_vendors = vendor_slugs - used_vendors
    if orphan_vendors:
        raise ValueError(f"Orphan vendors found without any associated cases: {orphan_vendors}")

    for tok, slugs in token_to_slugs.items():
        if len(slugs) > 1:
            if tok not in ALLOWED_COLLISIONS:
                raise ValueError(f"Unauthorized token collision for {tok}: {slugs}")
            if set(slugs) != ALLOWED_COLLISIONS[tok]:
                raise ValueError(f"Collision mismatch for {tok}: expected {ALLOWED_COLLISIONS[tok]}, got {set(slugs)}")

    for tok, expected_slugs in ALLOWED_COLLISIONS.items():
        if tok not in token_to_slugs:
            raise ValueError(f"Declared collision token {tok} does not occur in cases")
        if set(token_to_slugs[tok]) != expected_slugs:
            raise ValueError(f"Declared collision {tok} mismatch in cases")

    cases_dir = (Path(docs_root) / "cases").resolve()
    generated_case_files = list(cases_dir.glob("[0-9][0-9]-*.html"))
    if len(generated_case_files) != 54:
        raise ValueError(f"Expected 54 generated case files, found {len(generated_case_files)}")
    for rel_path in ("c2/index.html", C2_ARTICLE_PATH):
        if not (Path(docs_root) / rel_path).is_file():
            raise ValueError(f"Missing C2 article page: {rel_path}")

    for p in Path(docs_root).rglob("*"):
        if not p.is_file() or p.suffix.lower() not in {".html", ".xml", ".txt", ".js", ".json", ".css"}:
            continue
        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            raise ValueError(f"Failed to read {p}: {e}")

        m = UW_SF_RE.search(content)
        if m:
            snippet = content[max(0, m.start() - 25):min(len(content), m.end() + 25)].replace("\n", " ")
            if "UWE-concept-proof" not in snippet:
                raise ValueError(f"Forbidden acronym leak in {p}: ...{snippet}...")

        if "/home/hills/" in content:
            idx = content.find("/home/hills/")
            snippet = content[max(0, idx - 20):min(len(content), idx + 40)].replace("\n", " ")
            raise ValueError(f"Workspace path leak in {p}: ...{snippet}...")

    print("🛡️ [INTEGRITY CHECK PASSED] All 54 cases, 52 vendors, 6 physical domains, C2 articles and docs/ validated with zero leaks.")

def main():
    print("=" * 65)
    print("🚀 Building Unmanned Warfare Engine (UWE) Documentation Portal")
    print(f"📁 Target Output: {DOCS}")
    print("=" * 65)
    
    purge_stale_cases(DOCS)
    generate_css()
    generate_js()
    build_index()
    build_cases_index()
    build_case_pages()
    build_domains()
    build_c2_officer()
    build_c2_articles()
    build_vendors()
    build_hal()
    build_consulting()
    build_seo_assets()
    validate_uwe_integrity(CASES_DATA, VENDORS_DATA, DOMAINS_DATA, DOCS)
    
    print(f"\n✅ Build Complete! {len(CASES_DATA)} Cases, {len(DOMAINS_DATA)} Domains, C2 Officer Symbiosis, {len(VENDORS_DATA)} Vendors & HAL Registry Generated.")
    print("📊 All pages include Schema.org JSON-LD and pre-rendered static HTML.")

if __name__ == "__main__":
    main()


