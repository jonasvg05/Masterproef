#!/usr/bin/env python3
"""Logboek masterproef: wekelijkse rapportering volgens DoeJaar-richtlijnen.

Gebruik (vanuit de repo-root of de map Logboek):
    python3 Logboek/log.py dag "Literatuur over talent-ID modellen gelezen" 3.5
    python3 Logboek/log.py week [--datum 2026-11-16]
    python3 Logboek/log.py meeting "Feedback literatuurstudie" [--datum 2026-11-20]
    python3 Logboek/log.py mail [--datum ...]     # wekelijkse e-mail aan promotoren
    python3 Logboek/log.py teams                  # tweewekelijkse update voor Teams
    python3 Logboek/log.py uren                   # urenoverzicht t.o.v. 540 u
    python3 Logboek/log.py export                 # logboek.pdf voor Plato
"""

import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WEKEN = ROOT / "weken"
MEETINGS = ROOT / "meetings"
INFO = ROOT / "info.md"
EXPORT_DIR = ROOT / "export"
UREN_DOEL = 540

MAANDEN = ["jan", "feb", "mrt", "apr", "mei", "jun",
           "jul", "aug", "sep", "okt", "nov", "dec"]

WEEK_TEMPLATE = """# Week {week} ({van} – {tot})

**Datum:** {van} – {tot}

## Urenregistratie

| Datum | Uren | Activiteit |
|---|---|---|

## Omschrijving activiteiten

<!-- Voldoende gedetailleerde omschrijving van wat je deze week gedaan hebt. -->

## Resultaten

<!-- Concrete, controleerbare resultaten: hoofdstuk X doorgestuurd, script Y werkt op dataset Z, figuren, ... -->

## Problemen / vragen / opmerkingen

<!-- Waar loop je vast? Welke vragen heb je voor de begeleiders? -->

## Planning komende week

<!-- Wat ga je volgende week doen? -->
"""

MEETING_TEMPLATE = """# Meeting {datum}: {titel}

**Datum:** {datum}
**Aanwezigen:** Jonas Van Goethem, ...
**Presentatie:** <!-- link naar slides (uploaden in Teams, tab Files) -->

## Besproken

-

## Feedback

-

## Actiepunten

- [ ]
"""


def parse_datum(s):
    return dt.date.fromisoformat(s) if s else dt.date.today()


def nl_datum(d):
    return f"{d.day} {MAANDEN[d.month - 1]} {d.year}"


def week_pad(d):
    jaar, week, _ = d.isocalendar()
    return WEKEN / f"{jaar}-W{week:02d}.md"


def maak_week(d):
    pad = week_pad(d)
    if not pad.exists():
        jaar, week, _ = d.isocalendar()
        maandag = dt.date.fromisocalendar(jaar, week, 1)
        WEKEN.mkdir(exist_ok=True)
        pad.write_text(WEEK_TEMPLATE.format(
            week=week, van=nl_datum(maandag),
            tot=nl_datum(maandag + dt.timedelta(days=6))), encoding="utf-8")
        print(f"Nieuwe week aangemaakt: {pad.relative_to(ROOT.parent)}")
    return pad


def secties(tekst):
    """Splits een weekbestand in {kop: inhoud} (zonder HTML-commentaar)."""
    tekst = re.sub(r"<!--.*?-->", "", tekst, flags=re.S)
    delen = re.split(r"^## (.+)$", tekst, flags=re.M)
    return {delen[i].strip(): delen[i + 1].strip() for i in range(1, len(delen), 2)}


def uren_rijen(tekst):
    rijen = []
    for regel in secties(tekst).get("Urenregistratie", "").splitlines():
        cellen = [c.strip() for c in regel.strip().strip("|").split("|")]
        if len(cellen) >= 3 and re.match(r"\d{4}-\d{2}-\d{2}", cellen[0]):
            try:
                rijen.append((cellen[0], float(cellen[1].replace(",", ".")), cellen[2]))
            except ValueError:
                pass
    return rijen


