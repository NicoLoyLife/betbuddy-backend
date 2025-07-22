# Minimalistisches Dockerfile für BetBuddy Backend
FROM python:3.13-slim

# Arbeitsverzeichnis
WORKDIR /app

# Abhängigkeiten
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Projektdateien
COPY . .

# Django-Entrypoint
CMD ["gunicorn", "betbuddy.wsgi:application", "--bind", "0.0.0.0:8000"] 