"""Elo"""
def main():
    """Elo"""
    Ra = int(input())
    Rb = int(input())
    choose = input()
    if choose == "A":
        count = 1/(1+(10**((Rb-Ra)/400)))
        print(f"{count:.2f}")
    elif choose == "B":
        count = 1/(1+(10**((Ra-Rb)/400)))
        print(f"{count:.2f}")
main()
