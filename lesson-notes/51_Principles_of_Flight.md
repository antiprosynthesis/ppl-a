# Principles of Flight (Aeroplane) — Detailed Lesson Notes

These notes follow the Belgian flight-school sequence (lessons 8–12), in English, with Dutch terms where useful. They connect the concepts to the Principles of Flight question bank and include supplementary material from the supplied lesson extras. Aircraft-specific procedures always defer to the POH/AFM and instructor.

## Learning route

1. **Lesson 8:** understand airflow, pressure and what the aerofoil terms mean.
2. **Lesson 9:** calculate lift/drag; interpret the lift/drag polar; understand high-lift devices, drag and the propeller as a rotating wing.
3. **Lesson 10:** relate the controls to axes, trim and stability; resolve forces in steady flight, climb and descent.
4. **Lessons 11–12:** coordinate turns, understand load factor and accelerated stall, prevent spins, then connect stability and propeller effects.

## Lesson 8 — Why a wing produces lift

### Four forces and pressure

The aircraft moves through air under four principal forces: weight (`G`), lift (`L`), thrust (`T`) and drag (`D`). In straight, level, constant-speed flight, lift balances weight and thrust balances drag. Increasing power initially accelerates the aircraft; increasing speed also raises drag, until a new equilibrium is reached.

The lesson uses a constricted tube / Venturi demonstration to introduce Bernoulli: where a fluid speeds up, static pressure falls. A wing is not literally a half-Venturi tube, and the equal-transit-time explanation is not needed. Real wing lift results from a pressure distribution and momentum change in the airflow. The upper-surface pressure is lower and the lower-surface pressure higher for a conventional positive-lift condition. The instructor's approximate 70% upper-surface suction / 30% lower-surface pressure split is useful as a classroom picture, but is not a fixed physical ratio for all wings/conditions.

Static pressure acts in every direction. Total pressure is the sum of static and dynamic pressure (`q=½ρV²`). Lift is the aerodynamic resultant component perpendicular to relative airflow; drag is parallel to it and opposite flight direction.

### Aerofoil geometry and angles

- Chord (*koorde*) joins the leading edge (*aanvalsboord*) and trailing edge (*afvloeiboord*).
- The mean camber line (*skeletlijn*) sits midway between the profile surfaces. A symmetric profile has coincident chord and mean camber line; a cambered profile does not.
- Extrados = upper side; intrados = lower side. Thickness is measured perpendicular to chord.
- Angle of attack / angle of incidence in some ECQB translations (*aanvalshoek/invalshoek*) is chord-to-relative-airflow. The school material stresses “angle of attack” to avoid confusion with **angle of incidence**, the installed angle between wing chord and aircraft longitudinal axis.
- Relative airflow is opposite the flight path. A given aircraft pitch attitude can have different AoA in climb, level flight and descent. AoA is not the angle between the wing and horizon.
- Wing area is approximately span × mean chord; aspect ratio is span / mean chord (also `b²/S`). Wing loading is aircraft weight / wing area.

**Figure reading:** PFA-003 marks angle of attack between chord and airflow. PFA-010 identifies chord (label 2), mean camber (3) and maximum thickness (4). The stagnation point is near the leading edge: local flow speed is zero there and streamlines split over and under the profile.

### Airflow over the profile

The stagnation point moves down the leading edge as AoA increases. Along the upper surface, a laminar boundary layer starts near the front, transitions to turbulent, and may separate farther aft. Turbulent flow has more skin-friction drag but can remain attached at higher AoA; separation is the key event as stall develops. The lesson describes separation in two stages: transition, then separation. The question bank asks the laminar region's location (stagnation point to transition point) and which point divides the upper/lower flow (stagnation point).

Aerofoil contamination is dangerous because ice/frost changes the designed profile, increases drag and can make separation occur earlier. Do not interpret icing as merely extra mass.

### Lesson 8 exam concepts

