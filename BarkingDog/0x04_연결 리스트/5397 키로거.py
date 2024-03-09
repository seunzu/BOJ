n = int(input())

for _ in range(n):
    data = input()
    left = []
    right = []
    for j in data:
        if j == "<":
            if left:
                right.append(left.pop())
        elif j == ">":
            if right:
                left.append(right.pop())
        elif j == "-":
            if left:
                left.pop()
        else:
            left.append(j)
    left.extend(reversed(right))
    print("".join(left))