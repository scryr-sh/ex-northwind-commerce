# Decision Log

## 0001: Keep Checkout Risk Explainable

The sample uses a transparent heuristic risk score rather than a black-box model. This keeps demos easy to inspect and makes payment-review behavior deterministic in tests.

## 0002: Stub Stripe by Default

Local checkout uses `STRIPE_SECRET_KEY=sk_test_stub`. This shows the integration boundary while keeping the sample runnable without external credentials or network access.

## 0003: Terraform as Promotion Contract

The Terraform files are stubs instead of provider-specific infrastructure. This keeps the repository portable while still documenting the promotion inputs that real infrastructure would need.
