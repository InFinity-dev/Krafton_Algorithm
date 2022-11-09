import sys

# alias 지정
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = []  # 괄호 쌍을 저장하는 스택 선언
    a = input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:  # 스택에 괄호가 없을경우
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
