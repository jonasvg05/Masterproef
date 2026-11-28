"""Zet elk tabblad van codebook.xlsx om naar een aparte csv in de map codebook/."""

from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
INPUT_FILE = PROJECT_DIR / "data" / "codebook.xlsx"
OUTPUT_DIR = PROJECT_DIR / "data" / "codebook"


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Alles als tekst inlezen zodat waarden als "None" en "N/A" niet leeg worden
    # en getallen niet van vorm veranderen. header=None houdt elke rij intact,
    # ook op "Read me", dat geen kolomnamen heeft.
    sheets = pd.read_excel(
        INPUT_FILE, sheet_name=None, header=None, dtype=str, keep_default_na=False
    )

    for sheet_name, df in sheets.items():
        output_file = OUTPUT_DIR / f"{sheet_name.lower().replace(' ', '_')}.csv"
        # utf-8-sig: zelfde codering als ratings.csv en reports.csv
        df.to_csv(output_file, index=False, header=False, encoding="utf-8-sig")
        print(f"{sheet_name}: {len(df)} rijen -> {output_file.name}")


if __name__ == "__main__":
    main()
