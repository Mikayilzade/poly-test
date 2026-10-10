# Naval units — current community baseline (version check pending)

The numbers below are from community documentation (grade B), checked against official 2023 Path of the Ocean and 2024 Patch of the Ocean announcements. They are not verified against 2.17.3. [WIKI-UNITS, OFF-POTO-RELEASE-2023, OFF-PATCH24-STEAM]

| Unit | Origin/cost | HP | Attack | Defence | Move | Range |
|---|---|---:|---:|---:|---:|---:|
| Raft | ordinary unit enters Port | carried | 0 | 1 | 2 | 0 |
| Rammer | Raft +5 stars | carried | 3 | 3 | 3 | 1 |
| Scout | Raft +5 stars | carried | 2 | 1 | 3 | 2 |
| Bomber | Raft +15 stars | carried | 3 | 2 | 2 | 3 |
| Juggernaut | Giant enters Port | 40 | 4 | 4 | 2 | 1 |
| Dinghy | Cloak enters Port | 5 | 2 | 0.5 | 2 | 1 |
| Pirate | Dagger enters/spawns on Port | 10 | 2 | 2 | 2 | 1 |

[WIKI-UNITS, WIKI-RAFT-DETAIL, WIKI-RAMMER-DETAIL, WIKI-SCOUT-DETAIL, WIKI-BOMBER-DETAIL, WIKI-DINGHY-DETAIL, WIKI-PIRATE-DETAIL]

Raft upgrades are restricted to friendly territory and **do not heal** carried HP. Disembarking from Rammer/Scout/Bomber loses the hull upgrade; re-entering Port produces a Raft. Dinghy and Pirate cannot upgrade. Dinghy can infiltrate adjacent cities; Pirate may spawn if no empty land tile is available inside an infiltrated city's borders. [WIKI-RAFT-DETAIL, WIKI-DINGHY-DETAIL, WIKI-PIRATE-DETAIL]

Bomber Splash secondary damage is reported as floor(primary target damage / 2), **not** a separate combat calculation with half attack. This requires direct testing. Bomber has Stiff (no retaliation). Official 2024 patch reduced its attack from 4 to 3. [WIKI-BOMBER-DETAIL, OFF-PATCH24-STEAM]

**Conflicts:** Scout's own wiki header says Fishing while its prose says Sailing. Rammer/Raft pages say Aquaculture, but the ordinary naval tech branch changed in 2024. Do not hard-code these unlock labels without current-game verification. [WIKI-SCOUT-DETAIL, WIKI-RAMMER-DETAIL, WIKI-RAFT-DETAIL, OFF-PATCH24-STEAM]

**Tests:** verify 2.17.3 unlock labels, territorial upgrade eligibility, HP/status persistence, disembark/Port transitions, Pirate spawn fallback, Bomber splash rounding, and special-tribe replacements.
