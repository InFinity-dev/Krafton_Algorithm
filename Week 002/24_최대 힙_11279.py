# 부모 노드의 값이 자식 노드의 값보다 큰 자료구조
import sys
import heapq

# alias 지정
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -num)
