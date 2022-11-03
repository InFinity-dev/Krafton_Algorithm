import sys
import itertools
input = sys.stdin.readline

def solve(n):
    nums = [1, 2, 3]
    cnt = 0
    for i in range(1, n+1):
        li = itertools.product(nums, repeat=i)
        for l in li:
            if sum(l) == n:
                cnt += 1
    print(cnt)

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)