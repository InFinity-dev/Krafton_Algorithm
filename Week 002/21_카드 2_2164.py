import sys
from collections import deque

# alias 지정
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    queue.append(i + 1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())
