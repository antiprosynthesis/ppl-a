# Navigation — lesson notes

> **Source limitation:** The repository contains the complete 131-question bank, existing study notes and chart figures, but not the referenced `Vak1__` lesson extracts. The lesson directory was empty. These notes are therefore organised as a seven-lesson study sequence inferred from the bank and the lesson topics named in the request; they are not a verbatim account of the teacher's lesson handouts. Check the course's exact rules of thumb and examples against the original class materials.

## Lesson 1 — Earth, coordinates, distance and time

### Core ideas

- Navigation uses a geographic reference frame: geographic poles define the rotational axis; the Earth is approximated by an ellipsoid. Magnetic poles are separate and do not define geographic coordinates.
- Latitude measures north/south from the equator; longitude measures east/west from Greenwich. Use N/S and E/W carefully when reading charts and GPS values.
- A degree of latitude is 60 NM (one minute is one NM). A degree of longitude contracts with latitude: approximately 60 cos(latitude) NM.
- Great circles are shortest routes on a sphere; rhumb lines cross meridians at constant angles. A rhumb line is easier to fly on a constant compass direction, but often longer.
- The equator and meridians are great circles. Other parallels are small circles. One degree longitude on the equator is 60 NM, not 60 NM at every latitude.

### Procedure: coordinates and distance

1. Convert decimal degrees by multiplying the decimal part by 60; convert decimal minutes to seconds by multiplying by 60 again.
2. Calculate latitude difference in minutes. If points straddle the equator, add absolute values.
3. For longitude distance use longitude difference in minutes times cos(mean latitude); for short distances, combine components as a right triangle.
4. On an aeronautical chart, read latitude from parallels and longitude from meridians, interpolate, and then identify the feature at the fix.

**Worked examples**

- Travel 240 NM north: add 240′=4° to latitude. 47°50′27″N becomes 51°50′27″N.
- Latitude difference between 12°53′30″N and 07°34′30″S: 12°53′30″ + 7°34′30″ = 20°28′00″.
- At 50°N, 10° longitude is less than 600 NM: 10×60×cos50° ≈386 NM.
- At 51.83°N, 12.19°E, coordinates are approximately 51°49.8′N, 12°11.4′E. On the supplied chart this fixes overhead EDAD.

### Time and the Sun

- Earth rotates 15° per hour: 1° longitude = 4 minutes; 10° = 40 minutes, 20° = 80 minutes.
- The Sun appears earlier in the east. Sunrise and sunset in UTC are earlier at the eastern longitude if latitude/date are equal.
- Aviation uses UTC. CET=UTC+1, CEST=UTC+2. Convert local time to UTC by subtracting the stated offset.
- Civil twilight is when the Sun's centre is at or within 6° below the true horizon. Do not confuse with nautical twilight (12°).

**Worked time example:** Vienna is about 3°34′ east of Salzburg: difference ≈3.57×4=14.3 minutes. Vienna's sunrise and sunset occur about 14 minutes earlier in UTC.

### Teacher-style reminders inferred from bank

- Never assume “longitude degree” means 60 NM; that holds at the equator only.
- Look for the hemispheres before subtracting coordinates.
- Time of day can roll over the date line; UTC is the common anchor.
- The bank's “polar circles” expression is 23.5° from the poles (about 66.5° latitude).

### Beyond question bank

- A full great-circle route and a rhumb-line route require projection/route calculations beyond the simple bank questions.
- Sunrise/sunset varies with date, latitude and atmospheric refraction; use an almanac/table for exact operational times.

## Lesson 2 — Charts, projections, units and chart scale

### Chart projections

- Mercator is conformal, has straight meridians/parallels, straight rhumb lines, curved great circles, and scale that increases with latitude.
- Lambert conformal conic is conformal and nearly true to scale over its intended region. It is not equal-area; great circles are approximately straight over a limited area.
- A straight line on a chart is not necessarily a great circle: identify the projection first.

### Chart interpretation routine

