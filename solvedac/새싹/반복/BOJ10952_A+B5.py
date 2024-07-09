t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a == 0 & b == 0:
        break
    else: print(a+b)