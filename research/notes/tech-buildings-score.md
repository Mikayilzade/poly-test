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
| Forge | 5 | +1 population/level per adjacent Mine in the reverted 2025 public rule |
| Port | 7 | +1 population; naval transform/connectivity |
| Market | 5 | star income based on adjacent production buildings |
| Road | 3 | movement + connection |
| Bridge | 5 in aggregate current table | road-like one-tile water crossing |
| Embassy | variable/current balance needs exact formula | diplomacy income |

2025 official patch explicitly says Forges may be built on Forests and Embassy starting cost was reduced but scales with number of embassies owned. [OFF-2025BAL]

### Market current rule and documentation conflict

The community aggregate table still exposes stale/conflicting Market text, but developer-maintained Path of the Ocean changelogs provide a stronger versioned rule: Market income was changed to **1 star per turn per level of each adjacent Sawmill, Windmill or Forge**, capped at **8 levels per production building**, and the old Port doubling was removed. The dedicated Market page agrees with this model. Treat the aggregate "2 stars per adjacent resource building" wording as stale unless current-build observation disproves the developer changelog. [STEAM-BETA-CHANGELOG, WIKI-MARKET, OFF-OCEAN]

The same developer changelog records two related economy/state rules useful for reconstruction:
- **Parks give +1 star per turn** in the post-Path-of-the-Ocean ruleset.
- The **Network task unlocks automatically when the first city is connected**; it is therefore an event/state transition, not a task that should remain hidden until five-city completion. [STEAM-BETA-CHANGELOG]

Historical note: an experimental Forge change made each adjacent Mine grow the Forge by two levels. On 2025-09-09, developer Zoythrus explicitly confirmed that this was reverted; the public rule returned to one Forge level (and one population) per adjacent Mine. The 2025 balance pass separately retained the ability to build Forges on Forests. This matters for tactical city-upgrade solvers: do not count +2 population per Mine in the current regular-tribe route enumeration. [STEAM-BETA-CHANGELOG, STEAM-FORGE-REVERT-2025, OFF-2025BAL]

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


## Tactical score inference

The current score reference states that each population gained is worth **5 score**. City upgrades add a level-dependent bonus so population plus the upgrade itself totals 50 points per ordinary level: level 2 gives 40 upgrade points after 2 population, level 3 gives 35 after 3, etc. [WIKI-SCORE]

This permits reverse inference when a city panel exposes city score but not its population bar. Ordinary non-starving city baselines are level 1 = 100, level 2 = 150, level 3 = 200, level 4 = 250, level 5 = 300, etc. After accounting for other score-bearing local objects, positive population is the remaining score divided by 5. The next upgrade requires level+1 population. Monuments, temples, Parks and the newer starving-city penalty must be handled separately. [WIKI-SCORE, OFF-CYM25-STARVING]

For tactical analysis, enumerate visible legal population sources and calculate the cheapest feasible route to the threshold. Regular examples include harvest fruit/animal/fish (2 stars -> +1), Lumber Hut (3 -> +1), Farm/Mine (5 -> +2), adjacency-scaled Sawmill/Windmill/Forge, and monuments (+3). Treat technology ownership separately: visible existing improvements can prove a technology is owned; otherwise return conditional cost ranges rather than assuming it. [WIKI-POP, WIKI-BUILDINGS]

Midjiwan explicitly documents both sides of this tactic: a city upgrade that produces a Giant can push an invader out, while occupying resource tiles in another player's territory can make that city harder to level. A future advisor should therefore recompute the cheapest upgrade route after each candidate resource block. [OFF-UPGRADE-KEEP-CITY, OFF-PREVENT-UPGRADE]

Implementation target: infer level and city score; solve population where unambiguous; enumerate visible population sources and proven technologies; return minimum stars and conditional alternatives; flag one-turn Giant/displacement risk; test which blockable resource tiles increase the minimum route most; preserve ambiguity for unknown stars, technologies and unseen resources. Early-game tribe identification can similarly use the documented turn-0/turn-1 score fingerprints as candidate sets rather than forced labels. [WIKI-SCORE]


### High-level city-upgrade score edge case

The current community score reference exposes the exact decomposition behind the usual +50-per-city-level rule. Upgrading to level **N** requires N population, worth **5N** score, while the upgrade event itself contributes **50 - 5N**. Thus level 2 is 10 population-score + 40 upgrade-score, level 3 is 15 + 35, and so on. At level 10 the upgrade component reaches zero; above level 10 it becomes negative, while the population plus upgrade-event pair still nets +50 before optional reward score. [WIKI-SCORE]

