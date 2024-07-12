import sys

t = int(input())

for _ in  range(t):
    command = sys.stdin.readline()
    vps = []
    
    for j in command:
        if j == '(':
            vps.append(j)
        elif j == ')':
            if command:
                vps.pop()
            else:
                print('NO')
                break
    else:
        print('NO') if vps else print('YES')