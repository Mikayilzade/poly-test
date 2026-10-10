# Polytopia 2.16.3 — remaining regression contracts

First-party evidence: Midjiwan's 2026-02-16 patch notes [OFF-2163]. These are bug-fix descriptions, not complete current 2.17.3 rules.

- **City capture during cooldown:** a prior build incorrectly allowed capture in an unspecified cooldown state. The patch fixes it. The affected cooldown, its owner and duration are not documented. Test capture eligibility with controlled cooldown states; do not assume all movement blocks capture.
- **Bridge destruction:** a destroyed Bridge could leave a road graphic on an Ocean tile. Separate bridge removal, road overlay redraw, connection-graph recomputation and movement legality. The source does not say the underlying Road remained traversable.
- **Ice Archer Battle Preview:** an incorrect prediction was fixed. Compare preview and actual attack/freeze resolution against different defence states; the patch supplies no numerical formula. [OFF-2025BAL]
- **Last-turn Escape:** Escape-key deselection was fixed for the final turn of Perfection and Weekly Challenge. Test non-consuming deselection independently of end-turn restrictions; other modes and controller mappings are unspecified.

Open: confirm the affected states and whether all fixes persist in 2.17.3. Do not generalize from patch titles.
