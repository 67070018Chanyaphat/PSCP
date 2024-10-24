"""are you used to listened the song xoxo from somi"""
def check_winner(board):
    """Check the winner of the OX game."""
    # ตรวจสอบแถว
    for row in board:
        if row == "XXX":
            return "X WIN"
        if row == "OOO":
            return "O WIN"

    # ตรวจสอบคอลัมน์
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == "X":
            return "X WIN"
        if board[0][col] == board[1][col] == board[2][col] == "O":
            return "O WIN"

    # ตรวจสอบแนวทแยง
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return "X WIN"
        if board[0][0] == "O":
            return "O WIN"

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return "X WIN"
        if board[0][2] == "O":
            return "O WIN"

    # ถ้าไม่มีผู้ชนะ
    return "DRAW"

def main():

    """Main function to run the OX game check."""
    board = [input().strip() for _ in range(3)]
    result = check_winner(board)
    print(result)

if __name__ == "__main__":
    main()
