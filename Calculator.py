"""Calculator"""
def calculator():
    """total of time to add number from 1 to n"""
    n = int(input())
    timesofnum = ""
    for i in range(1,n+1):
        if n == 1:
            timesofnum += "1"
        else:
            if i < n:
                timesofnum += str(i)+"+"
            elif i == n:
                timesofnum += str(i)+"="
    print(len(timesofnum))
calculator()
