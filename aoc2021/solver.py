from pkg_resources import resource_string


def main():
    print(resource_string("aoc2021.resources.day01", "input.txt"))
