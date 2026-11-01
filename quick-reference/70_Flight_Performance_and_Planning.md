# 70 Flight Performance & Planning — Cheat Sheet

Exam = 106-question ECQB bank. Calculator allowed (no phone). Charts come from the bank figures (`figures/PFP-*.jpg`, `CAP697.jpg`). Q-numbers below = bank question numbers.
Golden rules: (1) read the unit asked (kg/lb, m/ft, L/USG, kt/mph, cm/m/in); (2) the charts are the "exam charts" – read them as described, then pick the **closest** option; (3) when options are close, redo the maths with the unrounded numbers.

---
## 1. Units, conversions, densities
| Item | Value |
|---|---|
| Avgas (AVGAS 100LL) | **0.72 kg/L** (1 L = 0.72 kg; 1 kg = 1.39 L) |
| Jet A1 | 0.80 kg/L |
| Engine oil | 0.9 kg/L |
| Water | 1.00 kg/L |
| kg → lb | ×2.205 (Q62) ; lb → kg ÷2.205 |
| 1 USG | 3.785 L (Avgas ≈ 6 lb = 2.72 kg per USG) |
| 1 NM | 1852 m ≈ 6076 ft |
| 1 kt | 1.852 km/h ; 1 kt = 1.15 mph |
| 1 m | 3.28 ft ; 1 ft = 0.3048 m |
| 1 inch | 2.54 cm |
| 1 hPa pressure change | ≈ 27–30 ft (ISA 1 hPa = 27 ft; use 30 ft for PA correction) |
| ISA | 15 °C & 1013.25 hPa at MSL; −2 °C/1000 ft (−1.98) up to 36 090 ft |
| Mass ↔ volume | kg = L × 0.72 ; L = kg ÷ 0.72 (Q6: 102 L → 73.4 ≈ 74 kg ; Q7: 5 kg → 7 L) |
| Time | min = decimal h × 60 (2 h 20 = 2.333 h) |

Quick maths: distance = GS × time. Time = dist ÷ GS. Fuel = flow × time. Endurance = fuel ÷ flow.

---
## 2. Mass & balance (M&B)
### 2.1 Definitions (Q1–15, 58–67)
- **CG** = point where the total weight acts. **Datum** = reference point arm is measured from (arm negative if in front of datum).
- **Arm** = distance datum → item CG. **Moment = mass × arm.** **CG = ΣMoment ÷ ΣMass.**
- **Standard empty mass** = airframe + engine + fixed equipment + **unusable fuel** + **full oil** (+ hydraulic fluid) (lesson). **Exam wording (Q4):** basic empty mass = aeroplane + fixed ballast + unusable fuel + **undrainable oil** + total engine coolant + hydraulic fluid — pick this option (small lesson/bank difference on oil). **Basic empty mass** = standard + optional equipment. In the empty-mass log (PFP-006) take the **LAST/latest** entry.
- **Useful load** = MTOM − basic empty mass (= crew + pax + bags + usable fuel + oil if not in empty mass).
- **Payload** = pax + baggage + cargo (excl. crew/fuel). **Zero-fuel mass** = everything except usable fuel.
- **MRM / ramp mass** = incl. start/taxi fuel. **MTOM** (take-off), **MLM** (landing), **min flight mass**. Burnt fuel reduces mass → landing mass = TOM − trip fuel.
- Weighed every ≤ 6 years (lesson); changes need an update of the W&B sheet.
- Check the **max masses first** (MTOM, MLM, zero-fuel, baggage limits) *before* the CG – quick elimination.