1. Read chart name, date, projection, scale, units and variation annotation.
2. Plot/check coordinates using graticule marks.
3. Read aerodrome, navaid and airspace symbols using the chart legend.
4. Check lateral boundaries and vertical limits; distinguish terrain elevation from obstacle height.
5. Measure route distance in consistent units and calculate direction with true north as reference before converting magnetic.
6. Verify chart currency, NOTAMs, frequencies and activity times for real flight.

### Scale calculations

- For 1:n, real distance = chart distance × n. To solve for n, convert real and chart distances to matching units, then divide.
- Example 220 NM = 407.44 km; measured length 40.7 cm (0.407 km): ratio ≈407.44/0.000407=1,001,000 → 1:1,000,000.
- Example 60.745 NM =112.5 km. If chart length is 7.5 cm, 112.5 km =11,250,000 cm; denominator =11,250,000/7.5 =1,500,000.

### Conversions to memorise

- 1 NM =1.852 km=1,852 m≈6,076 ft; 1 SM≈0.869 NM.
- 1 km≈0.540 NM; 1,000 ft≈300 m; 1 m≈3.28 ft.
- 1 US gallon=3.785 L; 1 Imperial gallon=4.546 L. Be exact about the type.
- 1 kg≈2.205 lb; fuel mass requires volume×density specified by the question.

### Teacher tips inferred from figure questions

- The bank's chart (EC-90-001) is dense: start from coordinate grid and identify features, not by guessing from map appearance.
- NAV-014 is a column-by-column flight planning exercise. Write intermediate TC/WCA/TH/VAR/MH/MC beside the table before filling blanks.
- NAV-031 is referenced for several questions but is absent from the repository. The stated coordinates still allow distance/course calculations.

### Beyond question bank

- Read the chart's legend and current issue before interpreting unfamiliar ICAO symbology. The question bank alone cannot teach every chart mark or active airspace procedure.

## Lesson 3 — Airspeed, wind triangle, heading and 1:60

### Speeds and wind

- IAS is instrument indication; CAS corrects instrument/position errors; TAS is speed through the air; GS is speed over ground.
- TAS rises with altitude as air density falls. The bank's shortcut is about 2% IAS per 1,000 ft: 150 kt IAS at 8,000 ft ≈174 kt TAS.
- Wind direction is reported **from**. Convert to the direction it blows **toward** when drawing the vector.
- Headwind lowers GS; tailwind raises GS. Crosswind creates drift; steer into the wind to maintain desired track.

### Wind triangle step sequence

1. Draw the desired TC/course.
2. Draw wind from the stated direction, with the vector pointing 180° opposite.
3. Resolve wind into along-track and cross-track components, or use an E6B.
4. Determine WCA (signed toward the wind); add it to TC to get TH.
5. Calculate GS from the along-track result; use GS for time and ETA.

Approximate components: headwind = wind speed × cos(relative angle); crosswind = wind speed × sin(relative angle). WCA magnitude ≈ arcsin(crosswind/TAS).

**Worked example:** TC040°, TAS180, wind350°/30. Wind is from left-forward; crosswind ≈23 kt and headwind≈19 kt. Correct about 7° left; TH≈033°, GS≈159 kt.

**Direct wind example:** TC270°, TAS100, wind090°/25 (blowing toward270) is a direct tailwind. GS125 kt. For 100 NM, time=60×100/125=48 min.

### 1:60 correction

- 1° error after 60 NM gives about 1 NM cross-track error.
- Track error =60×cross-track error/distance flown.
- To rejoin route and reach destination, add a closing angle: 60×cross-track error/distance remaining.

**Worked example:** 7 NM right after 55 NM flown on a 120 NM leg: drift angle ≈7.6° right; remaining 65 NM gives closing angle ≈6.5°. Turn ≈14° left to intercept destination.

### ETA, revised ETA and descent time

