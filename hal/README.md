# ⚡ Hardware Abstraction Layer (HAL) Interfaces

Live portal: **[https://sshill.github.io/UWE-concept-proof/hal/](https://sshill.github.io/UWE-concept-proof/hal/)**

Hardware Abstraction Layer (HAL) contracts decoupling operational software from chassis mechanics:

| Contract | Domain | Control Law / Physical Behavior |
|---|---|---|
| `IVtolTransitionDrive` | UAV | Dynamic rotor-to-wing lift crossfade ratio $\alpha \in [0, 1]$ without tiltrotor pitch instability. |
| `IFastInterdictor` | UCV | Microsecond motor torque control and terminal homing vectoring. |
| `IArticulatedChassis` | UGV | Yaw angle articulation steering $\gamma$ and differential torque allocation. |
| `ISkidSteerGround` | UGV | Skid-steering kinematic model bounded by Bekker soil mechanics. |
| `ISurfacePlanner` | USV | Sea state dynamic replanning and $G_z$ wave-impact limiting. |
| `ISubseaAcoustic` | UUV | Acoustic modem packet orchestration and depth horizon pressure hull safety. |
| `IOrbitalInterceptor` | UOV | Orbital rendezvous burns, Delta-V rationing, and reaction wheel desaturation. |
