# N개의 도시, 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스
# A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화시키려고 함
# 도시의 번호는 1부터 N까지
# input)
# 첫째줄 : 도시의 개수 N
# 둘째줄 : 버스의 개수 M
# 출발 도시의 번호 | 도착 도시의 번호 | 버스 비용
# 마지막줄 : 구하고자 하는 구간 출발점의 도시번호 | 도착점의 도시 번호

# 다익스트라(Dijkstra) 알고리즘

import heapq
from sys import maxsize
import sys

input = sys.stdin.readline

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

graph = [[] for _ in range(n + 1)]
cost_minimum = [maxsize] * (n + 1)  # start 도시에서 각 도시까지의 최소 비용 저장
for _ in range(m):
    departure, arrival, bus_num = map(int, input().split())
    graph[departure].append((bus_num, arrival))

start_city, end_city = map(int, input().split())


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    cost_minimum[start] = 0

    while pq:
        cost, start = heapq.heappop(pq)

        if cost_minimum[start] < cost:
            continue

        for next_cost, next_city in graph[start]:
            new_cost = cost + next_cost

            if cost_minimum[next_city] > new_cost:
                heapq.heappush(pq, (new_cost, next_city))
                cost_minimum[next_city] = new_cost


dijkstra(start_city)
print(cost_minimum[end_city])
