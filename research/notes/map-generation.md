# Map generation — public behavioral reference

This note records publicly documented observable behavior. Detailed community descriptions are treated as secondary evidence and should be black-box tested before implementation. Sources: [WIKI-MAP, STEAM-MOONRISE-FAQ, OFF-OCEAN, OFF-POTO-LAUNCH, WIKI-LIGHTHOUSE].

## Sizes and defaults

| Size | Dimensions | Tiles |
|---|---:|---:|
| Tiny | 11×11 | 121 |
| Small | 14×14 | 196 |
| Normal | 16×16 | 256 |
| Large | 18×18 | 324 |
| Huge | 20×20 | 400 |
| Massive | 30×30 | 900 |

Community documentation says Perfection uses Normal. Domination scales with opponents: 1→Tiny, 2→Small, 3→Normal, 4+→Large. Creative/multiplayer allow host selection; Tiny supports up to 9 players and other sizes up to 16. [WIKI-MAP]

Moonrise officially introduced Huge/Massive and selectable Dryland, Lakes, Continents, Archipelago and Water World. Pangea was added by Path of the Ocean. [STEAM-MOONRISE-FAQ, OFF-OCEAN]

## Map types / approximate wetness

| Type | Approx wetness | Character |
|---|---:|---|
| Drylands | 0–10% | almost entirely land |
| Lakes | 25–30% | inland lakes; land around outer edge |
| Continents | 40–70% | discrete large landmasses |
| Pangea | 40–60% | one central main landmass + ocean/islands |
| Archipelago | 60–80% | discontinuous island chains |
| Water World | 90–100% | mostly water; forced land for cities |

[WIKI-MAP]

Official Path of the Ocean confirms Pangea as one main landmass surrounded by water and says Continents/Pangea prioritize coastal capitals. It also says Continents was redesigned to allow rivers, separate player continents, or multiple players distributed over fewer landmasses. [OFF-OCEAN, OFF-POTO-LAUNCH]

## Generation stages

The community description gives the usual observable generation stages as capitals → villages → terrain → resources → ruins/starfish, with variations by map type. Continents/Pangea instead create land before village/capital selection. [WIKI-MAP]

For Drylands, Lakes, Archipelago and Water World, capital placement uses map domains:
- 1–4 players: 4 domains
- 5–9: 9 domains
- 10–16: 16 domains

Continents and Pangea do not use that scheme. Exact candidate weighting remains unverified. [WIKI-MAP]

## Village passes

Community documentation distinguishes:
- suburbs: Lakes + Archipelago;
- pre-terrain villages: Lakes + Archipelago + Water World;
- post-terrain villages: used broadly, with special land-first handling on Continents/Pangea.

Lakes/Archipelago attempt up to two suburb villages per capital before terrain is placed. Placement constraints can leave fewer. [WIKI-MAP]

The documented pre-terrain quantity is based on `floor(width/3)^2 - (capitals + suburbs)`, multiplied by density coefficient 0.3 for Lakes/Archipelago or 0.1 for Water World. Final rounding is not explicit in the public description. [WIKI-MAP]

Post-terrain placement continues while legal candidates remain rather than targeting a fixed count. The public City page independently confirms villages do not occupy the map edge and that at most one village occurs within a 3×3 area. [WIKI-MAP, WIKI-CITY]

## Pangea / Continents

Pangea: seed a central main landmass, place spaced villages, convert selected villages into well-separated capitals with coastal preference, then add size-dependent island villages. The coastal preference is first-party confirmed. [WIKI-MAP, OFF-OCEAN]

Continents: create separated landmasses, place villages on them, ensure landmasses receive settlements, then select capitals with preference for separate landmasses where possible. Official material confirms the post-2023 generator intentionally supports multiple continent/rivers layouts. [WIKI-MAP, OFF-POTO-LAUNCH]

Community table for extra island villages on Continents/Pangea: Tiny 0, Small 1, Normal 2, Large 3, Huge 4, Massive 9. [WIKI-MAP]

## Base terrain/resource distribution

Community documentation says the standard/base land distribution targets these percentages: [WIKI-MAP]

