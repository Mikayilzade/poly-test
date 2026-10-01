# Aquarion current/post-rework reference

Scope: 2024 Aquarion rework plus later public deltas.

## Rework baseline

Official launch material dates the reworked Aquarion to August 15, 2024 and summarizes amphibious mermaids, Sharks, Jellies and ocean Lost Cities. [OFF-AQ-REWORK]

Developer-maintained 2.10 changelog: [STEAM-AQ-CHANGELOG]
- starts with water movement, an amphibious Mermaid Warrior and no ordinary starting tech;
- native terrain is **Flooded**;
- Flooded supports land/water movement but is rough terrain for naval/water units;
- land roster becomes amphibious counterparts;
- ordinary naval line is replaced by sea creatures;
- Roads -> **Atolls**;
- can flood tiles for waterways/trade;
- Aqua Crop/Aqua Farm access;
- valid water ruins can yield a **Lost City**;
- Burn Forest -> **Fertilize** on suitable flooded fields;
- Catapult -> Puffer with Drench;
- Crab gets Auto Flood;
- the rework also added Landfill/manual-disembark interactions for other tribes.

Official 2.15.1 later says Aquarion can no longer **drain** tiles and others cannot “dash drain”; older Drain guidance is superseded. [STEAM-2151]

## Flooded / Bubbled / Waterways

Current community Waterways documentation says Waterways replaces Roads and grants Atolls; **Bubbled** gives +1 movement after moving onto flooded terrain until attacked or moving onto non-flooded land. [WIKI-ROADS]

Official Bubble Tech post confirms Bubble Tech was added in November 2024, but not the numeric mechanics. [OFF-BUBBLE]

## Atoll

Current community page: cost **5**, aquatic tiles only, connects cities/Atolls through water/ocean/Flooded within **3 tiles**, and currently documents **+1 population**. [WIKI-ATOLL]

Version warning: late 2024 beta explicitly removed Atoll population, while the current wiki documents it again. [STEAM-AQ-BETA, WIKI-ATOLL] Verify current build.

## Lost City

Developer beta/rework notes document water-ruin Lost Cities; an intermediate beta described level 3 + Wall and later added shallow water around them. [STEAM-AQ-BETA] Official launch confirms Lost Cities as a rework feature. [OFF-AQ-REWORK] Current reward probability/starting state remains a black-box target.

## Current unit seed

Recent community pages/tables: [WIKI-AQUARION, WIKI-SHARK, WIKI-PUFFER, WIKI-JELLY, WIKI-TRIDENTION, WIKI-SUPERUNIT]

| Unit | Replaces | Cost | HP | Atk | Def | Move | Range | Key skills |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Mermaid | Warrior | 2 | 10 | 2 | 2 | 1 | 1 | Amphibious, Dash, Fortify |
| Amphibian | Rider | 3 | 10 | 2 | 1 | 2 | 1 | Amphibious, Dash, Escape, Fortify |
| Mermaid Defender | Defender | 3 | 15 | 1 | 3 | 1 | 1 | Amphibious, Fortify |
| Swordsmaid | Swordsman | 5 | 15 | 3 | 3 | 1 | 1 | Amphibious, Dash |
| Siren | Mind Bender | 5 | 10 | 0 | 1 | 1 | 1 | Amphibious, Heal, Convert, Stiff |
| Scuba | Cloak | 8 | 5 | 0 | 0.5 | 2 | 1 | amphibious Cloak analogue |
| Tridention | Knight | 8 | 10 | 2.5 | 1 | 2 | 2 | Amphibious, Dash, Persist |
| Shark | naval role | 8 | 10 | 3.5 | 2 | 3 | 1 | Water, Dash, Surprise |
| Puffer | Catapult | 8 | 10 | 4 | 0 | 2 | 3 | Water, Drench, Stiff |
| Jelly | Bomber role | 8 | 20 | 2 | 2 | 2 | 1 | Water, Tentacles, Stiff, Static |
| Crab | Giant | upgrade | 40 | 4 | 4 | 2 | 1 | Amphibious, Escape, Auto Flood, Static |

Puffer can Drench empty tiles to flood them. [WIKI-PUFFER] Jelly is a defensive contact/adjacency unit rather than a long-range Bomber analogue. [WIKI-JELLY]

Shark's current page documents **3.5 attack**, superseding the 3-attack initial rework changelog value. [WIKI-SHARK, STEAM-AQ-CHANGELOG]

Tridention is range 2 with Persist (not Escape), 2.5 attack and no old Fortify profile. [WIKI-TRIDENTION, STEAM-AQ-CHANGELOG]

## Reproduction cautions

- Do not use pre-rework Tridention 3 attack / Escape / Fortify.
- Do not assume intermediate beta values remained final.
- Separate terrain state (**Flooded**), movement state (**Bubbled**), city-network state (Atolls), and locomotion type (Water/Amphibious).
