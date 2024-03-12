import sys

n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
sb = []
current_num = 1

for num in sequence:
    while current_num <= num:
        stack.append(current_num)
        sb.append("+\n")
        current_num += 1

    if stack and stack[-1] == num:
        stack.pop()
        sb.append("-\n")
    else:
        print("NO")
        sys.exit()

print("".join(sb))
