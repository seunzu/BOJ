import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

nums_sort = sorted(list(set(nums)))

numsdict = {}
for i in range(len(nums_sort)):
    numsdict[nums_sort[i]] = i
    
for i in nums:
    print(numsdict[i], end=' ')