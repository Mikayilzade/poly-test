# Special tribes and UI — research pass

## Weekly Challenges
Official 2025 documentation establishes a deterministic weekly scenario: all players receive the same seed, landmass, player tribe and opponents. Access unlocks after five ordinary games. One attempt is available per day, up to seven per week, and matches last 20 turns. [OFF-WEEKLY]

Leagues are Entry, Bronze, Silver and Gold. After Entry, the top third promote, bottom third demote and middle third stay; inactivity alone does not demote. Bot difficulty scales from Easy in Entry to Crazy in Gold. The assigned tribe or skin can be used without owning it. [OFF-WEEKLY]

Version 2.16.3 changed ruin-reward calculation to improve consistency in Weekly Challenges and fixed several save, button, friends-league and high-score issues. [OFF-2163]

## Battle Preview and replay UI
An official January 2025 post confirms that hovering or holding an enemy target previews damage to both units. A sweating enemy indicates the target will die; a skull indicates the attacking unit will die. [OFF-BATTLE-PREVIEW]

2.16.3 confirms status visuals for poison/frozen effects, a splash-damage visual, invisible-nearby-unit hints, replay scrubbing and controller navigation. The 2025 World Championship report also mentions enhanced spectator tools. [OFF-2163, OFF-WC25]

## Polaris
Polaris starts with Frostwork and a Mooni. Community documentation maps Frostwork/Fishing, Sledding/Sailing, Ice Fishing/Aquaculture, Polar Warfare/Navigation and Polarism/Aquatism, plus Ice Archer and Ice Bank substitutions. [WIKI-POLARIS]

Current community unit seed:
- Mooni: cost 5, HP 10, Atk 0, Def 1, Move 1, Range 1; Auto Freeze, Skate, Stiff, Static.
- Ice Archer: cost 3, HP 10, Atk 1, Def 1, Move 1, Range 2; Dash, Freeze, Fortify, Stiff.
- Battle Sled: cost 5, HP 15, Atk 3, Def 2, Move 2, Range 1; Dash, Escape, Skate.
- Ice Fortress: cost 15, HP 20, Atk 4, Def 3, Move 1, Range 2; Skate, Scout, Escape, Static.
- Gaami: upgrade unit, HP 30, Atk 4, Def 3, Move 1, Range 1; Auto Freeze, Freeze Area, Static. [WIKI-POLARIS, WIKI-MOONI, WIKI-BATTLE-SLED, WIKI-GAAMI]

Gaami freezes adjacent tiles/enemies after movement and has Freeze Area. Mooni cannot attack and is used for freezing. [WIKI-GAAMI, WIKI-MOONI]

Official 2025 balance deltas: Glide gives +1 move rather than doubling; Battle Sled has 3 movement on ice rather than 4; Ice Fortress gained Escape and Static; Ice Archer attack became 1. [OFF-2025BAL]

2.16.3 clarifies that Skate plus attacking on ice does not grant extra movement, while a Battle Sled killing from land into ice should still retain Escape. [OFF-2163]

Solaris is officially a Polaris skin with lava/fire/steam presentation; official examples include Pyro and Steam Wagon. [OFF-SOLARIS]

## Elyrion
Official material describes Elyrion as nature-focused and able to turn animals into monsters; community documentation calls the starting technology Forest Magic. Elyrion enchants animals into Polytaurs instead of ordinary hunting. [OFF-ELYRION-FOLDABLE, WIKI-ELYRION]

Polytaur cost increased to 3 stars in the official 2025 balance pass. [OFF-2025BAL]

Dragon growth is Dragon Egg to Baby Dragon to Fire Dragon. Community documentation gives Dragon Egg HP 10, Atk 0, Def 2, Move 1, Range 1 with Grow, Fortify, Stiff and Static. Egg becomes Baby Dragon after three turns, then Fire Dragon after three more; damage carries through growth. [WIKI-DRAGON-EGG]

