# Update baseline and high-impact deltas

This file tracks rules changes that invalidate older guides/screenshots.

## 2023–2024: Path of the Ocean / Patch of the Ocean

Official Path of the Ocean material documents: [OFF-OCEAN]

- Raft replaces the old basic Boat concept and transports a land unit.
- In friendly territory a Raft can upgrade into **Scout, Rammer, or Bomber**.
- Bomber is long-range and uses **Splash** damage; it is slow and lacks Dash.
- Starfish replace whale hunting as a recoverable star source that must be reached.
- Lighthouse objects appear at world edges; discovery grants capital population and tracks tribe discovery visually.
- Pangea map type.
- Custom House redesigned into **Market**; Market levels with unique adjacent Sawmill/Windmill/Forge and has doubled income beside a Port.
- Sailing/Fishing positions were swapped and Port access made cheaper/easier.
- Roads tech can construct one-tile orthogonal **Bridges** over water gaps; no diagonal bridges.
- Aqua Crop / Aquaculture introduced as water-resource development.

A March 2024 “Patch of the Ocean” followed with simplifications/adjustments; exact delta still needs extraction. [OFF-OCEAN, OFF-BLOG]

## 2024: Patch of the Ocean (2.8.5.11917) — superseding 2023 naval rules

Midjiwan's official Steam announcement dated **2024-02-26** publishes the **2.8.5.11917** changelog; its own site announces the Patch of the Ocean release on **2024-03-14**. Keep the preview/announcement and release dates distinct. The following are first-party **2024** rules, not an independently verified 2.17.3 specification. [OFF-PATCH24-STEAM, OFF-PATCH24-RELEASE]

- **Removed Aqua Crop/Aqua Farms** from the regular naval economy; Fishing became the first naval technology and included Ports. This supersedes the 2023 Path of the Ocean Aqua Crop/Aquaculture introduction. Special-tribe Aquarion substitutions must be modeled separately; do not globally prohibit its Aqua Farms. [OFF-PATCH24-STEAM, STEAM-AQ-CHANGELOG]
- **Markets** stopped doubling income next to Ports and instead earned **+1 star/turn for each level** of adjacent Windmills, Sawmills and Forges, with **Market level capped at 8**. The old 2023 unique-type/Port-doubling rule is historical only. [OFF-PATCH24-STEAM]
- **Bridges** fell to **5 stars**; bridge placement can reach a valid shore concealed by fog, and faint coastlines hint at eligible hidden land. **Lighthouses** begin under fog even when close to a corner-spawn capital. [OFF-PATCH24-STEAM]
- **Bomber attack** fell **4 → 3**. **Starfish harvesting** fell **10 → 8 stars**. A water ruin's veteran naval-unit reward changed **Bomber → Rammer**. These are patch-era numeric and reward-table deltas, not evidence that every special-tribe ruin reward follows the same table. [OFF-PATCH24-STEAM]
- **Temples** grew every **2 turns instead of 3**; the earlier 2020 12-turn-to-full-growth claim cannot be used as a current timing guarantee. Exact age-zero/upgrade-phase accounting and any later 2.17.x changes remain unverified. [OFF-PATCH24-STEAM, OFF-TEMPLE-GROWTH-2020]
- **Burn Forest** moved to Construction, **Destroy** to Chivalry. The Perfection opponent-count score multiplier was reduced, but the new numeric multiplier was not published. AI was reported to choose training/city improvements better and train fewer Cloaks; this does **not** specify an AI algorithm or numeric spawn probability. [OFF-PATCH24-STEAM]

Implementation boundary: keep naval resource availability, tech placement, Market calculation, ruin reward tables and Temple growth intervals versioned. In particular, do not combine the **2023** 10-star Starfish/Port-doubled Market/three-turn Temple with **2024+** state or assume 2024 values survived unchanged through **2.17.3**.

## 2022: Diplomacy

Official Diplomacy material documents: [OFF-DIP]

- Shields was renamed **Strategy**.
- Strategy retains Defender training and adds peace-treaty capability.
- **Diplomacy** tech follows Strategy.
- Diplomacy introduced Cloaks, Daggers, Embassies and capital vision.
- Tribe Relations UI explains relationship factors.
- Peace Treaties persist until a party cancels.

Later balance notes changed details (for example detection/infiltration limits), and special tribes may replace the branch, so the final spec must be versioned. [OFF-DIP, OFF-BLOG]

## 2025 balance pass

Official 2025 balance pass: [OFF-2025BAL]