### 2.2 Effects of CG position (Q59, 61, 64–67)
| Forward CG | Aft CG |
|---|---|
| More stable (static + dynamic) | **Less stable** (decreased longitudinal stability) |
| Higher stall speed, more elevator force/needed | Lower stall speed, better cruise speed |
| **More fuel consumption** (more trim drag) | Less fuel burn, longer range |
| Risk: can't flare/rotate (nose-heavy) | Risk: can't recover from stall/spin, tail-heavy, uncontrollable |
So "forward CG" = **1) more stability, 2) more fuel, 3) higher stall speed**. Out-of-limits fixes: move baggage forward/aft, swap rear/front passengers, take less fuel/baggage.
Moving mass: **ΔCG = m × distance ÷ total mass** (shift = mass moved × distance moved / total mass).

### 2.3 Standard method (table)
```
Item          Mass      Arm       Moment (=m×arm)
Empty         ...       ...       ...
Pilot/front   ...
Rear pax      ...
Baggage       ...
Fuel (L×0.72) ...
Oil (if not included)  → can be negative moment
TOTAL         Σm        —         ΣM       CG = ΣM / Σm
```
Fuel/oil in litres → convert to kg first (×0.72 / ×0.9). Keep units consistent (kg·m with m; lb·in with in; "moment/100" or /1000 in tables → rescale!). Answer options may be in cm: ×100.

**Worked – PFP-052e (lb, in):** total 4217.5 lb, total moment 598 824.5 lb·in → CG = **142.0 in** (Q16).
**Worked – PFP-053e (kg, m):** fuel 60 L × 0.72 = 43.2 kg @ 0.45 m = 19.44; total 768.2 kg, moment 285.19 kg·m → CG = 0.3712 m = **37.1 cm** (Q71).
**Morane example (beyond bank):** 455 kg/420 + oil 4.5/−2.5 + fuel 57.6/61.46 + front 150/142.05 + rear+bag 90/159.93 = 757.1 kg, 780.94 → 1.031 m (max 770 kg ok).

### 2.4 CG after fuel burn / load change (Q68–70)
New mass = old − burnt; new moment = old − (burnt kg × tank arm); CG = M/m.
- **Q68:** (2300×95.75 − 170×87) ÷ 2130 = **96.45 in** (170 lb burnt at arm 87 in; 2300 lb at 95.75 in).
- **Q69:** 30.5 L × 0.72 = 21.96 kg at 45 cm → **36.9 cm**.
- **Q70:** 55 L × 0.72 = 39.6 kg at 0.40 m → **24.8 cm**.
Fuel behind CG burnt → CG moves forward; fuel ahead of CG burnt → CG moves aft.

### 2.5 CG envelope (PFP-004; Q17)
Plot mass (vertical axis kg right) against moment (top axis, in mm·kg or kg·mm /1000). Compute the loaded point: find mass on the vertical axis, moment on the horizontal axis, mark the intersection; **inside the polygon = OK**. If a line (e.g. for max zero-fuel or landing mass) is given, test both TO and landing point (landing: subtract trip fuel). Q17: 725 kg and moment 650 → **point 3**.
Loading graph (beyond bank, C172 style): item mass → up to item line → across/down to moment/1000. Add moments, total mass → envelope point.

---
## 3. Fuel planning (Q44, 57, 98–105)
**Required fuel (VFR, EASA)** = taxi + trip (take-off+climb+cruise+descent+approach) + **contingency** (typically 5 % of trip or as stated, e.g. 30 % in Q44/100) + **alternate** (to alternate incl. approach) + **final reserve** (VFR day: 30 min; night: 45 min at cruise power) + additional.
- **Trip fuel (Q98)** = climb + cruise + descent only: 12 + 25 + 7 = **44 L** (excludes taxi/alternate/reserve).
- **Q44:** 3 h × 11.9 GPH = 35.7 USG; +30 % = 46.4; + 2 USG taxi = **48.4 USG**.
- **Q57:** fuel left 120 lb; minus alternate 40 and final 30 = 50 lb usable; rate (200−120)/25 min = 3.2 lb/min → 50/3.2 = **15.6 min**.
- **Q100:** 180 kg total incl. 30 % reserve ⇒ 54 reserve, 126 trip. After half the trip 100 kg left ⇒ 80 used in half ⇒ 20 kg at destination = **landing fuel** (reserve included).
- **Q101:** (80−20) USG ÷ 2.333 h = **25.7 USG/h**.
- **Q104:** trip 70 + 5 % = 73.5; used 40 at half → total 80; remain 15 vs required 20 reserve → **insufficient**.
- **Q105:** used 30 at half → total 60; 90−60 = 30 at landing; − 20 reserve = **10 USG extra**.
General: **fuel at destination = start fuel − used on trip**; compare with reserve/alternate. Fuel used in the first half ×2 = trip fuel (if flow constant).

