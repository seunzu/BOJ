import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    data = input()
    left = []
    right = []

    for i in data:
        if i == "<" and left:
            right.append(left.pop())
        elif i == ">" and right:
            left.append(right.pop())
        elif i == "-" and left:
            left.pop()
        else:
            left.append(i)

    left.extend(reversed(right))
    print("".join(left))