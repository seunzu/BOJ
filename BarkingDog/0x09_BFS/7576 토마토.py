from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()

ans = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans - 1)
