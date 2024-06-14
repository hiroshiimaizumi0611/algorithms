def main():

    def check(n):
        price = a * n + b * len(str(n))
        return price <= x

    a, b, x = map(int, input().split())

    ok = 0
    ng = 10**9 + 1

    while ng - ok > 1:

        mid = (ok + ng) // 2

        if check(mid):  # midが買える
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()
