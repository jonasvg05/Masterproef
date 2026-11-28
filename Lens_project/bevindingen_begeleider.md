# Lens Model bij scouts: eerste bevindingen

## Kernboodschap

- De data is technisch betrouwbaar en laat toe om de **kant van de scout** van het Lens Model te schatten. Er is geen prestatiecriterium, dus de accuraatheid van scouts kan niet onderzocht worden.
- Scouts wegen gemiddeld **Offensive het zwaarst (35%)** en **Set Pieces het minst (4%)**.
- De consistentie is onzeker. Volgens de methode uit de tutorial is de gemiddelde **Rs 0,79**, maar op rapporten buiten de modelschatting zakt die naar **0,30**.
- Oorzaak: per scout zijn er te weinig rapporten (14 tot 33) voor 7 cues. **De analyse per scout is daarom vooral beschrijvend.** 

## Onderzoeksdoel en aanpak

Het doel is onderzoeken **hoe scouts informatie wegen en hoe consistent ze dat doen**, volgens de tutorial van Peringa et al. (2025, *Psychology of Sport & Exercise*, 76, 102732).

| Lens Model | Operationalisatie |
|---|---|
| Rechter | scout |
| Oordeel (Ys) | algemene prestatie van de speler in de wedstrijd (`performance`, 1-4 sterren) |
| Cues (X) | gemiddelde score per categorie: 7 voor veldspelers, 4 voor keepers |
| Weging | OLS-regressie per scout en dominantieanalyse, herschaald naar 100% |
| Consistentie (Rs) | correlatie tussen het oordeel en de voorspelling van het eigen model |

Omdat er geen criterium (Ye) beschikbaar is, vallen ra, Re, rm, G en C buiten het onderzoek. De tutorial noemt deze beperking tot de kant van de beoordelaar als een mogelijke opzet.

**Afwijkingen van de tutorial:**

- De cues zijn categoriegemiddelden, omdat de 21 tot 25 vragen per positie te veel zijn voor een model per scout. De tutorial adviseert maximaal zeven cues.
- Naast Rs rapporteer ik een **leave-one-out-Rs**: elk rapport wordt voorspeld door een model dat op de andere rapporten van die scout geschat is.
- De gemiddelde Rs is een random-effects meta-analyse op Fisher-z (DerSimonian-Laird). De tutorial gebruikt het R-pakket psychmeta.

## Data

| Stap | Aantal |
|---|---|
| Ingediende individuele rapporten (na 6 drafts) | 284 rapporten, 14 scouts, 165 spelers |
| Sterrenscores | 5.403 (6,7% N/A, 3,5% niet ingevuld) |
| Bruikbaar na selectie* | 272 |
| Veldspelers: bruikbaar, volledig op alle cues, in de analyse | 204, 162, **154 (8 scouts)** |
| Keepers: bruikbaar, volledig op alle cues, in de analyse | 68, 36, **28 (1 scout)** |

\* Weggelaten: 2 herhaalde rapporten, 4 zonder oordeel en 7 met minder dan 50% beantwoorde vragen (1 rapport valt in twee groepen). Een scout komt in de analyse met minstens 2 volledige rapporten per cue.

De integriteitschecks (sleutels, koppelingen, tellingen, schaalbereik, datums) gaven geen fouten, en de aantallen komen overeen met de codebook.

**Opvallend in de data:**

- Het oordeel heeft weinig spreiding: 16% krijgt 1 ster, 47% 2 sterren, 35% 3 sterren en 2% 4 sterren.
- Ontbrekende cues zijn sterk geconcentreerd: bij 1v1 ontbreekt 46% van de scores en bij Set Pieces 27%, tegenover 2% tot 11% bij de andere categorieën.
- De gemiddelde `performance` per scout loopt van 1,5 tot 3,1 (scouts met minstens 10 rapporten). Dat kan op strengheid wijzen, maar ook op andere spelers of competities.
- Binnen scouts hangen de cues matig samen (r = 0,18 tot 0,58), wat de reden is om dominantieanalyse te gebruiken.

## Resultaten

### Weging (veldspelers, 8 scouts)

Aandeel van elke cue in de verklaarde variantie:

