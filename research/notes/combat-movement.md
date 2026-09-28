# Combat, movement, vision and unit skills

Community-sourced implementation notes. Current-build verification remains required for edge cases. [WIKI-COMBAT, WIKI-MOVE, WIKI-UNIT-SKILLS]

## Damage model

The wiki documents health-scaled attack and defence forces:

```text
attackForce  = attacker.attack  * attacker.health / attacker.maxHealth
defenseForce = defender.defense * defender.health / defender.maxHealth * defenseBonus
totalDamage  = attackForce + defenseForce
attackResult = round((attackForce  / totalDamage) * attacker.attack  * 4.5)
defenseResult= round((defenseForce / totalDamage) * defender.defense * 4.5)
```

Reported defence bonus multipliers:
- no bonus: 1
- ordinary terrain/city bonus: 1.5
- city wall: 4

The wiki reports altered effective defence multipliers for poisoned defenders: 0.5 / 0.7 / 2 for the corresponding states. This should be tested against the current 2025 poison rework before implementation. [WIKI-COMBAT, OFF-CYM25]

Splash/explosion damage is reported as half of the computed attack result, and community documentation notes fractional-HP display edge cases. [WIKI-COMBAT]

## Retaliation / kill movement / healing

- Defender retaliates unless prevented by range/visibility/skills or killed by the initial attack.
- A melee attacker that kills an adjacent defender normally occupies the defeated unit's tile, subject to movement/terrain constraints.
- Ranged units do not advance after a kill.
- Self-heal instead of acting: up to 4 HP in friendly territory, 2 HP elsewhere.
- Mind Bender Heal Others: up to 4 HP to adjacent friendly units. [WIKI-COMBAT]

## Defence terrain

Standard defence bonus is documented for:
- forest after Archery
- mountain after Climbing
- shallow water and ocean after Aquatism
- friendly city for units with Fortify
- city wall as the stronger city bonus

Giant lacks Fortify and therefore does not receive city/city-wall defence solely from occupying a city. [WIKI-COMBAT]

## Movement model

Base geometry uses Chebyshev distance. Ordinary adjacent movement costs 1. Movement between connected road tiles costs 0.5. [WIKI-MOVE]

Rough terrain such as forest and mountain normally stops further movement after entering (unless a relevant skill modifies this). Units cannot move into unexplored cloud tiles. [WIKI-MOVE]

### Zone of control

An enemy unit exerts zone of control on adjacent tiles. Entering an enemy ZOC normally ends further movement even if movement points remain. The current movement page distinguishes:
- **Creep**: ignores terrain barriers except mountains, but according to current text does *not* negate ZOC.
- **Sneak**: ignores enemy ZOC but cannot pass through occupied enemy tiles.
- **Hide**: ignores ZOC and may move through enemy units while hidden.

This area changed during the 2025 Cymanti rework, so special-unit behavior must be tested rather than inferred from old guide text. [WIKI-MOVE, WIKI-UNIT-SKILLS, OFF-CYM25]

### Roads and bridges

Road:
- cost: 3 stars
- field/forest, plus neutral village cases; not mountain/water/ice
- halves movement cost along road-connected movement
- connects cities
- no benefit from enemy roads; peaceful tribes can use one another's roads
- other buildings may coexist on road tiles [WIKI-ROADS]

Bridge follows road-like movement/connection rules across a one-tile orthogonal water gap. [OFF-OCEAN, WIKI-BUILDINGS]

## Port transformation

Current community docs:
- Port costs 7 stars and gives 1 population.
- Port participates in water city connections.
- moving most land units onto own/friendly usable Port turns them into a Raft;
- Giant -> Juggernaut, Cloak -> Dinghy, Dagger -> Pirate;
- some floating/flying units are exceptions. [WIKI-PORT]

Raft seed stats: Atk 0, Def 1, Move 2, range 0, HP inherited from carried unit; skills Water/Carry/Stiff/Static. It may upgrade in friendly territory into Rammer/Scout/Bomber when corresponding tech is available. [WIKI-UNITS]

## High-value skill semantics

- Dash: attack/break ice after moving.
- Escape: move after attacking.
- Persist: attack again after a kill, repeatable.
- Fortify: may receive city defence bonus.
- Stiff: no retaliation.
- Static: cannot become veteran.
- Scout: 5×5 vision rather than normal 3×3.
- Splash: affects enemies adjacent to target.
- Surprise: attacking does not trigger retaliation.
- Hide: invisibility + movement through ZOC/enemy units.
- Infiltrate: enemy-city revolt mechanic.
- Freeze / Freeze Area: unit/tile freezing actions.
- Heal: adjacent friendly heal action.
- Grow: transforms after a turn count.
- Explode: self-destruct AoE; Cymanti-related variants can poison/create spores/algae.
- Independent: does not consume a city population/unit-capacity slot.
- Stomp: damages adjacent enemies on movement.
- Tentacles: contact/adjacency reactive damage.
- Double Attack: two attacks in a turn with restricted action handling after the first.
- Swarm: movement buff to adjacent allies until they are attacked. [WIKI-UNIT-SKILLS]

## Vision / Explorer

Normal unit vision is generally a 3×3 area; Scout skill expands this to 5×5, and mountains give extended vision. [WIKI-COMBAT, WIKI-UNIT-SKILLS]

Official 2.16.3 says Explorer path steps were reduced from 15 to **12**. Older wiki text still says 15, which is a confirmed stale-data example. Explorer path-choice logic remains unknown. [OFF-2163]
