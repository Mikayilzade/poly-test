# Core mechanics — initial extraction

This is a seed, not a complete specification. Facts are tagged with source IDs from `research/sources.json`.

## Game identity and player count

Polytopia is a turn-based 4X strategy game centered on exploration, city development, technology research and war. The Steam description currently advertises 16 civilizations and single/multiplayer for up to 16 players. [OFF-HOME, STEAM-BASE]

## Modes

Community documentation currently lists four single-player modes: **Perfection, Domination, Creative, Boot Camp**; and two multiplayer victory modes: **Glory, Might**. [WIKI-MODES]

- Perfection: 30-turn score chase.
- Domination: eliminate all opposing tribes, no fixed time limit.
- Glory: multiplayer score race; wiki documents 10,000 points as the winning threshold.
- Might: needs a dedicated current-rules verification pass.
- Creative: configurable bot count/difficulty/map settings; exact current option matrix still to inventory.

## Map sizes

Current community map-generation table: [WIKI-MAP]

| Size | Dimensions | Tiles |
|---|---:|---:|
| Tiny | 11×11 | 121 |
| Small | 14×14 | 196 |
| Normal | 16×16 | 256 |
| Large | 18×18 | 324 |
| Huge | 20×20 | 400 |
| Massive | 30×30 | 900 |

Map generation varies terrain/resource spawn tendencies by tribe. The initial generator attempts roughly equal land distribution between tribes. [WIKI-MAP]

The same source reports ruins by size as 4 / 5 / 7 / 9 / 11 / 23 respectively. It reports starfish at approximately one per 25 water tiles with adjacency restrictions. Exact generator order/probabilities need a dedicated reconstruction pass. [WIKI-MAP]

Path of the Ocean added/reworked a **Pangea** map type: one main landmass surrounded by water; Continents and Pangea try to place capitals on coastlines. [OFF-OCEAN]

## Cities and population

Community city documentation states: [WIKI-CITY]

- A city produces **1 star per turn per city level**.
- Workshop and Park each increase city income by +1 star/turn.
- Human capital receives an additional +1 star/turn.
- A besieged city produces no income.
- Unit capacity is tied to city population bars and is documented as **city level + 1**.
- Connecting a city to the capital grants +1 population to both connected city and capital.
- Base city score: 100 points, plus 50 per level above level 1.

Upgrade choice sequence currently documented:
- level 2: Workshop / Explorer
- level 3: City Wall / Resources
- level 4: Border Growth / Population Growth
- level 5+: Park / Super Unit

Exact population thresholds and all special-tribe substitutions remain to extract. [WIKI-CITY]

## Technology cost

For regular tech tiers, the community wiki documents a base/current formula: [WIKI-TECH]

`cost = technologyTier * numberOfCities + 4`

Thus with one city, T1/T2/T3 are 5/6/7 stars; each additional city adds 1/2/3 stars respectively. The **Literacy** ability from Philosophy reduces research costs by 33%, rounding the discounted result upward. [WIKI-TECH]

The official 2025 balance pass says tech can be researched “backwards” in a branch, giving Vengir Smithery → Mining as the example. The exact UI/graph constraints need explicit modeling. [OFF-2025BAL]

## Regular land units — seed table

The current wiki lists these ordinary land units/stats. This table must be re-checked against the current build and special-tribe substitutions. [WIKI-UNITS]

| Unit | Cost | HP | Atk | Def | Move | Range | Noted skills |
|---|---:|---:|---:|---:|---:|---:|---|
| Warrior | 2 | 10 | 2 | 2 | 1 | 1 | Dash, Fortify |
| Rider | 3 | 10 | 2 | 1 | 2 | 1 | Dash, Escape, Fortify |
| Archer | 3 | 10 | 2 | 1 | 1 | 2 | Dash, Fortify |
| Defender | 3 | 15 | 1 | 3 | 1 | 1 | Fortify |
| Swordsman | 5 | 15 | 3 | 3 | 1 | 1 | Dash |
| Catapult | 8 | 10 | 4 | 0 | 1 | 3 | Stiff |
| Knight | 8 | 10 | 3.5 | 1 | 3 | 1 | Dash, Persist, Fortify |
| Mind Bender | 5 | 10 | 0 | 1 | 1 | 1 | Heal, Convert, Stiff |
| Giant | upgrade | 40 | 5 | 4 | 1 | 1 | Static |
| Cloak | 8 | 5 | 2 | 0.5 | 2 | 1 | Hide/Infiltrate + movement skills |

Important: the 2025 Cymanti rework changes Cymanti’s Diplomacy branch and replaces its cloak analogue with Moth/Egg/Larva behavior; do not treat the regular table as universal. [OFF-CYM25]

## AI difficulty

Current wiki text says higher bot difficulty changes aggressiveness and capital starting income; it lists Easy/Normal/Hard/Crazy capital income as **1/2/3/5 SPT** respectively. [WIKI-MODES]

A 2020 Steam discussion contains a developer response describing the same 1/2/3/5 capital-income progression and higher aggression on higher difficulties. This is strong historical evidence, but AI behavior may have changed since 2020, so current-build verification remains open. [STEAM-AI-DEV]

## Explorer

Official 2.16.3 changelog reduces the number of Explorer moves from **15 to 12**. Precise path selection/reveal weighting still needs reconstruction. [OFF-2163]


### AI advantage boundary — developer evidence

A developer response from April 2024 says the AI receives a small built-in advantage, described as only enough to give it a chance. The response does not identify the mechanism, so it supports a small non-zero AI advantage but not any particular resource, vision, combat, or decision rule. [STEAM-AI-ADVANTAGE-2024]

Keep this separate from the older 1/2/3/5 capital-income schedule. Also do not promote nearby player claims about full-map knowledge or prediction into implementation facts without reproducible evidence. Current-build tests should isolate starting/capital income, fog/target knowledge, combat rules and diplomacy behavior independently.
