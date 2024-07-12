from collections import deque

n = int(input())
standing = deque(map(int, input().split()))
stack = []
target = 1

while standing:
    if standing[0] == target:
        standing.popleft()
        target += 1
    else:
        stack.append(standing.popleft())
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break

print('Nice' if not stack else 'No')