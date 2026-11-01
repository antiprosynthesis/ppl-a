# 70 Flight Performance & Planning — Detailed Lesson Notes

Sources: lessons 31–33, ECQB deck, EXTRAs slides, TEST + solutions (OPL), flight log / W&B / FPL forms.
**Marking:** items not tested by the 106-question bank are labelled **(beyond question bank)**. Bank questions are written Qn. The compact exam version is `quick-reference/70_Flight_Performance_and_Planning.md`.
Teacher tips (general): the exam uses the **small footnotes** under tables and charts; exam examples come from the book's chart examples; units are mixed on purpose (kg/lb, L/USG, kt/mph, °C/°F); only a simple calculator is allowed; use a ruler and a fine pencil on charts.

---
# LESSON 31 — Weight & Balance (theory)

## 31.1 Context
- Flight time, fuel and GS (from Navigation) return here as **flight planning**: flight log, intermediate times, fuel.
- The POH/AFM holds the tables and graphs with mass and moment limits per type. Mass and moment decide the balance at take-off, in flight and at landing. Q13/Q15: masses and arms come from the W&B section of the POH of **this** aircraft.
- Other limitations: runway length/surface, take-off roll, TOD, landing distance, fuel burn, wind, altitude. Types used in class: Cessna 150/152/172, Mooney, Tobago, Piper. Principle is identical; the skill is reading the **conditions** of each table.

## 31.2 Loads and limits
- Total mass = empty aircraft + variable loads (passengers, fuel, baggage, sometimes oil). The CG may move but must stay between the **forward and aft limits**.
- Too much weight forward/aft makes the aircraft nose-/tail-heavy; compensating needs elevator, whose travel is limited, hence the limits. Q58: CG between front and rear limit. Q60 / test item 2: limits apply in **all phases** (stability and controllability).
- Fuel tanks are often near the empty CG, so burning fuel moves the CG little but reduces mass; always check the **landing** case too. The bank (Q68–70) uses tanks with their own arm, so the CG does shift.
- **Datum:** often the firewall; sometimes the spinner. Q10, 11, 66, 67: arm = distance from datum to the CG of that mass. The datum is placed far forward so all arms are positive (fewer sign errors).
- **Oil:** some manufacturers count it as variable (ahead of the datum → negative moment), others include it in empty mass. Unusable fuel belongs to the empty mass.
- Manual examples give real arms but not real masses — use your own masses.
- Empty mass: certificate / W&B section; re-weigh about every 6 years; modifications need an updated sheet. Q14: determined by **weighing** (3 wheels on scales in flight attitude; tail-dragger: tail raised on a barrel). Q72 / PFP-006: use the **most recent** entry.
- **Moment** = arm × force; use kg·m. Positive = clockwise, negative = anticlockwise. Seesaw demo: big mass × short arm = small mass × long arm.
- Lateral balance is ignored for light aeroplanes, but fuel tanks are alternated; matters for helicopters (beyond question bank).
- Densities by heart: **Avgas 0.72, Jet A1 0.8, oil 0.9** (Q5).
- Secure baggage (Q2, Q63): shifting loads cause uncontrollable attitudes, structural damage, injuries. (Cessna 150 baggage areas: beyond question bank.)

## 31.3 Terminology
1. **Standard empty weight** — aircraft incl. unusable fuel, operating fluids and engine oil.
2. **Basic empty weight** — standard + optional equipment; start of every calculation. (Q4 wording: aeroplane + fixed ballast + unusable fuel + **undrainable** oil + coolant + hydraulic fluid — pick that.)
3. **Useful load** = max ramp weight − basic empty weight.
4. **Payload** = passengers, bags, cargo.
5. **Max ramp (taxi) weight** — includes start/taxi/run-up fuel (Q7: ramp 1145 − MTOM 1140 = 5 kg ≈ 7 L).
6. **MTOW**; 7. **minimum flight weight**; 8. **MLW**.
- Q3: for basic empty mass, drain all **usable** fuel.