- Time (min)=60×distance/GS; ETA=ETD+leg time.
- If given TAS and headwind, subtract headwind before calculating time.
- Revised ETA uses actual progress/GS and remaining distance; do not just apply a schedule offset.
- Descent time=altitude difference/rate of descent.
- Temperature correction: ISA≈15°C−2°C/1,000 ft; true altitude correction≈4 ft/1,000 ft/°C difference from ISA. Add for warmer-than-ISA air; subtract for colder-than-ISA air. For the bank examples, QNH altitude 6,500 ft at +21°C gives about 7,000 ft true altitude, while FL75 at −9°C gives about 6,250 ft.

**Examples**

- 110 NM in 85 min: GS≈78 kt.
- 75 NM at TAS105 with 12 kt headwind: GS93 kt; time≈48 min; ETD1242 → ETA1330 UTC.
- 7,500 ft descent at 1,200 ft/min takes about 6.25 min.
- At a checkpoint 70 NM into a 220 NM route, if actual elapsed time is 30 minutes, actual GS=140 kt; remaining 150 NM takes 64 minutes. Departure 1200 gives revised ETA about 1335.

### Flight-planning tables

- Keep each course/heading field distinct. A typical flow is TC → WCA → TH → VAR → MH; deviation changes magnetic heading to compass heading.
- Variation conversions follow east-is-least/west-is-best (true to magnetic: subtract east, add west). Check the stated direction before applying.
- The bank's NAV-014 final row has TC179, WCA+6, TH185; use the table's column labels and options because it mixes magnetic course and magnetic heading.

### Beyond question bank

- Wind triangles with large crosswind need a graphical/analytical vector solution rather than the arcsine approximation.
- Real flight planning also accounts for temperature, pressure altitude, aircraft performance, fuel reserves, route restrictions and forecast winds at each level.

## Lesson 4 — Magnetic compass, variation, deviation and bearings

### North references

- True north points to the geographic North Pole; magnetic north follows Earth's magnetic field; compass north is what the aircraft's direct-reading compass indicates.
- Variation: true/magnetic difference, location-dependent and shown on charts. Agonic line = zero variation; isogonic line = equal variation.
- Deviation: compass error caused by aircraft magnetism/electrical equipment; read the compass card. Electronic devices may disturb the direct-reading compass.
- Inclination is smallest at the magnetic equator and largest near magnetic poles.

### Conversion chain

- Course/heading wind relation: TH=TC+WCA.
- True↔magnetic: true-to-magnetic subtract east/add west; reverse magnetic-to-true add east/subtract west.
- Magnetic↔compass: apply aircraft deviation card; traditional mnemonic: compass-to-magnetic add east/subtract west; magnetic-to-compass subtract east/add west.
- Normalize each answer to 000°–359°.

**Examples**

- TC245°, VAR7°W → MC252°.
- TC179°, WCA−12° → TH167°. VAR4°E → MC175°, MH163°.
- NAV-014 final row: TC179°, WCA+6° → TH185°. Use the printed variation and labels to obtain the remaining field.

> **Signed convention:** use East positive/West negative. In Q95–97, MH198° and CH200° imply DEV = −2° (2°W). The keyed answers are consistent when each E/W conversion is applied explicitly.

### Q codes and reciprocity

- QDM = magnetic bearing to station. QDR = magnetic bearing from station. QTE = true bearing from station. QUJ = true bearing to station.
- Reverse any bearing by 180°. Convert magnetic to true with variation before reversing if the requested result is true.

Examples: QTE229°, VAR10°W → QDR239°, reciprocal QDM059°. QDR022°, VAR10°E → QTE032°. QDM138°, VAR10°E → QUJ148°.

### Compass errors

- UNOS: undershoot north, overshoot south in Northern Hemisphere. Compass lags when turning to north and leads when turning to south.
- ANDS: on east/west headings, acceleration appears to turn compass north; deceleration appears to turn it south.
- These are direct-reading compass effects, not gyro indications. NAV-004 lists gyro/turning-instrument checks, which are distinct from compass operation.

### Beyond question bank

- Magnetic variation changes with location and epoch. Use current chart/model data in real route planning, rather than memorized local values.

## Lesson 5 — Radio aids: NDB/ADF, VOR, DME and VDF

### Wave propagation

