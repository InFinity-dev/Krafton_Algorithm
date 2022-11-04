# 첫째줄에 정수 N이 주어짐
# 두번째 줄에 A[N] 입력
# 셋째줄에 정수 M이 주어짐
# 넷째 줄에 B[M] 입력
# B[M]의 각 요소가 A안에 있는지 탐색하여 1/0으로 출력
import sys
from typing import Any, Sequence
# import copy

# alias 지정
input = sys.stdin.readline


# Sentinel Method 함수
# def seq_search(seq, q_arr, key):
#     # print("검색 함수 호출됨!")
#     a = copy.deepcopy(seq)
#     a = a + q_arr  # 보초키를 추가 (검색할 값을 마지막 인덱스에 추가)
#     # print(f'복사되어 보초값 추가된 배열 by.deepcopy : {a}')
#
#     k = 0
#     while True:  # k 값을 추가 시키면서 탐색 대상 배열 순회
#         # print("seq_search : While Loop 진입")
#         # print(f'탐색중인 인덱스 : {k}')
#         if a[k] == key:
#             break
#         k += 1
#     return 0 if k >= (len(seq)) else 1


# Binary Search 함수
def bin_search(a: Sequence, key: Any) -> int:

    pl = 0  # p left 는 인덱스 0 에서 부터 시작
    pr = len(a) - 1  # p right 는 가장 마지막 인덱스 에서 시작

    while True:
        pc = (pl + pr) // 2  # p center은 가운데 인덱스 에서 시작
        if a[pc] == key:  # 검색값이 a배열의 중앙 요소와 같으면
            return 1  # 1 반환
        elif a[pc] < key:  # 검색값이 a배열 중앙 요소 보다 작으면
            pl = pc + 1  # 새로운 p left 인덱스를 중앙인덱스 보다 오른쪽으로 옮겨줌 (우측 탐색)
        else:
            pr = pc - 1  # 검색값이 a배열 중앙 요소 보다 크면, 새로운 p right 인덱스를 중앙인덱스 보다 왼쪽으로 옮겨줌 (좌측 탐색)
        if pl > pr:  # p left 인덱스와, p right 인덱스가 교차하면, 배열안에 검색값이 없다는 뜻
            return 0


n = input()
A = [int(k) for k in input().split()]
m = input()
B = [int(j) for j in input().split()]

# 선형 탐색 : 시간 초과
# for b in B:
#     print(A.count(b))

# 보초법을 이용한 탐색 : 시간 초과
# for b in B:
#     print(seq_search(A, B, b))

# 이진 탐색
A.sort()  # 이진 탐색은 정렬된 배열을 탐색할때 가장 빠르다. 받아온 배열을 정렬.
for b in B:
    print(bin_search(A, b))
