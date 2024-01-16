# 자연수 N과 정수 K가 주어졌을 때 이항 계수를 10,007로 나눈 나머지를 구하는 프로그램
#
# 첫째 줄: N과 K 주어짐 (1 <= N <= 1,000, 0 <= K <= N)

# import sys
#
# MOD = 10007
# sys.setrecursionlimit(10 ** 7)
#
# N, K = map(int, input().split())
#
# def bino(n, k):
#     if k == 0 or k == n:
#         return 1
#
#     return bino(n - 1, k - 1) + bino(n - 1, k)
#
# print(bino(N, K))

# 메모이제이션 적용O
import sys
#
# MOD = 10007
# sys.setrecursionlimit(10 ** 7)
#
# cache = [[0] * 1001 for _ in range(1001)]
# N, K = map(int, input().split())
#
# def bino(n, k):
#     if cache[n][k]:
#         return  cache[n][k]
#
#     if k == 0 or k == n:
#         cache[n][k] = 1
#     else:
#         cache[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)
#         cache[n][k] %= MOD # 값 10007미만 초과 방지
#
#     return cache[n][k]
#
# print(bino(N, K))

# bottom-up
# 반복문(이중for문)
MOD = 10007

cache = [[0] * 1001 for _ in range(1001)]
N, K = map(int, input().split())

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD

# for i in range(7):
#     print(cache[i])

# print()
print(cache[N][K])


