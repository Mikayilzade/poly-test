# Cymanti post-rework mechanics (2025-10-29 baseline)

This note isolates the **post-2025 Cymanti rework** so older guides do not silently contaminate the current ruleset.

Primary authority: [OFF-CYM25-DEDICATED]. Secondary current wiki pages are used for exact numbers not stated in the official changelog.

## Official rework rules

The official 2025-10-29 rework establishes these current semantics:

- **Algae** is a tile effect rather than a tile improvement. Other improvements can coexist with it. Creating Algae no longer grants population; it creates Aphea Nectar instead. Naval movement is not slowed by Algae, but land units are. [OFF-CYM25-DEDICATED]
- **Raychi** lost its old combined role. **Boomchi** takes the explosive/algae-spreading role; the revised Raychi is the conventional naval combat unit. [OFF-CYM25-DEDICATED]
- **Boomchi** has Amphibious and may operate on land as well as water. [OFF-CYM25-DEDICATED]
- **Living Island** is the Navigation/Oceanology heavy water unit. It automatically creates Algae while moving and deals area damage, conceptually filling the Juggernaut role. [OFF-CYM25-DEDICATED, WIKI-LIVING-ISLAND]
- **Clathrus** is now a **land** building that grows from spores/Fungi rather than an Algae-powered water building. It remains poisonous and no longer creates network connections. **Mycelium can be built on Algae** instead. [OFF-CYM25-DEDICATED]
- Cymanti Explorers can travel water like other tribes. [OFF-CYM25-DEDICATED]

### Land/effect changes

- Fungi normally stop at level 2. **Microbes**, unlocked by Recycling, permits a third growth level. [OFF-CYM25-DEDICATED]
- **Mantis** replaces Swordsman with the same base stats plus Creep. [OFF-CYM25-DEDICATED]
- **Kiton** gains Creep. Creep no longer cancels the mountain movement penalty. [OFF-CYM25-DEDICATED]
- **Phychi** gains Double Attack. [OFF-CYM25-DEDICATED]
- Poison's defence debuff is **50%**, while terrain/city defence bonuses remain active. Poison also slows affected enemy units. [OFF-CYM25-DEDICATED]
- Units with Explode may explode after attacking. [OFF-CYM25-DEDICATED]
- **Doomux** attack is 3.5 and it cannot become veteran. [OFF-CYM25-DEDICATED]
- Growing/transformation units inherit damage rather than healing on transformation. The official examples include Centipede, Dragons and Larva. [OFF-CYM25-DEDICATED]

### Moth infiltration lifecycle

- Moth replaces Cloak. It flies, is not invisible, poisons city defences on infiltration and lays Eggs rather than Daggers. [OFF-CYM25-DEDICATED]
- Official rework wording: Egg waits **1 turn** before hatching to Larva; Larva becomes Moth after **3 more turns**. [OFF-CYM25-DEDICATED]
- Current wiki exact Moth stats: cost 5; HP 10; attack 2; defence 0.1; movement 2; range 1; Dash/Sneak/Scout/Infiltrate/Poison/Static/Stiff. [WIKI-MOTH]
- Official 2.16.3 explicitly added/fixed **Scout** on Moths, making that skill part of the 2026 baseline. [OFF-2163]
- Current wiki lists Egg as HP 10, attack 2, defence 3, movement/range 0, with Grow/Stiff/Static/Explode. It says “within 2 turns,” conflicting with the official rework’s “after a turn”; preserve this as a timing conflict pending in-game verification. [WIKI-INSECT-EGG, OFF-CYM25-DEDICATED]

### Shaman

- Boost was replaced by **Swarm**: movement buff only, retained until the unit is attacked. [OFF-CYM25-DEDICATED]
- Shaman moved to Meditation, renamed **Rituals** for Cymanti; Mountain Temple moved to Philosophy, renamed **Mysticism**. [OFF-CYM25-DEDICATED]
- Pacifist task becomes **Converter**: convert 3 enemies to unlock the **Church of Converts** monument. [OFF-CYM25-DEDICATED]
- Current wiki Shaman stats: cost 5; HP 10; attack 1; defence 1; movement/range 1; Swarm and Parasite. [WIKI-SHAMAN]

## Exact unit/building anchors

Current wiki data gives these useful exact post-rework anchors:

| Object | Current documented values |
|---|---|
| Living Island | 20 stars; 20 HP; 4 atk; 4 def; move 2; range 1; Stomp/Algae/Poison/Static [WIKI-LIVING-ISLAND] |
| Boomchi | 5 stars; 10 HP; 3 atk; 3 def; move 2; range 0; Amphibious/Dash/Explode/Stiff [WIKI-BOOMCHI] |
| Moth | 5 stars; 10 HP; 2 atk; 0.1 def; move 2; range 1 [WIKI-MOTH] |
| Shaman | 5 stars; 10 HP; 1 atk; 1 def; move 1; range 1 [WIKI-SHAMAN] |

## Historical trap: old Clathrus behavior

Some currently indexed wiki/search text still describes the **pre-rework Clathrus** as a 5-star water building generating +1 income per adjacent Algae. That directly conflicts with the official 2025 rework, which moved Clathrus to land/Fungi and removed its network role. Treat the water/Algae-income form as historical unless a newer first-party source reverses the change. [WIKI-CLATHRUS, OFF-CYM25-DEDICATED]

This is a concrete example of why implementation data must carry a ruleset/version field.

## New Dawn skin: mechanical identity remains Cymanti

The official 2025-12-08 New Dawn article supplies a large cosmetic substitution map. It describes New Dawn counterparts as replacements/renames while preserving Cymanti functions, consistent with skins being cosmetic. [OFF-NEW-DAWN]

Known mappings include:
- Shaman -> Guru
- ordinary rank-and-file -> Hooman theme
- Hexapod -> Top Hat
- Kiton -> Cacti
- Mantis -> Ruby
- Doomux -> Shoo
- Phychi -> Claude
- Exida -> Lily
- Boomchi -> Squishy
- Raychi -> Axolotl
- Living Island -> Super-Sponge
- Moth -> Fairy; its growth forms include Eggy and Kodama
- Algae visual/theme replacement -> Foam
- animal -> Snulle
- fruit -> Pupli Nectar

For a future engine, these should be cosmetic aliases/assets over the same rule IDs rather than separate gameplay definitions.

## Implementation-oriented state model

The public evidence is enough to model several Cymanti mechanics as stateful systems rather than one-off animations:

- tile effects: `algae`, `poison_source`
- unit status: `poisoned`, `swarmed`
- transform timers: Egg -> Larva -> Moth
- transform damage carry-over
- Fungi growth level with Microbes cap override
- movement modifier: poison slow / Algae land slow / mountain penalty despite Creep
- post-attack action availability for Explode

Exact ordering of end-turn growth, poison application, simultaneous effects and transformation still needs reproducible verification before coding.
