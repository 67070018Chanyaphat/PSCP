"""longer"""
import math
def longer():
    """cal long of circle from radius"""
    radius = float(input())
    width = float(input())
    length = float(input())
    cal_circle = 2*math.pi*radius
    cal_rec = width*2+length*2
    dif = abs(cal_circle-cal_rec)
    def check(a,b):
        if a>b:
            status = "Circle is longer"
        elif a<b:
            status = "Rectangle is longer"
        else:
            status = "Equal"
        return status
    print(check(cal_circle,cal_rec))
    print(f"{dif:.5f}")
longer()
