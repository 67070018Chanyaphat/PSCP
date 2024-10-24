"""Roman"""
def main():
    """Roman"""
    romanvalue = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman = input()
    ans = 0
    for i, j in enumerate(roman):
        if i == len(roman)-1:
            ans += romanvalue[j]
        elif romanvalue[j] >= romanvalue[roman[i+1]]:
            ans += romanvalue[j]
        else:
            ans -= romanvalue[j]
    print(ans)
main()
