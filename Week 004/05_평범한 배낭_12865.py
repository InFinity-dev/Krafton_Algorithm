import sys


input = sys.stdin.readline

n, k = map(int, input().split())
thing_w_v = [[0, 0]]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):
    thing_w_v.append((list(map(int, input().split()))))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = thing_w_v[i][0]
        value = thing_w_v[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])