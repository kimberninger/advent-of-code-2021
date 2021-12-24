from ast import literal_eval as read_list
from functools import reduce
from operator import add

from .snailfish import SnailfishNumber


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as input_file:
        resulting_number = reduce(
            add, (SnailfishNumber.from_list(read_list(line)) for line in input_file.readlines())
        )
        print(resulting_number.magnitude)
