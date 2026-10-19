Tim De Zitter's note on Ukraine's UNEX UGV towing a 3.2t D-30 howitzer highlights an important robotic prime mover milestone.

Moving a 4.4t train (gun + ammo) via electric UGV is impressive, but physics reveals the operational constraints.

🏷️ UWE CLASSIFICATION:

UNEX Amphibious Prime Mover:
UGV: GH-ET-DL
(Ground Amphibious | C3 Flatbed | Electric | Heavy Towing | Logistics Replenishment | Starlink/RF)

🟢 THE ELECTRIC ADVANTAGE:
Electric motors deliver peak torque at 0 RPM without stalling clutches, easily breaking static friction on a 3.2t gun. Carrying 1.2t ammo onboard adds crucial ballast for tire adhesion.

🔴 THE DRAWBAR & BRAKING TRAP:

🔹 Unbraked Deceleration:
The D-30 lacks synchronized brakes. Downhill on mud, 3.2t of trailing momentum pushes the lighter tractor, risking violent jackknifing.

🔹 Soil Adhesion Limits:
A 10t tow claim works on asphalt, but off-road drawbar pull is bounded by tire-soil friction (F = μ · m_ugv · g). Wheels spin out in mud regardless of motor kW.

⚡ HAL CONTRACT:
"Robotic prime movers require the IDrawbarTractionController HAL contract to limit torque to soil slip ratios (s < 0.2) and manage deceleration against hitch angles to stop unbraked howitzers from jackknifing the tractor."
