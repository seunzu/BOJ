n, m = map(int, input().split())
a, b = [], []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    c = []
    for j in range(m):
        c.append(a[i][j] + b[i][j])
    print(*c)