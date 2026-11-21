# Logboek

Het logboek of de wekelijkse e-mailrapportering is een **absolute voorwaarde om de masterproef te mogen verdedigen** ([DoeJaar: logboek](https://masterproef.tiwi.ugent.be/DoeJaar/logboek/)). Deze map houdt alles bij in het gevraagde formaat.

## Wat ze vragen

| Wie | Wat | Hoe vaak | Hoe in deze map |
|---|---|---|---|
| Faculteit | Logboek per week: datum, gedetailleerde omschrijving van de activiteiten, resultaten, problemen/vragen/opmerkingen, planning voor de komende week | wekelijks, aan alle promotoren en begeleiders | `weken/JJJJ-Www.md`, mail met `log.py mail` |
| Faculteit | Logboek als duidelijke .pdf op Plato | bij het indienen van de scriptie / na de verdediging | `log.py export` → `export/logboek.pdf` |
| Faculteit | Richtlijn: 540 u werk | totaal | urentabel per week, `log.py uren` |
| IDLab-IMPACT | Update in het Teams-kanaal | om de 2 weken | `log.py teams` |
| IDLab-IMPACT | Meetingnotities met actiepunten (tab *Notes*) + presentatie (tab *Files*) | na elke meeting | `meetings/`, `log.py meeting` |

## Gebruik

```bash
# Tijdens de dag: snel uren loggen (maakt het weekbestand automatisch aan)
python3 Logboek/log.py dag "Paper X over talent-ID in jeugdvoetbal gelezen en samengevat" 3
python3 Logboek/log.py dag "Dataset RBFA verkend: fysieke profielen U17" 2.5 --datum 2026-11-19

# Op het einde van de week: open weken/<week>.md en vul de 4 secties aan
# (omschrijving, resultaten, problemen/vragen, planning), daarna:
python3 Logboek/log.py mail      # e-mailtekst om naar promotor + begeleiders te sturen

# Om de 2 weken
python3 Logboek/log.py teams     # tekst om in het Teams-kanaal te plakken

# Na een meeting
python3 Logboek/log.py meeting "Feedback literatuurstudie"

# Overzicht en indienen
python3 Logboek/log.py uren      # uren per week + totaal t.o.v. 540 u
python3 Logboek/log.py export    # export/logboek.pdf (info + urenoverzicht + weken + meetings)
```

Tip: maak een alias in `~/.bashrc`:

```bash
alias log='python3 ~/School/Github/Masterproef/Logboek/log.py'
# daarna: log dag "..." 2
```

## Afspraken

- Schrijf de omschrijving **voldoende gedetailleerd**: het logboek moet de kwaliteit en de kwantiteit van je werk aantonen.
- Formuleer resultaten **controleerbaar** (dus niet "literatuurstudie gedaan", wel "hoofdstuk related work over X en Y doorgestuurd naar Maarten").
- Vorige weken aanvullen kan met `--datum`, bijvoorbeeld `log.py week --datum 2026-09-28`.
- Houd je de wekelijkse mails bij als rapportering, dan is de PDF van `export` je bundel voor Plato.
