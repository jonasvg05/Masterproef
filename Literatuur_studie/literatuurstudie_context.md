# Context: literatuurstudie masterproef

> **Instructie voor Claude.** Je helpt een masterstudent (Jonas Van Goethem, Industrieel Ingenieur Informatica, UGent) met de **literatuurstudie** van zijn masterproef. Schrijf in het **Nederlands**. Werk volgens de werkwijze in §5, en lever per nieuwe bron de output uit §6.
>
> **Harde regels:**
> - **Verzin nooit bronnen, auteurs, jaartallen, DOI's of resultaten.** Haal gegevens alleen uit de PDF of tekst die Jonas aanlevert, of uit een bron die je effectief geraadpleegd hebt. Noem je een bron uit je geheugen (bv. als zoektip), zeg dan expliciet dat de gegevens nog gecontroleerd moeten worden.
> - Zoek **geen nieuwe bronnen** op tenzij Jonas daarom vraagt.
> - Vul de kolom *Leesniveau* pas in als Jonas zegt hoe grondig hij de bron gelezen heeft.
> - Een bron uit de referentielijst van een andere paper is een **snowballing-kandidaat**, nog geen gelezen bron.

---

## 1. De masterproef

| | |
|---|---|
| **Titel** | Talent detection in youth soccer data of RBFA (voorstel 50295) |
| **Gekozen opdracht** | RBFA "Project 1": **fysieke spelersprofielen** en het detecteren van **fysieke mismatches** (duel, linie, team) |
| **Partners** | Koninklijke Belgische Voetbalbond (RBFA) / IDLab-IMPACT (UGent) |
| **Promotoren** | Steven Verstockt, Matthieu Lenoir |
| **Begeleiders** | Maarten Slembrouck, Laurens Gilson, Arne Jaspers |
| **Data** | Event-, tracking- en fysieke data (o.a. SkillCorner). Platform van de RBFA draait op Google Cloud. NDA: data enkel voor de masterproef. |

**Doelstelling:** datamodellen en metrieken voor fysieke spelersprofielen (volume/intensiteit, topsnelheid, richtingsveranderingen, acceleraties, luchtsterkte, ...) en voor het signaleren van gevaarlijke matchups, positief en negatief. Voorbeeldvragen van de RBFA: *"Welke van onze backs is het meest geschikt tegen Yamal?"*, *"Kunnen we de fysieke kracht van Senegal op het middenveld aan?"*

Het bestaande RBFA-platform toont per speler rolprofielen met een radar van metrics op schaal 1-20, vergeleken met dezelfde positie, competitie en seizoen (10.5 = gemiddelde, minstens 180 min, kleine samples geregresseerd naar het gemiddelde).

**Onderzoeksvragen:**
- **OV1.** Welke fysieke profielen kunnen op basis van event-, tracking- en fysieke data objectief onderscheiden worden, en hoe stabiel is het profiel van een speler over wedstrijden en seizoenen?
- **OV2.** Hoe kan een fysieke mismatch tussen tegenstanders gedefinieerd en gemeten worden op het niveau van een duel, een linie en het volledige team?
- **OV3.** In welke mate hangen de gesignaleerde mismatches samen met wat er op het veld gebeurt, zoals het creëren of toestaan van kansen?

**Relevante taken in het werkplan:** Taak 3 = baselinemodel (normalisatie per minuut en positie, clustering met k-means/GMM). Taak 7 = evaluatie: stabiliteitstest, voorspellende test (mismatches ↔ xG) en expertvalidatie met RBFA-analisten.

## 2. Deadlines

| Datum | Wat |
|---|---|
| **eind nov 2026** | Literatuurstudie + **spreadsheet met alle bronnen** uit de related work (IDLab) |
| 14-18 dec 2026 | Tussentijdse presentatie, minimaal related work + dataset |
| 31 mrt 2027 | Eerste 25 bladzijden scriptie naar promotor/begeleiders |

## 3. Topics

