if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        numbers = list(map(int, input_file.readlines()))
        solution = sum(
            1
            for n1, n2 in zip(numbers[1:], numbers[:-1])
            if n1 > n2
        )
        print(solution)
