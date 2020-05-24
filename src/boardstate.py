import numpy as np
from typing import Optional, List


def board_state_equals(myarr, list_arrays):
    return next((True for elem in list_arrays if np.array_equal(elem.board, myarr)), False)


def sign(x):
    return x and (1, -1)[x < 0]


class BoardState:
    def __init__(self, board: np.ndarray, current_player: int = 1):
        self.board: np.ndarray = board
        self.current_player: int = current_player

    def inverted(self) -> 'BoardState':
        return BoardState(board=self.board[::-1, ::-1] * -1, current_player=self.current_player * -1)

    def copy(self) -> 'BoardState':
        return BoardState(self.board.copy(), self.current_player)

    def do_move(self, from_x, from_y, to_x, to_y) -> Optional['BoardState']:
        """
        :return: new BoardState or None for invalid move
        """
        if from_x == to_x and from_y == to_y:
            return None

        if (to_x + to_y) % 2 == 0:
            return None

        result = self.copy()

        x_d = 1 if to_x > from_x else -1
        y_d = 1 if to_y > from_y else -1

        x_t = from_x + x_d
        y_t = from_y + y_d

        while x_t in range(from_x, to_x + x_d, x_d) and y_t in range(from_y, to_y + y_d, y_d):
            if sign(result.board[y_t, x_t]) == -sign(result.board[from_y, from_x]):
                result.board[y_t, x_t] = 0
            x_t += x_d
            y_t += y_d

        result.board[to_y, to_x] = result.board[from_y, from_x]
        result.board[from_y, from_x] = 0

        if board_state_equals(result.board, self.get_possible_moves()):
            return result

        return None
<<<<<<< Updated upstream
=======

    def steps3(self, x, y, a, b):
        new_board = self.copy()
        new_board.board[y + a, x + b] = new_board.board[y, x]
        new_board.board[y, x] = 0
        return new_board

    def steps4(self, x, y, a, b):
        new_board = self.copy()
        new_board.board[y + a, x + b] = 0
        if a > 0:
            if b > 0:
                new_board.board[y + a + 1, x + b + 1] = new_board.board[y, x]
            else:
                new_board.board[y + a + 1, x + b - 1] = new_board.board[y, x]
        elif a < 0:
            if b > 0:
                new_board.board[y + a - 1, x + b + 1] = new_board.board[y, x]
            else:
                new_board.board[y + a - 1, x + b - 1] = new_board.board[y, x]
        new_board.board[y, x] = 0
        return new_board
>>>>>>> Stashed changes

    def get_possible_moves(self) -> List['BoardState']:
        result = []
        for y in range(8):
            for x in range(8):
                if sign(self.board[y, x]) == self.current_player:
                    if abs(self.board[y, x]) == 1:
                        if y > 0:
                            if x > 0:
                                if self.board[y - 1, x - 1] == 0:
<<<<<<< Updated upstream
                                    new_board = self.copy()
                                    new_board.board[y - 1, x - 1] = new_board.board[y, x]
                                    new_board.board[y, x] = 0
                                    result += [new_board]
                                elif sign(self.board[y - 1, x - 1]) == -sign(self.board[y, x]) and y > 1 and x > 1 and self.board[y - 2, x - 2] == 0:
                                    new_board = self.copy()
                                    new_board.board[y - 1, x - 1] = 0
                                    new_board.board[y - 2, x - 2] = new_board.board[y, x]
                                    new_board.board[y, x] = 0
                                    result += [new_board]
                            if x < 7:
                                if self.board[y - 1, x + 1] == 0:
                                    new_board = self.copy()
                                    new_board.board[y - 1, x + 1] = new_board.board[y, x]
                                    new_board.board[y, x] = 0
                                    result += [new_board]
                                elif sign(self.board[y - 1, x + 1]) == -sign(self.board[y, x]) and y > 1 and x < 6 and self.board[y - 2, x + 2] == 0:
                                    new_board = self.copy()
                                    new_board.board[y - 1, x + 1] = 0
                                    new_board.board[y - 2, x + 2] = new_board.board[y, x]
                                    new_board.board[y, x] = 0
                                    result += [new_board]
                        if y < 7:
                            if x > 0:
                                if self.board[y + 1, x - 1] == 0:
                                    new_board = self.copy()
                                    new_board.board[y + 1, x - 1] = new_board.board[y, x]
                                    new_board.board[y, x] = 0
                                    result += [new_board]
                                elif sign(self.board[y + 1, x - 1]) == -sign(self.board[y, x]) and y < 6 and x > 1 and self.board[y + 2, x - 2] == 0:
                                    new_board = self.copy()
                                    new_board.board[y + 1, x - 1] = 0
                                    new_board.board[y + 2, x - 2] = new_board.board[y, x]
                                    new_board.board[y, x] = 0
                                    result += [new_board]
                            if x < 7:
                                if self.board[y + 1, x + 1] == 0:
                                    new_board = self.copy()
                                    new_board.board[y + 1, x + 1] = new_board.board[y, x]
                                    new_board.board[y, x] = 0
                                    result += [new_board]
                                elif sign(self.board[y + 1, x + 1]) == -sign(self.board[y, x]) and y < 6 and x < 6 and self.board[y + 2, x + 2] == 0:
                                    new_board = self.copy()
                                    new_board.board[y + 1, x + 1] = 0
                                    new_board.board[y + 2, x + 2] = new_board.board[y, x]
                                    new_board.board[y, x] = 0
                                    result += [new_board]
