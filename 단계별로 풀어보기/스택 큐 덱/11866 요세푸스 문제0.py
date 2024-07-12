import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, n+1)])
result = []

while dq:
    for i in range(k-1):
        dq.append(dq.popleft())
    result.append(str(dq.popleft()))

print('<' + ', '.join(result), ">", sep="")