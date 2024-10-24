"""Parity"""
def paritybit():
    """add bit behind binary from Pririty"""
    datanum = input()
    pririty = input()
    count_one = 0
    for i in datanum:
        if i == "1":
            count_one+=1
    if pririty == "Even":
        if not count_one % 2:
            print(datanum+"0")
        if count_one % 2:
            print(datanum+"1")
    else:
        if not count_one % 2:
            print(datanum+"1")
        if count_one % 2:
            print(datanum+"0")
paritybit()
