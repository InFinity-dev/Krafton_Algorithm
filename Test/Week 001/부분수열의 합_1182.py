import sys
from itertools import permutations
# alias 지정
input = sys.stdin.readline

n,s = map(int,input().split()) # 수열에 사용될 정수의 개수 N, 부분수열의 합이 될 S 공백기준 분리 입력
arr = [int(k) for k in input().split()] # 입력받은 수열을 공백기준으로 분리하여 arr 리스트에 저장
# print(arr)
total = sum(arr)
arr.sort()

sum_pre_made = [] # 각 조합을 담을 리스트 선언

for c in range(n):
   sum_pre_made.append(list(permutations(arr, c))) # 0개 선택 ~ N개 선택까지 모든 경우의 수
# print(sum_pre_made)
sum_made =[] # 각 조합의 합을 담을 리스트 선언

# 이하 미 작성
# for a in sum_pre_made:
#     sum_made.append(sum(a))
# print(sum_made)