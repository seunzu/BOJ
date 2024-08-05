from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs (x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]  
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
total_count = 0
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            total_count += 1
            ans = max(bfs(i, j), ans)
    

print(total_count)
print(ans)