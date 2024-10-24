"""Seeker"""
def main():
    """Seeker"""
    word = input()
    tmp = ""
    ans = 0
    for i in word:
        if i.isdigit():
            tmp += i
        else:
            if not tmp:
                ans += 0
            else:
                ans += int(tmp)
                tmp = ""
    if tmp.isdigit():
        print(ans+int(tmp))
    else:
        print(ans)
main()
