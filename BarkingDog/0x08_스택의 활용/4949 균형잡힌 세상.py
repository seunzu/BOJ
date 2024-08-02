while True:
    command = input()
    stack = []
    
    if command == '.':
        break
    
    for i in command:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
    
    print('no' if stack else 'yes')