- Ai-Mo begins with Philosophy and a Mind Bender instead of Meditation.
- Starting-star exceptions: Xin-xi 7, Oumaji 6, Hoodrick 7, Quetzali 7, Yădakk 7; Luxidoor gets 2 stars in addition to upgraded capital; others 5.
- Tech may be researched backwards in a branch.
- Forges may be built on Forests.
- Temples: 100 points per growth level instead of 50.
- Burn Forest cost reduced to 3.
- Polytaur cost increased to 3.
- Embassy cost starts cheaper and rises based on embassy count.
- Polaris movement/skill changes include Glide/Skate corrections, Ice Fortress Escape+Static, Ice Archer attack.
- Multiplayer fallbacks and some Solaris territory-state issues were fixed.

## 2025 Cymanti rework

Official blog documents a large Cymanti rework. Initial extracted points: [OFF-CYM25]

- Explorer can travel water like other tribes.
- Naval tech placement updated for Path of the Ocean.
- Algae becomes a tile effect and can coexist with improvements.
- Clathrus moves to land/spores; Mycelium can be built on Algae.
- Raychi split/adjusted; Boomchi added with explosion/algae and amphibious behavior.
- Floating/Living Island naval unit introduced in Navigation with algae + area damage.
- Mantis replaces Swordsman with creep behavior.
- Fungi growth limited, with an additional Microbes/Recycling interaction.
- Growing units inherit damage when transforming.
- Kiton gets Creep; Creep no longer ignores mountain movement penalty.
- Phychi gets double attack.
- Poison defense debuff strengthened; poison also slows enemies.
- Explode units may explode after attacking.
- Doomux cannot become veteran; attack reduced.
- Diplomacy analogue: Moth replaces Cloak; infiltration poisons defenses and lays Eggs; Eggs hatch to Larva; Larva later become Moths.
- Shaman Boost replaced by Swarm movement buff; buff persists until attacked.
- Shaman/temple tech locations changed.
- Pacifist task replaced by Converter task/monument.

Exact stats, turn counters and prerequisites still need atomization.

## 2026 version 2.16.3

Official numbered changelog dated 2026-02-16: [OFF-2163]

- new visuals for status effects and splash damage;
- New Dawn color tweaks;
- Explorer moves 15 → 12;
- fixes involving invisible-unit hints, replay centipede connector, frozen/flooded tile transitions, Skate+attack movement, and language refresh.

### Flood / freeze state boundary

The changelog makes two tile-state transitions explicit: **freezing an already flooded tile must not drain it**, and **changing a frozen tile's climate must not itself flood that tile**. [OFF-2163]

Implementation inference: flooded/water state, frozen state and climate/terrain presentation should not be collapsed into one destructive terrain conversion. Preserve the underlying flooded state across freeze, and do not synthesize flood merely from a climate change while frozen. Exact thaw ordering and all Polaris/Aquarion interactions remain unresolved.

This is the newest explicit version number located in the first research pass; later 2026 official news exists, so the update sweep remains open.


## 2026 mobile release-history baseline after 2.16.3

The official Midjiwan App Store listing establishes that **2.16.3 is no longer the newest explicit public version baseline**. The iOS history continues through 2.16.5/2.16.6/2.16.8 and the 2.17 line, with **2.17.3 dated 2026-09-07**. [APPSTORE-IOS-2026]

Mechanically relevant deltas exposed by that history:
- **2.16.5:** Splash damage is floored, specifically to avoid half-hit-point damage. Treat splash resolution as integer-flooring at the documented stage rather than allowing fractional HP. [APPSTORE-IOS-2026]
- **2.16.5:** choosing a random tribe had a wrong-climate bug; the fix is evidence that random-tribe selection must still resolve the selected tribe's proper climate rather than retaining an unrelated/default climate. [APPSTORE-IOS-2026]
- **2.16.5:** switching between Polaris siege and normal siege must clear/update siege-fire presentation rather than leaving stale fire state. [APPSTORE-IOS-2026]
- **2.16.8:** friends handling was optimized and Mac App Store support improved; no gameplay semantic change is documented. [APPSTORE-IOS-2026]
- **2.17.0:** a technical UI-system overhaul was intended to produce little/no user-visible behavior change. Treat it as an implementation boundary, not a rules change. [APPSTORE-IOS-2026]
- **2.17.1:** very quick touches should not be skipped; popup icon height was constrained, and a local-game-data sync crash was fixed. These are input/UI/persistence contracts, not game-rule changes. [APPSTORE-IOS-2026]
- **2.17.2:** Unity was updated; keyboard map zoom with **+ / -** was improved and disabling tribes in multiplayer was fixed. [APPSTORE-IOS-2026]
- **2.17.3 (2026-09-07):** the current App Store “What’s New” text explicitly identifies World-Championship-oriented changes: **removed/limited score counting**, **+2 meeting stars for player 2 in 1v1**, and **faster Explorers**, plus UI fixes. [APPSTORE-IOS-2026]

The App Store wording does not state whether the three World Championship changes are global 2.17.3 rules, tournament-configuration overrides, or conditional behavior used only by championship games. Preserve them as versioned observable release contracts but do **not** apply them globally without current-build/tournament verification. “Removed/limited score counting” is especially underspecified: the affected score categories/modes are not named. [APPSTORE-IOS-2026]

