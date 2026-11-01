# Meteorology — Detailed Lesson Notes (PPL(A), Belgian course)

These notes follow the Belgian Vak 4 Meteo lessons (chapters 1–13), the teacher's 2025–26 test comments, the Storm Goretti case study and the 143-question ECQB bank. Dutch terms are included where they help identify the lesson vocabulary. The companion [`quick-reference/30_Meteorology.md`](../quick-reference/30_Meteorology.md) is the compressed exam sheet. **Beyond question bank** marks useful lesson extensions not directly required by the 143 stems.

## How the course fits together

Meteorology for a VFR pilot is a chain: Sun heats the Earth unevenly → pressure and temperature differences develop → air moves and is modified → vertical motion and moisture create cloud/precipitation → fronts and local terrain organise hazards → reports, charts and observations describe present/expected weather. For flight planning, use observation + forecast + significant-weather/hazard products together, then decide if the route, altitude, time and aircraft limits are compatible. No single radar/satellite image is a go/no-go decision by itself.

## Chapter 1 — The atmosphere (De atmosfeer)

- The atmosphere is the gaseous envelope around Earth. Meteorology divides it in different ways; for pilots, the thermal layering is especially useful.
- Troposphere: lowest layer, variable depth and where almost all familiar weather and hydrometeors occur. Temperature generally declines with height; the average environmental lapse is about 6.5°C/km. The tropopause is the transition boundary.
- The tropopause is not at one fixed height: lesson values are 6–8 km and about −40°C near the poles; about 11 km and −56.5°C in mid-latitudes; 15–18 km and about −75°C over the equator. Seasons and air masses affect it. Stratospheric temperature rises again with height, largely associated with ozone absorption; near 50 km it approaches the surface temperature.
- Below roughly 85 km the atmosphere is the homosphere: gases are mixed relatively uniformly. Above it, the heterosphere has composition increasingly separated by molecular mass/diffusion. Named layers include troposphere, stratosphere, mesosphere, thermosphere and exosphere.
- Dry air is approximately 78% nitrogen, 21% oxygen and 1% other gases. Water vapour is variable (roughly 0.1–4%) and aerosols are suspended particles. Oxygen percentage remains similar with altitude, but oxygen partial pressure falls as total pressure falls—important to physiology.
- ISA assumes dry air, MSL pressure 1013.25 hPa, temperature +15°C, gravity 9.80665 m/s² and density 1.225 kg/m³. In its troposphere temperature falls about 6.5°C/km (1.98°C/1000 ft) to −56.5°C at 11 km/36,000 ft; it is isothermal from 11–20 km and rises above that.

**Teacher/exam emphasis:** distinguish the tropopause boundary from the stratosphere; weather is principally in troposphere; ISA values are reference values, not today's actual atmosphere. The exam asks both 11 km and 36,000 ft, 500 hPa at FL180, 1013.25 hPa and the 1.225 kg/m³ sea-level density.

## Chapter 2 — Heat transfer (Warmteoverdracht)

- Radiation: electromagnetic energy without direct contact. The Sun emits mainly shorter wavelengths; Earth absorbs/refects incoming energy and emits longer-wave infrared. Wien's law links the wavelength of peak emission inversely to absolute temperature. Earth's tilt (23.5°) creates seasonal differences; albedo describes reflected versus absorbed radiation.
- Conductance/conduction: heat transfer by molecular contact, e.g. ground warms the air touching it. It is strongest close to the surface and depends on material conductivity.
- Convection: vertical transfer as warmed, less-dense air rises and cooler air descends. The same process drives thermals, cloud development and large-scale circulation.
- Advective heat transport: movement of an air mass from one place to another, carrying its temperature/moisture. Turbulent mixing also redistributes heat.
- Latent heat is stored/released in phase changes. Evaporation consumes heat; condensation releases it. Condensation can warm the rising cloud parcel relative to a dry parcel, reducing its cooling rate and supporting deeper cloud.

**How to apply:** if a question asks why moist rising air cools more slowly than dry air, answer latent heat released during condensation. If it asks how air mass temperature changes horizontally, distinguish advection from convection.

## Chapter 3 — Temperature (De temperatuur)

