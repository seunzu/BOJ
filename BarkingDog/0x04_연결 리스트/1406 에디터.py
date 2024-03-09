import sys
text = list(input())
M = int(input())
curser = []

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == "L" and text:
        curser.append(text.pop())
    elif command[0] == "D" and curser:
        text.append(curser.pop())
    elif command[0] == "B" and text:
        text.pop()
    elif command[0] == 'P':
        text.append(command[1])

answer = text + curser[::-1]
print(''.join(answer))