def cmd_dag(args):
    d = parse_datum(args.datum)
    pad = maak_week(d)
    try:
        uren_f = float(args.uren.replace(",", "."))
    except ValueError:
        sys.exit(f"Ongeldig aantal uren: {args.uren}")
    uren = f"{uren_f:g}"
    activiteit = args.activiteit.replace("|", "/").strip()

    regels = pad.read_text(encoding="utf-8").splitlines()
    start = regels.index("## Urenregistratie")
    # Tabelrijen (na kop en scheidingslijn) verzamelen, nieuwe rij toevoegen, sorteren op datum
    tabel_idx = [i for i in range(start + 1, len(regels))
                 if regels[i].startswith("|")
                 and not any(regels[j].startswith("## ") for j in range(start + 1, i))]
    kop, data = tabel_idx[:2], tabel_idx[2:]
    rijen = [regels[i] for i in data] + [f"| {d.isoformat()} | {uren} | {activiteit} |"]
    rijen.sort(key=lambda r: r.strip("| ")[:10])
    regels[kop[-1] + 1:(data[-1] + 1) if data else kop[-1] + 1] = rijen
    pad.write_text("\n".join(regels) + "\n", encoding="utf-8")
    totaal = sum(r[1] for r in uren_rijen(pad.read_text(encoding="utf-8")))
    print(f"Gelogd: {uren} u op {d.isoformat()} (deze week: {totaal:g} u)")


def cmd_week(args):
    print(maak_week(parse_datum(args.datum)))


def cmd_meeting(args):
    d = parse_datum(args.datum)
    slug = re.sub(r"[^a-z0-9]+", "-", args.titel.lower()).strip("-")
    MEETINGS.mkdir(exist_ok=True)
    pad = MEETINGS / f"{d.isoformat()}_{slug}.md"
    if pad.exists():
        sys.exit(f"Bestaat al: {pad}")
    pad.write_text(MEETING_TEMPLATE.format(datum=nl_datum(d), titel=args.titel),
                   encoding="utf-8")
    print(pad)


def week_samenvatting(pad, met_uren=True):
    tekst = pad.read_text(encoding="utf-8")
    s = secties(tekst)
    rijen = uren_rijen(tekst)
    titel = tekst.splitlines()[0].lstrip("# ")
    uit = [titel, ""]
    if met_uren and rijen:
        uit.append(f"Uren: {sum(r[1] for r in rijen):g} u")
        uit += [f"  - {r[0]}: {r[2]} ({r[1]:g} u)" for r in rijen]
        uit.append("")
    for kop in ["Omschrijving activiteiten", "Resultaten",
                "Problemen / vragen / opmerkingen", "Planning komende week"]:
        uit += [f"{kop}:", s.get(kop) or "-", ""]
    return "\n".join(uit)


def cmd_mail(args):
    pad = week_pad(parse_datum(args.datum))
    if not pad.exists():
        sys.exit(f"Geen logboek voor deze week ({pad.name}). Maak het met: log.py week")
    titel = pad.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
    print(f"Onderwerp: [Masterproef] Weekrapportering {titel}\n")
    print("Beste,\n\nHieronder mijn rapportering van de voorbije week.\n")
    print(week_samenvatting(pad))
    print("Met vriendelijke groeten,\nJonas Van Goethem")


def cmd_teams(args):
    weken = sorted(WEKEN.glob("*.md"))[-2:]
    if not weken:
        sys.exit("Nog geen weken gelogd.")
    print("**Update masterproef (laatste 2 weken)**\n")
    for pad in weken:
        print(week_samenvatting(pad, met_uren=False))


def alle_uren():
    return [(p, sum(r[1] for r in uren_rijen(p.read_text(encoding="utf-8"))))
            for p in sorted(WEKEN.glob("*.md"))]


