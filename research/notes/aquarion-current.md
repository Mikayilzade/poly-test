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

## August-to-November 2024: first-party Lost City and Forgotten update contracts

**Water-ruin Lost City eligibility (August 8 release-era description, grade A).** Aquarion can receive a Lost City from a ruin on either shallow **Water** or **Ocean**, **only if the ruin is sufficiently far from other cities to permit city placement**. If it is too close, the ruin gives an **ordinary ruin reward** instead. This is a conditional placement test, not an unconditional water-ruin-to-city conversion. The official description does **not** publish the minimum distance, whether the test uses city centers/borders, or the order of other reward filters. [OFF-AQ-AUG24-DETAIL]

**November 4 Forgotten patch (grade A, post-August launch):**

- **Waterways** unlocks automatic **Bubbles** for Aquarion **Amphibious** units upon moving onto **Flooded** terrain. Bubbled gives **+1 movement** and is removed on attack or on stepping onto land; **Water-only** units such as Sharks do not get this bonus. The official text does not specify whether the movement increase affects remaining movement in the triggering action, whether attacking removes the bubble before/after combat, or how the status persists between turns. [OFF-AQ-NOV24-PATCH]
- **Atoll** improvement unlock moved **from Waterways to Aquaculture**. Do not derive its current prerequisite from the June/August rework notes or the community Waterways summary. [OFF-AQ-NOV24-PATCH]
- Aquarion starts with **two guaranteed fish** in its capital area. The patch does not specify exact tiles, map-type exceptions, or whether “in the capital” means the starting city territory rather than the center tile. [OFF-AQ-NOV24-PATCH]
- **Lost Cities** from water ruins became **smaller** and gained **surrounding resources**. This supersedes the older spatial/resource presentation; exact radius, resource generation and retention of the earlier level-3 + Wall payload are not stated in this patch. [OFF-AQ-NOV24-PATCH]
- **Crab defense 5 → 4; Shark attack 3 → 3.5; Jelly attack 0 → 2**, enabling normal Jelly attacks. For multiple Tentacles affecting one tile, **the strongest Tentacle performs the attack**. “Strongest” is not formally defined as base attack, remaining HP, or effective damage; exact tie handling remains unknown. [OFF-AQ-NOV24-PATCH]

These are official **2024** contracts, not direct proof that all details are unchanged in **2.17.3**. Keep the original August baseline and the November supersessions separate, then verify current state in-game. [OFF-AQ-AUG24-DETAIL, OFF-AQ-NOV24-PATCH]

## Flooded / Bubbled / Waterways

The current community Waterways description still associates Atolls with Waterways, but the **official November 2024 patch moved Atolls to Aquaculture**. Treat that community unlock text as potentially stale. The official Bubbled contract is restricted to **Amphibious** units, not all Aquarion units; see the versioned patch details above. [WIKI-ROADS, OFF-AQ-NOV24-PATCH]

Official Bubble Tech post confirms Bubble Tech was added in November 2024, but not the numeric mechanics. [OFF-BUBBLE]

## Atoll

Current community page: cost **5**, aquatic tiles only, connects cities/Atolls through water/ocean/Flooded within **3 tiles**, and currently documents **+1 population**. **Tech prerequisite:** official November 2024 patch moved Atolls to **Aquaculture**, superseding the initial Waterways unlock. [WIKI-ATOLL, OFF-AQ-NOV24-PATCH]

Version warning: beta 2.10.0.12669 removed Atoll population; beta 2.10.0.12709 then removed the **one-Atoll-per-city placement limit**. The current wiki documents +1 population again, but the public launch changelog does not document when or whether that value returned. [STEAM-AQ-BETA, WIKI-ATOLL] Verify current build.

## Lost City

Developer beta/rework notes document water-ruin Lost Cities. Beta 2.9.2.1249 described a **level 3 city + Wall** baseline; beta 2.10.0.12709 added **shallow water around the Lost City on spawn** plus a new animation. [STEAM-AQ-BETA] Official launch confirms Lost Cities as a rework feature. [OFF-AQ-REWORK] Official August 2024 notes additionally require a **valid city placement** (otherwise an ordinary ruin reward), for either Water or Ocean ruins. The November patch says Lost Cities became **smaller** and acquired **surrounding resources**. The placement-distance threshold, precise resource pattern and whether level 3 + Wall persisted remain black-box targets. [OFF-AQ-AUG24-DETAIL, OFF-AQ-NOV24-PATCH]

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
- Do not grant Bubbled movement to Sharks, use Waterways as the post-November Atoll prerequisite, or assume all Aquarion water ruins always create cities. [OFF-AQ-AUG24-DETAIL, OFF-AQ-NOV24-PATCH]
