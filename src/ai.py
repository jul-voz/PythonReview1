from typing import Optional

from .boardstate import BoardState

import numpy as np
import random


class PositionEvaluation:
    def __call__(self, board: BoardState, depth: int) -> float:
        value = 10101010100110
        if depth == 0:
            value = 0
            for x in range(8):
                value += x + np.sum(board.board[x])
            return value
        else:
            b = board.copy()
            b.current_player *= -1
            moves = b.get_possible_moves()
            for i in moves:
                value = min(value, self(i, depth - 1) * b.current_player)
            return value


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
