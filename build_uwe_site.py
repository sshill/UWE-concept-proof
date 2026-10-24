#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# [AI_PROVENANCE: TIER_2_GROQ | MODEL: openai/gpt-oss-120b]
import sys
import os
import re
import json
import shutil
from pathlib import Path

sys.dont_write_bytecode = True

WORKSPACE = Path(__file__).resolve().parent
DOCS = WORKSPACE / "docs"
BASE_URL = "https://uwe-standard.github.io"

# 13 Empirical Platform Benchmarks Metadata & Deep Cyber-Physical Content
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
    }
]

VENDORS_DATA = [
    {"slug": "anduril", "name": "Anduril Industries", "origin": "USA", "platforms": ["Anduril Fury (CCA)", "Ghost Shark XL-AUV", "ALTIUS Series"], "focus": "Autonomous defense-tech, Lattice OS, Collaborative Combat Aircraft, attritable robotic mass."},
    {"slug": "boeing", "name": "Boeing Defense, Space & Security", "origin": "USA / Australia", "platforms": ["MQ-25 Stingray CBARS", "MQ-28 Ghost Bat"], "focus": "Carrier-based unmanned aviation, aerial refueling infrastructure, modular CCA airframes."},
    {"slug": "lockheed-martin", "name": "Lockheed Martin (Skunk Works)", "origin": "USA", "platforms": ["Lamprey MMAUV", "U-2 / RQ-170 Heritage"], "focus": "Parasitic subsea autonomous systems, advanced stealth aerostructures, low-observable naval technologies."},
    {"slug": "exail", "name": "Exail Marine", "origin": "France", "platforms": ["DriX H-9 USV", "Oryx O-16 USV"], "focus": "Slender wave-piercing displacement unmanned surface vessels, drop-keel ASW hydrography, Sea State 5 endurance."},
    {"slug": "bae-falconworks", "name": "BAE Systems & Certo Aerospace", "origin": "UK", "platforms": ["CAPSTONE Coaxial Heavy-Lift UCV"], "focus": "Coaxial rotorcraft disc loading, 50% structural payload fraction, naval frigate deck operations."},
    {"slug": "unex", "name": "UNEX Automation", "origin": "Belgium / Ukraine", "platforms": ["ABRIS Amphibious Prime Mover"], "focus": "Heavy electric all-terrain logistics, robotic artillery towing, Bekker soil traction management."},
    {"slug": "honda", "name": "Honda Aircraft Company", "origin": "Japan / USA", "platforms": ["Honda eVTOL (GT-HEV)"], "focus": "Decoupled Lift+Cruise aerodynamics, gas turbine hybrid-electric powertrains, inter-city logistics."},
    {"slug": "frontline-ua", "name": "Ukrainian Frontline Defense-Tech", "origin": "Ukraine", "platforms": ["НРК SlimAk UGV", "Combat Multirotors", "Black Sea USVs"], "focus": "Asymmetric robotic warfare, articulated mud-conforming chassis, electronic warfare resilience, kinetic field prototyping."},
    {"slug": "nextgen-arsenal", "name": "NextGen Arsenal", "origin": "International", "platforms": ["Orbital Guardian ADR Hunter"], "focus": "Active Debris Removal, proximity operations (RPO), non-cooperative tumbling target capture, dual-use counter-space."},
    {"slug": "darpa", "name": "DARPA & Skunk Works Experimental", "origin": "USA", "platforms": ["Mach 6 Hypersonic Waverider (Corvus)"], "focus": "Hypersonic aerothermodynamics, compression lift waveriders, laser communications through plasma sheaths."},
    {"slug": "global-aerospace", "name": "Defense Aerospace Research", "origin": "USA / Global", "platforms": ["Transonic / Supersonic Stealth UCAV"], "focus": "Tailless blended wing-body stealth, internal weapons bays, aerothermal boundary layer dynamics."},
    {"slug": "hypersonic-consortium", "name": "Next-Gen Hypersonic Consortium", "origin": "International", "platforms": ["Autonomous Sickle Wing"], "focus": "Tailless sickle wing planforms, fluidic thrust vectoring (FTV), supersonic active flow control."}
]

