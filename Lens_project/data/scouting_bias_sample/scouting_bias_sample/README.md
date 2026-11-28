# Scouting-bias sample: event data for 59 matches

The scouting-report matches from `matches_usable_reports.csv` that have event data in the RBFA
analysis-platform event format (CDF). Source: BigQuery `SCISPORTS_SILVER`, exported 2026-11-23.
The other matches in the report list have no event data in our pipeline.

## Files

| File | Grain | Rows |
|---|---|---|
| `matches.csv` | one row per match | 59 |
| `squads.csv` | one row per player per match (line-up, minutes, position) | 1,761 |
| `events.csv` | one row per event | 86,312 |

## Joining

- `scouting_match_id` = `match_id` in the scouting platform / `matches_usable_reports.csv`.
- `match_id` = SciSports match id; joins all three files.
- `events.player_id` / `receiver_id` / `team_id` join to `squads` on (`match_id`, `player_id`)
  and (`match_id`, `team_id`). These ids are only unique **within a match**, so always join
  on `match_id` as well.
- `squads.scouting_player_id` = player id in the scouting platform (joins to the scout
  evaluations). `rbfa_player_id` is the RBFA/Firestore id. 26 squad rows have no link.

## Conventions

- Coordinates in metres, origin (0, 0) at the centre spot, fixed 105 x 68 m pitch
  (x in [-52.5, 52.5], y in [-34, 34]). The **home team always attacks +x**.
- `event_type`: pass, carry, recovery, duel, clearance, referee, interception, dribble, shot,
  gk_action, block. Details in `event_sub_type`, `outcome_type`, `is_successful`.
- Order events within a match by `period`, then `event_order` (or `match_clock`); do not rely
  on `event_time`.
- `possession_*` columns group events into possession sequences.
- `vendor_*` columns (xG, xA, ...) are the provider's own model values.

Full definitions: `docs/rbfa_data_model/` in the analysis-platform repo (`EVENT_TYPES.md`,
`COORDINATE_SYSTEM.md`, `GLOSSARY.md`).
