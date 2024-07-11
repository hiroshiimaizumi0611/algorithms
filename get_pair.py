from typing import Optional, Tuple


def get_pair(numbers: list[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def get_pair_half_sum(numbers: list[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    half_sum, reminder = divmod(sum_numbers, 2)
    if reminder != 0:
        return

    cache = set()
    for num in numbers:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num


if __name__ == "__main__":
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    print(get_pair(l, t))
    print(get_pair_half_sum(l))