- Heat is transferred energy; temperature measures average molecular kinetic energy. Absolute zero is 0 K = −273.15°C. Celsius/Kelvin conversion is `K = °C + 273.15`; Fahrenheit conversions are `°C=(°F−32)/1.8` and `°F=1.8×°C+32`.
- Temperature is observed with thermometers (mercury, alcohol, bimetal, electronic/IR; maximum/minimum instruments). A standard thermometer screen is white, about 1.5 m above grass, ventilated and shielded from direct sunlight.
- Solar heating depends on latitude/sun angle, season, time of day, ground type, altitude, prevailing wind, cloud and ground cover. Land heats/cools faster than sea; cloud and wind modify daily range.
- Daily minimum occurs around sunrise +1 hour; maximum near solar zenith +2 hours (course approximation). Changing cloud, precipitation, wind and air mass can overwhelm this usual daily pattern.
- ISA numbers and lapse rates are in the quick sheet. Distinguish the **environmental** vertical profile from a lifted parcel's **adiabatic** cooling. Ground, subsidence, frontal and tropopause inversions have different causes: night surface radiative cooling; broad high-pressure subsidence and compressional warming; frontal juxtaposition of warm/cold air; tropopause/isothermal layer.
- Subsidence warms and dries descending air; under persistent high pressure the subsidence inversion can descend gradually and trap moisture/pollution below. A ground inversion forms after nocturnal radiational cooling and can create poor visibility/fog and wind shear.

**Teacher test correction:** QNH is reduced to MSL using ISA conditions; QFF uses actual meteorological conditions. On the ground, set QNH and compare the altimeter with airfield elevation; alternatively set QFE and verify zero at its reference point. Don't call QFE an MSL setting.

## Chapter 4 — General atmospheric circulation (Algemene luchtcirculatie)

- Earth's absorbed energy is unevenly distributed. Heat is transported from low to high latitudes both advectively and convectively, chiefly through the atmosphere.
- In the idealised belt picture, the equator/ITCZ is a persistent low with rising air; subtropical highs occur near 30–35° N/S; subpolar lows are near 60°; polar regions have highs. The polar front separates cold polar and warm subtropical air, especially across Central Europe.
- Real circulation is not a fixed set of perfect cells: land/sea contrasts and seasonal heating shift pressure belts/fronts and alter air-mass tracks. The source region and route determine an air mass's character.

**Beyond question bank:** the Hadley/Ferrel/Polar cell model explains the broad belts but doesn't predict a particular day's synoptic chart. Flight planning should rely on actual analyzed/forecast charts rather than a memorized global schematic.

## Chapter 5 — Pressure (Luchtdruk)

- Atmospheric pressure is force per area produced by the mass of the air column above a point. Units: 1 Pa = 1 N/m²; 1 hPa = 1 mbar = 100 Pa; 1 bar = 100,000 Pa. Standard pressure corresponds to about 76 cm mercury / 29.92 in Hg.
- Pressure falls with height, rapidly near the surface. The lesson gives approximately 1 hPa per 8–12 m depending on height; for exam altimeter approximations, 1 hPa per about 27–30 ft is often used. These are local approximations, not a universal linear law.
- Pressure changes due to height, diurnal effects, movement/development of highs/lows, fronts and weather disturbances. A station's barometric tendency is its pressure change during the previous 3 hours; isallobars display pressure change.
- Surface charts use isobars (equal pressure). A ridge is a high-pressure extension; a trough is a low-pressure extension. Tight spacing = strong gradient; broad spacing = weak gradient.
- QNH/QFE/QNE/QFF definitions and ground checks are in the cheat sheet. `QNE` means standard 1013.25 hPa and flight-level reference. QNH altimetry is MSL-reduced using ISA; QFF is reduced using actual conditions.
- In a multi-station problem, transfer pressure using the question's ft/hPa approximation; do not mix the QNH difference sign. A lower QNH than 1013 means a flight level has a lower geometric altitude than its nominal pressure altitude. Cold air contracts the layer: true altitude is lower than indicated; warm air expands it.

**Teacher test correction:** the teacher identified pressure-setting/QNH/QFF confusion as a common error and explicitly restated the ground-check method. In any altitude question, identify the datum first, then correct pressure, then temperature.

## Chapter 6 — Depressions and anticyclones

- A high has pressure increasing inward; a low decreases inward. Surface low pressure is associated with convergence and ascent; high pressure with widespread subsidence. At upper levels the divergence/convergence structure supports or weakens the system.
- In a high, descending air warms adiabatically and dries, forming a subsidence inversion. In winter, moisture can collect below it, yielding mist/fog/low stratus. In summer, the same stable high often has cloud dissipation or scattered shallow Cu, weak synoptic gradient and local wind systems.
- A low has broad rising motion, cloud, precipitation and often stronger wind. Filling means pressure rises; deepening means pressure falls. Types include polar-front (mid-latitude), polar low, thermal low, orographic low, cold-pool low, tornado and tropical cyclone.
- The polar-front low's fronts and warm sector are described in Chapter 11. An upper trough is an elongated low aloft and often favours showers/CB.
- Satellite imagery: polar-orbiting satellites pass at low altitude (lesson roughly 500–1000 km); geostationary satellites remain over one longitude at about 35,800 km and provide repeated regional views. Visible, infrared and water-vapour channels answer different questions.