**Endurance** = usable fuel ÷ flow (subtract unusable and reserve). Example (test): 24.2 − 3.2 unusable = 21.0; 136 NM ÷ 86 kt = 1.58 h × 10.5 = 16.6 → 4.4 USG left.

---
## 4. Wind, GS, time (Q25, 81, 84; beyond bank: planning)
- **Headwind component = V·cos(α)**; **crosswind = V·sin(α)**, α = angle between wind direction and runway/track.
- Runway 22 (220°), wind 250/10 → α=30° → HW = 10·cos30 = **9 kt** (Q25).
- Runway 36, wind 240/12 → α=60° → HW/TW = 12·cos60 = **6 kt tailwind**, XW = 12·sin60 = **10.4 kt** from the left (Q81/84).
- Shortcut: α 30° → HW 0.87, XW 0.5; 45° → 0.7/0.7; 60° → 0.5/0.87. Wind direction is **from**.
- **Max wind at angle for XW limit** = limit ÷ sin α (12 ÷ sin30 = 24 kt).
- **Wind triangle:** WCA = asin(W·sin(wind angle)/TAS); GS ≈ TAS ± headwind component. Round trip with wind: t = d/(TAS+W) + d/(TAS−W).
- **TAS ≈ IAS × (1 + 2 % per 1000 ft)** (Q22: at constant IAS TAS **increases** in a climb). In strong tailwind the TAS for maximum range is slightly **lower**; headwind → higher (Q99).
- **Climb gradient:** rule: **climb % = ROC ÷ TAS** (e.g. 500 ft/min at 100 kt = 5 %); angle° ≈ % × 0.57. Required ROC = height ÷ time. Tailwind: same time and ROC, longer distance.

---
## 5. Take-off & landing performance (concepts; Q18–24, 73–80)
- Ground roll vs take-off distance (TOD) = to **15 m / 50 ft** obstacle. LDA, TORA, TODA, ASDA: declared distances; landing distance required must ≤ **LDA** (Q45: LDA 500 m < 550 m → **No**).
- **Longer** roll: high mass, high temperature/high elevation (low density), tailwind (Q73), soft/long grass, wet, uphill slope, flaps wrong, low tyre pressure, low power, rain/snow/slush. **Shorter**: headwind, downhill, low mass, dense air (Q106: higher temp → lower density → less power).
- Take-off distance/gradient: **headwind** shortens distance and gives steeper climb-out path; **tailwind** lengthens. Strong **headwind shortens landing distance** (Q20). Decreased tailwind → leaving the shear layer on climb-out: increasing tailwind = airspeed and ROC **decrease** (Q74).
- **Flaps (Q18, 19, PFP-007):** more flaps (take-off setting) = shorter ground roll & lower lift-off speed but poorer climb angle/rate. In PFP-007: A has shorter roll but shallower climb → **higher flap setting**.
- **Vx** = steepest climb (obstacles, minimum distance), **Vy** = best ROC (min time). Vx < Vy. Absolute ceiling: ROC 0; service ceiling: ROC 100 ft/min.
- **Ground effect** (beyond bank): within ~½ wingspan of ground; reduces induced drag → float in flare; low-wing aircraft more affected.
- **Speeds on ASI (PFP-008, Q23):** 1 = V_S0 (bottom white arc), 2 = V_S1 (bottom green), 3 = V_FE (top white), 4 = V_NO (top green / bottom yellow), 5 = V_NE (red line, top yellow).
- Stall speed rises with mass, bank (√(1/cos φ): 60° bank ×1.41), forward CG, flaps up, g-load.
- **Rules of thumb (beyond bank, C172 tables):** TOD +10 % per 25 °F (≈ 14 °C) above standard; grass +7 % (or +15 % of ground roll for other types); landing: −10 % per 5 kt (or 9 kt per chart) headwind, +20 % dry grass. **Always follow the footnotes of the table/chart in the question.**

