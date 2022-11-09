import sys

# alias 지정
input = sys.stdin.readline

n = int(input())  # 탑의 개수
tower = list(map(int, input().split()))  # 탑 리스트
stack = []
received = []

for idx in range(n):
    while stack:
        if stack[-1][1] > tower[idx]:  # 레이져 수신 가능
            received.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        received.append(0)
    stack.append([idx, tower[idx]])  # 인덱스, 값

print(*received)
