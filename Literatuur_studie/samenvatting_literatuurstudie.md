# Samenvatting literatuurstudie

> Werkdocument om de scriptie uit te schrijven. Bevat de belangrijkste begrippen, resultaten (met cijfers), argumenten en methodologische lessen uit de verwerkte bronnen, geordend per topic en per hoofdstuk van de scriptie. Elke bewering heeft een BibTeX-key, zodat je ze rechtstreeks kunt citeren met `\citet{key}` of `\citep{key}`.
>
> **Conventies**
> - `[key]` = de bron zelf beweert of meet dit.
> - `[via key: Auteur (jaar)]` = **secundaire vermelding**: de bron citeert een ander werk. Niet zo citeren in de scriptie zonder het originele werk zelf te lezen (dan is het een snowballing-kandidaat).
> - Engelse vakterm cursief, met de Nederlandse vertaling die in de scriptie gebruikt wordt.
>
> Laatst bijgewerkt: 27 november 2026. Verwerkte bronnen: 14 (`peringa2025uniform`, `houtmeyers2021managing`, `oonk2026databallpy`, `bergkamp2019methodological`, `bareli2024feudal`, `barraclough2022methodological`, `bennett2026talent`, `billen2022careers`, `denhartigh2016dynamic`, `johnston2025take`, `kite2025player`, `lundberg2026evidence`, `pintelon2026aigestuurde`, `davis2024methodology`).

---

## 1. Begrippenlijst

| Begrip (NL / *EN*) | Definitie | Bron | Topic |
|---|---|---|---|
| Beschrijvende analyse / *descriptive analytics* | Stap 1 van het data-analyseframework: *wat is er gebeurd?* Data centraliseren en samenvatten, bv. in dashboards; werkelijk vs. gepland proces vergelijken. | `houtmeyers2021managing` | X |
| Diagnostische analyse / *diagnostic analytics* | Stap 2: *waarom is het gebeurd?* Relaties tussen variabelen onderzoeken (bv. correlaties, hiërarchische en mixture-modellen, ML). | `houtmeyers2021managing` | X |
| Voorspellende analyse / *predictive analytics* | Stap 3: *wat zal er gebeuren?* Alle methoden die nieuwe of toekomstige data accuraat voorspellen (bv. regressie, beslissingsbomen). | `houtmeyers2021managing` | X |
| Voorschrijvende analyse / *prescriptive analytics* | Stap 4: *hoe laten we het gebeuren?* Stelt acties voor en toont de gevolgen van elke beslissingsoptie; verwant met *decision support systems*. Kan steunen op probabilistische voorspellingen of op expertsystemen (optimalisatie, constraint programming). | `houtmeyers2021managing` | X |
| *Data-informed* vs. *data-driven* | Stappen 1-3 *informeren* beslissingen, stap 4 *stuurt* ze. Topsport zit vandaag in data-informed besluitvorming. | `houtmeyers2021managing` | X |
| Eventdata | Data over specifieke gebeurtenissen (passes, schoten) met locatie, uitkomst en betrokken speler. Goedkoop en wijd beschikbaar, veel gebruikt in scouting. | `oonk2026databallpy` | B |
| Trackingdata | Spatiotemporele posities van alle spelers en de bal aan 10-25 Hz, meestal via computer vision op videobeelden; bevat ruis afhankelijk van aantal en kwaliteit van de camera's. | `oonk2026databallpy` | B |
| Synchronisatie event ↔ tracking | Events uit de eventdata koppelen aan het juiste frame van de trackingdata. De tijdstempels van beide bronnen komen slecht overeen, dus een algoritme is nodig. | `oonk2026databallpy` | B |
| Contextuele analyse | Analyse van specifieke momenten of fasen in een wedstrijd door eventdata te verrijken met de spatiotemporele context uit trackingdata, i.p.v. enkel geaggregeerde metrieken. | `oonk2026databallpy` | B / E |
| Pitch control | Model dat per locatie op het veld de kans schat dat een team de bal daar controleert. DataBallPy implementeert de versie van Fernandez & Bornn (2018, Gaussische invloedszones). `pintelon2026aigestuurde` gebruikt de versie van Spearman: een gewogen kansfunctie over de geschatte tijd die elke speler nodig heeft om de locatie te bereiken (zie *time-to-intercept*). | `oonk2026databallpy`, `pintelon2026aigestuurde` | D |
| *Time-to-intercept* (TTI) | Geschatte tijd die een speler nodig heeft om een locatie te bereiken: reactietijd plus de afstand (vanaf de positie na de reactietijd, rekening houdend met de huidige snelheid) gedeeld door een maximumsnelheid. In de gebruikte implementatie is die voor alle spelers gelijk: reactietijd 0,7 s, vmax = 5,0 m/s. | `pintelon2026aigestuurde` | D |
| Gepersonaliseerde pitch control | Voorstel om in de TTI de maximumsnelheid, maximale versnelling en de daling van de topsnelheid door vermoeidheid **per speler** uit trackingdata te gebruiken, zodat een snelle aanvaller tegen een trage verdediger correct gemodelleerd wordt. Enkel voorgesteld, niet uitgevoerd. | `pintelon2026aigestuurde` | D |
| Bezitsdetectie uit tracking | Bepalen welke speler de bal heeft uit ruwe trackingdata: dichtste speler binnen 1,5 m van de bal, aaneengesloten frames groeperen, en enkel als balbezit tellen als de bal binnen die periode > 10° van richting of > 5 m/s van snelheid verandert (methode van Vidal-Codina et al.). Nodig wanneer enkel tracking beschikbaar is (bv. tijdens de rust). | `pintelon2026aigestuurde` | B |
| Externe vs. interne belasting / *external vs. internal load* | Extern: hoeveelheid en soort activiteit (afstand, sprints, acceleraties; gemeten met GNSS, accelerometers, LPS). Intern: de fysiologische reactie van het lichaam daarop. | `davis2024methodology` | A |
| Afgeleide vs. modelgebaseerde indicator | Afgeleid: rechtstreeks uit de data geteld of gemiddeld (bv. aantal progressieve passes), zonder context. Modelgebaseerd: geschat met een getraind model dat context meeneemt (bv. xG, VAEP). | `davis2024methodology` | C / E |
| Temporele afhankelijkheid en *subject consistency* | Opeenvolgende metingen (frames, acties, wedstrijden) zijn sterk gecorreleerd, en dezelfde speler gedraagt zich gelijkaardig over metingen heen. Willekeurig splitsen in train/test meet dan een proxy (vorige waarde, zelfde speler) i.p.v. het doel. | `davis2024methodology` | B |
| Walk-forward / subject-level / leave-one-competition-out cross-validatie | Groepsgewijze splits: steeds een tijdsplit die opschuift (walk-forward); alle data van één speler in dezelfde fold (subject-level); één competitie als testset (leave-one-competition-out), afhankelijk van waarnaar je wilt veralgemenen. | `davis2024methodology` | B |
| Normalisatie van een indicator | Per actie (gemiddelde per actie; steekproefgrootte vermelden), per 90 min (maar wedstrijdduur varieert), per balspeeltijd (*ball-in-play time*; SkillCorner normaliseert sommige fysieke metrieken per 60 min balspeeltijd) of per balbezit (bezit moet vaak heuristisch afgeleid worden). | `davis2024methodology` | B |
| Betrouwbaarheid van een indicator / *reliability* | Een indicator die een vaardigheid meet, moet binnen een seizoen en tussen twee opeenvolgende seizoenen gelijkaardige waarden geven. Gemeten door de data in twee te splitsen (of opeenvolgende seizoenen te nemen) en de indicatorwaarden te correleren. | `davis2024methodology` | B / C |
| *Face validity* | Een indicator die flagrant ingaat tegen wat algemeen aanvaard is (bv. de beste aanvallers scoren slecht), heeft waarschijnlijk een probleem. Werkt beter voor offensieve dan voor defensieve prestaties. | `davis2024methodology` | E |
| *Credit assignment* | Het is vaak onduidelijk waarom een actie slaagt of faalt of waarom ze voorkomt (bv. veel tackles omdat een ploegmaat slecht staat, of omdat de tegenstander een zwakke verdediger viseert). | `davis2024methodology` | D / E |
| Verificatie van een model | Een getraind model bevragen over situaties die niet in de data zitten (robuustheid, counterfactual explanations, gedrag in situaties met sterke domeinintuïtie), eventueel met formele garanties; vindt labelfouten en onrealistisch modelgedrag die testmetrieken missen. | `davis2024methodology` | E |
| Pressure / druk | Maat voor de defensieve druk op een speler (implementatie volgens Andrienko et al., 2017 en Herold et al., 2022). | `oonk2026databallpy` | D |
| Expected Goals (xG) / Expected Threat (xT) | xG: kans dat een schot een doelpunt wordt; xT: waarde van balposities op basis van de kans op een doelpunt. Beide beschikbaar in DataBallPy. | `oonk2026databallpy` | E |
| Brier loss | Gemiddelde kwadratische fout van voorspelde kansen (lager = beter); gebruikt om xG-modellen te evalueren. Te verkiezen boven log loss als kansen later opgeteld of afgetrokken worden; combineren met een reliability diagram of ECE om kalibratie te controleren. | `oonk2026databallpy`, `pintelon2026aigestuurde`, `davis2024methodology` | E |
| Expected Passes (xPass) | Kans dat een pass aankomt, gegeven passer-, ontvanger- en passlijncontext en fysische features (*speed window* en *angle window*: de marge in balsnelheid en -hoek waarbinnen de ontvanger de bal als eerste bereikt). | `pintelon2026aigestuurde` | E |
| Isotone kalibratie | Nabewerking die de voorspelde kansen van een classifier (hier XGBoost) laat overeenkomen met de werkelijke frequenties. Nodig wanneer de kans zelf gebruikt wordt (in een formule) en niet enkel om te rangschikken. | `pintelon2026aigestuurde` | E |
| Expected Value (EV) van een passoptie | Verwachte offensieve waarde van een pass naar een ploegmaat: xPass × xG op de verwachte positie van de ontvanger, plus een term voor terreinwinst, vrijheid van de ontvanger en pitch control op die plek. Rangschikt alle passopties in één frame. | `pintelon2026aigestuurde` | E |
| Delta-evaluatie (ΔEV) | Verschil tussen de EV van de beste (aanbevolen) optie en de EV van de werkelijk gespeelde pass, berekend met dezelfde pijplijn. Positief = gemiste kans. Verschilt van passnauwkeurigheid: een geslaagde pass kan suboptimaal zijn. | `pintelon2026aigestuurde` | E |
| Decision Quality Score (DQS) | EV van de gespeelde pass gedeeld door de EV van de aanbeveling (in %), geaggregeerd over een campagne; bedoeld om spelers positie-onafhankelijk te vergelijken, maar instabiel in zones met lage EV. | `pintelon2026aigestuurde` | E |
| *Wordalisation* | Modeloutput omzetten naar tekst voor coaches in vier stappen (Caut et al.): modeloutput → populatierelatieve labels (bv. klein/matig/groot via p25/p75) → gestructureerde prompt → tekst door een LLM. | `pintelon2026aigestuurde` | X |

