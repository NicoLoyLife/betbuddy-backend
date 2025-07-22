# BetBuddy Backend

Automatisiertes Backend für Fußballwetten-Analyse und Wettempfehlungen.

## Setup (erster Schritt)

1. Python 3.13.5 installieren
2. (Optional) Virtuelle Umgebung anlegen
3. Siehe weitere Schritte nach Django-Initialisierung 

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