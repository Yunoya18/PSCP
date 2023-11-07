"""TicTacToe"""
def main():
    """process"""
    board = [input() for _ in range(3)]
    check = False
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        win = board[0][0]
        check = True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        win = board[0][2]
        check = True
    else:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
                win = board[i][0]
                check = True
                break
            elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
                win = board[0][i]
                check = True
                break
    if check:
        print(win, "WIN")
    else:
        print("DRAW")

main()
