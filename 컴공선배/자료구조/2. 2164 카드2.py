# N장의 카드
# 1~N까지의 번호가 붙어 있음_1번 카드-제일 위/ N번 카드-제일 아래 순서대로 카드가 놓여 있음
# 다음과 같은 동작 카드가 한 장 남을 때까지 반복
# 1. 제일 위에 있는 카드 바닥에 버림
# 2. 그 다음 제일 위에 있는 카드를 제일 아래 있는 카드 밑으로 옮김

# ex. N=4 카드 제일 위에서부터 1234 순서
# 1. 1을 바닥에 버림
# 2. 2를 제일 아래로 옮김 => 342
# 3. 3을 버림
# 4. 4를 밑으로 옮김 => 24
# 5. 2를 버림 => 남는 카드: 4

# => N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하기

# ver1
# 배열(Array)
# 맨 앞 값 삭제, 맨 앞의 값 맨 뒤로 보내기(삭제, 삽입)
# O(N), N <= 500,000 => (N-1)*3*O(N) => O(N^2)
N = int(input())
arr = [*range(1, N + 1)]
# for i in range(1, N + 1):
#     arr.append(i)
while len(arr) > 1:
    arr.pop(0)
    arr.append(arr.pop(0))

print(arr.pop())

# ver2
# 큐(Queue)
from collections import deque

N = int(input())
dq = deque(range(1, N + 1))  # 1, 2, 3, ... , N
# for i in range(1, N + 1):
#     dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.popleft())