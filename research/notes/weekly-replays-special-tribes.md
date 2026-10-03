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