DOMAINS_DATA = [
    {
        "code": "UAV",
        "name": "Unmanned Aerial Vehicles (Fixed-Wing & Hypersonic)",
        "medium": "Atmospheric Airspace (0 to 30 km)",
        "governing_laws": "Aerodynamic Lift-to-Drag (L/D), Mach number shock detachment, boundary-layer aerothermodynamics, wing loading.",
        "legacy_trap": "STANAG 4670 & DoD MTOW/HALE/MALE classifications rely on arbitrary weight and altitude boxes, ignoring kinetic threat omission limits and FPV interceptor speeds.",
        "cases": ["01-honda-evtol", "03-stealth-ucav", "04-waverider-corvus", "05-sickle-wing", "12-mq25-stingray", "13-fury-ghostbat"]
    },
    {
        "code": "UCV",
        "name": "Unmanned Copter Vehicles (Combat Multirotors & Coaxials)",
        "medium": "Low-Altitude Disc-Loaded Aerodynamics",
        "governing_laws": "Rotor disc loading (T/A), zero stall speed (V_stall = 0), momentum theory, advancing/retreating blade flapping dynamics.",
        "legacy_trap": "Conflating combat rotorcraft with hobbyist slang ('FPV'). FPV is a pilot screen mode, not a cyber-physical combat aircraft category.",
        "cases": ["09-capstone-coaxial"]
    },
    {
        "code": "UGV",
        "name": "Unmanned Ground Vehicles (Tactical Robotics & Prime Movers)",
        "medium": "Terrestrial & Amphibious Terrain",
        "governing_laws": "Bekker-Wong soil mechanics, drawbar pull (F_pull = μ * m * g), ground pressure (kg/cm²), rolling resistance, steering slip ratios.",
        "legacy_trap": "Amateur slang ('vozyk', 'cart') and marketing claims of 10-tonne towing based on electric motor kW while ignoring soil shear failure in mud.",
        "cases": ["02-slimak-ugv", "08-unex-artillery"]
    },
    {
        "code": "UUV",
        "name": "Unmanned Undersea Vehicles (Sub-Surface Robotics)",
        "medium": "Sub-surface Hydrospace (0 to 11,000m)",
        "governing_laws": "Hydrostatic pressure gradient (1 atm / 10m), acoustic transmission loss, acoustic cavitation, boundary-layer drag, parasitic energy harvesting.",
        "legacy_trap": "Classifying submersibles by geometric hull form factors (torpedo vs box) rather than physical Depth Horizons (D0 to D5) and acoustic signatures.",
        "cases": ["07-ghostshark-auv", "11-lockheed-lamprey"]
    },
    {
        "code": "USV",
        "name": "Unmanned Surface Vehicles (Littoral & Marine Vessels)",
        "medium": "Ocean Surface Boundary Layer (Air-Sea Interface)",
        "governing_laws": "Froude number, wave-piercing slender hull dynamics, Sea State (Beaufort scale) vertical g-shock limits, transverse metacentric height (GM_T).",
        "legacy_trap": "Using fragile recreational planing speedboats for open-ocean missions; high vertical g-shocks (>6g) destroy gimbal sensors and break hulls in Sea State 4+.",
        "cases": ["06-exail-usv"]
    },
    {
        "code": "UOV",
        "name": "Unmanned Orbital Vehicles (Counter-Space & Interceptors)",
        "medium": "Low Earth Orbit & Cislunar Space (160 to 36,000 km)",
        "governing_laws": "Keplerian two-body celestial mechanics, Clohessy-Wiltshire relative equations, Tsiolkovsky rocket equation ΔV limits, solar radiation pressure.",
        "legacy_trap": "Sci-fi free-flight orbital tropes: changing orbital inclination by 15° at LEO costs ~2,000 m/s ΔV, locking chemical hunters into narrow co-planar targets.",
        "cases": ["10-orbital-guardian"]
    }
]

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
                {"id": "09", "slug": "09-capstone-coaxial", "name": "CAPSTONE Coaxial", "insight": "Zero stall speed and disc loading strictly define UCV copter physics."}
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
                {"id": "13", "slug": "13-fury-ghostbat", "name": "Anduril Fury / MQ-28", "insight": "C2 dispersed runway operations enable distributed survivable air combat mass."}
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
                {"id": "13", "slug": "13-fury-ghostbat", "name": "Fury CCA", "insight": "Conformal bay decouples kinetic airframe from AIM-120/AIM-9X munitions."}
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
                {"id": "13", "slug": "13-fury-ghostbat", "name": "Fury CCA", "insight": "Token UAV: AL-TC-DR establishes transonic air superiority and Lattice OS edge mesh."}
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
                {"id": "08", "slug": "08-unex-artillery", "name": "UNEX ABRIS", "insight": "Bekker soil slip traction controller prevents wheel spin-down in clay soils."}
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
    <a href="{rel}cases/index.html" class="{'active' if active_nav=='cases' else ''}">13 Benchmarks</a>
    <a href="{rel}c2/officer.html" class="{'active' if active_nav=='c2' else ''}">C2 Officer Symbiosis</a>
    <a href="{rel}vendors/index.html" class="{'active' if active_nav=='vendors' else ''}">Vendors & OEMs</a>
    <a href="{rel}hal/index.html" class="{'active' if active_nav=='hal' else ''}">HAL Registry</a>
    <a href="https://ua.linkedin.com/in/serhii-khylevych-aa152322" target="_blank" rel="noopener">Author Profile ↗</a>
  </nav>
