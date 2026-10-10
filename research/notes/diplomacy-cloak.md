# Diplomacy, Embassy, Cloak and Dagger reference

This note separates the **2022 developer-defined baseline** from later balance changes and current community observations.

## Technology and peace state

Official material places Diplomacy after Strategy. Strategy enables Peace Treaties; Diplomacy adds Cloaks, Daggers, Embassies and Capital Vision. Peace lasts until one party cancels it. [OFF-DIP, DEV-DIP-FAQ-2022]

The 2022 developer FAQ documents treaty effects: partners cannot attack/capture/convert each other, may use each other's roads, do not impose normal ZOC on one another, and peace increases Embassy income. When peace is broken, the breaker cannot attack the former ally until the next turn; units belonging to the breaker inside the former ally's territory are destroyed. [DEV-DIP-FAQ-2022]

## Embassy

2022 developer baseline: [DEV-DIP-FAQ-2022]
- built remotely in another tribe's capital from Diplomacy UI;
- launch cost **5 stars**;
- reveals the capital plus its eight surrounding tiles;
- **+2 stars/turn to both parties**, rising to **+4 each** under peace;
- reciprocal Embassies are allowed, so reciprocal Embassies + peace could yield +8/turn each;
- war/attack destroys the relevant Embassy; capture of the host capital destroys the Embassy there.

### Price history

Do not hard-code 5 stars as current:
- 2022: fixed 5 stars. [DEV-DIP-FAQ-2022]
- **2023-04-01 purported Balance Pass 3 is an April Fools post, NOT a released balance change**. Its claimed +5 stars per existing Embassy must not be used as an historical rule. Retained solely as rejected source evidence. [DEV-BALANCE3-2023]
- **2025-09-01 official balance pass**: new Embassies “begin cheaper” and increase based on number already owned; no exact numerical formula is provided. [OFF-2025BAL]

Exact 2025+ numeric sequence was not found in reliable first-party public material. Keep pricing parameterized and black-box measure it.

## Cloak / infiltration

2022 developer baseline: Cloak is trained visible, becomes hidden after moving, has no ordinary attack, and uses Infiltrate on an adjacent enemy city. Infiltration consumes the Cloak and spawns Daggers equal to city level, capped at **5**. A developer follow-up independently confirms the count and says multiple Cloaks cannot infiltrate the same city on the same turn. [DEV-DIP-FAQ-2022, DEV-DAGGER-SPAWN-2022]

The launch FAQ says infiltrated cities do not make ordinary stars on their next turn and documents adjacent-Cloak warning UI. [DEV-DIP-FAQ-2022]

An official October 2022 balance note tightened two observable rules: **all unit types can detect Cloaks**, and **a city can be infiltrated at most once per turn**. This upgrades the latter from developer/community-only evidence to first-party release evidence. The official note does not state the detection radius or exact reveal timing, so those remain black-box targets. [OFF-DIP-BALANCE-2022]

Current community documentation adds later behavior: infiltration damages an occupying city unit, immediately awards stars equal to city income, prevents another infiltration before the owner's next turn / while under siege, and Cloak boarding a Port becomes Dinghy. [WIKI-CLOAK]

## Dagger / Pirate spawn

Developer launch material says spawn count equals city level (max 5) and prioritizes defensive tiles; water may be used when land space is exhausted. [DEV-DIP-FAQ-2022]

Current community documentation describes: city tile if available, then defense-bonus tiles; water can produce **Pirates**; inaccessible terrain is excluded; no valid tile means that Dagger does not materialize. [WIKI-DAGGER, WIKI-CLOAK]

Exact tie-break among equally eligible tiles remains unknown.

## Current black-box queue

1. Current Embassy price sequence for 0/1/2/3/... already-owned Embassies.
2. Embassy income timing versus turn-start income and peace accept/break.
3. Treaty-break action lock timing for both parties.
4. Exact Dagger/Pirate spawn tie-break.
5. Current hidden-Cloak detection indicator/radius.
6. Infiltration income interaction with Market/Ice Bank/Sanctuary and skins.


## 2.15.3–2.16.0 Pirate/Cloak compatibility boundaries

The official iOS release history records several post-Cymanti-rework fixes that constrain current infiltration behavior: [APPSTORE-IOS-2026]

- water spawns from ordinary Cloak infiltration can be **Pirates**;
- Mermaid/Aquarion Cloak infiltration damage was corrected to match ordinary Cloak damage;
- compatibility fallback was added for the Ciru Explorer when playing against an older game version that does not contain that unit;
- a later fix ensures Pirate boats actually contain the spawned Dagger unit;
- Daggers must **not** spawn on water when the player has not unlocked water movement.

Model the last point as an eligibility gate before water spawn selection, not merely as a visual conversion after a Dagger has already been placed. The public notes do not expose the exact shallow-water/ocean tech split, so keep that threshold unresolved.

## Peace-break cease-fire and allied naval upgrades — Path of the Ocean pre-release

Developer pre-release notes say ships can be upgraded in **ally territory**. The same changelog fixes Smash, Splash, Explode and similar effects harming former allies during the cease-fire immediately after breaking peace. [STEAM-BETA-CHANGELOG]

This is version-scoped pre-release evidence, but it establishes two important state boundaries to preserve when reconstructing behavior: friendly-upgrade territory can include treaty allies, and cease-fire protection must gate indirect/AoE damage as well as ordinary direct attacks. Exact cease-fire duration and the complete protected-effect list remain black-box targets.


## Cloak warning UI and historical Battle Preview information leak

Midjiwan's **2023-08-15** Cloak strategy tip identifies the **eye icon next to a unit** as the warning that a Cloak is nearby. This confirms the UI indicator, not an exact target-position reveal. [OFF-CLOAK-EYE-2023]

The community Cloak reference specifies that each unit detects an invisible enemy Cloak in any of its **eight adjacent tiles**, showing an eye on the unit icon without identifying which tile. It also says attempting to move onto the hidden Cloak's tile reveals it, cancels that movement and **does not consume the moving unit's action**. Peace-aligned Cloaks are described as visible instead of triggering the hostile warning. These details remain community-sourced until current-build verification. [WIKI-CLOAK]

A **2025-04-10** Steam bug report described a distinct information leak: hovering over a suspected hidden-Cloak tile with a unit selected could show a combat damage preview while the target remained invisible. Developer Zoythrus replied that this had been fixed for an **upcoming patch**. This does not establish the shipping version or prove every current preview pathway is leak-free. [STEAM-CLOAK-PREVIEW-2025]

Implementation / black-box boundary: keep adjacent detection and eye-icon state separate from target visibility and attack eligibility. Test eight-direction adjacency, multiple Cloaks, peace state, blocked-move reveal/action preservation, and preview hover over undiscovered tiles. Do not reproduce the historical preview leak as intended gameplay.
