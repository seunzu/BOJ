# 준규가 가지고 있는 동전은 총 N종류, 각각의 동전 매우 많이 가지고 있음
# 동전 적절히 사용해ㅓㅅ 그 가치의 합을 K로 만들려고 함
# 이때 필요한 동전 개수 최솟값 구하는 프로그램

# 첫째 줄: N, K ( 1 <= N <= 10, 1 <= K <= 100,000,000)
# -> K원을 만드는데 필요한 동전 개수의 최솟값 출력
# 둘째 줄: N개의 줄에 동전의 가치 A_j가 오름차순으로 주어짐
# 1 <= A_i <= 1,000,000, A_1 = 1, i >=2 인 경우에는 A_i는 A_(i-1)

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0

for coin in coins:
    ans += K // coin
    K %= coin

print(ans)