# 90 Navigation — complete exam cheat sheet

A worked procedure reference for the 131-question navigation bank. Use current approved charts, aircraft documents and the question's stated conventions in real flight; these notes are for theory study.

## 1. Solve every question systematically

1. Identify the requested quantity and its reference: **true / magnetic / compass**, **course / heading / bearing**, and **from / to**.
2. Write down all supplied data with units. Convert units before calculating.
3. Draw a small north-up sketch for bearings, wind, fixes, and 1:60 problems.
4. Select the matching procedure below; keep intermediate values unrounded.
5. Normalize directions to 000°–359° (add/subtract 360° as needed).
6. Check the sense: headwind lowers GS, eastward longitude means earlier solar time in UTC, and a “from” bearing reverses by 180° to become “to”.
7. Estimate the answer before choosing an option. Reject wrong units, wrong direction, and answers based on airspeed instead of groundspeed.

## 2. Earth, coordinates and distances

### Earth and reference geometry

- Earth is approximated as an **ellipsoid** for navigation, not a perfect sphere. The geographic rotational axis runs through the geographic poles and is perpendicular to the equatorial plane.
- Equator circumference ≈ **21,600 NM**. One full circle is 360° × 60 NM/degree.
- **Great circle (GC):** shortest surface path between two points on a sphere; its plane passes through Earth's centre. The equator and meridians are great circles; other parallels are small circles.
- **Rhumb line (loxodrome):** crosses every meridian at a constant angle; constant compass direction. It is not generally the shortest route.
- Along a meridian: **1° latitude = 60 NM**, **1′ latitude = 1 NM** (approximate). Thus a 240 NM northward move adds 4° latitude.
- Along the equator: 1° longitude = 60 NM. At latitude φ, the east-west distance per longitude degree is approximately **60 cos φ NM**.
- For a small-area route, distance from coordinates: north-south component = latitude difference in minutes NM; east-west component ≈ longitude difference in minutes × cos(mean latitude). Combine components with Pythagoras if a short-distance approximation is adequate.
- A degree of longitude is **less than 60 NM away from the equator**. Do not confuse latitude and longitude scale.
- The polar circles are 23.5° from the poles (latitudes ≈ 66.5° N/S).

### Read and write coordinates

- Standard form: degrees, minutes, seconds (e.g. 51°49′48″N) or decimal degrees (51.83°N). **Decimal part × 60 = minutes**: 0.83 × 60 = 49.8′; decimal minutes × 60 = seconds.
- N and E are positive; S and W are negative for arithmetic. When a latitude difference crosses the equator, **add** absolute latitudes (12°53′30″N to 07°34′30″S = 20°28′00″).
- To plot/read a chart fix: read latitude from the horizontal parallels and longitude from the meridians; interpolate between labelled grid lines; state hemisphere and units. Compare the plotted point to prominent labels/airfields, not just nearby towns.
- **Figure EC-90-001:** convert 51.83°N, 12.19°E to about 51°49.8′N, 12°11.4′E; locate the intersection on the chart. The bank's keyed location is overhead EDAD (Dessau), not EDCK or the nearby villages.
- If two points are on the same parallel, use the latitude-dependent longitude distance. For a rough route bearing, use east-west and north-south components and an atan ratio; for chart questions, plot and measure with the chart graticule.

### Bearings and directions on a chart

- Bearings are measured **clockwise from north**: 000°/360° N, 090° E, 180° S, 270° W.
- Reciprocal bearing = bearing ±180°, normalized. A radial is the direction **from** the VOR; the reciprocal is the course **to** it.
- To find a position from two bearings, plot each bearing line from its station (or reciprocal of a radial if the question describes bearing to station). Their intersection is the fix. Check the fix lies on the correct side of both stations.
- A geographic position can be described by a true bearing; a radial is conventionally magnetic.

## 3. Time, UTC, longitude and sun

- Earth rotates 360° in 24 h: **15°/h, 1°/4 min, 1′/4 s**. Longitude time difference = longitude difference × 4 min/degree.
- Local solar time is later to the **east** and earlier to the west. Sunrise/sunset expressed in UTC occur earlier at an eastern longitude. At equal latitude, 3°34′ longitude ≈ 3.57 × 4 = **14.3 min** earlier in the east.
- **UTC** is the standard aviation time reference. CET = UTC+1; CEST = UTC+2. To convert local time to UTC, subtract the stated offset (e.g. 1700 CET → 1600 UTC; 1600 CEST → 1400 UTC). Add offset to UTC for local time. Mind date rollover at midnight.
- Civil twilight: sun's **centre** is 6° or less below the **true** horizon before sunrise/after sunset. Do not substitute apparent horizon or 12° (nautical twilight).
- Sunrise/sunset is affected by date and latitude; use the provided almanac/table when supplied. Longitude gives the UTC shift; do not treat local time zones as solar time.

