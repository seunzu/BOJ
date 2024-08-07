from collections import deque

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

def bfs (x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + nx[i];
            ny = y + ny[i];
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                
    
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
        
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    
    print(cnt)