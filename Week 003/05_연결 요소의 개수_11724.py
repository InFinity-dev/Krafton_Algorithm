# 무방향 그래프에서 연결 요소의 개수를 구하는 프로그램 -> 단절 그래프 총 개수
# input line 1) 정점의 개수 N, 간선의 개수 M
# input line 2) M개의 줄에 간선의 양끝점 u,v
# output) 연결 요소의 개수 출력
import sys

sys.setrecursionlimit(10000)
# alias 지정
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