These are directly tested in bank questions 1–10 and 53–61: pressure in all directions; Bernoulli pressure/speed relationship; drag on an object in airflow; chord and AoA diagrams; aspect ratio; stagnation point; upper/lower pressure pattern; CP; CP movement; and stall-related lift loss.

## Lesson 9 — Lift, drag, polars, high-lift devices and propeller introduction

### Lift and drag equations

The lesson builds from the lift equation:

`L = ½ρV² S CL` and `D = ½ρV² S CD`.

Density (`ρ`), speed (`V`), wing area (`S`) and coefficient (`CL`/`CD`) determine the result. Speed is squared: double speed gives four times the force if the remaining values are held constant; triple speed gives nine times. In level flight, though, the pilot adjusts AoA/CL so lift matches weight. The pilot primarily controls lift by changing speed and AoA; configuration changes coefficients and usable AoA.

Higher altitude, warmer air and humidity generally reduce density. At the same true speed, lower density means less dynamic pressure/lift. The instrument speed and true speed should not be confused: IAS approximates dynamic-pressure effects, while true speed needed for a given lift rises as density falls.

### Lift curve, drag curve and stall

`CL` depends on aerofoil shape and AoA. Initially, increasing AoA increases lift coefficient; at the critical AoA, flow separates and `CL` falls abruptly. The lesson flags a common wording trap: “falls” can be true but the most precise curve description is a **sudden/abrupt fall** beyond critical AoA, not a progressive continuation of the pre-stall slope.

The drag coefficient generally increases with AoA and rises markedly after stall. At a small negative AoA it can be near its minimum for a cambered section. Lift falls and drag increases at/after stall.

Critical AoA is a property of the aerofoil/configuration and is not changed simply by aircraft weight. Weight instead changes the speed needed to generate the required lift. For a fixed configuration, stall speed follows `Vs ∝ √W`.

### Centre of pressure

CP is the point along the chord where the resultant aerodynamic force can be considered to act. On the positively cambered wing discussed in lessons, CP moves forward as AoA increases until critical AoA; if AoA decreases, CP moves aft. Around/after stall the pressure pattern changes and CP may move abruptly aft, pitching the nose down. Avoid the over-general claim that CP always moves forward with AoA, even after the critical angle.

### Finesse and reading polars

Finesse is `L/D = CL/CD`; it is the ratio of horizontal glide distance to height loss in still air. If finesse is 12, 1 km height above the landing point gives approximately 12 km distance, ignoring wind/turns/reserves. Manufacturer glide/range charts apply at the specified speed and conditions.

- In the bank's PFA-008 polar, horizontal axis is drag coefficient, vertical axis lift coefficient.
- The tangent from the origin to the polar gives maximum `CL/CD` (best glide angle). Point 4 is max finesse; point 5 is slow flight/high AoA; point 6 represents the post-stall part of the curve; point 1 inverted flight; point 3 fast flight.
- The drag-speed figure PFA-011 has decreasing induced drag, increasing parasite drag, and a U-shaped total. Their equality corresponds to minimum total drag in the exam model.

### Induced and parasite drag

Induced drag exists because a lifting wing turns airflow and generates tip vortices/downwash. It rises with lift demand and falls with speed and increasing aspect ratio. A low-AR wing generates more induced drag than a high-AR wing; an elliptical lift distribution has the least induced drag of the bank's listed planforms. Wingtip pressure equalisation creates vortices; winglets reduce their effect.

Parasite drag comprises form/pressure, skin-friction and interference drag. It rises approximately as speed squared. Interference occurs where flows from components meet, particularly wing/fuselage junctions. Total drag is induced + parasite; do not add interference a second time after parasite. As speed rises in level cruise, parasite drag rises and induced drag falls. Ground effect reduces induced drag and increases effective lift near the ground.

### Flaps, slots and slats

A flap deflects the trailing edge, increasing camber (Fowler flaps also extend aft, increasing area). At the same AoA, flap deployment raises `CL` and drag, generally lowers stall/approach speed, reduces finesse and changes trim. Initial flap increments commonly provide a large lift gain; with further extension drag increases substantially. Take-off flap can shorten ground roll, but extra drag can reduce climb performance. Follow aircraft performance tables.

