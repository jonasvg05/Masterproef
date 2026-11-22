# Context: herwerking werkplan masterproef

> **Instructie voor Claude.** Je helpt een masterstudent (Jonas Van Goethem, Industrieel Ingenieur Informatica, UGent) om het werkplan van zijn masterproef te herwerken. De **eerste versie werd afgekeurd** door de opleidingscommissie. Jonas heeft intussen een **tweede versie (Word)** gemaakt, die in §5 samengevat staat. Help hem die versie volledig in orde te brengen met de feedback (§1) en de officiële richtlijnen (§6). Schrijf in het **Nederlands** en volg de secties van het sjabloon. Vraag naar ontbrekende informatie in plaats van datums, data of afspraken te verzinnen. Behoud wat goed is aan versie 2 en stel gerichte aanpassingen voor in plaats van alles te herschrijven.
>
> Vandaag is het **21 november 2026**.

---

## 1. Feedback van de opleidingscommissie op versie 1

> Het werkplan is niet goedgekeurd door de opleidingscommissie. Eén van de doelstellingen van een werkplan is om het onderwerp beter af te bakenen, en het masterproefvoorstel te vertalen naar een concretere opdracht. Volgende opmerkingen werden geformuleerd:
>
> - Het kan niet dat er nog moet gekozen worden op het einde van het semester tussen twee doelstellingen; terwijl er al de helft van het totaal aantal studiepunten gepland is.
> - Het is net de bedoeling van een werkplan om een deadline te hebben waartegen zulke strategische beslissingen moeten genomen worden.

**Waarop dit sloeg in versie 1:** de doelstelling liet een keuze open tussen twee RBFA-projecten: (1) fysieke spelersprofielen + mismatches en (2) het meten van defensief gedrag (o.a. het omkeren van het model van Lore Pintelon om het afsluiten van passlijnen te evalueren). Taak 3 ("Projectkeuze en baselinemodel", deadline 18 december 2026) maakte die keuze pas op het einde van semester 1, terwijl semester 1 al 9 van de 18 SP bevat.

**Al opgelost:** Jonas heeft gekozen voor **project 1: fysieke profielen en mismatches**. Project 2 (defensief gedrag) valt volledig weg. Medestudent Matteo De Meersman, met dezelfde titel, werkt aan een ander deel. De afbakening met Matteo is geregeld en hoeft **niet** in het werkplan.

**Geest van de feedback (ook voor versie 2):** de commissie wil een **afgebakende, concrete opdracht**, waarin strategische beslissingen **een vaste datum** krijgen in de planning en niet open blijven.

---

## 2. Student en masterproef

| | |
|---|---|
| **Student** | Jonas Van Goethem |
| **Opleiding** | Industrieel Ingenieur Informatica (Campus Schoonmeersen, UGent) |
| **Titel** | Talent detection in youth soccer data of RBFA (voorstel 50295) |
| **Bedrijf / onderzoeksgroep** | The Royal Belgian Football Association / IDLab-IMPACT |
| **Promotoren** | Steven Verstockt, Matthieu Lenoir |
| **Begeleiders** | Maarten Slembrouck, Laurens Gilson, Arne Jaspers |
| **Studiepunten** | Semester 1: 15 SP vakken + 9 SP masterproef · Semester 2: 21 SP vakken + 9 SP masterproef |
| **Masterproef totaal** | 18 SP (1 SP = 30 u → richtlijn 540 u) |
| **Zittijd** | 1e zit, verdediging 23-25 juni 2027 |
| **Contactmomenten** | Fysiek in het RBFA-kantoor in Tubize, om de 3 à 4 weken. Tussendoor per e-mail aan Laurens Gilson. |

---

## 3. De opdracht (gekozen project)

### 3.1 RBFA "Project 1: Physical Profiles" (slides 33-34, presentatie RBFA × UGent)

