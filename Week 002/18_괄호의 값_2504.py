import sys

# alias 지정
input = sys.stdin.readline

stack = []  # 스택
temp = 1  # result에 더해주기 전 임시 변수
result = 0  # 결과 변수
n = list(input())  # 입력값

for i in range(len(n)):
    if n[i] == '(':
        temp *= 2
        stack.append(n[i])

    elif n[i] == '[':
        temp *= 3
        stack.append(n[i])

    elif n[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if n[i - 1] == '(':
            result += temp
        temp //= 2
        stack.pop()

    elif n[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if n[i - 1] == '[':
            result += temp
        temp //= 3
        stack.pop()

# 결과 출력
if stack:
    print(0)
else:
    print(result)