</header>"""

def render_footer():
    return """<footer class="page-footer">
  <div class="container">
    <p><strong>Unmanned Warfare Engine (UWE)</strong> — Authored by <strong>Serhii Khylevych</strong>, Systems Architect.</p>
    <p style="margin-top:0.5rem; font-size:0.8rem; color:#8b949e;">
      Architecting a software-defined containment line and automated interdiction shield for the Free World.<br>
      Strict adherence to physical laws, hardware abstraction, and cyber-physical matrices. Local Kyiv wartime conditions.
    </p>
  </div>
</footer>"""

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
    <a href="{rel}domains/{case['domain'].lower()}.html" class="badge badge-{case['domain'].lower()}">{case['domain']}</a>
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
  <meta name="description" content="Autonomous warfare doctrine, 6-character cyber-physical matrix, and 13 empirical platform benchmarks replacing legacy STANAG 4670. Authored by Serhii Khylevych.">
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
        <div class="kpi-num">13</div>
        <div class="kpi-label">Empirical Benchmarks</div>
        <div class="kpi-sub">Flight & field tests analyzed</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-num">6</div>
        <div class="kpi-label">Physical Domains</div>
        <div class="kpi-sub">Air, Copter, Ground, Sea, Subsea, Orbit</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-num">12</div>
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
    <div class="spectrum-wrap">
      <div class="spectrum-head">
        <strong style="font-size:0.95rem; color:#fff;">📊 Cross-Domain Operational Spectrum (13 Empirical Benchmarks)</strong>
        <span style="font-size:0.8rem; color:var(--text-muted);">Click bar segment to filter cases</span>
      </div>
      <div class="spectrum-bar">
        <div class="spec-seg" data-domain-filter="UAV" style="width:46.15%; background:#3fb950;" title="UAV Fixed-Wing & Hypersonic: 6 cases (46.2%)"></div>
        <div class="spec-seg" data-domain-filter="UCV" style="width:7.69%; background:#d29922;" title="UCV Copter Combat: 1 case (7.7%)"></div>
        <div class="spec-seg" data-domain-filter="UGV" style="width:15.38%; background:#bc8cff;" title="UGV Ground Robotics: 2 cases (15.4%)"></div>
        <div class="spec-seg" data-domain-filter="UUV" style="width:15.38%; background:#58a6ff;" title="UUV Subsea Robotics: 2 cases (15.4%)"></div>
        <div class="spec-seg" data-domain-filter="USV" style="width:7.69%; background:#38bdf8;" title="USV Surface Vessels: 1 case (7.7%)"></div>
        <div class="spec-seg" data-domain-filter="UOV" style="width:7.69%; background:#ff7b72;" title="UOV Counter-Space: 1 case (7.7%)"></div>
      </div>
      <div class="spectrum-legend">
        <span class="legend-item"><span class="legend-dot" style="background:#3fb950;"></span> UAV Air (46.2%)</span>
        <span class="legend-item"><span class="legend-dot" style="background:#d29922;"></span> UCV Copter (7.7%)</span>
        <span class="legend-item"><span class="legend-dot" style="background:#bc8cff;"></span> UGV Ground (15.4%)</span>
        <span class="legend-item"><span class="legend-dot" style="background:#58a6ff;"></span> UUV Subsea (15.4%)</span>
        <span class="legend-item"><span class="legend-dot" style="background:#38bdf8;"></span> USV Surface (7.7%)</span>
        <span class="legend-item"><span class="legend-dot" style="background:#ff7b72;"></span> UOV Orbital (7.7%)</span>
      </div>
    </div>

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

    <!-- 13 Empirical Case Studies Section -->
    <div style="margin-bottom:2rem;">
      <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--border); padding-bottom:0.5rem; margin-bottom:1rem;">
        <h2 style="font-size:1.4rem; margin:0;">
          🔬 13 Empirical Platform Benchmarks & Architectural Mapping
        </h2>
        <span style="font-size:0.85rem; color:var(--text-muted);">Showing <strong id="visible-count" style="color:#fff;">13</strong> of 13 platforms</span>
      </div>
      <p style="color:var(--text-muted); font-size:0.95rem; margin-bottom:1.25rem;">
        Scientific-practical stress-testing of western OEMs, Ukrainian frontline prototypes, and global aerospace systems against the 4 Invariant Laws of UWE.
      </p>

      <input type="text" id="case-search" class="search-bar" placeholder="Search 13 benchmarks by platform, token, HAL contract, or vendor (e.g., 'Anduril', 'coaxial', 'MQ-25', 'IVtol')...">
      
      <div class="filter-group-label">Filter by Physical Medium Domain:</div>
      <div class="filter-pills">
        <span class="filter-pill domain-pill active" data-domain-filter="ALL">All Domains (13)</span>
        <span class="filter-pill domain-pill" data-domain-filter="UAV">UAV Air (6)</span>
        <span class="filter-pill domain-pill" data-domain-filter="UCV">UCV Copter (1)</span>
        <span class="filter-pill domain-pill" data-domain-filter="UGV">UGV Ground (2)</span>
        <span class="filter-pill domain-pill" data-domain-filter="UUV">UUV Subsea (2)</span>
        <span class="filter-pill domain-pill" data-domain-filter="USV">USV Surface (1)</span>
        <span class="filter-pill domain-pill" data-domain-filter="UOV">UOV Orbital (1)</span>
      </div>

      <div class="filter-group-label">Filter by Defense-Tech OEM / Developer:</div>
      <div class="filter-pills">
        <span class="filter-pill vendor-pill active" data-vendor-filter="ALL">All Vendors (12)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="anduril">Anduril (2)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="boeing">Boeing (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="lockheed-martin">Lockheed Martin (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="exail">Exail (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="bae-falconworks">BAE / Certo (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="unex">UNEX (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="honda">Honda (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="frontline-ua">Frontline UA (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="nextgen-arsenal">NextGen Arsenal (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="darpa">DARPA (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="global-aerospace">Aerospace Res. (1)</span>
        <span class="filter-pill vendor-pill" data-vendor-filter="hypersonic-consortium">Hypersonic (1)</span>
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
  <title>Case #{case['id']}: {case['name']} | UWE Architectural Benchmark</title>
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
      <a href="index.html" style="font-size:0.9rem;">← Back to All 13 Benchmarks</a>
    </div>

    <article class="reddit-card">
      <div class="card-meta">
        <span>Author: <strong>Serhii Khylevych</strong></span>
        <span>•</span>
        <span>Date: {case['date']}</span>
        <span>•</span>
        <a href="../domains/{case['domain'].lower()}.html" class="badge badge-{case['domain'].lower()}">{case['domain']}</a>
        <a href="../vendors/index.html#{case['vendor_slug']}" class="badge badge-vendor">{case['vendor']}</a>
      </div>
      <h1 class="hero-title" style="font-size:1.85rem; margin-bottom:1rem;">
        Case #{case['id']}: {case['name']}
      </h1>

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
    </article>
  </div>
  {render_footer()}
</body>
</html>"""
        write_file(f"cases/{case['slug']}.html", html)