Leading-edge slots/slats re-energise upper-surface flow, delay separation and enable a higher usable AoA. In the course/bank comparison, slots generate less drag than trailing-edge flaps for the high-lift effect; flaps increase `CL` at all AoA while slats chiefly extend the critical-AoA range. Keep the distinction exact: flap = camber/lift/drag; slat/slot = separation delay/higher AoA.

### Propeller: rotating aerofoil

A propeller blade has aerofoil surfaces and creates thrust by lift. The blade tip's rotational speed is greater than the root's; a twist in blade pitch/angle accommodates this and gives nearly constant effective AoA/loading across the span. A fine-pitch prop suits low-speed take-off; coarse pitch suits high-speed cruise. Fixed-pitch propellers are designed for one operating range; variable/constant-speed systems adapt blade angle.

Lesson 9 introduces propeller icing, blade twist and pitch. Ice reduces aerofoil performance, so power and RPM tend to fall. The question bank asks these results, plus the purpose of blade twist.

## Lesson 10 — Controls, stability, straight flight, climb and descent

### Axes and primary controls

The CG is the reference pivot for aircraft rotation.

| Control | Primary motion | Axis | Structural contribution to stability |
|---|---|---|---|
| Elevator (*hoogteroer*) | Pitch | Lateral / transverse axis | Horizontal stabiliser contributes longitudinal stability |
| Ailerons (*rolroeren*) | Roll | Longitudinal axis | Dihedral and design contribute lateral stability |
| Rudder (*richtingsroer*) | Yaw | Vertical axis | Vertical fin contributes directional stability |

The axes are named by the aircraft body line they follow, but the motion is around that axis. Thus longitudinal stability is pitch stability around the lateral axis—a frequent exam distractor.

Elevator changes tail force and pitches the aircraft about its CG. Pulling back normally raises the nose; pushing forward lowers it. The exact force depends on surface area/deflection and dynamic pressure. The result changes speed/AoA as well as attitude. A stabilator (all-moving tail) can combine stabiliser/elevator functions.

Ailerons change lift on opposite wings and roll the aircraft. Differential ailerons and Frise geometry reduce adverse yaw. Aileron trim can correct small persistent rolling force but does not replace coordinated rudder.

Rudder deflection yaws the aircraft. A coordinated turn uses both roll and rudder; rudder alone is not the correct way to bank. Rudder can also induce roll (secondary effect). The ball indicates slip/skid; step on the ball to correct.

### Trim and balances

Trim tabs relieve steady control force. A tab is a small control surface with a long lever arm; its force balances the pilot's force on a short arm. The tab acts opposite the desired elevator force. If the nose tends to pitch up and the pilot must push forward, elevator goes down and tab is set up to relieve the force; the exam bank likewise keys tab up to eliminate a nose-raising tendency and calls the indication nose-down.

Aerodynamic balance reduces the force needed to move a control surface. Mass/static balance adds counterweight about the hinge to prevent flutter. Flutter is destructive vibration that can damage the wing/control system; the bank connects exceeding VNE with flutter and mechanical damage.

### Static stability and CG

Positive static stability means an aircraft initially tends back toward its original condition after a disturbance; neutral means it remains displaced; negative means it continues away. This definition concerns initial tendency. Dynamic stability concerns the subsequent oscillation and damping.

The horizontal tail restores pitch/longitudinal stability; the vertical tail restores yaw/directional stability; dihedral creates a restoring roll tendency in sideslip. Forward CG generally increases pitch stability but requires greater elevator force; aft CG reduces stability and can make recovery difficult. Loading controls CG; trim does not move it. Maintain POH limits.

### Straight-and-level flight

In ERHV, force magnitudes balance, but their points of application/moments may differ. Lift may act aft of CG; thrust/drag lines and downwash on the horizontal tail create moments that the tail/control system balances. Trim reduces required sustained pilot force.

