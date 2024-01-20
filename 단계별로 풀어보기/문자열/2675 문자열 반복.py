t = int(input())

for i in range(0, t):
    r, s = input().split()
    r = int(r)
    s = str(s)
    for j in range(len(s)):
        print(r*s[j], end='')
    print()

# for i in range(t):
#     r, s = input().split()
#     for j in s:
#         print(j*int(r), end='')
#     print()