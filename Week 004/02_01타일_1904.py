import sys

input = sys.stdin.readline

cache = [0] * 1000001

n = int(input())

cache[0] = 0
cache[1] = 1
cache[2] = 2

for i in range(3,n+1):
    cache[i] = (cache[i-2] + cache[i-1]) % 15746

print(cache[n])
