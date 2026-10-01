from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "CarPrice_Assignment.csv"
OUTPUT_DIR = ROOT / "cache" / "plot"
OUTPUT_PATH = OUTPUT_DIR / "engine_size_vs_horsepower.png"

FONT_SIZE = 10


def plot_engine(
    data_path=DATA_PATH,
    output_path=OUTPUT_PATH,
    save=True,
    show=True,
):
    """Строит график зависимости horsepower от enginesize."""
    plt.rcParams.update({"font.size": FONT_SIZE})

    df = pd.read_csv(data_path)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(
        df["enginesize"],
        df["horsepower"],
        alpha=0.7,
        label="Автомобили",
    )

    ax.set_title("Зависимость мощности от объёма двигателя", fontsize=FONT_SIZE)
    ax.set_xlabel("Объём двигателя (enginesize)", fontsize=FONT_SIZE)
    ax.set_ylabel("Мощность (horsepower)", fontsize=FONT_SIZE)
    ax.legend(fontsize=FONT_SIZE)
    ax.grid(True, alpha=0.3)

    if save:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150, bbox_inches="tight")

    if show:
        plt.show()

    return fig, ax