RBFA heeft een platform met spelersprofielen. Voorbeeld: een U17-back met de score per rolprofiel, een radar met metrics op schaal 1-20 tegenover dezelfde positie, competitie en seizoen (10.5 = gemiddelde, minstens 180 min), en sterktes en zwaktes per submetric. Kleine samples worden naar het gemiddelde geregresseerd.

**A. Fysieke profielen.** Een model dat fysieke profielen identificeert op basis van metrics uit event- en fysieke data: volume/intensiteit, hoge topsnelheid, snelle richtingsveranderingen, snelle acceleraties, luchtsterk, andere. SkillCorner is een goede bron voor fysieke metrics.

**B. Mismatches.** Een model dat gevaarlijke matchups signaleert, positief en negatief, op het niveau van een 1v1, een linie (unit) en het team. Voorbeelden uit de slides:
- Welke van onze flankspelers zetten we tegen Digne (Frankrijk)?
- Kunnen we de fysieke kracht van Senegal op het middenveld aan?
- Welke van onze backs is het meest geschikt tegen Yamal (Spanje)?

→ *"We want to identify mismatches which can help us to win games!"*

### 3.2 Oorspronkelijk masterproefvoorstel 50295 (ter info)

Het voorstel was breder: met AI/ML de parameters vinden die bijdragen aan vroege talentidentificatie (selecties en speeltijden in de nationale jeugdploegen, SciSport-data, event- en trackingdata). Het gekozen RBFA-project is een concrete invulling daarvan.

**Aandachtspunt:** de titel spreekt over *talent detection in youth soccer*, terwijl de inhoud nu fysieke profielen en mismatches is, met voorbeelden uit het A-elftal. Overweeg (in overleg met de promotor) een titel die de inhoud dekt, en baken af **op welke ploegen of competities** het werk gebeurt (nationale jeugdploegen, A-ploeg, tegenstanders?).

---

## 4. Versie 1 (afgekeurd) in het kort

Zelfde structuur en taken als versie 2 (§5), behalve:
- de doelstelling beschreef beide projecten, "waarvan er één gekozen wordt",
- Taak 2 leverde "eerste beschrijvende analyses voor beide projecten" als basis voor de projectkeuze,
- Taak 3 heette "Projectkeuze en baselinemodel", met een gemotiveerde projectkeuze op 22 november 2026,
- er waren geen onderzoeksvragen.

---

## 5. Versie 2 (huidig Word-bestand): samenvatting

**Bestaande situatie en probleemstelling:** data in het voetbal (Brentford, FC Midtjylland, Liverpool), de evolutie van descriptive naar predictive en prescriptive analytics (Charles Reep). De RBFA heeft een eigen datateam en stapt af van traditionele scouts. Ruwe event-, tracking- en fysieke data zijn moeilijk te interpreteren en te vergelijken. Objectieve metrieken voor het fysieke profiel en voor fysieke mismatches ontbreken.

**Doelstelling:** datamodellen en metrieken voor fysieke spelersprofielen en het detecteren van fysieke mismatches (duel, linie, team), op basis van event-, tracking- en fysieke data. De oplossing moet praktisch bruikbaar en implementeerbaar zijn in de platformen van de RBFA (Google Cloud).

**Onderzoeksvragen:**
1. Welke fysieke profielen kunnen op basis van event-, tracking- en fysieke data objectief onderscheiden worden, en hoe stabiel is het profiel van een speler over verschillende wedstrijden en seizoenen?
2. Hoe kan een fysieke mismatch tussen tegenstanders gedefinieerd en gemeten worden op het niveau van een individueel duel, een linie en het volledige team?
3. In welke mate hangen de gesignaleerde mismatches samen met wat er op het veld gebeurt, zoals het creëren of toestaan van kansen?

**Taken:**

