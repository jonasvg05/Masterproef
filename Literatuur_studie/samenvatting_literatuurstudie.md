# Samenvatting literatuurstudie

> Werkdocument om de scriptie uit te schrijven. Bevat de belangrijkste begrippen, resultaten (met cijfers), argumenten en methodologische lessen uit de verwerkte bronnen, geordend per topic en per hoofdstuk van de scriptie. Elke bewering heeft een BibTeX-key, zodat je ze rechtstreeks kunt citeren met `\citet{key}` of `\citep{key}`.
>
> **Conventies**
> - `[key]` = de bron zelf beweert of meet dit.
> - `[via key: Auteur (jaar)]` = **secundaire vermelding**: de bron citeert een ander werk. Niet zo citeren in de scriptie zonder het originele werk zelf te lezen (dan is het een snowballing-kandidaat).
> - Engelse vakterm cursief, met de Nederlandse vertaling die in de scriptie gebruikt wordt.
>
> Laatst bijgewerkt: 23 november 2026. Verwerkte bronnen: 8 (`peringa2025uniform`, `houtmeyers2021managing`, `oonk2026databallpy`, `bergkamp2019methodological`, `bareli2024feudal`, `barraclough2022methodological`, `bennett2026talent`, `billen2022careers`).

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
| Pitch control | Model dat per locatie op het veld de kans schat dat een team de bal daar controleert (implementatie volgens Fernandez & Bornn, 2018). | `oonk2026databallpy` | D |
| Pressure / druk | Maat voor de defensieve druk op een speler (implementatie volgens Andrienko et al., 2017 en Herold et al., 2022). | `oonk2026databallpy` | D |
| Expected Goals (xG) / Expected Threat (xT) | xG: kans dat een schot een doelpunt wordt; xT: waarde van balposities op basis van de kans op een doelpunt. Beide beschikbaar in DataBallPy. | `oonk2026databallpy` | E |
| Brier loss | Gemiddelde kwadratische fout van voorspelde kansen (lager = beter); gebruikt om xG-modellen te evalueren. | `oonk2026databallpy` | E |

---

## 2. Resultaten met cijfers

### Topic A: Fysieke prestatie-indicatoren
*Nog geen inhoudelijke bronnen.* Indirect: fysieke predictoren uit geïsoleerde testen (sprint, sprong, uithouding) hebben in talentstudies kleine tot matige effecten en hun onderscheidend vermogen hangt af van leeftijd en voorselectie `bergkamp2019methodological`.

### Topic B: Meten, betrouwbaarheid en normalisatie
- Gewoon de tijdstempels van event- en trackingdata naast elkaar leggen geeft een fout van **1.82 (±4.06) s** [via oonk2026databallpy: Anzer & Bauer (2021)]. De willekeurige component is het probleem: in 4 s kan de spelsituatie volledig veranderd zijn. `oonk2026databallpy`
- Met correcte synchronisatie daalt de **Brier loss van een xG-model van 0.096 naar 0.082**; features die event- en trackinginformatie combineren hebben enkel bij correcte synchronisatie een niet-nul belang [via oonk2026databallpy: Oonk, Grob & Kempe (2025)].
- DataBallPy synchroniseert een wedstrijd in **enkele seconden** i.p.v. ~10 min voor de oorspronkelijke Needleman-Wunsch-aanpak; alternatieven zoals ETSY duren tot 3 min per match en kunnen events niet toewijzen. `oonk2026databallpy`
- Ruwe trackingbestanden van **tot 400 MB per wedstrijd** worden 20-100 MB als opgeslagen Game-object (Parquet/JSON). `oonk2026databallpy`
- Data uit topsport (GNSS-variabelen, vragenlijsten) zijn vaak slecht gevalideerd en meten vaak indirect het mechanisme van interesse (bv. afstand aan hoge snelheid als proxy voor spierbelasting). `houtmeyers2021managing`

### Topic C: Fysieke profilering en rolclustering
*Nog geen bronnen.* Indirect: bij veel gecorreleerde variabelen zijn regressiegewichten geen goede maat voor belang; gebruik relatief belang (dominance analysis) `peringa2025uniform` of datareductie zoals PCA `houtmeyers2021managing`.

### Topic D: Matchups en mismatches
*Nog geen inhoudelijke bronnen.* Beschikbare tooling: pitch control, pressure, Voronoi-ruimte en *Dangerous Accessible Space* zijn geïmplementeerd in DataBallPy. `oonk2026databallpy`

