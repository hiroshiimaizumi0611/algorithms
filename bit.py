def main():
    n, x = map(int(input().split()))
    a = list(map(int, input().split()))

    for i in range(1 << n):
        use = [False] * n

        for j in range(n):
            if i & (1 << n):
                use[j] = True

        total = 0
        for j in range(n):
            if use[j]:
                total += a[j]

        if total == x:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