Elke bron krijgt één hoofdtopic (code), eventueel aangevuld met een subtopic.

| Code | Topic | Onderzoeksvraag | Sectie in hoofdstuk |
|---|---|---|---|
| A | Fysieke prestatie-indicatoren per positie (afstand, HSR, sprints, topsnelheid, acc/dec, richtingsveranderingen, luchtduels) | OV1 | 2.1 |
| B | Meten, betrouwbaarheid en normalisatie (tracking/GPS/SkillCorner, validiteit, variabiliteit, per 90 / positie / balbezit, snelheidszones) | OV1 (stabiliteit) | 2.2 |
| C | Fysieke profilering en rolclustering (regel/percentiel vs. k-means, GMM, aantal profielen, interpreteerbaarheid) | OV1 | 2.3 |
| D | Matchups en mismatches (marking assignment, duels, pitch control, linie/team) | OV2 | 2.4 |
| E | Link met wedstrijduitkomst (xG, waarde van acties, fysieke output ↔ uitkomst) | OV3 | 2.5 |
| F | Jeugd, talent en ethiek (maturatie, relative age effect, talentidentificatie, expertoordeel, data van minderjarigen) | Context + ethische reflectie | 2.6 |
| X | Andere / algemeen (bv. kaders over data-analyse in sport) | - | Inleiding / 2.7 Synthese |

## 4. Bestanden in de repository

| Bestand | Inhoud |
|---|---|
| `Literatuur_studie/bronnen_literatuurstudie.xlsx` | Bronnenspreadsheet (deliverable IDLab). Tabblad *Bronnen*: rij 2 = voorbeeldrij, echte bronnen vanaf rij 3. |
| `Literatuur_studie/papers/` | PDF's van de bronnen |
| `Literatuur_studie/samenvatting_literatuurstudie.md` | Samenvatting voor het schrijven: begrippenlijst, resultaten met cijfers, bouwstenen per hoofdstuk, synthesetabel, gaps (zie §7) |
| `Scriptie/referenties.bib` | BibTeX-bibliografie, met de hand bijgehouden (geen Zotero) |
| `Scriptie/hoofdstukken/literatuurstudie.tex` | Het hoofdstuk: een sectie per topic, met notities in `%`-commentaar |
| `Scriptie/main.tex` | LaTeX `report`, `natbib` (auteur-jaar), `plainnat`, bibtex, compileren met `latexmk` |

**Kolommen van de spreadsheet (tabblad *Bronnen*, in deze volgorde):**

| # | Kolom | Toegelaten waarden / formaat |
|---|---|---|
| A | BibTeX-key | `auteur + jaar + eerste betekenisvolle titelwoord`, kleine letters (bv. `peringa2025uniform`) |
| B | Auteurs | `Achternaam, I.I., Achternaam, I.I.` |
| C | Jaar | getal |
| D | Titel | |
| E | Venue | tijdschrift + volume(nummer), pagina's of artikelnummer |
| F | Type | Journal, Conferentie, Preprint, Thesis, Boek, Rapport, Website |
| G | DOI / URL | `https://doi.org/...` |
| H | Topic | A, B, C, D, E, F of X |
| I | Subtopic | vrij |
| J | Datatype | event, tracking (optisch), GPS/LPS, fysiek (SkillCorner, ...), ... |
| K | Data & populatie | wie/wat, aantal, niveau, seizoen |
| L | Methode | |
| M | Kernresultaat | met de belangrijkste cijfers |
| N | Beperkingen | |
| O | Relevantie voor mijn werk | koppeling aan OV1-OV3, taken in het werkplan, RBFA-platform |
| P | Relevantie (1-3) | 1 = context, 2 = nuttig, 3 = kernbron |
| Q | Leesniveau | Abstract, Skim, Volledig (enkel invullen op aangeven van Jonas) |
| R | Gevonden via | Begeleider, Zoekterm, Snowball achterwaarts, Snowball voorwaarts, Andere |
| S | Geciteerd in hoofdstuk | bv. `Lit. 2.6`, `Inleiding` |
| T | Notities | o.a. snowballing-kandidaten uit de referentielijst |