Increasing power tends to accelerate and may create a climb tendency depending on thrust line/trim; if a level path is required, use pitch/control input as appropriate. As speed rises drag also rises until a new steady state. The level-flight power curve explains why very slow flight on the “back side” of the power curve may require more power to sustain speed/lift.

### Climb and descent

A climb's flight path is inclined. The weight component along the flight path acts rearward with drag, so more thrust/power is needed. Lift remains perpendicular to relative airflow; in the simplified steady climb resolution its vertical component supports the vertical component of weight. Do not infer that lift must be greater than total weight simply because the aircraft climbs.

- `Vx` gives best angle of climb: greatest height per horizontal distance, useful for obstacle clearance.
- `Vy` gives best rate of climb: greatest height per time.
- Rate of climb is ft/min or m/s; gradient is height/horizontal distance; angle is an angle.
- Gradient example: `600 ft/min` at `120 kt` ground speed gives about `5%`. For small angles, angle in degrees ≈ gradient (%) × 0.57.
- Take-off distance includes ground roll plus distance to clear the standard 50 ft / 15 m obstacle in the lesson. Density, temperature, weight, wind, runway surface/slope, flap and power matter.
- Meteorological ceiling is the lowest broken/overcast cloud layer. Service ceiling is a performance definition; this course uses 100 ft/min as the limiting climb rate under standard conditions.

In descent, a component of weight helps move the aircraft along the flight path; power controls the path/rate and pitch controls speed in the school's simplified teaching model. Use aircraft-specific technique. VASI/PAPI indicates visual path relative to the approach slope.

## Lessons 11–12 — Turns, stall/spin, stability and propeller effects

### Coordinated turns and load factor

Bank tilts the lift vector. Its horizontal component provides centripetal force; its vertical component is less than total lift. To maintain level flight, raise total lift so the vertical component still balances weight. In a coordinated level turn, centrifugal/centripetal language describes the frame of reference; the exam's useful equation is `n=1/cosφ`.

At 30° bank `n≈1.15`; at 60° bank `n=2`. A typical person's tolerance and aircraft structural limits are separate issues; the POH limits control. Higher load factor raises stall speed: `Vs_turn=Vs_level√n`. A sudden upward gust can increase load factor and AoA even without a commanded turn.

The ball follows apparent gravity/resultant force. Centred ball = coordinated turn; displaced ball = slip/skid. “Step on the ball” is the correction mnemonic. Ball quality is not bank angle; turn coordinator/attitude indicator provide other information.

Rate-one turn is 360° in two minutes = 3°/s; rate half is 360° in four minutes; rate two is 360° in one minute. Bank required for a given turn rate depends on TAS (a faster aircraft needs greater bank). At the same bank, load factor does not depend on weight. The lesson question set explicitly revisits rate/ball interpretation.

### Stall recognition and factors

Stall occurs beyond critical AoA, not at a fixed attitude. Warning may be a horn/light/vane response and should activate before the stall. Buffet, sluggish controls, low IAS and wing drop are warning signs. Lower AoA restores attached flow; increasing power helps regain speed/energy but does not replace unloading.

Stall speed increases with weight and load factor; flaps lower it by increasing maximum lift coefficient. Density affects TAS at stall more than IAS. Other risks include icing, turbulence, manoeuvre, power/configuration and CG effects on controllability. A table must be read with its units/configuration: the instructor highlights a Cessna table in mph, so a value in knots cannot be compared directly without conversion.

On landing approach, do not casually retract flaps because lift can fall sharply. The lesson cites `VAT = 1.3 × VSO` as the approach-speed rule for its syllabus; aircraft/operator procedures and published speeds take precedence. The bank's go-around answer (absent another procedure) is intermediate flap, not immediate full retraction. The oral Q&A gives one school's gradual 30°→20°→10°→0° sequence; this is a training/type example, not universal.

### Spin versus spiral dive and recovery