| Cue | Gemiddeld | Laagste scout | Hoogste scout |
|---|---|---|---|
| Offensive | 34,6% | 3,0% | 60,2% |
| Mental | 16,8% | 6,1% | 46,2% |
| Offensive Transition | 14,2% | 2,0% | 26,5% |
| Defensive | 12,9% | 3,3% | 25,3% |
| Physical | 10,7% | 2,6% | 19,1% |
| Defensive Transition | 6,7% | 1,1% | 11,6% |
| Set Pieces | 4,0% | 0,7% | 9,2% |

### Consistentie (veldspelers)

| Scout | Rapporten | Spelers | Posities | Verschillende oordelen | Rs | Rs leave-one-out |
|---|---|---|---|---|---|---|
| 19 | 17 | 16 | 7 | 3 | 0,96 | 0,80 |
| 20 | 16 | 13 | 8 | 3 | 0,86 | 0,46 |
| 15 | 21 | 17 | 8 | 3 | 0,83 | 0,39 |
| 16 | 18 | 13 | 9 | 2 | 0,78 | 0,24 |
| 13 | 16 | 16 | 8 | 3 | 0,77 | 0,32 |
| 30 | 33 | 24 | 9 | 2 | 0,72 | 0,46 |
| 14 | 14 | 13 | 4 | 3 | 0,67 | -0,31 |
| 23 | 19 | 19 | 6 | 4 | 0,43 | -0,36 |
| **Gemiddeld (95%-BI)** | | | | | **0,79 (0,66 tot 0,88)** | **0,30 (-0,01 tot 0,55)** |

Ter vergelijking: de tutorial vindt een gemiddelde Rs van 0,93, met 50 oordelen per scout op 4 cues en vooraf vastgelegde cues.

### Keepers

Alleen scout 22 heeft genoeg volledige rapporten (28 rapporten, 12 spelers, 4 cues). Rs is 0,86 en leave-one-out 0,79. Relatieve belangrijkheid: 2D 38,9%, 1v1 22,7%, 3D 21,6%, Distribution 16,7%. Een vergelijking tussen keeperscouts is niet mogelijk.

## Beperkingen

1. **Overfitting.** Met 14 tot 33 rapporten op 7 cues past het model zich sterk aan de steekproef aan, zodat Rs te hoog uitvalt. Bij twee scouts is de leave-one-out-waarde negatief: daar voorspelt het model nieuwe rapporten slecht.
2. **Bootstrap-intervallen per scout zijn hier niet bruikbaar.** Ze liggen soms bijna volledig boven de puntschatting (scout 23: Rs 0,43, interval 0,42 tot 0,98). Ook het interval rond de gemiddelde Rs is met voorzichtigheid te lezen.
3. **Gewichten per scout zijn onstabiel.** De verschillen tussen scouts in de tabel hierboven zijn daarom een eerste indicatie, geen bewezen verschillen in beoordelingsbeleid.
4. **Cues en oordeel komen uit hetzelfde formulier.** In de tutorial liggen de cues vooraf vast. Hier scoort de scout zowel de cues als het oordeel, dus een algemene indruk kan beide kleuren en Rs opdrijven.
5. **Geen gestandaardiseerde taak.** Scouts beoordelen verschillende spelers en meerdere posities door elkaar, en "Offensive" bevat per positie andere vragen. Verschillen tussen scouts kunnen dus ook van de spelers komen.
6. **Beperkte schaal.** Het oordeel heeft vier waarden, en twee scouts gebruikten er in deze rapporten slechts twee.
7. **Herhaalde metingen.** Sommige spelers komen meermaals voor per scout, wat de onafhankelijkheid van de rapporten beperkt.
8. **Selectie door ontbrekende cues.** Alleen volledige rapporten tellen mee. Scout 19 verliest zo 18 van de 35 rapporten, en de ontbrekende waarden zijn waarschijnlijk niet willekeurig.

Gevoeligheidsanalyses zijn nog niet uitgevoerd. Van de 272 bruikbare rapporten komen er 29 uit een bulkimport zonder gekende modus of timing, en hebben er 11 overal dezelfde score.
