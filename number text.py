"""Number Message"""
def main():
    """print the resl meaning of the text"""
    text = input()
    lenght = len(text)
    index = 0
    new_txt = ""
    while index < lenght:
        if text[index:index+2] == "13":
            new_txt += "B"
            index += 1
        elif text[index:index+2] == "12":
            new_txt += "R"
            index += 1
        elif text[index] == "1":
            new_txt += "I"
        elif text[index] == "3":
            new_txt += "E"
        elif text[index] == "4":
            new_txt += "A"
        elif text[index] == "5":
            new_txt += "S"
        elif text[index] == "0":
            new_txt += "O"
        elif text[index].isalpha() or text[index].isspace():
            new_txt += text[index]
        index += 1
    print(new_txt.upper())
main()