### Topic E: Link met wedstrijduitkomst
*Nog geen inhoudelijke bronnen.* Zie het xG-resultaat onder topic B: de kwaliteit van de koppeling tussen event en tracking beïnvloedt rechtstreeks de kwaliteit van uitkomstmodellen. `oonk2026databallpy`

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

### Topic X: Algemeen / kaders
- Vier analysestappen, hiërarchisch geordend naar waarde en complexiteit; idealiter worden ze gelijktijdig toegepast zodat inzichten uit de ene stap de andere verbeteren. `houtmeyers2021managing`
- Predictive en prescriptive analytics zijn nog weinig ingeburgerd in topsport; er is nog geen sterk bewijs voor accurate voorspelling van trainingsprocesdata. `houtmeyers2021managing`
- Dashboards met enkel beschrijvende data lopen het risico op *cherry picking* om bestaande overtuigingen te bevestigen. `houtmeyers2021managing`

---

## 3. Bouwstenen per hoofdstuk van de scriptie

### Inleiding (context en probleemstelling)
- Positioneer de masterproef in het framework van `houtmeyers2021managing`: fysieke profielen = **descriptive**, mismatches verklaren en koppelen aan kansen = **diagnostic/predictive**, advies over matchups (*welke back tegen Yamal?*) = richting **prescriptive**.
- De RBFA evolueert van scoutoordeel naar datagestuurde profielen; `peringa2025uniform` onderbouwt waarom een consistente, actuariële combinatie van metrieken accurater is dan een holistisch oordeel.
- Event- en trackingdata leveren elk iets anders; samen geven ze context die geen van beide apart biedt `oonk2026databallpy`.
- Talentidentificatie evolueert van subjectieve evaluatie door coaches en scouts naar evidence-based procedures, maar de bevindingen zijn inconsistent en er is geen eenduidige set predictoren `bergkamp2019methodological`.

### Lit. 2.1 / 2.3: Waarom fysieke profielen uit wedstrijddata?
- Fysieke metrieken uit trackingdata van wedstrijden zijn **high-fidelity samples** van het criteriumgedrag, i.p.v. geïsoleerde testen (*signs*); samples voorspellen in de selectiepsychologie beter, zeker in homogene groepen en bij multidimensionale uitkomsten `bergkamp2019methodological`.
- Verschillende posities vereisen andere taken en vaardigheden: vergelijk spelers binnen positie (sluit aan bij de normalisatie per positie van het RBFA-platform) `bergkamp2019methodological`.

### Lit. 2.2: Meten
- Trackingdata bevat ruis; filteren en afleiden van snelheid en versnelling is een noodzakelijke preprocessingstap `oonk2026databallpy`.
- Naïeve synchronisatie (±4 s willekeurige fout) is onvoldoende voor contextuele analyse `oonk2026databallpy`.
- Valideer variabelen en wees je bewust dat fysieke metrieken proxy's zijn `houtmeyers2021managing`.

### Lit. 2.3 / Methodologie (Taak 3: baselinemodel)
- Kies variabelen op basis van evidentie en reduceer gecorreleerde variabelen (bv. PCA) zonder unieke informatie te verliezen `houtmeyers2021managing`.
- Bij gecorreleerde metrieken: relatief belang via dominance analysis i.p.v. ruwe regressiegewichten `peringa2025uniform`.
- Consistente weging (ook van een niet-optimale formule) verhoogt de accuraatheid t.o.v. een holistisch oordeel: argument voor vaste profielscores `peringa2025uniform`.
- Tooling: DataBallPy voor inladen, synchroniseren, snelheid/versnelling en afstand in snelheids- en acceleratiezones `oonk2026databallpy`.

### Lit. 2.4 / Methodologie (OV2: mismatches)
- Pitch control en pressure als bestaande bouwstenen om duels en linies te kwantificeren `oonk2026databallpy`.

