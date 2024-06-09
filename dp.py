def main():
    n = int(input())
    h = list(map(int, input().split()))

    dp = [0] * n

    for i in range(n):
        if i == 0:
            continue

        if i == 1:
            dp[1] = abs(h[0] - h[1])
            continue

        dp[i] = min(
            dp[i - 1] + abs(h[i - 1] - h[i]),
            dp[i - 2] + abs(h[i - 2] - h[i]),
        )

    print(dp[n - 1])


if __name__ == "__main__":
    main()
