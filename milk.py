"""milk"""
def milk():
    """cal bottle that recieved"""
    price_per_bottle = int(input())
    promotion_lid = int(input())
    receive_bottle = int(input())
    money_have = int(input())

    normal_buy,lid_from_buy,promotion_bottle = 0,0,0
    normal_buy = money_have//price_per_bottle # จำนวนที่จ่ายราคาปกติ

    if money_have > 0: # มีเงิน > 0 บาท
        if promotion_lid > 0: # มีโปรโมชันขวด
            lid_from_buy = normal_buy//promotion_lid # ฝาขวดที่ได้จากซื้อปกติ
            lid_from_pro = lid_from_buy*receive_bottle # ขวดทั้งที่ได้จากแลกฝาแล้ว
            if lid_from_pro >= promotion_lid: # ขวดที่ได้มายังสามารถแลกต่อได้
                lid_pro = lid_from_pro
                while lid_pro:
                    if lid_pro > promotion_lid:
                        lid_pro = (lid_pro//promotion_lid)*receive_bottle
                    else:
                        break
                lid_pro = (lid_from_pro//promotion_lid)*receive_bottle #ขวดที่ได้จากฝาที่ยังแลกมาได้
                promotion_bottle = lid_pro + lid_from_pro + normal_buy #ขวดทั้งหมดที่ได้
            else:
                promotion_bottle = lid_from_pro+normal_buy
        else:
            promotion_bottle = normal_buy
    else:
        promotion_bottle = 0 # ไม่มีเงิน 0

    print(f"{promotion_bottle}")
milk()
