from typing import Optional

from .boardstate import BoardState

import numpy as np
import random


class PositionEvaluation:
<<<<<<< Updated upstream
    def __call__(self, board: BoardState, depth: int) -> float:
        value = 10101010100110
        if depth == 0:
            value = 0
            for x in range(8):
                value += x + np.sum(board.board[x])
            return value
=======
    def changed(self, board):
        temp = 0
        for x in range(8):
            for y in range(8):
                temp += board.board[y, x]
                if abs(board.board[y, x]) == 2:
                    temp += (board.board[y, x] // 2)
        return temp

    def __call__(self, board: BoardState, depth: int, color) -> float:
        value = 0
        if depth == 0:
            return self.changed(board)
>>>>>>> Stashed changes
        else:
            b = board.copy()
            b.current_player *= -1
            moves = b.get_possible_moves()
            for i in moves:
<<<<<<< Updated upstream
                value = min(value, self(i, depth - 1) * b.current_player)
            return value
=======
                value = max(value * board.current_player, self.__call__(i, depth - 1) * board.current_player)
                return value
>>>>>>> Stashed changes


class AI:
    def __init__(self, position_evaluation: PositionEvaluation, search_depth: int):
        self.position_evaluation: PositionEvaluation = position_evaluation
        self.depth: int = search_depth

    def next_move(self, board: BoardState) -> Optional[BoardState]:
        moves = board.get_possible_moves()
        random.shuffle(moves)
        if len(moves) == 0:
            return None
        return max(moves, key=lambda b: self.position_evaluation(b, self.depth) * b.current_player)
