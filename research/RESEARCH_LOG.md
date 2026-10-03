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


## 2026-10-01 — Path of the Ocean economy reconciliation

- Resolved the Market documentation conflict in favor of the developer-maintained changelog plus the dedicated Market page: 1 SPT per adjacent production-building level, cap 8 per building, with old Port doubling removed.
- Added two overlooked state rules from the same developer changelog: Parks produce +1 SPT and the Network task unlocks automatically on the first city connection.
- Kept experimental Forge beta behavior as historical rather than promoting it to current rules.
- No GitHub Actions/CI enabled or run.


## 2026-10-01 — replay behavior pass

- Added the developer-described 2022 replay baseline: replay list access, sharing, favorites, player-view information and playback controls.
- Added the 2023 developer statement that recent replays should be retained, with no exact count stated.
- Kept these as historical baselines; current limits and spectator visibility rules still need verification.
- No GitHub Actions or CI used.


## 2026-10-01 — 2.16.3 replay/state edge-case pass

- Added current first-party replay/Pass & Play presentation contracts, including per-player resource-theme rendering during replay.
- Recorded replay scrubbing as non-linear state traversal evidence and kept ongoing-game share-URL support explicitly unresolved despite the official crash-fix clue.
- Added random friend-game turn order and enemy-turn Weekly resignation as observable state-machine rules.
- Added the 2.16.3 ruin-reward compatibility rule: no unusable water-unit reward when the explorer lacks water movement, plus improved Weekly consistency.
- No GitHub Actions/CI enabled or run.


## 2026-10-01 — Weekly replay archive pass

- Added first-party evidence that winner replays from previous Weekly Challenges remain revisit-able, including direct access to the previous week's top-score replay.
- Kept retention duration, archive depth, non-winner retention and download/export behavior unresolved rather than inferring them.
- No GitHub Actions/CI enabled or run.


## 2026-10-01 — map-mode boundary pass

- Added developer corroboration that Perfection/Domination historically use Continents as their default/fixed map type.
- Added current 2026 developer confirmation that Massive remains the largest public map size, supporting 900 tiles as the public maximum.
- Kept the 2021 mode/map statement version-scoped rather than silently assuming later generator rewrites preserved every detail.
- Current generator fairness/spawn weighting and mode-specific override behavior remain open. No GitHub Actions/CI enabled or run.


## 2026-10-01 — Weekly first-party corroboration pass

- Upgraded the 2026 six-league count from secondary mirrors to direct official Steam announcement evidence.
- Added Command & Konka as first-party evidence for Weekly scenarios with unusual map objects/state and capture-driven city upgrade/border-growth behavior on a Massive map.
- Exact six league names and promotion/demotion mapping remain unresolved; no unsupported values were added.
- No GitHub Actions/CI enabled or run.


## 2026-10-01 — tactical score-inference pass

- Added 5-points-per-population as an explicit reverse-inference rule for city population from visible city score.
- Added a tactical upgrade-threat model: visible population sources, proven-vs-unknown technologies, minimum-star routes and Giant/displacement risk.
- Added first-party counterplay evidence that occupying resource tiles can hinder city upgrades, plus official Giant-upgrade displacement corroboration.
- Added early-game tribe score fingerprints as a candidate-set inference target; ambiguous hidden state remains explicit.
- No GitHub Actions/CI enabled or run.


## 2026-10-01 — Forge tactical-cost correction

- Reconciled a tactical-solver-relevant Forge conflict using a direct 2025 developer reply: the experimental two-level/two-population-per-Mine behavior was reverted.
- Updated the regular building table and upgrade-route guidance to use one Forge level/population per adjacent Mine; Forest placement remains from the 2025 balance pass.
- This prevents overestimating one-turn city-upgrade/Giant routes when advising from screenshots.
- No GitHub Actions/CI enabled or run.


## 2026-10-02 — New Dawn visual-normalization pass

- Added a first-party New Dawn -> base Cymanti presentation mapping for units, growth forms and resources.
- Recorded the implementation boundary explicitly: skin recognition should normalize cosmetic identities to base gameplay entities before tactical reasoning.
- Left exact building/technology/terrain icon substitutions for a later visual-reference pass; no assets were copied.
- No GitHub Actions/CI enabled or run.


## 2026-10-02 — late-2026 Weekly scenario-state pass

- Added first-party 2026 Weekly examples that require global resource suppression, explicit starting armies and explicit technology grants.
- Earth Overshoot Day removes every ordinary natural-resource class; Oumaji starts with Riders + Mind Bender; Quetzali grants all level-1 technologies alongside Swordsmen/Defenders.
- Strengthened the implementation boundary: Weekly scenario state cannot be reconstructed from seed + normal tribe start alone.
- Exact six-league names/mapping and generic scenario serialization remain open.
- No GitHub Actions/CI enabled or run.


## 2026-10-02 — high-level city score decomposition pass

