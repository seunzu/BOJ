num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
n, b = n[::-1], int(b)
result = 0

for i, j in enumerate(n):
    result += (b**i)*(num_list.index(j))
print(result)


