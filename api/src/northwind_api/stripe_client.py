from uuid import uuid4

import stripe


def create_payment_intent(
    *,
    stripe_secret_key: str,
    amount_cents: int,
    currency: str,
    metadata: dict[str, str],
) -> dict[str, str]:
    if not stripe_secret_key or stripe_secret_key == "sk_test_stub":
        checkout_id = uuid4().hex[:12]
        return {
            "payment_intent_id": f"pi_stub_{checkout_id}",
            "client_secret": f"pi_stub_{checkout_id}_secret_stub",
            "status": "stubbed",
        }

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=amount_cents,
        currency=currency,
        automatic_payment_methods={"enabled": True},
        metadata=metadata,
    )
    return {
        "payment_intent_id": intent["id"],
        "client_secret": intent["client_secret"],
        "status": intent["status"],
    }
