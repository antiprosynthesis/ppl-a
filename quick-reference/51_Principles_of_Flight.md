# 51 Principles of Flight (Aeroplane) — Exam Cheat Sheet

Use this as a reasoning sheet, not a substitute for the aircraft POH/AFM. Aircraft-specific speeds, limitations and emergency/recovery procedures always come from the approved manual. **Exam-bank answers are identified where an operational simplification needs context.**

## 1. The aerodynamic model

### The four forces

| Force | Symbol | Direction / source | Straight, level, unaccelerated flight |
|---|---:|---|---|
| Weight (gravity) | `W` or `G` | Vertically down through centre of gravity (CG) | Balanced by lift |
| Lift | `L` | Perpendicular to relative airflow / flight path | `L = W` |
| Thrust | `T` | Forward, from propeller/engine | Balanced by drag |
| Drag | `D` | Opposes relative airflow / flight path | `T = D` |

**ERHV** (Dutch: *eenparig rechtlijnige horizontale vlucht*) means straight, level, unaccelerated flight. In a climb/descent or acceleration, resolve forces along and perpendicular to the flight path; do not blindly use `L=W` and `T=D`.

### Pressure, airflow and Bernoulli

- Static pressure acts **in all directions**. Dynamic pressure is the pressure associated with airflow speed: `q = ½ρV²`.
- Bernoulli (steady, frictionless, incompressible flow): `p_total = p_static + q`. Where flow speed increases, static pressure decreases.
- A positive-lift aerofoil normally has lower pressure over the upper surface (extrados) and higher pressure underneath (intrados). Both contribute to lift. The lesson's approximate 70% upper-surface / 30% lower-surface explanation is a teaching model, not a universal fixed split.
- An object in airflow produces drag; an asymmetrical body or a body at an angle to the flow can produce both lift and drag.
- Lift is the aerodynamic-force component perpendicular to the relative airflow; drag is the component parallel and opposite to it.
- Pressure difference leaks around the wingtips from the high-pressure lower surface to the low-pressure upper surface. The resulting tip vortices/downwash produce **induced drag**. Vortices appear whenever the wing is generating lift (the bank answer says from rotation/lift generation).

### Aerofoil vocabulary and diagram reading

| Term | Meaning |
|---|---|
| Leading edge / trailing edge | Front / rear of the aerofoil |
| Chord | Straight line joining leading and trailing edges |
| Mean camber line | Midline between upper and lower surfaces |
| Camber | Curvature of the mean camber line |
| Extrados / intrados | Upper / lower surface |
| Thickness | Distance between upper and lower surfaces, measured perpendicular to the chord |
| Angle of attack `α` (*aanvalshoek/invalshoek*) | Angle between chord and relative airflow |
| Angle of incidence | Fixed installation angle between chord and aircraft longitudinal axis |
| Relative airflow | Airflow opposite the aircraft's flight path; attitude/pitch is **not** angle of attack |
| Aspect ratio `AR` | Span divided by mean chord; equivalently `b²/S` for a planar wing |

**Figure keys from the question bank:**

- **PFA-003:** `α` is chord-to-relative-airflow angle. The direction of flight/relative airflow and pitch attitude are not interchangeable.
- **PFA-010:** label 2 is chord; label 3 is mean camber line; label 4 is maximum thickness; label 1 marks the leading-edge region.
- **PFA-009:** point 1 is the stagnation point. It is near the leading edge, where speed is locally zero and streamlines divide over/under the aerofoil. Aft along the upper surface, the boundary layer transitions from laminar to turbulent and may later separate.
- At positive angle of attack, the stagnation point moves down the leading edge as `α` increases.

### Boundary layer and centre of pressure