---

## 2. Resultaten met cijfers

### Topic A: Fysieke prestatie-indicatoren
*Nog geen inhoudelijke bronnen.* Indirect: fysieke predictoren uit geïsoleerde testen (sprint, sprong, uithouding) hebben in talentstudies kleine tot matige effecten en hun onderscheidend vermogen hangt af van leeftijd en voorselectie `bergkamp2019methodological`.

### Topic B: Meten, betrouwbaarheid en normalisatie
- Gewoon de tijdstempels van event- en trackingdata naast elkaar leggen geeft een fout van **1.82 (±4.06) s** [via oonk2026databallpy: Anzer & Bauer (2021)]. De willekeurige component is het probleem: in 4 s kan de spelsituatie volledig veranderd zijn. `oonk2026databallpy`
- Met correcte synchronisatie daalt de **Brier loss van een xG-model van 0.096 naar 0.082**; features die event- en trackinginformatie combineren hebben enkel bij correcte synchronisatie een niet-nul belang [via oonk2026databallpy: Oonk, Grob & Kempe (2025)].
- DataBallPy synchroniseert een wedstrijd in **enkele seconden** i.p.v. ~10 min voor de oorspronkelijke Needleman-Wunsch-aanpak; alternatieven zoals ETSY duren tot 3 min per match en kunnen events niet toewijzen. `oonk2026databallpy`
- Ruwe trackingbestanden van **tot 400 MB per wedstrijd** worden 20-100 MB als opgeslagen Game-object (Parquet/JSON). `oonk2026databallpy`
- **RBFA-dataplatform** (beschreven in een eerdere masterproef): event- en trackingdata van 369 interlands (UEFA Nations League 2024, WK-kwalificatie 2026); tracking van Second Spectrum aan 25 Hz, veldcoördinaten met de oorsprong in het midden (x ∈ [−52,5; 52,5] m, y ∈ [−34; 34] m). Twee formaten: JSONL (coördinaten wisselen van teken na de rust) en genormaliseerde PKL-bestanden (thuisploeg valt altijd naar +x aan). Events zijn door de RBFA al aan een trackingframe gekoppeld (`tracking_frame`), maar bij 2 wedstrijden ontbrak die kolom. Batchresultaten in BigQuery. `pintelon2026aigestuurde`
- De aanvalsrichting kan automatisch gedetecteerd worden uit de gemiddelde x-positie van de doelman in beide helften. `pintelon2026aigestuurde`

