import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
dq = deque()

for _ in range(n):
    command = input().split()
    
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        print(-1 if not dq else dq.popleft())
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        print(1 if not dq else 0)
    elif command[0] == 'front':
        print(-1 if not dq else dq[0])
    elif command[0] == 'back':
        print(-1 if not dq else dq[-1])