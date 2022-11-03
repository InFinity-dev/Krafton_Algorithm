import sys
import itertools
input = sys.stdin.readline

n, s = map(int, input().split())
li = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    sub = itertools.combinations(li, i)
    for sq in sub:
        if sum(sq) == s:
            cnt += 1

print(cnt)