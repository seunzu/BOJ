# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나눠져 있는 MxN 크기의 보드 찾음
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있음
# 이 보드를 잘라서 8x8 크기의 체스판으로 만들려고 함
# -> (N-7)(N-7)
# 체스판 검은색, 흰색 번갈아서 칠해져 있어야 함
# -> 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있음
# => 체스판을 칠하는 경우는 2가지뿐 - 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우
#
# 보드가 체스판처럼 칠해져 있다는 보장이 없음
# -> 8x8 크기의 체스판으로 잘라낸 후 몇 개의 정사각형 다시 칠해야 함
# 8x8 크기는 아무데서나 골라도 됨
#
# => 다시 칠해야 하는 정사각형의 최소 개수 구하는 프로그램
#
# 첫째 줄: N과 M ( 8 <= N, M <= 50, 자연수 )
# 둘째 줄: N개의 줄에는 보드의 각 행의 상태 주어짐
# B: 검은색, W: 흰색

N, M = map(int, input().split())
board = [input() for _ in range(N)]
ans = 64

def fill(y, x, bw):
    global ans
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                if board[y + i][x + j] == bw:
                    cnt +=1
            else:
                if board[y + i][x + j] != bw:
                    cnt += 1

    ans = min(ans, cnt)

for i in range(N - 7):
    for j in range(M - 7):
        fill(i, j, 'B')
        fill(i, j, 'W')

print(ans)