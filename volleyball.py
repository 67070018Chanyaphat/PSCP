"""Volleyball"""
def main():
    """Volleyball"""
    match_score = input()
    game_set = 1
    a_win = 0
    b_win = 0
    a_score = 0
    b_score = 0
    finished = False
    for m in match_score:
        if m == "A":
            a_score += 1
        else:
            b_score += 1
        winning_threshold = 25
        if game_set == 5:
            winning_threshold = 15
        if a_score >= winning_threshold and a_score - b_score >= 2:
            a_win += 1
        elif b_score >= winning_threshold and b_score - a_score >= 2:
            b_win += 1
        else:
            continue
        print(f"Set {game_set}: A ({a_score}) | B ({b_score})")
        game_set += 1
        a_score = 0
        b_score = 0
        if a_win == 3:
            print(f"A won {a_win}:{b_win} set")
            finished = True
        elif b_win == 3:
            print(f"B won {b_win}:{a_win} set")
            finished = True
    if not finished:
        print(f"Set {game_set}: A ({a_score}) | B ({b_score})")
        print("The game has not finished yet.")
main()
