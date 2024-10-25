"""Cat parade"""
def main():
    """Cat Parade"""
    cats = []
    saipan = []
    while True:
        word = input()
        if word == "END":
            break
        if word != "IT'S A DOG":
            for cat in word.split(","):
                cats.append(cat.strip())
                if not saipan.count(cat.strip()):
                    saipan.append(cat.strip())
        elif word == "IT'S A DOG":
            cats.pop()
            saipan.pop()

    saipan.sort()
    for cat in saipan:
        print(cat, cats.index(cat) + 1, cats.count(cat))

main()