## 5. Werkwijze

1. **Bron toevoegen:** BibTeX-entry in `referenties.bib`, een rij in de spreadsheet met dezelfde key, en een notitie in `%`-commentaar in de juiste sectie van `literatuurstudie.tex` (of `inleiding.tex`).
2. **Zoeken** (alleen op vraag van Jonas): startpapers van de begeleiders → Google Scholar / Scopus / Web of Science → snowballing (referentielijst + "cited by").
3. **Lezen in drie niveaus:** abstract (triage), skim (figuren, methode, conclusie), volledig (enkel kernbronnen).
4. **Schrijven per topic, niet per paper.** Elke sectie: wat is er bekend (synthese over bronnen heen) → hoe wordt het gemeten → beperkingen → **gap** en welke OV die invult. De synthesesectie bevat een tabel met technieken (sterktes, beperkingen, benodigde data) en wat meegenomen wordt naar het baselinemodel.
5. **Doel:** 40-60 bronnen in de spreadsheet, waarvan ongeveer 15 volledig gelezen.

## 6. Gevraagde output per nieuwe bron

Als Jonas een paper aanlevert, geef je terug:

1. **BibTeX-entry** met de key volgens het formaat uit §4 (titelwoorden die hoofdletters moeten houden tussen `{}`).
2. **Spreadsheetrij** als tabel met de kolommen A-T uit §4, inhoud in het Nederlands, kernresultaten met cijfers.
3. **LaTeX-notitie** in `%`-commentaar voor de juiste sectie, met `\citet{key}` en 2-5 regels: kernpunt + waarom het relevant is voor de masterproef.
4. **Relevantie in 2-4 zinnen:** hoe de bron bijdraagt aan OV1-OV3 of de werkplantaken, ook als het verband indirect is.
5. **Snowballing-kandidaten:** de 3-8 interessantste referenties uit de referentielijst, met een halve zin waarom.

Heeft de chat toegang tot de repository, pas dan zelf de drie bestanden aan, en compileer de scriptie met `latexmk` in `Scriptie/` om te controleren dat de citatie werkt.

**Altijd, zonder dat Jonas erom vraagt:**

- **Stand van zaken bijwerken.** Na elke verwerkte bron (of gewijzigd leesniveau, nieuwe snowballing-kandidaten, ...) pas je §8 van dit bestand aan: de datum, de tabel met verwerkte bronnen, de snowballing-kandidaten (verwijder ze zodra ze zelf verwerkt zijn), de onverwerkte PDF's en de openstaande vragen. Heeft de chat geen toegang tot de repository, geef dan aan het einde van je antwoord de volledige bijgewerkte §8 als blok dat Jonas kan plakken.
- **Samenvatting bijwerken.** Na elke verwerkte bron (of wanneer het leesniveau naar *Volledig* gaat) werk je `samenvatting_literatuurstudie.md` bij volgens het stappenplan in §7. Zonder toegang tot de repository geef je de nieuwe of gewijzigde stukken als blok dat Jonas kan plakken.
- **PDF's een leesbare naam geven.** Heeft een PDF in `Literatuur_studie/papers/` een onleesbare naam (bv. `joss.10223.pdf`, `1-s2.0-S146902922...pdf`, een DOI of een downloadnummer), hernoem hem dan naar een korte, beschrijvende Nederlandse titel in dezelfde stijl als de bestaande bestanden: `<Onderwerp> - <kern of invalshoek> (<type, bv. tutorial, review, studie>).pdf`, bv. `Oordeel van scouts analyseren met het Lens Model - consistentie en optimale weging van informatie (tutorial).pdf`. Gebruik `git mv` als het bestand al in git zit, hernoem het bijhorende `:Zone.Identifier`-bestand mee (of verwijder het), en vermeld de nieuwe bestandsnaam in §8. Zonder toegang tot de repository stel je de nieuwe naam voor.

