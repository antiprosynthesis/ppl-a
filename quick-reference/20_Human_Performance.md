# Human Performance & Limitations — Exam Cheat Sheet

A complete revision sheet for the supplied 60-question HPL bank. **Bank answers take precedence** where a lesson source differs; discrepancies are flagged. Use the `Q` references to audit coverage.

## 1. Atmosphere, altitude and gas laws

### Composition and pressure

| Exam fact | Answer / use |
|---|---|
| Oxygen in the atmosphere | **21%** at 6,000 ft and throughout ordinary flight altitudes (Q1). The fraction is essentially constant; pressure and oxygen partial pressure fall with altitude. |
| Nitrogen | About **78%**. |
| Other gases | About **1%** (Q2). |
| MSL standard pressure | Approximately **1,013 hPa** (lesson: 1,013.25 hPa). |
| Pressure half MSL value | Approximately **18,000 ft** (Q3). |
| Body usually starts reacting to falling pressure | About **7,000 ft** (Q4). |
| Lower limit beyond which the body cannot completely compensate | About **12,000 ft** (Q45). |

**Key distinction:** percentage of O₂ stays ~21%, but lower total pressure means lower partial pressure of O₂, so less oxygen moves into the blood. Never answer “12% oxygen at 6,000 ft.”

### Gas laws — formula, how to use, worked example

| Law | Relationship | HOW TO USE / worked example |
|---|---|---|
| **Boyle** (constant temperature) | `P₁V₁ = P₂V₂` | For a fixed gas mass, pressure and volume vary inversely. At ~18,000 ft pressure is about half MSL, so a 1 L gas volume expands to about 2 L. Relevant to trapped gas in ears, sinuses, gut, teeth and gas spaces. |
| **Charles** (constant pressure) | `V₁/T₁ = V₂/T₂` | Use **absolute temperature (K)**. Example: 3.0 L at 300 K becomes `3.0 × 330/300 = 3.3 L` at 330 K, if pressure is unchanged. |
| **Combined gas law** | `P₁V₁/T₁ = P₂V₂/T₂` | Use when pressure, volume and temperature all change; convert temperatures to kelvin first. Example: at constant temperature with pressure halved, volume doubles (Boyle case). |
| **Dalton** (gas mixture) | `Ptotal = Σ partial pressures`; `pO₂ ≈ 0.21 × Ptotal` | Multiply total pressure by the oxygen fraction to get oxygen partial pressure. At 1,013 hPa: `0.21 × 1,013 ≈ 213 hPa`; at half pressure (~507 hPa): `≈106 hPa`. The fraction remains 21%, but pO₂ halves. |
| **Henry** (gas dissolved in liquid) | Dissolved gas amount is proportional to its partial pressure at equilibrium. | As pressure falls, dissolved nitrogen can come out of solution as bubbles. This explains decompression sickness after diving / rapid pressure reduction; there is no simple bank calculation. |

### Other standard-atmosphere lesson values — beyond the question bank

- Sea-level ISA: **15°C**, **1,013.25 hPa**, density **1.225 kg/m³**.
- Approximate ISA temperature lapse: **0.65°C per 100 m** (about 2°C per 1,000 ft in the lesson); tropopause about **11 km**, around **−56.5°C**.
- These are lesson reference values, not additional answers to the bank questions.

## 2. Oxygen, blood and hypoxia

### Hypoxia (zuurstoftekort)

**Definition:** inadequate oxygen available to body tissues. The exam’s altitude mechanism is falling atmospheric pressure → falling oxygen partial pressure. Hypoxia may be insidious: judgement and self-awareness can be impaired before the pilot recognizes the problem.

| Hypoxia type | Main cause | Example / distinction |
|---|---|---|
| **Hypoxic / hypobaric** | Low oxygen partial pressure at altitude | High altitude; oxygen fraction in air is still 21%. |
| **Anaemic** | Blood cannot carry enough oxygen | **Carbon monoxide (CO)** binds haemoglobin; blood loss/anaemia can also reduce carrying capacity (Q5). |
| **Stagnant / circulatory** | Blood flow/oxygen delivery is inadequate | Lesson concept; e.g. high positive G can reduce blood reaching the brain. |
| **Histotoxic** | Cells cannot use delivered oxygen normally | Lesson concept; some poisons / alcohol can impair cellular use. |

