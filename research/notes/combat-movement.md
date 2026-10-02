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

Official 2.16.3 says Explorer path steps were reduced from 15 to **12**. Older wiki text still says 15, which is a confirmed stale-data example. Official 2.15.1 additionally says Explorer pathfinding includes **mountains** and considers **increased sight range** when evaluating which tile to move toward. This constrains the chooser but does not reveal its complete scoring or tie-break algorithm. [OFF-2163, STEAM-2151]


## Forced super-unit spawn / push ordering

Spawning a super unit in an already occupied city forces the previous unit out. Current community documentation confirms the forced-spawn mechanic. [WIKI-SUPERUNIT]

A 2020 developer explanation gives the exact public directional algorithm located so far. For a unit that **has not moved yet** (the example is a newly spawned unit), preferred direction is toward the center of the map. If that direction is north, fallback order is:

`N -> NW -> NE -> W -> E -> SW -> SE -> S`

If every candidate tile is invalid, the displaced unit disappears. [DEV-PUSH-2020]

For an **enemy unit that already moved into the city**, the developer confirmed a different rule: push opposite its previous movement direction. In the documented example the unit moved south into the city and was pushed north. [DEV-PUSH-2020]

Current-build forced-spawn existence is corroborated, but the exact 2020 ordering should still receive a fixed-map regression test before being treated as immutable.

### Creep / ZOC documentation conflict

The current community documentation contradicts itself: the Movement page's general ZOC section says Creep bypasses ZOC, while a later Creep subsection on the same page says Creep does **not** remove ZOC; Unit Skills also says Creep does not negate ZOC. Cloak-specific text further mixes Creep with Hide, which independently bypasses ZOC. [WIKI-MOVE, WIKI-UNIT-SKILLS, WIKI-CLOAK]

Resolve this with a current-build black-box test using a Creep unit that lacks Hide/Sneak rather than choosing one wiki sentence.


## First-party tactical UI and vision rules

- A unit standing on a mountain explores two tiles around it instead of only bordering tiles. [WIKI-MOVE]
- Exploration knowledge is player-relative: opponents do not necessarily see the same tiles, so troops can be concealed on tiles that opponent has not explored. [WIKI-MOVE]
- An eye icon next to a unit indicates that a Cloak is nearby. [WIKI-CLOAK]
- After three enemy kills, a unit can be promoted to Veteran; promotion adds 5 maximum health and fully heals it. [WIKI-UNITS]

Implementation note: keep explored-map state per player. Treat the eye icon as evidence of a nearby Cloak, but source exact detection geometry separately. Veteran promotion should remain an action/state transition rather than being assumed automatic on the third kill.


## Battle Preview UI contract

Midjiwan documents a built-in Battle Preview interaction: hover over or hold on the enemy being targeted to preview the expected HP change for both units. The target visibly sweats when the preview predicts its removal; a skull appears when the attacking unit is predicted to be removed by the exchange. [OFF-BATTLE-PREVIEW]

Implementation boundary: this is presentation derived from the prospective combat result, not a separate combat rule. A tactical assistant can use the same damage resolver to reproduce the preview and outcome indicators without mutating game state.
