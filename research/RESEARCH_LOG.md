# Research log

## 2026-09-28 — initial pass

- Created research protocol, source confidence model and coverage index.
- Established initial source set: official site/blog, official Path of the Ocean/Diplomacy/2025 balance/2.16.3 pages, official asset guidance, Steam/Nintendo, community wiki, developer Steam comment.
- Seeded core mechanics: modes, map sizes, city economy/capacity, tech-cost formula, regular land-unit table, AI difficulty, Explorer move change.
- Seeded complete tribe + skin name catalogue.
- Seeded high-impact update timeline: Diplomacy, Path of the Ocean, 2025 balance, 2025 Cymanti rework, 2.16.3.
- Added CI validator for research metadata.
- Next priority: exact tech tree/unlocks; complete unit stats/skills; combat and movement formulas; city population thresholds; terrain/resources/buildings; special-tribe specs; detailed AI behavior.


## 2026-09-28 — mechanics pass 2

- Added explicit combat damage formula, defence multipliers, healing and retaliation notes.
- Added movement/ZOC/roads/bridge/port transformation rules and a unit-skill semantics glossary.
- Added regular technology-tree skeleton and confirmed unlock examples.
- Added resource/economic building seed table, population upgrade threshold, monuments/tasks, ruin rewards and score model.
- Recorded a live conflict in public Market documentation instead of guessing which formula is current.
- Confirmed older Explorer wiki text is stale against official 2.16.3 (15 -> 12 moves).
- Next: complete every tech unlock/cost/action; full naval + special unit stats; all special tribes; exact diplomacy/embassy formula; map generator spawn rates; current Market behavior.


## 2026-09-29 — multiplayer/UI pass

- Added a dedicated multiplayer/UI/turn-flow note and moved those coverage areas from todo to partial.
- Confirmed developer-described Live Game timing intent and the 24-hour asynchronous alternative; recorded 2024 bot-animation timer consumption as historical/current-unverified.
- Added 2026 official evidence that Weekly Challenges can override ordinary seeded starts with custom armies, technologies, and resource constraints.
- Confirmed current in-game tournament path (Multiplayer > Tournaments) and retained replay/spectator evidence.
- Did not record an exact Live timer formula because sufficiently strong current first-party evidence was not found.
- Next: multiplayer setup matrix, timeout/skip/kick/reconnect behavior, ordinary turn sequencing, replay/spectator controls, and AI black-box behavior.


## 2026-09-29 — forced-spawn research

- Located a developer Steam explanation of forced-spawn push direction and fallback ordering.
- Cross-checked it against the current Movement wiki and recent community reports.
- Found an internal wiki conflict about Creep versus zone of control; current-build verification is still needed.