**Beyond question bank:** a pressure centre alone does not determine weather at an airport; wind, frontal position, air-mass stability, terrain and moisture all matter.

## Chapter 7 — Wind (De wind)

- Wind is horizontal air motion relative to the surface. Pressure-gradient force starts it, directed high-to-low and perpendicular to isobars. Coriolis deflects motion (right NH/left SH); centrifugal force acts outward in curved flow; friction opposes motion.
- Straight isobars aloft: geostrophic balance of PGF and Coriolis, wind parallel to isobars. Curved isobars: gradient wind balances PGF, Coriolis and centrifugal force. At the surface, friction reduces speed and Coriolis; wind crosses isobars toward low pressure. More rugged/vegetated terrain causes greater friction.
- Buys-Ballot law: in NH with back to wind, low lies to the left and high to the right. Veering means clockwise/right; backing means anticlockwise/left. Wind generally speeds up and becomes more parallel to isobars with height as friction decreases.
- Jet streams are narrow bands of fast wind in upper troposphere/lower atmosphere. Types include polar, subtropical, equatorial, stratospheric and low-level jets; low-level jets can occur near fronts/night inversions.
- Local modifications: anabatic daytime upslope and katabatic night drainage; sea/land breeze from differential heating; Mistral strengthened by channel narrowing; Bora cold NE katabatic flow to Adriatic; foehn warming/drying on lee after descent.
- Turbulence types in lesson: convective, wind-shear/mechanical, orographic, clear-air (CAT), low-level jet and wake. Wind shear is abrupt direction/speed change over short distance and may accompany inversions, showers, fronts or terrain.

**Exam method:** first identify chart level (surface or above friction), then isobar spacing (speed), orientation (direction), hemisphere, curvature, and terrain. A large spacing means low pressure gradient and light/variable wind/local breezes, not strong westerlies.

## Chapter 8 — Thermodynamics (Thermodynamica)

- Gas state relates pressure, volume and absolute temperature. For fixed mass: Boyle `PV=constant` at fixed T; pressure law `P/T=constant` at fixed V; Charles `V/T=constant` at fixed P; combined `PV/T=constant`; ideal gas equation `PV=nRT`.
- Isothermal compression allows heat exchange to keep T fixed; adiabatic compression/expansion occurs without heat exchange. Air rising expands and cools; descending air compresses and warms.
- Density `ρ=P/(RT)`: depends mainly on pressure and absolute temperature, with humidity a smaller influence. Lower density reduces lift and aircraft performance. Lesson gives density-altitude correction of 120 ft per °C: at PA 7000 ft and OAT 18°C, ISA there is +1°C, hence DA ≈ 7000 +17×120 = 9040 ft.
- Water vapour is invisible gas; cloud/fog/precipitation contain liquid and/or ice. Phase changes exchange latent heat. Dalton's law says total pressure equals partial-pressure sum. Vapour pressure is actual vapour pressure; saturation vapour pressure is the maximum at that T. Exceeding saturation causes condensation.
- Mixing ratio is water vapour mass per dry-air mass; saturated mixing ratio depends on temperature and pressure. RH = actual amount / saturation amount ×100. Lesson example: at 24°C, 15 g/m³ actual vs 22 g/m³ saturation gives 68% RH.
- Dew point is the temperature at which air becomes saturated by cooling at essentially constant pressure. T−Td is spread/dewpoint depression. A falling T at roughly constant Td raises RH and reduces spread.
- Saturation occurs through cooling to dew point or through adding water vapour. Cooling mechanisms include convection, orographic lift, frontal lift, advection over cold ground/sea and radiation cooling.
- Stability: stable displaced parcel returns; unstable parcel continues; neutral parcel rests in new equilibrium. Read radiosonde/skew-T (T-log-P) profiles; compare ELR to DALR/SALR. The course examples and thresholds are on the cheat sheet.

**Beyond question bank:** a sounding can also show wind/temperature/moisture at multiple levels and inform cloud bases, freezing level, inversion, fog and maximum/minimum forecasts. It is a forecast/observation aid, not a direct guarantee of local surface weather.