---
## 6. Chart cookbook (read exactly this way)

### 6.1 PFP-009 – Take-off distance nomogram (m) (Q24, 82, 83)
Order of sections left → right: **OAT → pressure altitude → mass → wind → distance**.
1. Start at OAT on bottom axis; go **up** to the PA line (interpolate between PA lines; ISA line optional).
2. Go **horizontally** right to the first **reference line** (mass section).
3. Follow the **guide lines** (parallel, curved) to the actual mass (the 750 kg-start); then horizontal to the next reference line (wind).
4. Follow guide lines to the wind speed on the bottom (solid = **headwind**, dashed = **tailwind**); then horizontally to the right axis; read m.
**Answers:** Q24 = **380 m**; Q82 = **900 m**; Q83 = **880 m**.

### 6.2 PFP-011 – Rate of climb (Q27, 89, 90)
OAT → up to PA line → horizontal to the weight diagonal/mass line → down to read ROC. **Answers:** Q27 = 390 ft/min; Q89 = 200; Q90 = 480.

### 6.3 PFP-012 – Power / cruise table, 785 kg (Q29, 85)
Columns: 20 °C below ISA | ISA | 20 °C above ISA; rows by PA & rpm/BHP%: TAS & fuel flow (l/h). **Use pressure altitude** (FL60 ⇒ PA 6000; QNH irrelevant). Find ISA dev = OAT − (15 − 2×PA/1000).
- Q29: FL60, ISA−20, 70 % → **110 kt, 23.9 l/h** (as asked).
- Q85: PA 2000, 31 °C (=ISA 11 +20), 2400 rpm → **19.5 l/h**.

### 6.4 PFP-013 – Range (Q28, 86)
Layout: left block = OAT axis (−40…+40 °C, bottom) with diagonal **pressure-altitude lines** (MSL, 2000 … 12 000 ft); right block = range axis (400–550 NM, bottom) with three near-vertical **power curves** (75 % leftmost = shortest range, 65 %, 55 % rightmost = longest). Printed "Sample": −5 °C, 10 000 ft → 500 NM at 65 %.
1. Mark OAT on the bottom axis and go **straight up** until you hit the diagonal line of the given pressure altitude (interpolate between lines if the PA is in between).
2. From that point go **horizontally right**, across the vertical thick line, until you meet the curve of the given power %.
3. From the curve go **straight down** and read NM on the range axis (each small box = 10 NM).
- **Q28** (6 °C, PA 6000, 65 %): up from 6 °C to the 6000-ft line → right to the 65 % curve → down = **482 NM**.
- **Q86** (22 °C, PA 2000, 55 %): up from 22 °C to the 2000-ft line → right to the 55 % curve → down = **500 NM**.
Traps: curves are almost vertical so the ranges differ little – pick the nearest option; use PA (not altitude); higher altitude line → higher on the page → shifts the answer slightly (a bit more range).

### 6.5 PFP-014 – TAS vs altitude/temp, power lines labelled 55 % (17 l/h), 65 % (20 l/h), 75 % (23 l/h) (Q87, 88, 91)
Go from OAT up to the PA line, horizontally across to the power line, read TAS below; fuel flow from the power label (**interpolate** between lines).
Q87 = **92 kt**; Q88 = **104 kt**; Q91 (FL85, −25 °C, 60 %) → 85 kt and between 17 and 20 l/h → **18.5 l/h**.

