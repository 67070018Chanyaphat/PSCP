"""for ball"""
def where_ball():
    """Find the final position of the ball after the swaps."""
    play = input()
    position = 1
    ###################
    for move in play:
        if move == 'A':
            if position == 1:
                position = 2
            elif position == 2:
                position = 1
        elif move == 'B':
            if position == 2:
                position = 3
            elif position == 3:
                position = 2
        elif move == 'C':
            if position == 1:
                position = 3
            elif position == 3:
                position = 1
    print(position)
where_ball()