Sanctuary is documented as a 5-star Forestry building, one per city, earning +1 SPT per adjacent wild animal. If eligible empty adjacent forests exist it attracts one animal every three turns. It can be placed on field, forest or mountain and replaces Elyrion clear/burn-forest actions. [WIKI-SANCTUARY]

## Cymanti current deltas
The official 2025 rework documents Algae as a tile effect that can coexist with improvements; Raychi/Boomchi separation; Living Island; land-based Clathrus; Mycelium on Algae; Fungi level cap and Microbes; Mantis replacing Swordsman; Kiton Creep; Phychi Double Attack; stronger poison plus movement slow; post-attack Explode; Doomux veteran removal and 3.5 attack; Moth/Egg/Larva cycle; Swarm replacing Boost; and tech/task relocations. [OFF-CYM25]

2.16.3 later adds Scout to Moths and changes ruin rewards so units without water movement are not awarded unusable water units from water ruins. [OFF-2163]

## Next gaps
Aquarion full post-2024 tree and unit table; complete Elyrion stats; Polaris buildings/freeze economy; complete Cymanti unit/building tables; replay/spectator controls; setup and in-game UI.


## Aquarion handoff

Dedicated Aquarion implementation note: `research/notes/aquarion-current.md`. It contains the 2024 rework baseline, current unit seed, Flood/Bubble/Atoll/Lost-City distinctions and version traps. [OFF-AQ-REWORK, STEAM-AQ-CHANGELOG]


## 2026 league expansion and scenario complexity

The 2025 launch article is now demonstrably historical on league count: it documents **4 leagues** (Entry, Bronze, Silver, Gold). [OFF-WEEKLY]

Official Steam announcements from April 2026 explicitly state that Weekly Challenges have **six leagues**. This upgrades the six-league count from mirror evidence to first-party evidence. One community discussion from January 2026 identifies **Diamond** as the then-top league, but the exact full six-name sequence was not recovered from first-party text in this pass. Therefore record only the count (6) and Diamond existence as current-era evidence; do not invent the missing league names. [STEAM-WEEKLY-APR26]

The 2026 challenge announcements also strengthen the scenario-override model:
- **Hats of Steel**: Sha-Po starts against a Xin-Xi empire with Riders/Swordsmen; player starts with a Cloak and two Archers; New Dawn is present elsewhere on the map. [STEAM-HATS26-MIRROR]
- **Ruin Run**: ∑∫ỹriȱŋ races several tribes to ruins and the opponents explicitly start with a head start. [STEAM-RUINRUN26-MIRROR]
- Later official site examples independently include Sharks, Riders + Mind Bender, level-1-tech armies, and a map with no natural resources. [OFF-AQ-WEEKLY26, OFF-OUMAJI-WEEKLY26, OFF-POLYNEWS26]

Implementation inference: Weekly Challenge scenario data must support arbitrary starting units, faction placement/state, technology grants, resource/map constraints and asymmetric starting progress, not merely seed + tribe + bot difficulty.

### Confidence caveat

The six-league count is now first-party-confirmed by official Steam announcements. The original 2025 four-league article remains first-party and should be retained as version history. Exact 2026 league names/promotion mapping remain open.


## Weekly winner-replay archive behavior

An official March 2025 Polynews post states that players can **revisit winner replays from previous weeks** and tap to watch the previous week's top score. This is stronger than treating Weekly replay access as only a one-week transient surface: the public UI contract includes historical winner-replay retrieval. The source does not specify retention duration, number of archived weeks, downloadability, or whether non-winning runs are retained, so those remain open. [OFF-WEEKLY-REPLAYS25]


## Kickoo 2026 scenario override

The official June 2026 Steam announcement for **Command & Konka** describes a Massive-map Weekly scenario built around an island containing multiple Konka mounds. Capturing the relevant city makes it level up enough to enable border growth. This is additional first-party evidence that Weekly scenarios can encode unusual map objects/state and city-upgrade outcomes, not just starting armies or technologies. [STEAM-WEEKLY-APR26]