**Symptoms and tested clues:** impaired judgement, reduced concentration / responsiveness, fatigue or drowsiness, headache, euphoria, visual impairment, and in more severe cases blue lips/fingernails (**cyanosis**, Q8). **Vision is the sense most affected by hypoxia** (Q44). Not every person experiences the same symptoms, and the pilot may not notice their own impairment.

**Threshold answers to memorise:** the body usually reacts from **7,000 ft**; it cannot fully compensate from about **12,000 ft**; pressure is roughly half at **18,000 ft**. Do not mix these three separate questions (Q3, Q4, Q45).

### Oxygen transport and blood-cell roles

| Component | Primary function | Memory hook |
|---|---|---|
| Red blood cells / erythrocytes | Carry oxygen (via haemoglobin) (Q46) | **Red = respiratory transport** |
| White blood cells / leucocytes | Immune defence (Q48) | **White = ward off infection** |
| Platelets / thrombocytes | Blood clotting / coagulation (Q47, Q49) | **Platelets plug** |

### Carbon monoxide (CO) poisoning

- CO is produced by incomplete combustion; the bank specifically tests **a cracked cabin-heater heat exchanger** (Q6) and **smoking** (Q7).
- CO binds haemoglobin and impairs oxygen transport; it is odourless and dangerous. Headache, nausea, dizziness, drowsiness or confusion may occur.
- **Exam answer:** anaemic hypoxia can be caused by CO poisoning. Do not select CO as a hypoxic-altitude cause.
- Suspected CO in flight: heater off, fresh air / oxygen as appropriate, land promptly and obtain medical attention. Follow aircraft procedure.

### Hypoxia vs hyperventilation: recognize and act

| Feature | Hypoxia | Hyperventilation (overbreathing) |
|---|---|---|
| Basic problem | Insufficient oxygen reaching tissues | Excess ventilation removes too much CO₂; blood chemistry changes |
| Typical clues | Altitude exposure; poor judgement / vision, drowsiness, possible cyanosis | Tingling, dizziness, muscle spasm, possible altered consciousness |
| Cyanosis? | May occur; blue lips/nails are a bank hypoxia clue | **No** — cyanosis is the “NOT a symptom” answer (Q9) |
| First priority | Suspect it early; use oxygen if available and descend | Calm, slow breathing; reduce stress. If uncertain, do not assume it is only hyperventilation—treat possible hypoxia first. |

```text
Symptoms in flight
       |
       +-- altitude / visual or judgement change? --> suspect HYPOXIA
       |       oxygen as appropriate + descend + land / medical help
       |
       +-- rapid breathing + tingling / spasm? ------> consider HYPERVENTILATION
               slow, controlled breathing; check oxygenation / altitude first
```

### Decompression sickness (DCS, caisson sickness)

- Falling pressure can release dissolved nitrogen as bubbles (Henry’s law). Diving before flight loads tissues with extra nitrogen; ascent / cabin altitude can then promote bubble formation.
- “Bends” = joint / limb pain; “creeps” = itchy skin; “chokes” = breathing problems. Neurological or circulatory symptoms are serious.
- **Scuba diving prior to flight is a DCS risk factor (Q56).** Diving is **not** the “risk factor for hypoxia” answer in Q50. Keep the two conditions separate.
- If suspected: oxygen, descend if safe, land and seek urgent medical help; do not rub painful joints. Avoid flying after diving and follow current approved waiting guidance.

### Pressure-related ear / sinus problems

- Middle ear connects with the nose/throat by the **Eustachian tube (buis van Eustachius)** (Q15).
- Equalisation is impossible when that tube is **blocked** (Q22); a cold can make descent painful and may cause vertigo / barotrauma.
- Swallowing, yawning or gentle equalisation may help. Severe cold / blocked ears or sinuses: do not fly; never force a manoeuvre through severe pain.

