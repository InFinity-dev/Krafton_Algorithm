# 수열 A가 주어졌을때, 가장 긴 증가하는 부분수열을 구하는 프로그램을 작성하시오.
# 최장 증가 부분 수열 (LIS : Longest Increasing Subsequence)
# O(N^2) / O(N log N) 두 가지 방법이 있다. 동적 계획법 (Dynamic Programming)의 대표적인 케이스
# 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 효율적으로 값을 구하는 알고리즘 설계 기법
# 이진 탐색을 이용한 O(N log N) 방법


import sys

# alias 지정
input = sys.stdin.readline

# n : 수열의 크기
# O(N^2) 알고리즘
# n = int(input())
# a = list(map(int, input().split()))
# dp = [0 for k in range(n)]
# for i in range(n):
#     for j in range(i):
#         if a[i] > a[j] and dp[i] < dp[j]:
#             dp[i] = dp[j]
#     dp[i] += 1
# print(max(dp))

# O(N log N) 알고리즘
from bisect import bisect_left


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