Implementation note: use **2.17.3 (2026-09-07)** as the newest explicit numbered public baseline recovered in this pass, while preserving 2.16.3 as the richer official-site changelog baseline.

## 2022 Diplomacy balance: first contact, Ice Bank, and infiltration

The official **2.2.9.8251** release notes record these versioned balance changes: **Ice Bank maximum level increased to 30**; **tribe-meeting income reduced by one star per level** (the exact absolute formula and meaning of “level” are not stated); **Explosion damage reduced by 50%**; **Fungi no longer deals damage**. They also document all units detecting Cloaks, once-per-city-per-turn infiltration, defending-unit damage on infiltration, Daggers spawning inside an undefended city, and stolen city star production. [STEAM-DIP-RELEASE-2022]

Do not interpret “one less star per level” as a fully specified first-contact reward formula without a source defining level and rounding. Do not apply 2022 Ice Bank income-per-level or Fungi behavior to the 2025 Cymanti/Path-of-the-Ocean rules without later corroboration. Current Ice Bank level cap and its later **2 SPT per 20 frozen tiles** formula are separately documented in the Polaris spec. [WIKI-ICE-BANK, STEAM-DIP-RELEASE-2022]

Black-box targets: first-contact star payout by opponent city level/own city level/turn and game mode; whether current alliance healing and infiltration theft resolve before or after city income accrual.

## 2024-11-04: Aquarion post-launch Forgotten patch

The official Steam release notes give a critical post-rework delta: Bubbles activate for Amphibious units on Flooded terrain after Waterways (+1 movement, removed by attack/land); Atoll unlock moved to Aquaculture; starting capital gained two guaranteed fish; Lost Cities became smaller and gained nearby resources; Crab defence fell to 4, Shark attack rose to 3.5, Jelly attack rose to 2, and overlapping Tentacles select the strongest attacker. Earlier August 2024 official design notes make Lost City generation conditional on water-ruin city-placement validity, otherwise an ordinary ruin reward. [OFF-AQ-NOV24-PATCH, OFF-AQ-AUG24-DETAIL]

The patch does not specify the Lost City placement-distance formula, resource seeding, Tentacles tie-breaking, or whether these 2024 rules all remain unchanged in 2.17.3. Detailed test targets: [research/notes/aquarion-current.md](aquarion-current.md).

## 2021-09-08 — official 2.0.58 Balance Pass 2 (historical contracts)

The developer's first-party release notes establish the following *2021 versioned* mechanics, not guaranteed current 2.17.3 constants. [STEAM-BALANCE2-2058]

- **First contact:** tech theft was replaced by a star reward calculated from the **encountered tribe's score**: `stars = min(12, 3 * ceil(encountered_score / 1000))` for positive score. Examples: score 1–1000 → 3 stars, 1001–2000 → 6, 2001–3000 → 9, >3000 → 12. The release explicitly says this also applies to Domination. It does not specify zero-score handling, fractional/negative scores, or simultaneous first contact. [STEAM-BALANCE2-2058]
- **Ruin reward:** ordinary land-ruin Giant/super-unit rewards were replaced with a **Veteran Swordsman** (with Dash). Ruins could spawn beside villages and were more likely on mountains. This directly conflicts with the community map page's no-village-adjacency assertion; see map-generation notes. [STEAM-BALANCE2-2058, WIKI-MAP]
- **Other numeric balance:** Clear Forest income became 2 stars; Knight training price 10 stars; Burn Forest cost 2 stars; Elyrion lost Burn Forest. Mountain defence bonus moved to the Climbing tech. These are historical changes that later tech/balance passes may supersede. [STEAM-BALANCE2-2058]
- **Cymanti 2021:** Poison defence reduction changed 20%→30%; a single Recover or Mind Bender/Mycelium heal removed Poison; Fungus stopped slowing movement; Boost was removed after taking an attack or exploring a ruin; converting any Centipede Segment with a Mind Bender captured the entire Centipede; Phychi Surprise prevented retaliation; Raychi cost became 8 and Hexapod cost 3; Algae lost population yield and gained network connectivity. Later 2025 Cymanti rework substantially changed these systems, so preserve them only as dated history. [STEAM-BALANCE2-2058, OFF-CYM25]

**Chronology/conflict:** the 2022 Diplomacy patch subsequently says first-contact income was reduced by one star per level, without defining its replacement formula; 2.17.3 separately advertises +2 meeting stars for the second player in 1v1, with scope uncertain. Do **not** implement the 2021 contact formula as a universal current rule. Measure payouts across encountered-score buckets, player order, modes and city levels on the current build. [STEAM-BALANCE2-2058, STEAM-DIP-RELEASE-2022, APPSTORE-IOS-2026]
