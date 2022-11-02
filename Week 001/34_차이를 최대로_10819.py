# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
# 배열의 순서를 바꿔서 식의 최대값 찾기
from itertools import permutations
from sys import stdin

input = stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
# 모든 순열의 리스트
num_list = list(permutations(num_list, n))
result = 0

for num in num_list:
    tmp = 0
    # 순회, 최대값 서칭
    for i in range((len(num)) - 1):
        tmp += abs(num[i] - num[i + 1])
    result = max(result, tmp)

print(result)
