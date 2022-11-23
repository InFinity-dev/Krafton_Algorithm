import sys

from bisect import bisect_left

input = sys.stdin.readline


def get_lis(arr):
    dp = [arr[0]]
    for i in range(1, len(arr)):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            lower_bound = bisect_left(dp, arr[i])
            dp[lower_bound] = arr[i]
    return len(dp)


n = int(input())
a = list(map(int, input().split()))

print(get_lis(a))
