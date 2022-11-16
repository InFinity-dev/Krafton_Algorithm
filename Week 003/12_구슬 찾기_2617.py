import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, True))
    graph[b].append((a, False))


def bfs(start):
    dq = deque()
    chk_heavier, chk_lighter = set(), set()
    dq.append((start, False))
    dq.append((start, True))
    while dq:
        node, s = dq.popleft()
        if len(chk_heavier) > n // 2 or len(chk_lighter) > n // 2:
            return 1
        for n_n, n_s in graph[node]:
            if (n_n not in chk_heavier) and (n_n not in chk_lighter):
                if (not s) and (not n_s):
                    dq.append((n_n, n_s))
                    chk_heavier.add(n_n)
                elif s and n_s:
                    dq.append((n_n, n_s))
                    chk_lighter.add(n_n)
    return 0


count = 0
for i in range(1, n + 1):
    count += bfs(i)
print(count)
