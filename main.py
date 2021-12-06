
from tic_tac_toe import Board

def main():
    board = Board(3,3,3)
    # states_map, inv_states_map = board.get_game_states()
    #
    # print(states_map)

    input_type = "numpad" \
                 ""

    while not board.game_over:
        board.draw()
        if input_type == "coordinate":
            row = int(input("Enter row:"))
            col = int(input("Enter column:"))
        elif input_type == "numpad":
            num = int(input("Enter move:"))
            if num == 7:
                row = 0
                col = 0
            elif num == 8:
                row = 0
                col = 1
            elif num == 9:
                row = 0
                col = 2
            elif num == 4:
                row = 1
                col = 0
            elif num == 5:
                row = 1
                col = 1
            elif num == 6:
                row = 1
                col = 2
            elif num == 1:
                row = 2
                col = 0
            elif num == 2:
                row = 2
                col = 1
            elif num == 3:
                row = 2
                col = 2
            else:
                print("invalid input")
                continue

        board.play_move(row, col)

    board.draw()
    if board.winner is not None:
        print(board.winner + " won.")
    else:
        print("It's a draw.")
