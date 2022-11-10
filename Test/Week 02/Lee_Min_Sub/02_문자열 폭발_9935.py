# 문자열 폭발 : 폭발 문자열은 문자열에서 사라짐. 남은 문자열을 순서대로 이어붙여 새로운 문자열 생성.
# 폭발 문자열은 같은 문자를 두개이상 포함 하지 않는다.
# 남아있는 문자가 없는 경우에는 FRULA를 출력

import sys

# alias 지정
input = sys.stdin.readline

string = list(input().strip())
c4 = list(input().strip())

stack = []  # 스택 선언

for i in range(len(string)):
    stack.append(string[i]) # 입력받은 문자열에서 앞글자 부터 하나씩 받아옴

    if stack[-len(c4):] == c4:  # 받아 올때 마다 체크 if 스택에 폭발 문자열이 있다면
        for k in range(len(c4)): # 폭발 문자열 길이 만큼 pop
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
