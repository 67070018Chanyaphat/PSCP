"""ท้อ"""
def milk():
    """นมวัวมันหากินยาก ก็ไปกินนมอื่นกันดีกว่า ท้อ"""
    price_per_bottle = int(input())
    promotion_lid = int(input())
    receive_bottle = int(input())
    money_have = int(input())

    normal_buy = money_have // price_per_bottle
    promotion_bottle = normal_buy

    if promotion_lid > 0:
        lids = normal_buy
        while lids >= promotion_lid:
            new_bottles = (lids // promotion_lid) * receive_bottle
            promotion_bottle += new_bottles
            lids = (lids % promotion_lid) + new_bottles

    print(f"{promotion_bottle}")

milk()
