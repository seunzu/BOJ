arr = input()
stack = []
tmp = 1
answer = 0

for i in range(len(arr)):
    if arr[i] == '(':
        tmp *= 2
        stack.append(arr[i])
    elif arr[i] == '[':
        stack.append(arr[i])
        tmp *= 3
    elif arr[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if arr[i - 1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if arr[i - 1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3

print(0 if stack else answer)