- Added the exact city-upgrade score decomposition: level-N population contributes 5N while the upgrade event contributes 50-5N, preserving +50 total even when the event component becomes negative above level 10.
- Flagged Park, super-unit, Explorer and Border Growth rewards as separate score deltas so tactical score inference does not misclassify tall-city turns.
- No GitHub Actions/CI enabled or run.


## 2026-10-02 — Temple growth/version-boundary pass

- Added first-party confirmation that a fully grown Temple takes 12 turns to develop.
- Separated that timing baseline from the historical 400-point maximum in the same 2020 source; the official 2025 balance change supersedes the score value with 100 points per growth level, matching the current 500-point level-5 community table.
- Kept exact intermediate growth-turn cutoffs unresolved rather than promoting old community timing as current fact.
- Score/building coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-02 — Battle Preview UI pass

- Added first-party documentation for Battle Preview: hover/hold a target to preview both sides' expected HP change.
- Recorded the two outcome indicators: sweating target for target removal; skull for attacker removal after the exchange.
- Kept this as a UI projection of the combat resolver rather than a separate mechanic.
- Combat/UI coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-02 — first-party movement/vision corroboration pass

- Upgraded Rider follow-up movement, mountain vision, player-relative fog, Cloak eye indicator and Veteran promotion from community-only citations to direct Midjiwan evidence.
- Added the 2.16.3 Polaris action-accounting boundary: Skate plus a combat action on ice gives no extra movement by itself, while the documented Battlesled land-to-ice case retains Escape afterward.
- Kept exact Cloak detection radius and broader Skate/Escape combinations unresolved.
- Combat/movement coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-02 — AI diplomacy threshold pass

- Added first-party evidence that bots accept Peace Treaty offers when their opinion is **Great**.
- Relation calculation and opinion-label boundaries remain unresolved.
- AI/diplomacy coverage remains partial.


## 2026-10-02 — Explorer first-party reward pass

- Added direct Midjiwan evidence that Explorer can collect stars and is especially valuable with many opponents.
- Kept exact star quantity, probability and technology-vs-stars reward selection unresolved rather than guessing.
- Vision/fog/Explorer coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-02 — Lighthouse shared-discovery-state pass

- Added first-party detail that Lighthouse discovery grants +1 population to the discoverer's capital and adds that tribe's color as a visible tier on the Lighthouse.
- Split implementation inference into per-player discovery/task state versus shared visible multi-tribe Lighthouse state.
- Left discovery ordering, duplicate handling and lost-capital behavior unresolved.
- Map-generation/UI coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — startup persistence / Bridge cleanup pass

- Added first-party 2.16.3 evidence that games persist to disk on startup, before any player command; this also affected Weekly Challenge play-button readiness.
- Added the Bridge-destruction presentation contract: removed Bridges must not leave a road visible on the ocean tile.
- Kept internal save timing/data structures and Bridge/road storage representation as implementation details rather than inferred mechanics.
- UI/turn-flow coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — last-turn input / Domination result pass

- Added first-party 2.16.3 evidence that Escape deselection remains available on the last turn of Perfection/Weekly Challenge.
- Added the Domination end-screen result-ratio contract: 3 wins / 3 losses must display 50%, not 57%.
- Kept rounding, draw/unfinished handling and reuse of the percentage component unresolved.
- UI/turn-flow coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — flood/freeze tile-state pass

- Added first-party 2.16.3 state-transition constraints: freezing a flooded tile must preserve its flooded state, and climate change on a frozen tile must not itself create flooding.
- Recorded the implementation boundary that flood, freeze and climate should remain separable state dimensions rather than destructive terrain aliases.
- Left thaw ordering and broader Polaris/Aquarion flood-freeze interactions unresolved.
- Update/special-tribe coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — friend-presence / capture-occupancy pass

- Added first-party multiplayer UI evidence that online friends are marked with a green dot and can be invited from that surface.
- Added first-party corroboration that the capturing unit persists as the immediate city defender after capture; Defender is explicitly recommended to resist next-turn recapture.
- Kept presence refresh/invite lifetime and exact capture-confirmation/cooldown sequencing unresolved.
- Multiplayer/UI/turn-flow coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — Diplomacy detection/infiltration corroboration pass

- Added first-party post-launch evidence that every unit type can detect Cloaks and that each city can be infiltrated at most once per turn.
- Upgraded the infiltration limiter from secondary/developer evidence while keeping detection radius and reveal timing unresolved.
- Diplomacy/Cloak coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — tournament replay-surface pass

- Added first-party evidence that World Championship qualifier replays were exposed on the official Tournament Page, alongside the in-game Multiplayer > Tournaments entry point.
- Kept retention depth, completeness, spectator fog/hidden-information rules and export behavior unresolved.
- Replay/spectator coverage remains partial. No GitHub Actions/CI enabled or run.
