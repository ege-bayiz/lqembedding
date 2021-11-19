# This is a sample Python script.
from tic_tac_toe import Board
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    board = Board(4,4,3)
    input_type = "coordinate"

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
