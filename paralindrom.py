"""Palindrome"""
def main():
    """main"""
    count = int(input())
    txt = input()
    while count > 0 :
        last = str(int(txt[-2:]) + 1)
        hour = txt[:2].replace(":" , "")
        if not int(last) % 60 and int(last):
            last = "00"
            hour = str(int(hour) + 1)
        hour = str(int(hour) % 24)
        if int(last) < 10 and int(last):
            last = "0" + last
        txt = hour + ":" + last
        if int(txt.replace(":" , "")) == int(txt[::-1].replace(":" , "")):
            print(txt)
            count -= 1
main()
