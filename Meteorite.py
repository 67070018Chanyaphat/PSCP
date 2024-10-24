"""Meteorite"""
def meteorite():
    """cal num less of ขีปนาวุธ for protect earth"""
    a = float(input())
    b = int(input())
    c = float(input())
    times_bang = 0
    num = 1
    while a >= c:
        times_bang+=num
        a = a/b
        num = num*b
    print(times_bang)
meteorite()
