# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기 찾아옴
# 일과 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명
# 아홉 명의 난쟁이 모두 자신이 일곱 난쟁이의 주인공이라고 주장
# 일곱 난쟁이의 키의 합 = 100

# 아홉 개의 줄에 걸쳐 난쟁이 키 주어짐
# 주어지는 키는 100을 넘지 않는 자연수, 아홉 난쟁이의 키는 모두 다름
# 가능한 정답이 여러 가지인 경우 아무거나 출력

# => 일곱 난쟁이의 키 오름차순 출력, 일곱 난쟁이 찾을 수 없는 경우 없음

# ver1
# 조합 combinations
# 9개 중에 7개 뽑기
from itertools import combinations

heights = [int(input()) for _ in range(9)]
for combi in combinations(heights, 7):
    if sum(combi) == 100:
        for height in sorted(combi):
            print(height)

        break

# ver2
# 9개 중에 2개 뽑기 -> 이중 반복문
heights = [int(input()) for _ in range(9)]
heights.sort()
tot = sum(heights)

def f():
    for i in range(8):
        for j in range(i + 1, 9):
            if tot - heights[i] - heights[j] == 100:
                for k in range(9):
                    if i != k and j != k:
                        print(heights[k])

                return


f()