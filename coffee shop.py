"""Coffeee"""
def coffee(a_value, b_value, c_value, d_value, e_value):
    """calulate the promotion for coffeees"""
    pro1 = a_value + (e_value - 1)*a_value*(1 - b_value / 100)
    pro2 = a_value*e_value
    if pro2 >= d_value:
        pro2 = pro2 * (1 - c_value / 100)
    if pro2 <= pro1:
        print(2)
        print(f"{pro2:.2f}")
    else:
        print(1)
        print(f"{pro1:.2f}")
coffee(float(input()), float(input()), float(input()), float(input()), int(input()))