- **Laminar boundary layer:** orderly, relatively thin; usually less skin-friction drag, but separates more readily.
- **Turbulent boundary layer:** thicker and more skin-friction drag, but has more energy near the surface and can follow the aerofoil at higher angle of attack before separation.
- Transition point: laminar becomes turbulent. Separation point: flow no longer follows the surface; stall is associated with major separation over the wing.
- **Centre of pressure (CP):** effective point on the chord where the resultant aerodynamic force is treated as acting (the bank's phrasing: point of origin of the aerofoil's aerodynamic forces). Do not confuse it with CG.
- On a positively cambered profile, increasing `α` moves CP forward **until the critical angle**; reducing `α` moves it aft. Near/after stall the pressure distribution changes abruptly and CP may move aft, pitching the nose down. A symmetric bi-convex profile is taught as having CP near 25% chord; do not apply that as a rule for every cambered aerofoil.

## 2. Lift, drag and useful proportions

### Core equations

`q = ½ρV²`  (dynamic pressure)

`L = ½ρV² S CL = q S CL`

`D = ½ρV² S CD = q S CD`

Where `ρ` = density (kg/m³), `V` = true airspeed (m/s), `S` = reference wing area (m²), and `CL`, `CD` = dimensionless lift/drag coefficients. Keep units consistent. The coefficients depend on aerofoil/configuration and angle of attack; they are **not** simply proportional to speed.

#### Calculation: dynamic pressure and lift

1. Convert speed to m/s if using SI; square it.
2. Calculate `q = ½ρV²`.
3. Multiply by wing area and `CL`.

**Worked example:** `ρ=1.225 kg/m³`, `V=50 m/s`, `S=16 m²`, `CL=0.80`.
`q = 0.5×1.225×50² = 1,531.25 Pa`; `L = 1,531.25×16×0.80 = 19,600 N`.

**Scaling trap:** if all else (including `CL`) stays constant, doubling speed multiplies lift by `2²=4`; tripling it multiplies lift by `3²=9`. In actual level flight, the pilot/configuration changes `CL` to balance weight.

#### Calculation: drag

Use `D=qSCD` with the same unit sequence. **Worked example:** `ρ=1.225`, `V=40 m/s`, `S=16 m²`, `CD=0.040`: `q=980 Pa`, so `D=980×16×0.040=627.2 N`.

At fixed density, area and `CD`, doubling speed quadruples parasite/profile drag. During level cruise, `CD` and `CL` change with trim/AoA; use the exam's “all other parameters constant” assumption for the square-law question.

### Aspect ratio, wing loading, finesse

- `AR = b / c̄ = b²/S`. A long, slender wing / high AR reduces induced drag; a short, broad wing / low AR increases it.
- **Wing loading:** `W/S` (weight divided by wing area), not the inverse. Example: `W=10,000 N`, `S=16 m²` gives `625 N/m²`. If given mass, first find weight (`W=mg`); aviation tables may instead quote mass/area in kg/m².
- **Finesse / glide ratio:** `L/D = CL/CD = horizontal distance / height lost` in still air at the appropriate glide condition. A finesse of 8 means about 8 units forward for 1 unit height.
- Elliptical spanwise lift distribution gives the lowest induced drag among the bank's wing-shape choices. Winglets weaken tip-vortex effects; they do not eliminate induced drag.

#### Calculation: aspect ratio and wing loading

**Aspect ratio example:** span `b=10 m`, wing area `S=12.5 m²`: `AR=b²/S=100/12.5=8` (equivalently mean chord `S/b=1.25 m`, then `10/1.25=8`).

**Wing loading example:** aircraft weight `9,600 N`, wing area `16 m²`: `W/S=600 N/m²`. For equal wing area/configuration, more weight means higher loading and greater required lift/speed.

#### Calculation: glide range

Use height **above the intended landing point**, not altitude above sea level: `range ≈ finesse × height`. Convert units at the end. Example: finesse `8.8`, height `6,000 ft` above the field gives `52,800 ft = 8.69 NM` (`1 NM=6,076 ft`), ignoring wind and manoeuvre margins. This matches the lesson's `52,600 ft / 6,000 ft ≈ 8.8` example.

## 3. Drag curves and chart recognition

### Drag components

`Total drag = induced drag + parasite drag`

`Parasite drag = form/pressure drag + skin-friction drag + interference drag`

