n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    stack = []
    
    for i in word:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if not stack: 
        cnt += 1

print(cnt)