| Taak | Duur | Deadline | Inhoud | Verifieerbare resultaten |
|---|---|---|---|---|
| 1. Literatuurstudie en verkenning van voetbaldata | 6 w | 1 nov 2026 | Literatuur over fysieke data, fysieke profilering, mismatches | Eerste versie van de literatuurstudie in de scriptie. Overzicht van technieken met sterktes, beperkingen en benodigde data |
| 2. Verkenning en voorbereiding van de RBFA-data | 2 w | 15 nov 2026 | Event-, tracking- en fysieke data verkennen (competities, seizoenen, leeftijden, formaat). Pipeline in Google Cloud | Data-overzicht + werkende pipeline. Beschrijvende analyses (afstanden, sprints, snelheden, acceleraties per positie). 15 nov: datahoofdstuk in de scriptie |
| 3. Fysieke metrieken en baselinemodel | 5 w | 18 dec 2026 | Metrieken vastleggen met de RBFA. Normalisatie per minuut en per positie. Clustering (k-means, GMM) | 4 dec: lijst van metrieken met definities, afgestemd met de RBFA. 18 dec: baselinecode in Git. 18 dec: literatuur aangevuld + hoofdstuk methodologie baseline |
| 4. Tussentijdse presentatie | 2 w | 14-18 dec 2026 | Probleemstelling, literatuur, data, metrieken, eerste profielen, planning S2 | 11 dec: slides naar de begeleiders. Presentatie in de inhaalweek. Feedback verwerkt in Taak 5 |
| 5. Ontwikkeling van het geavanceerde model | 6 w | 21 mrt 2027 | Trackingdata: richtingsveranderingen, herhaalde sprints, explosiviteit. Matchupmodel (wie staat tegenover wie) met mismatches per duel, linie en team | 28 feb: demo van de trackingkenmerken met visualisaties. 21 mrt: volledig model op alle seizoenen + vergelijking met de baseline. 21 mrt: hoofdstuk methodologie |
| 6. Scriptie: eerste 25 bladzijden | 3 w | 31 mrt 2027 | Inleiding, literatuur, data, methodologie baseline | 31 mrt: 25 p. doorgestuurd. 1 apr: Plato-gegevens. 18 apr: feedback verwerkt |
| 7. Evaluatie en validatie | 4 w | 25 apr 2027 | Stabiliteitstest (correlatie per speler over seizoenshelften, silhouette score), voorspellende test (mismatches ↔ xG), expertvalidatie met RBFA-analisten op video | 11 apr: testresultaten in tabellen en grafieken. 25 apr: expertvalidatie + evaluatiehoofdstuk |
| 8. Integratie in het RBFA-platform | 3 w | 9 mei 2027 | Automatische herberekening in Google Cloud, tabellen voor de dashboards en scouting/pre-match. Unit-testen | 2 mei: demo van een automatische verwerking van een nieuwe speeldag. 9 mei: unit-testen slagen + documentatie |
| 9. Scriptie afwerken + examen | 7 w | 23 jun 2027 | Hoofdstukken model, evaluatie, integratie, conclusie, abstract. Presentatie + demo | 13 mei: 95%-versie. 20 mei: indienen + abstract. 11 jun: proefpresentatie. 23-25 jun: verdediging + logboek |

**Contactmomenten:** zie §2.

**Gantt chart:** ongewijzigd ten opzichte van versie 1. Week 1 = 21/09/26 t.e.m. week 13 = 14/12/26 (T1 w1-6, T2 w7-8, T3 w9-13, T4 w12-13), daarna Kerstvakantie en examens, semester 2 vanaf 8/02/27 (T5 w1-6, T6 w6-paas w1, T7 paas w1-w9, T8 w9-w11, T9 w12-w18).

---

## 6. Officiële richtlijnen werkplan (DoeJaar)

