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


## 2026-10-03 — capture-cooldown boundary pass

- Added first-party 2.16.3 evidence that city capture during the relevant cooldown was a bug; legal capture must remain gated until cooldown permits it.
- Kept cooldown trigger, duration, ownership and exact re-enable timing unresolved because the changelog does not expose them.
- Turn-flow/capture coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — Explorer reward evidence pass

- Added a first-party source clarifying the two Explorer encounter reward categories.
- Exact quantities and selection logic remain unresolved.
- Explorer coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — Zebasi Weekly enemy-composition pass

- Added first-party evidence that the Zebasi Tribe Moon Special Weekly Challenge pits the player against hordes of Polytaurs.
- Strengthened the scenario model: Weekly enemy-unit composition can depart from ordinary tribe-derived starts and may require explicit unit/spawn state.
- Kept exact count, spawn timing, ownership and technologies unresolved; no unsupported mechanics were inferred.
- Weekly/game-mode coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — Cymanti Algae fruit intent/bug boundary pass

- Added a first-party intent-versus-observation conflict: the rework specifies Aphea Nectar on spawned Algae, while an official Admin acknowledged regional fruit appearing and described that behavior as unintended.
- Kept regional-fruit behavior as a release-era discrepancy rather than a rule; current-build fruit selection remains to be verified.
- Cymanti tile/resource coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — recovered 2.16.3 Weekly/UI contracts

- Added first-party evidence that Weekly Challenge must not leak ordinary Perfection stars or tribe-highscore updates through the bugged Perfection path.
- Added the in-game localization contract that an already-open building info pop-up refreshes after a language change.
- Kept other profile/achievement side effects and broader UI hot-reload scope unresolved.
- Weekly/UI coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — runtime localization UI pass

- Added the 2.16.3 first-party contract that an already-open building info pop-up refreshes its text when the language changes.
- Kept broader hot-reload behavior for other screens/modals unresolved rather than extrapolating.
- UI/localization coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-03 — historical Clear Forest / Customs House pass

- Added first-party 2020 baseline that Clear Forest yielded 2 stars.
- Added first-party Customs House constraints: one per city, with economy driven by surrounding Ports and placement therefore adjacency-sensitive.
- Kept both as historical/versioned rules; exact Clear Forest transition version and historical Customs House per-Port income remain unresolved.
- Economy/building/update-history coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-04 — Weekly pending-friend membership pass

- Added first-party 2.16.3 evidence that pending friend requests must not appear in the Weekly Challenge friends league.
- Split pending and accepted friendship into distinct league-eligibility states; refresh timing after accept/remove and blocking remain unresolved.
- Weekly/social-state coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-04 — special-tribe skin semantics pass

- Reconciled the ordinary cosmetic-skin rule with first-party special-skin marketing.
- Added official Midnight, Forgotten and Solaris presentation contracts; skin-specific nouns are not promoted to new mechanics without independent evidence.
- Exact Midnight and Forgotten base-entity mapping remains open; Solaris is partly mapped already.
- No GitHub Actions/CI enabled or run.


## 2026-10-04 — action-order / carried-status edge-case pass

- Added developer-maintained first-party constraints for Explode damage-before-population ordering, invisible-unit reveal on Break Ice/Harvest Starfish, poison propagation/healing between naval vessel and carried unit, and Giant-push interaction with Skate action state.
- Kept broader trigger ordering, poison tick timing and forced-movement interactions unresolved rather than inferring internals.
- Combat/movement/state coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-04 — Cymanti post-rework atomization pass

- Added a dedicated current/post-2.15 Cymanti note from first-party rework material instead of leaving the tribe as a coarse changelog summary.
- Atomized Algae coexistence/movement/network rules; Fungi/Microbes levels; Creep/poison changes; Boomchi/Raychi/Living Island roles; Swarm persistence; Moth→Egg→Larva timing; damage inheritance; and the Converter monument condition.
- Preserved the official Algae-fruit intent/observed discrepancy and separated unsupported numeric/timing details into black-box targets.
- Added explicit Cymanti coverage to the structured index; coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-04 — Ice Archer battle-preview consistency pass

- Added first-party 2.16.3 evidence that Ice Archer required unit-specific Battle Preview correction.
- Recorded the implementation boundary that preview should share the authoritative combat/status resolver rather than duplicate a simplified damage estimate.
- Kept exact Freeze/damage/retaliation preview ordering unresolved instead of guessing the pre-fix defect.
- Combat/UI coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-05 — post-2.16.3 release-history / Splash rounding pass

