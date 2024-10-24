"""MissingCard"""
def main():
    """MissingCard I"""
    card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    havecard = []
    for i in card:
        havecard.append(i+"S")
        havecard.append(i+"H")
        havecard.append(i+"D")
        havecard.append(i+"C")
    for i in range(51):
        miss = input()
        if miss in havecard:
            havecard.remove(miss)
    print(havecard[0])
main()
