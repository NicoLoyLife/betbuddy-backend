#!/bin/sh
# Warte, bis die Datenbank erreichbar ist

set -e

host="$1"
port="$2"

until nc -z "$host" "$port"; do
  echo "Warte auf Datenbank $host:$port ..."
  sleep 1
done 