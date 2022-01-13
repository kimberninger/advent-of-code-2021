from abc import ABC, abstractmethod

from ..io import PuzzleInput


class Puzzle(ABC):
    def __init__(self, puzzle_input: PuzzleInput):
        self.puzzle_input = puzzle_input
        super().__init__()

    @abstractmethod
    def solve(self):
        pass
