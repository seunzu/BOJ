n = list(input())
num = [0] * 10

for i in n:
    if i == '6' or i == '9':
        # 둘 중 작은 것에 추가
        if num[6] <= num[9]:
            num[6] += 1
        else:
            num[9] += 1
    else: 
        num[i] += 1
        
print(max(num))