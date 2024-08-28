import random


def generate_triagnle_list(depth: int, max_num: int) -> list[list[int]]:
    return [[random.randint(0, max_num) for _ in range(i)] for i in range(1, depth + 1)]


def print_triangle(data: list[list[int]]) -> None:
    max_digit = len(str(max([max(l) for l in data])))
    width = max_digit + (max_digit % 2) + 2
    for index, line in enumerate(data):
        numbers = "".join([str(i).center(width, " ") for i in line])
        print(" " * int(width / 2) * (len(data) - index), numbers)

def sum_min_path(triangle: list[list[int]]) -> int:
    pass

if __name__ == "__main__":
    data = generate_triagnle_list(5, 20)
    print(data)
    print_triangle(data)
