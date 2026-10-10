# Polytopia reference project

Goal: build a source-backed, implementation-oriented reference for **The Battle of Polytopia** from publicly available information, sufficient to later reproduce observed game behavior locally from scratch.

## Working rules

1. Prefer first-party Midjiwan / Polytopia pages and storefront descriptions for current behavior and update history.
2. Use the community wiki and Steam discussions/guides to fill mechanical details that official pages do not document. Mark those facts as community-sourced until independently verified.
3. Do not commit leaked/decompiled proprietary source code, ripped game packages, credentials, DRM bypasses, or private material.
4. Screenshots and official graphics may be referenced and catalogued. Only store third-party/official assets in this repo when the source explicitly permits that use; otherwise keep a URL + description + provenance.
5. Every factual research note should point to one or more source IDs from `research/sources.json`.
6. Prefer exact numbers, formulas, state transitions, prerequisites, costs, ranges, map rules, AI rules, and edge cases over strategy prose.
7. Record version/date when behavior may have changed.
8. Conflicting sources are not silently reconciled. Record the conflict and investigate it.
9. The research branch is additive. Do not delete older observations merely because a patch changed them; move superseded facts into update/history notes.
10. Keep implementation inference separate from observed/documented behavior.

## Research loop

Each pass should:
- inspect current gaps in `research/index.json`;
- research one or more uncovered areas;
- add/update sources;
- add exact mechanics to the relevant note;
- record uncertainty/conflicts;
- update coverage status and the research log;
- run `python tools/validate_research.py`.

## Source confidence

- **A**: official Midjiwan/Polytopia documentation, official store page, official patch notes.
- **B**: Polytopia community wiki with concrete tables/mechanics.
- **C**: developer comments on Steam/official community channels, reputable guides, reproducible player testing.
- **D**: unverified discussion; useful only as a lead.

## Current target

Start from the newest publicly documented ruleset we can establish, then preserve historical deltas needed to understand older screenshots/guides. As of the 2026-10-05 release-history sweep, the newest explicit numbered first-party public baseline located is **2.17.3 (2026-09-07)** in Midjiwan's Apple App Store version history. The official site’s detailed **2.16.3 (2026-02-16)** changelog remains useful for richer mechanics/state notes; later 2026 news and event posts are tracked separately when they do not expose a numbered build.

> NOT AN OFFICIAL Polytopia PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MIDJIWAN.
