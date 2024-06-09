from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def main():
    h, w = map(int, input().split())
    sy, sx = map(lambda x: int(x) - 1, input().split())
    gy, gx = map(lambda x: int(x) - 1, input().split())

    grid = [input() for _ in range(h)]

    INF = 1001001001
    dist = [[INF] * w for _ in range(h)]
    dist[sy][sx] = 0

    q = deque()
    q.append((sy, sx))

    while len(q) > 0:
        y, x = q.popleft()

        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue

            if grid[ny][nx] == "#":
                continue

            if dist[ny][nx] != INF:
                continue

            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

    print(dist[gy][gx])

if __name__ == "__main__":
    main()
