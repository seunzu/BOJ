# 1 7 19 37
# 1/ 1+6*1/ 7+6*2/ 19+6*3

n = int(input())
num = 1
cnt = 1

while n > num:
    num += 6 * cnt
    cnt += 1
    
print(cnt)