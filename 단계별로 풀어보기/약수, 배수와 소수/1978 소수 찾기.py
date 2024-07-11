n = int(input())
arr = list(map(int, input().split()))

# ver1
cnt = 0
for i in arr:
    if i > 1:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            cnt += 1
            
print(cnt)

# ver2
# result = 0
# for num in arr:
#     cnt = 0
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 cnt += 1
#         if cnt == 0:
#             result += 1
    
# print(result)

# ver3 
# for i in n:
#     for j in range(2, i+1):
#         if i % j == 0:
#             if i == j:
#                 cnt += 1
#             break

# print(cnt)