## 7. Samenvatting bijhouden (stappenplan)

`Literatuur_studie/samenvatting_literatuurstudie.md` is het werkdocument waaruit Jonas de scriptie schrijft. Het is geordend op **begrip, topic en hoofdstuk**, niet per paper (dat doet de spreadsheet al). Werk het per nieuwe bron bij in deze volgorde:

1. **Bron lezen, niet de spreadsheet.** Haal begrippen en cijfers uit de PDF zelf. Neem enkel op wat de bron beweert of meet; verzin niets en rond geen cijfers anders af dan de bron.
2. **Primair vs. secundair.** Wat de bron zelf meet of beweert: `` `key` ``. Wat de bron uit een ander werk citeert: `[via key: Auteur (jaar)]`. Zo'n secundaire vermelding mag niet zo in de scriptie geciteerd worden; het oorspronkelijke werk is een snowballing-kandidaat (zet het ook in §8).
3. **§1 Begrippenlijst.** Voeg nieuwe vaktermen toe (Nederlandse term / *Engelse term*, korte definitie in eigen woorden, key, topic). Bestaat het begrip al, vul dan de definitie aan of voeg de key toe; let op tegenstrijdige definities tussen bronnen en vermeld ze allebei.
4. **§2 Resultaten met cijfers.** Zet de kernresultaten onder het juiste topic (A-F, X): steekproef, effectgroottes, BI's, p-waarden. Bij een studie met veel parameters: een kleine tabel. Haal "*Nog geen bronnen*" weg zodra een topic een bron heeft.
5. **§3 Bouwstenen per hoofdstuk.** Vertaal de bron naar bruikbare argumenten voor een specifiek deel van de scriptie (Inleiding, Lit. 2.1-2.7, Methodologie/Taak 3, OV2, Evaluatie/Taak 7, Ethiek). Formuleer als stelling + key, zodat Jonas er direct een zin met `\citet{}` van kan maken.
6. **§4 Synthesetabel.** Nieuwe techniek, metriek of tool? Voeg een rij toe (sterktes, beperkingen, benodigde data, bron). Deze tabel is de basis voor de synthesesectie (Lit. 2.7) en het verifieerbare resultaat van Taak 1.
7. **§5 Gaps.** Pas aan wat nog ontbreekt: vult de bron een gap, haal die weg; legt ze een nieuwe gap bloot, voeg die toe met de OV die ze invult.
8. **Kop bijwerken.** Datum "Laatst bijgewerkt" en de lijst met verwerkte bronnen bovenaan.
9. **Controle.** Elke key in de samenvatting bestaat in `referenties.bib`; geen enkele bewering zonder key.

Bronnen met leesniveau *Abstract* krijgen een regel in §2, eventueel §5, en **wel** de belangrijke begrippen in §1 (uit de PDF gehaald); bouwstenen (§3) en de synthesetabel (§4) pas vanaf *Skim*.

**Begrippenlijst:** voeg enkel begrippen toe uit de bron die je op dat moment verwerkt, en enkel als ze nuttig zijn voor het eigenlijke project (fysieke profielen, mismatches, meten/normalisatie, koppeling met uitkomsten, evaluatie). Algemene begrippen uit de talent- en beslissingspsychologie horen er niet in. Jonas schrapt soms zelf begrippen die hij niet nuttig vindt: voeg een begrip dat uit de lijst verdwenen is niet opnieuw toe.

## 8. Stand van zaken (27 november 2026)

> Deze sectie wordt na elke wijziging automatisch bijgewerkt (zie §6).

**Verwerkt (in bib, spreadsheet en LaTeX-notities):**

