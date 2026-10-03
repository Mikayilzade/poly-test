# Polaris and Elyrion — current implementation reference

This pass isolates two special tribes from the generic rules. Values below are community-documented unless an official source is cited; official 2025 changes override older community/history values where they conflict.

## Polaris

### Start and technology substitutions

Polaris starts with **Frostwork** and a **Mooni**. Unlike ordinary tribes, its territory/resource distribution is inherited from the other tribes participating in map generation; an all-Polaris game uses the default/Imperius-style land distribution. [WIKI-POLARIS]

Current substitution map: [WIKI-POLARIS]

| Technology | Replaces / modifies | Unlocks |
|---|---|---|
| Frostwork | Fishing | Mooni, Outpost |
| Sledding | Sailing | Battle Sled |
| Ice Fishing | Aquaculture | Fishing action |
| Polar Warfare | Navigation | Ice Fortress, Gather Stars |
| Polarism | Aquatism | Ice Temple, Glide |
| Archery | modified ordinary tech | Ice Archer + forest defence |
| Trade | modified ordinary tech | Ice Bank + Wealth |

### Unit table

| Unit | Replaces | Cost | HP | Atk | Def | Move | Range | Skills |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Mooni | Raft | 5 | 10 | 0 | 1 | 1 | 1 | Auto Freeze, Skate, Stiff, Static |
| Ice Archer | Archer | 3 | 10 | 1 | 1 | 1 | 2 | Dash, Freeze, Fortify, Stiff |
| Battle Sled | Scout | 5 | 15 | 3 | 2 | 2 | 1 | Dash, Escape, Skate |
| Ice Fortress | Bomber | 15 | 20 | 4 | 3 | 1 | 2 | Skate, Scout, Escape, Static |
| Gaami | Giant | upgrade | 30 | 4 | 3 | 1 | 1 | Auto Freeze, Freeze Area, Static |

[WIKI-POLARIS, WIKI-MOONI, WIKI-BATTLE-SLED, WIKI-ICE-FORTRESS, WIKI-GAAMI]

The 2025 official balance pass is important for versioning this table: Ice Archer attack became 1; Ice Fortress gained Escape and Static; Skate was corrected so Battle Sled reaches 3 movement on ice rather than 4; Glide adds one move instead of doubling movement. [OFF-2025BAL]

### Freeze behavior

Mooni cannot deal ordinary attack damage. Its role is terrain freezing; current documentation gives it Auto Freeze. Gaami automatically freezes adjacent tiles/enemies after moving and also exposes a Freeze Area action. A frozen enemy cannot retaliate while frozen. [WIKI-MOONI, WIKI-GAAMI]

Implementation note: **frozen terrain** and the **Frozen unit status** must be separate state. Ice is traversable terrain with Polaris-specific movement effects; freezing an enemy disables its action/retaliation state.

2.16.3 records a subtle movement fix: attacking while skating on ice must not accidentally grant extra movement; a Battle Sled killing from land into ice should retain Escape. Treat this as an explicit regression test when movement is implemented. [OFF-2163]

### Outpost

Outpost replaces the Port. It costs **5**, gives **1 population**, can only be built on ice, and forms city connections to other Outposts no more than **five ice tiles away**. [WIKI-OUTPOST]

Historical warning: launch-era Outposts gave 2 population. That value is obsolete. [WIKI-OUTPOST]

### Ice Bank

Ice Bank replaces the Market and is limited to one per Polaris player. Current community documentation gives: **20-star cost**, buildable on field/ice, +2 SPT for every 20 frozen land/ice tiles in the world, maximum level 30. Frozen tiles count regardless of which Polaris player created them. [WIKI-ICE-BANK]

Path-of-the-Ocean history reduced income from 3 to 2 stars per level. Any aggregate building table still saying +3 is stale. [WIKI-ICE-BANK]

### Solaris skin mapping

Solaris remains mechanically Polaris but renames/reskins much of the freeze system: Ice→Lava, Frozen→Petrified, Mooni→Pyro, Battle Sled→Steam Wagon, Ice Fortress→Steam Fortress, Gaami→Ralmi, Outpost→Crater, Ice Bank→Lava Bank, Frostwork→Heatwork, Sledding→Steam Engine, Polarism→Magmaism and Polar Warfare→Explosives. [WIKI-POLARIS]