**Methodologie en evaluatie van indicatoren** `davis2024methodology` (positionpaper, KU Leuven + Arne Jaspers; volledig gelezen):
- Zeven uitdagingen bij sportdata: geen ground truth, credit assignment, ruis in features en labels (annotatiefouten, occlusies in tracking die doorwerken in snelheid en versnelling), kleine steekproeven (34-38 competitiewedstrijden per seizoen, 1500-3000 balacties per wedstrijd), niet-stationaire data (data ouder dan één of twee seizoenen is mogelijk niet meer relevant), counterfactuals en interventies (de staf beïnvloedt wat geobserveerd wordt).
- Data zijn niet i.i.d.: splits groepsgewijs op tijd (single split midden of tussen seizoenen, walk-forward), op speler of op competitie. Er is weinig onderzoek naar wanneer data verouderd raakt.
- Contextfactoren die **fysieke** indicatoren beïnvloeden: tactisch systeem (back three vs. back four), thuis/uit, veldconditie, omgevingsvariabelen (temperatuur, hoogte). Veldafmetingen beïnvloeden ruimtelijke metrieken zoals pitch control en zonedefinities. Op indicatorniveau: speeltijd, tempo, stand, tegenstander, moment in het seizoen; invallers genereren meer waarde dan basisspelers.
- Biases: goede spelers en ploegen voeren meer acties uit, wat herhaalde metingen per speler geeft; hiërarchische/multilevelmodellen of multicalibratie kunnen groepsstructuur (posities, ploegen) opvangen.
- Betrouwbaarheid (Fig. 5): Pearson-correlatie van indicatoren over 10 paren opeenvolgende seizoenen in de Premier League (2009/10-2019/20, ≥ 900 min per seizoen). *Minutes played* is de minst betrouwbare indicator; Atomic-VAEP is betrouwbaarder dan VAEP en xT; schoten weglaten verhoogt de betrouwbaarheid. Een chronologische split binnen een seizoen is hier minder geschikt (blessures clusteren, moeilijkheid van de kalender is niet gelijk verdeeld, veroudering).
- Andere stabiliteitsmaten: bootstrap binnen een seizoen om te meten hoeveel een indicator van context en vaardigheidsverandering afhangt [via davis2024methodology: Franks et al. (2016)]; nearest-neighbour over opeenvolgende seizoenen: op welke plaats staat de speler zelf in de lijst van meest gelijkaardige spelers [via davis2024methodology: Decroos & Davis (2019)].
- Data uit topsport (GNSS-variabelen, vragenlijsten) zijn vaak slecht gevalideerd en meten vaak indirect het mechanisme van interesse (bv. afstand aan hoge snelheid als proxy voor spierbelasting). `houtmeyers2021managing`

### Topic C: Fysieke profilering en rolclustering
*Nog geen bronnen over fysieke clustering.* Methoden om de stabiliteit van profielen te testen (split-half, opeenvolgende seizoenen, nearest-neighbour) staan onder topic B `davis2024methodology`. Indirect: bij veel gecorreleerde variabelen zijn regressiegewichten geen goede maat voor belang; gebruik relatief belang (dominance analysis) `peringa2025uniform` of datareductie zoals PCA `houtmeyers2021managing`.

### Topic D: Matchups en mismatches
*Nog geen bronnen die mismatches zelf definiëren.* Beschikbare tooling: pitch control, pressure, Voronoi-ruimte en *Dangerous Accessible Space* zijn geïmplementeerd in DataBallPy. `oonk2026databallpy`
- In een prescriptief systeem op RBFA-data gebruikt `pintelon2026aigestuurde` Spearman-pitch control met **voor elke speler dezelfde** vmax = 5,0 m/s en reactietijd 0,7 s. De auteur noemt dat een gekende beperking: een snelle aanvaller en een trage verdediger worden identiek gemodelleerd, wat tot foute TTI-schattingen leidt in duels waar het snelheidsverschil beslist. Voorstel: topsnelheid, maximale versnelling en vermoeidheidsverloop per speler uit tracking afleiden en in de TTI invullen [via pintelon2026aigestuurde: Vermeulen (2025)].
- Looplijnadvies (*AI-Advised Movement*): per aanvaller 32 kandidaatposities in een polaire grid, bereikbaar met v = max(huidige snelheid, 2,0 m/s) in de tijd dat de bal onderweg is; gefilterd op veldgrenzen, fysieke haalbaarheid (≤ 1,05 × v × T), 2 m afstand tot ploegmaats, buitenspel en ≥ 0,5 m progressie. Looptempo vertaald naar labels: ≥ 5,5 m/s *full sprint*, ≥ 3,5 m/s *sharp run*. `pintelon2026aigestuurde`

### Topic E: Link met wedstrijduitkomst
Zie het xG-resultaat onder topic B: de kwaliteit van de koppeling tussen event en tracking beïnvloedt rechtstreeks de kwaliteit van uitkomstmodellen. `oonk2026databallpy`

