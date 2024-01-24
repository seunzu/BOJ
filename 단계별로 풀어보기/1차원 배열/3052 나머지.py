numList = []

for i in range(10):
    n = int(input()) % 42
    if n not in numList:
        numList.append(n)
print(len(numList))