- **Induced drag (`Di`):** consequence of lift and wingtip vortices; increases with lift demand, falls as speed increases in level flight, and falls with increasing AR. Small AR and high lift coefficient mean more induced drag.
- **Parasite drag (`Dp`):** form/pressure + skin friction + interference; rises approximately with `V²`. Interference is prominent where flows meet, e.g. wing/fuselage root.
- **Interference drag** is one component of parasite drag, not a separate addition to parasite drag in the total-drag equation. Compressibility/wave drag is mainly a high-speed consideration, outside ordinary light-aeroplane PPL speeds. The drag coefficient `CD` has a non-negative minimum; it cannot be negative.
- In a steady level-cruise speed increase: parasite drag increases while induced drag decreases. With a speed decrease, the reverse is true.
- **Minimum total drag / best L/D:** induced and parasite drag are equal at the minimum-total-drag condition in the standard exam model. The same condition is the best-glide angle/speed in the simplified polar treatment.

**PFA-011 drag-versus-speed chart:** curve 1 (falls as speed rises) = induced drag; curve 2 (rises) = parasite drag; curve 3 (U-shaped sum) = total drag; minimum occurs where 1 and 2 meet. Identify curve direction and axes before reading a number. The bank's induced-drag answer is curve 1.

**PFA-008 aerofoil polar:** vertical axis is `CL`, horizontal is `CD`. Moving along the curve changes AoA/flight condition. Point 1 = inverted flight (negative lift); 2 = near zero lift; 3 = fast flight (small AoA); 4 = maximum finesse/best glide (line from origin tangent to polar); 5 = slow flight (high `CL`/large AoA); 6 = post-stall. Do not call point 5 the stall: point 6 is beyond the peak and shows lift loss.

**Ground effect:** near the surface, wingtip-vortex/downwash effects weaken: induced drag decreases and effective lift increases. It is more noticeable with low-wing aircraft in the lesson explanation. It can cause floating after flare; it does not mean parasite drag disappears.

## 4. Stall, load factor and safe speed reasoning

### The stall is an angle-of-attack event

- A stall occurs when the **critical angle of attack** is exceeded, at any indicated speed, attitude or flight phase. It is not defined by a particular pitch attitude or one universal speed.
- Before critical AoA, increasing AoA increases `CL` and lift (if speed/configuration remain constant). Beyond critical AoA, separation causes `CL`/lift to fall sharply and drag to rise. The precise critical AoA is aerofoil/configuration-specific and is **not changed merely by aircraft weight or CG position**.
- Stall warning normally activates just before the stall / stall speed `VS`; common vane/horn systems respond to a local airflow/stagnation-point change. It is a warning, not a stall detector with guaranteed time margin.
- Clues: warning/buffet, high nose attitude may occur, low IAS, sluggish controls, wing drop. Do not wait for all clues.
- Recovery principle: reduce AoA first (unload/push as appropriate), add suitable power, level wings with coordinated rudder/aileron as the aircraft responds, then recover without exceeding limits. Follow the actual POH/AFM and instructor procedure.
- Ice contamination changes aerofoil shape, increases weight/drag and can cause early separation; a small roughness can sharply degrade lift. Treat icing as a serious performance/stall hazard.

### Load factor and banked turns

- Load factor `n = lift / weight` (in straight, unaccelerated level flight `n=1`). It is the aerodynamic load relative to weight, often expressed in `g`.
- In a **coordinated, level, constant-speed turn** with bank angle `φ`: `n = 1/cosφ`. The vertical lift component balances weight; the horizontal component supplies centripetal acceleration. Total lift must increase to preserve altitude.
- At `30°`: `n=1/0.866=1.155` (about `1.15 g`). At `60°`: `n=1/0.5=2 g`. Upward gusts can also increase load factor; weight alone does not determine `n`.
- **Bank is not AoA.** A steep turn increases required lift/AoA and stall speed, even when the aircraft's attitude seems normal.

#### Calculation: load factor from bank

1. Set calculator to degrees.
2. Find `cosφ`; take reciprocal.
3. Example, `φ=45°`: `n=1/0.7071=1.414`. At `60°`, `n=2`.

#### Calculation: stall speed versus load factor/bank

