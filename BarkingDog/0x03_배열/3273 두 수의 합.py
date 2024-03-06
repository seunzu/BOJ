n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

# 투 포인터
left, right = 0, n - 1
cnt = 0

while left < right:
    tmp = arr[left] + arr[right]
    if tmp == x:
        cnt += 1
        left += 1
    elif tmp < x:
        left += 1
    else:
        right -= 1

print(cnt)