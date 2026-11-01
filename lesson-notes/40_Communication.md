# 40 Communication / Radiotelephony — Lesson Notes

Sources: APCK course "Communicatie" (Johan De Boeck), UK CAA CAP 413 Radiotelephony Manual, ECQB bank. Items marked **(beyond question bank)** are not tested by the 82 bank questions but are useful for real flying/oral exams. ⚠ = lesson/manual vs bank difference.

## 1. Radio basics
* Radio signals = electromagnetic waves travelling at the speed of light, **300,000 km/s** (300,000,000 m/s).
* The field strength is a sine wave; one full cycle = one **wavelength (λ)**. Frequency = c / λ. Example: λ = 100 m → 3,000,000 Hz = 3,000 kHz = 3 MHz.
* **VHF = 30–300 MHz** (λ = 10–1 m). The aviation voice band **118.000–136.975 MHz** is VHF; frequencies are in **MHz** (118.75 MHz), never kHz (kHz ≈ LF/MF NDBs).
* **AM** (amplitude modulation): same wavelength, varying amplitude; lower quality but "good enough" and retained in aviation. **FM**: constant amplitude, varying frequency; better sound quality **(beyond question bank)**.
* **Simplex**: only one party transmits at a time (push-to-talk). If two transmit together → garbled; ATC says "two stations calling together". *Teacher tip:* after a frequency change wait a moment — listen before you press PTT.
* **VHF is line-of-sight**: range depends on **altitude** (also terrain). HF/NDB phenomena (shoreline effect, twilight/night error, ionosphere height) do not affect VHF → Q82.
* **Range formula:** NM = 1.23 × √(height ft AGL) + 10 %.
  * 10,000 ft AGL: 123 + 12.3 = 135.3 NM. 6,400 ft: 98.4 + 9.8 = 108.2 NM.
  * Flying higher gives longer range and better quality (and better emergency options). Weather ducting can occasionally let you hear stations very far away (lesson anecdote: Marseille).
  * **(beyond)** True line-of-sight uses both antenna heights: 1.23(√h_aircraft + √h_station).
* **(beyond)** Cockpit hardware (lesson photos): audio panel (KMA 26: COM1/COM2/NAV1… selector, intercom volume/VOX, MIC selection, speaker), and COMM/NAV radios with **active ↔ standby** frequency swap button; the pull-test/volume knob. Remember to set squelch/volume, select the right COM on the audio panel, and check headset when "no reception".

## 2. Alphabet, numbers, time
* ICAO alphabet: Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India **Juliett** Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray **Yankee** Zulu.
* Digits: zero, wun, too, tree, fower, fife, six, seven, ait, niner; "decimal", "hundred", "tousand".
* Rules:
  * Altitudes, heights, cloud ceilings, RVR: digit + hundred/tousand → 4500 ft "four tousand five hundred".
  * Headings, bearings, wind direction: 3 separate digits → 285 = "two eight five".
  * Flight level: separate digits.
  * Frequencies: digit by digit, trailing zeros dropped → 119.500 = "one one niner decimal five". **(beyond)** Radios show 6-digit 8.33 kHz channel names; read the digits shown (e.g. 118.725 = "one one eight decimal seven two five").
  * Time: **UTC**, four digits individually: 1620 = "one six two zero". (Minutes only, e.g. "two zero", is used in practice when there is no ambiguity, but the exam asks for the unambiguous full form.)
  * Clock positions: "twelve o'clock".
  * **Visibility**: below/up to 5 km in **metres**; above 5 km in **km**; 10 km or more = "one-zero kilometres or more".
* **(beyond)** Local time, daylight saving: always convert to UTC before transmitting. Belgian summer time = UTC+2, winter UTC+1.