### 6.6 PFP-023 – Time, fuel & distance to climb (Q26, 92, 93)
Chart: OAT/PA at left, cumulative time/fuel/distance at right (diagram bottom right). **Read the value at the top altitude and at the start altitude, then SUBTRACT.** For a start altitude not at SL, convert both the temperature-corrected PA points.
Q26 (3000 ft, 25 °C → FL75, 0 °C, 3000 lb) = **7 NM**. Q92 = **1 gal**. Q93 (FL65 → FL95) = **6 NM**.

### 6.7 CAP697 Table 2.2.3 – 23" Hg / 2300 rpm, 3400 lb (Q102, 103, 44)
Rows: ISA dev (−20/0/+20) × PA. Columns: IOAT, MAP, PPH, **GPH**, **KIAS**, **KTAS**. **Interpolate between PA rows** when FL is between rows. FL → PA (use ISA with 1013). 
- Q102: FL75, ISA → **TAS 160 kt, 11.9 GPH**.
- Q103: FL65, ISA+20 → **IAS 142 kt**, 11.5 GPH (asks IAS!).

### 6.8 Charts seen in the lessons (beyond bank)
- **Take-off/landing table (C172):** interpolate between 2 PA rows (and temperature), then apply footnotes, e.g. (1005+720)/2 = 862.5 ×1.1 = 949 ft. **Order of corrections: table → temp/wind → surface.**
- **Density altitude chart:** PA = altitude + (1013 − QNH hPa) × 30 ft; DA = PA at actual temperature (ISA deviation ×120 ft/°C).
- **Crosswind chart:** wind speed arc × angle line → read headwind (vertical) & crosswind (horizontal).
- Power curves: min power = max endurance; tangent from origin = (L/D)max = best range/glide (Vy-ish for power, Vx-ish for thrust).

---
## 7. Altitudes, levels, VFR rules (Q47–48, 94–97)
- **Altitude** = above MSL (QNH); **height** = above ground/aerodrome (QFE); **FL** = on 1013.25. Q47: "9500 FT AMSL" = altitude 9500 ft.
- **Semicircular rule (Q48, 95):** based on **MAGNETIC course** (variation applied: MC = TC − E, i.e. East is least; W add). Q48: TC 181°, var E 3° → MC 178° → 000–179° → **odd thousands +500** (VFR). Lowest VFR level above 3000 ft/FL050 → **FL055**. 180–359° → even thousands +500 (FL065, FL085…).
- VFR cruising levels: 000–179° → FL035, 055, 075, 095…; 180–359° → FL045, 065, 085…
- **MEF (Q33)** = highest elevation in the 30'×30' quadrangle + safety margin, rounded up to the next 100 ft.
- Airspace upper/lower limits (Q96–97): LO R 16 "1500 FT MSL / GND" → upper 1500 ft MSL; LO R 4 → 4500 ft MSL upper.
- Interception (Q94): lines/features that help orientation when lost.
- Icing (Q49): **leave the icing area without delay**.

