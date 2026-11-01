# Meteorology — Full Exam Cheat Sheet (PPL(A), EASA/ECQB)

Use this as an exam reference, not as a substitute for a current briefing. Values marked **approx.** are approximations; for actual flight decisions use official, current products and aircraft limitations. Lesson/test feedback is incorporated. Where the bank key is peculiar, the bank's expected answer is identified.

## 1. Atmosphere, ISA and temperature

### Composition and layers

| Item | Memorise | Exam use |
|---|---|---|
| Dry air | about 78% nitrogen, 21% oxygen, 1% other gases | Water vapour is variable (about 0.1–4%); it is not the 78% component. |
| Weather layer | Troposphere | Almost all ordinary weather/hydrometeors occur here. |
| Tropopause | Boundary/transition between troposphere and stratosphere | Not the stratosphere itself; temperature becomes nearly constant at the ISA tropopause. |
| ISA tropopause | 11 km = 36,000 ft; about −56.5°C | Mid-latitude ISA reference; real tropopause varies with latitude/weather. |
| Approx. real tropopause | Poles: 6–8 km, about −40°C; mid-latitudes: 11 km, −56.5°C; equator: 15–18 km, about −75°C | Do not assume the real tropopause is always 36,000 ft. |
| Stratosphere | Temperature generally increases with height above the tropopause (ozone absorption) | A temperature inversion aloft is not unusual. |

### ISA reference values

| At/within | ISA value |
|---|---|
| Mean sea level (MSL) | 1013.25 hPa; +15°C; density 1.225 kg/m³; gravity 9.80665 m/s² |
| Troposphere (surface to 11 km) | Temperature decreases about 6.5°C/km = 1.98°C/1000 ft (exam shortcut: 2°C/1000 ft, or 0.65°C/100 m). |
| FL180 / about 5500 m | Pressure about 500 hPa (both Q9 and Q10). |
| ISA near 10 km | About −50°C (the question-bank answer; exact ISA value at 10 km is approximately −50°C). |

**Temperature vocabulary:** lapse rate = temperature change per height; inversion = temperature rises with height; isothermal layer = temperature is constant with height. A ground inversion commonly follows night-time radiation cooling; a subsidence inversion forms as air descends and warms in a high; a frontal inversion lies across a frontal surface; the tropopause is approximately isothermal.

### Temperature change in a moving air parcel

| Parcel state | Cooling on ascent | Equivalent | Use |
|---|---:|---:|---|
| Dry / unsaturated adiabatic (DALR) | 3°C/1000 ft | 1°C/100 m | Use while parcel is unsaturated. |
| Saturated adiabatic (SALR) | about 1.5°C/1000 ft | 0.6°C/100 m | Use after saturation; latent heat released makes cooling slower than dry rate. It varies with temperature/moisture. |
| ISA environmental rate | 2°C/1000 ft | 0.65°C/100 m | Environmental reference, not the parcel's DALR. |

**How to classify stability:** calculate the environmental lapse rate (ELR) = temperature drop between levels ÷ height difference. Compare rates as positive magnitudes:
- ELR < SALR → absolutely stable; ELR = SALR → saturated neutral; SALR < ELR < DALR → conditionally unstable; ELR = DALR → dry neutral; ELR > DALR → absolutely unstable.
- An inversion (ELR is negative because temperature increases upward) and an isothermal layer are stable.
- Example (lesson): +6°C at 2,000 ft and −10°C at 10,000 ft: drop 16°C over 8,000 ft = 2°C/1000 ft, between SALR 1.5 and DALR 3 → conditionally unstable. At +4°C/3,000 ft and −8°C/15,000 ft: drop 12°C/12,000 ft = 1°C/1000 ft < SALR → stable.

### Heat, density and density altitude