def build_cases_index():
    cases_html = "\n".join(render_case_card(c, depth=1) for c in CASES_DATA)
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Empirical Case Studies Registry (13 Validated Platforms) | UWE</title>
  <meta name="description" content="Cumulative registry of all 13 empirical defense-tech systems analyzed under the Unmanned Warfare Engine (UWE) framework.">
  <link rel="canonical" href="{BASE_URL}/cases/index.html">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
  {render_header("cases", depth=1)}
  <div class="container">
    <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--border); padding-bottom:0.5rem; margin-bottom:1rem;">
      <h1 class="hero-title" style="font-size:1.85rem; margin:0;">Empirical Platform Benchmarks (13 Cases)</h1>
      <span style="font-size:0.85rem; color:var(--text-muted);">Showing <strong id="visible-count" style="color:#fff;">13</strong> of 13 platforms</span>
    </div>
    <p style="color:var(--text-muted); margin-bottom:1.5rem;">
      Cross-referencing western OEMs, frontline Ukrainian prototypes, and aerospace systems against the 4 Invariant Laws of UWE.
    </p>

    <input type="text" id="case-search" class="search-bar" placeholder="Search 13 benchmarks by platform, token, HAL contract, or vendor...">
    
    <div class="filter-group-label">Filter by Physical Medium Domain:</div>
    <div class="filter-pills">
      <span class="filter-pill domain-pill active" data-domain-filter="ALL">All Domains (13)</span>
      <span class="filter-pill domain-pill" data-domain-filter="UAV">UAV Air (6)</span>
      <span class="filter-pill domain-pill" data-domain-filter="UCV">UCV Copter (1)</span>
      <span class="filter-pill domain-pill" data-domain-filter="UGV">UGV Ground (2)</span>
      <span class="filter-pill domain-pill" data-domain-filter="UUV">UUV Subsea (2)</span>
      <span class="filter-pill domain-pill" data-domain-filter="USV">USV Surface (1)</span>
      <span class="filter-pill domain-pill" data-domain-filter="UOV">UOV Orbital (1)</span>
    </div>

    <div class="filter-group-label">Filter by Defense-Tech OEM / Developer:</div>
    <div class="filter-pills">
      <span class="filter-pill vendor-pill active" data-vendor-filter="ALL">All Vendors (12)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="anduril">Anduril (2)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="boeing">Boeing (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="lockheed-martin">Lockheed Martin (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="exail">Exail (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="bae-falconworks">BAE / Certo (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="unex">UNEX (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="honda">Honda (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="frontline-ua">Frontline UA (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="nextgen-arsenal">NextGen Arsenal (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="darpa">DARPA (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="global-aerospace">Aerospace Res. (1)</span>
      <span class="filter-pill vendor-pill" data-vendor-filter="hypersonic-consortium">Hypersonic (1)</span>
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
  <title>UWE Domain Taxonomy & Cyber-Physical Horizons</title>
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
  <title>Vendor & OEM Defense-Tech Mapping | UWE</title>
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
      <h2 style="color:#bc8cff; margin-top:0;">2. The Hal Moore & CSM Basil Plumley Symbiosis (E2E Combat Lifecycle)</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        The primary anxiety of military commanders regarding AI is the <em>"loss of control"</em>—the fear of opaque algorithms usurping command or executing unauthorized escalations.
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
          <strong style="color:#58a6ff;">Phase 1: Planning & Intent vs. Physical Reality:</strong> The Commander dictates operational vectors. UWE calculates the dynamic feasibility index against terramechanics, waves, and jamming. Like Plumley, UWE grumbles in cold numbers: <em>"Sir, your vector is 82% viable; shift deployment to C2 mobile rails for 100%."</em>
        </div>
        <div style="background:#111827; padding:0.85rem 1rem; border-radius:6px; border:1px solid #1f2937;">
          <strong style="color:#58a6ff;">Phase 2: Decentralized Logistics & Sustainment:</strong> The Commander focuses on operational geometry. UWE automatically manages the supply continuum (Law II): monitoring battery SOC, routing <a href="../domains/ugv.html">UGV</a> mobile powerbanks (LLD-2), and pre-positioning munition pods.
        </div>
        <div style="background:#111827; padding:0.85rem 1rem; border-radius:6px; border:1px solid #1f2937;">
          <strong style="color:#58a6ff;">Phase 3: The Kinetic Kill Web (LLD-1):</strong> The Commander tracks operational tempo. UWE binds orbital sensors (<a href="../domains/uov.html">UOV</a>) to tactical multirotors (<a href="../domains/ucv.html">UCV</a>) and surface interceptors (<a href="../domains/usv.html">USV</a>) at machine speed, resolving microsecond target handoffs without human cognitive lag.
        </div>
        <div style="background:#111827; padding:0.85rem 1rem; border-radius:6px; border:1px solid #1f2937;">
          <strong style="color:#f85149;">Phase 4: Critical States & "Broken Arrow" (Law III Decoupled Lethality):</strong> When defense lines are breached, the Commander authorizes the cybernetic equivalent of "Broken Arrow." UWE activates runtime One-Way Mission (OWM / LLD-5) decorators: uncapping thermal limits, commanding 15G defensive turns, and transforming recon platforms into sacrificial kinetic rams to save human lives.
        </div>
        <div style="background:#111827; padding:0.85rem 1rem; border-radius:6px; border:1px solid #1f2937;">
          <strong style="color:#3fb950;">Phase 5: Post-Engagement Recovery & Sleeper Fortresses:</strong> UWE coordinates autonomous CASEVAC, schedules 15-minute fast charging, and settles subsea nodes back into the seabed in low-power "Zhdun" sleeper mode (LLD-3). Master Sergeant UWE reports: <em>"Fleet re-armed, defensive pickets silent, awaiting orders, Sir."</em>
        </div>
      </div>
    </section>

    <!-- Section 3: APM vs CPM -->
    <section class="reddit-card" style="border-left:4px solid var(--green);">
      <h2 style="color:#3fb950; margin-top:0;">3. Cognitive Discrimination: APM vs. CPM</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        Military leaders rightly fear the <em>"twitch-panic"</em> scenario—the fear that an overstimulated operator will panic-click and trigger an unintended kinetic escalation. UWE neutralizes this through a strict architectural separation:
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
        <h4 style="color:#fff; margin:0 0 0.5rem 0;">✈️ The "Nuclear Pilot" Standard & Why Pure Gamers Fail</h4>
        <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin:0;">
          This standard mirrors a <strong>fighter pilot carrying tactical nuclear munitions</strong>: possessing superhuman subconscious motor control at 9G, paired with icy moral clarity regarding the weapon release switch. Pure esports gamers fail as combat commanders because tournaments occur in risk-free environments where defeat is merely a lost match; under kinetic artillery fire, unconditioned psychology fractures. In UWE doctrine, gamers serve strictly as <strong>Technical Instructors for ARM-SRM Simulators</strong> to drill muscle memory, while the combat seat is held exclusively by a commissioned officer bound by military oath.
        </p>
      </div>
    </section>

    <!-- Section 4: Reflex Loop & Shoot As Think -->
    <section class="reddit-card" style="border-left:4px solid var(--cyan);">
      <h2 style="color:#38bdf8; margin-top:0;">4. The Cyber-Physical Reflex Loop & "I Shoot As I Think"</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        The transition from command intent to kinetic execution requires an indivisible three-stage <strong>Cyber-Physical Reflex Loop</strong>:
      </p>

      <div style="display:flex; flex-direction:column; gap:1rem; margin:1.25rem 0;">
        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1rem;">
          <h4 style="color:#38bdf8; margin:0 0 0.35rem 0;">🔹 Stage I: Ergonomics of Intent — Why the Mechanical Manipulator Wins</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Futuristic concepts often push gesture control or eye-tracking. In high-intensity combat, UWE rejects these gimmicks in favor of precision mechanical manipulators (mouse or trackball). Eye-tracking suffers from involuntary saccadic micro-glances (10–30 ms), while touchscreens block visual telemetry and lack tactile feedback under mechanical vibration. A physical cursor trajectory plus an intentional tactile click with resistance requires coordinated motor-cortex activation — the ultimate biological indicator of conscious intent.
          </p>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1rem;">
          <h4 style="color:#d2a8ff; margin:0 0 0.35rem 0;">🔹 Stage II: The Biometric Sentinel — Fallout 4-STDFUA Protocol</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Drawing on the real-time feedback loops proven in the author's technical project <strong>Fallout 4-STDFUA</strong>, UWE implements an automated multimodal biometric fail-safe monitoring Blood Glucose, Heart Rate Variability (HRV), vocal micro-tremors, and FACS facial action coding. If shrapnel impact, acute concussion, or panic is detected, erratic mouse movement is identified as an involuntary muscle spasm: <strong>the system immediately locks the lethal command line (CPM)</strong>, preventing accidental detonation, and Master Sergeant UWE transfers command up-chain while taking the fleet into defensive station-keeping.
          </p>
        </div>

        <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1rem;">
          <h4 style="color:#7ee787; margin:0 0 0.35rem 0;">🔹 Stage III: The Operational Creed — "I Shoot As I Think" (Zero Translation Latency)</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.5; margin:0 0 1rem 0;">
            In the microsecond domain of Dagger Dogfights where closing speeds reach km/s and EW pulses blind standard radios, linear decision cycles are fatal: <em>"Shoot, then think"</em> leads to fratricide; <em>"Think, then shoot"</em> leads to destruction via adversary Edge-AI translation latency.
          </p>
          
          <div style="text-align:center;">
            <img src="../assets/img/hal_moore_shoot_as_think.png" alt="Lt. Col. Hal Moore executing command and kinetic fire simultaneously" style="width:100%; max-width:850px; height:auto; border-radius:6px; border:1px solid var(--border);">
            <p style="font-size:0.83rem; color:var(--text-muted); margin-top:0.5rem;">
              <em>Figure 2: The Physical Embodiment of "I Shoot As I Think" — Lt. Col. Hal Moore in the Ia Drang firefight. Handset to ear coordinating sovereign multi-domain fires (CPM), while his rifle simultaneously engages charging assault waves (APM). Zero translation latency between thought, command, and kinetic delivery.</em>
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Coastal Extraction & System Rescue -->
    <section class="reddit-card" style="border-left:4px solid var(--amber);">
      <h2 style="color:#d29922; margin-top:0;">5. The Coastal Extraction: Jane's Cold-State Topology & System Rescue</h2>
      <p style="color:e6edf3; font-size:0.95rem; line-height:1.6;">
        The climax on the hostile coast in <em>G.I. Jane</em> anchors <strong>Lt. Jordan O'Neil</strong> in our human triad orbiting the <strong>Plumley Anchor (UWE Engine)</strong>:
      </p>

      <div style="text-align:center; margin:1rem 0;">
        <img src="../assets/img/jordan_oneil_coastal_rescue.jpg" alt="Lt. Jordan O'Neil on the Hostile Coast" style="width:100%; max-width:850px; height:auto; border-radius:6px; border:1px solid var(--border);">
        <p style="font-size:0.83rem; color:var(--text-muted); margin-top:0.5rem;">
          <em>Figure 3: Lt. Jordan O'Neil on the Coastline — Cold calculation under mortal stress: emotional noise severed, functioning as a pure tactical processor rescuing the system when automation fractures.</em>
        </p>
      </div>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1rem; margin-top:1rem;">
        <div style="background:#111827; padding:1rem; border-radius:6px; border:1px solid #1f2937;">
          <h4 style="color:#fff; margin:0 0 0.35rem 0;">Cold-State Calculation Under Pressure</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Emotional noise is severed: her mind operates as a pure tactical processor, evaluating terrain contours and vectors with algorithmic detachment, perfectly synchronized with Master Sergeant UWE.
          </p>
        </div>
        <div style="background:#111827; padding:1rem; border-radius:6px; border:1px solid #1f2937;">
          <h4 style="color:#e3b341; margin:0 0 0.35rem 0;">System Rescue (Overriding Damaged Automation)</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Her mission on that coast is the rescue of Master Chief. In UWE doctrine, this carries vital architectural meaning: a human with this mindset <strong>saves the cyber-physical system itself</strong> when automation is damaged, blinded by EW strikes, or trapped in an algorithmic deadlock.
          </p>
        </div>
      </div>
    </section>

    <!-- Section 6: Character Synthesis Summary -->
    <section class="reddit-card" style="border-left:4px solid var(--green);">
      <h2 style="color:#7ee787; margin-top:0;">6. The Trinity of Command: Character Synthesis Summary</h2>
      <p style="color:#e6edf3; font-size:0.95rem; line-height:1.6;">
        Neither Maverick, Moore, nor O'Neil is a ready-made UWE Officer. What unites them is <strong>acceptance of the physical reality of combat (Law I)</strong> and non-linear decision-making. The UWE Officer is an engineered psychological alloy:
      </p>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:1rem; margin:1.25rem 0;">
        <div style="background:#161b22; border:1px solid var(--border); border-radius:6px; padding:1rem;">
          <h4 style="color:#58a6ff; margin:0 0 0.5rem 0;">🎖️ The Hal Moore Component</h4>
          <div style="font-size:0.82rem; color:#3fb950; font-weight:700; margin-bottom:0.4rem;">MORAL SOVEREIGNTY & CPM ANCHOR</div>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Absolute fidelity to the military oath, ethical command, and human stewardship. The officer never views robotic fleets as a video game; they carry sovereign accountability under the Law of Armed Conflict.
          </p>
        </div>

        <div style="background:#161b22; border:1px solid var(--border); border-radius:6px; padding:1rem;">
          <h4 style="color:#38bdf8; margin:0 0 0.5rem 0;">🌊 The Jordan O'Neil Component</h4>
          <div style="font-size:0.82rem; color:#38bdf8; font-weight:700; margin-bottom:0.4rem;">SPATIAL TELEMETRY & PREDICTIVE OODA</div>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Compressed situational awareness and total elimination of panic. Reads compressed 6-character tokens across 6 operating domains simultaneously, anticipating edge-AI maneuvers before network bottlenecks register.
          </p>
        </div>

        <div style="background:#161b22; border:1px solid var(--border); border-radius:6px; padding:1rem;">
          <h4 style="color:#ff7b72; margin:0 0 0.5rem 0;">⚡ The Pete Maverick Component</h4>
          <div style="font-size:0.82rem; color:#ff7b72; font-weight:700; margin-bottom:0.4rem;">KINEMATIC PRIMACY & 9G ADAPTATION</div>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin:0;">
            Rejection of administrative dogma in favor of immutable physical laws. In high-G crises (Dagger Dogfights), pushes platforms to structural limits, overriding peacetime limiters because they know the metal will hold.
          </p>
        </div>
      </div>

      <div style="background:#111827; border:1px solid #1f2937; border-radius:6px; padding:1rem; margin-top:0.75rem;">
        <strong style="color:#bc8cff;">⚙️ The Basil Plumley Anchor (The Cyber-Physical Engine):</strong>
        <p style="font-size:0.88rem; color:var(--text-muted); margin:0.35rem 0 0 0; line-height:1.5;">
          These three human dimensions converge around the Plumley Anchor (UWE Engine): a tireless, objective master sergeant executing kinematics, containerization, and fail-safe supervision. The machine protects the human from physiological errors; the human infuses the machine with sovereign moral intent.
        </p>
      </div>
    </section>

    <!-- Section 7: Lexicon Mapping -->
    <section class="reddit-card" style="border-left:4px solid var(--purple);">
      <h2 style="color:#d2a8ff; margin-top:0;">7. Lexicon & Architectural Mapping of the UWE Master Infographic</h2>
      <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6;">
        To ensure total doctrinal fidelity, every visual badge, vector, and arc on the master infographic corresponds to an exact cyber-physical subsystem:
      </p>

      <div style="display:flex; flex-direction:column; gap:0.75rem; font-size:0.88rem; margin-top:1rem;">
        <div style="background:#161b22; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
          <strong style="color:#fff;">1. Central Anchor (Sam Elliott / Plumley):</strong> 
          <code style="color:#58a6ff;">[INVARIANT HAL ANCHOR | FALLOUT 4-STDFUA MULTIMODAL SUITE]</code> — The machine executor managing the pressure gauge dial across 6 saturated domains (<code>UOV</code>, <code>UAV</code>, <code>UCV</code>, <code>UGV</code>, <code>USV</code>, <code>UUV</code>).
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
    </section>

    <!-- Section 8: Deep Crosslink Matrix -->
    <section class="reddit-card" style="border-left:4px solid var(--accent); background:rgba(31, 111, 235, 0.04);">
      <h2 style="color:#58a6ff; margin-top:0;">8. Deep Cross-Domain & Empirical Benchmark Topology</h2>
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

def build_seo_assets():
    # 1. Sitemap.xml
    urls = [
        f"{BASE_URL}/index.html",
        f"{BASE_URL}/domains/index.html",
        f"{BASE_URL}/cases/index.html",
        f"{BASE_URL}/c2/officer.html",
        f"{BASE_URL}/vendors/index.html",
        f"{BASE_URL}/hal/index.html",
    ]
    for d in DOMAINS_DATA:
        urls.append(f"{BASE_URL}/domains/{d['code'].lower()}.html")
    for c in CASES_DATA:
        urls.append(f"{BASE_URL}/cases/{c['slug']}.html")

    sitemap_entries = "\n".join(f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-10-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{'1.0' if u.endswith('index.html') and 'cases/' not in u and 'domains/' not in u else ('0.9' if 'c2/' in u else '0.8')}</priority>
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

def main():
    print("=" * 65)
    print("🚀 Building Unmanned Warfare Engine (UWE) Documentation Portal")
    print(f"📁 Target Output: {DOCS}")
    print("=" * 65)
    
    generate_css()
    generate_js()
    build_index()
    build_cases_index()
    build_case_pages()
    build_domains()
    build_c2_officer()
    build_vendors()
    build_hal()
    build_seo_assets()
    
    print("\n✅ Build Complete! 13 Cases, 6 Domains, C2 Officer Symbiosis, Vendors & HAL Registry Generated.")
    print("📊 All pages include Schema.org JSON-LD and pre-rendered static HTML.")

if __name__ == "__main__":
    main()


