# Architecture

Northwind Commerce is organized around a buyer-facing React storefront and a FastAPI backend.

## Request Flow

1. The web app loads `/catalog` from `northwind-api`.
2. The buyer selects case quantities and submits a checkout request.
3. The API validates inventory, calculates order value, scores payment risk, and creates a Stripe payment intent.
4. Postgres is the source of record for products and orders.
5. Redis is reserved for session state, checkout idempotency, and risk-score caching.

## Services

- `northwind-web`: React/Vite storefront.
- `northwind-api`: FastAPI catalog and checkout service.
- `northwind-postgres`: relational data store.
- `northwind-redis`: cache and ephemeral checkout state.
- `stripe-integration`: payment intent creation and webhook target.

## Payment Risk

The sample risk model is deliberately transparent. It increases score for high order value, large quantities, expedited shipping, and cold-chain seafood items. Production systems should replace this with a policy engine or model that uses audited features.

## Deployment Promotion

`deploy.yml` models manual promotion to staging or production. The Terraform files are stubs that show the variables a real deployment would bind to managed compute, database, cache, secrets, and DNS resources.
