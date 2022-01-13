from ...solver import Puzzle

window_size = 3


class Part1(Puzzle):
    def solve(self) -> str:
        numbers = list(map(int, self.puzzle_input.read_lines()))
        return str(sum(1 for n1, n2 in zip(numbers[1:], numbers[:-1]) if n1 > n2))


class Part2(Puzzle):
    def solve(self) -> str:
        numbers = list(map(int, self.puzzle_input.read_lines()))
        return str(sum(1 for n1, n2 in zip(numbers[window_size:], numbers[:-window_size]) if n1 > n2))