A spin is a stalled, autorotative descent: one wing has greater separation/lower lift, the aircraft rolls and yaws, and the nose pitches down. A wing drop can increase AoA on the dropping wing and reduce it on the rising wing, reinforcing autorotation. The IAS is usually low, near stall, and height loss is substantial. The lesson's C152 illustration is about 400 ft per turn in ideal conditions; this is an example, not a guaranteed value.

A spiral dive is not stalled: both wings remain unstalled and the aircraft describes a steep descending turn with rapidly increasing speed/load. Distinguish it by speed and stall state, not just by seeing rotation.

Prevention: maintain adequate speed, coordinated flight and situational awareness; avoid uncoordinated stall entry. Stall prevention is spin prevention. In a stall/wing drop, do not use aileron to force wings level if it worsens the stall. For training, use neutral ailerons and appropriate rudder toward the high wing to oppose yaw/autorotation while reducing AoA.

The spin lesson's general developed-spin teaching sequence is: power idle, ailerons neutral, opposite rudder to stop rotation, elevator forward to unstall, then neutral controls when rotation ceases and recover from the dive without exceeding limits. **Always use the aircraft POH/AFM—spin procedures differ by type, and many aircraft are not approved for intentional spins.** Never practise without an instructor, approved aircraft, height and briefing. The teacher notes HASELL for aerobatic training checks (Height, Airframe, Safety, Engine, Location, Lookout), with the required height set by the approved exercise/aircraft.

Spin extras discuss incipient versus developed spin, slipstream/power and flap effects, aft CG making a flatter spin more difficult to recover, and operational scenarios (base-to-final, stretched glide, steep climb, distraction). These are beyond the bank but reinforce prevention. C152 training numbers and recovery steps are not general operational guidance.

### Stability and CG recap

A stable aircraft tends toward its original condition after disturbance; an unstable one tends farther away. The design trades stability for manoeuvrability. Dihedral, high wing/low CG, sweep and high tail can contribute to lateral stability in different ways; vertical tail gives directional stability. CG forward increases pitch stability and control force; aft CG reduces stability and can compromise recovery. “More manoeuvrable” does not always mean “easier to control.”

### Propeller: pitch, constant speed, icing, secondary effects

A propeller is a rotating wing. Rotational speed is greater at the tip; blade twist compensates for that. Geometric pitch is blade angle/ideal advance per revolution; effective pitch is less because air slips. Fixed pitch gives best efficiency near one design point: fine pitch for low-speed/take-off, coarse for cruise.

A constant-speed unit (CSU) holds selected RPM by varying blade pitch; it does not hold aircraft speed constant. Throttle/manifold pressure controls engine power; propeller control selects RPM. In the bank's engine-idle descent setup, moving the propeller lever aft increases pitch and decreases sink rate. After engine failure, an unfeathered windmilling propeller creates drag; prop ice lowers power/RPM.

Beyond bank, lessons discuss right-turning propeller slipstream striking the tail, torque, gyroscopic precession and asymmetric blade thrust/P-factor at high AoA. These can yaw the aircraft on take-off/climb and require coordinated rudder. Magnitude/direction depend on engine/propeller rotation and aircraft attitude; use the aircraft's procedures.

## Supplementary material and instructor emphasis

### Flight Control Systems extra (beyond question bank)

The systems handout classifies elevator, rudder and ailerons as primary controls; flaps/slats, spoilers/airbrakes and trim as secondary devices. Control transmission can be mechanical, hydraulic, electrical or electronic. It distinguishes reversible manual controls, powered/irreversible controls and power-assisted controls. Inspection topics include cable tension, locking, travel range/correct deflection, friction, freedom of movement and backlash. Gust locks must be removed before flight. Large-aircraft take-off configuration warnings may check trim, flap/slat position, speed brakes, doors and control locks; system architecture is type-specific and beyond the PPL question bank.

### Besturing / Tobago extra decks (beyond question bank)