- Electromagnetic waves travel about 300,000 km/s. Moving transmitter/receiver apart lowers perceived frequency; moving together raises it (Doppler).
- LF/MF NDB signals can use ground wave and sky wave; night-time sky-wave interference causes fading/night effect.
- VHF signals (VOR/VDF) are quasi-optical/direct and generally line-of-sight. Greater transmitter/aircraft altitude improves range.

### NDB / ADF

- NDB is a non-directional LF/MF beacon; ADF is the aircraft receiver. Locator beacon range is lower than a full NDB.
- RBI indicates relative bearing from aircraft nose to station. QDM=MH+RB (modulo 360). Example MH095 + RB355 = QDM090.
- For direct-to-beacon in calm wind, steer QDM. In wind, track the desired inbound course and correct drift.
- Night effect and shoreline refraction cause bearing errors. Shoreline effect is strongest at acute coastal crossing angle and low altitude.
- NAV-017's under-fuselage loop/fairing is the NDB aerial. NAV-019 shows RBI/ADF indications; read needle head as direction to beacon and combine with aircraft heading. Q77’s keyed calm-wind QDM is 260°.

### VOR

- VOR compares phase of reference/variable signals; radial is magnetic bearing from station (QDR).
- On a VOR display: set OBS, read selected course, CDI and TO/FROM. TO means selected course leads to the station; FROM means aircraft is on an outbound radial if centred.
- A full CDI deflection is angular; in the bank at least 10°. Do not interpret as a distance in NM.
- For cross-bearing, plot radials from both stations and find their intersection. Reverse a radial when the requested line is a course to the station.
- NAV-022/NAV-024 are CDI/OBS figure-reading questions. Read OBS and flag first, then needle and quadrant. Q85 keyed radial is 234° (not reciprocal 054°/060°).

### DME and VDF

- DME times interrogation/reply and displays slant range. Difference from horizontal distance is most significant near overhead and at altitude.
- VDF is a ground station that finds bearing from a pilot's VHF radio transmission. Aircraft needs a VHF radio. QDR135 places aircraft southeast of station; QDR225 southwest; QDR315 northwest.

### Teacher tips inferred from bank

- Use a compass rose and mark station-to-aircraft vs aircraft-to-station. Many wrong answers are just reciprocals.
- VOR range questions are about line-of-sight altitude, not daytime sky waves.
- NDB night questions test LF/MF propagation effects, not time-of-day receiver settings.

### Beyond question bank

- ADF signal errors also arise from thunderstorms, terrain, precipitation/static and aircraft attitude; never rely on a single bearing for safe navigation.
- VOR service volume, equipment flags and CDI sensitivity vary by facility/equipment; use current documentation.

## Lesson 6 — Radar, transponder, GNSS, charted fixes and holding

### Radar and SSR

- Primary radar sends a pulse and receives reflection from the aircraft. Time gives range; antenna orientation gives bearing.
- SSR interrogates an aircraft transponder; transponder reply supplies identification and, in Mode C, pressure altitude.
- Codes: 7500 hijacking/unlawful interference, 7600 radio failure, 7700 emergency.

### GNSS

- Four satellites provide a precise, verified 3D position, including receiver clock correction.
- GPS lateral deviation bar represents distance in NM from desired course; full-scale sensitivity depends on operating mode. It is not inherently an angular error.
- Distinguish GPS track/groundspeed from aircraft heading/TAS.

### Charted radio fixes

- To calculate course/distance from coordinates, use latitude-minute and longitude cosine approximations, or plot on chart.
- BKD (53°02′N, 11°33′E) to Pritzwalk (53°11′N, 12°11′E): roughly 9′ north and 38′ east at 53°N; east component ≈22.9 NM, north 9 NM; distance≈25 NM (bank: 24 NM) and radial approximately 068°.
- Fix from HAM radial119° and BKD radial320°: draw each radial outward from the named station; their intersection matches 53°20′N, 11°10′E in the bank.
- Uelzen→Neustadt coordinates give TC≈061°; reverse route is reciprocal. Distance is about 46 NM.

