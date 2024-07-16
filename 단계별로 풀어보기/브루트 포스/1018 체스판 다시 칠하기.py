n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = []

# 8x8 크기 체스판 검사 -> 전체 보드판 인덱스 벗어나지 X
# i + 7 < n => i < n - 7
for i in range(n - 7):
    for j in range(m - 7):
        # 시작점 바뀔 때마다 처음부터 칠해줌
        draw1 = 0 # 시작: 검은색
        draw2 = 0 # 시작: 흰색
        
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    # 왼쪽 위 모서리가 검은색(B)인 경우
                    # draw1가 검은색이 아닐 때 1 더해서 칠해줌
                    if board[a][b] != 'B': 
                        draw1 += 1
                    # 왼쪽 위 모서리가 흰색(W)인 경우
                    # draw2가 흰색이 아닐 때 1을 더해서 칠해줌 
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    # 왼쪽 위 모서리가 검은색(B)인 경우
                    if board[a][b] != 'W':
                        draw1 += 1
                    # 왼쪽 위 모서리가 흰색(W)인 경우
                    if board[a][b] != 'B':
                        draw2 += 1
        
        result.append(draw1)
        result.append(draw2)
        
print(min(result))
