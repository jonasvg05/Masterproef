# RBFA × Ghent University — Project 1: Physical Profiles

*Bron: "RBFA – Ghent University" presentatie, slides 33–34.*

---

## Slide 33 — Voorbeeld: player profile (screenshot RBFA-platform)

**Sami El Morabet** — Belgium U17
Badges: ⚡ 1× · 🛡 6× · ⌃ 2×

**Position breakdown**

| Positie | Matches | Aandeel |
|---|---|---|
| ★ LB | 6 | 60% |
| RB | 4 | 40% |

### Player Profile (BETA)

*vs 75 full backs in UEFA European Under-17 Championship · 2025/2026*

| Profiel | Sterren | Score | Fit | Opmerking |
|---|---|---|---|---|
| ★ Offensive full back / wing back (geselecteerd) | ★★☆☆☆ | 18.0/20 | 92% | low sample |
| Defensive full back | ★★★★☆ | 15.4/20 | 18% | low sample |

**Radar chart (metrics, schaal 1–20)**

| Metric | Score |
|---|---|
| Involvement | 13.6 |
| Active defence | 12.9 |
| Intelligent defence | 13.8 |
| Territorial dominance | 12.5 |
| Chance prevention | 9.9 |
| Progression | 15.9 |
| Passing quality | 14.9 |
| Run quality | 16.4 |
| Providing teammates | 15.0 |

**Strengths**

| Score | Submetric | Hoofdmetric |
|---|---|---|
| ↗ 20.0 | Defensive area | Territorial dominance |
| ↗ 19.5 | Pre-assists per 90 | Providing teammates |
| ↗ 19.2 | Box entries (carry) per 90 | Run quality |

**Weaknesses**

| Score | Submetric | Hoofdmetric |
|---|---|---|
| ↘ 4.0 | Aerial duels per 90 | Involvement |
| ↘ 4.1 | Opposition xG after defensive action | Chance prevention |
| ↘ 6.8 | xG blocked per 90 | Chance prevention |

> Metrics are rated 1–20 against the same position in the selected competition and season (10.5 is the average peer). Strengths and weaknesses are the submetrics furthest above or below that average (at most two per metric). Players need 180 minutes to be rated; small samples are regressed toward the average (the confidence dot shows how far). Possession-adjusted values are scaled to a 90-minute match at 50/50 possession; their samples show the equivalent adjusted minutes.

---

## Slide 34 — Opdracht

### Create a model to identify different physical profiles based on metrics from event & physical data

- Volume/Intensity
- High max speed
- Quick change of direction
- Quick accelerations
- Aerial dominant player
- Other

(Skillcorner good provider for physical metrics – can help for ideas)

### Create a model to flag potential dangerous match up's during games both positive & negative (1v1, unit, team)

- If we play France which of our wingers do we put against Digne to create chances?
- If we play Senegal can we cope with their physicality in midfield?
- If we play Spain which of our full backs is most suitable against Yamal?

> ➢ *We want to identify mismatches which can help us to win games!*