| Key | Bron | Topic | Leesniveau | Kern |
|---|---|---|---|---|
| `peringa2025uniform` | Peringa, Niessen, Meijer & den Hartigh (2025). A uniform approach for advancing athlete assessment: A tutorial on the Lens Model. *Psychology of Sport & Exercise*, 76, 102732. | F | Volledig | 18 scouts beoordelen 50 centrale verdedigers op 4 cues; het lineaire model van elke scout is accurater dan de scout zelf (ra = .62, rm = .68, Re = .77). Argument voor consistente, gewogen profielscores; subjectzijde bruikbaar voor de expertvalidatie (Taak 7). |
| `houtmeyers2021managing` | Houtmeyers, Jaspers & Figueiredo (2021). Managing the Training Process in Elite Sports: From Descriptive to Prescriptive Data Analytics. *IJSPP*, 16(11), 1719-1723. | X | Volledig | Framework descriptive → diagnostic → predictive → prescriptive; topsport is "data-informed". Positionering: profielen = descriptive, mismatches ↔ kansen = diagnostic/predictive, matchupadvies = richting prescriptive. Co-auteur Arne Jaspers is begeleider. |
| `oonk2026databallpy` | Oonk, Grob & Kempe (2026). DataBallPy: Load, synchronize, and Analyse your Soccer Data. *Journal of Open Source Software*, 11(120), 10223. PDF: `Python-pakket DataBallPy - event- en trackingdata inladen, synchroniseren en analyseren (software).pdf` | B | Volledig | Open-source Python-pakket: event + tracking in één Game-object, synchronisatie via Needleman-Wunsch. Naïeve alignering wijkt 1.82 (±4.06) s af; met synchronisatie daalt de Brier loss van xG van 0.096 naar 0.082. Bevat afstand in snelheids-/acc-zones, pressure, pitch control, xT. Tooling voor de pijplijn (Taak 3, OV3), bouwstenen voor OV2. |
| `bergkamp2019methodological` | Bergkamp, Niessen, den Hartigh, Frencken & Meijer (2019). Methodological Issues in Soccer Talent Identification Research. *Sports Medicine*, 49, 1317-1335. PDF: `Methodologie van talentidentificatie in het voetbal - criterium, fidelity, range restriction en base rate (position statement).pdf` | F | Skim | Vier methodologische problemen (selectiepsychologie): criterium = prestatieniveau i.p.v. individuele prestatie; low-fidelity signs vs. high-fidelity samples; range restriction in voorgeselecteerde groepen; base rate/utiliteit (r = .4 → success ratio 5.3%, 73.5% geschikte spelers gemist). Onderbouwt profielen uit wedstrijddata, waarschuwt voor kleine verschillen bij RBFA-spelers, richtlijn voor uitkomstmaat OV3. |
| `bareli2024feudal` | Bar-Eli, Lidor, Lath & Schorer (2024). The feudal glove of talent-selection decisions in sport – Strengthening the link between subjective and objective assessments. *Asian Journal of Sport and Exercise Psychology*, 4, 1-6. PDF: `Talentselectie - subjectief oordeel (coach's eye), objectieve testen en big data combineren (conceptueel artikel).pdf` | F | Abstract | Conceptueel: talentselectie combineert het subjectieve coach's eye en objectieve testformules; pleidooi voor big data / sport analytics als derde aanpak. Relevantie 1 (context). |
| `barraclough2022methodological` | Barraclough, Till, Kerr & Emmonds (2022). Methodological Approaches to Talent Identification in Team Sports: A Narrative Review. *Sports*, 10, 81. PDF: `Talentidentificatie in teamsporten - tijdspanne, multidisciplinaire variabelen en fidelity van onderzoeksdesigns (narrative review).pdf` | F | Abstract | Narrative review: drie aandachtspunten voor TID-onderzoek (tijdspanne, mono- vs. multidisciplinair, fidelity); pleit voor longitudinale, multidisciplinaire, ecologisch valide designs. Bevestigt Bergkamp et al. (2019). Relevantie 2. |
| `bennett2026talent` | Bennett, McCalman, Goddard, Williams & Fransen (2026). Talent identification and development recommendations in youth sports: a real-time Delphi study. *Journal of Applied Sport Psychology* (online 5 maart 2026). PDF: `Aanbevelingen talentidentificatie en -ontwikkeling - consensus en haalbaarheid volgens experts (real-time Delphi-studie).pdf` | F | *nog in te vullen* | Real-time Delphi met 20 experts over 15 aanbevelingen. Objectieve data als aanvulling: 90% eens, maar data moet betekenisvol zijn ("te veel ruis"). Indicatoren longitudinaal opvolgen: 75% eens, 10% haalbaar. Argument voor interpreteerbare profielen en een automatische pijplijn; Delphi als optie voor de expertvalidatie (Taak 7). |
| `billen2022careers` | Billen, Dossche, Vercauteren & Waelkens (2022). Careers of young Red Devils: an exploratory statistical analysis. Onuitgegeven bachelorproef, KU Leuven. PDF: `Loopbanen van jonge Rode Duivels - relative age effect en jeugdtraject naar de A-ploeg (bachelorproef).pdf` | F | Skim | RBFA-data (29.631 datapunten): RAE in U15-U18, niet in U19, U21 en de Rode Duivels; geen effect van positie. U21 (OR = 4.55) en Olympische ploeg (OR = 6.89) voorspellen een selectie bij de Rode Duivels. Niet peer-reviewed, statistiek discutabel; voorzichtig citeren. Data via Arne Jaspers. |
| `denhartigh2016dynamic` | Den Hartigh, Van Dijk, Steenbeek & Van Geert (2016). A Dynamic Network Model to Explain the Development of Excellent Human Performance. *Frontiers in Psychology*, 7, 532. PDF: `Ontwikkeling van excellentie - dynamisch netwerkmodel van interagerende factoren en scheve prestatieverdelingen (theorie en simulatie).pdf` | F | Abstract | Theorie + simulatie: excellentie ontstaat uit interacties tussen factoren in een individueel netwerk. Vroeg ↔ eindniveau r ≈ 0 bij de start, ≈ 0.5 rond 12 jaar; gelijke niveaus via verschillende trajecten. Doelpunten van 272 Nederlandse internationals rechtsscheef (power law p = 1.18). Context voor jeugd, interpretatie van stabiliteit (OV1) en ethiek. Relevantie 2. |
| `johnston2025take` | Johnston & Baker (2025). Take Your Pick! Examining Decision-Making Behavior in Athlete Selection: A Methodological Description and Pilot Study. *Sport, Exercise, and Performance Psychology*, 14(1), 175-192 (Online First 6 juni 2024). PDF: `Selectiebeslissingen van coaches onderzoeken - Take Your Pick, naturalness bias en methodologische uitdagingen (pilotstudie).pdf` | F | Abstract | Online tool om beslissingsgedrag van selectors te testen; pilot met 18 rugby league-coaches, 15 gesimuleerde profielen, naturalness bias (natural vs. striver). Randomisatie mislukt, enkel beschrijvend. Coaches vonden foto, positie, leeftijd, lengte en gewicht het belangrijkst en misten wedstrijdstatistieken. Lessen over scenario, framing en informatie: context voor de expertvalidatie (Taak 7). Relevantie 2. |
| `kite2025player` | Kite, Johnston & Baker (2025). What Do We Know About Player Selection in Academy Soccer? A Narrative Review. *Journal of Expertise*, 8(2-3), 150-178. PDF: `Spelersselectie in jeugdacademies - fysieke testen, maturatie, subjectief oordeel en bias (narrative review).pdf` | F | Abstract | Narrative review: fysieke predictoren inconsistent (antropometrie 4 studies wel, 12 niet onderscheidend); coaches wegen psychologisch en technisch-tactisch hoger dan fysiek; maturatiebias; holistisch model 88% selectieaccuraatheid vs. 71% subjectief [secundair]. Toekomstpistes: compensatiefenomeen en weging van attributen (relevant voor OV2), survivorship bias en halo-effect, gevolgen van deselectie. Gevonden via begeleider. Relevantie 2. |
| `lundberg2026evidence` | Lundberg, Lind, Baker, Lundkvist, Lascu, Johnston, Côté, Fransen & Ivarsson (2026). Evidence-Based Insights for the Development and Talent Promotion of Young Athletes in a National Sports Context. *Sports Medicine* (leading article, aanvaard 30 augustus 2026; volume nog niet bekend). PDF: `Ontwikkeling en talentpromotie van jonge atleten - vroege selectie vs. lange termijn, evidence-based aanbevelingen (leading article).pdf` | F | Abstract | Perspectief (Zweden): vroege talentpromotie vs. duurzame ontwikkeling. Topjuniors en topsenioren zijn grotendeels verschillende populaties; trajecten zijn niet-lineair; RAE en maturiteitsbias bij vroege selectie; multidimensionale selectie voorspelt beter maar nog zwak [meeste cijfers secundair]. 8 aanbevelingen voor federaties. Gevonden via begeleider. Relevantie 1. |