For the same aircraft, weight, configuration and density: `Vs_n = Vs_1g √n`. In a coordinated level turn, `Vs_φ = Vs_1g √(1/cosφ)`.

**Worked example:** wings-level stall speed `50 kt`, bank `60°`: `n=2`, so `Vs_turn=50√2=70.7 kt`. At `30°`, `Vs=50√1.155≈53.7 kt`. The banked-turn stall speed is higher.

### Stall speed versus weight, density, configuration

From `L=W` at stall: `Vs = √[2W/(ρSCLmax)]`. Use this relationship for proportional questions; `CLmax` depends on aerofoil/configuration.

- Same aircraft/configuration/density: `Vs₂/Vs₁ = √(W₂/W₁)`. **Example:** weight rises 20%: `Vs₂=Vs₁√1.20`; if `Vs₁=50 kt`, then `Vs₂≈54.8 kt`.
- Lower weight lowers stall speed; higher weight raises it. Changing weight does **not** change critical AoA.
- Flaps increase `CLmax`, normally lowering the stall speed for the selected configuration (while increasing drag). Slats/slots delay separation/increase usable critical AoA.
- Lower density increases the **true** speed needed to produce the same dynamic pressure; indicated stall speed is approximately tied to dynamic pressure and is much less density-sensitive. Do not choose “lower altitude” as a cause of decreased indicated stall speed in this bank; the correct cause is lower weight.
- An upward gust increases AoA/load factor; turbulence can trigger a stall if near critical AoA.

### Stall warning, spin and spiral dive

| State | Wing / speed / motion | Essential recognition |
|---|---|---|
| Stall | Critical AoA exceeded; lift falls, drag rises | May be straight, turning, climbing or descending |
| Spin | Stall plus sustained autorotation; one wing more stalled; roll + yaw + nose-down pitch | Low IAS near stall, rapid rotation and height loss |
| Spiral dive | Both wings remain unstalled; steep, tightening/high-speed descending turn | IAS and structural loads rise rapidly; not a stalled autorotation |

- A spin can follow an **uncoordinated stall**. Aileron into the rising wing may worsen AoA on the dropping/stalled wing; keep ailerons neutral during the incipient/developed-spin recovery unless POH says otherwise.
- General developed-spin sequence taught in the lesson: power idle, ailerons neutral, apply rudder opposite rotation to stop yaw/rotation, move elevator forward to unstall, neutralise controls when rotation stops, then recover from the dive within limits. **This is not a universal checklist**: use the aircraft's POH/AFM procedure, and never practise without an instructor/approved aircraft and adequate height.
- For a wing drop at the stall, prevent autorotation with coordinated rudder toward the high wing; lower AoA and add power as prescribed. Do not use opposite aileron as the primary spin recovery.
- Bank/lesson wording for stall warning: push/reduce AoA and apply power as appropriate. Confirm actual response with aircraft POH.

## 5. High-lift devices, wing features and aircraft configuration

| Feature | Main effect / exam distinction |
|---|---|
| Trailing-edge flap | Increases camber (Fowler type also moves aft/increases area); at same AoA increases `CL` and drag; lowers approach/stall speed but reduces `L/D` and changes trim. First flap increments often give large lift benefit. |
| Fowler flap | Profile-like flap extends aft from wing, then deflects down; more area/camber. |
| Slot / slat | Leading-edge gap/device energises upper-surface boundary layer; permits higher AoA before separation. Less drag than a trailing-edge flap at a comparable high-lift task; increases usable critical AoA. |
| Fixed slot vs slat | Slot is a fixed passage; slat is a movable leading-edge device that opens a slot. |
| Washout | Wing incidence/twist reduces toward tip, so root stalls before tip; helps keep ailerons effective. Geometric = physical twist; aerodynamic = section change. |
| Stall strip | Forces inboard/root stall first, helping preserve outboard aileron control. |
| Vortex generators | Small vanes energise boundary layer locally, delaying separation. |
| Dihedral (`V` shape) | Improves lateral/roll stability in sideslip. Anhedral reduces that effect. |
| Sweepback / high tail / high wing | Can contribute to lateral or directional stability depending on design; do not confuse with primary control axes. |
| Winglet | Weakens tip vortex/induced drag. |
| Differential aileron | Upgoing aileron travels farther than downgoing; reduces adverse yaw by limiting drag on the down-aileron wing. |
| Frise aileron | Upgoing aileron's nose protrudes into airflow, creating balancing drag; reduces adverse yaw. |
| Ground effect | Reduces induced drag near ground; not a flap or a direct change to CG. |

