# BetBuddy Backend

Automatisiertes Backend für Fußballwetten-Analyse und Wettempfehlungen.

## Setup (erster Schritt)

1. Python 3.13.5 installieren
2. (Optional) Virtuelle Umgebung anlegen
3. Siehe weitere Schritte nach Django-Initialisierung 

## Wichtige Umgebungsvariablen

- `DJANGO_SECRET_KEY`: Geheimer Schlüssel für Django (Pflicht, in Produktion unbedingt sicher wählen!)
- `DJANGO_DEBUG`: Debug-Modus (`True` für Entwicklung, `False` für Produktion)
- `DJANGO_ALLOWED_HOSTS`: Kommagetrennte Liste erlaubter Hosts (z. B. `localhost,127.0.0.1`)
- `DJANGO_LANGUAGE_CODE`: Sprache (z. B. `de-de`, `en-us`)
- `DJANGO_TIME_ZONE`: Zeitzone (z. B. `Europe/Berlin`)
- `DJANGO_STATIC_URL`, `DJANGO_STATIC_ROOT`: URL und Speicherort für statische Dateien (z. B. `/static/`, `./staticfiles`)
- `DJANGO_MEDIA_URL`, `DJANGO_MEDIA_ROOT`: URL und Speicherort für Medien-Dateien (z. B. `/media/`, `./media`)
- `DJANGO_LOG_LEVEL`: Log-Level für die Konsole (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`: Datenbankzugang (siehe `.env.example`)

## Entwicklung & Code-Qualität

- Entwicklungsabhängigkeiten: `requirements-dev.txt` (black, flake8, pre-commit)
- Pre-Commit-Hooks prüfen und formatieren automatisch den Code vor jedem Commit:
  - [black](https://black.readthedocs.io/): Automatisches Code-Formatieren
  - [flake8](https://flake8.pycqa.org/): Linting und Fehlerprüfung
- Konfiguration:
  - `pyproject.toml` für black (Zeilenlänge 88, Python 3.13)
  - `.flake8` für flake8 (Zeilenlänge 88, Black-Kompatibilität)
- Installation & Aktivierung:
  ```bash
  pip install -r requirements-dev.txt
  pre-commit install
  ```
- Manuelles Ausführen für alle Dateien:
  ```bash
  pre-commit run --all-files
  ``` 