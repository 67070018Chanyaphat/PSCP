"""Run Length Encoding"""
def encode():
    """encode for short form of text"""
    text = input()
    encoded_string = ""
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            i += 1
            count += 1
        encoded_string += str(count) + text[i]
        i += 1
    print(encoded_string)
encode()
