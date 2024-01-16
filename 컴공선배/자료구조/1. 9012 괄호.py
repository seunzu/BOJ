# 괄호 문자열(Parenthesis String, PS): 두 개의 괄호 기호로 구성된 문자열
# 올바른 괄호 문자열(Valid PS, VPS): 괄호 모양이 바르게 구성된 문자열
# 기본 VPS: 한 쌍의 괄호 기호로 된 문자열
#
# 만일 x가 VPS라면 이것을 하나의 괄호에 넣은 새로운 문자열 "(x)"도 VPS가 된다
# 두 VPS x와 y를 접합(concatenatoin)시킨 새로운 문자열 xy도 VPS가 된다
# ex. "(())()"와 "((()))"는 VPS 이지만, "(()(", "(())()))" 그리고 "(()"는 모두 VPS가 아닌 문자열
#
# => 입력으로 주어진 괄호 문자열이 VPS인지 아닌지 판단 -> 결과를 YES/NO로 나타냄

# 스택(Stack)
# ver1
T = int(input())
for _ in range(T):
    stk = []
    isVPS = True
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else:
            # == stk:
            if len(stk) > 0:
                stk.pop()
            else:
                isVPS = False
                break

    if stk:
        isVPS = False

    print('YES' if isVPS else 'NO')

#ver2
t = int(input())
for _ in range(t):
    stk = []
    s = input()
    isVPS = True

    for ch in s:
        if ch == '(':
            stk.append('(')
        if ch == ')':
            if stk:
                stk.pop()
            elif not stk:
                isVPS = False
                break
    if not stk and isVPS:
        print('YES')
    elif stk or not isVPS:
        print('NO')