This matters for score-delta inference in unusually tall cities: do not clamp the upgrade component to zero. Park (+250), super-unit (+50 nominal), Explorer fog reveals and Border Growth territory are separate score-bearing consequences and can make the observed delta larger than the base +50. [WIKI-SCORE]


## Temple growth timing and score-version boundary

Midjiwan's 2020 strategy tip states that a fully grown Temple takes **12 turns** to develop. This is a historical 2020 timing baseline; the first-party 2.8.5 patch changed the growth cadence from every three turns to every two, so the old endpoint is not a current timing guarantee. [OFF-PATCH24-STEAM] The same historical tip says a fully grown Temple was worth 400 points, but that score value is superseded by the official 2025 Balance Pass, which changed Temples to **100 points per level of growth**. The current community score table correspondingly reports 100 base + 100 per level above level 1, max **500 at level 5**. [OFF-TEMPLE-GROWTH-2020, OFF-2025BAL, WIKI-SCORE]

Implementation boundary: keep **growth timing** and **score-per-growth-level** as separately versioned rules. Do not import the old 400-point maximum merely because the 12-turn timing comes from the same 2020 source. The official 2024 patch confirms a two-turn growth interval for version 2.8.5, superseding the 2020 twelve-turn endpoint. The exact construction-turn offset and current 2.17.3 thresholds still need black-box verification; neither the 2020 endpoint nor the wiki's three-turn table should be promoted as current. [OFF-PATCH24-STEAM]


## Historical economy/building deltas — 2020 first-party baseline

Two official 2020 strategy tips expose rules that must remain versioned rather than silently mixed into the current economy:

- On **2020-03-18**, Midjiwan stated that **Clear Forest returned 2 stars**. This is a historical yield baseline; do not apply it to the current ruleset without a source establishing the later transition/current value. [OFF-CLEAR-FOREST-2020]
- On **2020-05-28**, Midjiwan described **Customs House** as an economy building strengthened by surrounding Ports and explicitly limited placement to **one Customs House per city**. The tip also recommends planning its tile when placing the first Port, corroborating a local adjacency/placement relationship. [OFF-CUSTOMS-HOUSE-2020]

Customs House belongs to the pre-Path-of-the-Ocean economy and should not be projected onto the current Market system. Exact historical per-Port income and the patch/version where Clear Forest changed away from 2 stars remain unresolved in this pass.


## Temple intermediate-age community table — chronology and internal conflict

The dedicated community **Temples** page provides a concrete five-level age schedule measured in turns **since construction**, with construction itself counted: **level 1 at age 0–2; level 2 at 3–5; level 3 at 6–8; level 4 at 9–11; level 5 at 12+**. Its own older score table shows **100/150/200/250/300**, while the opening summary now says +100 per growth step and elsewhere says temples level **every two turns**. The displayed three-turn age bands contradict that two-turn prose. Therefore the age table is a **grade-B candidate**, not a verified current schedule. [WIKI-TEMPLES]

The **12-turn fully grown** endpoint is independently supported for the **2020** ruleset only. Midjiwan's official **2024** Patch of the Ocean changed Temple growth from every three turns to **every two turns**. This makes the community page's two-turn prose consistent with the 2024 patch, while its three-turn age table appears historically stale; neither establishes exact current 2.17.3 thresholds. [OFF-PATCH24-STEAM, OFF-TEMPLE-GROWTH-2020] Midjiwan's 2025 Balance Pass updates scoring to **100 points per level of growth**, making a current five-level score candidate **100/200/300/400/500**. This is a **version-crossing synthesis** (2024 growth cadence + community five-level table + 2025 score change), not an official 2.17.3 end-to-end specification. Do **not** copy the wiki's stale 50-point intermediate score increments into the current ruleset. [OFF-TEMPLE-GROWTH-2020, OFF-2025BAL, WIKI-TEMPLES]

**Reproducible verification:** in the current build, construct one Temple at known turn T, capture its displayed level and raw score contribution immediately and on T+1 through T+13 (checking before and after end-turn separately). Repeat at a late Perfection turn and with another Temple terrain type. Distinguish construction-turn-inclusive age, UI visual level, raw score, and final score multiplier. If observed thresholds are T+3/6/9/12, the older community age table matches; if T+2/4/6/8 (subject to construction-turn counting), the official 2024 two-turn cadence matches. Until then, retain both as conflicting hypotheses. [WIKI-TEMPLES, OFF-TEMPLE-GROWTH-2020]