## 3. G-forces and acceleration

| Effect | Cause / recognition |
|---|---|
| **Grey-out** | Positive G; colour vision / peripheral vision fade as blood is displaced away from the head (Q10). |
| **Black-out** | More severe / sustained positive G; vision lost, possibly followed by loss of consciousness. |
| **Red-out** | “Red vision” during negative G (Q43). |

**Lesson limits (not asked numerically in this bank):** sustained >1 second: about **+3.5 G / −3 G** tolerance in an unprotected person; **+7 to +8 G** with anti-G protection in the cited lesson. Very brief impact tolerance is listed as 25 G vertical / 45 G perpendicular to vertical; this is not a flying target or operating limit.

**Turn-load formula (lesson):** `n = Lift/Weight`; in a coordinated level turn `n = 1/cos(bank angle)`. **HOW TO USE:** enter bank angle, take cosine, divide 1 by it. **Worked example:** at 60° bank, `cos 60° = 0.5`, so `n = 1/0.5 = 2 G`. Avoid unnecessary steep turns; respond to G symptoms by reducing load.

## 4. Nervous system, senses and vision

### Nervous system and reflex

- **Autonomic nervous system** (autonoom zenuwstelsel) regulates involuntary functions such as breathing, digestion and heart rate (Q11).
- **Reflex:** involuntary, stereotyped response to receptor stimulation (Q51).
- Central nervous system = brain and spinal cord; peripheral nervous system carries signals to / from the body. Hypoxia, alcohol, fatigue, stress and medication impair function.

### Eye and visual perception

| Structure / concept | Function / exam fact |
|---|---|
| **Cones** | Colour and sharp central/day vision (Q12). |
| **Rods** | Dim-light / night and peripheral vision; poor colour/detail. |
| Blind spot | Optic nerve / vessels pass through; no visual receptors there. |
| Retina | Light-sensitive surface; the brain interprets the image. |
| Iris | Controls pupil size and incoming light (supplemental lesson question). |
| Central vision | Fine detail; peripheral vision helps detect motion and orientation. |

- **Parallax error:** wrong instrument reading caused by viewing angle (Q13). View a scale straight-on; align the pointer/mark with its scale.
- Choose **non-polarised** pilot sunglasses (Q14): polarisation can obscure LCD / instrument displays or interfere with viewing other cockpit displays. Use suitable UV protection; do not choose “no UV filter.”
- Brain interpretation, not “bad eyes,” causes most visual illusions (Q18).
- Night vision relies on rods; allow time for dark adaptation, avoid bright light and use a deliberate scan. Lesson notes discuss a blind-spot method: look slightly to one side of a faint object rather than staring directly at it.

## 5. Ear, vestibular system and spatial disorientation

### The balance organs

- **Semicircular canals** detect angular / rotational acceleration (turning).
- **Otolith organs** detect linear acceleration and gravity / tilt.
- The inner ear can be fooled: in poor visual reference, trust flight instruments over bodily sensation.

### Illusions to recognize

| Illusion / trigger | What the pilot may feel | Exam action / memory |
|---|---|---|
| **Leans**: slow roll below vestibular detection threshold; then a correction | Aircraft seems to be banking the opposite way | Prolonged turn then wings level can feel like turning opposite direction (Q19, Q52). Trust instruments. |
| **Somatogravic**: acceleration in straight, level flight | Nose-up / climb illusion (Q17); deceleration can feel like descent | **Accelerate = climb; decelerate = descend.** |
| **Coriolis / vertigo**: move head during a turn | Strong tumbling / disorientation | Vertigo most likely when moving the head **during a turn** (Q16). Keep head still in turns. |
| **Motion sickness**: sensory mismatch, turbulence, alcohol, head movement | Nausea, pallor, sweating, dizziness | Non-accelerated straight-and-level flight does **not** stimulate it (Q53). |
| **Visual horizon / false horizon** | False bank or pitch cue | Cross-check instruments. |
| **Autokinesis** (lesson) | A fixed light in darkness seems to move | Avoid staring at a single light; maintain references / scan. |

