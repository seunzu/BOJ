# reverse()의 시간복잡도: O(N)
# sys.stdin.readline -> 마지막에 개행 문자(\n) 포함 => strip()로 공백 문자 제거
from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    nums = deque(input()[1:-1].split(','))

    if n == 0:
        nums = []
        
    flag = 0
        
    for i in p:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if len(nums) == 0:
                print('error')
                break
            else:
                if flag % 2 == 0:
                    nums.popleft()
                else:
                    nums.pop()
            
    else:
        if flag % 2 == 1:
            nums.reverse()
        print('[' + ','.join(nums) + ']')