- Recovered the official Midjiwan App Store version history through 2.17.3 (2026-09-07), superseding 2.16.3 as the newest explicit numbered public baseline while retaining 2.16.3 as the richer official-site changelog.
- Added the 2.16.5 Splash contract: damage is floored so combat state does not retain half hit points.
- Added versioned observable fixes for random-tribe climate, Polaris/normal siege-fire presentation, quick-touch handling, keyboard +/- zoom and multiplayer tribe disabling.
- Kept the later World-Championship update summary unversioned because the retrieved store history does not attach a clear version/date to it.
- Update/combat/UI coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-05 — World Championship Face Off format pass

- Added first-party 2026 tournament-format evidence: two six-player/tribe groups, single round robin within each group, five rounds per participant and top four from each group advancing to the eight-player Stockholm finals.
- Kept tournament bracket/standings state separate from ordinary multiplayer mechanics; public tie-break ordering remains unresolved.
- Tournament/replay coverage remains partial. No GitHub Actions/CI enabled or run.


## 2026-10-06 — blocked-write recovery and reconciliation pass

- Recovered the previously unattached Aquarion late-beta refinements: removal of the one-Atoll-per-city limit and the Lost City level-3+Wall → shallow-water-ring beta sequence.
- Added the 2020 developer Explorer baseline (Sailing gate for water, nearest-cloud behavior, Explorer-owner-only tech reward) and version-bounded it against the richer 2.15.1 pathfinding update.
- Added 2.8.5 Bridge-into-fog placement, shoreline hinting and forced initial Lighthouse fog.
- Added post-rework Cloak/Pirate release-history boundaries: Mermaid-Cloak damage parity, water-spawn gating, Pirate boat payload and Ciru compatibility fallback.
- Added Path-of-the-Ocean pre-release boundaries for ship upgrades in ally territory and cease-fire protection against indirect Smash/Splash/Explode-style damage.
- Added detailed Forgotten→Aquarion and Solaris→Polaris visual normalization tables without promoting cosmetic names to mechanics.
- Strengthened spectator documentation with first-party visibility of tech choices, city upgrades and attacks.
- Added the current 2026 championship snapshot: 12 qualifier replay links, the 8-player quarterfinal→semifinal→final bracket, the Face-Off “semi-finals” wording conflict, and the Hoodrick 2–1 / deciding Game 3 series evidence.
- Refined the Aquarion Weekly scenario to “pack of Sharks” versus already-bunkered opponents.
- Verified that several previously blocked items were already present and intentionally avoided duplicating them: five-game Weekly access gate, Shared Fog replay option, Moth Scout, capital camera focus, New Dawn replay/Pass & Play icons, six-league count, and current Bubbled movement-state notes.
- No GitHub Actions/CI enabled or run. Research remains partial rather than saturated.


## 2026-10-06 — Moonrise random-matchmaking baseline pass

- Added the developer-documented Moonrise public matchmaking flow: open a match publicly or join another public match without first adding opponents as friends.
- Recorded historical matching dimensions (including player count and map type), friend/account-name identity changes, and mirror-match support including AI duplicate tribes.
- Version-bounded all of this to the 2020 Moonrise baseline; current 2026 quick-match filters, Elo/ranking, lobby ownership and allowed setup matrix remain unresolved.
- No GitHub Actions/CI enabled or run. Multiplayer coverage remains partial; research is not saturated.


## 2026-10-06 — AI relationship halo pass

- Added first-party historical evidence for the game-stats halo as a friendly-AI signal: haloed tribes are less likely to attack, while avoiding trespass and attacking their enemies helps preserve the relationship.
- Cross-referenced the community relation model only as a version-sensitive lead; no hidden numeric opinion weights were inferred.
- Linked this baseline to the already documented Peace Treaty acceptance-at-Great evidence without assuming the 2020 and current thresholds are identical.
- Exact current opinion thresholds, update timing and diplomacy decision weights remain open. Research is not saturated.
- No GitHub Actions/CI enabled or run.


## 2026-10-06 — baseline reconciliation sweep

- Re-swept current first-party/storefront and targeted developer material for unresolved map-generation, diplomacy and multiplayer gaps; no stronger public numeric rules were found for current generator fairness/weights or AI relation thresholds.
- Reconciled the research protocol's stale initial 2.16.3 target statement with the already sourced first-party App Store history: 2.17.3 (2026-09-07) is now the newest explicit numbered public baseline located, while 2.16.3 remains the richer detailed official-site changelog.
- Avoided adding redundant Steam storefront facts already represented in the corpus (16-player support, current map types, Pangea, Massive).
- Important black-box gaps remain, so the corpus is not saturated. No GitHub Actions/CI enabled or run.


