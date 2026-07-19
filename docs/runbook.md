# Runbook

## Start Local Stack

```bash
cp .env.example .env
docker compose up
```

## Verify Services

```bash
curl http://localhost:8000/health
curl http://localhost:8000/catalog
./scripts/smoke-test.sh
```

## Seed Data

```bash
DATABASE_URL=postgresql://northwind:northwind@localhost:5432/northwind ./scripts/seed-data.sh
```

## Stripe Mode

Use `STRIPE_SECRET_KEY=sk_test_stub` for local development. The API will return deterministic stub-shaped payment intent data without contacting Stripe.

Use a real Stripe test key only in isolated test environments. Never commit real keys.

## Promotion

1. Confirm CI is green on `main`.
2. Trigger the `Deploy` workflow.
3. Select `staging`.
4. Run smoke tests.
5. Trigger the workflow again for `production`.
