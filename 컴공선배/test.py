t = int(input())

for i in range(1, t):
    n = int(input())
    l = sorted(list(map(int, input().split())))

    print('#%d' % i, end='')
    for j in range(n):
        print(l[j], end=' ')
    print()


