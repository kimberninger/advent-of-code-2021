from ..io import PuzzleInput, ResourcePuzzleInput
from ..puzzles.day01.day01 import Part1, Part2


def main():
    puzzle_input: PuzzleInput = ResourcePuzzleInput(1)
    print(Part2(puzzle_input).solve())
