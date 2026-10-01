# Multiplayer and Weekly scenario observations

## Live versus asynchronous timing

A developer response describes Live Game as a timed format inspired by chess clocks; removing the timer would contradict the format. The same response points players wanting effectively untimed play to the 24-hour option. [STEAM-LIVE-24H]

A separate developer response confirms an unintuitive observable behavior reported in 2024: in a Live game containing bots, time spent watching bot animations before the human can act can consume that human player's displayed timer. The developer said this was designed behavior at that time rather than a bug. Treat this as historical/current-unverified because later releases may have changed timer accounting. [STEAM-LIVE-BOTS]

Do not yet hard-code an exact Live clock formula. This pass did not find sufficiently strong current first-party evidence for the exact seconds added per turn, city, or unit.

## Current multiplayer UI evidence

Official 2026 material repeatedly directs players to Multiplayer > Tournaments to enter official competitions, confirming Tournaments as an in-game multiplayer surface in the current UI. [OFF-POLYNEWS26]

The 2025 balance pass fixed two multiplayer fallback bugs: games should not fall back to a 60-day turn limit and should not fall back to Perfection mode. [OFF-2025BAL]

## Weekly Challenges support custom initial scenarios

The original Weekly Challenge documentation guarantees the same seed, settings, tribe and opponents, one attempt per day, and 20 turns. [OFF-WEEKLY]

Official 2026 examples show additional non-standard initial state:
- Aquarion: player begins with a pack of Sharks while enemies are bunkered up. [OFF-AQ-WEEKLY26]
- Oumaji Raid of Dolnus: player begins with Riders and a Mind Bender against Imperius. [OFF-OUMAJI-WEEKLY26]
- Quetzali Chetiq: both sides start with Swordsmen and Defenders and access to all level-1 technologies. [OFF-POLYNEWS26]
- Earth Overshoot Day: no natural resources: no trees, crop, animals, fish, or gold. [OFF-POLYNEWS26]

Implementation inference: a Weekly Challenge representation should allow explicit scenario overrides such as starting units, unlocked technologies, and resource constraints rather than assuming seed plus ordinary settings fully defines initial state. This is an inference from observable examples, not a claim about the game's internal data format.

## Replay and spectator UI

Weekly Challenges expose winner replays from previous weeks and track the player's best score. [OFF-WEEKLY-HUB]

Version 2.16.3 explicitly mentions scrubbing in replays, proving a timeline/scrub interaction rather than replay being only a fixed-speed video. The same changelog includes controller-navigation and invisible-nearby-unit-hint fixes. [OFF-2163]

The 2025 World Championship report refers to enhanced spectator tools. Exact spectator controls, fog visibility policy, and delay behavior remain to inventory. [OFF-WC25]

## Remaining gaps

- exact current multiplayer setup matrix;
- exact current Live timer formula and timeout consequences;
- skip, kick, resign, and replacement behavior;
- reconnect and notification behavior;
- complete replay controls and spectator fog policy;
- ordinary turn start/end sequencing for income, status effects, growth timers, and capture.


## 2.16.3 UI / replay state contracts

Official 2.16.3 exposes several implementation-relevant UI/state rules: [OFF-2163]

- Weekly Challenge must allow **resign during an enemy turn**.
- Replay and Pass & Play income icons must respect skin resource theme (Stars versus Hearts for New Dawn).
- Embassy-income UI likewise uses the New Dawn heart icon where appropriate.
- Opening a game should **focus the camera on the player's capital even when auto-focus is disabled**.
- Replay scrubbing and controller navigation have explicit bug-fix coverage, confirming both as supported interaction surfaces.


## Replay model — historical developer baseline

The 2022 Tournament Update described multiplayer replays as server-saved records accessible from the Multiplayer **Replays** tab. Replay links could be shared, and replays could be favorited. The viewer exposed whose turn it was, that player's visible map state and research, with playback controls including **fast-forward, rewind and pause**. [DEV-REPLAYS-2022]

A February 2023 developer response says the system should keep a player's **most recent replays**, while acknowledging that some could fail to appear. No exact retention count was stated. Treat this as historical retention behavior, not a current quota. [STEAM-REPLAY-RETENTION-2023]

Current evidence remains compatible with this model: 2.16.3 explicitly supports replay scrubbing, and the current Weekly Challenge surface exposes previous winners' replays. Current ordinary-replay retention limits, favorite limits, share-link lifetime, fog/perspective switching and spectator-delay rules remain unverified. [OFF-2163, OFF-WEEKLY-HUB]


## Current replay/pass-and-play state contracts from 2.16.3

The February 2026 official changelog exposes several additional black-box contracts that matter for a faithful replay/state model. Replay and Pass & Play must render each player's own resource theme correctly (including New Dawn Hearts), and replay income must preserve that per-player presentation. The same release fixed Centipede segment connectors while **scrubbing**, which is further evidence that replay state can be traversed non-linearly rather than only played forward. [OFF-2163]

The changelog also mentions a crash caused by modifying a **share URL** so that it pointed to an ongoing game and then resigning. This is not enough evidence to claim ongoing-game links are a supported public feature, but it does establish that share-URL routing can resolve game state rather than only static finished-replay media. Keep supported URL lifetime/permissions unresolved. [OFF-2163]

For turn/setup behavior, 2.16.3 says games started with a friend use **random player turn order**. Weekly Challenges additionally permit resignation during an enemy turn. Both are observable state-machine rules and should not be inferred from UI order. [OFF-2163]

Finally, 2.16.3 changed ruin-reward calculation to improve Weekly Challenge consistency and prevents a water ruin from awarding a water unit when the exploring unit lacks water movement (the changelog gives Moth as the example). Treat pre-2.16.3 ruin tables as version-sensitive rather than assuming seed alone reproduces older reward selection. [OFF-2163]
