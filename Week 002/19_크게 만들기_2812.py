import sys

# alias 지정
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(input())
t, stack = k, []

for i in range(n):
    while t > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        t -= 1
    stack.append(num[i])

print(''.join(stack[:n - k]))
