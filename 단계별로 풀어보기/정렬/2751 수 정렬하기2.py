import sys

n = int(input())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

for i in arr:
    print(i)