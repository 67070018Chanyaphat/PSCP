"""PH"""
def ph(ph_check):
    """check ph rate from"""
    if 0 <= ph_check < 7:
        ph_rate = "acidic"
    elif ph_check == 7:
        ph_rate = "neutral"
    elif 7 < ph_check <= 14:
        ph_rate = "akaline"
    else:
        ph_rate = "error"
    print(ph_rate)
ph(float(input()))
