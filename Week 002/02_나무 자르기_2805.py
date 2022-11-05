# 상근이는 나무 M미터가 필요
# 절단기 작동 방법 : 높이 H 지정, 한 줄에 있는 나무 전부를 벌목 (H 보다 낮은 나무는 잘리지 않는다)
# ex)
#     20 15 10 17 : 높이 H = 15m 일때
#     5m 0m 0m 2m : 가져 가는 나무의 길이 = 7m
#
# 나무 러버라 필요한 만큼인 Mm만 집에 가져가려고 함.(가져가는 나무 길이를 최대한 딱 맞춰야 함)
import sys

# alias 지정
input = sys.stdin.readline

# n 나무의 수
# m 가져가려는 나무의 길이
n, m = map(int, input().split())
arr = [int(t) for t in input().split()]
# print(f'나무들의 높이 : {arr}')
# 로직 아이디어
# 시작 값 1m, 나무 길이 중 가장 높은 나무의 높이를 끝값으로 절단기 높이의 범위 설정하고 해당 범위 안에서 이진탐색
pl, pr = 1, max(arr)

while pl <= pr:
    pc = (pl + pr) // 2  # 중앙값 = pc(p center) : 절단기 높이

    cut = 0  # 벌목한 나무의 총합
    for i in arr:  # 나무 높이 배열에서
        if i >= pc:  # 나무의 높이가 중앙값보다 크거나 같으면
            cut += i - pc
            # 벌목할 수 있는 길이는 해당 나무 높이에서 중앙값(=절단기 설정값)을 뺀 높이,
            # for 루프 동안 모든 나무에 대해 벌목 높이 cut 변수에 합산

    if cut >= m:  # 자른 길이가 목표값 m 보다 크면
        pl = pc + 1  # p center 오른쪽 탐색
    else:
        pr = pc - 1  # 자른 길이가 목표값 m 보다 작을경우, p center 왼쪽 값 탐색
print(pr)
