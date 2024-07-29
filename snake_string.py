def snake_string_v1(chars: str) -> list[list[str]]:
    result = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1
    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
    return result


if __name__ == "__main__":
    numbers = [str(i) for j in range(5) for i in range(10)]
    strings = "".join(numbers)
    for line in snake_string_v1(strings):
        print("".join(line))
