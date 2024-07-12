import sys
from collections import deque

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

m = int(input())
c = list(map(int, sys.stdin.readline().split()))

queuestack = deque([])
for i in range(n):
    if a[i] == 0:
        queuestack.append(b[i])

for i in range(m):
    queuestack.appendleft(c[i])
    print(queuestack.pop(), end=' ')
