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
**Hinweis:** Im Docker-Setup für Entwicklung liefert Django die statischen Dateien selbst aus. In Produktion müssen statische Dateien (z. B. /static/admin/...) von einem Webserver wie nginx ausgeliefert werden. Siehe Django-Doku zu "Deploying static files". 

## Hinweise für Produktion

- `DJANGO_CSRF_TRUSTED_ORIGINS`: Kommagetrennte Liste vertrauenswürdiger Domains für CSRF-Schutz (z. B. https://meine-domain.de)
- `DJANGO_USE_X_FORWARDED_PROTO`: Auf `True` setzen, wenn ein Proxy wie nginx/Traefik SSL terminiert
- `DJANGO_SESSION_COOKIE_SECURE`, `DJANGO_CSRF_COOKIE_SECURE`: Auf `True` setzen, wenn HTTPS verwendet wird
  
**Statische Dateien:** In Produktion müssen statische Dateien (z. B. /static/admin/...) von einem Webserver wie nginx ausgeliefert werden. Siehe Django-Doku zu "Deploying static files". 

## Best Practices für Produktion

- **Django- und Python-Version aktuell halten**: Immer aktuelle, sichere Versionen nutzen.
- **Datenbank- und Backup-Strategie**: Regelmäßige Backups, sichere DB-User, Restore testen.
- **Gunicorn/Uvicorn-Konfiguration**: Worker-Anzahl und Timeouts sinnvoll setzen.
- **Reverse Proxy/Webserver (nginx, Traefik)**: Statische/Medien-Dateien ausliefern, HTTPS aktivieren, HTTP auf HTTPS umleiten.
- **Sicherheits-Header**: HSTS, X-Frame-Options, Content-Type-Nosniff, XSS-Filter etc. setzen (siehe Django-Settings-Beispiel unten).
- **Monitoring & Error-Tracking**: Tools wie Sentry, ELK, Prometheus, Grafana nutzen.
- **Automatisierte Tests & CI/CD**: Hohe Testabdeckung, automatisierte Deployments.
- **Rate Limiting & API-Schutz**: z. B. mit django-ratelimit, Authentifizierung für APIs.
- **Django Admin absichern**: Admin-URL umbenennen, Zugriff beschränken, 2FA nutzen.
- **Umgang mit Secrets**: Niemals im Code, nur per Umgebungsvariablen oder Secret-Management.
- **Settings trennen**: Entwicklung, Test, Produktion sauber trennen.
- **DB-Verbindungen absichern**: SSL/TLS, Zugriff nur von nötigen Hosts.
- **CORS & CSRF**: Header restriktiv setzen, CSRF immer aktivieren.
- **Logging & Datenschutz**: Keine sensiblen Daten loggen, DSGVO beachten.

**Beispiel für zusätzliche Sicherheits-Header in settings.py:**
```python
SECURE_HSTS_SECONDS = 31536000  # 1 Jahr
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
```

**Hinweis:** Viele dieser Maßnahmen sind für ein MVP nicht zwingend, aber für den Live-Betrieb sehr wichtig! 