---
## 8. ICAO flight plan (Q50–56) & NOTAM (Q46)
Fields: **3** message type (FPL) · **7** aircraft ID · **8** flight rules (**V** VFR, I IFR, Y, Z) + type of flight (G general) · **9** number/type/wake · **10** equipment/SSR · **13** departure aerodrome + **EOBT (UTC)** · **15** cruising speed (**N0100 = 100 kt**, K = km/h, M = mach), level (F095 = FL95, A045 = alt 4500 ft), route · **16** destination + **total EET** + alternate(s) · **18** other info · **19** endurance, persons on board, emergency equipment.
**PFP-051 sample:** OEABC, V G, DV20/L, ORV/C, LOWK 2000, N0100 F095, KFT GRZ PUBEG SNU, LOWW EET 0215, ALTN LOAN. **Q52** speed field = 100 kt. **Q51** EOBT in UTC.
**Q53 (PFP-051a):** flight rule V + EOBT 2000 ⇒ answer = "night flight under VFR" (bank's answer – check against EOBT/sunset: ambiguous wording).
- **Q54** flight plan **required** for cross-border flights. **Q50** file in flight → with FIS. **Q55** uncontrolled aerodrome: report take-off time immediately after take-off. **Q56** landed elsewhere → contact AIS/ATS promptly (close flight plan).
- **Flight log (nav log):** checkpoints/idents, frequencies, MSA, ALT/FL, **M TRK**, **M HDG**, GS, DIST, TIME/ETE, ETA/ATA, fuel on board/remaining; header: clock start/stop, safe flight time (**sunset −45 min** limit). Required on board with W&B sheet.
- **NOTAM (Q46):** Q) line; A) location (LEPA = Palma); B)/C) validity in **UTC** (YYMMDDhhmm: 2111212200–2111220500). Answer: Palma, UTC.
- **Map items (Q30–32, 34–43) – methods (figures EC-70-001…007 checked):**
  **A) Which airspace at a point / altitude (Q30, 31, 32, EC-70-004 Linz, EC-70-006 Luxembourg):** (1) locate the numbered point on the route; (2) find the blue/red airspace box that contains it (TMA = blue outline, CTR = red); (3) read its **stacked labels**: class, lower limit – upper limit, e.g. `TMA LNZ 3 "C" FL195–FL245 / "D" 4500–FL195 / "E" 1000AGL–4500`; (4) choose the band that contains your altitude (altitudes are MSL; AGL/GND = above ground; FL above ≈ transition). Same position, other altitude = other class.
  - Q30: overhead Eferding (point 2), 5000 ft → within 4500–FL195 → class **D**. Q31: 6500 ft, same point → **TMA LNZ 3 "D"** (not LNZ 1, which lies south; not "C", which starts at FL195).
  - Q32: Luxembourg chart, point 1 near Noertrange at 4500 ft → band "D 3500–FL165" → **D**.
  **B) Frequency of an airport/navaid (Q36–38, 42, 43, 37):** read the airport legend/blue VOR box next to the symbol: `LMML Luqa 297° 135,100 / APP 128,150 / ATIS 127,400 / GND 121,600`. Midfield crossing of the Luqa CTR/TMA at 6500 ft (above the CTR, inside TMA C 2000–FL195) → request clearance from **APP 128.150** (Q36); ATIS = **127.400** (Q38). Q37: EDHM Hartenholm legend "118,130" → **118.130**. Q42: DIK box "Diekirch 114,4 DIK" → **114.40**. Q43: "Saint Prex 113,90 SPR" → **113.90**. Traps: Tower/ATIS/Approach/Ground frequencies sit together – pick the one named in the question; comma = decimal point.
  **C) Radio-aid check of a turning point (Q39, 40, 41):** radial = bearing **FROM** the station (QDR); draw a line from the VOR symbol through the point; its magnetic bearing (compass rose around the VOR, or protractor on the north line) = radial; add DME if the point lies on a given distance. Q39 point 2 (Vlasim VOR/DME VLM 114.30, point is NNW) → **R330 + DME**. Q40 point 5 is WSW of Dolsko VOR/DME (DOL 112.7) → **radial 245**. Q41 KILO (point 1) from Linz VOR/DME LNZ 116.60 → **R018 + DME**. A point north-east of a VOR has a radial ~045; south = 180; west = 270 etc. – check with a rough compass-rose estimate to eliminate wrong options.
  **D) ICAO symbols (Q34, 35):** group of unlighted obstacles = option **C**; general spot elevation = option **C** (small dot with elevation number; spot elevations are dots/crosses, obstacles are triangle-based). Pick by image as in the bank.

