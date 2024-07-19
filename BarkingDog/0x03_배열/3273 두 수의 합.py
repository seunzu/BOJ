import sys

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0

# ai + aj = x -> (ai, aj) 개수
# 투 포인터 -> 시간 복잡도 O(n)
# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] + arr[j] == x:
#             cnt += 1
#         if arr[i] + arr[j] > x:
#             break

# 이중 for문 -> 시간 복잡도 O(n^2)
left = 0
right = n-1

while left < right:
    tmp = arr[left] + arr[right]
    if tmp == x:
        cnt += 1
        left += 1
    elif tmp > x:
        right -= 1
    else:
        left += 1

print(cnt)