# Cymanti current mechanics — post-2.15 rework

This note isolates publicly documented current/post-rework Cymanti behavior from older guides. The primary source is Midjiwan's official 2025 Cymanti rework post. [OFF-CYM25]

## Algae, water movement and networks

- **Algae is a tile effect, not an improvement.** Improvements can therefore be built on top of an Algae tile. [OFF-CYM25]
- Creating Algae does **not** itself grant population; the rework instead specifies that spawned Algae carries a fruit resource. The official text names Aphea Nectar, while a later official Admin reply acknowledged that regional fruit could appear and called that behavior unintended. Treat the release-era regional-fruit result as an observed discrepancy, not the intended rule. [OFF-CYM25]
- Algae no longer slows naval units, but still slows land units. [OFF-CYM25]
- **Mycelium can be built on Algae.** Clathrus no longer supplies network connections. [OFF-CYM25]
- Cymanti Explorers can move on water like ordinary-tribe Explorers. [OFF-CYM25]

Implementation boundary: Algae should be modeled as a tile state/effect that can coexist with another improvement and a resource, rather than as the improvement occupying the tile's building slot.

## Naval roster changes

- The old Raychi role was split. **Boomchi** owns the explosive/algae-creation role and has **Amphibious**, allowing land movement; Raychi remains as a more conventional naval unit. [OFF-CYM25]
- The **Living/Floating Island** is the Cymanti Navigation-era heavy naval unit. The prose calls it **Living Island**, while the full changelog calls it **Floating Island**; treat these as first-party naming variants for the same described role unless current-build UI proves otherwise. It creates fruitless Algae while moving and deals area damage; the official explanation frames it as Cymanti's functional answer to the Juggernaut and as support for moving land armies across water. [OFF-CYM25]
- Exact numerical stats, algae-spawn footprint/order and area-damage formula are not established by this source and remain open.

## Fungi, Creep and poison

- Fungi are capped at **level 2** by default. The **Microbes** ability unlocked through Recycling permits one additional level, for level 3. [OFF-CYM25]
- **Creep no longer cancels the mountain movement penalty.** Kiton and Mantis have Creep after the rework. [OFF-CYM25]
- Poison's defense debuff is **50%**, while ordinary defense bonuses remain applicable; poison also slows enemy units. [OFF-CYM25]
- Do not interpret the 50% debuff as removal of city-wall or terrain defense: the official post explicitly distinguishes those systems. Exact multiplication/rounding order should remain tied to reproducible combat evidence.

## Unit/action changes

- **Mantis** replaces Swordsman with the same base role/stats plus Creep. [OFF-CYM25]
- **Phychi** has Double Attack. [OFF-CYM25]
- Explode-capable units may **Explode after attacking**. [OFF-CYM25]
- Doomux cannot become Veteran and has **3.5 attack** in this rework. [OFF-CYM25]
- Shaman **Boost** became **Swarm**: it buffs movement only, not damage, and the movement buff persists until the affected unit is attacked. [OFF-CYM25]
- Shaman moved to the Meditation branch (renamed **Rituals** in the Cymanti presentation) and Mountain Temple moved to Philosophy (**Mysticism** in that presentation). [OFF-CYM25]

## Moth → Egg → Larva lifecycle

The ordinary Cloak/Dagger branch is replaced by a growth cycle: [OFF-CYM25]

1. **Moth** can fly and infiltrate cities, but has no Hide skill and therefore is not invisible.
2. Infiltration poisons the city's defenses and lays **Eggs** instead of spawning Daggers.
3. Eggs cannot move, but can Explode.
4. After **1 turn**, surviving Eggs hatch into **Larva**.
5. After **3 more turns**, surviving Larva transform into **Moths**.

The official 2.15.1 follow-up further establishes that mind-bent Larva can still mature into Moths and mind-bent Moths spawn Eggs rather than Daggers. [STEAM-2151]

Open: exact Egg count/placement priority, whether every ordinary infiltration limiter maps unchanged to Moth, and timing at turn-boundary granularity.

## Transformation damage inheritance

Growing/transformation units inherit existing damage instead of healing to full. The official rework explicitly names Centipede heads, dragons and Larva as examples. [OFF-CYM25]

Implementation inference: preserve **damage taken** across a growth transform, then derive resulting HP from the new form's maximum HP rather than treating transformation as a heal. The exact clamp behavior when the new form has lower maximum HP is not documented here.

## Converter task

Cymanti's Pacifist task is replaced by **Converter**: converting **3 enemies** unlocks the **Church of Converts** monument. [OFF-CYM25]

## Remaining black-box targets

- complete current numeric table for Raychi, Boomchi, Living/Floating Island, Moth, Egg and Larva;
- exact poison slow movement arithmetic and poison/defense rounding;
- Living Island algae footprint, movement-trigger timing and area-damage targeting;
- Moth infiltration spawn count/placement and all ordinary-city infiltration restrictions;
- transform timing under freeze, poison, mind-bend and forced movement;
- current fruit identity on newly created Algae in the 2.16.x line.
