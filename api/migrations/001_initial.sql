create table if not exists products (
  id text primary key,
  sku text not null unique,
  name text not null,
  category text not null,
  image_url text not null,
  unit_price_cents integer not null check (unit_price_cents > 0),
  inventory integer not null check (inventory >= 0),
  lead_time_days integer not null check (lead_time_days >= 0)
);

create table if not exists orders (
  id text primary key,
  account_id text not null,
  currency text not null default 'usd',
  total_cents integer not null check (total_cents >= 0),
  risk_score integer not null check (risk_score between 0 and 100),
  stripe_payment_intent_id text not null,
  created_at timestamptz not null default now()
);

insert into products (id, sku, name, category, image_url, unit_price_cents, inventory, lead_time_days)
values
  ('chai-001', 'BEV-CHAI-48', 'Chai Tea Master Case', 'Beverages', 'https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?auto=format&fit=crop&w=640&q=80', 18900, 128, 3),
  ('ikura-002', 'SEA-IKURA-24', 'Ikura Cold Chain Pack', 'Seafood', 'https://images.unsplash.com/photo-1617196034796-73dfa7b1fd56?auto=format&fit=crop&w=640&q=80', 62400, 42, 2),
  ('tarte-003', 'CON-TARTE-36', 'Tarte au Sucre Tray', 'Confections', 'https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=640&q=80', 27600, 75, 5)
on conflict (id) do update set
  sku = excluded.sku,
  name = excluded.name,
  category = excluded.category,
  image_url = excluded.image_url,
  unit_price_cents = excluded.unit_price_cents,
  inventory = excluded.inventory,
  lead_time_days = excluded.lead_time_days;