| Tile/resource | Inner city | Outer |
|---|---:|---:|
| Field total | 48% | 48% |
| fruit | 18% | 6% |
| crop | 18% | 6% |
| empty field | 12% | 36% |
| Forest total | 38% | 38% |
| animal | 19% | 6% |
| empty forest | 19% | 32% |
| Mountain total | 14% | 14% |
| metal | 11% | 3% |
| empty mountain | 3% | 11% |

Fish baseline is 50% of shallow-water tiles. Ordinary resources are documented as appearing only within two tiles of a city/village. [WIKI-MAP]

## Tribe modifiers

Current community table: [WIKI-MAP]

- Xin-xi: 1.5× mountain, 1.5× metal
- Imperius: 0.5× animal, 2× fruit
- Bardur: 0.8× forest, 0× crop
- Oumaji: 0.2× forest/animal, 0.5× mountain; water modifier is uncertain in current behavior
- Kickoo: 0.5× mountain, 1.5× fish; water modifier uncertain
- Hoodrick: 0.5× mountain, 1.5× forest
- Luxidoor: base
- Vengir: 2× metal, 0.1× animal/fruit/fish
- Zebasi: 0.5× mountain/forest/fruit
- Ai-Mo: 1.5× mountain, 0.1× crop
- Quetzali: 2× fruit, 0.1× crop
- Yădakk: 0.5× mountain/forest, 1.5× fruit
- Aquarion: 0.5× forest; water modifier uncertain
- Elyrion: 0.5× mountain, 1.5× crop
- Polaris: follows non-Polaris opponent biome where applicable, otherwise base
- Cymanti: 1.2× mountain; crop slot becomes spores; no crop

The public description applies mountain adjustment before forest adjustment, with fields becoming the remainder. [WIKI-MAP]

## Ruins, starfish and lighthouses

Ruins are placed after villages/resources/lighthouses; they can occur on field, forest, mountain or deep ocean and cannot be adjacent to another ruin or village. Lakes limits water ruins to at most one third. [WIKI-MAP]

Ruins by size: Tiny 4, Small 5, Normal 7, Large 9, Huge 11, Massive 23. [WIKI-MAP]

Starfish are documented at approximately one per 25 water tiles and cannot be adjacent to another starfish, lighthouse or city. [WIKI-MAP]

Path of the Ocean added one Lighthouse in each corner. Discovering one gives +1 population to the discoverer’s capital; all four complete the Explorer task. The Lighthouse page says they begin fogged even if normal starting vision would expose the corner. [OFF-OCEAN, WIKI-LIGHTHOUSE]

## Version notes and open tests

Moonrise officially replaced the older terrain generator and added the larger sizes/map customization. Path of the Ocean added Pangea and overhauled Continents. Its changelog also says AI was improved, without algorithmic detail. [STEAM-MOONRISE-FAQ, OFF-POTO-LAUNCH]

A developer response in December 2023 said a new map generator was being tested in beta. The public sources in this pass do not establish exactly which beta changes later shipped. [DEV-MAPGEN-2023]

Still requiring black-box verification:
- exact RNG and iteration ordering;
- capital candidate weighting and fairness/retry rules;
- final rounding for pre-terrain village counts;
- edge-distance details for post-terrain villages;
- Water World island settlement logic;
- current behavior of tribe water modifiers;
- biome ownership at borders between tribes;
- overcrowded/impossible-placement fallback behavior.


## First-party mode/map constraints

A 2021 developer answer states that **Perfection and Domination use Continents**, describing Continents as the default map type for those score/star modes at that time. This is useful first-party corroboration of the community map-mode table, but should be treated as a historical baseline because later map-generation rewrites may have changed implementation details. [DEV-MODE-CONTINENTS-2021]

For the current upper size boundary, a March 2026 developer reply states that **Massive is the largest map size**. Combined with the established 30×30/900-tile Massive table, this supports keeping 900 tiles as the current public maximum rather than extrapolating larger hidden sizes. [DEV-MASSIVE-MAX-2026, WIKI-MAP]

These sources do not resolve current Perfection/Domination generator internals, map-type override possibilities, or spawn fairness; those remain black-box targets.
