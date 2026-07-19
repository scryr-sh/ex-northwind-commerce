#!/usr/bin/env sh
set -eu

API_URL="${API_URL:-http://localhost:8000}"

curl -fsS "$API_URL/health" >/dev/null
curl -fsS "$API_URL/catalog" >/dev/null
curl -fsS \
  -H "Content-Type: application/json" \
  -d '{"accountId":"northwind-wholesale","currency":"usd","shippingSpeed":"expedited","lines":[{"productId":"chai-001","quantity":2}]}' \
  "$API_URL/checkout" >/dev/null

echo "Smoke test passed for $API_URL"