**Evaluatie van indicatoren en modellen** `davis2024methodology`:
- Een indicator moet (1) nieuwe inzichten geven, (2) gebaseerd zijn op domeinkennis zodat niet-ML-experts ze begrijpen, en (3) vertrouwd worden door experts (o.a. robuust, niet wild fluctuerend).
- Vijf manieren om een indicator te evalueren: correlatie met bestaande succesindicatoren (afgeraden als doel: marktwaarde en transferprijs bevatten ook commerciële waarde en contractduur, speeltijd is niet altijd op verdienste), face validity, een voorspelling vooraf publiceren, expertvalidatie (ook bruikbaarheid: tijdwinst, correcte interpretatie) en betrouwbaarheid.
- Verificatie met Veritas: van 200 gegenereerde schoten buiten de zestien met de hoogste xG lag een cluster bij de cornervlag; in die 5 m-zone 11 schoten en 8 goals (72%), een labelfout (zo'n actie wordt enkel als schot gelabeld als ze een goal of redding oplevert). Bij VAEP sprong de scoringskans plots rond minuut 27 bij verder identieke features: tijd moet anders voorgesteld worden.

**Prescriptieve passanalyse op RBFA-data** `pintelon2026aigestuurde` (masterproef UGent, niet peer-reviewed, vertrouwelijk; skim). 215.859 open-spelpasses uit 367 interlands (93,8% geslaagd; 21,3% < 10 m, 68,1% 10-30 m, 10,6% > 30 m; gemiddelde pashoek 81,6°, dus vooral zijwaarts/achterwaarts; 72,9% zonder directe druk).

| Model / analyse | Resultaat |
|---|---|
| xG (XGBoost, 11 features; 58.573 StatsBomb-schoten, 11,1% doelpunten) | AUC = 0,817; isotone kalibratie: Brier 0,161 → 0,081 |
| xPass (XGBoost, 23 features, RBFA-passes) | AUC = 0,930 (Anzer & Bauer: 0,955 op ~5× meer Bundesligadata); BSS = 0,370 vs. 0,241 voor hun event-only baseline; kalibratie: Brier 0,090 → 0,035; werkpunt τ = 0,85: TPR 93,0%, TNR 72,9% |
| Feature importance xPass (mean gain) | pasafstand 9,7%, tegenstanders dichter bij doel dan de ontvanger 8,9%, x-positie ontvanger 7,7%; speed window 3,6%, angle window 3,3% |
| DQS, alle open-spelpasses (8 WK-kwalificatiewedstrijden, 3.484 passes, 18 spelers met ≥ 30 passes over ≥ 3 wedstrijden) | van 16,1% (doelman) tot 53,1% (De Ketelaere) |
| DQS, enkel progressieve passes | Saelemaekers 67,0%, Doku 64,0%, Meunier 60,1%, De Cuyper 56,3%, Castagne 50,8%, De Bruyne 50,4% |

- Een ranking op enkel xPass bevoordeelt veilige terugspeelpasses (93% slaagt); daarom combineert de EV slaagkans met dreiging. Filters in de campagneanalyse: onderschepte passes uit, enkel open spel, ΔEV ≥ 0,005. `pintelon2026aigestuurde`
- Beperkingen volgens de auteur: doelmannen en diepe verdedigers scoren structureel laag door instabiele normalisatie bij lage EV, niet door slechte beslissingen; de multiplicatieve xPass-factor straft risicovolle diepe passes (verklaart de relatief lage DQS van De Bruyne); gewichten van de EV-formule (0,15; 0,6/0,4) heuristisch; geen stand, speeltijd, formatie of vermoeidheid; EV van een niet-gespeelde pass is een counterfactual zonder reactie van de tegenstander. `pintelon2026aigestuurde`

### Topic F: Jeugd, talent en ethiek
Studie bij **18 scouts** van een Nederlandse profclub (gem. 9.5 jaar ervaring), die elk dezelfde **50 centrale verdedigers** beoordelen op 4 cues (FIFA 22-ratings: tackles, interceptions, sprintsnelheid, spelinzicht); criterium = marktwaarde. `peringa2025uniform`

| Parameter | Resultaat (gemiddelde, 95%-BI) | Betekenis |
|---|---|---|
| *Rₛ* | .93 [.92; .94], bereik .86-.95 | Scouts zijn consistent, maar niet perfect |
| *rₐ* | .62 [.56; .67], bereik .39-.74 | Accuraatheid van de scouts |
| *Rₑ* | .77 [.70; .84] | Wat de cues optimaal toelaten (opgeblazen door outlierverwijdering en n = 50) |
| *rₘ* | .68 [.64; .73] | **Voor elke scout** is het eigen model accurater dan de scout zelf |
| Δ *rₘ − rₐ* | .07 [.05; .09], bereik .02-.15 | Inconsistentie voegt ruis toe |
| *C* | −.04 [−.10; .02] | Afwijkingen van het eigen beleid zijn ruis, geen extra inzicht |
| *G* | .88 [.82; .94] | Hoog door gecorreleerde cues, niet door gelijke gewichten |

- *Rₑ* vs. *rₐ*: z = 2.46, p = .02: scouts hadden significant accurater kunnen zijn. *Rₑ* vs. *rₘ*: z = 1.93, p = .05 (niet significant).
- Relatief belang, scouts vs. optimaal: spelinzicht **35% vs. 11%**, interceptions 24% vs. 34%, tackles **23% vs. 44%**, sprintsnelheid 18% vs. 11%. Grote spreiding tussen scouts (sprintsnelheid 3-72%).
- Hoe dichter het beleid van een scout bij de optimale weging ligt, hoe accurater (r = −.96 met het gemiddelde absolute verschil); consistentie hangt samen met accuraatheid (*Rₛ* ↔ *rₐ*: r = .60).
- Uit eerdere literatuur: actuariële combinatie met optimale gewichten verslaat het klinische oordeel; zelfs gelijke of willekeurige gewichten doen het vaak beter, zolang ze consistent toegepast worden [via peringa2025uniform: Dawes & Corrigan (1974); Karelaia & Hogarth (2008); Yu & Kuncel (2020)]. Meta-analyse van 86 Lens Model-studies: r = .56 tussen accuraatheid en consistentie [via peringa2025uniform: Karelaia & Hogarth (2008)].
- Weinig tot geen consensus tussen scouts bij het rangschikken van spelers [via peringa2025uniform: Lüdin et al. (2023)].

**Methodologie van talentidentificatie** `bergkamp2019methodological` (position statement; overzichtstabel van 40 voetbalstudies, 2000-2018, n = 16 tot >20.000, U9 tot volwassen):
- **Criterium:** de meeste studies gebruiken het prestatieniveau of de selectiebeslissing als uitkomst; slechts enkele gebruiken een individuele prestatiemaat (gestructureerde ratings, succesvolle/onsuccesvolle acties in wedstrijden). Analyses zijn dan meestal t-tests/ANOVA op groepsgemiddelden.
- **Fidelity:** effectgroottes van klassieke predictoren (fysiek, fysiologisch, psychologisch) zijn **klein tot matig**. Voetbalspecifieke technische testen discrimineren consistenter, maar ook die missen context: de Loughborough Soccer Passing Test voorspelt passprestatie in een wedstrijd slecht [via bergkamp2019methodological: Serpiello et al. (2016)]. Predictoren op basis van acties in SSG's of wedstrijden (eventdata) onderscheiden elite van sub-elite relatief goed.
- **Range restriction:** in een nationale academie (U14-U16) waren er weinig grote verschillen tussen latere internationals, profs en amateurs; bij U16 onderscheiden enkel maximaal anaeroob vermogen en lengte (matig effect), niet sprint over 10-40 m of verticale sprong [via bergkamp2019methodological: le Gall et al. (2010)]. Sprintvermogen onderscheidt beter bij U14-U16 dan bij U17-U19 (meer fysiek divers, minder voorgeselecteerd).
- **Base rate, rekenvoorbeeld (Taylor-Russell):** 100.000 U12-spelers, 5.000 geselecteerd (selectieratio 5%), validiteit r = .4, base rate 1% → **success ratio 5.3%** (265/5.000), tegenover 1% zonder selectie; **73.5%** (735/1.000) van de geschikte spelers wordt niet geselecteerd; ±95% van de ongeschikte spelers wordt terecht afgewezen.
- Slechts **één** studie in de tabel bekijkt utiliteit [via bergkamp2019methodological: Höner & Votteler (2016)].
- Oordelen van coaches/scouts zijn vatbaar voor bias: huidskleur, reputatie, systematische voorkeur voor rijpere of vroeger geboren spelers (relative age effect).

**Subjectief vs. objectief vs. big data** `bareli2024feudal` (enkel abstract; conceptueel, geen cijfers): talentselectie steunt op het subjectieve *coach's eye* en op objectieve testformules (motorisch, psychologisch), die als complementair gezien worden; de auteurs pleiten voor big data / sport analytics als derde aanpak die beide verbindt.

**Methodologie TID in teamsporten** `barraclough2022methodological` (enkel abstract; narrative review, geen cijfers): drie aandachtspunten, namelijk de tijdspanne van het design, mono- vs. multidisciplinaire variabelen en de fidelity van de methode. Longitudinale, multidisciplinaire en ecologisch valide designs zijn te verkiezen. Sluit aan bij `bergkamp2019methodological`.

**Expertconsensus over TID/TD-aanbevelingen** `bennett2026talent` (real-time Delphi, 20 experts: 10 onderzoekers, 5 praktijkmensen, 5 beide; 15 aanbevelingen, beoordeeld op instemming en haalbaarheid; consensus = IQR ≤ 1.25):
- Consensus over instemming voor 100% van de TID-, 83% van de TD- en 80% van de systeemaanbevelingen.
- *Intuïtie aanvullen met contextueel gepaste, gevalideerde objectieve data*: **90% eens, 80% haalbaar**.
- *Longitudinaal de meest voorspellende prestatie-indicatoren opvolgen*: **75% eens, maar slechts 10% haalbaar** (60% onhaalbaar).
- *TID uitstellen tot na de groeispurt*: 50% eens, 35% haalbaar.
- Vier drempels: middelen en tijd, opleiding van coaches en atleten, **gebrek aan betekenisvolle objectieve data** (prestatiedata bevat "te veel variabiliteit en ruis"; data moet bruikbaar zijn voor selectors), concurrentie tussen sporten.

**Relative age effect en jeugdtraject bij de Belgische nationale ploegen** `billen2022careers` (bachelorproef KU Leuven, **niet peer-reviewed**; RBFA-data via Arne Jaspers: spelers geboren 1982-2006, wedstrijden 1995-2021, 29.631 datapunten):
- Significant RAE (oververtegenwoordiging van spelers uit het eerste geboortekwartaal) in **U15-U18** (p = .006-.016, Q1 vs. Q4), **niet** in U19 (p = .110), U21 (p = .293) en de Rode Duivels (p = .763). Geen verschil in RAE tussen posities.
- Selectie bij de **U21 (OR = 4.55)** en de **Olympische ploeg (OR = 6.89)** voorspelt een selectie bij de Rode Duivels; U15-U19 zijn niet significant. Spelers uit Q1 hebben lagere odds dan Q4 (OR = 0.55).
- 75% van de topspelers (>50 caps) speelde in de U21; sommige topspelers kwamen pas in oudere categorieën in beeld.
- De RBFA richtte het project *Futures* op voor laatrijpe jeugdspelers.
- Kanttekening: one-way ANOVA op aantallen per kwartaal (in plaats van een chi-kwadraattest tegen de geboorteverdeling) en een wisselende definitie van "selectie". Gebruik de peer-reviewed bronnen erachter (o.a. Helsen et al., Herrebrøden & Bjørndal) als je dit wilt onderbouwen.

**Dynamisch netwerkmodel van excellentie** `denhartigh2016dynamic` (enkel abstract; theorie + simulaties): excellentie ontstaat niet uit specifieke componenten (aanleg, motivatie, training, coaching) maar uit hun voortdurende interacties in een idiosyncratisch netwerk; simulaties reproduceren de idiosyncratische ontwikkelingstrajecten naar excellentie en de sterk scheve verdeling van productiviteit.

**Beslissingsgedrag van selectors** `johnston2025take` (enkel abstract; methodologische beschrijving + pilotstudie): de auteurs ontwikkelen een aanpak om het beslissingsgedrag van selectors (coaches, scouts, administrators) bij het beoordelen en selecteren van atleten te onderzoeken, testen die in een gesimuleerde selectieomgeving en bespreken de methodologische uitdagingen om cognitieve "quirks" rigoureus en valide in de juiste context te onderzoeken.

**Spelersselectie in academievoetbal** `kite2025player` (enkel abstract; narrative review): identificatie en selectie zijn cruciaal in de ontwikkeling van talent; spelers moeten in academies op verschillende leeftijden selectierondes overleven, en dat proces kan de ontwikkeling van veel talenten belemmeren. De review bundelt wat bekend is over het verbeteren van talentselectie, benoemt gaps en bespreekt persoonlijke en systemische cognitieve biases die beïnvloeden welke spelers ontwikkelingskansen krijgen.

**Vroege talentpromotie vs. duurzame ontwikkeling** `lundberg2026evidence` (enkel abstract; leading article, Zweedse context): het debat over vroege talentpromotieprogramma's tegenover inclusieve langetermijnmodellen weerspiegelt een wereldwijde spanning tussen topsportambities en levenslange sportdeelname. De auteurs stellen dat evidence-based jeugdsportsystemen beide doelen tegelijk kunnen dienen en geven principes (geen one-size-fits-all) voor federaties en clubs, met nadruk op welzijn, intrinsieke motivatie, contextueel bestuur en continue evaluatie.

### Topic X: Algemeen / kaders
- Vier analysestappen, hiërarchisch geordend naar waarde en complexiteit; idealiter worden ze gelijktijdig toegepast zodat inzichten uit de ene stap de andere verbeteren. `houtmeyers2021managing`
- Predictive en prescriptive analytics zijn nog weinig ingeburgerd in topsport; er is nog geen sterk bewijs voor accurate voorspelling van trainingsprocesdata. `houtmeyers2021managing`
- Dashboards met enkel beschrijvende data lopen het risico op *cherry picking* om bestaande overtuigingen te bevestigen. `houtmeyers2021managing`
- Het RBFA-platform ondersteunt vooral descriptieve analyse en toont geen alternatieve acties binnen spelsituaties; prescriptieve systemen die in open spel concrete alternatieven genereren zijn schaars. `pintelon2026aigestuurde`
- Zonder scenario-specifieke promptinstructies koos het LLM steeds de framing "gemiste kans", ook wanneer de speler de betere keuze had gemaakt; bij falen van de API valt het systeem terug op een sjabloonzin uit de labels. `pintelon2026aigestuurde`

---

## 3. Bouwstenen per hoofdstuk van de scriptie

### Inleiding (context en probleemstelling)
- Positioneer de masterproef in het framework van `houtmeyers2021managing`: fysieke profielen = **descriptive**, mismatches verklaren en koppelen aan kansen = **diagnostic/predictive**, advies over matchups (*welke back tegen Yamal?*) = richting **prescriptive**.
- De RBFA evolueert van scoutoordeel naar datagestuurde profielen; `peringa2025uniform` onderbouwt waarom een consistente, actuariële combinatie van metrieken accurater is dan een holistisch oordeel.
- Event- en trackingdata leveren elk iets anders; samen geven ze context die geen van beide apart biedt `oonk2026databallpy`.
- Talentidentificatie evolueert van subjectieve evaluatie door coaches en scouts naar evidence-based procedures, maar de bevindingen zijn inconsistent en er is geen eenduidige set predictoren `bergkamp2019methodological`.
- Een eerdere masterproef bij RBFA/IDLab bouwde een prescriptief tactisch dashboard (pass- en looplijnadvies) en ging ervan uit dat alle spelers dezelfde fysieke capaciteiten hebben; deze masterproef vult de fysieke kant in `pintelon2026aigestuurde`.

### Data-hoofdstuk (RBFA-dataplatform)
- Beschrijf het platform zoals het al gedocumenteerd is: Second Spectrum-tracking aan 25 Hz, coördinaten met oorsprong in het midden, JSONL- vs. genormaliseerde PKL-bestanden, `tracking_frame`-koppeling door de RBFA, BigQuery `pintelon2026aigestuurde`. Na te gaan welke van deze bronnen ook SkillCorner-fysieke data bevatten.
- Controleer de aanvalsrichting per helft (bv. via de doelman) en ontbrekende `tracking_frame`-kolommen vóór je fysieke metrieken per balbezit berekent `pintelon2026aigestuurde`.

### Lit. 2.1 / 2.3: Waarom fysieke profielen uit wedstrijddata?
- Fysieke metrieken uit trackingdata van wedstrijden zijn **high-fidelity samples** van het criteriumgedrag, i.p.v. geïsoleerde testen (*signs*); samples voorspellen in de selectiepsychologie beter, zeker in homogene groepen en bij multidimensionale uitkomsten `bergkamp2019methodological`.
- Verschillende posities vereisen andere taken en vaardigheden: vergelijk spelers binnen positie (sluit aan bij de normalisatie per positie van het RBFA-platform) `bergkamp2019methodological`.

### Lit. 2.2: Meten
- Trackingdata bevat ruis; filteren en afleiden van snelheid en versnelling is een noodzakelijke preprocessingstap `oonk2026databallpy`.
- Naïeve synchronisatie (±4 s willekeurige fout) is onvoldoende voor contextuele analyse `oonk2026databallpy`.
- Valideer variabelen en wees je bewust dat fysieke metrieken proxy's zijn `houtmeyers2021managing`.
- Trackingfouten (occlusies, lage resolutie) werken door in afgeleide snelheid en versnelling, en dus in fysieke indicatoren `davis2024methodology`.
- Kies de normalisatie bewust: per 90 min houdt geen rekening met variabele wedstrijdduur en balspeeltijd; SkillCorner normaliseert sommige fysieke metrieken per 60 min balspeeltijd `davis2024methodology`.

### Lit. 2.3 / Methodologie (Taak 3: baselinemodel)
- Kies variabelen op basis van evidentie en reduceer gecorreleerde variabelen (bv. PCA) zonder unieke informatie te verliezen `houtmeyers2021managing`.
- Bij gecorreleerde metrieken: relatief belang via dominance analysis i.p.v. ruwe regressiegewichten `peringa2025uniform`.
- Consistente weging (ook van een niet-optimale formule) verhoogt de accuraatheid t.o.v. een holistisch oordeel: argument voor vaste profielscores `peringa2025uniform`.
- Neem contextfactoren op die fysieke metrieken beïnvloeden: formatie van de ploeg (back three vs. back four), thuis/uit, stand, tegenstander `davis2024methodology`.
- Herhaalde metingen van dezelfde speler en verschillen tussen posities: overweeg hiërarchische modellen (groepen = positie, ploeg) `davis2024methodology`.
- Afgeleide indicatoren (tellingen, gemiddelden) negeren context; modelgebaseerde indicatoren leren die uit historische data `davis2024methodology`. Het RBFA-platform werkt nu met afgeleide metrieken.
- Tooling: DataBallPy voor inladen, synchroniseren, snelheid/versnelling en afstand in snelheids- en acceleratiezones `oonk2026databallpy`.

### Lit. 2.4 / Methodologie (OV2: mismatches)
- Pitch control en pressure als bestaande bouwstenen om duels en linies te kwantificeren `oonk2026databallpy`.
- Bestaande pitch control op RBFA-data neemt voor iedereen vmax = 5,0 m/s en 0,7 s reactietijd aan, wat duels met een groot snelheidsverschil fout modelleert; fysieke profielen (topsnelheid, versnelling, vermoeidheid) kunnen de TTI personaliseren. Dat geeft een concrete, meetbare definitie van een fysieke mismatch op duelniveau: het verschil in bereikbare ruimte tussen gepersonaliseerde en uniforme pitch control `pintelon2026aigestuurde`.
- Fysieke haalbaarheid van looplijnen wordt nu begrensd met een vaste snelheid (max(huidige snelheid, 2,0 m/s)); met spelersprofielen kan die grens per speler gezet worden `pintelon2026aigestuurde`.

### Lit. 2.5 / Evaluatie (OV3, Taak 7)
- Correlatie ≠ causaliteit; observationeel sportonderzoek laat zelden causale conclusies toe → formuleer de link mismatch ↔ kans als associatie `houtmeyers2021managing`.
- Evalueer voorspellende modellen out-of-sample (split-sample) en met geschikte maten (sensitiviteit, specificiteit, MAE) `houtmeyers2021managing`.
- Rapporteer onzekerheid (betrouwbaarheidsintervallen); data bevat meetfout en biologische variatie `houtmeyers2021managing`.
- Synchronisatiekwaliteit beïnvloedt de kwaliteit van xG-modellen `oonk2026databallpy`.
- **Keuze van de uitkomstmaat:** gebruik een individuele, positiespecifieke prestatiemaat (gewogen events per positie, met gewichten van experts of via ML; of positiedata), niet het prestatieniveau of de selectie. Valideer de betrouwbaarheid en validiteit van die maat vóór je ze als criterium gebruikt `bergkamp2019methodological`.
- Individuele prestatie hangt af van ploegmaats en tegenstanders: een directe brug naar mismatches (OV2) en een confounder om te benoemen bij OV3 `bergkamp2019methodological`.
- **Range restriction bij de RBFA:** nationale jeugd- en A-ploegspelers zijn sterk voorgeselecteerd, dus fysieke verschillen en verbanden met uitkomsten zullen kleiner lijken dan in de populatie. Vermeld expliciet naar welke populatie je veralgemeent `bergkamp2019methodological`.
- Meet prestatie longitudinaal over een reeks wedstrijden voor betrouwbare individuele scores: onderbouwt de stabiliteitstest (OV1, Taak 7) `bergkamp2019methodological`.
- Een gekalibreerde xG/EV-pijplijn op RBFA-tracking bestaat al (xG AUC 0,817, xPass AUC 0,930) en kan dienen als uitkomstmaat om mismatches aan kansen te koppelen (OV3). Kalibreer kansen als je ze in een formule gebruikt (Brier halveert) `pintelon2026aigestuurde`.
- Split op wedstrijdniveau (80/20) om lekken tussen train en test te vermijden `pintelon2026aigestuurde`.
- Let op met verhoudingsmaten in zones met lage waarden: de DQS wordt instabiel wanneer teller en noemer bijna nul zijn. Hetzelfde risico geldt voor relatieve mismatchmaten `pintelon2026aigestuurde`.
- **Stabiliteitstest (OV1):** correlatie van profielmetrieken tussen twee helften van de data of tussen opeenvolgende seizoenen (minimum speeltijd, bv. ≥ 900 min zoals in de illustratie); of een nearest-neighbourtest: vindt het profiel van seizoen t de speler terug in seizoen t+1? Een chronologische split binnen een seizoen is minder geschikt `davis2024methodology`.
- Evalueer de profielen (indicator) en de modellen eronder (bv. clustering, mismatchmodel) apart `davis2024methodology`.
- Valideer niet via correlatie met marktwaarde of speeltijd: die bevatten veel niet-prestatiegebonden informatie, en een hoge correlatie betekent dat de indicator niets nieuws toevoegt `davis2024methodology`.
- Splits voor voorspellende tests (mismatch ↔ xG) op wedstrijd of seizoen, niet willekeurig over frames of acties `davis2024methodology`.
- Credit assignment, counterfactuals en interventies (coaches passen tactiek aan aan de stand) beperken causale uitspraken over mismatches ↔ kansen (OV3) `davis2024methodology`.
- Bij kansmodellen waarvan je kansen optelt of aftrekt (bv. xG-verschillen): Brier-score + reliability diagram `davis2024methodology`.
- Les uit dezelfde context: een formele expertvalidatie werd niet uitgevoerd wegens tijdgebrek (enkel informele feedback van RBFA-analisten). Plan de expertvalidatie van Taak 7 dus vroeg in `pintelon2026aigestuurde`.

### Evaluatie: expertvalidatie met RBFA-analisten (Taak 7)
- Combineer een face validity-check (staan de spelers die iedereen als snel/sterk kent bovenaan?) met een diepere expertvalidatie die ook bruikbaarheid meet: tijdwinst, nieuwe inzichten, correcte interpretatie door de analist `davis2024methodology`. Let op: face validity werkt slechter voor defensieve prestaties.
- Verificatie laat domeinexperts zelf het model bevragen in situaties met sterke intuïtie, zonder ML-kennis `davis2024methodology`.
- Gebruik de **subjectzijde van het Lens Model**: laat analisten profielen/mismatches beoordelen op basis van fysieke metrieken (≤ 7 cues), schat hun beoordelingsbeleid (*bₛ*) en consistentie (*Rₛ*), en vergelijk met de modelscores. Kan zonder prestatiecriterium `peringa2025uniform`.
- Aandachtspunten uit de studie: 50 beoordelingen per expert is klein (overfitting); bij één positie is de taak makkelijker consistent dan bij meerdere posities `peringa2025uniform`.
- Experts verzetten zich soms tegen gestandaardiseerde procedures; laat hen bv. eigen wegingsregels opstellen om de acceptatie te verhogen [via peringa2025uniform: Neumann et al. (2021)]. Acceptatie van voorschrijvende analyse hangt ook af van haalbaarheid, complexiteit en bruikbaarheid `houtmeyers2021managing`.

### Lit. 2.6 / Ethische reflectie
- Gestandaardiseerde beoordeling is transparanter (indicatoren communiceerbaar naar spelers) en eerlijker (dezelfde procedure voor iedereen) `peringa2025uniform`.
- Expertkennis is gevoelig voor cognitieve biases zoals confirmation bias `houtmeyers2021managing`.
- Oordelen over talent worden beïnvloed door factoren die los staan van prestatie (huidskleur, reputatie, maturiteit, geboortemaand) `bergkamp2019methodological`.
- Bij Belgische jeugdinternationals is er een RAE t.e.m. U18: fysieke profielen van jeugdspelers kunnen vertekend zijn door maturiteit en geboortekwartaal. Overweeg om dat te vermelden of te corrigeren, en benoem het als ethisch risico als profielen gebruikt worden voor selectie `billen2022careers`.
- Trackingdata wordt bij de RBFA gepseudonimiseerd opgeslagen (interne tracking-ID's); volledige anonimisering is niet haalbaar zonder bruikbaarheid te verliezen, dus transparantie naar spelers is aangewezen `pintelon2026aigestuurde`.
- Risico dat een spelersscore (daar de DQS) buiten de coachingcontext gebruikt wordt, bv. bij transfers of contracten; hetzelfde geldt voor fysieke profielscores. Het systeem als gesprekspartner van de coach, niet als autoriteit `pintelon2026aigestuurde`.
- Zelfs een valide procedure (r = .4) mist bij een lage base rate de meerderheid van de geschikte spelers (73.5% in het rekenvoorbeeld): realistische verwachtingen communiceren naar staf en spelers `bergkamp2019methodological`.

---

## 4. Synthese: technieken en tools

| Techniek / tool | Sterktes | Beperkingen | Benodigde data | Bron |
|---|---|---|---|---|
| Lens Model (subject + ecologie) | Maakt weging en consistentie van experts zichtbaar; vergelijkt met optimale combinatie | Vereist kwantificeerbare cues en voor accuraatheid een prestatiecriterium; kleine n per expert | Cues, expertoordelen, (criterium) | `peringa2025uniform` |
| Dominance analysis | Relatief belang bij gecorreleerde variabelen | Rekenintensief bij veel variabelen | Regressiemodel | `peringa2025uniform` |
| PCA / datareductie | Beschrijft gecorreleerde metrieken efficiënter | Componenten minder interpreteerbaar | Veel gecorreleerde metrieken | `houtmeyers2021managing` |
| Split-sample validatie | Detecteert overfitting | Minder data voor training | Voldoende observaties | `houtmeyers2021managing` |
| Needleman-Wunsch-synchronisatie (DataBallPy) | Snel (seconden), provider-onafhankelijk, learning-free | Validatie in aparte paper; SkillCorner-ondersteuning nog na te gaan | Event- + trackingdata | `oonk2026databallpy` |
| Pitch control / pressure (DataBallPy) | Kant-en-klaar, kwantificeert ruimte en druk | Aannames van het onderliggende model | Trackingdata (+ snelheden) | `oonk2026databallpy` |
| Correctie voor range restriction | Schat het verband in de onbeperkte populatie | Vereist variantie van de volledige kandidatenpool; nog niet toegepast in talentonderzoek | Predictorscores van alle kandidaten | `bergkamp2019methodological` |
| Spearman-pitch control met TTI (uniforme parameters) | Fysisch interpreteerbaar; per frame berekenbaar, cachebaar | Zelfde vmax (5,0 m/s) en reactietijd (0,7 s) voor iedereen: fout bij snelheidsverschillen | Tracking (posities + snelheden) | `pintelon2026aigestuurde` |
| Gepersonaliseerde pitch control (voorstel) | Koppelt fysieke profielen aan ruimtecontrole en duels | Niet geïmplementeerd of gevalideerd in de bron | Tracking + spelersspecifieke topsnelheid, versnelling, vermoeidheid | `pintelon2026aigestuurde` |
| Bezitsdetectie uit tracking (Vidal-Codina et al.) | Werkt zonder eventdata (realtime, rust) | Vaste drempels (1,5 m; 10°; 5 m/s) | Tracking speler + bal | `pintelon2026aigestuurde` |
| xG/xPass met XGBoost + isotone kalibratie | Goede discriminatie (AUC 0,817 / 0,930), gekalibreerde kansen | xG op andere data dan xPass (domain shift) | Event + tracking; StatsBomb voor schoten | `pintelon2026aigestuurde` |
| EV per passoptie + ΔEV / DQS | Vergelijkt gespeelde met beste optie in dezelfde situatie; positie-onafhankelijk bedoeld | Heuristische gewichten; geen matchcontext; counterfactual; instabiel bij lage EV | Event + tracking, xG/xPass, pitch control | `pintelon2026aigestuurde` |
| Wordalisation (4 stappen, LLM) | Maakt modeloutput leesbaar voor coaches | Drempels voorlopig heuristisch; framing moet expliciet per scenario | Modeloutput + populatieverdeling | `pintelon2026aigestuurde` |
| Split-half / seizoen-op-seizoen-correlatie | Eenvoudig, interpreteerbaar maat voor betrouwbaarheid | Chronologische split binnen een seizoen vertekend (blessures, kalender); vraagt minimum speeltijd | Indicator per speler over ≥ 2 periodes | `davis2024methodology` |
| Nearest-neighbour over seizoenen | Test of een multidimensioneel profiel een speler herkenbaar terugvindt | Afhankelijk van afstandsmaat en populatie | Profielvectoren in opeenvolgende seizoenen | [via davis2024methodology: Decroos & Davis (2019)] |
| Groepsgewijze cross-validatie (walk-forward, subject-level, leave-one-competition-out) | Vermijdt lekken door temporele afhankelijkheid en zelfde speler | Minder trainingsdata per fold; seizoenen lopen niet overal gelijk | Tijd-, speler- of competitie-ID | `davis2024methodology` |
| Hiërarchische modellen / multicalibratie | Vangen herhaalde metingen en groepsstructuur (positie, ploeg) op | Complexer te fitten en uit te leggen | Spelers- en groeps-ID's | `davis2024methodology` |
| Face validity + expertvalidatie | Meet vertrouwen en bruikbaarheid in de praktijk | Toegang tot experts; vaak niet publiceerbaar; zwakker voor defensie | Experts (bv. RBFA-analisten) | `davis2024methodology` |
| Modelverificatie (bv. Veritas voor tree ensembles) | Vindt labelfouten en onrealistisch gedrag buiten de data | Je moet weten wat te zoeken; iteratief | Getraind model + domeinkennis | `davis2024methodology` |
| Taylor-Russell-utiliteitsmodel | Vertaalt validiteit naar praktisch nut (success ratio) | Dichotomiseert het criterium; base rate moeilijk te schatten (eventueel via experts) | Validiteit, selectieratio, base rate | `bergkamp2019methodological` |

---

## 5. Gaps en open punten

- **Topics A en C** hebben nog geen inhoudelijke bronnen (positiespecifieke fysieke metrieken, clustering van fysieke profielen). Topics D en E hebben enkel `pintelon2026aigestuurde` (tactisch, niet fysiek) en tooling: een definitie van fysieke matchups/mismatches en de link fysiek ↔ uitkomst ontbreken nog.
- Gap: pitch control en looplijnmodellen op RBFA-data gaan uit van **identieke fysieke capaciteiten** voor alle spelers (vmax 5,0 m/s, reactietijd 0,7 s) `pintelon2026aigestuurde`. Spelersspecifieke fysieke parameters uit profielen (OV1) invullen en het verschil met het uniforme model als duelmismatch meten (OV2) is een concrete bijdrage. Eerst Vermeulen (2025) lezen: daar is dit mogelijk al uitgewerkt.
- Gap: het prescriptieve RBFA-systeem werd **niet formeel gevalideerd** met experts `pintelon2026aigestuurde`; een expertvalidatie (Taak 7) zou de eerste in deze context zijn.
- Geen enkele verwerkte bron onderzoekt **SkillCorner/broadcast tracking** zelf (enkel vermeld: normalisatie per 60 min balspeeltijd `davis2024methodology`).
- Gap: methoden voor de **betrouwbaarheid** van indicatoren bestaan en zijn toegepast op technische indicatoren (VAEP, xT, minuten), maar niet op **fysieke profielen** of matchupmaten `davis2024methodology`. Stabiliteit over wedstrijden en seizoenen blijft dus open voor OV1.
- Gap: er is weinig onderzoek naar wanneer sportdata verouderd raakt (hoeveel seizoenen mee te nemen) `davis2024methodology`. Relevant voor de keuze van het aantal seizoenen in het baselinemodel.
- Gap: er bestaat nog geen gevalideerde **individuele, objectieve maat voor wedstrijdprestatie** die rekening houdt met ploegmaats en tegenstanders `bergkamp2019methodological`. Relevant voor de uitkomstmaat in OV3 en de context-afhankelijkheid in OV2.
- Gap: modellen van talentontwikkeling zoals `denhartigh2016dynamic` zijn theoretisch en gebruiken grove uitkomsten (doelpunten, caps); hoe **fysieke** wedstrijdprofielen zich individueel ontwikkelen over seizoenen is niet onderzocht. Raakt de stabiliteitsvraag van OV1.
- Gap: er zijn weinig valide methoden om het beslissingsgedrag van selectors te onderzoeken in een representatieve context `johnston2025take`. Raakt de opzet van de expertvalidatie met RBFA-analisten (Taak 7).
- Gap: volgens `kite2025player` blijven er belangrijke gaps in onderzoek naar talentselectie in academievoetbal, o.a. over cognitieve biases bij selectie. Na grondiger lezen te concretiseren (bv. voor de link met OV2).
- Gap die al te formuleren is: het Lens Model is nog weinig toegepast in sport `peringa2025uniform` en nog niet op **fysieke** tracking-metrieken of matchup-oordelen. Mogelijke bijdrage in Taak 7.