The supplied aircraft-control and Tobago PDFs are principally image/diagram slides with little selectable text. Their relevant course concepts are captured in lessons 10–12 and the question-bank illustrations: control linkages, trim, anti-spin features and aircraft-specific layouts. Do not infer a generic procedure from an image of one type. The lesson mentions Tobago anti-spin keels and a Cirrus leading-edge notch as design examples; these are beyond the bank and not a substitute for type documentation.

### Aerodynamics and propeller extras (beyond question bank)

The supplied aerodynamics and propeller extra PDFs contain mostly image-based slides rather than selectable text. Use the examinable figure-reading routines in the cheat sheet and the written lessons; do not treat a schematic as a scale drawing. The question-bank images inspected include the AoA sketch (PFA-003), dihedral diagram (PFA-006), polar (PFA-008), boundary-layer points (PFA-009), chord geometry (PFA-010) and drag curves (PFA-011).

### Spin extra (beyond question bank) and school test / question-and-answer notes

The spin extra reinforces the stall → wing drop → autorotation chain, incipient/developed phases, neutral ailerons, idle power, opposite rudder and forward elevator for the developed-spin teaching sequence, then recovery from the dive. It warns that added power/slipstream can worsen rotation or flatten a spin on some aircraft. Treat all as training theory; actual approved procedure is aircraft-specific.

The school test and oral Q&A repeat the bank's core ideas: laminar flow; weight vs critical AoA/stall speed; flap lift and approach configuration; PFA-008 labels; induced/parasite drag; turn coordination/load; CG and stability; rudder/aileron effects; and control-force trim. The oral explanations clarify that rate-one means 3°/s, rate two 6°/s and rate half 1.5°/s, and that ball/needle indicate different aspects of a turn. A question comparing two weights of the same type has the same critical AoA but the heavier aircraft has a higher stall speed.

## Instructor and exam tips

- Always distinguish *invalshoek/angle of attack* from *instelhoek/angle of incidence*. The Austrian/ECQB translation may use “angle of incidence” where the school means AoA; interpret the geometry in the stem/figure.
- If two answers are technically true, choose the most complete statement. The lesson's CL-curve example prefers a sudden/abrupt decline beyond critical AoA rather than merely “decreases.”
- Check chart axes, scale, units, configuration and reference height before calculating. A lesson stall table is in mph; glide height is height above the destination field, not QNH altitude.
- For a question that says “all other parameters constant,” use the equation's direct proportionality. Do not mix that simplified comparison with a trimmed level-flight change in `CL`.
- Separate turn rate, bank angle, turn radius, load factor and coordination: rate-one is 3°/s, bank for that rate depends on TAS, load factor depends on bank, and the ball shows slip/skid.
- Exam keys select a theoretical answer, not an operating procedure. Use POH/AFM for flap, stall, spin, propeller, speed and load limits.

## Bank coverage audit (all 98 questions)

| Question numbers | Concepts to answer from cheat sheet |
|---|---|
| 1–10 | Pressure, Bernoulli, drag/lift, chord, AoA, AR, stagnation and CP |
| 11–21 | Stall drag, tip pressure equalisation, drag components/curves, induced drag, ground effect |
| 22–29 | AoA/stall, critical angle, weight and turn stall speed, washout, stall/spin recovery |
| 30–45 | Flap trim, slot, boundary layer, longitudinal/lateral/directional stability, axes, adverse yaw, balance/trim, VNE |
| 46–52 | Wing loading, prop blade twist/ice, turn force/bank/rate, horizontal climb force component |
| 53–70 | CP, AoA, vortex start, stagnation, CP movement, washout, CD/AR, interference, drag chart, slat/flap, stall warning |
| 71–90 | Flap coefficients/Fowler/take-off/go-around, boundary layer, static stability, flight AoA/CG/control, gust load |
| 91–98 | Constant-speed prop, windmilling, prop lever, polar points, turn stall speed, tip-vortex induced drag, spin/spiral |

**Cross-check result:** each of the 98 bank questions maps to a definition, formula, table, decision rule or figure key in the cheat sheet. Where lesson wording is simplified or aircraft-specific, the cheat sheet preserves the bank's expected answer while explicitly flagging the limitation.
