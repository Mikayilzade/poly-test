# Poison recovery and movement — secondary evidence

The community Combat reference states that Poison halves defence while preserving terrain/wall bonuses, subtracts 1 movement (minimum 1), and blocks HP healing. Recover, Mind Bender healing and Mycelium remove Poison but restore zero HP on that cure action. A poisoned unit's death can produce Spores on land or Algae on water, subject to resource-tile exclusions. [WIKI-COMBAT]

The official 2025 Cymanti rework confirms the 50% defence reduction, continued defence bonuses and movement slowdown, but does not specify the movement floor, recovery ordering or death-tile exceptions. These remain grade-B current-page claims pending a 2.17.3 client test. [OFF-CYM25, WIKI-COMBAT]

Test: Poisoned movement 1/2/3 with roads; self-Recover/Mind Bender/Mycelium HP-vs-status transition; full-HP poisoned unit cure availability; death on resource-bearing land and water; simultaneous splash deaths. Do not implement undocumented tie-breaking or overwrite rules.