- Heat transfer: **radiation** (Sun's short-wave energy; Earth returns long-wave IR), **conduction** (contact, chiefly ground-to-air), **convection** (vertical parcel motion). **Advection** transports air/horizontal properties from place to place; turbulent mixing also transports heat.
- Condensation releases latent heat to the surrounding air/upper troposphere; evaporation absorbs heat. The Sun is the main energy source for weather.
- Gas law: `P V / T = constant` for a fixed mass of gas; `ρ = P/(R T)` (T in kelvin). At comparable conditions, pressure ↑ → density ↑; absolute temperature ↑ → density ↓. Humid air is slightly less dense than dry air at the same pressure and temperature.
- ISA sea-level air density = 1.225 kg/m³; a 1 m³ cube therefore has mass 1.225 kg.
- Density altitude rises when pressure is low, temperature is high, or humidity is high: performance (lift/engine/propeller) generally worsens.

**Density-altitude shortcut / HOW TO USE:** find pressure altitude (PA); compare actual OAT with ISA temperature at that altitude; add about 120 ft per °C warmer, subtract about 120 ft per °C colder. **Worked example:** PA 7000 ft, OAT 18°C. ISA at 7000 ft ≈ +1°C; difference +17°C. DA ≈ 7000 + (17×120) = **9040 ft**. Use aircraft performance data at about 9040 ft, not 7000 ft. This is a rule of thumb, not a replacement for the POH.

## 2. Pressure, altimeters and pressure charts

### Pressure and pressure-level basics

- Pressure is force per area and the weight of the air column above a unit area. 1 Pa = 1 N/m²; 1 bar = 100,000 Pa; 1 mbar = 1 hPa = 100 Pa. Standard sea-level pressure is 1013.25 hPa ≈ 760 mm Hg ≈ 29.92 in Hg.
- Pressure decreases with height. Near the surface, **1 hPa ≈ 27 ft** is the Notes/bank calculation shortcut; the Belgian lesson/test material also quotes **about 30 ft per hPa** (and 1 hPa per 8–12 m depending on level). Treat these as approximations; never confuse them with a precise hypsometric calculation.
- Isobars join equal pressure. Pressure tendency is the pressure change in the preceding 3 hours. Isallobars show pressure change; strongest falls help indicate a low's movement/development.

### Altimeter pressure settings (teacher's test feedback)

| Setting | What the altimeter reads / means | Memory cue |
|---|---|---|
| QNH | Pressure reduced to MSL using ISA; altimeter indicates altitude above MSL. On the airfield set QNH and check indication equals published field elevation. | QNH → altitude. |
| QFE | Airfield reference pressure; altimeter reads height above the airfield reference (zero at the reference point). Ground check should read 0 ft when set to QFE. | QFE → field/height. |
| QNE | Standard 1013.25 hPa setting; altimeter reads pressure altitude / flight levels (e.g. FL180). | QNE → standard / FL. |
| QFF | Station pressure reduced to MSL using actual meteorological conditions; used in meteorology, not the altimeter setting answer. | QFF → actual-weather reduction. |

**Exam traps:** the altimeter always measures pressure level relative to the selected datum, not intrinsically height above ground/MSL. QNH is ISA-reduced; QFF is actual-condition-reduced. Do not select QFE for an MSL altitude.

### Pressure/temperature altitude correction — HOW TO USE

1. Identify the setting/datum: a flight level is referenced to 1013.25 hPa.
2. Apply pressure correction using the supplied QNH and the question's stated approximation (often 27 or 30 ft per hPa).
3. Apply the cold/hot-temperature correction: colder-than-ISA air makes true altitude **lower** than indicated; warmer-than-ISA makes it **higher**. Use the exam's correction table/rule if supplied; nearest-50-ft rounding is common.
4. Check sign: **high to low, look out below**; cold air contracts pressure surfaces.

**Worked bank example:** FL85 (= 8500 ft on standard pressure), QNH 983 hPa, OAT ISA−10°C; asked true altitude nearest 50 ft. The keyed answer is **7300 ft**. The bank's expected calculation uses approximate pressure and cold-temperature corrections. The lesson/test uses 1 hPa ≈ 30 ft in some exercises whereas Notes uses ≈27 ft; exact result depends on the specified correction method/mean layer temperature. Use given exam tables and choose the keyed nearest option; do not treat this rough shortcut as a precision altimetry formula.

### Pressure systems, circulation and charts

- **Low/depression/cyclone:** pressure decreases toward centre; surface convergence and rising air → cloud/precipitation, often stronger wind; divergence aloft helps maintain ascent. Deepening = central pressure falls; filling = rises.
- **High/anticyclone:** pressure increases toward centre; broad descent (subsidence), compressional warming and drying → stable air/inversion. Winter: moisture trapped below inversion, mist/fog/low stratus. Summer: clear or few cumulus; large day/night temperature range possible.
- **Ridge/wedge:** elongated extension of high pressure. **Trough:** elongated extension of low pressure.
- Surface chart: actual sea-level pressure pattern, pressure centres, isobars and fronts. Wind chart: wind at a specified level. Upper-air/hypsometric chart: height/contours of a pressure surface (e.g. 850, 700, 500 hPa), not surface isobars. SWC: significant flight hazards. Prognostic chart: forecast, not observed surface analysis.
- Cold air aloft contracts the atmospheric column: pressure-surface heights fall and contours/height lines become closer; can form an upper trough/low and promote showers/CB. Warm air aloft expands the column and raises pressure-surface heights.

## 3. Global circulation, wind and local flows

### Pressure-gradient and wind rules

1. **Pressure-gradient force (PGF):** the force that initiates wind; directed from high toward low pressure, perpendicular to isobars. Tighter isobars = stronger gradient = stronger wind.
2. **Coriolis:** due to Earth's rotation; deflects moving air right in Northern Hemisphere (NH), left in Southern Hemisphere; proportional to speed, strongest at poles and zero at equator.
3. **Centrifugal force:** acts outward around curved flow.
4. Above friction layer with straight isobars, PGF and Coriolis balance → geostrophic wind flows parallel to isobars (roughly from 2000–3000 ft upward in lesson). Curved isobars add centrifugal force → gradient wind.
5. Surface friction slows wind, weakens Coriolis and makes wind cross isobars **toward low pressure**. Rough/mountainous/vegetated terrain slows it more than smooth ocean/flat terrain.

| Pattern | Northern Hemisphere circulation |
|---|---|
| Low | Counter-clockwise, inward at surface; rising air. |
| High | Clockwise, outward at surface; sinking air. |
| Buys-Ballot | Stand with back to wind: low is on the left, high on the right. |
| Veer / back | Veer = clockwise/rightward shift (e.g. 160°→180°). Back = anticlockwise/leftward shift (160°→140°). Surface friction tends to back/turn wind across isobars; wind generally veers with height in a frontal warm-air profile and backs with height in a cold-front profile. |

- Isobars far apart → weak gradient, light/variable winds, local breezes more important. Isobars close together → strong prevailing wind.
- **Convergence** = air flows together; at the surface it must rise → cloud formation (if moist). **Divergence** = air flows apart; surface divergence favours sinking/dissipation. Do not confuse these with advection (horizontal transport) or subsidence (descent).
- Global belts (idealised): equatorial low/ITCZ; subtropical highs near 30°–35° N/S; subpolar lows/polar front near 60°; polar highs. Polar cold air meets subtropical warm air along the **polar front**. Central Europe is mainly influenced by polar and tropical air masses. Seasonal circulation shifts.

### Local wind and mountain effects

| Wind / effect | Recognise it |
|---|---|
| Anabatic | Daytime upslope/valley-to-mountain wind, strengthened by solar heating of the windward slope. |
| Katabatic / mountain wind | Night-time downslope flow as cooled dense air drains under gravity. |
| Valley breeze | Daytime upslope/along-valley flow; reverse drainage at night. |
| Sea breeze | Day: cooler sea air flows toward warmer land; land breeze generally reverses at night. |
| Mistral | Strong cold, northerly/northwesterly flow toward Mediterranean; speed enhanced by channelling/venturi narrowing (the bank answer for a wind accelerated by mountain narrowing). |
| Bora | Cold, gusty katabatic NE wind into the Adriatic. |
| Foehn | Stable air crossing a ridge: windward ascent/cloud/rain; lee descent, warming/drying and strong gusty wind. |
| Scirocco | Warm southerly flow from Sahara toward Mediterranean; not the bank's cold Adriatic wind. |
| Passat / trade wind | Persistent tropical easterly flow; not Bora/Mistral. |

**Mountain wave diagram method:** identify flow crossing a ridge, then read windward-to-lee: forced ascent and cloud on windward slope; wave crests downwind. Smooth lens-shaped **altocumulus lenticularis** marks a wave crest; rolling/rotor cloud beneath the wave on the lee side signals severe low-level turbulence. Expect lee-side sink/updraft, rotor turbulence and possible abrupt wind-direction/speed change; in a valley approach, wind shear can reverse direction by 180° (bank Q137).

## 4. Humidity, stability, clouds and precipitation

### Moisture terms

- Water exists in atmosphere as gas (invisible water vapour), liquid droplets and solid ice crystals.
- **Dew point (Td):** temperature to which air must cool at essentially constant pressure to become saturated (RH 100%). **Spread/dew-point depression = T − Td.** Smaller spread → air nearer saturation and greater fog/cloud risk.
- Relative humidity (RH) = actual water vapour / saturation amount at that temperature ×100%. Cooling air without adding/removing vapour makes RH rise and spread shrink; Td remains approximately constant until saturation. Warming does the reverse (spread grows, RH falls). Saturation can also occur by adding water vapour.
- Saturated vapour pressure/capacity increases with temperature. At 1000 hPa and 20°C the lesson gives saturation mixing ratio about 14.9 g/kg dry air. Lesson example: at 24°C, 15 g/m³ vapour with saturation capacity 22 g/m³ → RH = 15/22 ×100 ≈ **68%**.
- Dalton's law: total pressure of gas mixture = sum of partial pressures. Mixing ratio is mass of water vapour per mass of dry air. Supercooled water is liquid below 0°C and may freeze on impact.

### Cloud formation and cloud families

Air reaches saturation by cooling (convection, orographic lift, frontal lift, advection over colder surface, night radiation cooling) or by adding moisture. Cumulus base forms where the rising parcel temperature reaches **its dew point** (not environmental dew point). A parcel cools dry-adiabatically until saturation, then at the saturated rate. An inversion can cap vertical cloud growth.

| Family / prefix | Main types and visual cue | Typical weather / exam cue |
|---|---|---|
| High: **cirro-** (Ci/Cc/Cs) | Cirrus: fine wisps/feathers, ice; Cirrocumulus: tiny white ripples; Cirrostratus: thin transparent veil | Ci = wisps; Cs often gives halo around Sun/Moon; high cloud often precedes a warm front. |
| Middle: **alto-** (Ac/As) | Altocumulus: patches/rolls; Ac castellanus: turreted tops; Altostratus: broad grey layer, Sun dimmed/obscured | Ac castellanus can warn of instability/thunder later. As commonly thickens ahead of a warm front. |
| Low: **strato-/nimbo-** (St/Sc/Ns) | Stratus: uniform low layer; Stratocumulus: low rolls/lumps; Nimbostratus: thick, dark, widespread layer | Ns = prolonged/continuous rain or snow; St can give drizzle/mist and poor visibility. |
| Vertical: **cumulo-** (Cu/Cb) | Cu: detached cauliflower; Cb: towering cloud, often anvil | Cu/Cb are convective; showers, turbulence; Cb adds lightning, hail, icing, gusts and severe turbulence. |

**Cloud amount codes (octas):** SKC 0/8; FEW 1–2/8; SCT 3–4/8; BKN 5–7/8; OVC 8/8. Cloud base in METAR is normally reported in hundreds of feet above aerodrome. `///` = unavailable/unknown group in some automatic reports.

### Stability and precipitation

- Stable parcel displaced upward returns toward equilibrium: layered/stratiform cloud, limited vertical development, smooth conditions but widespread low cloud/steady precipitation possible.
- Unstable parcel continues rising: cumuliform cloud, showers, thermals and turbulence. Conditional instability means unsaturated air is stable but saturated air is unstable.
- Precipitation particle growth needs adequate cloud depth and moderate/strong updrafts. **Coalescence**: droplets collide/merge in warmer clouds. **Wegener–Bergeron–Findeisen**: in mixed supercooled-droplet/ice cloud (especially below about −12°C), vapour deposits onto ice crystals, crystals grow and fall as snow/precipitation.
- Continuous precipitation is commonly frontal/stratiform; showers are convective, intermittent and more variable/heavy. Rain vs rain showers are separate codes/categories. Ns is the prolonged-rain answer; Cb yields showers/hail.

## 5. Fog, visibility and icing

### Fog / obscuration decision table

| Type | Trigger and typical setting | Quick recognition / clearing |
|---|---|---|
| Radiation fog | Ground loses heat on a clear night; moist surface air cools to Td. Light wind, often 2–6 kt (lesson), stagnant/slow air. | Land, valleys, dawn; overcast prevents it; sunshine or increased mixing usually clears it. |
| Advection fog | Warm, moist air moves over colder land/sea and cools to Td; moving air needed (lesson example around 15 kt). | Coast/sea, can persist day or night; warm moist air over cold surface. |
| Orographic / hill fog | Moist air forced upslope cools adiabatically to saturation. | Cloud on terrain; windward slopes/high ground. |
| Steaming / evaporation fog | Cold air over warmer water gains vapour until saturated. | Sea smoke over lakes/sea in cold air. |
| Frontal / precipitation fog | Rain from warm/occluded front evaporates into cooler air underneath and saturates it. | Near fronts, persistent precipitation. |
| Haze | Fine dust/pollution aerosols scatter light; often trapped below inversion. | Not especially temperature-sensitive (bank Q40). |

- **Visibility:** fog (FG) = less than 1 km; lesson's mist/nevel = 1–3 km; haze (HZ) is aerosol, not tiny water droplets. In METAR, BR = mist and BCFG = patches of fog. METAR visibility is prevailing reported visibility; RVR is runway visual range. Visibility against the Sun is worse; at night a lit target is used.
- Low spread + falling temperature = fog tendency. Strong wind is not typical radiation-fog set-up. Overcast sky suppresses nocturnal radiative cooling and can prevent radiation fog.

### Icing

| Type | Formation / typical cloud | Appearance and danger |
|---|---|---|
| Clear (glaze) ice | Large supercooled droplets spread before freezing; often convective cloud/freezing rain; strongest danger about 0 to −10°C. | Smooth/transparent, heavy, hard to detect; severe shape/weight change. |
| Rime | Many small supercooled drops freeze immediately; often stratiform/Stratus. | Rough, opaque/milky, trapped air; chiefly on leading edges. |
| Mixed | Both droplet sizes/processes. | Irregular, can be severe. |
| Hoar frost | Vapour deposits/freezes directly on a cold parked airframe. | Crystalline/opaque; must be removed before take-off. |

- Airframe icing requires **sub-zero air plus visible supercooled liquid water** (cloud or precipitation); exam's most dangerous range is **0 to −12°C** (lesson says especially 0 to −10/−15°C). Ice crystals alone in very cold clear air do not make the usual airframe icing condition.
- Carburettor icing: venturi pressure drop and fuel evaporation cool the intake; can occur **outside cloud and at OAT +15 to −10°C**. This differs from airframe icing and may occur even when ambient temperature is above freezing.
- Frost/ice on lifting surfaces must be removed before flight. Do not fly into known severe icing or a thunderstorm.

## 6. Air masses, pressure systems, fronts and upper troughs

### Air-mass classification and modification

Air mass = very large body with relatively uniform horizontal temperature/humidity. Character comes from **source region plus track**. `c` = continental (dry source), `m` = maritime (moist); `P` = polar (cold), `T` = tropical (warm), `A` = arctic (very cold). It is modified on its route.

| Air mass / movement | General exam tendency |
|---|---|
| Continental polar (cP), e.g. Russia to Central Europe in winter | Cold, generally dry/stable at source; correct bank answer for Russian winter source. |
| Maritime polar (mP) | Cool/moist; often unstable with showers, good visibility outside showers. |
| Tropical maritime (mT) | Warm, very moist; often stable low cloud/drizzle/fog if moving over colder surface. |
| Continental tropical (cT) | Hot/dry; may be unstable in summer, haze/dust possible. |
| Polar air travelling south in spring/summer | Warmer ground heats the lower air → destabilises it, convective Cu/showers. |

Warm air passing over a colder surface cools from below → stabilises (stratus, prolonged precipitation, poor visibility); cold air over a warmer surface warms below → destabilises (Cu/showers, good visibility between). Subsidence also stabilises; forced lifting destabilises/produces cloud if moisture is sufficient.

### Fronts and polar-front low

A front is the transition zone between dissimilar air masses. On a chart, **cold-front triangles point in direction of motion; warm-front semicircles point in direction of motion; occlusion alternates triangles/semicircles on the same side; stationary front symbols alternate on opposite sides.** A front aloft is not a surface front.

| Feature | Warm front | Cold front |
|---|---|---|
| Motion/slope | Warm air glides gently over retreating cold air; average slope about 1:150; usually slower. | Cold air undercuts/lifts warm air steeply; average slope about 1:50; usually faster. |
| Cloud order | Ci → Cs → As → Ns, then St/Sc in/near warm sector; high cloud appears far ahead. | Cu/Cb in active narrow band; embedded Cb possible; broken Cu/Sc behind. |
| Precipitation/visibility | Broad, prolonged steady rain/drizzle, typically 200–400 km ahead near surface front; low cloud, mist/murky visibility; warm sector can remain poor. | Narrower, heavier showers/rain, possible thunder/hail; visibility moderate in rain, rapidly good behind. |
| Temperature/dew point | T often rises; dew point rises ahead then levels off. | T and Td usually fall after passage; clear/cool air behind. |
| Pressure | Falls increasingly ahead; usually steadies in warm sector (keeps falling if low deepens). | Near minimum at front; falls ahead, then rises quickly behind. |
| Surface wind | Tends to back/increase ahead; veers on passage. | May back slightly ahead, then veers sharply/gustily on passage. |
| Main flying implication | Long-duration low ceiling, poor visibility, steady precipitation and icing risk. | Shorter but more intense band; turbulence, showers, embedded Cb, hail and gusts. |

**Bank/lesson distinction on veering:** Q55 expects **veering at passage of both warm and cold fronts** in a Central European polar-front low. Lesson text also says warm-front surface wind may back ahead, then veer at passage. Read the question's time phrase: a wind change *ahead of* the warm front is not the same as *during passage*.

- Warm sector = between warm and cold fronts; typically milder, relatively stable summer weather, moderate/good visibility and scattered clouds. Bank summer VFR answer: moderate-to-good visibility, scattered cloud.
- Cold-front passage: pressure briefly falls then rises; after a cold front expect backside weather (Rückseitenwetter): good visibility with Cu and isolated rain/snow showers.
- A polar-front low generally travels parallel to isobars in its warm sector; strongest pressure-fall/isallobar direction is another movement clue. The cold front catches the warm front → occlusion. Occluded-front weather combines warm-front layered rain and cold-front features.
- Stationary front: boundary with no significant horizontal displacement.
- An upper trough/cold-air inflow aloft promotes instability, showers and thunderstorms; not calm stable weather. In NH, low-level cyclone flow counter-clockwise.

## 7. Local weather hazards and thunderstorm avoidance

### Thunderstorms

Conditions: moisture + instability + lift/trigger. Thermal storms especially need warm, humid lower air and conditional instability. Triggers include daytime surface heating, fronts, cold-air advection aloft and orographic lift. An upper trough/cold pool often favours showers/Cb. **Overdevelopment** in a report means vertical growth of cumulus into rain showers (Q106).

| Stage | Dominant motion / cue |
|---|---|
| Cumulus / developing | Updrafts dominate; growing Cu, no mature precipitation core yet. |
| Mature | Strong updrafts **and downdrafts**, heavy precipitation, lightning, turbulence, icing, hail, gusts and wind shear; most hazardous. |
| Dissipating | Downdrafts dominate; precipitation/outflow continue as updraft weakens. |

- Cold downdraft and precipitation spreading at surface create a **gust front**; near heavy showers/CB expect severe low-level wind shear and downdrafts. A nearby visible shower on approach is a warning, not a reason to continue.
- Lightning can overheat/damage aircraft skin and exposed parts and cause electrical/radio effects. Main exam answer: surface heating and damage to exposed parts.
- Avoid thunderstorms and their hazards; radar/satellite do not make penetrating a CB safe. Wind shear is a sudden change in speed and/or direction over a short distance.
- Ground inversion: during take-off/climb, leaving the inversion can cause a sudden decrease in airspeed and climb performance (bank answer). Expect strong low-level shear/turbulence at inversion boundaries.

### Mountain / foehn / turbulence

Stable cross-mountain flow can form standing waves: lenticular cloud in wave crests, rotor cloud below in lee. Rotor clouds indicate moderate/severe turbulence; lee-side rotors are more hazardous than uniform layered cloud. Foehn windward side: layered cloud, mountains obscured, poor visibility and moderate/heavy rain. In the Bavarian/Alpine case in the bank, expect nimbostratus on the southern (windward) Alps; lee-side rotor clouds and warm, dry foehn to the north. Lee side generally has warm, dry, gusty descending flow, possible lenticulars/rotors. Unstable humid air forced up a ridge can instead produce embedded Cb, thunder, hail and showers. Valley approach with strong cross-ridge wind can have 180° direction change/shear.

Other turbulence types: convective (below Cu from thermals), mechanical/wind-shear, orographic/rotor, clear-air turbulence (CAT, often near jet/front), low-level jet and wake turbulence. Light turbulence is commonly found below cumulus because of thermal convection.

## 8. Weather imagery, charts and aviation products

### Choose the right product

| Product | What it shows / is for | What it does not prove |
|---|---|---|
| Surface weather chart | Analysed MSL pressure, high/low centres, isobars and fronts; spacing gives gradient/wind strength. | Not a detailed route hazard chart or airport observation. |
| Significant Weather Chart (SWC) | Significant hazards (e.g. turbulence/CAT, icing, CB, fronts, freezing level) for a layer/time; best bank answer for current/forecast flight hazards such as CAT and thunderstorm frequency. | Not a direct precipitation radar image. |
| Low-Level SWC / LLSWC | Low-level hazards, icing, turbulence, fronts, cloud/weather, freezing level (depending chart). | Does **not** show radar echoes of precipitation (bank Q138). |
| Weather radar | Current precipitation location/intensity; reflectivity depends on size and nature of hydrometeors. Composite combines local radar scans. | Not cloud, temperature, pressure, or a full forecast; weak/no echo does not mean safe. |
| Satellite visible / HRV | Daylight cloud coverage/texture, especially convective structure; compact bright spots often Cu/Cb; semi-transparent streaks often Ci. | Does not directly measure precipitation intensity or temperature. |
| Satellite IR | Cloud-top temperature; colder tops generally higher cloud tops. Usable day and night. | Not cloud base, surface visibility or turbulence itself. |
| RGB | Combines channels to distinguish cloud type/height/phase more easily; superiority over HRV is improved differentiation by colour composites. | Not simply a forecast model. |
| NWP model | Numerical forecast fields; visualize expected hazards along route, pressure/front/wind fields. | Not actual airport conditions and not a precise 14-day airport cloud/visibility report. |
| GAFOR | General Aviation Forecast by region/route, visibility and cloud ceiling; areas classified open/difficult/marginal/closed. Belgian lesson: 7 zones, 6-hour outlook in 2-hour periods. | Not an ATC clearance or substitute for actual observations/briefing. |

**Radar intensity mnemonic:** **green → yellow → orange → red = increasing intensity**. Orange/red suggests heavy showers, hail or graupel. Radar echo strength relates to particle size/nature. A **composite** is a mosaic of smaller local radar pictures. Radar can miss/overstate precip (snow at altitude, low stratus, attenuation/clutter, inversion effects); lesson tip: never base the whole decision on radar alone—use it with METAR, satellite, charts and forecast.

### METAR decode order and keys

Read: `type station time wind visibility [RVR] present weather cloud temperature/dew point QNH [trend/recent weather]`.

Example: `METAR EBAW 090850Z 25015KT 8000 -RA SCT004 BKN007 OVC013 05/04 Q0974` = routine Antwerp observation at day 09, 08:50 UTC; wind from 250° at 15 kt; visibility 8 km; light rain; scattered cloud at 400 ft, broken at 700 ft, overcast at 1300 ft; T 5°C/Td 4°C; QNH 974 hPa.

| Code / pattern | Meaning |
|---|---|
| METAR / SPECI | Routine aerodrome observation / special observation when significant change occurs. `AUTO` = automated report. `COR` = corrected report. `CAVOK` = visibility ≥10 km, no significant weather, and no significant low cloud (use only when all conditions meet the definition). |
| `ddffKT`, `dddffGggKT` | Wind direction in degrees **from** which wind blows, speed in knots; gust `G`. Example `225/15` or `22515KT` = SW wind from 225° at 15 kt, not km/h. `VRB` variable; `00000KT` calm; `dddVddd` directional variation. |
| Visibility | Metres (`9999` = 10 km or more); `CAVOK` only when full criteria apply. RVR often `Rxx/####` for runway visual range. |
| `− / (no sign) / +` | Light / moderate / heavy intensity. Example `+RA` = heavy rain; `SHRA` = rain showers (moderate unless `+SHRA`). |
| `MI, BC, PR, DR, BL, SH, TS, FZ` | Shallow, patches, partial, low drifting, blowing, showers, thunderstorm, freezing. Prefixes modify following weather (`FZRA` freezing rain, `TSRA` thunderstorm with rain, `SHRA` rain showers). |
| Precipitation | `DZ` drizzle; `RA` rain; `SN` snow; `SG` snow grains; `PL` ice pellets; `GR` hail; `GS` small hail/snow pellets; `UP` unknown precipitation (automated). |
| Obscuration / other | `BR` mist; `FG` fog; `HZ` haze; `FU` smoke; `DU` widespread dust; `SA` sand; `VA` volcanic ash; `SQ` squall; `FC` funnel cloud/tornado; `SS` sandstorm; `DS` duststorm. |
| Cloud | `FEW/SCT/BKN/OVC` amount; followed by height in hundreds of feet and type if significant, e.g. `BKN020CB` = broken CB at 2000 ft; `VV///` vertical visibility unavailable. `NSC` no significant cloud; `NCD` no cloud detected by automatic system. |
| Temperature / pressure | `05/04` = +5°C / +4°C; `M02/M05` = −2°C / −5°C. `Q1013` = QNH 1013 hPa; `A2992` = altimeter inches Hg. |
| Trend / remarks | `NOSIG` no significant change expected; `TEMPO` temporary; `BECMG` becoming; `RE/` recent weather (e.g. `RESHRA`). These groups are not the core observation. |
| Exam-specific | `SHRA` = (moderate) rain showers (Q101); `+RA` = heavy rain (Q139); `225/15` = SW 15 kt (Q102). |

### TAF, SIGMET, GAMET, ATIS and other reports

- **TAF** = Terminal Aerodrome Forecast: forecast for aerodrome, with station, issue/validity period, wind, visibility, weather, cloud, and change groups. It is not a current METAR.
- `FMhhmm` = from a specified time; `BECMG` = gradual change; `TEMPO` = temporary fluctuations (usually shorter spells); `PROB30/40` = 30/40% probability; `TX/TN` = max/min temperature (where included); `NSW` = no significant weather; `NOSIG` is a METAR trend, not a replacement for TAF change groups.
- **SIGMET** = warning for specified significant en-route weather in an **FIR/UIR**, with phenomenon, vertical extent, validity, movement/intensity as coded. Bank answer: issued for FIRs/UIRs, not airports/countries/routings. Decode the valid area/time and hazard, then compare with route/altitude.
- **GAMET** = area forecast for low-level flights (typically below FL100, or FL150 in mountainous areas as nationally specified); covers weather/hazards and cloud/visibility/wind for a region/time. **Beyond question bank:** exact national format/limits are product-specific; consult the issuing authority's legend.
- **ATIS** = continuous aerodrome information for arriving/departing aircraft; includes operational items such as runway in use, transition level, and weather. It can provide destination operational information in flight. Bank asks what it has that METAR does not: runway/transition-level operational information.
- **VOLMET** = broadcast of meteorological reports/forecasts for aerodromes; **PIREP/AIREP** = pilot aircraft weather report; neither is the answer for airport operational information. METAR = observation; TAF = forecast; SIGMET = en-route hazard warning; ATIS = aerodrome operating broadcast.

## 9. Figure / scenario question methods and exam traps

### Quick decision flow

```text
Question asks about...
├─ observed airport weather? → METAR / SPECI (decode groups)
├─ forecast airport weather? → TAF (validity + FM/BECMG/TEMPO)
├─ en-route hazard? → SWC/LLSWC + SIGMET (route, altitude, validity)
├─ current precipitation location/intensity? → weather radar (not cloud/safety)
├─ cloud cover / fronts overview? → satellite (VIS/HRV, IR, RGB)
├─ pressure centres/fronts/wind gradient? → surface chart (isobars)
└─ VFR regional ceiling/visibility? → GAFOR
```

| Figure type | Read it in this order |
|---|---|
| Front symbol map | Triangles = cold front, semicircles = warm front; both same side = occlusion; alternating opposite sides = stationary. Symbol side gives direction of travel. Match labelled front to legend, not line colour alone. |
| Cloud photograph | Wispy fibres → Ci; thin veil/halo → Cs; small ripples → Cc/Ac; flat layer → St/As/Ns; detached cauliflower → Cu; tall tower/anvil → Cb. Ask whether layered (stable) or vertical/convective (unstable). |
| Mountain cross-section | Windward forced lift; lee wave; lens-shaped cloud aloft = Ac lenticularis; rolling low lee cloud = rotor; expect turbulence and shear. |
| Satellite | Compact white cloud spots on HRV/VIS = Cu/Cb; semi-transparent streaks = Ci; IR cold tops indicate high cloud. RGB distinguishes types/levels better. |
| Radar | Find echo position first, then colour/intensity. Green weak → yellow moderate → orange/red heavy convective precip/hail risk; composite = mosaic. Never infer cloud top/base or flight safety from radar alone. |
| Surface chart | Find H/L and front symbols; isobar spacing = pressure gradient/wind strength; near-parallel flow aloft, surface flow crosses toward low. Large spacing = light/variable/local winds. |
| Vertical temperature diagram | Read temperature at two heights, compute ELR; compare with SALR/DALR. Inversion slopes toward warmer temperature with height; inversion caps Cu. |
| Front-passage timeline | Warm front: pressure falls, high-to-low cloud sequence/steady rain, warm sector; cold front: pressure minimum then rise, sharp showers/Cb/gusts, then good visibility and Cu/showers. |

### High-yield traps / bank-key notes

- **SalR is lower than DALR** because condensation releases latent heat; it is not a fixed exact rate in nature. Use exam mean 1.5°C/1000 ft or 0.6°C/100 m.
- 0.65°C/100 m is ISA environmental lapse rate; 1°C/100 m is DALR; 0.6°C/100 m is SALR. Don't swap them.
- A parcel's cloud base occurs at parcel T = parcel Td. An inversion usually limits Cu tops and stabilizes air.
- Warm/moist over cold = advection fog; cold over warm water = steaming fog; clear/calm moist night = radiation fog; forced upslope = orographic fog; frontal rain evaporating in cool air = frontal fog.
- Haze is aerosol; fog/mist is water droplets/ice crystals. HZ is least sensitive to temperature change (Q40).
- Stable high pressure is not automatically foggy: winter subsidence inversion traps moisture; summer high often has clear sky or scattered/few Cu and weak local winds.
- Wind is initiated by PGF, not Coriolis/centrifugal force; closer isobars mean stronger wind. Above friction layer wind is parallel to isobars; surface wind crosses toward low.
- Convergence at ground → rising air/cloud; divergence at ground → sinking/dissipation. Cold-air advection at the surface destabilises; cold air aloft also destabilises.
- Wind-direction convention is direction **from** which it blows. `225/15` is 225° (southwest) at 15 **knots**.
- Warm-front sequence begins with high clouds and gradually lowers; warm-front rain is widespread and prolonged. Cold-front weather is usually intense, narrow, convective; post-front is good visibility with Cu/showers, not settled clear sky.
- Cumulus-stage storm = updraft; mature stage = both strong up- and downdrafts; dissipating = downdrafts. Gust front comes from cold precipitation downdraft.
- Clear ice = large droplets, spread, transparent; rime = small droplets, freeze immediately, white/opaque. Airframe icing is not the same as carb ice.
- Satellite = cloud overview; radar = precipitation; neither directly gives flight visibility/turbulence. SWC gives hazards; surface chart gives MSL pressure/fronts.
- **Keyed peculiarities:** bank Q19's keyed true-altitude result is 7300 ft under its approximate correction method; Q55 wants veering *on passage* of both fronts; Q117 calls descending air behind a mountain range katabatic; Q133 selects Mistral for channelling; Q134 selects Bora for cold NE katabatic Adriatic wind. Apply distinctions in the relevant sections above.

## 10. Bank coverage index (questions 1–143)

| Questions | Covered in |
|---|---|
| 1–19 | Atmosphere, ISA, density, lapse rates, altimeter pressure settings and true altitude (sections 1–2). |
| 20–29 | Geostrophic/surface wind, friction, convergence, divergence, global circulation, anabatic wind (section 3). |
| 30–43 | Water phases, spread/RH, cloud base/type/top, fog tendency, HZ, radiation fog, precipitation updrafts (section 4). |
| 44–64 | Air masses, source/track, front symbols and passage, polar-front low, upper trough, high-pressure summer, foehn/mountain-wave figure (sections 3 and 6). |
| 65–79 | Airframe icing, turbulence, wind shear, thunderstorms, lightning, gust front, ground inversion, foehn/rotors (sections 5 and 7). |
| 80–104 | Satellite channels, radar, composite/intensity, SWC/surface/wind charts, ATIS, METAR wind/showers, SIGMET, NWP (section 8). |
| 105–120 | Orographic/advection fog, overdevelopment, troposphere/ISA/inversions, QFF, density, PGF, katabatic, Td/RH, instability (sections 1–5). |
| 121–143 | Cloud prefixes, Ns/precipitation, warm-sector VFR, stationary front, pressure sequence, upper low/height contours, Mistral/Bora, icing, valley shear, LLSWC, +RA, ATIS, mountain wind, backside weather, foehn (sections 3–8). |

**Coverage check:** all 143 question stems/options are addressed by the keyed facts, decoding rules, calculations, figure methods and distinctions above. For true-altitude arithmetic, follow any correction table explicitly supplied with the exam question; the bank's nearest-option key is authoritative for its stated example.
