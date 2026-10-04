# Tribes and skins — catalogue seed

Sources: [WIKI-TRIBES, OFF-2025BAL, NIN-SKINS]

## Tribe set

Current public material describes **16 tribes**: 12 regular and 4 special.

### Regular tribes

| Tribe | Starting tech / state | 2025 starting stars |
|---|---|---:|
| Xin-xi | Climbing | 7 |
| Imperius | Organization | 5 |
| Bardur | Hunting | 5 |
| Oumaji | Riding | 6 |
| Kickoo | Fishing | 5 |
| Hoodrick | Archery | 7 |
| Luxidoor | upgraded Capital, no ordinary starting tech | 2 extra stars |
| Vengir | Smithery | 5 |
| Zebasi | Farming | 5 |
| Ai-Mo | Philosophy + Mind Bender (changed from Meditation in 2025) | 5 |
| Quetzali | Strategy | 7 |
| Yădakk | Roads | 7 |

The “all other tribes begin with 5 stars” rule and listed exceptions above come from the official 2025 balance pass. [OFF-2025BAL]

### Special tribes

- Aquarion
- ∑∫ỹriȱŋ (Elyrion)
- Polaris
- Cymanti

Each special tribe modifies the ordinary technology/unit/building system rather than being a simple cosmetic reskin. Dedicated atomized specs are still required. [WIKI-TRIBES]

## Cosmetic skins

Community and official store material identify the following tribe skins:

| Base tribe | Skin |
|---|---|
| Xin-xi | Sha-po |
| Imperius | Lirepacci |
| Bardur | Baergøff |
| Oumaji | Khondor |
| Kickoo | Ragoo |
| Hoodrick | Yorthwober |
| Luxidoor | Aumux |
| Vengir | Cultist |
| Zebasi | Anzala |
| Ai-Mo | To-Lï |
| Quetzali | Iqaruz |
| Yădakk | Ürkaz |
| Elyrion | Midnight / ₼idŋighţ |
| Aquarion | Forgotten |
| Polaris | Solaris |
| Cymanti | New Dawn |

Nintendo’s Special Tribe Skins page describes ordinary tribe skins as aesthetic-only (clothes/buildings/music and sometimes animals), with no added gameplay abilities or units. [NIN-SKINS]

Official pages for special-tribe skins use broader replacement language: Midnight Elyrion mentions graves, crypts and demons; Forgotten Aquarion mentions bubbles, giant squids, crocodiles and toads; Solaris Polaris mentions water becoming lava and enemies becoming ashes. [OFF-MIDNIGHT, OFF-FORGOTTEN, OFF-SOLARIS] Treat these as presentation contracts, not proof of extra mechanics: normalize skin-specific identities to the base special-tribe rules until a mechanical delta is independently evidenced.

### Known visual substitutions to catalogue later

The community wiki describes skins changing unit equipment, terrain appearance, fruits/animals, city buildings, monuments, music and sometimes tribe color. Example: Sha-po uses assassin styling and different weapon visuals; To-Lï uses bamboo-themed terrain/buildings; special skins have much broader thematic substitutions. [WIKI-TRIBES]

For implementation later, keep gameplay identity and skin identity separate:
- `tribeRulesId`
- `skinId`
- cosmetic asset/theme mapping

This avoids accidentally encoding cosmetic differences as mechanics.


## New Dawn visual-recognition mapping

The official New Dawn feature article gives an unusually detailed first-party mapping from the Cymanti ruleset to its skin presentation. These are **cosmetic identities, not new gameplay units**; use them when interpreting screenshots/replays while resolving mechanics through the base Cymanti counterpart. [OFF-NEW-DAWN]

| New Dawn presentation | Cymanti counterpart / role |
|---|---|
| Guru | Shaman |
| Hooman | Warrior |
| Top Hat | Hexapod |
| Cacti | Kiton |
| Ruby | Mantis |
| Shoo | Doomux |
| Claude | Phychi |
| Lily | Exida |
| Squishy | Boomchi |
| Axolotl | Raychi |
| Super-Sponge | Living Island |
| Fairy | Moth |
| Kodama / Eggy | Moth growth-cycle forms |
| Foam | Algae |
| Snulles | animal resource |
| Pupli Nectar | fruit resource |

The article explicitly describes the replacements as retaining the corresponding gameplay jobs (for example Top Hats retain Hexapod mobility, Claudes retain the flying/poisonous double-strike role, and Axolotls retain the Raychi naval/city-capture role). This is valuable for visual parsers: recognizing a skin-specific model/name must normalize to the base gameplay entity before tactical reasoning. [OFF-NEW-DAWN]

Open visual-reference work: catalogue exact New Dawn building/technology/terrain substitutions and iconography from first-party screenshots without copying the underlying assets.
