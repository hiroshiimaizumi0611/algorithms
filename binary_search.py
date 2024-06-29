def linear_serch(numbers: list[int], value: int) -> int:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


# def binary_search(numbers: list, value: int) -> int:
#     left, right = 0, len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == value:
#             return mid
#         elif numbers[mid] < value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


def binary_search(numbers: list, value: int) -> int:
    def recursive(numbers: list[int], value: int, left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return recursive(numbers, value, mid + 1, right)
        else:
            return recursive(numbers, value, left, mid - 1)

    return recursive(numbers, value, 0, len(numbers) - 1)


if __name__ == "__main__":
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    print("index num = " + str(binary_search(nums, 15)))
