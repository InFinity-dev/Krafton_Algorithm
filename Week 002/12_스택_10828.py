import sys

# alias 지정
input = sys.stdin.readline

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]
    # push
    if order == "push":
        value = word[1]
        stack.append(value)
    # pop
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # size
    elif order == "size":
        print(len(stack))
    # empty
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # order가 top이라면
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
