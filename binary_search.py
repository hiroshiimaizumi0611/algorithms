def binary_search(a: list, key: int) -> bool:
    n = len(a)

    l = -1
    r = n

    while r - l > 1:
        m = (l + r) // 2

        if a[m] == key:
            return True

        if a[m] > key:
            r = m
        else:
            l = m

    return False


def main():
    a = [
        3,
        1,
        4,
        1,
        5,
        9,
        2,
        6,
        5,
    ]
    a.sort()

    key = 1
    print(binary_search(a, key))


if __name__ == "__main__":
    main()
