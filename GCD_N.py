"""pla nin aeb mong kan tum mai"""
from math import gcd
from functools import reduce
numlist = [int(input()) for _ in range(int(input()))]
def find_gcd(num_list):
    """find gcd from library easier"""
    return reduce(gcd, num_list)
print(find_gcd(numlist))