## 2026-10-06 — Weekly personal-best UI pass

- Added the current first-party Weekly Challenge progress contract: the UI tracks the player's best score for the active challenge and displays a comparison against it during play.
- Reconfirmed the current hub's 20-turn/same-seed/same-tribe/same-opponents/same-map/same-settings contract without duplicating older launch-only league rules.
- Exact bracket semantics (raw delta vs turn-aligned comparison), ties and unfinished-run handling remain unresolved.
- Weekly/UI coverage remains partial; research is not saturated. No GitHub Actions/CI enabled or run.

## 2026-10-06 — Cymanti source normalization

- Replaced the generic blog pointer with Midjiwan's dedicated Cymanti rework mechanics/changelog page.
- Recorded the official naming discrepancy: prose uses **Living Island**, while the full changelog uses **Floating Island**; retained them as aliases pending current-build verification.
- Numeric and edge-case gaps remain, so research is not saturated.


## 2026-10-06 — Defender / Mind Bender first-party interaction pass

- Added direct Midjiwan evidence that ranged attacks avoid Defender counter-attacks and that adjacent Mind Benders can convert Defenders.
- Kept conversion action-order, status interactions and current edge-case restrictions unresolved rather than extrapolating from the 2021 strategy tip.
- Combat/unit-skill coverage remains partial; research is not saturated. No GitHub Actions/CI enabled or run.


## 2026-10-06 — Archer / Giant kiting first-party pass

- Added direct Midjiwan corroboration that Archers can reposition and fire in the same turn and can repeatedly kite a Giant without allowing it to attack when spacing is maintained.
- Kept exact range/movement values and ZOC/terrain edge cases sourced separately rather than over-reading the strategy tip.
- Combat/movement coverage remains partial; research is not saturated. No GitHub Actions/CI enabled or run.


## 2026-10-07 — Elyrion dragon damage-inheritance first-party pass

- Upgraded Dragon growth damage inheritance from community-only evidence to direct Midjiwan confirmation: the 2025 Cymanti rework explicitly names Baby Dragon → Fire Dragon as an example of a growing unit retaining prior damage rather than healing to full.
- Kept exact current Dragon growth timers version-sensitive rather than promoting the community 3 + 3 interval to first-party fact; current-build black-box verification is still needed.
- Added explicit Elyrion special-tribe coverage to the structured index. Research remains partial rather than saturated. No GitHub Actions/CI enabled or run.


## 2026-10-07 — Phychi Double Attack action-matrix pass

- Added first-party confirmation that Phychi has Double Attack from the 2025 Cymanti rework.
- Added the current community action-order detail that after the first attack, Drain/Break Ice remain available while Capture/Excavate do not.
- Kept this action matrix explicitly secondary until current-build black-box verification; broader post-first-attack actions remain unresolved.
- Cymanti/action-order coverage remains partial; research is not saturated. No GitHub Actions/CI enabled or run.


## 2026-10-07 — Quetzali Weekly authored-state pass

- Added current first-party evidence from the 2026 Quetzali Tribe Moon challenge that both sides can begin with authored Swordsman/Defender armies and access to all level-1 technologies.
- Recorded the implementation boundary that Weekly scenarios need per-side roster and technology-state overrides rather than assuming ordinary tribe starts.
- Kept exact counts/positions/stars and the meaning of “access” (pre-researched vs permission) unresolved for black-box verification.
- Weekly/scenario coverage remains partial; research is not saturated. No GitHub Actions/CI enabled or run.


## 2026-10-07 — Oumaji authored-force / resource-free Weekly pass

- Added first-party 2026 Oumaji Weekly evidence for a starting force of Riders plus a Mind Bender, strengthening the requirement for scenario rosters independent of ordinary tribe tech starts.
- Added the Earth Overshoot Day Weekly constraint: a challenge can suppress trees, crops, animals, fish and gold entirely.
- Kept ambiguous “battalion” count, exact positions/tech state, and unlisted map-feature behavior unresolved for black-box verification.
- Weekly/scenario/map-generation coverage remains partial; research is not saturated. No GitHub Actions/CI enabled or run.


## 2026-10-07 — 2.16.3 out-of-turn resignation / friend-order pass

- Added first-party observable turn-flow rules from 2.16.3: Weekly Challenge resignation is allowed on an enemy turn, and friend games randomize initial player turn order.
- Kept cross-mode resignation behavior and friend-lobby RNG/rematch/team details unresolved rather than generalizing the patch-note wording.
- Turn-flow/multiplayer coverage remains partial; research is not saturated. No GitHub Actions/CI enabled or run.

## 2026-10-09 — repository access recovery check