## Chapter 9 — Clouds (Wolken)

- A cloud is suspended condensed water droplets and/or ice crystals. Condensation nuclei (salt, dust, pollution) provide surfaces for droplets/crystals.
- Stability gives two broad forms: stable layered/stratiform clouds and unstable cumuliform clouds. Cloud family (high/middle/low/vertical), genus and species describe height and shape.
- High: Ci, Cc, Cs; composed mainly of ice. Cirrus fibres; cirrostratus veil and halo. Middle: Ac and As; Ac castellanus has turrets and can precede thunderstorms; As thickens toward fronts. Low: Sc, St, Ns. Ns is thick and gives continuous/prolonged precipitation; St gives low ceiling, mist/drizzle. Cu grows vertically from heating; Cb has towers/anvil and severe hazards.
- Cloud base can be estimated by parcel reaching its dew point; an inversion caps vertical development. In a stable front, high cloud often arrives first and progressively thickens/lowers. The teacher test sequence is Ci → Cs → As → Sc/St/Ns.
- Cloud amount in aviation octas: SKC 0; FEW 1–2; SCT 3–4; BKN 5–7; OVC 8. Height groups in METAR are hundreds of feet.
- Precipitation growth: coalescence in warmer clouds; Bergeron–Findeisen in mixed ice/supercooled-water cloud. Strong updrafts allow medium/large particles to grow; convection produces showers; stratiform cloud often produces continuous precipitation.

**How to answer picture questions:** classify visual structure first (fibrous/veil/layer/roll/lump/tower), then cloud prefix/height and associated weather; don't infer cloud solely by colour. Cumulus is detached with vertical cauliflower tops; cirrus is feather-like; Ns is thick continuous precipitation cloud.

## Chapter 10 — Air masses (Luchtmassa's)

- Air mass covers a very large area with relatively uniform horizontal temperature/humidity; it may span millions of km² through much of troposphere. It forms over a source region where air stagnates: subtropical high source for tropical air; polar regions for polar air.
- Name from source and track: continental or maritime moisture character; polar/tropical/arctic thermal character. The route modifies the original signature.
- Warm air crossing a colder surface is cooled from below and stabilised: layered cloud, prolonged precipitation, moderate/poor visibility. Cold air crossing a warmer surface is warmed at its base and destabilised: Cu/showers/thunder, good visibility outside precipitation.
- Forced ascent by low pressure/orography promotes instability/cloud; broad subsidence in high pressure stabilises. Lesson air-mass examples include cT, cP, mT, mP, arctic maritime and returning polar maritime, whose seasonal behaviour varies.
- Bank example: air entering Central Europe across Russia in winter = continental polar (cP). A polar air mass moving south over warmer spring/summer surfaces destabilises as its lower layers warm.

**Teacher test correction:** the air-mass's properties originate in source region but are modified during its track. Never classify only by current temperature or by the region where the exam says it is located.

## Chapter 11 — Fronts (Fronten)

- A front is the transition zone separating air masses with different temperature/density. They do not simply mix at the boundary; warm air ascends over colder air or cold air undercuts warm air. Passage produces weather change.
- Cold front: steep average slope ~1:50, narrow band, Cu/Cb or embedded Cb; heavy showers, possible thunder/hail, gusts/turbulence; pressure falls approaching and rises rapidly behind; wind veers sharply on passage; visibility improves rapidly after precipitation. Behind: unstable Cu, isolated showers and good visibility.
- Warm front: gentler slope ~1:150. High cloud appears far in advance, thickens and lowers: Ci, Cs, As, Ns, then low St/Sc. Continuous rain begins roughly 200–400 km ahead of surface front and moderates near it; warm sector may have drizzle. Pressure falls ahead, generally becomes steady in warm sector. Wind tends to back/increase ahead and veer on passage. Conditions often stable, low-ceiling, poor visibility.
- Occlusion forms when faster cold front catches warm front. In a warm occlusion, the air behind is warmer than the air ahead; in a cold occlusion it is colder. Weather blends warm-front widespread layered precipitation and cold-front convection.
- Quasi-stationary front has no horizontal movement. Standard map symbols: blue triangles on cold front, red semicircles on warm front, both same side on occlusion, alternating opposite sides on stationary front; symbol points toward motion where applicable.
- Polar-front low development: wave/frontal development, mature stage with warm sector and separate fronts, occlusion as cold front catches warm, then weakening/dissipation. Movement generally parallel to warm-sector isobars; isallobars/strongest falls offer another clue.

