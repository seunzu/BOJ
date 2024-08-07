from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while fire:
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if graph[nx][ny] != '#' and not f_time[nx][ny]:
                f_time[nx][ny] = f_time[x][y] + 1
                fire.append((nx, ny))
                
    while jihoon:
        x, y = jihoon.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return j_time[x][y]
            if graph[nx][ny] == "#" or j_time[nx][ny]:
                continue
            if not f_time[nx][ny] or f_time[nx][ny] > j_time[x][y] + 1:
                j_time[nx][ny] = j_time[x][y] + 1
                jihoon.append([nx, ny])
    return "IMPOSSIBLE"

r, c = map(int, input().split())
graph = [list(map(int, input())) for _ in range(r)]
jihoon = deque()
fire = deque()
f_time = [[0]*c for _ in range(r)]
j_time = [[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == "J":
            jihoon.append([i, j])
            j_time[i][j] = 1
        if graph[i][j] == "F":
            fire.append([i, j])
            f_time[i][j] = 1
            
print(bfs())