**Disorientation response:** recognize the mismatch → stop manoeuvring / minimize head movement → fly attitude and wings from instruments → ask for help if needed → continue only when stable. Never “correct” toward a false sensation.

## 6. Runway / approach visual illusions

The **brain misinterprets** visual geometry. Maintain the published / planned approach path, airspeed and procedures; do not chase an illusion.

| Visual cue | Typical perception / tendency |
|---|---|
| Upslope runway | Appears higher / too high; pilot may descend below the normal glide slope (Q54). The bank’s separate impression question expects **overshoot** (Q21). See trap below. |
| Downslope runway | Can appear lower / too low, encouraging a higher approach (lesson). |
| Narrow runway | Can seem too high / too close; tendency to fly low (lesson). |
| Wide runway | Can seem too low / too far; tendency to fly high and overshoot (lesson). |

**Bank wording trap:** Q21 asks what impression may be caused by an upslope and its marked answer is **an overshoot**; Q54 gives the detailed misperception as “approach too high” and descent below the regular glide slope. These wordings do not align intuitively. Memorize both bank-marked answers, report the discrepancy to an instructor, and in real flight follow stabilized-approach criteria—not the illusion.

## 7. Health, fitness and substances

### Medical / fitness factors

- Being **overweight** is a tested risk factor for diabetes (Q23, Q55).
- **Blood alcohol decreases by about 0.01% per hour on average** (Q24). This is an approximate metabolism fact, **not** permission to fly or a reliable individual “safe to fly” calculation.
- **Worked calculation:** If a question starts at 0.08% and asks for an estimate after 3 hours, use `0.08 − (3 × 0.01) = 0.05%`. Do not use this arithmetic to make an operational fitness decision.
- Smoking increases CO exposure, reduces effective oxygen transport and can worsen night vision / hypoxia susceptibility (lesson).
- Fatigue, illness, dehydration, stress, emotional upset and impairing medication can reduce attention, judgement, memory and situational awareness.
- **I’M SAFE:** Illness, Medication, Stress, Alcohol, Fatigue, Emotion. If unfit or uncertain, do not fly; seek advice / reassess.

### Alcohol conflict in lesson sources

The supplied book and slide deck differ on an old classroom “bottle-to-throttle” interval (24 h in one; 12 h in another). Neither replaces current rules, medical advice or the bank fact of **0.01% per hour**. Ask the school which current rule it teaches; never infer fitness from the metabolism formula alone.

## 8. Memory and information processing

- **Short-term memory:** for the supplied bank, approximately **5 ± 2 items** for **10–20 seconds** (Q25, Q26). Use the bank answer even though a supplementary ECQB excerpt says 7 ± 2 items and the lesson describes short-term capacity / duration differently. **Discrepancy flagged** in notes.
- **Working memory** actively holds and manipulates information; checklists, written notes, readbacks and chunking reduce load.
- Long-term memory stores learned knowledge and experience; repetition and meaningful / intense events support encoding.
- Attention is selective: task fixation and confirmation bias can cause important cues to be missed.

### Biases and error concepts

| Term | Meaning / response |
|---|---|
| **Confirmation bias** | Prefer information that supports your existing mental model; actively seek disconfirming evidence (Q28). |
| Expectation bias | Seeing what you expect rather than what is actually there; can cause human error (Q29). Pause, verify, cross-check. |
| **Swiss-cheese model** | Accident/error chain occurs when holes in multiple defences line up (Q30). Use independent layers: planning, procedures, checks, monitoring, communication. |
| **Latent error** | Hidden weakness / error remaining undetected in the system for a long time (Q31). |
| Active error | Immediate action / slip at the controls; distinguish from latent condition. |
| **Complacency** | Reduced vigilance, particularly with increased cockpit automation (Q37). Monitor automation and verify outputs. |
| **Human error** | Most accidents in this question bank are attributed to human error (Q27); errors are predictable, not proof of bad intent. Build barriers and report / learn. |

## 9. Situation awareness, problem solving and communication

