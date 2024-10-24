"""Heron of Alexandria"""
def area():
    """input side of triangle to calculate area"""
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a+b+c)/2
    Area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f"{Area:.3f}")
area()