## 31.4 Calculation procedure
1. List items; mass and arm from the manual; moment = mass × arm.
2. Oil not in empty mass → negative moment.
3. **Add masses first**; if over max, stop and fix.
4. CG = ΣM ÷ Σm; compare to the envelope.
5. Out of limits: move baggage, swap passengers, reduce fuel.
- Graph methods (book 2.4.3, Fig 2.7–2.11) (beyond question bank except Q17): loading graph (no calculator, low accuracy); CG envelope (mass vs CG); mass vs moment/1000 envelope (no arm needed); Fig 2.11 shows fuel-burn effect on landing mass/CG. Q17: mass–moment envelope, 725 kg, 650 → point 3.
- Q59/61: forward CG = more stability, higher stall speed, more fuel use; aft CG = less stability.
- Flight log and W&B sheet must be on board. Video links (seesaw W&B basics, CG effect on performance) are in the LINKS file (beyond question bank).

---
# LESSON 32 — Calculations

## 32.1 Table examples (book p14–19)
- C172: CG = ΣM/Σm = 103 100 / 2451 = **42.1"**.
- Adding load: 2451 lb → 117.1 (×1000 lb·in); −44 lb, −4.0 → 2407 lb, 113.1.
- Burning fuel: −249 lb fuel (−12.0) → 2202 lb, 91.1 → 91 100/2202 = **41.4"** (CG forward).
- Bank equivalents: Q16 / PFP-052e = 4217.5 lb, 598 824.5 → **142.0 in**; Q71 / PFP-053e = 768.2 kg, 285.19 → **37.1 cm**; Q68 = 96.45 in; Q69 = 36.9 cm; Q70 = 24.8 cm.

## 32.2 Morane Rallye 880B (book p21–23)
- **Ex. 1:** empty 455 kg / 420; oil 5 L; fuel 100 L; pilot 70, front 70, rear 70; baggage 10; max 770 kg. Oil 5 L × 0.9 = 4.5 kg; fuel 100 × 0.72 = 72 kg; arms from table; then ΣM/Σm.
- **Ex. 2:** fuel 80 L, pilot 80, front 70, rear 75, baggage 15:

| Item | kg | kg·m |
|---|---|---|
| Empty | 455 | 420 |
| Oil 5 L | 4.5 | −2.5 |
| Fuel 80 L (57.6 kg) | 57.6 | 61.46 |
| Front seats | 150 | 142.05 |
| Rear + baggage | 90 | 159.93 |
| **Total** | **757.1** | **780.94** → CG **1.031 m**, within limits (max 770 kg) |

## 32.3 Cessna 172 exercise (book p52)
Empty 1507 lb / 56.6; oil 8 qt = 15 lb / −0.3; fuel 36 USG = 216 lb / 10.4; front 374 lb / 13.5; rear 360 lb / 25.8; baggage 60 lb / 5.5 → **2532 lb, 111.3 → CG 44"**. Over the **2300 lb** max → cannot depart: remove baggage, fuel or passengers. Watch the kg→lb conversion.

## 32.4 Other slides (beyond question bank)
- Cessna 150 tables; **PA-28-161 Cadet** loading graph, CG-moment envelope, sample loading problem (ramp mass, −24 lb start/taxi, take-off mass, landing = take-off − trip fuel); limits vary with mass.
- **Wind components** chart (p61): wind arc × angle line → headwind (vertical), crosswind (horizontal). Example: wind 30° off, 40 kt → head ≈ 35, cross ≈ 20.
- **Airspeed calibration** (p62): IAS → CAS from the table.
- **Mooney M20K** tables; **density altitude** chart: OAT up to the PA line, across to the DA axis. Altimeter-setting table gives PA correction (28.0 → +1825 ft; 29.92 → 0; 31.0 → −965 ft).
- EXTRAs also show loading graphs, "useful load" tables, turboprop take-off power charts (torque vs OAT), and complete W&B tables.

## 32.5 Flight log and forms (APCK)
- **Flight log columns:** checkpoint, frequencies, MSA, ALT/FL, magnetic track, heading, GS, distance, ETE, ETA/ATA, fuel. **Header:** clock start/stop, T/O, Ldg, safe flight time (sunset − 45 min), UTC. Blocks for ADEP/ADES/ALTN and a W&B table.
- **ICAO FPL:** Item 3 message type; 7 aircraft ID; 8 flight rules + type of flight; 9 number/type/wake; 10 equipment; 13 departure + EOBT (UTC); 15 speed, level, route; 16 destination, total EET, alternates; 18 other info; 19 endurance, persons on board, emergency/survival equipment, colour, PIC.
- Bank: PFP-051 sample (OEABC, V G, DV20/L, N0100 F095, KFT GRZ PUBEG SNU, LOWW EET 0215, ALTN LOAN). Q52 speed = 100 kt; Q51 EOBT in UTC; Q50 file in flight via FIS; Q54 cross-border → flight plan; Q55 report take-off right after departure from an uncontrolled aerodrome; Q56 landing elsewhere → inform AIS/ATS. Q53: bank answer "night flight under VFR".