Official 2025 notes specifically fixed Solaris Crater and Lava Bank state when territory changes owner, confirming these are skin presentations of Polaris mechanics rather than independent rule objects. [OFF-2025BAL]

## Elyrion

### Start and rule substitutions

Elyrion starts with **Forest Magic** and a Warrior. Forest Magic replaces Hunting and exposes Enchant Animal. Elyrion cannot harvest wild animals for population; enchanting an animal creates a Polytaur. Forestry additionally unlocks Sanctuary, and Elyrion does not receive Clear Forest; Construction does not grant Burn Forest. Elyrion can detect ruins through unexplored clouds via a rainbow-flame indicator. [WIKI-ELYRION]

### Polytaur

Enchanting a wild animal costs **3 stars** after the official 2025 balance increase. The resulting Polytaur is not city-trained. Current stats: HP 15, attack 3, defence 1, move 1, range 1; Dash, Fortify, Independent, Static. [OFF-2025BAL, WIKI-POLYTAUR]

### Dragon state machine

A level-5+ Elyrion city can choose its super-unit reward as a Dragon Egg rather than a Giant. The growth chain is deterministic: [WIKI-DRAGON-EGG, WIKI-BABY-DRAGON, WIKI-FIRE-DRAGON]

| Stage | HP | Atk | Def | Move | Range | Skills | Growth |
|---|---:|---:|---:|---:|---:|---|---|
| Dragon Egg | 10 | 0 | 2 | 1 | 1 | Grow, Fortify, Stiff, Static | Baby Dragon after 3 turns |
| Baby Dragon | 15 | 3 | 3 | 2 | 1 | Air, Grow, Dash, Escape, Scout, Static | Fire Dragon after 3 more turns |
| Fire Dragon | 20 | 4 | 3 | 3 | 2 | Air, Dash, Splash, Scout, Static | final |

Damage is inherited across growth rather than healed away. An Egg can continue its growth timer while transported in a Raft but cannot transform into the flying Baby Dragon while still in that transport state. [WIKI-DRAGON-EGG]

Fire Dragon Splash applies half of the regular damage dealt to the primary target, rounded down, to adjacent enemies. [WIKI-FIRE-DRAGON]

Implementation model should therefore store dragon **age/growth counter independently of current form HP**, and transform without resetting damage.

### Sanctuary

Sanctuary costs **5**, unlocks with Forestry, is limited to one per city, and can be placed on field, forest or mountain. It earns **+1 SPT for each adjacent wild animal in the player's territory**. If an adjacent empty forest is eligible, the Sanctuary attracts one animal to a random eligible forest every **three turns**. [WIKI-SANCTUARY]

This means animal entities/resources are persistent economic state for Elyrion; enchanting one into a Polytaur can reduce Sanctuary income. The attraction timer/random eligible-forest selection needs its own deterministic simulation rule rather than being treated as a static building yield.

### Removed historical unit

Navalon is still visible in some historical/community tables, but Path of the Ocean removed it from the current Elyrion ruleset. Do not include Navalon in a current implementation table except as historical data. [WIKI-ELYRION]

## Cross-version tests to preserve

1. Polaris Outpost produces 1 population, not historical 2. [WIKI-OUTPOST]
2. Ice Bank produces 2 stars/level, not historical 3. [WIKI-ICE-BANK]
3. Current Ice Archer has 1 attack even though its attack action freezes rather than dealing ordinary damage. [OFF-2025BAL, WIKI-POLARIS]
4. Battle Sled ice movement follows the 2025 corrected Skate rule and the 2.16.3 Escape edge case. [OFF-2025BAL, OFF-2163]
5. Polytaur enchant cost is 3, not older 2. [OFF-2025BAL]
6. Dragon growth takes 3 + 3 turns and carries damage. [WIKI-DRAGON-EGG]
7. Navalon is historical/removed after Path of the Ocean. [WIKI-ELYRION]
