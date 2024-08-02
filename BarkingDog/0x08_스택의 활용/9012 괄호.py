t = int(input())

for _ in range(t):
    ps = input()
    stack = []
    
    for i in ps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    
    else:
        print("NO" if stack else "YES")