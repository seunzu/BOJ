import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = list(map(int, sys.stdin.readline().split()))
    
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        print(stack.pop()) if stack else print(-1)
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        print(1) if len(stack) == 0 else print(0)
    else:
        print(stack[-1]) if stack else print(-1)