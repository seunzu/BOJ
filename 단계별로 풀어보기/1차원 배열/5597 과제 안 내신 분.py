students = [i for i in range(1, 31)]

for i in range(28):
    n = int(input())
    students.remove(n)

print(min(students))
print(max(students))
