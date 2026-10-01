# Multiplayer turn flow, Live timer and AI evidence

This note separates **documented mechanics** from AI behavior that is only historically confirmed. Source IDs live in `research/sources.json`.

## Sequential multiplayer turn order

Polytopia online multiplayer is sequential rather than simultaneous: players act one after another. The 2022 Tournament Update changed lobby behavior so that **turn order is randomized when the match starts**, rather than being determined by lobby join order. [STEAM-TOURNAMENT-BETA]

Moonrise's multiplayer server uploads moves to the server in real time, preventing the older practice of resetting a turn to undo already-taken actions. Opponents' moves can be shown in real time. [WIKI-MOONRISE]

### Lobby behavior documented in the Tournament Update

- Lobbies can be joined through a shareable invite link.
- A player counts as having accepted an invite after choosing a tribe.
- If the lobby owner leaves and another invited player has accepted, ownership can transfer.
- Turn order is randomized at match start. [STEAM-TOURNAMENT-BETA]

These are useful implementation-level state transitions for a later local multiplayer shell, but they should not be confused with the rules of an individual unit action.

## Live Games: chess-clock model

The Tournament Update introduced **Live Games** as the replacement for the old 5-minute timer. The official Steam announcement describes a time bank: unused time rolls into later turns and more time is added as play progresses. [STEAM-TOURNAMENT-BETA, STEAM-TOURNAMENT-RELEASE]

The beta announcement gives the timer constants:

| Parameter | 2022 documented value |
|---|---:|
| Initial bank | 60 seconds |
| Per-turn addition | 8 seconds |
| Per-city addition | 12 seconds |
| Per-unit addition | 1 second |
| timeout | turn skipped |
| repeated timeout | automatic kick after 3 skips |

[STEAM-TOURNAMENT-BETA]

This yields the **historical documented** replenishment model:

`new allowance contribution = 8s + 12s * cityCount + 1s * unitCount`

plus any banked unused time. The source does not precisely specify the internal moment at which city/unit counts are sampled, so that detail remains open.

### Important current-version caveat

The exact 2022 constants above are not yet proven unchanged in the 2026 build. Treat them as a versioned baseline, not an asserted current constant.

Developer responses in 2023–2024 still describe Live Games as deliberately timer-based/chess-clock-like and say the timer cannot be disabled; players wanting near-unlimited asynchronous play are directed to the 24-hour mode. [STEAM-LIVE-2023, STEAM-LIVE-2024]

A May 2024 developer response also says that time being consumed while preceding bot animations are shown in a Live Game was **designed that way**, not considered a bug at that time. [STEAM-LIVE-BOTS-2024]

## 24-hour / asynchronous mode

The 2022 Tournament beta announcement states that matchmaking timer choices were simplified to **Live Games and 24 Hours**, removing the other timer choices available at that time. [STEAM-TOURNAMENT-BETA]

The 2025 Balance Pass includes fixes so multiplayer would not unexpectedly fall back to a **60 days** turn limit or to **Perfection** mode. This proves those values could occur as erroneous fallback state, not that 60 days was an intended selectable contemporary timer. [OFF-2025BAL]

Current exact custom/private-game timer options should still be verified directly from a 2026 UI capture; public discussions conflict because old lobbies/games and older versions preserve historical timer values.

## Replays and defeated-player spectating

The Tournament Update made online multiplayer games cloud-saved and accessible through a **Replays** tab. Replay links can be shared and replays can be favorited even if the viewer did not play in the match. [STEAM-TOURNAMENT-BETA, STEAM-TOURNAMENT-RELEASE]

The same update explicitly allowed a defeated player to spectate the game, but **without gaining extra map vision**, to reduce ghosting/cheating. [STEAM-TOURNAMENT-BETA]

Later official championship material documents newer spectator/replay surfaces separately; those are tracked in `weekly-replays-special-tribes.md`.

## Crossplay

Update 2.4.3.9541 publicly released Live Games, Replays, Tournaments, Lobbies and **Steam/iOS/Android crossplay** in December 2022. The beta announcement notes that platform accounts remained separate rather than being merged. [STEAM-TOURNAMENT-RELEASE, STEAM-TOURNAMENT-BETA]

## AI difficulty — what is actually established

A developer answer from August 2020 explicitly documented two difficulty effects: [STEAM-AI-DEV]

| Difficulty | AI capital income |
|---|---:|
| Easy | 1 star/turn |
| Normal | 2 stars/turn |
| Hard | 3 stars/turn |
| Crazy | 5 stars/turn |

The developer additionally stated that harder difficulties have **higher aggression ratings**. [STEAM-AI-DEV]

