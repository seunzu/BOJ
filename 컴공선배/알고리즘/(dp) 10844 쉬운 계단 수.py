# 45656이란 수를 보면 인접한 모든 자리의 차이가 1
# -> 계단 수
#
# => N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하기
# 0으로 시작하는 수는 계단 수가 아님
# -> 1 ~ 8: +1/-1, 0: +1, 9: -1
# 첫째 줄: N (1 <= N <= 100, 자연수)
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지 출력
# -> f(n, d): 길이가 n이고 마지막 숫자가 d인 계단수 개수
# (f(n, 0) + f(n, 1) + ... + f(n, 9)) % MOD
# -> f(n, d) = f(n-1, d-1)  + f(n-1,d+1)
#               (d > 0)         (d < 9)
# f(1, 1~9) = 1, f(1, 0) = 0

MOD = 1_000_000_000

# cache[n][d]: 길이가 n이고 마지막 숫자가 d인 계단수 개수
cache = [[0] * 10 for _ in range(101)]
for j in range(1, 10):
    cache[1][j] = 1

for i in range(2, 101):
    for j in range(10):
        if j > 0:
            cache[i][j] += cache[i - 1][j - 1]
            cache[i][j] %= MOD
        if j < 9:
            cache[i][j] += cache[i - 1][j + 1]
            cache[i][j] %= MOD

ans = 0
N = int(input())
for j in range(10):
    ans += cache[N][j]
    ans %= MOD

print(ans)

