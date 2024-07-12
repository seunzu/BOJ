while True:
    command = input()

    if command == '.': 
        break
    
    stack = []
    for i in command:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
            
    print('no') if stack else print('yes')