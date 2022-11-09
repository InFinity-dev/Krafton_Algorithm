import sys

# alias 지정
input = sys.stdin.readline

n = int(input())

stk = []

for i in range(n):
    num = int(input())
    # pop
    if num == 0:
        stk.pop()
    # push
    else:
        stk.append(num)

print(sum(stk))
