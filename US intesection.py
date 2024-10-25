"""US Interstate Number System"""
def main():
    """main"""
    txt = str(int(input()))
    if len(txt) <= 2:
        if txt[-1] == "0" and int(txt):
            print("Horizontal Major Interstate")
            print(f"I-{int(txt)}")
        elif txt[-1] == "5":
            print("Vertical Major Interstate")
            print(f"I-{int(txt)}")
        else:
            print("Others")
    elif len(txt) == 3:
        if not int(txt[1:]):
            print("Others")
            return 0
        if not int(txt[0]) % 2 and txt[-1] in ("0" , "5"):
            print("Even Minor Interstate")
            print(f"I-{int(txt[1:])}")
        elif int(txt[0]) % 2 and txt[-1] in ("0" , "5"):
            print("Odd Minor Interstate")
            print(f"I-{int(txt[1:])}")
        else:
            print("Others")
    else:
        print("Others")
    return 0
main()