This is stronger evidence than player inference, but it is historical. It should not be expanded into invented rules such as “Crazy evaluates combat N plies deeper” or “Hard has X% attack probability”: no public source located in this pass specifies such algorithms.

### Known AI development history

In January 2022 a developer stated that AI improvements were planned with the Diplomacy update. [STEAM-AI-DIP-2022]

Update 2.2.9.8251 later explicitly says **AI is now better at trying to reveal Cloaks**. [STEAM-229]

Therefore the AI is not safe to model as a frozen 2020 decision system even if the 1/2/3/5 income schedule survives in community documentation.

### 2026 behavior lead, not a rule

A June 2026 Steam bug report describes AI behavior becoming abnormal after external memory cheating created 1000 stars. A developer replied only with a warning not to use Cheat Engine; this does **not** establish a usable AI rule and should not be encoded into a clone. [STEAM-AI-CHEAT-2026]

## Implementation confidence / remaining unknowns

**High-confidence historical multiplayer behavior:** sequential turns; randomized start order from the 2022 lobby system; server-side move upload; Live time bank; replay/link/favorite surface; defeated-player spectating without extra vision; crossplay.

**Version-sensitive:** exact Live timer constants, current selectable timer menu, timeout/kick handling, current replay UI.

**AI unknowns:** target scoring, economic priorities, tech-selection weights, city-upgrade heuristics, unit production weights, path planning preferences, diplomacy thresholds, retreat behavior and difficulty-specific aggression values.

For a later faithful bot recreation, those unknowns should be derived from reproducible black-box scenarios or newer public developer material rather than guessed.

## AI behavior deltas recovered from developer-maintained changelogs

Public developer material exposes several narrow AI rules without exposing the proprietary decision algorithm:

- During the November 2023 Path of the Ocean beta, AI was changed so it would **no longer train Cloaks specifically to defend cities**; the same beta/pre-release sequence also records general AI improvements. [STEAM-BETA-CHANGELOG]
- Public update 2.8.5.11904 (February 2024) says AI became **better at choosing which unit to train** and **better at improving cities**. This establishes two decision domains that were explicitly retuned, but gives no weights or scoring formula. [STEAM-BETA-CHANGELOG]
- A February 2025 developer reply confirms AI **still trains Cloaks**, but deliberately much less frequently than when Cloaks were first introduced because players disliked the earlier frequency. This is useful negative evidence against modeling Cloaks as forbidden for AI. [STEAM-AI-CLOAK-2025]

### Reproduction implications

Treat AI unit production as weighted/contextual rather than a hard allow/deny list. In particular, a black-box harness should measure Cloak frequency separately for (a) empty/ordinary production, (b) threatened-city defence, and (c) late-game high-tech economies. For city development, record available improvements, stars, city level, nearby production resources and the chosen action over many fixed-map turns. These observations can constrain a clean-room policy without assuming undocumented internals.


## Difficulty / scoring boundary clarified by later official notes

The historical bot-difficulty evidence above should not be conflated with the **Perfection difficulty score bonus** shown by the UI. Official release 2.15.1 (November 2025) fixed display of the Perfection difficulty-bonus percentage in game setup. That proves the setup surface exposes a score modifier associated with difficulty, but the release note does **not** publish the percentages or establish that the modifier is identical to AI income/aggression settings. [STEAM-2151]

For reconstruction, keep these as separate parameters until measured:
1. AI economic bonus / capital income;
2. AI aggression/decision policy;
3. Perfection end-score difficulty multiplier.

The 2020 developer statement remains the best public numeric source found for (1), while no newer first-party source located in this sweep republishes the current 1/2/3/5 values. [STEAM-AI-DEV]

### Black-box matrix for current-build verification

A reproducible current-build test should run the same tribe/map seed at Easy, Normal, Hard and Crazy and record:
- bot capital SPT before any city upgrade, connection, embassy or other modifier;
- first hostile action / peace acceptance under otherwise matched diplomatic state;
- Perfection setup UI difficulty-bonus percentage and final score multiplier.

This separates three observables that older discussions often collapse into a single "difficulty" effect.


## Perfection difficulty bonus — documented community formula

Current community Game Modes/Score documentation publishes this Perfection end-score candidate: [WIKI-GAME-MODES-CURRENT]

`bonusPercent = 100 + 41 * ln(numberOfOpponents) + difficultyAdd`

with Easy +0, Normal +20, Hard +40, Crazy +80; its table reaches **291%** for 15 Crazy opponents. [WIKI-GAME-MODES-CURRENT]

Do **not** promote this to first-party current truth. Official 2.15.1 only confirms that setup displays a Perfection difficulty-bonus percentage; it does not publish the formula. Preserve this as a community-documented candidate and use current setup UI as the black-box authority. [STEAM-2151]

This multiplier is separate from AI capital income/aggression.
