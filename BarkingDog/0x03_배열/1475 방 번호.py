n = int(input())
arr = [0 for _ in range(10)]

# ver 1
for i in str(n):
    if i == "9" or i == "6":
        if arr[6] == arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[int(i)] += 1

print(max(arr))

# ver 2
while n > 0:
    arr[n % 10] += 1
    n //= 10

answer = 0
for i in range(10):
    if i == 6 or i == 9:
        continue
    answer = max(answer, arr[i])

answer = max(answer, (arr[6] + arr[9] + 1) // 2)
print(answer)