- Confirmed read access to the existing research branch and located the canonical log at `research/RESEARCH_LOG.md` (not repository root).
- No new mechanics claim added in this access-only pass; outstanding tournament preset evidence still requires source-ledger and index integration.
- Research remains partial and not saturated. No GitHub Actions/CI enabled or run.

## 2026-10-09 — first-party skin entitlement / 2022 balance and tournament contracts

- Recovered an official Steam skin-launch FAQ: skins are cosmetic, same-base-tribe skins count as mirror matches, the picker is separate, and 2022 AI skin selection depended on local ownership; all entitlement rules are version-scoped.
- Recovered the official 2.2.9.8251 release's +4 HP allied-territory healing, Ice Bank level-30 cap, first-contact reward reduction, and explicit infiltration/balance deltas; kept ambiguous first-contact formula unresolved.
- Added the 2022 tournament-specific Live-only / no-ELO / icon contract; flagged current applicability for black-box testing.
- Updated source ledger and coverage pointers. No GitHub Actions/CI enabled or run. Research remains partial, not saturated.


## 2026-10-09 — frozen terrain, Skate/Escape and startup UI contracts

- Extracted previously uncatalogued first-party 2.16.3 behavior: freezing flooded tiles preserves flooding; climate change on frozen tiles must not cause flooding.
- Separated Battlesled land-to-ice kill Escape eligibility from the prohibition on extra Skate+attack movement.
- Added opening-camera capital focus despite auto-focus off, startup disk-save before player command, and a version-scoped Domination 3 won/3 lost → 57% end-screen case.
- Kept the anomalous win percentage and Escape path budget unresolved rather than inventing a formula; updated structured open questions.
- Research remains partial and not saturated. No GitHub Actions/CI created, enabled, or run.

## 2026-10-09 — Moth stats and historical Explorer routing

- Added community-backed post-rework Moth numerical table (5 stars, 10 HP, 2 attack, 0.1 defence, 2 movement, 1 range), skill list and Synergy unlock, explicitly flagged for current-build verification.
- Recovered a developer-attributed historical Explorer routing description (nearest fog, 4/5 reveal cap, lighthouse preference, tie RNG, backtrack penalty and bounded BFS) without promoting its stale 15-step count to current rules.
- Recorded conflicts/chronology against official 2.15.1 routing changes, 2.16.3 12-step Explorers and 2.17.3 faster-Explorer release text; updated source ledger and coverage questions.
- Research remains partial; no GitHub Actions/CI created, enabled or run.

## 2026-10-09 — forced-spawn directional edge cases

- Extended forced-spawn spec from historical developer direction to community-reported friendly movement, ranged last-attack, exact-center south and alternating CCW/CW fallback.
- Documented disappearance with all eight destinations blocked and the community claim that it grants neither Gate of Power kill nor Altar of Peace attack; added a 2025 Catapult-specific anecdotal cross-check.
- Kept ambiguous move-vs-attack precedence, diagonal tie-breaking, port transformations and current-build validity as black-box tests; index and source ledger updated.
- Research remains partial; no GitHub Actions/CI created, enabled or run.

## 2026-10-09 — Cloak warning icon / hidden-target preview boundary

- Added first-party eye-icon warning confirmation; community-sourced eight-neighbor detection and blocked-move reveal/action preservation.
- Recorded a 2025 developer-acknowledged Battle Preview information leak for hidden Cloaks; fix promised for an upcoming patch, shipping version unknown.
- Kept warning presence separate from exact target visibility, and updated coverage/index/source ledger.
- Research remains partial and not saturated. No GitHub Actions/CI created, enabled or run.


## 2026-10-09 — Temple age-table conflict and score chronology

- Added the dedicated community Temple age table: levels 1–5 at age 0–2 / 3–5 / 6–8 / 9–11 / 12+ turns, including construction turn.
- Flagged the page's conflicting “every two turns” wording and obsolete 50-point-per-level table instead of importing them as current mechanics.
- Kept first-party 12-turn full-growth endpoint and 2025 100-point-per-level score change separate; documented a current-build black-box test for exact timing and score.
- Updated source ledger and score/building open questions. Research remains partial; no GitHub Actions/CI created, enabled, or run.


## 2026-10-10 — official 2.8.5 Patch of the Ocean chronology and Temple correction

