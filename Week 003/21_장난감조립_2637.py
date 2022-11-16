import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 부품 수
graph = [[] for _ in range(n + 1)]  # 연결 관계
inDegree = [0 for _ in range(n + 1)]  # 진입차수
# inDegree = [0] * (n + 1)
requires = [[0] * (n + 1) for _ in range(n + 1)]  # 필요량 배수, (n+1)x(n+1) 정사각행렬

q = deque()

for _ in range(int(input())):  # M 입력
    x, y, k = map(int, input().split())
    graph[y].append((x, k))  # y는 x에게 필요, k개 만큼
    inDegree[x] += 1

for i in range(1, n + 1):
    if inDegree[i] == 0:  # 진입 차수가 0이면
        q.append(i)

while q:  # q가 비어있지 않는 동안
    cursor = q.popleft()
    for target_product, target_require in graph[cursor]:
        if requires[cursor].count(0) == n + 1:
            requires[target_product][cursor] += target_require
        else:
            for i in range(1, n + 1):
                requires[target_product][i] += requires[cursor][i] * target_require

        inDegree[target_product] -= 1

        if inDegree[target_product] == 0:
            q.append(target_product)

# print(f'requires[n] = {requires[n]}')

for p in range(len(requires[n])):
    if requires[n][p] > 0:
        num = requires[n][p]
        print(p, num)

# for p in enumerate(requires[n]):
#     if p[1] > 0:
#         print(*p)