- Flaps down: lift and drag increase; trim condition changes; CG does not move just because flaps deploy. In the bank, take-off flaps shorten the take-off run, not necessarily improve climb. Use POH setting and performance data.
- Go-around: bank key, where no other aircraft procedure is specified, is retract flaps to an **intermediate** position. The lesson Q&A gives a training sequence such as 30°→20°→10°→0°; that is aircraft/training-specific, not a universal rule. Maintain safe speed and follow POH.
- Never retract landing flaps in a way that causes abrupt lift loss close to the ground; the lesson explicitly warns against reducing flaps during landing approach.

## 6. Stability, axes, controls, trim and limitations

### Three axes — remember L-L-V

| Axis (body) | Rotation | Primary control | Main stability feature |
|---|---|---|---|
| Longitudinal (nose to tail) | Roll | Ailerons | Dihedral / lateral stability |
| Lateral (wingtip to wingtip) | Pitch | Elevator | Horizontal tail / longitudinal stability |
| Vertical (top to bottom) | Yaw | Rudder | Vertical tail / directional stability |

**Mnemonic:** ailerons roll around the long axis; elevator pitches around lateral axis; rudder yaws around vertical axis. “Longitudinal stability” means pitch stability about the **lateral** axis.

### Stability and centre of gravity

- **Static stability:** initial tendency after displacement. Positive = tends back toward original position; neutral = stays displaced; negative = moves farther away. Dynamic stability describes what happens over time (damped, constant or increasing oscillation).
- Horizontal stabiliser mainly contributes longitudinal/pitch stability; vertical stabiliser contributes directional/yaw stability; dihedral contributes lateral/roll stability.
- A forward CG generally increases longitudinal stability and elevator force/rotation demand; too far forward can limit control authority. An aft CG reduces pitch stability and recovery margin, making the aeroplane more manoeuvrable but less forgiving. CG must remain within loaded POH limits; trim does not shift CG.
- Center of pressure and CG are different points. A forward CG requires more elevator deflection at rotation (bank answer). Correct loading is how the CG is controlled.

### Controls and secondary effects

- Ailerons create roll by differential lift. In a right roll, right aileron up / left down; adverse yaw may initially yaw the nose left (bank Q86). Coordinate with rudder.
- Rudder creates yaw; yaw can produce roll through differing wing speeds/dihedral effect. In a coordinated turn, keep the slip/skid ball centred: “step on the ball” (apply rudder toward the ball).
- Elevator creates pitch; its primary effect is pitch about lateral axis. A nose-up input tends to reduce speed/increase AoA; no separate primary yaw/roll effect.
- Differential/Frise ailerons mitigate adverse yaw. Aileron-rudder interconnect, if fitted, also helps coordinate.
- **Aerodynamic control balance** reduces pilot control forces. **Mass/static balance** (counterweight) prevents flutter by balancing the control surface about its hinge. Do not mix the two.
- **Flutter** is potentially destructive aeroelastic vibration; flying above `VNE` risks flutter and structural damage.

### Trim

- Trim tab relieves a sustained control force; it does **not** move the CG. A small tab force at a long lever arm counters the pilot's larger force at a short arm.
- Elevator trim tab moves aerodynamically opposite the elevator's desired effect. In the bank's conventional example: nose tends up → trim tab up, corresponding indicator “nose-down.” Check the aircraft's indicator convention.
- Trim is not the primary means to initiate a manoeuvre. Flap deployment can change trim/balance.

### Speed/load limits from the lesson

