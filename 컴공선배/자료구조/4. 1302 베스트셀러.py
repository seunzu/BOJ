# 김형택은 탑문고의 직원이고 계산대에서 계산을 하는 직원
# 그날 근무가 끝난 후, 오늘 판매한 책을 보며 가장 많이 팔린 책의 제목을 칠판에 써놓는 일

# 오늘 하루 동안 팔린 책의 제목이 입력 -> 가장 많이 팔린 책의 제목을  출력하는 프로그램

# 첫째 줄: 오늘 하루 동안 팔린 책의 개수 N
# 둘째 줄 ~ N개 줄: 책의 제목이 들어옴(알파벳 소문자)

# 가장 많이 팔린 책 여러 개 -> 사전 순 가장 앞서는 제목

# 딕셔너리(dictionary)
d = dict()
for _ in range(int(input())):
    book = input()
    if book in d: # 딕셔너리에 해당 책 존재
        d[book] += 1
    else: # 딕셔너리에 해당 책 존재 X
        d[book] = 1


m = max(d.values()) # 가장 많이 팔린 권수
candi = []
for k, v in d.items():
    if v == m:
        candi.append(k)

# print(sorted(candi)[0])
candi.sort()
print(candi[0])
