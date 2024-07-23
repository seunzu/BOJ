import sys

input = sys.stdin.readline
# # 시간 복잡도: O(N)
# s = list(input())
# n = int(input())
# cursor = len(s)
#
# for i in range(n):
#     command = input().split()
#
#     if command[0] == "L" and cursor > 0:
#         cursor -= 1
#     elif command[0] == "D" and cursor < len(s):
#         cursor += 1
#     elif command[0] == "B" and cursor > 0:
#         s.pop(cursor-1)
#         cursor -= 1
#     elif command[0] == "P":
#         s.insert(cursor, command[1])
#         cursor += 1
#
# for i in range(len(s)):
#     print(s[i], end="")

# 시간 복잡도: O(1)
left = list(input())
right = []

for _ in range(int(input())):
    command = sys.stdin.readline().split()

    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print(*left, *reversed(right), sep='')