import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque(enumerate(map(int, input().split())))
ans = []

while dq:
    idx, paper = dq.popleft()
    ans.append(idx + 1)

    if paper > 0:
        dq.rotate(-(paper - 1))
    elif paper < 0:
        dq.rotate(-paper)

print(*ans, end=' ')