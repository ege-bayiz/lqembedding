import colorama
from collections import deque

class Board():
    def __init__(self, m: int = 3, n: int = 3, k: int = 3):
        self.p1moves = list()
        self.p2moves = list()
        self.m = m  #num of rows
        self.n = n  #num of columns
        self.k = k  #winning number (k-in-a-row wins the game)
        self.winner = None
        self.winning_cells = []
        self.game_over = False
        self.update_game_over()
        self.turn = "p1"
        self.round = 0
        colorama.init()
        colorama.deinit()

    def copy(self):
        b = Board(self.m, self.n, self.k)
        b.p1moves = self.p1moves.copy()
        b.p2moves = self.p2moves.copy()
        b.winner = self.winner
        b.game_over = self.game_over
        b.turn = self.turn
        b.round = self.round
        return b

    def draw(self):
        colorama.reinit()
        for row in range(self.m):
            s = ""
            for col in range(self.n):
                if (row, col) in self.p1moves:
                    if self.game_over and (row, col) in self.winning_cells:
                        s = s + " " + colorama.Fore.YELLOW + colorama.Style.BRIGHT + "X" + colorama.Style.RESET_ALL + " "
                    else:
                        s = s + colorama.Fore.GREEN + " X " + colorama.Fore.RESET

                elif (row, col) in self.p2moves:
                    if self.game_over and (row, col) in self.winning_cells:
                        s = s + " " + colorama.Fore.YELLOW + colorama.Style.BRIGHT + "O" + colorama.Style.RESET_ALL + " "
                    else:
                        s = s + colorama.Fore.RED + " O " + colorama.Fore.RESET
                else:
                    s = s + "   "
                if col < self.n - 1:
                    s = s +"|"
            print(s)
            if row < self.m - 1:
                hline = "---"
                for i in range(self.n - 1):
                    hline += "+---"
                print(hline)
        colorama.deinit()

    def play_move(self, row, col):
        assert not self.game_over
        assert self.has_empty_slot_at(row, col)
        if self.turn == "p1":
            self.p1moves.append((row, col))
            self.turn = "p2"
        else:
            self.p2moves.append((row, col))
            self.turn = "p1"
            self.round += 1
        self.update_game_over()

    """
    If game is over and sets self.winner to the winning player (sets self.winner = None if game draws) and 
    sets self.game_over to True. If game is not over, sets self.game_over to False.
    """
    def update_game_over(self):
        # checking winning condition in rows
        if self.k <= self.n:
            for row in range(self.m):
                start_cols = range(self.n - self.k + 1)
                for start in start_cols:
                    if all([(row, start + offset) in self.p1moves for offset in range(self.k)]):
                        self.winning_cells = [(row, start + offset) for offset in range(self.k)]
                        self.game_over = True
                        self.winner = "p1"
                        return
                    elif all([(row, start + offset) in self.p2moves for offset in range(self.k)]):
                        self.winning_cells = [(row, start + offset) for offset in range(self.k)]
                        self.game_over = True
                        self.winner = "p2"
                        return


        # checking winning condition in columns
        if self.k <= self.m:
            for col in range(self.n):
                start_rows = range(self.m - self.k + 1)
                for start in start_rows:
                    if all([(start + offset, col) in self.p1moves for offset in range(self.k)]):
                        self.winning_cells = [(start + offset, col) for offset in range(self.k)]
                        self.game_over = True
                        self.winner = "p1"
                        return
                    elif all([(start + offset, col) in self.p2moves for offset in range(self.k)]):
                        self.winning_cells = [(start + offset, col) for offset in range(self.k)]
                        self.game_over = True
                        self.winner = "p2"
                        return

        # checking winning condition in diagonals (-45 degrees)
        if self.k <= self.m and self.k <= self.n:
            start_cols = range(self.n - self.k + 1)
            start_rows = range(self.m - self.k + 1)
            for col in start_cols:
                for row in start_rows:
                    if all([(row + offset, col + offset) in self.p1moves for offset in range(self.k)]):
                        self.winning_cells = [(row + offset, col + offset) for offset in range(self.k)]
                        self.game_over = True
                        self.winner = "p1"
                        return
                    elif all([(row + offset, col + offset) in self.p2moves for offset in range(self.k)]):
                        self.winning_cells = [(row + offset, col + offset) for offset in range(self.k)]
                        self.game_over = True
                        self.winner = "p2"
                        return

        # checking winning condition in diagonals (+45 degrees)
        if self.k <= self.m and self.k <= self.n:
            start_cols = range(self.n - self.k + 1)
            start_rows = range(self.m - self.k, self.m)
            for col in start_cols:
                for row in start_rows:
                    if all([(row - offset, col + offset) in self.p1moves for offset in range(self.k)]):
                        self.winning_cells = [(row - offset, col + offset) for offset in range(self.k)]
                        self.game_over = True
                        self.winner = "p1"
                        return
                    elif all([(row - offset, col + offset) in self.p2moves for offset in range(self.k)]):
                        self.winning_cells = [(row - offset, col + offset) for offset in range(self.k)]
                        self.game_over = True
                        self.winner = "p2"
                        return

        # checking for draws
        if not any([self.has_empty_slot_at(row, col) for row in range(self.m) for col in range(self.n)]):
            self.game_over = True
            self.winner = None
            return

        self.game_over = False
        return

    def has_empty_slot_at(self, row, col):
        if (row,col) in self.p1moves or (row,col) in self.p2moves:
            return False
        if row >= self.m or col >= self.n:
            return False
        if row < 0 or col < 0:
            return False
        return True

    def equivalent_to(self, other):
        if self.p1moves == other.p1moves and self.p2moves == other.p2moves:
            return True
        return False

    def get_available_move_list(self):
        moves = list()
        for row in range(self.m):
            for col in range(self.n):
                if (row, col) not in self.p1moves and (row, col) not in self.p2moves:
                    moves.append((row, col))

        return moves

"""
    def get_game_states(self):
        states_map = dict() #maps index to state
        inv_states_map = dict() #maps state to index


        stack = deque()
        board = Board(self.m, self.n, self.k)
        stack.append(board)
        idx = 0
        states_map[idx] = (list(board.p1moves), list(board.p2moves))
        inv_states_map[(board.p1moves, board.p2moves)] = idx

        while not len(stack) == 0:
            b = stack.pop()
            for row in range(self.m):
                for col in range(self.n):
                    if b.has_empty_slot_at(row, col) and not b.game_over:
                        b_new = b.copy()
                        if (b_new.p1moves, b_new.p2moves) in inv_states_map:
                            b_new.play_move(row, col)
                            stack.append(b_new)
                            idx += 1

                            states_map[idx] = b_new
                            inv_states_map[b_new] = idx

        return states_map, inv_states_map
"""

