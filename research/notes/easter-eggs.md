# Easter eggs and hidden observable behavior

Scope: publicly documented hidden interactions that can affect a faithful local behavioral reference. These are community-documented unless independently confirmed; treat current-build availability as provisional.

Sources: `WIKI-EASTER`, `WIKI-LUXIDOOR`.

## Nature Bunny / Bunta

- Community documentation says a Nature Bunny can be spawned in **single-player only** by tapping an unoccupied tile in the player's territory **10 times**. [WIKI-EASTER]
- The Bunny destroys a building when it moves onto that building's tile. [WIKI-EASTER]
- During the December holiday season the Bunny is visually replaced by the **Bunta**; the wiki describes its behavior as otherwise identical. [WIKI-EASTER]
- Implementation status: **current-unverified**. Black-box test mobile/Steam separately because hidden interactions can be platform-specific.

## Sunrise background

- Holding the night-sky background and releasing after about **20 seconds** switches to a yellow/pink sunrise gradient; repeating the hold or relaunching reverts it. [WIKI-EASTER]
- The wiki dates introduction to update 1.5. [WIKI-EASTER]
- This is cosmetic/UI state, not simulation state.

## Mixed tribes

Community documentation describes a hidden tribe-selection interaction available only for tribes with three stars. [WIKI-EASTER]

- Mobile: hold two tribe icons simultaneously.
- Steam: hold Alt, click the first tribe, then hold the second without releasing Alt until the merge completes.
- The **first tribe** supplies the first four name characters, city style, color and unit style.
- The **second tribe** supplies the final three name characters, terrain style, music, skin and gameplay technology (including starting/special technology).
- Therefore this is not merely a palette swap: appearance can be decoupled from the second tribe's actual gameplay rules.
- Mixed-tribe highscores are documented as being saved in the Throne Room.
- Wiki dates introduction to 1.14.2.

This behavior needs current-build/platform verification before implementation because unlock and input details may have changed.

## Elyrion language

Owners of Elyrion are documented as receiving an Elyrion-language option in Settings. The wiki dates it to 1.15.1. [WIKI-EASTER]

## Unowned Luxidoor opponent

The wiki documents a small chance for mobile single-player to select Luxidoor as an AI opponent even when the player does not own Luxidoor. On Steam, where Luxidoor is part of the base game, the wiki says the analogous behavior extends to unowned tribes. [WIKI-EASTER, WIKI-LUXIDOOR]

Treat exact probability and current platform behavior as **unknown**.

## Removed / broken historical interaction

A former cosmetic interaction alternated taps on the bottom-left/bottom-right city tiles to make a city visually rise or sink. The wiki says it stopped working in 2021 and cites a community-manager statement that it was apparently not intentionally removed. Preserve this only as historical behavior, not as a current requirement. [WIKI-EASTER]

## Black-box verification queue

1. Verify Bunny 10-tap trigger, valid target constraints, unit stats/skills and building-destruction semantics on current mobile/Steam.
2. Verify seasonal Bunta date window and whether it is client-date/server-event driven.
3. Verify sunrise hold duration/touch-vs-mouse behavior and persistence.
4. Verify current mixed-tribe eligibility, exact input sequence, special-tribe combinations and high-score handling.
5. Verify Elyrion language ownership gating.
6. Measure unowned-opponent probability and platform differences.

## Confidence

All mechanics in this note are grade **B** community-wiki evidence. They are useful reproduction targets but should not override contradictory current first-party evidence or direct current-build testing.
