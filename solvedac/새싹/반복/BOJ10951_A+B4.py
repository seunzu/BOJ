# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# EOF 자동으로 처리
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)