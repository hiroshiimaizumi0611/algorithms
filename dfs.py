import sys

sys.setrecursionlimit(10**6)

from collections import deque


def main():
    n, m = map(int, input().split())

    g = build_graph(n, m)

    seen = [False] * n
    k = 0
    for v in range(n):
        if seen[v]:
            continue

        dfs(v, seen, g)
        k += 1

    print(k - 1)


def build_graph(n: int, m: int):
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())

        a -= 1
        b -= 1

        g[a].append(b)
        g[b].append(a)

    return g


def dfs(st: int, seen: list[bool], g: list[list]):
    stack = list()
    stack.append(st)

    seen[st] = True

    while len(stack) != 0:
        v = stack.pop()

        seen[st] = True

        for nv in g[v]:
            if seen[nv]:
                continue

            seen[nv] = True
            stack.append(nv)


if __name__ == "__main__":
    main()


