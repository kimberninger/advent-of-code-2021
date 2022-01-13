from abc import ABC, abstractmethod
from importlib.resources import open_text, read_text
from pathlib import Path
from typing import TextIO


class PuzzleInput(ABC):
    @abstractmethod
    def read_content(self) -> str:
        pass

    @abstractmethod
    def open(self) -> TextIO:
        pass

    def read_lines(self) -> list[str]:
        with self.open() as task_input:
            return [line.rstrip("\n") for line in task_input]


class ResourcePuzzleInput(PuzzleInput):
    def __init__(self, day_number: int):
        self.resource_package = f"aoc2021.resources.day{day_number:02}"

    def read_content(self) -> str:
        return read_text(self.resource_package, "input.txt")

    def open(self) -> TextIO:
        return open_text(self.resource_package, "input.txt")


class FilePuzzleInput(PuzzleInput):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read_content(self) -> str:
        return self.file_path.read_text()

    def open(self) -> TextIO:
        return self.file_path.open()
