n = int(input())

for i in range(n):
    result = i + sum(map(int, str(i)))
    if result == n:
        print(i)
        break
else:
    print(0)