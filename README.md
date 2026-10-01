Учебный проект по работе с LaTeX вместе с ИИ-агентом.

Инструкция по настройке рабочего окружения.

## 1. Установите дистрибутив TeX

LaTeX распространяется в виде дистрибутивов, включающих компиляторы (`pdflatex`, `xelatex`, `lualatex`), пакеты и утилиты.

### Linux

Рекомендуется **TeX Live**.

- Официальная инструкция: https://www.tug.org/texlive/quickinstall.html
- Страница загрузки: https://www.tug.org/texlive/acquire.html

Установка через менеджер пакетов (проще, но пакеты могут быть неполными):

```bash
# Debian / Ubuntu
sudo apt update
sudo apt install texlive-full

# Fedora
sudo dnf install texlive-scheme-full

# Arch Linux
sudo pacman -S texlive-most
```

Проверка установки:

```bash
pdflatex --version
```

### Windows

Рекомендуется **MiKTeX** или **TeX Live**.

- MiKTeX (загрузка): https://miktex.org/download
- TeX Live (загрузка, инструкция): https://www.tug.org/texlive/windows.html
- Альтернатива: https://tug.org/texlive/acquire-netinstall.html

Шаги для MiKTeX:

1. Скачайте установщик со страницы https://miktex.org/download.
2. Запустите его и следуйте мастеру установки.
3. Разрешите автоматическую установку отсутствующих пакетов (опция "Install missing packages on-the-fly").

Проверка установки (в PowerShell или CMD):

```powershell
pdflatex --version
```

## 2. Установите VS Code

- Скачать: https://code.visualstudio.com/download
- Linux (Debian / Ubuntu):

```bash
sudo apt install ./code_*.deb
```

- Linux (snap):

```bash
sudo snap install code --classic
```

- Windows: скачайте установщик `.exe` по ссылке выше и запустите его.

## 3. Установите LaTeX Workshop

Расширение **LaTeX Workshop** добавляет сборку, предпросмотр PDF и подсветку синтаксиса.

Установка:

1. Откройте VS Code.
2. Перейдите в **Extensions** (`Ctrl+Shift+X`).
3. Найдите `LaTeX Workshop`.
4. Нажмите **Install**.

Либо из командной строки:

```bash
code --install-extension James-Yu.latex-workshop
```

Страница расширения: https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop

## 4. Установите ИИ-агента

Выберите любой удобный инструмент:

- **KiloCode** — https://kilo.ai
- **OpenCode** — https://opencode.ai
- Либо свой агент: **Codex**, **Claude Code** и т.п.

Установка KiloCode как расширения VS Code:

1. Откройте **Extensions** (`Ctrl+Shift+X`).
2. Найдите `KiloCode`.
3. Нажмите **Install**.

Либо из командной строки:

```bash
code --install-extension kilocode.kilo-code
```

## 5. Привязка модели от провайдера LLM (например, router.ai)

Некоторые агенты требуют API-ключ и указание модели. Рассмотрим на примере провайдера **router.ai** (https://router.ai):

1. Зарегистрируйтесь на https://router.ai и создайте API-ключ в личном кабинете.
2. Откройте настройки модели в вашем ИИ-агенте (в KiloCode: **Settings → Providers**).
3. Выберите провайдера `router.ai` (или `OpenAI Compatible` / `Custom`).
4. Укажите:
   - Base URL: URL API провайдера, например `https://api.router.ai/v1` (уточните в документации router.ai);
   - API Key: созданный ключ;
   - Model: идентификатор нужной модели.
5. Сохраните настройки и проверьте подключение, отправив тестовый запрос агенту.

Не храните API-ключи в репозитории — используйте переменные окружения или менеджер секретов.

## 6. Установите uv и инициализируйте Python-окружение

[uv](https://docs.astral.sh/uv/) — быстрый менеджер Python-пакетов и виртуальных окружений, используемый в этом проекте (`pyproject.toml` и `uv.lock`).

### Установка uv

- Документация по установке: https://docs.astral.sh/uv/getting-started/installation/

Linux / macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Либо через pip, если Python уже установлен:

```bash
pip install uv
```

Проверка установки:

```bash
uv --version
```

### Инициализация окружения после скачивания репозитория

1. Склонируйте репозиторий и перейдите в его каталог:

```bash
git clone <URL_РЕПОЗИТОРИЯ>
cd latex_with_ai
```

2. Создайте виртуальное окружение и установите зависимости (включая dev-группу для Jupyter):

```bash
uv sync --dev
```

`uv sync` создаст каталог `.venv` и установит все зависимости из `uv.lock` в точных версиях. Ключ `--dev` дополнительно ставит пакеты из группы `dev` (ipykernel, jupyterlab).

3. Проверьте окружение, запустив интерпретатор:

```bash
uv run python --version
```

4. Запустите Jupyter Lab (для работы с `discover.ipynb`):

```bash
uv run jupyter lab
```

Все команды Python в проекте выполняйте через `uv run <команда>`, чтобы они использовали нужное окружение.