## 4. Units, chart scale and fuel

### Memorize these conversions

| Quantity | Conversion / useful approximation |
|---|---|
| Nautical mile | 1 NM = 1.852 km = 1,852 m ≈ 6,076 ft |
| Statute mile | 1 SM = 1.609 km ≈ 0.869 NM |
| Kilometer | 1 km = 0.540 NM; 10 km ≈ 5.4 NM |
| Meter / foot | 1 ft = 0.3048 m; 1,000 ft ≈ 300 m; 1 m ≈ 3.28 ft |
| Feet / meters | meters × 3.281 = feet; feet × 0.3048 = meters |
| Nautical miles / km | NM × 1.852 = km; km ÷ 1.852 = NM |
| US gallon | 1 US gal = 3.785 L |
| Imperial gallon | 1 Imp gal = 4.546 L; identify which gallon is specified |
| Mass | 1 kg ≈ 2.205 lb; 1 lb ≈ 0.454 kg |
| Fuel mass | kg = litres × stated fuel density (use question's density; typical avgas ~0.72 kg/L, approximate only) |

- Exam rounding: 5,500 m ≈ 18,000 ft; 1,000 ft ≈ 300 m. Do not mix NM with statute miles or US with Imperial gallons.
- Aircraft fuel quantity is commonly volume; fuel burn/mass questions may require density. Use the given density rather than assuming a universal value.

### Time–distance–speed (TDS)

Use consistent units: knots = NM/hour; km/h = km/hour.

$$
GS=\frac{D}{t_{hours}},\qquad t_{hours}=\frac{D}{GS},\qquad D=GS\times t_{hours}
$$

- Convert minutes to hours: 25 min = 25/60 h. Or calculate directly: **time (min) = 60 × distance / GS**; **GS (kt) = 60 × NM / minutes**.
- Example: 110 NM in 1 h 25 min = 85 min. GS = 60×110/85 = 77.6 ≈ **78 kt**.
- Example: 100 km in 56 min: GS = 100/(56/60) = **107 km/h**. Keep answer in km/h unless converting to knots.
- Example: 236 NM at 134 kt: time = 236/134 h = 1.761 h = **1 h 46 min**.
- For descent/climb time: elapsed minutes = altitude change (ft) ÷ vertical rate (ft/min). 9,000 to 1,500 ft at 1,200 ft/min: 7,500/1,200 = 6.25 min (bank rounds to 6).

### Fuel planning calculation

- Fuel used = **fuel flow × time**. Endurance = usable fuel ÷ fuel flow. Range = endurance × GS. Units must agree (e.g. L/h × h = L).
- Example: 25 L/h for 1 h 30 min uses 25×1.5 = 37.5 L. If 60 L usable, endurance = 60/25 = 2.4 h (2 h 24 min), before reserves.
- Include taxi, climb, contingency, alternate and final reserve only as required by the question/rule stated. Do not count unusable fuel as usable.
- For fuel weight: convert volume to litres, then multiply by the specified kg/L. For gallons, establish US vs Imperial first.

### Chart scale

- Scale 1:n means **1 unit on chart = n of the same units on Earth**. Convert both to the same units before dividing.
- Method: real distance ÷ chart distance = denominator n. Convert NM to cm or km to cm first.
- Example: 220 NM = 407.44 km = 40,744,000 cm. Chart measure 40.7 cm: denominator ≈ 40,744,000/40.7 ≈ **1,000,000**, hence 1:1,000,000.
- Example: 60.745 NM = 112.5 km = 11,250,000 cm; represented by 7.5 cm gives **1:1,500,000**.
- Reverse method: chart length × scale denominator = real length. Do not compare cm directly with NM.

## 5. Airspeed, wind, heading and track

### Airspeed and altitude

- **IAS** is indicated airspeed; **CAS** corrects instrument/position error; **TAS** is speed through the air mass; **GS** is speed over the ground. Wind changes GS, not TAS.
- Rule of thumb: TAS increases approximately **2% per 1,000 ft** above sea level: TAS ≈ IAS × (1 + 0.02 × altitude/1,000). At 8,000 ft, 150 IAS → 150×1.16 = **174 kt**. This is a rough rule, not a precision correction.
- Use CAS, pressure altitude/flight level, OAT, or an E6B/performance chart if specified. For quick questions, stated rule-of-thumb often controls. 155 kt at FL80 by the bank's rule gives ≈180 kt.
- Do not use QNH altitude in place of pressure altitude for an airspeed correction unless the question tells you to.

### Pressure altitude, QNH altitude and true altitude (temperature correction)

- Pressure altitude is altitude with 1013.25 hPa set; flight levels use this reference. QNH altitude is the altimeter indication with local QNH set. True altitude is actual vertical height above mean sea level and changes with air temperature.
- Rule of thumb for temperature error: **4 ft per 1,000 ft per °C** difference from ISA. ISA temperature at altitude ≈15°C − 2°C per 1,000 ft. Warm air: true altitude is higher than indicated; cold air: true altitude is lower.
- Approximate correction = indicated/QNH altitude (thousands of ft) × 4 × (OAT − ISA temperature). Add when warmer than ISA; subtract when colder. This is a rough exam method; use the stated altitude reference and the chart/table if supplied.
- Example: QNH altitude 6,500 ft, OAT +21°C. ISA near 6,500 ft ≈+2°C; correction ≈6.5×4×19=494 ft. True altitude ≈7,000 ft.
- Example: FL75, OAT −9°C, QNH altitude 6,500 ft. ISA near 7,500 ft ≈0°C; cold correction ≈6.5×4×9=234 ft below indicated, true altitude ≈6,250 ft.

### Wind triangle — use this sequence

Wind direction is the direction **from which** the wind blows. Wind 350°/30 kt blows toward 170°.

1. Draw TC/course as the desired ground track, north-up. Draw wind **from** its reported direction; the wind vector itself points 180° opposite.
2. Find relative wind angle to course. Resolve wind into a head/tail component and crosswind component, or use a navigation computer/E6B.
3. Crosswind pushes the aircraft downwind; steer **into** the wind. WCA is signed: right correction positive, left negative (unless question explicitly defines another convention).
4. **TH = TC + WCA.** Normalize to 000°–359°.
5. Calculate GS from the along-track component: GS ≈ TAS + tailwind component (tailwind positive, headwind negative); with a material crosswind use wind triangle/E6B for exact value.
6. Use **GS**, not TAS, for time/distance/ETA.

Approximate component formulas, with δ = wind-from direction minus TC:

$$
H_{head}=W\cos\delta \quad(positive=headwind),\qquad X=W\sin\delta
$$

Crosswind correction magnitude ≈ arcsin(|X|/TAS), for |X|≤TAS; its sign points into the wind. Then GS ≈ TAS cos(WCA) − H_head. These are approximations; solve the vector triangle for exact results.

- Example: TC 040°, TAS 180 kt, wind 350°/30. Wind is from 50° left of track: crosswind ≈23 kt from left, headwind ≈19 kt. WCA ≈ −arcsin(23/180) ≈ **7° left**; TH ≈033°; GS ≈180 cos7°−19 ≈ **159 kt**.
- Example: TC 270°, TAS 100 kt, wind 090°/25 blows toward 270°: direct tailwind, WCA 0°, GS = **125 kt**. For 100 NM, time = 60×100/125 = **48 min**.
- Example: TAS 180 kt, headwind 25 kt for 2 h 25 min: GS=155 kt; duration=2.4167 h; distance ≈ **375 NM**.
- With a direct headwind, subtract it from TAS. Example: 130 TAS, 15 kt headwind, 210 NM → GS 115 kt; time ≈1.826 h; ETD 0915 → ETA about **1105 UTC**.
- WCA asks for the correction angle, not heading. Heading asks for TC plus WCA. If TC is held and the wind changes, recalculate WCA and GS.

### Course/heading and 1:60 correction

- **Course/track** is intended or actual direction over ground; **heading** is aircraft nose direction. Wind makes them differ by WCA/drift.
- 1:60 rule (small-angle approximation): after 60 NM, 1° error produces 1 NM cross-track error.
  $$
  error\ angle(°)\approx60\times\frac{cross\ track\ error}{distance\ flown}
  $$
- For direct recovery to destination, correction angle = **track error + closing angle**. Closing angle ≈ 60 × lateral error ÷ remaining distance to destination. Turn toward the route/destination.
- Example: planned distance 120 NM; after 55 NM, 7 NM right of track. Track error ≈60×7/55=7.6° right. Remaining 65 NM; closing angle≈60×7/65=6.5° leftward intercept. Correct about 7.6+6.5=**14° left**.
- If exactly halfway (90 NM route, 45 flown, 4.5 NM north of eastbound track): error≈6°; remaining closing ≈6°; turn about **12° right** toward the destination.
- A 1:60 problem may ask **drift angle only** (use distance flown) or **corrected course to destination** (add closing angle). Read wording carefully.

### Revised ETA / actual progress

- First compute remaining distance, then use **actual GS** and actual time/checkpoint; do not simply add the schedule error.
- Revised ETA = present time + remaining distance / actual GS. Alternatively, revise remaining leg time; retain elapsed real time.
- If 220 NM total at 120 kt; after 70 NM, the aircraft is 5 min ahead of schedule (actual elapsed = 35 min − 5 = 30 min). Actual GS = 70/(30/60)=140 kt. Remaining 150 NM takes 64.3 min. Depart 1200 → arrival ≈ **1334**, rounded to the bank option 1335 UTC.
- If schedule is ahead/behind but no actual speed or observation time is inferable, don't invent one; use the supplied actual progress information.

## 6. Direction references: TC → TH → MC → MH → CH

Always write each quantity out. Variation and deviation are signed in the equations below: **East positive, West negative**.

$$
TH=TC+WCA;\quad MC=TC-VAR;\quad MH=TH-VAR;\quad CH=MH-DEV
$$

Equivalent reverse conversions:

$$
TC=TH-WCA;\; VAR=TC-MC=TH-MH;\; DEV=MH-CH;\; MC=MH-WCA
$$

- “East is least, west is best” is a mnemonic when converting **true to magnetic**: subtract easterly variation, add westerly variation. In the signed equation true = magnetic + variation, so magnetic = true − variation.
- Compass conversion: magnetic = compass + deviation; therefore compass = magnetic − deviation. A positive/easterly deviation means compass reads low relative to magnetic in this convention.
- Example TC 245°, VAR 7°W (−7): MC = 245−(−7) = **252°**. This is the traditional “east is least, west is best” rule.

**Exam-safe conversion table (traditional aviation mnemonic):**

| Conversion | East variation/deviation | West variation/deviation |
|---|---:|---:|
| True → Magnetic (TC to MC or TH to MH) | subtract | add |
| Magnetic → True | add | subtract |
| Magnetic → Compass (MH to CH) | subtract east DEV | add west DEV |
| Compass → Magnetic | add east DEV | subtract west DEV |

- Apply each step to the heading/course of the same type; do not apply WCA to MC unless converting between course and heading.
- Example: TC 179°, WCA −12° → TH 167°. VAR 4°E → MC=175° and MH=163°. If DEV=2°E, CH=161°.
- Example: TC183°, WCA+11° → TH194°. With VAR4°W, MH=198°. If CH=200°, deviation is 2°W (MH 198 to compass 200); consistent with bank notation DEV = −2°.
- Example reverse: TH125°, WCA−12° → TC137°. MC139° → VAR=2°E by TC→MC relation. DEV2°E → CH=MH−2°.
- The bank’s keyed conversions are consistent with this signed convention: Q58 gives MC252° for TC245°/VAR7°W; Q95 gives VAR4°W; Q95–97 imply DEV2°W (signed −2°).

### Variation, deviation, compass and magnetic earth

- **Variation** is the angle between true and magnetic north at a location; charted and changes geographically/time. Isogonic lines join equal variation; **agonic line** joins zero variation.
- **Deviation** is aircraft compass error caused by the aircraft's own magnetic/electrical fields; it depends on heading and is read from the compass deviation card. Electronic devices can affect a direct-reading compass.
- Compass north is the direction a direct-reading compass aligns under combined Earth's and aircraft magnetic fields.
- Inclination/dip is lowest (approximately zero) at the **magnetic equator**, greatest near magnetic poles.
- Runway numbers are rounded magnetic direction in tens of degrees; a changed magnetic variation can eventually change runway designation even if runway pavement alignment is unchanged.

## 7. Radio bearing/Q-code arithmetic

### Definitions (station is the reference unless stated)

| Code | Meaning |
|---|---|
| QDM | Magnetic bearing **to** the station (magnetic heading to steer in calm wind) |
| QDR | Magnetic bearing/radial **from** the station (magnetic bearing from station to aircraft) |
| QTE | True bearing **from** station to aircraft |
| QUJ | True bearing **to** station |

- QDM and QDR are reciprocal magnetic directions: QDM = QDR ±180°.
- QTE is QDR converted from magnetic to true using local variation; QUJ is reciprocal of QTE.
- For the bank convention: true = magnetic + VAR (east positive); therefore QTE = QDR + VAR. Example QDR022°, VAR10°E → QTE032°; QUJ is reverse of the true bearing from station.
- QTE229°, VAR10°W: magnetic from-station QDR = 229° + 10° = 239°; reciprocal QDM = 059°.
- QTE248°, VAR10°W → QDR258°. QTE203°, VAR10°E → QDR193°. QDR067°, VAR5°E → QDM247°.
- QDM138°, VAR10°E: true-to-station QUJ = QDM + VAR = **148°**. QDR152°, VAR5°W: true from-station QTE147°; reciprocal QUJ327°.
- Do not apply deviation to a Q-code unless the problem explicitly gives aircraft compass deviation; Q codes are station-referenced magnetic/true bearings.

### ADF/NDB relative bearing

- An NDB is non-directional; the aircraft ADF detects direction. RBI shows **relative bearing** (RB), clockwise from aircraft nose to beacon.
- **QDM ≈ MH + RB**, normalized to 000°–359°. Example MH 095° plus RBI 355° = QDM 090°.
- To go to beacon in calm wind, fly QDM. In wind, maintain desired track using drift corrections.
- If the needle moves toward the nose (RB decreases toward 000°), relative geometry is changing; compare successive readings rather than assuming a single reading is course.
- In a tracking question, hold desired QDM and observe RBI trend. If RBI drifts away from the desired relative bearing, crosswind drift is increasing; correct heading in the direction required to restore the desired bearing/track. The bank's Q78: RBI changes 355°→358° while approaching on QDM090°; keyed interpretation is crosswind increasing, increase MH.
- RBI/ADF figure NAV-019: first identify fixed lubber line/aircraft heading and needle head (to beacon). Add RB to MH for QDM; tail gives reciprocal direction/from bearing. In Q77 the keyed calm-wind QDM is 260°. Avoid reading the opposite end of the needle.

## 8. Maps, charts, projections and visual navigation

### Map projections

- **Mercator:** conformal; scale increases with latitude; meridians and parallels are straight; rhumb lines are straight; great circles are generally curved. High latitudes are enlarged. It is useful for constant-course plotting, not equal-area measurement.
- **Lambert conformal conic:** conformal and nearly true to scale over its standard-parallel region; great circles are approximately straight over a limited area. It is not equal-area. Often suited to mid-latitude aeronautical charts.
- Projection distortion matters: a line's appearance and scale depend on the projection. Do not assume every straight chart line is a great circle.

### Chart-reading checklist

1. Confirm chart title, edition/date, units, scale, projection and variation annotation.
2. Locate position from latitude/longitude graticule; read magnetic variation and its date/annual change where provided.
3. Read airspace by its lateral boundary, vertical limits (floor/ceiling), class, operating hours and activity/frequency. Verify legend; do not infer vertical limits from colour alone.
4. Identify aerodromes by name/ICAO designator, runway, elevation, frequencies and symbol. Read navaid ident/frequency and symbol; distinguish VOR, VOR/DME, NDB, DME and reporting points.
5. Check terrain/obstacle elevations and heights, restricted/prohibited/danger areas, controlled airspace, corridors, reporting points and scale bars.
6. Measure route distance along intended track using the chart scale or latitude scale (on suitable charts 1′ latitude ≈ 1 NM); don't measure an arbitrary curved route with a straight ruler.
7. For actual flight use current chart, NOTAMs and official legend. The bank may show simplified or partial chart extracts.

- Prefer stable conspicuous features for visual navigation: rivers, railways and major highways. Avoid easily confused minor farm tracks/streams and power lines; borders may be hard to identify.
- **Terrestrial navigation** means orientation by ground features in visual flight, not celestial, instruments or GPS.
- For a chart-position figure: read the coordinate first, then identify the matching aerodrome/town; don't identify a place solely from visual proximity.

## 9. Radio navigation and surveillance

### Radio wave basics

- Electromagnetic waves travel approximately **300,000 km/s**. As source/receiver move apart, received frequency decreases; moving together, perceived frequency increases (Doppler effect).
- Oscillation phase describes the progress of a cycle; amplitude is signal strength; frequency is cycles per second.
- LF/MF (e.g. NDB) can propagate as ground/surface wave and sky wave. VHF (e.g. VOR/VDF) is direct, quasi-optical line-of-sight propagation through air.
- Horizon/range of VHF aids and VDF depends principally on transmitter and receiver altitude; terrain/obstruction and equipment also matter. Higher aircraft altitude generally increases range.
- LF/MF NDB night sky-wave effects cause fading/interference and can increase apparent range; strongest night effects are exam traps. Shoreline refraction is greatest at an acute angle to the coast and at low altitude (bank: below 6,000 ft).

### NDB / ADF

- NDB transmits LF/MF; aircraft requires an **ADF** receiver/indicator. Locator beacons are lower-power/shorter-range than full NDBs.
- NDB signal can be affected by night effect, thunderstorms, terrain, coastal refraction and precipitation/static; verify position with other sources.
- An NDB aerial is often a small loop/sense or combined antenna under/within the fuselage; recognize the pictured NDB aerial by its characteristic loop/fairing and compare alternatives (VOR/DME aerials are not this indicator).

### VOR

- VOR determines bearing by comparing the **phase** of reference and variable signals. VOR radials are magnetic bearings **from** the station (QDR).
- CDI/OBS method: set selected course on OBS; observe **TO/FROM** flag and needle. A centred CDI with TO indicates the selected course leads to station; centred with FROM indicates aircraft is on the selected radial outbound. A CDI left/right means course line is displaced from aircraft; fly toward needle to intercept (correct sense depends on TO/FROM and selected course).
- Full CDI deflection in the bank corresponds to at least **10°** off selected course (angular, not 10 NM). Actual sensitivity may vary with equipment/phase of flight.
- Figure NAV-022: read OBS course, CDI, and TO/FROM flag together; first infer selected radial/course and whether it is TO or FROM, then place aircraft in the corresponding quadrant. Bank answer is **northeast** of the VOR.
- Figure NAV-024: read the OBS/radial scale at the selected course indication; the bank identifies radial **234°**. A reciprocal course may look plausible—distinguish the radial FROM the VOR from a course TO it.
- VOR range is line-of-sight; transmitter/receiver altitude controls range. Radial questions from coordinates: compute/plot the station-to-point direction; the bank's BKD→Pritzwalk radial is 068°.
- Cross-bearing: extend each station radial outward; intersection gives position. Bank cross-bearing fix from HAM radial119° and BKD radial320° is 53°20′N, 11°10′E.

### DME

- DME measures elapsed time between aircraft interrogation and station reply (with system turnaround delay accounted for); converts it to **slant range**.
- Displayed distance is slant range, not horizontal ground distance. Difference is greatest near/overhead the station and at high altitude; it becomes negligible when far away compared with height. Approaching directly overhead increases the relative discrepancy.
- DME distance is not a ground-track distance if the aircraft is offset from the station.

### VDF

- Ground VHF direction finder uses a bearing measured from the aircraft's VHF transmission; aircraft needs a **VHF radio**, not a special onboard VDF receiver or two aerials.
- VDF can report magnetic bearings (QDM/QDR depending on request). A QDR of 135° puts aircraft southeast of the station; 225° southwest; 315° northwest.
- Range depends on aircraft altitude/line of sight.

### Radar and transponder

- Primary radar transmits pulses and detects reflections from aircraft; range from elapsed time, bearing from antenna orientation. It does not need an aircraft transponder.
- Secondary surveillance radar interrogates a **transponder**, which replies with coded identity/altitude; SSR replies are not simply reflections from the skin.
- Mode C transmits **pressure altitude** (referenced to standard pressure), not QNH/QFE altitude.
- Codes: **7500 unlawful interference**, **7600 radio communication failure**, **7700 general emergency**. 7000 is a common VFR conspicuity code where locally applicable.
- Radar instantaneously obtains range and direction/azimuth from the antenna; it cannot directly infer TAS/heading from a primary return alone.

### GNSS / GPS

- GNSS position is calculated from satellite signals; at least **four satellites** are needed for a precise, verified 3D position including receiver clock error.
- GPS CDI/track-deviation bar indicates **lateral distance** from desired course in NM, not necessarily degrees. Full-scale sensitivity depends on operating mode/phase; verify annunciation.
- GPS groundspeed/track are not the same as TAS/heading. Cross-check route, mode, database and chart; a GPS indication does not replace airspace awareness.

## 10. Compass errors and instruments

- Direct-reading magnetic compass aligns with Earth's magnetic field plus aircraft deviation. Electrical/electronic equipment can create deviation; use the compass deviation card and switch off/interference check where appropriate.
- Gyroscopic/turning instruments are not the direct-reading compass. In the pre-start checklist figure NAV-004, “Gyro” and “Turning Instruments” are the items related to checking those instruments; the direct-reading compass is not itself a gyro.
- **UNOS** (Northern Hemisphere): when turning onto north, compass lags → undershoot north; turning onto south, it leads → overshoot south. Roll out early for north, late for south.
- **ANDS** (Northern Hemisphere, east/west headings): accelerate → apparent compass turn toward north; decelerate → apparent turn toward south.
- These are magnetic-compass errors, most apparent at low speed/high latitude; do not apply them to gyro heading indicators.

## 11. Holding and procedure recognition

- Identify the holding fix, inbound track, direction of turns, leg timing/distance and wind correction from the depicted pattern. Standard holding uses right turns unless published otherwise; non-standard uses left turns.
- In a wind-corrected hold, compensate drift on both outbound and inbound legs to maintain the published tracks; inbound timing is normally the reference and outbound time is adjusted for wind as taught/published.
- For an entry question, compare aircraft arrival direction to the inbound course and choose the sector/entry shown by the applicable rule (direct, parallel or offset/teardrop); first identify the inbound track and turn direction, then the entry sector. Do not confuse inbound course with outbound reciprocal.
- Holding is not directly tested by a specific standalone item in this 131-question bank; use this as a recognition framework and follow the course's exact entry convention if a diagram is supplied.

## 12. Radius of turn and turn geometry

- Coordinated level turn load factor: $n=1/\cos\phi$, where φ is bank angle. Higher bank increases load factor and decreases turn radius; this relation also appears in general flying knowledge.
- Turn radius: $r=V^2/(g\tan\phi)$ with speed in consistent linear units and g=9.81 m/s². Use TAS/GS as appropriate to the stated geometry; a simple exam rule may instead supply a standard-rate-turn approximation.
- Example: V=50 m/s, bank=30°: r=50²/(9.81 tan30°) ≈ 441 m ≈ 0.24 NM. Always convert speed units before using SI formula.
- For a standard-rate turn (3°/s), angular speed = 3π/180 rad/s; $r=V/\omega$, with V in NM/s (GS kt ÷ 3600). A bank-angle formula and standard-rate formula are different assumptions.

## 13. Position, ETA, PET/ETP and flight-planning use

- Leg time = distance/GS. Add leg times sequentially to UTC ETD for ETA; include planned climb/descent or delays only if supplied.
- If headwind/tailwind given instead of GS, find GS before ETA. E.g. 75 NM, TAS105, headwind12 → GS93 kt; time≈48.4 min; ETD1242 → ETA≈1330 UTC.
- **PET (Point of Equal Time)** / **ETP (Equal Time Point):** point along a route at which time to return to departure equals time to continue to destination (or to the stated alternatives). With constant speeds and wind, calculate each direction's groundspeed separately.
- For a single route A–B with distance D, outbound GS from A toward B = V_A; return GS from point toward A = V_R; continue GS toward B = V_B. At distance x from A:
  $$
  x/V_R=(D-x)/V_B\quad\Rightarrow\quad x=D\,V_R/(V_R+V_B)
  $$
  where VR is speed from the point back toward A, and VB speed toward B. If equal groundspeeds, PET is halfway. Check the question's stated meaning and wind direction.
- **ETP** can also mean equal-time point between two diversion/landing options; solve time-to-left = time-to-right using each route's distance and groundspeed. Avoid assuming the geometric midpoint when winds/speeds differ.
- Flight plan table: complete in sequence TC → WCA → TH → VAR → MH → DEV → CH/MC according to the column labels. Example NAV-014 final row: TC179°, WCA+6° ⇒ TH185°; VAR1°E gives MH184°; MC178° is course corrected by variation, consistent with the given table's direction fields. Always confirm what each column explicitly means.
- Bank revised ETA and direction conversion questions often use deliberately plausible alternatives; recalculate from the formula rather than pattern-matching.

## 14. Common exam traps and recall table

| Trap | Correct check |
|---|---|
| Confusing course and heading | Course/track is over ground; heading points nose through air. Wind causes WCA. |
| Using TAS for ETA | ETA uses GS. |
| Wind “from” vs “toward” | Wind is named from its source; draw vector toward the opposite direction. |
| Reciprocal ambiguity | Reverse direction by 180°; say explicitly “to” or “from”. |
| Variation vs deviation | Variation is geographic true↔magnetic; deviation is aircraft magnetic↔compass. |
| East/west conversions | Apply one conversion step at a time; use the bank's convention table and normalize. |
| Variation signs | Bank answers use traditional east-is-least/west-is-best. Its prose may call DEV signs +/-; interpret through MH↔CH, not sign alone. |
| Degrees/minutes | 60′=1°; 1′ latitude≈1 NM. Decimal degrees are not decimal minutes. |
| Longitude distance | 60 NM/degree only at equator; multiply by cos(latitude) elsewhere. |
| Latitude across equator | Add absolute latitudes. |
| Time zones vs longitude | CET/CEST offsets are civil time; longitude gives solar-time difference. |
| Chart scale | Convert real distance to chart units before dividing. |
| Mercator vs Lambert | Mercator: rhumb straight, GC curved, scale grows with latitude. Lambert conformal, nearly true scale locally; not equal-area. |
| CDI / VOR | Identify OBS and TO/FROM before interpreting needle or radial. |
| DME | Slant range, especially significant close overhead. |
| Radar | Primary = reflected; secondary = transponder reply. Bearing comes from antenna orientation. |
| ADF RBI | QDM = MH + RB; needle head points to beacon. |
| GPS deviation bar | Lateral distance in NM; full-scale changes by mode. |
| Sunrise | East is earlier in UTC, about 4 min per longitude degree at same latitude. |
| 1:60 | Course correction to destination = track error + closing angle. |
| Rounding | Carry exact values through; round only at the end and respect the provided answer precision. |

### Bank coverage checklist (all question themes)

- Q1–12: Earth shape/axis, great circles/rhumb lines, latitude/longitude distance, polar circles.
- Q13–18, Q94: longitude/time, UTC/CET/CEST, civil twilight, sunrise/sunset.
- Q19–23, Q58–60, Q95–99: direction references, variation/deviation, agonic/isogonic lines, compass, inclination.
- Q24–27, Q35–38, Q44–47, Q66, Q106–110: units, TAS, chart scale, TDS, ETA, descent time, altitude/coordinate/chart reading.
- Q28, Q36–37: Mercator/Lambert and line depiction.
- Q29–34, Q117–119: Q-codes and bearing conversions.
- Q39–45, Q49–56, Q62–66, Q107, Q111–113: GS, time, ETA, wind triangle, WCA/heading, 1:60.
- Q48 and Q61: chart position and visual ground navigation.
- Q67–71, Q115, Q124: electromagnetic waves, Doppler, propagation and phase.
- Q72–80, Q114, Q116, Q120–123: VDF, NDB/ADF, RBI, antenna, range, night effect and shoreline effect.
- Q81–89: VOR, CDI/radial interpretation, range and DME slant range.
- Q90–91, Q125–129: primary/secondary radar, transponder and codes/mode C.
- Q92–93, Q103–105: coordinate differences, chart radial/cross-bearing and distance.
- Q100–102: compass-related checklist, interference, true-bearing position fixing.
- Q130–131: GNSS satellite count and GPS CDI interpretation.

**Bank figure cautions:** NAV-014 is a flight-planning table; NAV-017 an NDB aerial; NAV-019 an RBI/ADF display; NAV-022 and NAV-024 VOR CDI/OBS displays; NAV-004 checklist; EC-90-001 chart. NAV-031 is absent in this repository; questions 103–105 and 109–110 can still be solved from the supplied coordinates, using plotting/coordinate methods above. For VOR displays, read course, TO/FROM, needle and reciprocal separately.
