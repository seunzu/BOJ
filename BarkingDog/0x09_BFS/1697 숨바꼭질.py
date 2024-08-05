from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x):
    queue = deque()
    queue.append(x)
    
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for i in (x-1, x+1, x*2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

MAX = 10 ** 5
n, k = map(int, input().split())
visited = [0] * (MAX + 1)

print(bfs(n))