**Teacher test corrections:** before warm front pressure falls as warm air arrives aloft; warm sector pressure is largely steady; behind cold front it rises as denser cold air arrives. Cold air entering upper troposphere contracts pressure levels: height contours drop and pack closer. Bank Q55 expects veering during passage of both warm and cold fronts; distinguish passage from the pre-front backing described in the lesson.

## Chapter 12 — Weather phenomena (Weerfenomenen)

### Precipitation and visibility

- Precipitation includes rain, drizzle, snow, sleet, hail; intensity is light/moderate/heavy. It is measured with a rain gauge in mm/m² or litres/m². Continuous frontal rain differs from convective showers. Drizzle is small droplets and poor visibility; hail is associated with Cb; snow is ice crystals aggregating.
- Dew forms when air above vegetation cools to Td; frost/hoar frost is ice deposition/freezing; freezing rain/black ice freezes on contact with a cold surface.
- Visibility is distance at which a conspicuous object can be seen by day or illuminated at night. Meteorological visibility is the worst visibility in any direction; RVR is runway visual range; slant-range visibility is an airborne pilot's oblique view.
- Fog is cloud at ground with visibility below 1 km; lesson calls mist/nevel 1–3 km. Haze is fine dust/industrial/traffic particles scattering sunlight, often trapped beneath inversion. Types and formation rules are tabulated in the cheat sheet.
- Radiation fog: clear sky, night ground cooling, moist air, light wind (lesson 2–6 kt). Advection fog: warm moist air over cold surface, moving air (lesson example ~15 kt), often North Sea/coast. Evaporation/steaming fog: cold air over warmer water; frontal fog: rain evaporates into cooler air; orographic fog: forced ascent to saturation.

### Icing

- Airframe icing occurs when supercooled liquid drops strike an aircraft below freezing. Main risk layer is roughly 0 to −10/−12/−15°C depending source; bank target range is 0 to −12°C.
- Large droplets spread then freeze: clear/glaze ice, often convective cloud/freezing rain, transparent and heavy. Small droplets freeze immediately: rime, rough white opaque and often stratiform cloud. Mixed ice combines both. Hoar frost forms by direct vapour deposition onto a cold surface.
- Carburettor icing differs: venturi expansion and fuel vaporisation cool the intake; possible at OAT +15 to −10°C, including clear air/no precipitation. Remove all ice/frost before departure.

### Thunderstorms and mountain hazards

- Thunderstorm is associated with Cb, electrical discharge, turbulence, icing, wind gusts, heavy rain and poor visibility. Lightning may be intra-cloud, cloud-to-cloud or cloud-to-ground.
- Thermal/convective storms: surface heating destabilises warm humid air; advective storms form as cold moist air moves over warmer surface; frontal storms can be embedded in cold fronts; orographic storms are triggered by terrain lifting. Squall lines and supercells are more organised severe variants (**Beyond question bank**: recognition only, no penetration tactics).
- Life cycle: cumulus stage updrafts; mature stage simultaneous strong up/downdrafts and precipitation; dissipating stage downdrafts. Cold outflow forms gust front; microbursts create exceptionally strong near-ground shear (**Beyond question bank:** severe hazard in take-off/landing path).
- Light turbulence can occur below Cu from thermals. Showers near airfield indicate possible strong wind shear; cold downdrafts, gust fronts and terrain/inversions may cause rapid changes.
- Foehn: stable cross-ridge air gives windward layered cloud/poor visibility/rain and descending warm dry lee wind; lenticular cloud marks standing wave, rotor cloud marks severe turbulence. In unstable humid air, forced windward lift may make embedded Cb, showers and hail. In lee-side valley, wind may change by 180°.

## Chapter 13 — Weather reports, charts and practical flight planning

### Aviation messages and charts

