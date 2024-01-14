import string
from typing import List, Sequence, Union


class Piece:
    BLACK = "X"
    WHITE = "O"
    EMPTY = "-"


class Board(object):
    """A board for Wu Zi Qi game"""

    def __init__(self, size: int) -> None:
        self.size: int = size
        self.state: List[List[str]] = [
            [Piece.EMPTY for _ in range(size)] for _ in range(size)
        ]

    def __str__(self) -> str:
        board: List[Sequence[Union[str, Piece]]] = [
            ["  "] + list(string.ascii_uppercase[0 : self.size])
        ]
        for i, row in enumerate(self.state):
            board.append(
                [str(i).ljust(2)] + [str(cell) for cell in row] + [str(i).ljust(2)]
            )
        board += [["  "] + list(string.ascii_uppercase[0 : self.size])]
        return "\n".join([" ".join(str(cell) for cell in row) for row in board])


b = Board(19)
print(b)