- Vertrek van het officiële sjabloon en dien in als **.pdf op Plato**.
- **Opsplitsing per semester:** SP voor andere vakken + verdeling van de 18 SP.
- Grondige **bestaande situatie en probleemstelling** en **doelstelling**.
- Concrete **taken** met een **aantal weken** en een **deadline**.
- Per taak **resultaten** (eventueel in iteraties), met **hoe het behalen geverifieerd kan worden**. Bijvoorbeeld "op datum D: hoofdstuk X, Y, Z doorgestuurd naar promotor", "op datum D: demonstratie van stappen X, Y, Z aan het bedrijf", "platform slaagt voor alle unit-testen uit week 1". Dus **niet** "literatuurstudie afgewerkt" of "functionaliteit X af".
- Begrijpbaar voor buitenstaanders, voldoende details.
- Tijd voor **literatuurstudie/technologieverkenning**, met duidelijk welke topics.
- Bij **testen**: welke testen.
- De scriptie schrijf je **niet in de laatste twee weken**.
- **Presentaties** en hun voorbereiding in de planning.
- Vakantie, examens en testen van andere vakken worden **niet** vermeld.
- **Tussentijdse communicatie** vermelden.
- **Gantt chart** toevoegen.
- Bespreken met de promotor(en)/begeleider(s) **vóór** het indienen.

---

## 7. Vaste deadlines en verplichtingen (1e zit)

| Datum | Mijlpaal | Bron |
|---|---|---|
| eind nov 2026 | Literatuurstudie + **spreadsheet met alle bronnen** uit de related work | IDLab |
| 14-18 dec 2026 | Tussentijdse presentatie (verplicht), minimaal related work + dataset | Faculteit / IDLab |
| jan 2027 | **1e code review** (private GitHub-repo gedeeld met de begeleiders) | IDLab |
| 4 mrt 2027 | **Bedrijfsbezoek** (verplicht) | Faculteit |
| mrt 2027 | **2e code review** | IDLab |
| mrt/apr 2027 (rond Pasen) | **Presentatie van een bijna-finale versie** aan de onderzoeksgroep | IDLab |
| 31 mrt 2027 | Eerste deel scriptie (25 p.) voor nalezen *(te verifiëren)* | Faculteit |
| 1 apr 2027 | Administratieve gegevens in Plato *(te verifiëren)* | Faculteit |
| ± 6 mei 2027 | Korte abstract op Plato, twee weken vóór het indienen | Faculteit |
| 13 mei 2027 | Scriptie 95% aan de promotoren/begeleiders | Faculteit |
| 20 mei 2027 (23:59) | Scriptie indienen op Plato + papieren versie per jurylid | Faculteit |
| 23-25 jun 2027 | Masterproefexamen: 15 min presentatie + 30 min vragen. Logboek en presentatie op Plato | Faculteit |

**Communicatieverplichtingen IDLab-IMPACT/faculteit:**
- **Wekelijks** een logboek of e-mailrapportering aan **alle promotoren en begeleiders**: datum, gedetailleerde omschrijving van de activiteiten, resultaten, problemen/vragen, planning voor de komende week. Dit is een absolute voorwaarde om te verdedigen.
- **Om de 2 weken** een update in het Teams-kanaal "MP 26-27 – Jonas Van Goethem".
- Na elke meeting: notities met actiepunten in de Teams-tab *Notes* en de slides in de tab *Files*.
- 1 à 2 stakeholdermeetings met de RBFA in semester 1.

**Verwachtingen van IDLab:** een creatieve oplossing (niet enkel state of the art), kritische zin, autonomie, en vooral **praktisch gebruik**: een tastbare demo die met de stakeholders getest wordt. De code moet voldoen aan de code-review-checklist: Engels, gescheiden stappen (loading, preprocessing, modelling, evaluatie), configuratiebestanden, README's, tests, reproduceerbaarheid, nette git-historiek.

**Ethiek/data:** er is een NDA. De data mag enkel voor de masterproef gebruikt worden. Bij data van (minderjarige) jeugdspelers hoort een korte ethische reflectie, die ook een evaluatiecriterium is.

---

## 8. Resterende werkpunten in versie 2 (na te kijken en op te lossen)

