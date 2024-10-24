"""decode"""
import math
def decode():
    """decode text"""
    text = input()
    decoder = ""
    for i in range(len(text)):
        if text[i].isnumeric():
            decoder+=((text[i+1])*(math.floor(int(text[i]))))
    print(math.ceil(1.5)) 
decode()
