from pathlib import Path

from .measurements import count_larger_measurements

if __name__ == "__main__":
    input_path: Path = Path(__file__).parent / "input.txt"
    with open(input_path, encoding="utf8") as input_file:
        measurements = list(map(int, input_file.readlines()))
        print(count_larger_measurements(measurements))