def cmd_uren(args):
    cum = 0.0
    for pad, uren in alle_uren():
        cum += uren
        print(f"{pad.stem}  {uren:6.1f} u   totaal {cum:6.1f} u")
    print(f"\nTotaal: {cum:g} / {UREN_DOEL} u ({cum / UREN_DOEL:.0%})")


def cmd_export(args):
    EXPORT_DIR.mkdir(exist_ok=True)
    delen = [re.sub(r"<!--.*?-->", "", INFO.read_text(encoding="utf-8"), flags=re.S)]

    cum, tabel = 0.0, ["| Week | Uren | Cumulatief |", "|---|---|---|"]
    for pad, uren in alle_uren():
        cum += uren
        tabel.append(f"| {pad.stem} | {uren:g} | {cum:g} |")
    delen.append("## Urenoverzicht\n\n" + "\n".join(tabel) +
                 f"\n\n**Totaal: {cum:g} u** (richtlijn {UREN_DOEL} u)")

    delen.append("# Overzicht weekresultaten")
    for pad in sorted(WEKEN.glob("*.md")):
        tekst = re.sub(r"<!--.*?-->", "", pad.read_text(encoding="utf-8"), flags=re.S)
        delen.append("\\newpage\n\n" + re.sub(r"^# ", "## ", tekst, flags=re.M,
                                               count=1).replace("\n## ", "\n### "))

    if not args.zonder_meetings and any(MEETINGS.glob("*.md")):
        delen.append("\\newpage\n\n# Bijlage: meetingverslagen")
        for pad in sorted(MEETINGS.glob("*.md")):
            tekst = re.sub(r"<!--.*?-->", "", pad.read_text(encoding="utf-8"), flags=re.S)
            delen.append(re.sub(r"<!--.*?-->", "", re.sub(r"^# ", "## ", tekst, count=1), flags=re.S).replace("\n## ", "\n### "))

    md = EXPORT_DIR / "logboek.md"
    md.write_text("\n\n".join(delen) + "\n", encoding="utf-8")
    print(f"Markdown: {md.relative_to(ROOT.parent)}")

    if not shutil.which("pandoc"):
        print("pandoc niet gevonden: alleen markdown geëxporteerd.")
        return
    pdf = EXPORT_DIR / "logboek.pdf"
    subprocess.run(["pandoc", str(md), "-o", str(pdf), "--pdf-engine=xelatex",
                    "-V", "geometry:margin=2cm", "-V", "lang=nl",
                    "-V", "mainfont=DejaVu Sans", "-V", "fontsize=10pt"], check=True)
    print(f"PDF: {pdf.relative_to(ROOT.parent)}")


def main():
    p = argparse.ArgumentParser(description="Logboek masterproef")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("dag", help="uren + activiteit loggen")
    s.add_argument("activiteit")
    s.add_argument("uren", help="bv. 2.5 of 2,5")
    s.add_argument("--datum", help="YYYY-MM-DD (standaard: vandaag)")
    s.set_defaults(f=cmd_dag)

    s = sub.add_parser("week", help="weekbestand aanmaken")
    s.add_argument("--datum")
    s.set_defaults(f=cmd_week)

    s = sub.add_parser("meeting", help="meetingverslag aanmaken")
    s.add_argument("titel")
    s.add_argument("--datum")
    s.set_defaults(f=cmd_meeting)

    s = sub.add_parser("mail", help="weekrapportering als e-mailtekst")
    s.add_argument("--datum")
    s.set_defaults(f=cmd_mail)

    s = sub.add_parser("teams", help="tweewekelijkse Teams-update")
    s.set_defaults(f=cmd_teams)

    s = sub.add_parser("uren", help="urenoverzicht")
    s.set_defaults(f=cmd_uren)

    s = sub.add_parser("export", help="logboek.pdf voor Plato")
    s.add_argument("--zonder-meetings", action="store_true")
    s.set_defaults(f=cmd_export)

    args = p.parse_args()
    args.f(args)


if __name__ == "__main__":
    main()
