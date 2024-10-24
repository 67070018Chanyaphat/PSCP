"""black jack"""
def play_blackjack():
    """cal score to play"""
    num_card = int(input())
    card1 = input()
    card2 = input()
    score_totall = 0
    def check(a):
        if a in ("J","K","Q"):
            a = 10
        elif a == "A":
            a = 11
        elif a in ("1","2","3","4","5","6","7","8","9","10"):
            a = int(a)
        return a
    if num_card == 2:
        score = check(card1)+check(card2)
        if score>21:
            score-=10
        else:
            score+=0
    elif num_card == 3:
        card3 = input()
        score = check(card1)+check(card2)+check(card3)
        while score > 21:
            if card1 == "A" or card2 == "A" or card3 == "A":
                score-=10
            else:
                break
    score_totall = score
    print(score_totall)

play_blackjack()