### Lit. 2.5 / Evaluatie (OV3, Taak 7)
- Correlatie ≠ causaliteit; observationeel sportonderzoek laat zelden causale conclusies toe → formuleer de link mismatch ↔ kans als associatie `houtmeyers2021managing`.
- Evalueer voorspellende modellen out-of-sample (split-sample) en met geschikte maten (sensitiviteit, specificiteit, MAE) `houtmeyers2021managing`.
- Rapporteer onzekerheid (betrouwbaarheidsintervallen); data bevat meetfout en biologische variatie `houtmeyers2021managing`.
- Synchronisatiekwaliteit beïnvloedt de kwaliteit van xG-modellen `oonk2026databallpy`.
- **Keuze van de uitkomstmaat:** gebruik een individuele, positiespecifieke prestatiemaat (gewogen events per positie, met gewichten van experts of via ML; of positiedata), niet het prestatieniveau of de selectie. Valideer de betrouwbaarheid en validiteit van die maat vóór je ze als criterium gebruikt `bergkamp2019methodological`.
- Individuele prestatie hangt af van ploegmaats en tegenstanders: een directe brug naar mismatches (OV2) en een confounder om te benoemen bij OV3 `bergkamp2019methodological`.
- **Range restriction bij de RBFA:** nationale jeugd- en A-ploegspelers zijn sterk voorgeselecteerd, dus fysieke verschillen en verbanden met uitkomsten zullen kleiner lijken dan in de populatie. Vermeld expliciet naar welke populatie je veralgemeent `bergkamp2019methodological`.
- Meet prestatie longitudinaal over een reeks wedstrijden voor betrouwbare individuele scores: onderbouwt de stabiliteitstest (OV1, Taak 7) `bergkamp2019methodological`.

### Evaluatie: expertvalidatie met RBFA-analisten (Taak 7)
- Gebruik de **subjectzijde van het Lens Model**: laat analisten profielen/mismatches beoordelen op basis van fysieke metrieken (≤ 7 cues), schat hun beoordelingsbeleid (*bₛ*) en consistentie (*Rₛ*), en vergelijk met de modelscores. Kan zonder prestatiecriterium `peringa2025uniform`.
- Aandachtspunten uit de studie: 50 beoordelingen per expert is klein (overfitting); bij één positie is de taak makkelijker consistent dan bij meerdere posities `peringa2025uniform`.
- Experts verzetten zich soms tegen gestandaardiseerde procedures; laat hen bv. eigen wegingsregels opstellen om de acceptatie te verhogen [via peringa2025uniform: Neumann et al. (2021)]. Acceptatie van voorschrijvende analyse hangt ook af van haalbaarheid, complexiteit en bruikbaarheid `houtmeyers2021managing`.

### Lit. 2.6 / Ethische reflectie
- Gestandaardiseerde beoordeling is transparanter (indicatoren communiceerbaar naar spelers) en eerlijker (dezelfde procedure voor iedereen) `peringa2025uniform`.
- Expertkennis is gevoelig voor cognitieve biases zoals confirmation bias `houtmeyers2021managing`.
- Oordelen over talent worden beïnvloed door factoren die los staan van prestatie (huidskleur, reputatie, maturiteit, geboortemaand) `bergkamp2019methodological`.
- Bij Belgische jeugdinternationals is er een RAE t.e.m. U18: fysieke profielen van jeugdspelers kunnen vertekend zijn door maturiteit en geboortekwartaal. Overweeg om dat te vermelden of te corrigeren, en benoem het als ethisch risico als profielen gebruikt worden voor selectie `billen2022careers`.
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
| Taylor-Russell-utiliteitsmodel | Vertaalt validiteit naar praktisch nut (success ratio) | Dichotomiseert het criterium; base rate moeilijk te schatten (eventueel via experts) | Validiteit, selectieratio, base rate | `bergkamp2019methodological` |

---

## 5. Gaps en open punten

- **Topics A, C, D en E** hebben nog geen inhoudelijke bronnen: positie-specifieke fysieke metrieken, clustering van fysieke profielen, definities van matchups/mismatches en de link fysiek ↔ uitkomst ontbreken nog volledig.
- Geen enkele verwerkte bron behandelt **SkillCorner/broadcast tracking** of de **stabiliteit** van fysieke profielen over wedstrijden en seizoenen (OV1).
- Gap: er bestaat nog geen gevalideerde **individuele, objectieve maat voor wedstrijdprestatie** die rekening houdt met ploegmaats en tegenstanders `bergkamp2019methodological`. Relevant voor de uitkomstmaat in OV3 en de context-afhankelijkheid in OV2.
- Gap die al te formuleren is: het Lens Model is nog weinig toegepast in sport `peringa2025uniform` en nog niet op **fysieke** tracking-metrieken of matchup-oordelen. Mogelijke bijdrage in Taak 7.