## 3. Phraseology
| Word | Meaning |
|---|---|
| Roger | Received all of your last transmission (not "yes", not "will comply") |
| Wilco | Understood, will comply |
| Affirm / Negative | Yes / No |
| Approved | Permission for proposed action granted |
| Correction | An error was made, correct version is… |
| Say again, Standby, Monitor, Request | repeat; wait (neither approval nor denial); listen out on freq; ask permission/info |
| Ready for departure | I'm ready for take-off (not "ready for start-up", not "request take-off") |
| Going around | Go-around announced |
| How do you read? | Readability check |

* Call-up format: **"<station called>, <own call sign>"**, e.g. "Dusseldorf Tower, D-EAZF" — never "over", "from", "is calling". *Teacher tip:* "who you call, who you are, what you want."
* Call-sign words: **Tower** (aerodrome control), **Ground** (surface movement), **Information** (FIS), Approach, Radar, Departure, Delivery.
* Own call sign: full at first contact; abbreviated (first character + last two) **only when the ground station has done so first** (D-EAZF → "DZF"; HB-YKM → "HKM").
* Request to cross controlled airspace: **"Request"** (not want/would like/apply).

## 4. Readback and acknowledgement
* **Read back** (and end with call sign): runway in use, clearances (take-off, landing, line-up, crossing, entering/leaving airspace), altitudes/levels, headings, speeds, altimeter settings, SSR codes, frequencies, taxi/hold-short instructions.
* **Do NOT read back:** wind, traffic information (answer "Roger" or "Traffic in sight" **(beyond)**).
* Answers by instruction type:
  * Pure info ("You are now entering airspace Delta") → **Roger**.
  * Instruction without readback item ("Next report PAH") → **Wilco**.
  * Frequency change ("Call Hamburg Tower on 121.275") → **121.275**.
  * "Squawk 4321, call Bremen Radar 131.325" → **"Squawk 4321, 131.325"**.
  * Long clearance with wind: read back runway, headings, altitudes, clearance — omit wind (Q44: "DZF after lift-off climb straight ahead 2500 feet, then turn right heading 220, runway 12, cleared for take-off").
* **Leaving a control frequency** (except at final parking) needs **approval** from the controller — don't change on your own.

## 5. Readability scale
1 Unreadable · 2 Readable now and then · 3 Readable with difficulty · 4 Readable · 5 Perfectly readable. Radio check: "Borton Tower, G-ABCD, radio check 118.725" → "G-ABCD, readability 5" **(beyond)**.

## 6. Message categories & priority
Annex 10 order: **1 Distress, 2 Urgency, 3 Direction-finding communications, 4 Flight safety messages, 5 Meteorological messages, 6 Flight regularity messages.**
* Distress: grave and imminent threat, immediate assistance. Urgency: safety of aircraft, vehicle or person in sight (not immediate danger). Flight safety = ATC messages. Regularity: operation/maintenance of facilities essential for safety/regularity.
* **(beyond)** Information messages (ATIS, VOLMET) and administrative messages are lower still.

## 7. Distress and urgency
* **MAYDAY ×3** (distress) / **PAN PAN ×3** (urgency). First call on **current frequency** (the one you are already using); 121.500 MHz is the international emergency frequency to use if you have no contact **(beyond; 243.0 MHz UHF military)**.
* Message order: station → call sign → type → nature → intentions → position/level/heading → other info (persons on board, endurance, colour/markings) (CAP 413 adds pilot qualification; **solo students prefix "STUDENT"** **(beyond)**).
* Urgency content in the exam: nature of problem or observation, info useful for support, pilot's intentions, position/heading/altitude.
* Set transponder **7700** (preferably before the call if not already under ATC); if already under ATC you may keep assigned code. Cancel the emergency when no longer needed — **better to declare early and cancel later**. **(beyond)**
* If no reply from the addressed station, other stations must help; others keep radio silence ("Silence MAYDAY") **(beyond)**.
* *Teacher tip:* Aviate – Navigate – Communicate: fly the plane first, then call.

