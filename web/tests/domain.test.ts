import { describe, expect, it } from "vitest";
import { cartTotalCents, formatCurrency, riskTone } from "../src/domain";

describe("commerce domain helpers", () => {
  it("totals priced cart lines", () => {
    expect(
      cartTotalCents([
        { unitPriceCents: 1200, quantity: 2 },
        { unitPriceCents: 450, quantity: 3 }
      ])
    ).toBe(3750);
  });

  it("formats whole-dollar order values", () => {
    expect(formatCurrency(18900)).toBe("$189");
  });

  it("maps risk scores to checkout tones", () => {
    expect(riskTone(20)).toBe("low");
    expect(riskTone(60)).toBe("review");
    expect(riskTone(90)).toBe("blocked");
  });
});