- **Situational awareness (SA):** ongoing monitoring / understanding of the current flight situation (Q34): perceive cues → understand what they mean → anticipate what happens next.
- In a problem, first **fly the aeroplane and keep it stable**, then address the problem while continuing to fly (Q33). Prioritize control, then navigate / communicate / troubleshoot as appropriate.
- Use checklists, verify ambiguous indications and avoid fixation. A checklist reduces omissions; it does not eliminate risk or replace training.
- Radio phraseology provides a shared communication **code** (Q35). Use standard wording, listen actively and read back critical instructions.

```text
Problem or surprise
       ↓
CONTROL — keep aircraft stable
       ↓
ASSESS — identify / prioritize the threat; use checklist
       ↓
ACT — simplest safe action; navigate / communicate as needed
       ↓
RECHECK — did it work? update SA and plan
```

## 10. Risk, attitude, teamwork and stress

### Risk management

Four appropriate ways to handle risk: **Avoid, Reduce, Transfer, Accept** (Q57).

1. **Avoid:** do not launch / change route or plan to remove the risk.
2. **Reduce:** add controls, margins, training or safeguards.
3. **Transfer:** pass / share the exposure or responsibility where appropriate (does not remove pilot accountability).
4. **Accept:** consciously accept only a residual risk within limits.

Do not confuse “accept” with ignoring risk. Group dynamics can increase risk acceptance: the **risky shift** is a tendency to accept higher risks in a group (Q32, Q58). Use an independent go/no-go standard.

### Dangerous attitudes and antidotes

| Attitude | Self-talk / behaviour | Antidote |
|---|---|---|
| Anti-authority | “Rules don’t apply to me.” | Rules have reasons; follow them. |
| Impulsivity | “Do it now.” | Pause; think before acting. |
| Invulnerability | “It won’t happen to me.” | It can happen to me too; use margins. |
| Macho | “I can prove myself / impress them.” | Why take an unnecessary risk? **Macho + invulnerability commonly combine** (Q39, Q59). |
| Resignation / self-abandonment | “Nothing I do matters.” | There is usually something useful to do; keep thinking and act. |

A bank question identifies risky manoeuvres to impress spectators as **macho** (Q38). The bank’s preferred trait pairing is **extroverted–stable** (Q36); treat this as a test response, not a diagnosis of individuals.

### Stress and performance

- Some arousal can improve alertness; too little or too much reduces performance. The optimum is **point B** (Q40); **point D** is overstrained (Q42).
- Stress may arise when a problem appears to have **no solution** (Q60). It affects **attention, concentration, responsiveness and memory—all four** (Q41).
- Training / experience can affect coping; people do not all react identically. Stress symptoms matter to safety.

```text
Performance
   ^                  B = ideal (moderate arousal)
   |                /\
   |              /    \         D = overstrained / too much
   |            /        \       performance falls
   |__________/____________\________________> arousal / stress
          too little
```

## 11. Passenger discomfort and routine handling

During cruise, if a passenger suddenly feels uncomfortable: **adjust cabin temperature and avoid excessive banking** (Q20). Keep the aircraft stable, communicate calmly and assess for a medical issue; do not automatically increase speed or provide oxygen unless indicated.

## 12. Quick memory hooks

- **“21 stays; partial pressure pays”** — oxygen fraction remains 21%; available pO₂ falls with total pressure.
- **7–12–18 ladder:** body reacts ~7,000 ft → compensation incomplete ~12,000 ft → pressure half ~18,000 ft.
- **R-W-P:** red cells carry O₂; white cells defend; platelets plug.
- **CO = Carrying capacity compromised** (anaemic hypoxia); heater exchanger crack / smoking.
- **Cones = colour; rods = dark.**
- **Accelerate up, decelerate down** (somatogravic pitch illusion).
- **Turn + head movement = Coriolis / vertigo.**
- **A-B-C before action:** Aviate, then assess / navigate, then communicate / troubleshoot; first keep the aircraft stable.
- **A-R-T-A:** Avoid, Reduce, Transfer, Accept risk.
- **I’M SAFE:** check the pilot before checking out the aircraft.

