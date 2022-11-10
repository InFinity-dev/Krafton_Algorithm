import heapq
import sys

# alias 지정
input = sys.stdin.readline

n = int(input())
card = []
for c in range(n):
    heapq.heappush(card, int(input()))

cnt = 0

if len(card) == 1:
    print(cnt)

else:
    while len(card) > 1:
        min_1 = heapq.heappop(card)
        min_2 = heapq.heappop(card)
        cnt += min_1 + min_2
        heapq.heappush(card, min_1 + min_2)

    print(cnt)
