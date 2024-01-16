# 피보나치 수는 0과 1로 시작
# 0번째 피보나치 수: 0, 1번째 피보나치 수: 1, 그 다음 2번째부터는 바로 앞 두 피보나치 수의 합
# -> F_n = F_{n-1} + F_{n-2} (n >= 2)
# ex. n = 17 -> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
#
# => n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램 작성
#
# 첫째 줄: n (n <= 90, 자연수)

# Top-down
# 피보나치 수열
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     return f(n - 1) + f(n - 2)
#
# print(f(int(input())))

# 메모이제이션
cache = [-1] * 91 # 길이 91인 리스트 만들고, 초기값 -1로 설정
cache[0] = 0
cache[1] = 1
# cnt = 0

def f(n):
    # global cnt

    # cnt += 1
    if cache[n] == -1: # 만약 피보나치 수가 아직 계산되지 않았다면,
        cache[n] = f(n - 1) + f(n - 2)

    return cache[n]

print(f(int(input())))
# print(f'cnt: {cnt}')

# Bottom up
# 반복문
# N = int(input())
# cache = [-1] * 91
# cache[0] = 0
# cache[1] = 1
#
# for i in range(2, N + 1):
#     cache[i] = cache[i - 1] + cache[i - 2]
#
# print(cache[N])