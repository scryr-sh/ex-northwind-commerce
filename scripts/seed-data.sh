#!/usr/bin/env sh
set -eu

DATABASE_URL="${DATABASE_URL:-postgresql://northwind:northwind@localhost:5432/northwind}"

if ! command -v psql >/dev/null 2>&1; then
  echo "psql is required to seed data" >&2
  exit 1
fi

psql "$DATABASE_URL" -f api/migrations/001_initial.sql
