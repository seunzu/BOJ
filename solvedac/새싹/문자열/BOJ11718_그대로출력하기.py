# while True:
#     try:
#         print(input())
#     except EOFError:
#         break

import sys

for line in sys.stdin.readlines():
    print(line.rstrip())