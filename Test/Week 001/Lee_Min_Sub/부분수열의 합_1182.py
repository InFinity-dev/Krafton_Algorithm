import sys
from itertools import combinations

# alias 지정
input = sys.stdin.readline


# 2차원 리스트 평탄화 함수
def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += flatten(item)
        else:
            result += [item]
    return result


n, s = map(int, input().split())  # 수열에 사용될 정수의 개수 N, 부분수열의 합이 될 S 공백기준 분리 입력
arr = [int(k) for k in input().split()]  # 입력받은 수열을 공백기준으로 분리하여 arr 리스트에 저장
# print(arr)
total = sum(arr)

sum_pre_made = []  # 각 조합을 담을 리스트 선언
arr.sort()  # 아무것도 고르지 않은 경우를 제외하기 위해 정렬

for c in range(1, n + 1):  # 아무것도 고르지 않은 경우 = 0번째 인덱스에 위치, range 1부터 시작하여 제외시킴
    sum_pre_made.append(list(combinations(arr, c)))  # 1개 선택 ~ N개 선택까지 모든 경우의 수
# print("sum_pre_made : {}".format(sum_pre_made))
sum_list = flatten(sum_pre_made)  # 각 조합의 합을 담을 리스트를 선언하고, 2차원 리스트 평탄화
# print("sum_list : {}".format(sum_list))
m = len(sum_list)
# print("조합 경우의 수 : {}".format(m))

sum_ans = []
for i in range(m):  # 아무것도 고르지 않은 첫번째 조합 제외
    sum_ans.append(sum(list(sum_list[i])))  # 모든 조합의 합을 담은 리스트

# print("조합으로 부터 나온 합의 케이스 : {}".format(sum_ans))
print(sum_ans.count(s))  # 부분수열들의 합 중 입력받은 S와 같은 합의 경우 카운트하여 출력
