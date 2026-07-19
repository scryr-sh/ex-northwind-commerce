from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    id: str
    sku: str
    name: str
    category: str
    image_url: str
    unit_price_cents: int
    inventory: int
    lead_time_days: int


CATALOG: tuple[Product, ...] = (
    Product(
        id="chai-001",
        sku="BEV-CHAI-48",
        name="Chai Tea Master Case",
        category="Beverages",
        image_url="https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?auto=format&fit=crop&w=640&q=80",
        unit_price_cents=18900,
        inventory=128,
        lead_time_days=3,
    ),
    Product(
        id="ikura-002",
        sku="SEA-IKURA-24",
        name="Ikura Cold Chain Pack",
        category="Seafood",
        image_url="https://images.unsplash.com/photo-1617196034796-73dfa7b1fd56?auto=format&fit=crop&w=640&q=80",
        unit_price_cents=62400,
        inventory=42,
        lead_time_days=2,
    ),
    Product(
        id="tarte-003",
        sku="CON-TARTE-36",
        name="Tarte au Sucre Tray",
        category="Confections",
        image_url="https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=640&q=80",
        unit_price_cents=27600,
        inventory=75,
        lead_time_days=5,
    ),
)


def get_product(product_id: str) -> Product | None:
    return next((product for product in CATALOG if product.id == product_id), None)