## Late-2026 first-party scenario overrides

The official 2026 Polynews archive adds three concrete scenario-state examples that should be representable without special-case game logic: [OFF-POLYNEWS26]

- **Earth Overshoot Day (2026-07-27):** a challenge with no natural resources at all — explicitly no trees, crop, animals, fish or gold. This is strong first-party evidence that Weekly map/scenario data can suppress ordinary resource classes globally.
- **Oumaji Tribe Moon (2026-08-03):** the player starts with a battalion of Riders and a Mind Bender in a historical Oumaji-vs-Imperius setup.
- **Quetzali Tribe Moon (2026-08-31):** both sides start with armies containing Swordsmen and Defenders and with access to **all level-1 technologies**.

Implementation inference: scenario serialization needs explicit technology grants and resource-generation overrides in addition to seed, starting units and faction state. In particular, do not derive a Weekly participant's known techs only from its tribe's normal starting technology.


## Tournament replay surface

An official September 2025 World Championship update states that replays from more than a thousand qualifier matches were available on the official Tournament Page. The same post gives the in-game tournament path as **Multiplayer > Tournaments**. This establishes a first-party public tournament-replay surface distinct from the ordinary recent-replay list and the Weekly winner archive. The post does not define replay retention, whether every match remains available indefinitely, spectator fog rules, or export/download behavior, so those remain open. [OFF-WC25-QUALIFIERS]


## Zebasi Tribe Moon 2026 scenario override

The official 2026 Polynews archive describes the **Zebasi Tribe Moon Challenge** as a Special Weekly Challenge in which the player must hold ground against **hordes of Polytaurs**. This is first-party evidence that Weekly scenarios can prescribe an unusual enemy-unit composition built around another tribe's signature unit rather than only normal tribe starts. The announcement does not specify exact Polytaur count, spawn timing, ownership, technologies, or whether the horde is pre-placed versus generated, so those details remain unresolved. [OFF-POLYNEWS26]

Implementation inference: Weekly scenario serialization should not assume that unit rosters are derivable from the participating tribe's ordinary tech tree/start state; explicit scenario-owned unit composition/spawn state may be required.


## Weekly Challenge progression isolation — 2.16.3

The official 2.16.3 changelog fixes Weekly Challenge games giving **stars and tribe highscores in Perfection mode**. Treat those rewards as leakage from the ordinary Perfection progression path rather than intended Weekly behavior: Weekly Challenge runs must not update the ordinary Perfection-star award or tribe-highscore state through that bugged path. The changelog does not establish whether achievements, profile statistics, tournament records or other account-level counters are isolated the same way, so those remain unresolved. [OFF-2163]


## Weekly friends-league membership boundary — 2.16.3

The official 2.16.3 changelog fixes **pending friends appearing in the Weekly Challenge friends league**. Treat a pending friend request as a distinct relationship state from an accepted friendship: pending users must not be included in the Weekly friends-league membership set. [OFF-2163]

The changelog does not define when league membership refreshes after accepting/removing a friend, whether blocking has a separate effect, or whether an already-loaded league updates live. Keep those as black-box verification targets rather than inferring them.


## World Championship 2026 Face Off format

The official 2026 championship site documents the **Face Off** stage as two groups of six regular-tribe representatives. Within each group, every tribe/player meets every other member **once** (five rounds per player); the **top four from each group advance**, producing eight Stockholm finalists. The published schedule exposes five synchronized rounds for each group and records standings by wins. [OFF-CHAMP26-FACEOFF]

This is tournament-format evidence rather than a general game-mode rule. Do not bake the two-groups-of-six bracket into ordinary multiplayer. It does, however, establish that the tournament surface must represent round-robin groups, per-round pairings, standings and advancement separately from the underlying 1v1 match state. Tie-break ordering is not explained on the public Face Off page and remains unresolved. [OFF-CHAMP26-FACEOFF]


