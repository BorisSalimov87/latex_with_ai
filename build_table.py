from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "stars.csv"
OUTPUT_DIR = ROOT / "cache" / "tables"
OUTPUT_PATH = OUTPUT_DIR / "stars.tex"

COLUMNS = [
    "Temperature (K)",
    "Luminosity(L/Lo)",
    "Radius(R/Ro)",
    "Absolute magnitude(Mv)",
]

HEADERS = [
    "Температура, K",
    "Светимость, L/Lo",
    "Радиус, R/Ro",
    "Абс. звёздная величина, Mv",
]

N_ROWS = 15


def build_table(
    data_path=DATA_PATH,
    output_path=OUTPUT_PATH,
    n_rows=N_ROWS,
    save=True,
):
    """Строит LaTeX-таблицу по первым строкам набора данных о звёздах."""
    df = pd.read_csv(data_path)
    subset = df[COLUMNS].head(n_rows)

    lines = [
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Характеристики звёзд (первые %d строк)}" % n_rows,
        r"\label{tab:stars}",
        r"\begin{tabular}{rrrr}",
        r"\hline",
        " & ".join(HEADERS) + r" \\",
        r"\hline",
    ]

    for _, row in subset.iterrows():
        cells = " & ".join(f"{row[col]:g}" for col in COLUMNS)
        lines.append(cells + r" \\")

    lines += [
        r"\hline",
        r"\end{tabular}",
        r"\end{table}",
    ]

    table = "\n".join(lines) + "\n"

    if save:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(table, encoding="utf-8")

    return table


if __name__ == "__main__":
    build_table()
