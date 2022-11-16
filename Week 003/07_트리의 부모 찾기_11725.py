import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())  # 노드의 개수

# 트리
Tree = [[] for _ in range(N + 1)]

# 부모 노드 저장
Parents = [0 for _ in range(N + 1)]

# 트리 구조 입력
for _ in range(N - 1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)


def dfs(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


dfs(1, Tree, Parents)

for i in range(2, N + 1):
    print(Parents[i])