---
## 9. Exam traps checklist
- Fuel L → kg ×0.72 (not 0.8!). Oil ahead of datum = negative moment.
- kg/lb or m/in/cm mix-ups; moment tables scaled /100 or /1000.
- FL ≠ altitude: use **pressure altitude** for chart entries, QNH irrelevant for FL.
- Subtract bottom from top for climb charts.
- Q103 asks IAS, not TAS.
- Semicircular rule uses **magnetic** course.
- Trip fuel excludes taxi, alternate, reserves.
- Fuel burn: landing CG ≠ take-off CG.
- Wind is "from"; headwind uses cos, crosswind sin; tailwind → longer take-off/landing.
- Table footnotes (+10 %, +7 %, grass) apply to the figure(s) the footnote names.
- Lesson vs bank: lessons mix MPH/kt for stall tables; bank charts are consistent per chart. Prefer bank answers.

---
## 10. Definition / concept answer key (every non-calculation question)
| Q | Answer to memorise |
|---|---|
| 1 | Exceeding max mass = not permissible and dangerous |
| 2, 63 | Secure loads to avoid CG shifts; otherwise uncontrollable attitudes, structural damage, injuries |
| 3 | To determine basic empty mass: **drain all usable fuel** (unusable stays) |
| 4 | See 2.1 (fixed ballast, unusable fuel, undrainable oil, coolant, hydraulic fluid) |
| 5 | AVGAS 100LL = 0.72 kg/L |
| 6 | 102 L × 0.72 = 73.4 → **74 kg** |
| 7 | Ramp 1145 − MTOM 1140 = 5 kg → 5 ÷ 0.72 = **7 L** to burn on taxi |
| 8, 9, 64 | CG = point where total mass/weight acts |
| 10, 11, 67 | Balance arm = distance datum ↔ CG of a mass |
| 12 | Moment = mass × arm |
| 13, 15 | Data in **mass & balance (weight & balance) section of the POH/AFM of this particular aircraft** (not performance section, not C of A) |
| 14 | Empty mass/CG initially determined **by weighing** |
| 16, 17, 71, 72 | see 2.3–2.5 |
| 21 | Angle of descent = angle between horizontal plane and actual flight path (°) |
| 58 | CG must be between forward and aft limit |
| 59 | Rear CG → decrease of stability |
| 60 | CG within limits in all phases ⇒ stability and controllability |
| 61 | Forward CG → 1,2,3 (stability, fuel consumption, stall speed up) |
| 62 | kg × 2.205 = lb |
| 65, 76 | Unaccelerated/steady flight: thrust = drag, lift = weight (four forces in equilibrium) |
| 66 | Datum = reference point on the longitudinal axis from which all arms are measured |
| 75 | Vx = given altitude reached in minimum **distance** (steepest climb) |
| 77, 80 | Vy = best rate of climb (minimum time to altitude) |
| 78 | VFE = maximum flap-extended speed |
| 79 | VS0 = stall speed / minimum steady flight speed in landing configuration |
| 45 | Check NOTAM/chart: the NOTAM shortens the usable runway at LOKH to LDA 500 m (< required 550 m) → **No**, not safe as alternate |
| 49 | Icing: flight into known/forecast icing prohibited unless equipped; if inadvertent, leave the area without delay |
| **106** | *"How does air temperature influence the output of a piston engine?"* → **Higher temperature = lower air density → lower engine power** (cold air = denser = more power; the other options have the logic reversed) |

## 11. Final cross-check (all 106)
Q1–15 §10/§2 · 16–17, 68–72 §2 · 18–24, 73–80 §5/§6 · 25, 81, 84 §4 · 26–29, 82–93 §6 · 30–43 §8 · 44, 57, 98–105 §3 · 45–56, 94–97 §7/§8 · 58–67 §2/§10 · 102–103 §6.7 · 106 §10. All 106 questions are answerable from this sheet; the only ones that still need the actual picture are Q34/35 (symbol letters) and the exact map readings in Q39–41 (bank answers given).
