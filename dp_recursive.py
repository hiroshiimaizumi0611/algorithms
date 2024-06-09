import sys

sys.setrecursionlimit(10**6)


def main():

    def rec(i):
        if dp[i] != -1:
            return dp[i]

        if i == 0:
            return 0

        if i == 1:
            return abs(h[i] - h[0])

        result = min(
            rec(i - 1) + abs(h[i] - h[i - 1]),
            rec(i - 2) + abs(h[i] - h[i - 2]),
        )

        dp[i] = result

        return result

    n = int(input())
    h = list(map(int, input().split()))
    dp = [-1] * n

    print(rec(n - 1))


if __name__ == "__main__":
    main()
