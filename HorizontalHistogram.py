"""HorizontalHistogram"""
def sortans(var):
    """Sort"""
    char = var[0]
    return ord(char) + (100 if char.isupper() else 0)

def main(string):
    """HorizontalHistogram"""
    for char, count in sorted({i: string.count(i) for i in string}.items(), key=sortans):
        print(char, ":", "".join(["-" if i % 5 else "-|" for i in range(1, count+1)]).rstrip("|"))
main(input())