### Holding recognition

- Find fix, inbound course, turn direction and leg timing. Standard pattern normally uses right turns unless published otherwise.
- For entry diagrams, establish inbound course and arrival direction, then identify direct/parallel/teardrop sector under the course rule. Keep inbound vs outbound reciprocal straight.
- Wind correction maintains the published inbound and outbound tracks; adjust outbound leg timing as appropriate.

> Holding is not independently represented by a dedicated question in this bank; use the class's prescribed entry method where a holding diagram is tested.

### Beyond question bank

- GNSS integrity/augmentation, RAIM, database currency, alternate navigation and approach minima are not covered by these bank questions.
- Holding entries, leg lengths and timing depend on published procedure and current rules; this section is only a recognition reminder.

## Lesson 7 — Integrated calculations, PET/ETP, fuel and exam practice

### Integrate a route leg

1. Read route distance, TC and any wind/airspeed data.
2. Calculate TAS if necessary; resolve wind; calculate WCA, TH and GS.
3. Convert TC/TH between true and magnetic using VAR; convert MH to CH using aircraft DEV if requested.
4. Calculate time from distance/GS; add to UTC departure for ETA.
5. If off track, apply 1:60 track error and closing angle; if position/time updated, recompute revised ETA from remaining distance and actual GS.
6. Record fuel used/range only after using correct flow, time, units and density.

### PET/ETP

- Point of equal time is where time to turn back equals time to continue (or where time to two alternate destinations is equal).
- For distance D and constant ground speeds: if speed back to A is VR and speed forward to B is VB, distance from A to PET is x = D×VR/(VR+VB). Equal speeds put PET halfway.
- With wind, calculate each direction's GS independently; do not use TAS for both.
- For equal-time point between alternate airports, equate distance/speed for each option and solve the distance from the aircraft.

### Fuel examples and checks

- Fuel used = flow × hours. Endurance = usable fuel/flow. Range = endurance×GS.
- 25 L/h for 1.5 h uses 37.5 L. At 60 L usable, endurance is 2.4 h before reserves.
- Convert US/Imperial gallons separately. Convert volume to mass only using the density supplied or explicitly permitted.
- Treat final reserve, contingency, unusable fuel and taxi fuel according to question wording; don't make up a reserve convention.

### Radius of turn

- Coordinated-turn load factor n=1/cos(bank). Radius r=V²/(g tan bank), with consistent units.
- Example: 50 m/s, bank30° gives r≈441 m≈0.24 NM. If using a standard-rate turn, use its angular rate (3°/s) and GS; do not mix the two assumptions.

### High-value exam checks

- Write labels next to every angle: TC, TH, MC, MH, CH, QDM etc.
- Mark wind as “from” and use opposite vector direction.
- Find GS before time; find actual GS before revised ETA.
- Use remaining distance—not whole route—for closing-angle/revised-ETA steps.
- For CDI and chart figures, inspect every label and flag before deciding quadrant.
- Keep unrounded intermediate values and check if answer should be a reciprocal, a true/magnetic conversion, or a unit conversion.

### Beyond question bank

- The bank does not explicitly test holding calculations, fuel-load density arithmetic, turn-radius calculations, or a standalone PET/ETP problem. These are included because the requested course notes/cheat sheet named them; follow teacher's worked examples and any prescribed exam formulas.

## Bank coverage and unresolved source material

- The cheat sheet's final coverage checklist maps every question number 1–131 to a topic; all bank questions can be answered from the bank text, coordinate data and available figures.
- Questions 103–105 and 109–110 refer to NAV-031, which is not present in the repository. They are still solvable from coordinate data printed in the bank.
- The user's requested original lessons, exercises, VUISTREGELS, worked NAV book answers, Q-code sheets and tests were not in the repository. The notes above cannot claim to include teacher-specific extras or validate any conflict against those missing materials. The one explicit convention issue observed in the bank (direction/sign wording for variation/deviation) is flagged in the cheat sheet and here; for this bank, trust the keyed answers and apply each E/W conversion step explicitly.
