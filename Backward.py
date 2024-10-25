"""backward"""
def backward():
    """append word and ruturn backward"""
    word_list = []
    while True:
        word = input()
        if word != "NULL":
            word_list.append(word)
        else:
            break
    for i in word_list[-1::-1]:
        print(i)
backward()
