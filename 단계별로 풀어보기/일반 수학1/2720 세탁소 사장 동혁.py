changes = [25, 10, 5, 1]
T = int(input())

for _ in range(T):
    c = int(input())
    res = []

    for i in changes:
        res.append(c // i)
        c = c % i

    print(*res)



