# deque를 사용하기 위해
from collections import deque

N, M, K, X = map(int, input().split())

# 편하게 도시 1 부터 확인하기위해 그래프 0번째 칸은 빈칸으로 생성
graph = [[] for _ in range(N + 1)]

# 도로의 개수(M)번 도로의 연결 정보를 받아 graph에 삽입
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
# 예제 입력 1 기준 아래와 같이 그래프 생성
# [ [], [2, 3], [3, 4], [], []]

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N + 1)  # 방문하지 않은 도시는 -1
distance[X] = 0  # 출발 도시(X)는 0으로 설정

# BFS(너비우선 탐색) 을 위해 deque()를 사용
queue = deque()
queue.append(X)

# queue가 빌 때까지 반복
while queue:

    now = queue.popleft()  # now 에는 1이 담기고 queue는 비게 됨

    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_nod in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_nod] == -1:
            # 최단 거리 갱신
            # 현재 도시와 출발 도시 사이의 거리 + 1
            distance[next_nod] = distance[now] + 1
            queue.append(next_nod)

# 출발 도시로 부터의 최단 거리가 K인 도시가 존재하지 않는다면
# -1을 출력하기위해 check 변수를 False로 초기화
check = False

for i in range(1, N + 1):
    # 도시들간에 최단 거리를 확인하여 K와 동일하면 그 도시를 출력
    if distance[i] == K:
        print(i)
        # 최단거리가 K인 도시가 존재한다면 check를 True로 바꿔주어
        # -1이 출력되지 않도록 함.
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if not check:
    print(-1)