=======
                                    result += [self.steps3(self, x, y, -1, -1)]
                                elif sign(self.board[y - 1, x - 1]) == -sign(self.board[y, x]) and y > 1 and x > 1 and self.board[y - 2, x - 2] == 0:
                                    result += [self.steps4(self, x, y, -1, -1)]
                            if x < 7:
                                if self.board[y - 1, x + 1] == 0:
                                    result += [self.steps3(x, y, -1, 1)]
                                elif sign(self.board[y - 1, x + 1]) == -sign(self.board[y, x]) and y > 1 and x < 6 and self.board[y - 2, x + 2] == 0:
                                    result += [self.steps4(self, x, y, -1, 1)]
                        if y < 7:
                            if x > 0:
                                if self.board[y + 1, x - 1] == 0:
                                    result += [self.steps3(x, y, 1, -1)]
                                elif sign(self.board[y + 1, x - 1]) == -sign(self.board[y, x]) and y < 6 and x > 1 and self.board[y + 2, x - 2] == 0:
                                    result += [self.steps4(self, x, y, 1, -1)]
                            if x < 7:
                                if self.board[y + 1, x + 1] == 0:
                                    result += [self.steps3(x, y, 1, 1)]
                                elif sign(self.board[y + 1, x + 1]) == -sign(self.board[y, x]) and y < 6 and x < 6 and self.board[y + 2, x + 2] == 0:
                                    result += [self.steps4(self, x, y, 1, 1)]
>>>>>>> Stashed changes
                    elif abs(self.board[y, x]) == 2:
                        for i in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
                            y_t = y + i[0]
                            x_t = x + i[1]
                            deleted_pos = []
                            while y_t in range(8) and x_t in range(8):
                                new_board = self.copy()
                                if sign(new_board.board[y_t, x_t]) == -sign(new_board.board[y, x]):
                                    deleted_pos += [(y_t, x_t)]
                                elif new_board.board[y_t, x_t] == 0:
                                    for t in deleted_pos:
                                        new_board.board[t[0], t[1]] = 0
                                    new_board.board[y_t, x_t] = new_board.board[y, x]
                                    new_board.board[y, x] = 0
                                    result += [new_board]
                                else:
                                    break
                                y_t += i[0]
                                x_t += i[1]

        return result

    @property
    def is_game_finished(self) -> bool:
        return not np.any(self.board < 0) or not np.any(self.board > 0)


    @property
    def get_winner(self) -> Optional[int]:
        if self.is_game_finished:
            return 0 if np.any(self.board < 0) else 1
        return None

    @staticmethod
    def initial_state() -> 'BoardState':
        board = np.zeros(shape=(8, 8), dtype=np.int8)

        board[7, 0] = 1  # шашка первого игрока
        board[6, 1] = 2  # дамка первого игрока
        board[0, 1] = -1  # шашка противника

        return BoardState(board, 1)
