"""hometown cha cha cha"""
import math
def cal_moneyy():
    """hongwon work hour to cal money from rate"""
    day = int(input())
    salary = 0
    for _ in range(1, day+1):
        hour = math.ceil(float(input()))
        salary += (hour*8720)
    print(salary)
cal_moneyy()
