class UnionFind:

    def __init__(self, n: int):
        self.parent = [-1] * n
        self.rank = [1] * n

    def find(self, x: int):
        if self.parent[x] == -1:
            return x

        tmp = self.find(self.parent[x])
        self.parent[x] = tmp
        return tmp

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            x, y = y, x

        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1

        self.parent[x] = y


def main():
    n, q = map(int, input().split())

    uf = UnionFind(n)
    for _ in range(q):
        p, a, b = map(int, input().split())

        if p == 0:
            uf.union(a, b)

        if p == 1:
            if uf.find(a) == uf.find(b):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