- Recovered Midjiwan's 2024-02-26 official Steam announcement for 2.8.5.11917 and its 2024-03-14 official release notice; distinguished preview/announcement from release timing.
- Recorded major supersessions of the 2023 naval rework: removal of ordinary Aqua Crops/Farms, Fishing/Port technology move, Market per-level income capped at 8 without Port doubling, 5-star Bridges, Bomber 4→3, Starfish 10→8, and water-ruin Veteran Rammer instead of Bomber.
- Corrected Temple chronology: the first-party 2024 two-turn growth cadence supersedes the 2020 12-turn full-growth claim; the community three-turn age table is likely historical, and current 2.17.3 thresholds remain to be verified.
- Added 2024 Burn Forest/Destroy tech placement, qualitative AI changes and Perfection opponent-count multiplier reduction without inventing missing formulas or probabilities.
- Updated source ledger and index. No GitHub Actions/CI created or run; research remains partial.

## 2026-10-10 — Aquarion Forgotten post-launch official mechanics pass

- Recovered the first-party November 4, 2024 Forgotten update, resolving a stale unlock assumption: **Atolls moved to Aquaculture**, while Waterways unlocks **Amphibious-only Bubbles** (+1 movement on Flooded, lost after attack/stepping onto land).
- Added first-party two guaranteed capital fish, smaller resource-bearing Lost Cities, Crab 5→4 defence, Shark 3→3.5 attack, Jelly 0→2 attack, and strongest-Tentacle selection on overlapping tiles.
- Recovered the August 2024 official Lost City eligibility boundary: Water or Ocean ruin must allow valid city placement, otherwise normal ruin rewards; distance formula unknown.
- Explicitly kept the June beta level-3+Wall Lost City payload, current Bubbled timing, resource distribution and 2.17.3 persistence as verification targets rather than guessing.
- Updated Aquarion notes, version baseline, source ledger and coverage questions together. No GitHub Actions/CI created or run; research remains partial.


## 2026-10-10 — Centipede/Segment chain mechanics and damage-version boundary

- Recovered detailed community Centipede/Segment numerical baselines and transition rules: direct-kill versus retaliation Segment creation, movement restrictions, head/middle-Segment promotions, downstream Explode cascade, and Segment siege without capture.
- Cross-checked against first-party 2025 damage-inheritance change and 2.16.3 multiple-tail bug fix; kept older full-heal reports and ambiguous chain topology as version-sensitive, not current facts.
- Added a reproducible black-box test matrix, two grade-B source records and an indexed Cymanti coverage question. Research remains partial, not saturated.
- No GitHub Actions/CI created or run; no PR/branch creation or merge.

## 2026-10-10 — GitHub write recovery verification

- Verified read access to protocol, index, source ledger and canonical log on the existing research branch.
- Tested a single minimal log-only commit to confirm GitHub write access; no mechanics assertions or coverage changes made in this check.
- Research remains unsaturated. No GitHub Actions/CI created or run.

## 2026-10-10 — pending verification

- Recovered notes are already present. Prioritize current-version verification of historical mechanics and avoid duplicate entries.
- No CI or PR changes.

## 2026-10-10 — official 2.0.58 historical encounter/ruin mechanics

- Recovered the original first-party 2021-09-08 2.0.58 release notes: first-contact reward `min(12, 3 * ceil(encountered_score/1000))` for positive score, replacing tech theft and applying to Domination at that date.
- Flagged a concrete generator-source conflict: 2021 official notes permit ruins next to villages, whereas the current community map page prohibits them. Added a version-scoped black-box test rather than choosing a rule silently.
- Recorded Veteran Swordsman land-ruin replacement and versioned 2021 Cymanti poison/conversion/boost, terrain, and economy changes. Explicitly separated from 2022 contact reduction, 2025 Cymanti rework and 2.17.3 1v1 second-player meeting bonus.
- Updated source ledger, map/version notes and index together. Research remains partial, not saturated. No GitHub Actions/CI, new PR/branch, or merge.


## 2026-10-10 — 2023 launch and beta skill-state reconciliation

- Cross-checked October 2023 developer beta notes with the first-party November 21 release: Mooni Auto Freeze/defence 1; Gaami manual freeze removal then restoration and defence 4→3; Swordsman Fortify removal.
- Extracted launch action contracts: Raft movement 2/no attack, Scout range/vision 2, Bomber no Dash/retaliation, Juggernaut Stomp on move including disembark/no retaliation.
- Recorded experimental village burning on capture as beta-only and removed before launch.
- Added first-party release source and Polaris coverage pointer; kept 2.17.3 applicability unresolved.
- Research remains partial, not saturated. No GitHub Actions/CI, new PR/branch or merge.

## 2026-10-10 — naval reference

- Seven naval unit stats, Port transitions, upgrade constraints and source conflicts documented in research/notes/naval-unit-spec.md. Six community source records added. Current build needs verification. No CI or PR changes.
