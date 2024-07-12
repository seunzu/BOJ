n = int(input())
nums = []

for _ in range(n):
    nums.append(list(map(int, input().split())))

nums.sort(key=lambda x: (x[1], x[0]))

for i in nums:
    print(i[0], i[1])
