# 숫자 카드는 정수 하나가 적혀져 있는 카드, 상근이는 숫자 카드 N개를 가지고 있음
# => 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지 구하는 프로그램 작성
#
# 첫째 줄: 상근이가 가지고 있는 숫자 카드의 개수 N(1 <= N <= 500,000)
# 둘째 줄: 숫자 카드에 적혀 있는 정수 주어짐(-10,000,000 <= 적힌 수 <= 10,000,000)
# 두 숫자 카드에 같은 수가 적혀 있는 경우 없음
# 셋째 줄: M(1 <= M <= 500,000)
# 넷째 줄: 상근이가 가지고 있는 숫자 카드인지 아닌지 구해야할 M개의 정수
# , 공백으로 구분(-10,000,000 <= M <= 10,000,000)

# 첫째 줄 입력으로 주어진 M개의 수에 대해
# 각 수가 적힌 숫자 카드 상근이가 가지고 있으면 1, 아니면 0 공백으로 구분 출력

# 이분탐색
from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(map(int, input().split()))
# print(cards)
M = int(input())
qry = list(map(int, input().split()))
ans = []
for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    # print(l, r)
    ans.append(1 if r - 1 else 0) # ans.append(1 if r - 1 > 0 else 0)

print(' '.join(map(str, ans))) # print(*ans)