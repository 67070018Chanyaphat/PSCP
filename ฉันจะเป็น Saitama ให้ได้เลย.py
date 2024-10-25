"""saimata"""
import math
def saitama():
    """"tyg"""
    vidpeun = int(input())
    situp = int(input())
    standsit = int(input())
    run = int(input())
    countvidpeun = int(input())
    countsitup = int(input())
    countrun = int(input())
    countstandsit = int(input())
    thisisthelargestnumber = 0
    countvidpeun = vidpeun/countvidpeun
    if thisisthelargestnumber < countvidpeun:
        thisisthelargestnumber = countvidpeun
    countsitup = situp/countsitup
    if thisisthelargestnumber < countsitup:
        thisisthelargestnumber = countsitup
    countrun = run/countrun
    if thisisthelargestnumber < countrun:
        thisisthelargestnumber = countrun
    countstandsit = standsit/countstandsit
    if thisisthelargestnumber < countstandsit:
        thisisthelargestnumber = countstandsit
    print(math.ceil(thisisthelargestnumber))
    # print(countvidpeun)
saitama()