## 8. Transponder special codes
7000 VFR conspicuity (Europe) · **7500** unlawful interference · **7600** radio failure · **7700** emergency. Mnemonic 75-76-77: Hijack – Radio – Emergency. "Squawk ident" = press IDENT **(beyond)**.

## 9. Radio failure and blind transmission
* Checklist: correct frequency/COM selected? station open? out of range? volume/squelch? headset/microphone/PTT? circuit breakers/fuse? try another frequency; use other aircraft as a relay **(beyond)**.
* Squawk **7600**.
* **Transmitting blind**: when you cannot reach the station but have reason to think it hears you. Phrase "TRANSMITTING BLIND", on the **current frequency**, message includes the addressee. Receiver failure: "TRANSMITTING BLIND DUE TO RECEIVER FAILURE" and report at scheduled points.
* ⚠ **Number of repeats:** CAP 413 says transmit **twice** (bank Q31 agrees), but bank Q78 marks **"One time"** as correct. Read the answer list: if "Twice" is available take it; if the choices are Two/Three/Four/One time, take One time.
* **Class D (VFR) radio failure:** continue according to last clearance complying with VFR, **or** leave the airspace by the **shortest route**. Entry with radio failure only with **prior approval**.
* **(beyond)** Speechless code: with a faulty microphone, you can still answer questions by keying the carrier wave (CAP 413 "Speechless Code", chapter 8). Tower light signals are covered in Air Law.

## 10. Q-codes
* QFE: altimeter reads **0 on the aerodrome**; QNH: altitude above MSL; QNE: 1013.25 hPa.
* QDM magnetic **to** station; QDR magnetic **from** station; **QUJ true to**; **QTE true from**.
* Direction-finding request (VDF "Request QDM") has priority above flight safety messages.
* *Teacher tip:* QDM is what you steer (magnetic heading to station, zero wind); QDR = radial you are on.

## 11. Abbreviations (non-ICAO-alphabet ones the teacher highlighted)
ABM abeam · FIS flight information service · FIR flight information region · H24 24 h service · HX no specific hours · OBST obstacle · QDR · QTE · QUJ · VFR visual flight rules. **(beyond)** HJ sunrise–sunset · HN sunset–sunrise · VMC · IMC · SSR · VDF · ATIS · VOLMET · NOTAM · SIGMET.

## 12. Weather information
* METAR cloud: FEW 1–2 oktas · SCT 3–4 · BKN 5–7 · OVC 8 (NSC/ SKC none).
* **VOLMET**: VHF/HF broadcast of **meteorological reports** of several airports. **ATIS**: continuous broadcast about one aerodrome (runway in use, wind, QNH, visibility, cloud, NOTAM info, information letter); **valid 30 minutes** unless a new letter is issued; can be broadcast on a **VOR** frequency (e.g. approach-area VOR). Report "Information Bravo" on first contact **(beyond)**.

## 13. Typical full examples (beyond question bank)
* Departure: "Antwerp Tower, OO-ABC, ready for departure" → "OO-ABC line up runway 29" → "Line up 29, OO-ABC" → "OO-ABC wind 250/10, runway 29 cleared for take-off" → "Runway 29 cleared for take-off, OO-ABC".
* Entering a control zone: "Request transit of Delta airspace" → "OO-ABC cleared…".
* Go-around: "OO-ABC going around."

## 14. Study checklist
1. Phonetic alphabet & digit pronunciation cold.
2. Readability 1–5, priority D-U-D-F-M-R.
3. 7500/7600/7700; QDM/QDR/QUJ/QTE; QFE.
4. Readback list; Roger vs Wilco.
5. Distress vs urgency definitions; initial call on current frequency.
6. Class D radio failure rules; blind transmission wording.
7. FEW/SCT; ATIS 30 min; VOLMET; abbreviations (HX, H24, OBST, ABM).
8. 300,000 km/s; VHF band; range formula.
