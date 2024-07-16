n = int(input())
students = list(map(int, input().split()))
tmp = []
target = 1

for i in students:
    tmp.append(i)
    # 스택 비어 있지 x, 스택의 마지막 학생 번호 == 현재 기대 번호
    while tmp and tmp[-1] == target:
        tmp.pop()
        target += 1
    
print("Sad" if tmp else "Nice")