## 13. Bank cross-check: every supplied question

| Q | Answer fact covered above |
|---:|---|
| 1 | Air contains 21% oxygen at 6,000 ft. |
| 2 | Other gases approximately 1%. |
| 3 | Pressure halves around 18,000 ft. |
| 4 | Body usually reacts from 7,000 ft. |
| 5 | Anaemic hypoxia: CO poisoning. |
| 6 | Cracked heat exchanger can cause CO poisoning. |
| 7 | Smoking can cause CO exposure / poisoning. |
| 8 | Hypoxia clue: blue lips / fingernails. |
| 9 | Cyanosis is NOT a hyperventilation symptom. |
| 10 | Grey-out: positive G. |
| 11 | Autonomic nervous system controls involuntary functions. |
| 12 | Cones are responsible for colour vision. |
| 13 | Parallax: instrument misread due to viewing angle. |
| 14 | Pilot sunglasses should be non-polarised. |
| 15 | Middle ear connects through Eustachian tube. |
| 16 | Vertigo most likely with head movement during turn. |
| 17 | Straight-flight acceleration can feel like a climb. |
| 18 | Visual illusions mainly reflect brain misinterpretation. |
| 19 | Wings level after prolonged turn may feel like opposite turn. |
| 20 | Passenger discomfort: adjust temperature; avoid excessive bank. |
| 21 | Upslope runway impression: bank answer = overshoot (wording flagged). |
| 22 | Blocked Eustachian tube prevents pressure compensation. |
| 23 | Overweight is diabetes risk factor. |
| 24 | Blood alcohol falls about 0.01% per hour. |
| 25 | Short-term memory about 10–20 seconds. |
| 26 | Bank answer: 5 ± 2 items for 10–20 seconds (conflict flagged). |
| 27 | Majority of aviation accidents: human error. |
| 28 | Confirmation bias favours own mental model. |
| 29 | Expectation bias can lead to human error. |
| 30 | Swiss-cheese model explains error chain. |
| 31 | Latent error remains undetected in system for long time. |
| 32 | Group dynamics make higher risk acceptance more likely. |
| 33 | Keep aircraft stable / fly first, then solve problem. |
| 34 | Ongoing monitoring of flight situation = situational awareness. |
| 35 | Radio phraseology helps ensure same communication code. |
| 36 | Bank’s best trait combination: extroverted–stable. |
| 37 | Increased cockpit automation can cause complacency. |
| 38 | Risky manoeuvres to impress = macho attitude. |
| 39 | Macho and invulnerability commonly combine. |
| 40 | Ideal arousal / stress point = B. |
| 41 | Stress affects attention, concentration, responsiveness and memory. |
| 42 | Overstrained point = D. |
| 43 | Red-out = red vision under negative G. |
| 44 | Hypoxia most influences vision. |
| 45 | Compensation incomplete from about 12,000 ft. |
| 46 | Red cells / erythrocytes transport oxygen. |
| 47 | Thrombocytes responsible for blood coagulation. |
| 48 | Leucocytes provide immune defence. |
| 49 | Platelets / thrombocytes clot blood. |
| 50 | Diving is NOT the hypoxia risk answer; it is a DCS risk. |
| 51 | Reflex = involuntary stereotyped response to receptor stimulus. |
| 52 | Wings level after long turn may feel like turn opposite direction. |
| 53 | Non-accelerated straight-and-level flight does not stimulate motion sickness. |
| 54 | Upslope: perceived too high; descent below regular glide slope. |
| 55 | Overweight is diabetes risk factor. |
| 56 | Scuba diving before flight is DCS risk factor. |
| 57 | Risk handling: avoid, reduce, transfer, accept. |
| 58 | Risky shift = groups tend to accept higher risk. |
| 59 | Dangerous attitudes often combined: macho and invulnerability. |
| 60 | Stress can occur when a problem seems to have no solution. |

**Coverage result:** all 60 supplied bank questions have an answer fact or explicit discrepancy note above. No question was left uncovered.
