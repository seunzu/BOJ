# 방향이 없는 그래프 주어졌을 때, 연결 요소(Connected Component)의 개수를 구하는 프로그램
# -> 무방향 그래프 = 양방향 그래프
# 첫째 줄: 정점의 개수 N과 간선의 개수 M (1 <= N <= 1,000, 0 <= M <= N*(N-1)/2)
# -> 인접행렬 NC2 = N*(N-1)/2
# 둘째 줄: M개의 줄에 간선의 양 끝점 u와 v (1 <= u, v <= N, u != v)

# dfs
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

# for row in adj:
#     print(row)

ans = 0 # 연결 요소 개수
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        # adj[now][nxt] = True -> 현재 노드 now와 다음 노드 nxt 사이 간선 존재
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)