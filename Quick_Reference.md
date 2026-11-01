# PPL(A) Quick Reference — Index

The quick reference is split into **nine subject cheat sheets**, built from the question banks, `Notes.md`, the real exam reports and the lesson material (`vakken` folder). Memorise the sheet, then use its HOW-TO-USE lines, worked examples and exam traps to answer any question. Each subject also has detailed lesson notes for understanding.

| Subject | Cheat sheet | Lesson notes |
|---|---|---|
| 10 — Air Law | [Open cheat sheet](quick-reference/10_Air_Law.md) | [Lesson notes](lesson-notes/10_Air_Law.md) |
| 20 — Human Performance | [Open cheat sheet](quick-reference/20_Human_Performance.md) | [Lesson notes](lesson-notes/20_Human_Performance.md) |
| 30 — Meteorology | [Open cheat sheet](quick-reference/30_Meteorology.md) | [Lesson notes](lesson-notes/30_Meteorology.md) |
| 40 — Communication | [Open cheat sheet](quick-reference/40_Communication.md) | [Lesson notes](lesson-notes/40_Communication.md) |
| 51 — Principles of Flight (Aeroplane) | [Open cheat sheet](quick-reference/51_Principles_of_Flight.md) | [Lesson notes](lesson-notes/51_Principles_of_Flight.md) |
| 60 — Operational Procedures | [Open cheat sheet](quick-reference/60_Operational_Procedures.md) | [Lesson notes](lesson-notes/60_Operational_Procedures.md) |
| 70 — Flight Performance and Planning | [Open cheat sheet](quick-reference/70_Flight_Performance_and_Planning.md) | [Lesson notes](lesson-notes/70_Flight_Performance_and_Planning.md) |
| 80 — Aircraft General Knowledge | [Open cheat sheet](quick-reference/80_Aircraft_General_Knowledge.md) | [Lesson notes](lesson-notes/80_Aircraft_General_Knowledge.md) |
| 90 — Navigation | [Open cheat sheet](quick-reference/90_Navigation.md) | [Lesson notes](lesson-notes/90_Navigation.md) |

## Visual flashcards

Open [`flashcards.html`](flashcards.html) in a browser (download it from GitHub first; GitHub does not run HTML pages). It has 1,300+ flip cards across all nine subjects, most with a diagram. Filter by subject and topic, shuffle, and mark cards "Know it" / "Again" (progress is saved in your browser). Keyboard: Space = flip, ←/→ = navigate, 1 = Again, 2 = Know it. The card data lives in `flashcards/*.json`; rebuild the page with `python3 flashcards/build.py`.

## Quiz app

`docs/quiz.html` has all 902 questions. Pick one or more subjects and get 20 random questions. Wrong answers are explained, and the summary shows the score per subject and the sub-topics to re-study. Questions come from `quiz/questions/*.json`, explanations from `quiz/explanations/*.json`; rebuild with `python3 quiz/build.py`.

**Hosting:** after merging to `main`, enable GitHub Pages (Settings → Pages → Deploy from branch → `main` / `/docs`). The quiz is then at `https://jonathanva.github.io/ppl-a/quiz.html`.

**Saving reports:** "Download .md" always works; commit the file to `reports/`. "Save to repo" commits it directly: open ⚙️ in the quiz and paste a fine-grained token (this repo only, Contents: read & write). The token stays in your browser only.

Where the lesson material and the question bank disagree, the sheets follow the bank and flag the difference. These are rapid-recall aids, not substitutes for current regulations, the State AIP, or your aircraft's POH/AFM. Check units, sign conventions, and local procedures before applying a formula or rule.
