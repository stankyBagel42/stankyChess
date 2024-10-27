import numpy as np


class Board:
    def __init__(self):
        self.state = np.zeros((8, 8, 12))
        self.moves = []

    def get_black_pieces(self):
        return self.state[:, :, 6:11].sum(axis=2)

    def get_white_pieces(self):
        return self.state[:, :, 0:5].sum(axis=2)

    # TODO: "Is Check" function, pawn promotion+en-passant, castling (Can-castle func, king+rook inp)
