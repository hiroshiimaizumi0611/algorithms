def generate_pascal_triangle(depth: int) -> list[list[int]]:
    data = [[1] * (i + 1) for i in range(depth)]
    for line in range(2, depth):
        for i in range(1, line):
            data[line][i] = data[line - 1][i - 1] + data[line - 1][i]
    return data


if __name__ == "__main__":
    for r in generate_pascal_triangle(5):
        print(r)
