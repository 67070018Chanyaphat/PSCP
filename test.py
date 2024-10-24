def cal_money():
    """Calculate if adding an extra item for a discount promotion is worth it."""
    # Read inputs
    foodbuy_price = float(input().strip())
    promotion = float(input().strip())
    discount = float(input().strip())
    buy_more = float(input().strip())

    # Compute total price after adding the extra item
    total_with_additional = foodbuy_price + buy_more

    # Determine if the promotion applies
    if total_with_additional >= promotion:
        # Calculate the discount amount
        discount_amount = (discount / 100) * total_with_additional
        final_amount_with_promo = total_with_additional - discount_amount
    else:
        # No discount applies
        final_amount_with_promo = total_with_additional

    # Determine the output based on comparison
    if final_amount_with_promo < foodbuy_price:
        # Promotion is beneficial
        savings = foodbuy_price - final_amount_with_promo
        print(f"Yes {savings:.3f}")
    elif final_amount_with_promo > foodbuy_price:
        # Additional food costs more than the discount
        extra_cost = final_amount_with_promo - foodbuy_price
        print(f"No {extra_cost:.3f}")
    else:
        # Final amount is the same as the initial amount
        print("Yes")

cal_money()
