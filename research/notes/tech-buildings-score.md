# Technology, buildings, resources, ruins and score

## Regular technology tree skeleton

Current community category structure: [WIKI-TECH, WIKI-TRADE]

- Climbing
  - Mining -> Smithery
  - Meditation -> Philosophy
- Fishing
  - Sailing -> Navigation
  - Ramming -> Aquatism
- Hunting
  - Archery -> Spiritualism
  - Forestry -> Mathematics
- Organization
  - Farming -> Construction
  - Strategy -> Diplomacy
- Riding
  - Roads -> Trade
  - Free Spirit -> Chivalry

2025 official balance notes add the ability to research “backwards” along a branch, with Vengir Smithery -> Mining as the explicit example. The exact graph eligibility algorithm needs current-build verification. [OFF-2025BAL]

## Confirmed unlock examples

- Organization: Harvest Fruit (2 stars -> 1 population), reveals crop. [WIKI-ORG]
- Hunting: harvest animal (2 stars -> 1 population); Elyrion replaces this with Forest Magic / enchantment. [WIKI-HUNTING]
- Forestry: Clear Forest + Lumber Hut; current page says clearing gives 1 star and hut gives 1 population. [WIKI-FORESTRY]
- Archery: Archer + forest defence bonus. [WIKI-TECH]
- Philosophy: Mind Bender, Literacy (-33% tech cost), Genius task. [WIKI-PHILOSOPHY]
- Strategy: Defender + offer Peace Treaty; Quetzali starts here. [WIKI-STRATEGY]
- Fishing: fish harvest, Port, Raft and shallow-water movement in the current post-Patch-of-Ocean tree. [WIKI-FISHING]
- Sailing: Scout + ocean movement; special tribes substitute their own techs. [WIKI-SAILING]
- Navigation: Bomber + Starfish Harvesting. [WIKI-NAVIGATION]
- Ramming: Rammer; Aquarion keeps an Aquaculture variant for Aqua Farm. [WIKI-RAMMING]
- Aquatism: Water Temple + defence bonus on water/ocean. [WIKI-TECH]
- Mathematics: Catapult + Sawmill. [WIKI-TECH]
- Trade: Market + Wealth task. [WIKI-TRADE]

## Building catalogue seed

Regular resource/economic buildings from the current aggregate table: [WIKI-BUILDINGS]

| Building | Cost | Main effect |
|---|---:|---|
| Lumber Hut | 3 | +1 population |
| Sawmill | 5 | +1 population per adjacent Lumber Hut |
| Farm | 5 | +2 population |
| Windmill | 5 | +1 population per adjacent Farm |
| Mine | 5 | +2 population |
| Forge | 5 | +2 population per adjacent Mine |
| Port | 7 | +1 population; naval transform/connectivity |
| Market | 5 | star income based on adjacent production buildings |
| Road | 3 | movement + connection |
| Bridge | 5 in aggregate current table | road-like one-tile water crossing |
| Embassy | variable/current balance needs exact formula | diplomacy income |

2025 official patch explicitly says Forges may be built on Forests and Embassy starting cost was reduced but scales with number of embassies owned. [OFF-2025BAL]

### Market conflict to resolve

Public community pages currently disagree:
- aggregate Buildings/Trade text says **2 stars per turn for each adjacent resource building** (Sawmill/Windmill/Forge);
- dedicated Market page says **1 star per level** of each adjacent Sawmill/Windmill/Forge, max level 8, and its history describes older “2 per unique building, doubled by Port” behavior.

Do not implement until current-build behavior is verified or a newer official note resolves the discrepancy. [WIKI-BUILDINGS, WIKI-MARKET, OFF-OCEAN]

## Population / city level threshold

The current Population page states that upgrading from city level L to L+1 requires **L+1 population**: level 1 -> 2 requires 2, level 2 -> 3 requires 3, etc. Population is reversible if supporting buildings/connections disappear. [WIKI-POP]

## Monuments and tasks

Aggregate current building table reports monuments give 3 population and 400 score. Seed tasks: [WIKI-BUILDINGS]
- Altar of Peace: Pacifist
- Emperor's Tomb: Wealth / accumulate 100 stars
- Eye of God: Explorer / find all lighthouses
- Gate of Power: Killer / 10 enemy kills
- Grand Bazaar: Trade / connect five cities to capital
- Park of Fortune: Metropolis / level 5+ city
- Tower of Wisdom: Genius / research all technology

Cymanti 2025 changes replace its old pacifist analogue with a converter task/monument; model special-tribe tasks separately. [OFF-CYM25]

## Ruins

Current community rules: examining a ruin requires beginning the turn on it and consumes the unit's action. Random reward candidates are documented as: [WIKI-RUIN]
- 10 stars
- one random currently researchable technology
- +3 population to capital (with fallback rules if original capital is lost)
- Explorer, conditional on nearby unexplored tiles
- veteran Swordsman on appropriate non-water ruin

No special weighting is reported by the page. Deep-water/special-tribe exceptions and current Aquarion lost-city behavior require a separate pass. [WIKI-RUIN, WIKI-MAP]

## Score model seed

Community score page reports: [WIKI-SCORE]
- unit: 5 points per star of nominal cost; super units 50
- territory: 20 per owned tile
- explored tile: 5
- city: 100 + 50 per level above 1
- Park: 250
- monument: 400
- technology: 100 per tech tier
- temples: base 100, +100 per growth level, max 500 under current 2025 rule

Official 2025 balance confirms temples were changed to 100 points per growth level (from 50), supporting the current score-page value. [OFF-2025BAL]


## Starving cities / negative population

Negative population is shown as red population bars. Current community documentation says each negative population point reduces that city's ordinary star income by **1 SPT**, with income floored at zero; negative population does **not** reduce the city's unit-capacity limit. [WIKI-POP-CURRENT]

This economic penalty is distinct from a newer score rule. The official Cymanti-rework / 2.15.0-era notes explicitly added a **“Score penalty for starving cities”** as a non-Cymanti adjustment. [OFF-CYM25-STARVING]

The official note does not publish the numeric score formula. A September 2026 player reproduction reports a candidate of **-105 score per negative population point** after inspecting a captured starving city. This is grade-D evidence only and must not be hard-coded without reproduction. [REDDIT-STARVING-SCORE-2026]

Implementation model should therefore keep two independent effects:
1. economy: `-1 SPT` per negative population, floor city income at zero;
2. score: post-2.15 starving-city penalty, exact current coefficient/formula unresolved.

Black-box target: create the same city at negative population 0/-1/-2/-3 without changing buildings, tech, territory or units, record score deltas before/after each step, and repeat outside Perfection to determine whether the penalty belongs to generic score state or only Perfection scoring.
