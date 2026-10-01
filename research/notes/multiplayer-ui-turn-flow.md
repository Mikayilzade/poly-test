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
