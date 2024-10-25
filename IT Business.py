"""Hello"""
def main():
    """HAHA"""
    a = float(input())
    now = float(input())
    count = 0
    while True:
        x = input()
        if x == "end":
            break
        if x[0] == "D":
            if float(x[2:]) <= now:
                a += float(x[2:])
                now -= float(x[2:])
                count = 0
            else:
                count += 1
        else:
            if float(x[2:]) <= a:
                a -= float(x[2:])
                now += float(x[2:])
                count = 0
            else:
                count += 1
        if count == 3:
            break
    print(f'{a:.2f}')
    print(f'{now:.2f}')
main()
