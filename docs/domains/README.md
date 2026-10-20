# 🌐 Physical Medium Domains

Live portal: **[https://sshill.github.io/UWE-concept-proof/domains/](https://sshill.github.io/UWE-concept-proof/domains/)**

The UWE standard classifies military autonomous systems across 6 physical domains:

| Domain | Namespace | Physical Interface & Kinematics | HAL Interface |
|---|---|---|---|
| **[UAV](uav.html)** | Air (Fixed-Wing / Transonic) | Aerodynamic Lift, Crossfade Transitions | `IVtolTransitionDrive` |
| **[UCV](ucv.html)** | Copter Combat | Microsecond Vectoring, Fast Interdiction | `IFastInterdictor` |
| **[UGV](ugv.html)** | Ground Robotics | Ground Pressure, Articulation, Skid-Steer | `IArticulatedChassis` |
| **[USV](usv.html)** | Surface Vessels | Sea State Hydrodynamics, Wave Slamming | `ISurfacePlanner` |
| **[UUV](uuv.html)** | Subsea Robotics | Hydrostatic Pressure Horizons, Acoustics | `ISubseaAcoustic` |
| **[UOV](uov.html)** | Orbital Space | Orbital Mechanics, Delta-V, Proximity | `IOrbitalInterceptor` |
