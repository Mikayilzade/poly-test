# Tech-action economy: 2025 baseline and version traps

Source grades: **A** = first-party patch, **B** = community Wiki. Values here are *not* direct 2.17.3 measurements.

| Unlock | Action | Effect / cost | Source |
|---|---|---|---|
| Free Spirit | Disband | Refund `floor(unit nominal cost/2)` stars; a super unit has nominal cost 10 and refunds 5. Requires a unit that has not acted; unit and its score disappear. | [WIKI-TECH] |
| Free Spirit | Temple | Field Temple costs 20 stars and provides 1 population. | [WIKI-TEMPLES] |
| Spiritualism | Grow Forest | 5 stars, own empty field without building -> forest; Forest Temple costs 15 stars. | [WIKI-TECH, WIKI-TECH] |
| Construction | Burn Forest | 3 stars in official September 2025 balance, own eligible forest -> crop field; wild animal is forfeited. | [OFF-2025BAL, WIKI-TECH] |
| Chivalry | Destroy | No star cost; immediate removal of building/ruin, removing its population/score benefits. | [WIKI-TECH] |
| Cymanti Recycling | Decompose | Community describes end-turn removal of a building/ruin and full building-cost refund, unlike immediate Destroy. | [WIKI-TECH, OFF-CYM25] |

**Derived, not observed:** forest -> Burn Forest (3) -> Farm (5) costs 8 stars for 2 population; empty field -> Grow Forest (5) -> Burn Forest (3) -> Farm (5) costs 13 stars. Forest Temple on empty field: Grow Forest (5) + Forest Temple (15) = 20 stars, excluding tech costs. [OFF-2025BAL, WIKI-TECH, WIKI-TECH, WIKI-BUILDINGS, WIKI-TEMPLES]

**Contradictions:** Burn Forest Wiki infobox says 3 stars but body says 2; Construction Wiki says 5. Official 2025 balance says **3**. Smithery Wiki still forbids backward research and gives Forge 2 population per Mine; official 2025 explicitly allows Vengir Smithery -> Mining and the developer reverted Forge to 1 population per Mine. Do not import the stale community claims as current rules. [OFF-2025BAL, WIKI-TECH, STEAM-FORGE-REVERT-2025, WIKI-TECH, WIKI-TECH]

**Current-build tests:** Disband after movement/attack, super-unit refund and transported-unit handling; Destroy population-starvation score timing; Decompose before/after turn-end income and simultaneous capture; Burn Forest eligibility and 3-star cost; backward-tech eligibility beyond the Vengir example. Keep `unitActionUsed`, `pendingTileRemoval`, `refund`, `populationDelta` and `scoreDelta` separate in the implementation.

Page-level evidence and URLs are catalogued in `research/source-addenda/2026-10-10-tech-actions.json` (grade B); the main source ledger retains the broader `WIKI-TECH` source ID until safe consolidation.