## 2026 championship replay and finals-bracket snapshot

The current official 2026 championship homepage exposes a **Replay** link for each of the twelve regular-tribe qualifier winners, providing a current late-2026 tournament replay surface rather than only the 2025 historical one. [OFF-CHAMP26]

The same page renders the Stockholm finals as an eight-player elimination tree with **four Quarterfinals → two Semifinals → one Final → Champion**. The displayed quarterfinal pairings are Yădakk–Quetzali, Hoodrick–Xin-Xi, Kickoo–Luxidoor and Zebasi–Bardur. [OFF-CHAMP26]

There is a first-party wording conflict: the Face Off page says the top four from each six-player group “advance to the semi-finals in Stockholm,” while the main championship page explicitly labels the next eight-player stage **Quarterfinal**. Preserve this as a site-label conflict; the visible bracket structure is unambiguous about eight players entering four quarterfinals. [OFF-CHAMP26, OFF-CHAMP26-FACEOFF]

An official Hoodrick qualifier report separately confirms that at least one 2026 qualifier final was a **multi-game match series**: Willibomb won 2–1, with Game 3 described as the deciding game. Do not generalize this single report into a universal best-of-three rule for every 2026 stage without a tournament rules source. [OFF-HOODRICK26]

## Aquarion 2026 Weekly scenario detail

The official Aquarion Weekly Challenge states that the player begins with a **pack of Sharks** while the enemies have already **bunkered up**. [OFF-AQ-WEEKLY26] This strengthens the scenario-state model beyond a generic “Sharks are present” observation: both starting army composition and opponent readiness/positioning may be authored overrides.


## Hoodrick Tribe Moon 2026 — authored starting squad

The official Polynews archive for **2026-10-05** describes *The Forest's Jest* Weekly Challenge as starting the player with **two Warriors, one Archer and one Defender** in an autumn forest with unspecified hidden dangers. [OFF-POLYNEWS26]

This is another current first-party example of an authored mixed-unit opening squad. The announcement does **not** identify the hidden dangers, exact positions, technologies, map seed/type, opponent army, or whether the forest presentation changes gameplay; keep all of those unresolved rather than inferring them from the lore text.

Implementation inference: Weekly scenario state should encode exact unit type/count independently of a tribe's ordinary starting unit and tech-derived production options.


## Current Weekly progress UI contract

The current official Weekly Challenge hub documents an in-run progress surface beyond the final leaderboard: the game tracks the player's **best score for the current challenge** and shows comparison against it in brackets while playing. The same current hub reiterates that each Monday's challenge is 20 turns and uses the same seed, tribe, opponents, map and settings for participants. [OFF-WEEKLY-HUB]

Implementation boundary: preserve a per-challenge personal-best value separately from the live run score, and expose their comparison during the run. The public page does not define whether the bracket value is a raw score delta, target score, turn-aligned ghost score, or how ties/unfinished runs are handled; those details remain black-box targets.


## Quetzali Tribe Moon 2026 — symmetric authored armies and tech access

The official Polynews archive for **2026-08-31** describes the Quetzali *Chetiq* Weekly Challenge as a head-to-head scenario where **both the player and opponent start with armies containing Swordsmen and Defenders and with access to all level-1 technologies**. [OFF-POLYNEWS26]

This is first-party evidence that a Weekly scenario can override both sides' initial military composition and technology availability, rather than merely selecting a tribe/map/seed. The announcement does not give exact unit counts, positions, starting stars, city state, map settings, or whether “access to all level-1 techs” means pre-researched technologies versus a scenario-specific research permission; keep that distinction unresolved pending in-game verification.

Implementation inference: scenario serialization should support explicit per-side starting rosters and technology-state overrides independently of ordinary tribe starting techs.
