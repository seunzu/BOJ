# 1. 배열에 정수 x(x!=0)를 넣음
# 2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거
# 절댓값이 가장 작은 값이 여러 개 -> 가장 작은 수 출력, 그 값을 배열에서 제거
# => 프로그램은 처음에 비어있는 배열에서 시작

# 첫째 줄: 연산의 개수 N
# 다음 N개의 줄: 연산에 대한 정보 나타내는 정수 x
# x!=0 -> 배열에 x라는 값을 넣는(추가하는) 연산
# x=0 -> 배열에서 절댓값이 가장 작은 값 출력, 그 값을 배열에서 제거
# 배열 비어 있는 경우 절댓값이 가장 작은 값 출력 -> 0 출력

# ver1
# 우선순위 큐(min-Heap)에 튜플
import heapq as hq
import sys

N = int(input())
pq = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(pq, (abs(x), x)) # 튜플(절댓값, 원본값)
    else:
        print(hq.heappop(pq)[1] if pq else 0)

# ver2
# 우선순위 큐 힙 2개
import heapq as hq
import sys

N = int(input())
min_heap = [] # 최소힙, 1, 2, 3, 4, 5, 6, ... 원본값이 작으면 절대값도 작음 -> 양수
max_heap = [] # 최대힙, -1, -4, -10, ... 절대값이 작을수록 큼 -> 음수
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        if x > 0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)