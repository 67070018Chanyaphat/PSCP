"""Restuarant"""
def cal_money():
    """help call money to value of price"""
    foodbuy_price = float(input())
    promotion = float(input())
    discount = float(input())
    buy_more = float(input())
    #############################################
    price_discount = promotion*(discount/100)+buy_more*(discount/100)
    price_buymore = foodbuy_price+buy_more
    discount_buymore = price_buymore-(price_buymore*(discount/100))
    ############################################
    if promotion <= foodbuy_price or not discount:
        status = "Yes"
        print(status)
    else:
        if price_discount < buy_more:
            status = "No"
            money_paid = discount_buymore-foodbuy_price
        else:
            status = "Yes"
            money_paid = foodbuy_price-discount_buymore
        print(f"{status} {money_paid:.3f}")
    ###############################
cal_money()