---
# LESSON 33 — Performance & planning

## 33.A Take-off distance (book 5.2.4)
**Factors:** runway state (hard/soft, grass, wet), usable length, slope, elevation, temperature (hotter = longer), humidity, rain, water/ice/snow, mass and configuration (flaps 10°, prop type, tyre pressure), **wind (take off into wind)**, engine power. Bank: Q73 tailwind = longer; Q74 tailwind increase → airspeed and ROC decrease; Q106 higher temperature → lower density → less piston power; test 19: increased density does NOT lengthen take-off.
**Definitions:** *Ground roll*; *TOD* = ground roll + distance to clear **50 ft (15 m)**. Read the right column.
**C172 table method** (beyond question bank, practice for footnote logic):
- Ex. 2: 2300 lb, 15 kt HW, 2500 ft, 75 °F, grass: 15 kt is the average of 10 and 20 kt: (1485+1100)/2 = 1293 ft; +10 % for temperature = 1422; grass +7 % → **1522 ft**.
- Ex. 3: 2000 lb, same conditions, hard runway: (1005+720)/2 = 862.5 → ×1.1 = **949 ft**.
- Trap: grass +7 % applies to the TOD; even for ground roll ask, add 7 % of the TOD.
- Stall table is in **MPH**: 50 kt = 57.5 mph.
- **PA-28 graphs** (p63): OAT/PA, mass, wind in one chart (e.g. −20 °C, 2000 ft, 2000 lb, 10 kt HW). Same technique as PFP-009 (Q24, 82, 83): OAT → PA line → mass → wind → distance.

## 33.B Landing distance (book p56)
- Phases: approach, round-out, hold-off, touchdown, roll-out, braking. Terms: **landing distance** (50 ft obstacle) and **ground roll**.
- Tables normally give max mass (worst case).
- **−10 % per 5 kt headwind** (10 kt → 20 %). **Dry grass +20 %**, also for the roll.
- Bank: Q20 strong headwind shortens landing; Q45 LDA 500 m < required 550 m → not an acceptable alternate.

## 33.C More graphs (PA-28-161, beyond question bank)
| Exercise | Answer |
|---|---|
| Stall, 2000 lb, flaps 0°, bank 40° | CAS 52 / IAS 62 kt |
| TO ground roll, +10 °C, 2200 lb, PA 3000, 5 kt tailwind | 1680 ft |
| TOD, −10 °C, 2200 lb, PA 4000 | 2000 ft |
| Landing roll, 0 °C, 3000 ft, 15 kt HW | 460 ft |
| Table: 2000 lb, hard, PA 3000, +20 °C, 10 kt HW | 1750 ft (TOD) |
- Chart types: best-economy cruise; **best-power range**; **best-economy range**; endurance; fuel/time/distance to descend; engine performance (RPM); **fuel/time/distance to climb** (PFP-023: top minus bottom); climb performance; cruise & range table.
- Flaps shorten the ground run but hurt climb angle/rate (Q18, 19). **Oxygen** if more than 30 min above 10 000 ft.

## 33.D Planning exercises
1. **Density altitude:** 12 000 ft, −25 °C, QNH 990 → 23 hPa below standard → PA = 12 000 + 23×30 = 12 690 ft; computer → **DA ≈ 11 000 ft**.
2. **A→B→A**, 240 NM, wind 15, TAS 105, 44 L/h: out GS 120 → 2 h; back GS 90 → 2 h 40; total 4.67 h × 44 = **205.5 L**.
3. **A→B 320 NM**, W/V 270/20, TAS 113 kt, 42 L/h, WR 330°: **GS 102 kt, WCA 9° left → WH 321°**; 188 min; fuel **131.6 L**.
4. **Mountain:** 2000 ft, TAS 88, 15 kt tailwind, mountain 9000 ft at 12 NM, +1000 ft clearance: climb 8000 ft; GS 103 → 7 min → **ROC ≈ 1142 ft/min**.
(Flight computer: put 60 under the GS; read time over distance.)

