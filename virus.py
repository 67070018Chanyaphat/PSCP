"""virus"""
def help_check():
    """virus check head"""
    virus = input()
    virus_bad = 0
    for i in virus:
        if i == "o":
            virus_bad+=1
    print(virus_bad)
help_check()
