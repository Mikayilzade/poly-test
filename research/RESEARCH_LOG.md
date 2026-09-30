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


## 2026-09-29 — easter-egg / hidden-UI pass

- Added a dedicated hidden-behavior note covering Nature Bunny/Bunta, sunrise background, mixed tribes, Elyrion language, the unowned-Luxidoor opponent behavior and the removed floating/sinking-city interaction.
- Kept all of these at community-wiki confidence and explicitly separated historical/current-unverified behavior.
- Added a black-box verification queue for platform differences, trigger timing and unknown probabilities.
- Moved achievements/easter-eggs coverage from todo to partial; achievement enumeration itself remains open.
- Next: first-party/current-build corroboration, exact achievement catalogue, AI behavior, diplomacy edge cases and movement/Creep-ZOC verification.


## 2026-09-29 — first-party hidden-UI / Explorer corroboration

- Upgraded Chipmunk Mode from an undocumented lead to first-party-confirmed behavior using the 2025 World Championship recap and official 2.15.1 release notes.
- Recorded observable head-presentation effects; retained the egg trigger and audio transformation as lower-confidence community behavior because exact spawn conditions conflict.
- Recovered an overlooked 2.15.1 Explorer rule: pathfinding evaluates mountains and increased sight range when choosing the next tile.
- Coverage remains partial: Chipmunk trigger/persistence and exact Explorer scoring/tie-break logic still need black-box verification.


## 2026-09-29 — AI evidence pass

- Recovered developer-maintained 2023–2024 changelog evidence that AI stopped using Cloaks specifically as city defenders and was later improved at unit selection and city improvement.
- Added a 2025 developer confirmation that AI still trains Cloaks, but deliberately at much lower frequency than at Cloak launch; this rules out a hard “AI never builds Cloaks” implementation.
- Added black-box targets for production context and city-development choices; exact AI weights, scoring and difficulty-specific aggression remain unknown.
- AI coverage remains partial; next priorities are diplomacy decisions, path/target scoring and current difficulty modifiers.


## 2026-09-29 — AI difficulty/scoring boundary pass

- Re-swept first-party/developer material for current AI difficulty modifiers; no newer public numeric replacement for the historical 1/2/3/5 capital-income schedule was located.
- Added official 2.15.1 evidence that Perfection has a difficulty-bonus percentage exposed in game setup, and explicitly separated that score modifier from AI income/aggression.
- Added a fixed-seed black-box matrix to measure current capital SPT, diplomacy/aggression and Perfection score bonus independently.
- AI remains partial; current numeric modifiers and decision thresholds still require direct current-build observation.

## 2026-09-30 — connector write check

- GitHub connector write path verified after reconnect; no research claim added.


## 2026-09-30 — recovered blocked research after connector reconnect

- Recovered previously blocked research into one coherent commit.
- Added dedicated Aquarion current/post-rework spec.
- Added dedicated Diplomacy/Embassy/Cloak/Dagger spec with 2022 baseline, 2023/2025 Embassy pricing history and unresolved current price sequence.
- Added developer-described forced-spawn/Giant-push ordering and the Creep/ZOC documentation conflict.
- Added Google Play achievement snapshot; Sunbringer trigger remains unknown.
- Added 2.16.3 UI/replay state contracts and community Perfection bonus candidate with current-version caveat.
- Fixed map-generation index pointer. No GitHub Actions/CI enabled or run.


## 2026-10-01 — Weekly Challenge evolution pass

- Recovered evidence that Weekly Challenges expanded from the four launch leagues to six leagues by April 2026; retained the 2025 four-league model as historical rather than overwriting it.
- Added Hats of Steel and Ruin Run as scenario examples with explicit starting armies/opponent composition and asymmetric head-start state.
- Strengthened the implementation inference that Weekly scenarios need arbitrary state overrides beyond seed/settings.
- Exact six league names and current promotion/difficulty mapping remain open; no unsupported names were guessed.
- No GitHub Actions/CI enabled or run.


## 2026-10-01 — starving-city score boundary pass

- Recovered the official 2.15.0-era addition of a score penalty for starving cities.
- Kept it separate from the older/current economic rule of -1 SPT per negative population point.
- Recorded the 2026 community observation of -105 score per negative population only as a black-box candidate, not an implemented constant.
- Added a controlled verification matrix to isolate the score coefficient and whether it is generic or Perfection-specific.
- No GitHub Actions/CI enabled or run.
