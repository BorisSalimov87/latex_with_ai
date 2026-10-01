from pathlib import Path

ROOT = Path(__file__).resolve().parent

ARTICLE_PATH = ROOT / "article" / "article.tex"
PLOT_PATH = ROOT / "cache" / "plot" / "engine_size_vs_horsepower.png"
TABLE_PATH = ROOT / "cache" / "tables" / "stars.tex"

def clear_article(path=ARTICLE_PATH):
    """Полностью очищает файл статьи."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")
    return path


def remove_generated(path):
    """Удаляет сгенерированный файл, если он существует."""
    path = Path(path)
    if path.exists():
        path.unlink()
        return True
    return False


def clear_all(
    article_path=ARTICLE_PATH,
    plot_path=PLOT_PATH,
    table_path=TABLE_PATH,
):
    """Очищает статью и удаляет сгенерированные график и таблицу."""
    clear_article(article_path)
    remove_generated(plot_path)
    remove_generated(table_path)


if __name__ == "__main__":
    clear_all()
