"""Squid Game 3 - Tug-of-War"""
def die_survived():
    """cal who team will die from score"""
    teamA = 0
    teamB = 0
    for i in range(1,21):
        force = int(input())
        if i <= 10:
            teamA += force
        else:
            teamB += force
    if teamA > teamB:
        print("B")
    elif teamA < teamB:
        print("A")
    else:
        print("AB")
die_survived()
