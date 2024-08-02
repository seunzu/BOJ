# rotate(1): R 이동/ rotate(-1): L 이동
from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dq = deque(range(1, n+1))
cnt = 0

for i in nums:
    while True:
        if i == dq[0]:
            dq.popleft()
            break
        else:
            if dq.index(i) <= len(dq) // 2:
                dq.rotate(-1) # dq.append(dq.popleft())
                cnt += 1
            else:
                dq.rotate(1) # dq.appendleft(dq.pop())
                cnt += 1

print(cnt)