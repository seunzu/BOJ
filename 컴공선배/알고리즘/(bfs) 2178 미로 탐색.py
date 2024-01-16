# N*M크기의 배열로 표현되는 미로
# 미로에서 1: 이동할 수 있는 칸, 0: 이동할 수 없는 칸 나타냄
# => (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수 구하는 프로그램
# 칸을 셀 때는 시작 위치와 도착 위치도 포함
# -> 전형적인 길찾기 문제 => 최단거리: bfs
# 첫째 줄: 두 정수 N, M(2 <= N, M <= 100)
# 다음 N개의 줄: M개의 정수로 미로 주어짐
# 각각의 수 붙어서 입력으로 주어짐

# bfs
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N, M = map(int, input().split())
board = [input() for _ in range(N)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        y, x, d = dq.popleft()

        if y == N - 1 and x == M - 1:
            return d

        nd = d + 1
        for k in range(4):
            ny = y + dy[k] # 처음 좌표 + 상대 좌표
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))

print(bfs())