| Marking | Meaning |
|---|---|
| `VNE` | Never-exceed speed; do not exceed (flutter/structural damage risk). |
| `VNO` | Maximum normal-operation / normal operating speed. |
| `VA` | Manoeuvring speed as stated in POH; structural protection depends on weight and input, not a licence for abrupt simultaneous full controls. |
| `VFE` | Maximum speed with flaps extended. |
| `VLO` / `VLE` | Maximum landing-gear operating speed / maximum speed with gear extended; commonly `VLO < VLE`. |

Aircraft category/load limits are manual-specific. Lesson examples (beyond bank): normal-category design load around 4g, utility around 4.5g, aerobatic higher; never substitute these examples for the actual aircraft placard/POH.

## 7. Straight flight, climb, descent and take-off concepts

- In steady straight-and-level flight, force balance is `L=W`, `T=D`. The CP/CG offsets and downwash create pitching moments, so trim is needed even when forces balance.
- In a steady climb, a rearward component of weight acts along the flight path with drag; additional thrust/power is required. Lift is perpendicular to flight path and its vertical component supports weight. At the same speed/configuration, climb requires greater AoA than straight-and-level flight. In steady descent, a component of weight aids motion down the flight path. Resolve vectors rather than assuming all force arrows remain vertical/horizontal.
- Climb angle `Vx`: greatest angle / shortest horizontal distance to clear an obstacle. Best rate `Vy`: greatest altitude gain per unit time. Use speeds from POH.
- Rate of climb `ROC` is vertical speed (e.g. ft/min); climb gradient is height gained per horizontal distance; small-angle approximation `gradient (%) ≈ 100 × ROC(ft/min) / groundspeed(ft/min)` or, in consistent units, `100 × vertical speed / horizontal speed`.
- Example from lesson: `ROC=600 ft/min`, `TAS≈120 kt=12,160 ft/min`; gradient ≈ `4.9%` (about 5 ft gained per 100 ft travelled). Approximate climb angle in degrees ≈ gradient (%) × `0.57`; 5% ≈ 2.85°.
- Take-off performance depends on weight, density/temperature, wind, runway surface/slope, power, flap setting and obstacles. Standard obstacle screen in lesson: 50 ft / 15 m. Flaps may shorten ground roll but can reduce climb performance due to added drag.
- “Ceiling” has two meanings: meteorological ceiling is lowest BKN/OVC layer; aircraft service ceiling (lesson definition) is altitude at which climb rate falls to 100 ft/min under standard conditions.
- Descent: use power to manage flight path/rate and pitch to manage speed, within aircraft technique. PAPI/VASI shows path relative to the visual glide slope; it does not replace airspeed control.

#### Calculation: climb gradient / angle

Use same speed units. Example: climb `500 ft/min`, groundspeed `100 kt` (`≈10,133 ft/min`) → gradient `100×500/10,133≈4.93%`; angle `≈4.93×0.57=2.81°`. Wind affects groundspeed and therefore gradient.

## 8. Turns, coordination and rate-one

- To turn, bank the lift vector. The vertical component supports weight; the horizontal component turns the aircraft. Increase total lift to maintain altitude; at a given bank the load factor is set primarily by bank, not aircraft weight.
- A coordinated turn balances the required lateral acceleration with no slip/skid. If the ball is displaced, step on it. Ball indicates coordination, not bank angle; attitude indicator shows bank.
- `Rate 1` = 3°/s = 360° in 2 minutes. `Rate ½` = 1.5°/s = 360° in 4 minutes; `Rate 2` = 6°/s = 360° in 1 minute.
- For a standard rate turn, required bank depends on TAS (higher TAS requires more bank for the same turn rate), not weight or wind. Approximate relation: `tanφ = Vω/g` (`V` in m/s, `ω` in rad/s, `g≈9.81 m/s²`).
- Turn radius at constant speed: `r=V²/(g tanφ)`; faster speed makes a much wider turn at the same bank. This equation is supplementary; the question bank only tests the TAS dependence of rate-one bank.

#### Optional calculation: rate-one bank

For `V=100 kt=51.44 m/s`, rate one `ω=3°/s=0.05236 rad/s`: `tanφ=51.44×0.05236/9.81≈0.275`, so `φ≈15.4°`. Use aircraft/instrument technique and standard approximations in practical flight.

