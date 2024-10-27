from abc import ABC, abstractmethod
from enum import Enum

import numpy as np


class Piece(Enum):
    WHITE_KING = 0
    WHITE_QUEEN = 1
    WHITE_ROOK = 2
    WHITE_BISHOP = 3
    WHITE_KNIGHT = 4
    WHITE_PAWN = 5
    BLACK_KING = 6
    BLACK_QUEEN = 7
    BLACK_ROOK = 8
    BLACK_BISHOP = 9
    BLACK_KNIGHT = 10
    BLACK_PAWN = 11


class BasePiece(ABC):
    """Base piece class"""

    def __init__(self, position, is_white: bool):
        self.pos = position
        self.is_white = is_white

    @abstractmethod
    def move(self, board, new_location) -> None:
        pass

    @abstractmethod
    def get_moves(self, board) -> list[np.ndarray]:
        pass


class Pawn(BasePiece):
    def __init__(self, position, is_white):
        super().__init__(position, is_white)
        self.has_moved = False

    def get_moves(self, board) -> list[np.ndarray]:
        y, x = self.pos
        direction = +1 if self.is_white else -1
        enemy_pieces = board.get_black_pieces() if self.is_white else board.get_white_pieces()

        moves = []
        if enemy_pieces[y + direction, x + 1] is not 0:
            moves.append([y + direction, x + 1])
        if enemy_pieces[y + direction, x - 1] is not 0:
            moves.append([y + direction, x - 1])
        if self.has_moved:
            moves.append([y + (2 * direction), x])
