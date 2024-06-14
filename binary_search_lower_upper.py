def lower_bound(a: list, key: int) -> int:

    n = len(a)

    ng = -1
    ok = n

    while ok - ng > 1:
        mid = (ok + ng) // 2

        if a[mid] >= key:
            ok = mid
        else:
            ng = mid

    return ok


def upper_bound(a: list, key: int) -> int:

    n = len(a)

    ng = -1
    ok = n

    while ok - ng > 1:
        mid = (ok + ng) // 2

        if a[mid] > key:
            ok = mid
        else:
            ng = mid

    return ok


def main():

    key = 5
    a = [2, 2, 5, 5, 9]  # sorted

    print(lower_bound(a, key))
    print(upper_bound(a, key))


if __name__ == "__main__":
    main()
