# Kruskal 알고리즘
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
Vroot = [i for i in range(V + 1)]
print(Vroot)
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))

Elist.sort(key=lambda x: x[2])
print(f'정렬된 Elist : {Elist}')


def find(x):
    print(f'{x}에 대한 루트노드 찾는 중')
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
        print(f'>>> 재귀 호출된 {Vroot[x]}')
    return Vroot[x]


answer = 0
for s, e, w in Elist:
    print(f'Elist 의 {s}, {e}, {w} 받아옴')
    sRoot = find(s)
    print(f'{s}의 루트 노드는 {sRoot}')
    eRoot = find(e)
    print(f'{e}의 루트 노드는 {eRoot}')
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        print(f'경로 비용  {w} 추가')
        answer += w

print(Vroot)
print(answer)

# # Prim 알고리즘
# import sys
# import heapq
# input = sys.stdin.readline
#
# V, E = map(int, input().split())
# visited = [False]*(V+1)
# Elist = [[] for _ in range(V+1)]
# heap = [[0, 1]]
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     Elist[s].append([w, e])
#     Elist[e].append([w, s])
#
# answer = 0
# cnt = 0
# while heap:
#     if cnt == V:
#         break
#     w, s = heapq.heappop(heap)
#     if not visited[s]:
#         visited[s] = True
#         answer += w
#         cnt += 1
#         for i in Elist[s]:
#             heapq.heappush(heap, i)
#
# print(answer)