## 9. Propeller fundamentals

- A propeller is a rotating aerofoil: blade lift is thrust. Blade rotational speed is greatest at the tip, so blade angle/pitch is twisted along the span to keep effective AoA/load reasonably even (bank Q47).
- **Pitch** is geometric advance per revolution; effective advance is less in air because of slip. Fine/low pitch suits take-off/low speed; coarse/high pitch suits cruise/high speed.
- Fixed-pitch propeller: engine RPM changes with throttle, airspeed and load; it is efficient around a design condition.
- Constant-speed propeller: governor changes blade pitch to maintain selected **RPM**; it does not hold aircraft speed constant. As speed increases, blade pitch can increase to maintain RPM (bank answer). Power/throttle and RPM/propeller controls are distinct; follow engine/propeller limitations.
- Windmilling propeller after engine failure produces drag, not useful thrust; feathering (where available) reduces drag.
- Propeller icing degrades aerofoil shape and typically reduces power and RPM.
- Bank Q93: in an idle-power descent at constant speed, moving propeller lever aft increases pitch and decreases sink rate. Treat as that exam setup; real operation follows aircraft/engine POH.
- Beyond bank: right-turning propeller secondary effects include slipstream, torque, gyroscopic precession and asymmetric blade thrust (`P-factor`), especially at high AoA. Correct with aircraft-specific rudder technique.

## 10. Figure / question-bank quick index and traps

| Bank questions | Subject / must retrieve |
|---|---|
| 1–10, 53–61 | Static/total/dynamic pressure, aerofoil vocabulary, airflow, pressure distribution, CP/stagnation/transition, AoA and incidence |
| 11–21, 62–67, 97 | Stall drag trend, induced vs parasite, total drag, ground effect, AR/wing shape, wingtip vortices |
| 22–29, 68–70, 90, 94–98 | Critical AoA, weight/stall speed, stall warning/recovery, spin vs spiral, gust load, polar chart |
| 30–33, 71–77 | Flaps, slats/slots, lift/drag/trim effects, boundary layers, take-off and go-around |
| 34–45, 51, 78–89 | Stability axes, primary/secondary control effects, adverse yaw, trim, control balance/flutter, CG |
| 46–48, 91–93 | Wing loading, propeller twist/ice, constant-speed propeller, windmilling/prop lever |
| 49–50, 96 | Turn force resolution, coordinated-turn load factor/stall-speed relation, rate-one bank/TAS |
| 52, 81–83 | Climb/descent force components, AoA in climb vs level, CG/loading and elevator input |

**High-yield exam traps**

1. `α` = chord vs relative airflow; incidence = chord vs fuselage. Pitch attitude is neither.
2. Stall is critical AoA, not “too little speed” by itself. A high-speed accelerated stall is possible.
3. Weight changes required lift and stall speed, **not** the critical AoA. In bank, both `n` and stall speed rise.
4. More speed: parasite drag up, induced drag down (steady level cruise). Total drag is their sum; interference drag is already inside parasite drag.
5. Flaps increase lift **and** drag; slats chiefly delay separation/raise usable AoA. Neither is “free lift.”
6. Longitudinal stability is pitch about the lateral axis. Map body axis to rotation, not by name-matching.
7. Right roll input can yaw left (adverse yaw). Rudder coordinates; differential/Frise ailerons reduce adverse yaw.
8. Aerodynamic balance reduces stick/pedal forces; mass balance prevents flutter. `VNE` exceedance risks flutter/damage.
9. Trim relieves force; it cannot correct an out-of-limits CG.
10. In turns, lift is tilted; the horizontal component turns, vertical component holds altitude. Do not call horizontal lift the centrifugal force.
11. A spin is stalled autorotation; a spiral dive is unstalled and rapidly accelerating. Neutral ailerons for spin recovery; use POH.
12. Read chart axes, units and configuration before choosing an answer. One lesson stall table used **mph**, not kt; an apparent numeric answer can be wrong if units are ignored.
13. The bank may test simplified textbook statements; answer that model for the exam, but use aircraft POH/AFM for flight.