**Snowballing-kandidaten (nog niet gelezen, gegevens uit de referentielijsten):**
- Uit Peringa et al.: Bergkamp et al. (2022, *Eur J Sport Sci* en *Psychol Sport Exerc*), Sieghartsleitner et al. (2019), Lüdin et al. (2023), Johnston et al. (2018), Den Hartigh et al. (2018).
- Uit Houtmeyers et al.: Delen & Ram (2018), Schelling & Robertson (2020), Thornton et al. (2019), Ryan et al. (2020), Shmueli (2010), Grove et al. (2000), Gamble et al. (2020), Rommers et al. (2020).
- Uit Oonk et al. (2026): Oonk, Grob & Kempe (2025, MathSports), Anzer & Bauer (2021), Jerome et al. (2024), Linke et al. (2020), Fernandez & Bornn (2018), Herold et al. (2022), Bassek et al. (2025), Raabe et al. (2022, Floodlight).
- Uit Bergkamp et al. (2019): Vaeyens et al. (2008) en Deprez et al. (2015) (beide met promotor Matthieu Lenoir), Vaeyens et al. (2006, Ghent youth soccer project), Wilson et al. (2017), Pappalardo et al. (2018, PlayeRank), Murr et al. (2018), Sackett & Yang (2000).
- Uit Bar-Eli et al. (2024): Williams & Reilly (2000), Lath et al. (2021, coach's eye), Höner et al. (2021), Leyhr et al. (2021, relative age bias), Johnston & Baker (2020). Sieghartsleitner et al. (2019) staat ook al bij Peringa.
- Uit Barraclough et al. (2022): Woods et al. (2015, fysieke en technische matchprofielen gedraft vs. niet-gedraft), Kelly & Williams (2020, fysieke kenmerken en TID in jeugdvoetbal), Williams, Ford & Drust (2020), Saward et al. (2020, longitudinale fysieke ontwikkeling), Peña-González et al. (2022, maturiteit en fysieke prestatie). Williams & Reilly (2000) en Bergkamp et al. (2019) komen ook hier terug.
- Uit Bennett et al. (2026): McCalman et al. (2022, skill-assessments in jeugdvoetbal), Beiderbeck et al. (2021, Delphi-methodologie), Millington & Millington (2015, big data in sport), Faber et al. (2022), Hauser et al. (2024). Till & Baker (2020) komt ook bij Bar-Eli et al. terug.
- Uit Billen et al. (2022): Herrebrøden & Bjørndal (2022, ervaring bij U17/U19/U21 als voorspeller van succes bij de senioren), Helsen et al. (1998, 2005, 2012, RAE in het voetbal), Romann & Fuchslocher (2013, RAE per positie), Meylan et al. (2010, maturiteit en fysieke kenmerken). Vaeyens et al. (2006) staat ook bij Bergkamp et al.
- Uit Den Hartigh et al. (2016): Abbott et al. (2005) en Abbott & Collins (2004, niet-lineaire TID/TD), Phillips et al. (2010, expert performance en dynamiek van talentontwikkeling), Simonton (2001, talentontwikkeling als multiplicatief, dynamisch proces), Elferink-Gemser et al. (2011, idiosyncratische trajecten in het Nederlandse longitudinale project), Gulbin et al. (2013, ontwikkelingspatronen van elite-atleten), Den Hartigh (2015, doctoraat met fits voor tennis en voetbal), Van Yperen (2009, psychologische voorspellers van succes in het profvoetbal). Vaeyens et al. (2008) komt ook hier terug.
- Uit Johnston & Baker (2025): Lath et al. (2020, talentselectie en heuristieken), Roberts et al. (2019, coach knowledge in TID, meta-synthese) en Roberts et al. (2021, gut instinct van coaches), Roy et al. (2024, naturalness bias in sport), Christensen (2009, 'eye for talent' bij topvoetbalcoaches), Bradbury & Forsyth (2012, selectiepraktijken van coaches). Den Hartigh et al. (2018, *Eur J Sport Sci*, selectieprocedures) en Johnston et al. (2018, systematic review TID) staan ook bij Peringa et al.
- Uit Kite et al. (2025): Dugdale et al. (2021, attributen van geselecteerde, gedeselecteerde en opnieuw geselecteerde spelers), Woods et al. (2016, compensatie van zwakke punten), Huijgen et al. (2014, multidimensionale kenmerken geselecteerd vs. gedeselecteerd), Baker, Johnston & Wattie (2022, survival vs. attraction advantages), Cumming et al. (2017, bio-banding), Towlson & Barrett (2024, technische, fysieke en maturiteitskenmerken bij een nationale selectie). Sieghartsleitner et al. (2019) en Bergkamp, Frencken et al. (2022, hoe scouts talent identificeren) staan ook bij Peringa et al.
- Uit Lundberg et al. (2026): Güllich et al. (2023, topjuniors en topsenioren als twee populaties), Barth et al. (2024, meta-analyse junior- vs. seniorprestatie), Brustio et al. (2024, Europees voetbal: van jeugd naar senior en geboortedata), Verbeek et al. (2025, de typische weg naar de top is atypisch), Güllich (2014, selectie en deselectie in het Duitse voetbal), Lüdin et al. (2022, player-labelling tegen maturatiebias). Den Hartigh et al. (2018) staat ook bij Peringa et al. en Johnston & Baker (2025).

**Samenvatting** (`samenvatting_literatuurstudie.md`): bijgewerkt voor alle 12 verwerkte bronnen.

**Nog niet verwerkt:** geen PDF's meer in `Literatuur_studie/papers/` die nog niet in de spreadsheet of bib zitten.

**Openstaande vragen:**
- De faculteit heeft mogelijk een verplicht LaTeX-sjabloon (na te vragen).
- De topics A, C, D en E bevatten nog geen inhoudelijke bronnen.
- `oonk2026databallpy`: kolom *Gevonden via* is nog leeg (hoe gevonden?). Na te gaan: kan DataBallPy SkillCorner-data inladen, bv. via Kloppy?
- `bergkamp2019methodological`: kolom *Gevonden via* is nog leeg. Volume 49 en pagina's staan in de PDF, het nummer van het tijdschriftnummer niet (daarom niet in de bib).
- `bareli2024feudal`, `barraclough2022methodological`, `bennett2026talent` en `billen2022careers`: kolom *Gevonden via* is nog leeg (voor `billen2022careers` waarschijnlijk *Begeleider*, want Arne Jaspers leverde de data aan).
- `bennett2026talent`: leesniveau nog niet opgegeven (kolom *Leesniveau* leeg).
- Begripsafbakening: volgens Williams & Reilly (2000, via Bar-Eli et al.) betekent *talent detection* het ontdekken van spelers die nog in geen enkel programma zitten, en *talent identification* het herkennen van potentieel bij spelers die al in een programma zitten. De titel van de masterproef gebruikt "talent detection", maar de RBFA-context past eerder bij identification/selection. Bespreken met de begeleiders, of verantwoorden in de inleiding.
