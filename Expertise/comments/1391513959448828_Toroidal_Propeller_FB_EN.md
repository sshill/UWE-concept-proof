UWE CLASSIFICATION: UCV: MQ-EE-AR
(Medium Quadcopter • Electric Battery • Acoustic-Stealth • Assault/Recon • RF-Mesh)

AERODYNAMIC AUDIT: TOROIDAL ROTORS & 15% EFFICIENCY RECOVERY
(Neuronautics Experiment / Aeroacoustic Benchmark)

Why do open blades yield ~75% efficiency while toroidal props drop to ~65%?
1. Viscous Skin Friction: A closed loop doubles wetted area (Swet x2). At Re ≈ 10^5, viscous drag doubles profile power (P0).
2. Cascade Wake Interference: The trailing branch operates in downwash, degrading effective angle of attack.
3. Rotational Inertia (Izz x3): Peripheral mass slows PID response.

Why is it significantly quieter?
Eliminating blade tips diffuses tip vortices into a broad sheet. BPF peaks (200-800 Hz) disappear; noise drops 4-6 dBA and shifts into white spectrum (>2 kHz) that attenuates within 40m.

NEUTRALIZING THE 15% DRAG PENALTY
Cantilever open blades require 10-12% thickness (t/c) against root bending. But a closed loop is an ARCH (Euler's elastica)!
Bending load is shared across branches, cutting moment 3-4x. This enables an ultrathin profile (t/c = 4-5% in CFRP), halving drag (Cd0 from 0.030 to 0.015).
Math: Area doubles (x2), thin-foil drag halves (x0.5): 2 x 0.5 = 1.0! Friction penalty is neutralized; acoustic stealth is preserved.

In VTOL, high arch stiffness resists gyroscopic precession, pushing Mcrit > 0.82 for quiet 250+ km/h cruise.