## 33.E Rules of thumb
- **Climb % = ROC ÷ TAS** (test 7: 5 % at 100 kt → 500 ft/min × 6 min = 3000 ft ≈ 915–926 m).
- **Rate-1 bank = TAS/10 + 7** (110 kt → 18°).
- Climb angle ≈ % × 0.57.
- TAS ≈ IAS × (1 + 0.02 per 1000 ft) (Q22); 1 hPa ≈ 27–30 ft; −2 °C per 1000 ft.
- Fuel planning (Q44, 57, 98–105): taxi + trip + contingency + alternate + final reserve (see quick-reference §3).

---
# EXTRAs slides — theory pictures (beyond question bank unless noted)
- **Drag:** total = induced (falls with speed) + parasite (rises with V²); minimum = (L/D)max.
- **Power required:** minimum power = **best endurance**; tangent from origin = best range. Region of reversed command: slower needs **more** power.
- **Excess power** largest at **Vy**; excess thrust largest at **Vx** (Q75, 77, 80). Service ceiling (100 ft/min) and absolute ceiling (0) where Vx and Vy merge.
- **Heavier aircraft:** curves shift up/right; a lighter glider has a lower best-glide speed (test 21).
- **Ground effect:** within about one span of the ground induced drag drops → aircraft floats in the flare (test 15); stronger on low-wing (test 13).
- **Multi-engine slides:** accelerate-stop distance, 115 % rule, V1/VR/VLO, 35 ft screen; normal landing nomogram — same reading rules as PFP-009.

---
# TEST + SOLUTIONS (2025–2026)

| # | Topic | Answer and working |
|---|---|---|
| 1 | Max wind at 30° for 12 kt crosswind | 12 ÷ sin30° = **24 kt** |
| 2 | CG within limits in all phases | stability and controllability (Q60) |
| 3 | A→B→A 120 NM, wind 20, TAS 90, 6 USG/h | 120/110 + 120/70 = 2.8 h → **16.8 USG** |
| 4 | Taxi fuel to reach MTOM | 5 kg ÷ 0.72 = **7 L** (Q7) |
| 5 | Climb 3000 ft in 6 min / 5 NM, with tailwind | **6 min, 6 NM** |
| 6 | CG PFP-052e | **142 in** (Q16) |
| 7 | 100 kt, 5 %, 6 min | **≈ 926 m** |
| 8 | Shorter landing distance | **strong headwind** (Q20) |
| 9 | 136 NM, GS 86, fuel 24.2 − 3.2 unusable, 10.5 USG/h | 16.6 USG used → **4.4 USG** left |
| 10 | Start of green arc | VS1 (Q23) |
| 11 | 600 ft obstacle, TAS 105, +25 kt tailwind, ROC 100 | 6 min × 130 kt = **13 NM** |
| 12 | Distance to FL75 (PFP-023) | **7 NM** (Q26) |
| 13 | Ground effect on low-wing | **larger than on high-wing** |
| 14 | ELNT 4500 ft point 1 | **D** (Q32) |
| 15 | Ground effect awareness | **reduced induced drag → hard to lose speed in the flare** |
| 16 | Luqa ATIS | **127.400** (Q38) |
| 17 | Longitudinal stability depends on | **CG relative to centre of pressure** |
| 18 | VFR fuel plan (CAP697, 7500 ft ISA, 2300 rpm; 2:42 + 8 + 10 min; taxi 2 USG; reserve 30 %) | 3 h × 11.9 = 35.7 + 30 % = 46.4 + 2 = **48.4 USG** (Q44) |
| 19 | What does not lengthen take-off | **increase of air density** |
| 20 | NOTAM overflight prohibition | **altitude 9500 ft MSL** (Q47) |
| 21 | Glider loses mass (water) | **lower speed** for best glide |
| 22 | Flight abroad | **flight plan required** (Q54) |

---
# Differences between lessons and bank
- Q4: lesson says standard empty mass has full oil; bank says "undrainable oil" — use the bank.
- Lesson: tanks near CG (little shift); Q68–70 give a tank arm → compute the shift.
- Footnotes differ between tables (+10 %/25 °F, +7 % grass, −10 %/5 kt landing vs other charts): **apply the footnote printed with the question's table**.
- Q53 wording is odd — bank answer "night flight under VFR".
- Lesson stall tables are in MPH.
