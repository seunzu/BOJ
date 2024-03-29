# 국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것
# 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해주기는 어려울 수도 있음
#
# -> 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정
# 1. 모든 요청이 배정될 수 있는 경우: 요청한 금액 그대로 배정
# 2. 모든 요청이 배정될 수 없는 경우: 특정한 정수 상한액을 계산
# 그 이상인 예산요청에는 모두 상한액 배정,상한액 이하의 예산 요청에 대해서는 요청한 금액 그대로 배정
#
# ex. 전체 국가예산: 485, 4개의 지방 예산요청: 120, 110, 140, 150
# 상한액: 127 -> 배정: 120, 110, 127, 127 => 합: 484 가능한 최대
#
# => 어려 지방의 예산 요청과 국가예산의 총액이 주어졌을 때, 위의 조건 모두 만족 예산 배정하는 프로그램
#
# 첫째 줄: 지방 수 의미하는 정수 N (3 <= N <= 10,000)
# 다음 줄: 각 지방의 예산 요청 표현하는 N개의 정수가 빈칸을 사이에 두고 주어짐 (1 <= 값 <= 100,000)
# 그 다음 줄: 총 예산을 나타내는 정수 M (N <= M <= 1,000,000,000)

# 파라메트릭 서치
N = int(input())
req = list(map(int, input().split()))
M = int(input())

lo = 0
hi = max(req)
mid = (lo + hi) // 2
ans = 0

def is_possible(mid):
    return sum(min(r, mid) for r in req) <= M

while lo <= hi:
    # print(f'lo: {lo}, mid: {mid}, hi: {hi}, ans: {ans}')
    if is_possible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1

    mid = (lo + hi) // 2

print(ans)