1. **Strategische beslissingen zonder deadline.** De projectkeuze is gemaakt, maar de feedback vraagt in het algemeen dat strategische keuzes een datum krijgen. Voeg expliciete beslismomenten toe, bijvoorbeeld:
   - de **scope van de data**: welke ploegen, competities, leeftijdscategorieën en seizoenen (vóór/bij 4 dec samen met de metrieken),
   - de **keuze van de profileringsmethode** na de baseline (bv. clustering tegenover regel- of percentielgebaseerde profielen, het aantal profielen), op een datum begin semester 2,
   - de **definitie van een mismatch** en het niveau (duel/linie/team), vastgelegd vóór de bouw van het matchupmodel,
   - een **terugvaloptie** als trackingdata niet of slechts beperkt beschikbaar is (bv. alleen fysieke en eventdata), met een datum waarop dat beslist wordt.
2. **Taken en deadlines die al voorbij zijn.** Taak 1 (1 nov) en Taak 2 (15 nov) liggen in het verleden, en de gemotiveerde keuze stond in versie 1 op 22 nov. Laat de planning de werkelijkheid weerspiegelen: wat is effectief opgeleverd, en wat schuift op? *Vraag Jonas naar de huidige stand.*
3. **IDLab-deadline ontbreekt:** literatuurstudie + spreadsheet met bronnen tegen eind november.
4. **Taak 5 is zwaar en het matchupmodel heeft geen eigen deliverable.** Ze combineert de verfijnde profielen (tracking) met het volledige matchupmodel in 6 weken, en de tussentijdse demo (28 feb) gaat alleen over de trackingkenmerken. Splits ze bij voorkeur in twee taken, of geef het matchupmodel een eigen verifieerbaar resultaat met een datum (bv. "op datum D: mismatchrapport voor wedstrijd X gedemonstreerd aan het datateam").
5. **Ontbrekende presentaties en verplichtingen in de planning:** de IDLab-presentatie rond Pasen, de code reviews in januari en maart, het bedrijfsbezoek op 4 maart, de stakeholdermeetings met de RBFA.
6. **Niet-verifieerbaar resultaat in Taak 4:** "feedback verzameld en verwerkt" krijgt beter een datum en een vorm (bv. "op 8 feb 2027: verslag van de feedback met actiepunten in Teams en aangepaste planning naar de begeleiders").
7. **Onvolledige tussentijdse communicatie:** nu staan er alleen contactmomenten om de 3 à 4 weken + e-mail aan Laurens. Vul aan met de wekelijkse rapportering aan alle promotoren en begeleiders, de tweewekelijkse Teams-update en de meetingnotities in Teams.
8. **Gantt chart:** werk hem bij volgens de nieuwe planning (bij gesplitste of verschoven taken). De rijen "Kerstvakantie", "Examenperiode" en "Paasvakantie" botsen met de richtlijn dat vakanties en examens niet vermeld worden. Overweeg die weg te laten of neutraal te houden.
9. **Titel en afbakening:** zie §3.2. Kijk na of de titel nog klopt en vermeld op welke data of ploegen het werk focust.
10. **Concrete literatuurtopics in Taak 1:** noem expliciet welke topics behandeld worden (bv. fysieke prestatie-indicatoren en het meten ervan, SkillCorner-metrics, player role/profile clustering, matchup- en mismatchanalyse, tracking-datamodellen, normalisatie naar speeltijd en positie).
11. **Consistentie in Taak 7:** "mismatches leiden tot meer kansen (xG) in die zone" vraagt een concrete testopzet (welke wedstrijden, welke statistische test).

---

## 9. Nog te vragen aan Jonas als het nodig is

1. Wat is effectief al gedaan en opgeleverd (Taak 1 en 2, metrieken, pipeline)?
2. Welke data is al beschikbaar: SkillCorner, tracking, event, en voor welke ploegen, competities en seizoenen?
3. Wat is de deadline om het werkplan opnieuw in te dienen?
4. Moet de titel aangepast worden (in overleg met de promotor)?
5. Zijn de datums van de contactmomenten in Tubize al vastgelegd?
