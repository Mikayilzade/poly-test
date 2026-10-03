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
- 2023 Balance Pass 3: cost increased by **5 stars for every existing Embassy built**. [DEV-BALANCE3-2023]
- 2025 official balance pass: new Embassies “begin cheaper” and increase based on number already owned. [OFF-2025BAL]

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
