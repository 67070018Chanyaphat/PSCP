"""BTS MRT"""
def price_vehicle():
    """cal price of vehicle to paid"""
    special_day = input()
    age = float(input())
    height = float(input())
    status = "PAY"
    if age < 14:
        if height < 90:
            status = "FREE"
        elif height <= 140:
            if special_day == "Children Day":
                status = "FREE"
    elif age >= 60:
        if special_day == "Senior Day":
            status = "FREE"
    else:
        status = "PAY"
    print(status)
price_vehicle()
