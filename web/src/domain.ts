export type PricedLine = {
  unitPriceCents: number;
  quantity: number;
};

export function cartTotalCents(lines: PricedLine[]): number {
  return lines.reduce((total, line) => total + line.unitPriceCents * line.quantity, 0);
}

export function formatCurrency(cents: number): string {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0
  }).format(cents / 100);
}

export function riskTone(score: number): "low" | "review" | "blocked" {
  if (score >= 80) {
    return "blocked";
  }
  if (score >= 45) {
    return "review";
  }
  return "low";
}