- METAR is an aerodrome observation; TAF is a terminal forecast. Decode station/time, wind, visibility, weather, cloud, temperature/dew point, pressure and trend. The full example and tested abbreviations are in the cheat sheet.
- GAFOR (General Aviation Forecast) is a regional VFR product based on ceiling/cloud height and visibility, classified open/difficult/marginal/closed. Belgian lesson: seven zones, six-hour forecast divided into two-hour periods.
- Surface chart shows isobars, pressure centres and fronts. Upper-air charts show isohypses/height contours for pressure levels (925, 850, 700, 500, 300 hPa, etc.) and may include temperature, relative humidity, geopotential height and wind. SWC/LLSWC depicts significant hazards such as cloud, icing, freezing level, turbulence, CB, fronts and precipitation forecast; LLSWC does not show radar echoes.
- Ground-based radar shows current precipitation position/intensity; colour intensity commonly green-yellow-orange-red. A composite combines local radar images. Echo reflectivity relates to size/nature of particles. It does not show all clouds or prove clear air is safe.
- Satellite: visible/HRV shows cloud shape/coverage (daylight); IR shows cloud-top temperature and is available at night; RGB composites distinguish cloud type/height more readily. Satellite is an overview, not direct turbulence/visibility measurement.
- SIGMET warns of significant en-route hazards in an FIR/UIR. ATIS provides current aerodrome weather and operational information (runway in use, transition level). VOLMET broadcasts meteorological information; PIREP/AIREP is an aircraft report. NWP model guidance helps visualize forecast hazards on route, not actual current destination visibility/cloud.
- GAMET (**Beyond question bank**) is low-level area forecast; exact content/levels vary by national product, so use issuing authority legend.

### Practical planning sequence (course method)

1. Begin several days ahead with medium-range models and check forecast consistency rather than trusting one run.
2. Day before: assess broad synoptic setup, likely fronts/airmass, pressure evolution and route/altitude viability; make initial go/no-go.
3. Flight day: surface pressure analysis/front positions; observations (METAR, satellite, radar); forecasts (TAF, pressure/front maps, significant-weather charts); wind/icing/turbulence/cloud-base visibility along the route.
4. Compare the planned route and altitude/time against each hazard's location and validity. Account for alternates and realistic escape options.
5. Update with ATIS/official information before arrival; continue observing actual changes. Do not rely on radar alone or extrapolate an airport forecast to a whole route.

**Teacher's practical caution:** radar can be misread (onset of instability, snow at altitude, low stratus precipitation, deflection/clutter at inversions). Use it as support/confirmation with ground observations and other products, not as sole evidence of safe conditions.

## Lesson test corrections and bank reconciliation

The teacher's 2025–26 comments explicitly flag these frequent mistakes:

1. Ground inversion = nocturnal radiational cooling under clear sky, near surface. Subsidence inversion = large-scale sinking in high pressure and may descend gradually. Frontal inversion = warm air in frontal zone; height depends on position relative to front.
2. QNH is MSL pressure reduced by ISA; QFF is MSL pressure reduced using actual meteorological conditions.
3. Ground altimeter check: QNH → field elevation; QFE → zero at its datum.
4. Air-mass nature begins in source region but changes along track.
5. Warm-front sequence: high clouds first then middle then low (Ci → Cs → As → Sc/St/Ns).
6. Pressure: falls before warm front; roughly steady in warm sector; rises behind cold front.
7. Polar-front low motion: parallel to warm-sector isobars; strongest pressure falls/isallobars help with movement direction.
8. Cold air in upper troposphere: pressure-level height decreases and contours crowd closer.

The 143-bank key also fixes the intended answers for FL180 ≈500 hPa, the FL85/QNH983/ISA−10 true-altitude example = 7300 ft under its rough method, warm- and cold-front passage wind veering, Q117's katabatic wording, Mistral channelling, Bora as cold NE Adriatic wind, orange/red radar = showers/hail/graupel, composite radar, and LLSWC not containing radar echoes. The quick sheet reproduces these. Where a physical approximation is underspecified (especially true altitude), use the exam's supplied rule/table and the bank's keyed nearest option.

## Beyond the question bank — useful context

- **Forecast products are time- and area-bounded.** Check issue time, validity, altitude band, amendments and the route intersection; a forecast symbol outside your time window is not a current observation.
- **More than one mechanism can create the same cloud.** Cloud appearance tells structure; synoptic context (front, terrain, heating, stability) explains why and helps predict change.
- **Hazards compound.** A low ceiling plus crosswind, gust front, icing and terrain can be much more restrictive than any single field. Apply the school's/authority's operating minima and aircraft POH, not just theory answers.
- **Sources used:** Belgian course PDFs 1–13, “Toets PPL25_26_commentaar”, “Case Study Storm Goretti”, the ECQB METEO question-bank presentation, student's `Notes.md` meteorology formulas, and the complete 143-question `30_Meteorology.md` bank. The presentation's 83 slides are principally question-bank screenshot/answer slides; the searchable text carries only its titles/section labels, so its unique image-only question wording cannot be independently transcribed from the text extraction. The existing repo bank remains the complete question-level coverage source.
