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

Nintendo’s Special Tribe Skins page explicitly says skins change aesthetics (clothes/buildings/music and sometimes animals) but **do not add gameplay abilities or units**; skinned tribes play like their base tribe. [NIN-SKINS]

### Known visual substitutions to catalogue later

The community wiki describes skins changing unit equipment, terrain appearance, fruits/animals, city buildings, monuments, music and sometimes tribe color. Example: Sha-po uses assassin styling and different weapon visuals; To-Lï uses bamboo-themed terrain/buildings; special skins have much broader thematic substitutions. [WIKI-TRIBES]

For implementation later, keep gameplay identity and skin identity separate:
- `tribeRulesId`
- `skinId`
- cosmetic asset/theme mapping

This avoids accidentally encoding cosmetic differences as mechanics.
