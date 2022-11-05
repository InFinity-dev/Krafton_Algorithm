import sys

# alias 지정
input = sys.stdin.readline

# n : 집의 개수
# c : 공유기의 개수
# arr : 집의 좌표를 받는 배열
n, c = map(int, input().split())
# arr=[]
arr = [int(input()) for _ in range(int(n))]
arr.sort()  # 이분 탐색을 위해 집의 좌표를 오름차순으로 정렬
# print(f'정렬 된 집의 좌표 : {arr}')


# 이진 탐색 범위 설정 (설치 시 가능한 공유기 간 거리의 범위)
# 최소 거리 = 1
# 최대 거리 = arr[n-1](끝집) - arr[0](첫집)

pl = 1  # 이진 탐색 범위 p left = 1
pr = arr[n - 1] - arr[0]  # 이진 탐색 범위 p right = 끝집에서 첫집 까지의 거리
pc = 0


def possible(gap):  # 공유기간 거리가 dist 라고 할 때 c 개 만큼의 공유기를 설치 가능한지 판별하는 함수
    print(f'\np Center = {pc} : 가장 인접한 공유기간 최대 거리가 {pc}(으)로 설치 가능한지 판별시작합니다.\n')
    router = 1  # 가능한 공유기 수를 카운트 (첫집에 설치 하고 시작한다고 가정하므로 1부터 시작)
    prev = arr[0]  # 이전 집의 최초 값은 첫번째 집의 좌표로 설정
    print(f'>>>>>>>>>>>> 1번째 집 (좌표 : {arr[0]})에 설치하였다고 가정합니다. >>>>>>>>>>>> [공유기가 {c - router}개 남았습니다]')
    for k in range(1, n):  # 남은 집의 범위 내에서
        print(f'{k + 1}번째 집 (좌표 : {arr[k]})에 설치 할 경우 인접한 공유기간 최대거리 {gap}(으)로 공유기 {router}개 설치 가능한지 탐색중...')
        if arr[k] - prev >= gap:  # 이전에 설치했던 집과, 해당 집까지의 거리가 주어진 gap 보다 멀수 있으면
            router += 1  # 설치 가능한 공유기 수에 한개 더 해줌
            prev = arr[k]  # 해당 집에 공유기를 설치하고 해당 집을 이전 집으로 설정
            print(f'>>>>>>>>>>>> {k + 1}번째 집 (좌표 : {arr[k]})에 설치하였다고 가정합니다. >>>>>>>>>>>> [공유기가 {c - router}개 남았습니다]')
    if router >= c:  # 만약 설치 가능한 공유기 수가 설치하려는 공유기 수 인 c 보다 크면 (= 간격 더 늘릴 수 있음)
        print(f'[공유기가 {c - router}개 남았습니다] 인접한 공유기간 최대거리 {pc}(으)로 설치 가능')
        return 1  # True 반환
    else:
        print(f'>>>>>>>>>>>> {k + 1}번째 (좌표 : {arr[k]}) 집에 설치 불가능!')
        print(f'[공유기가 {c - router}개 남았습니다] 인접한 공유기간 최대거리 {pc}(으)로 모두 설치 불가능')
        return 0  # 아닐 경우 False 반환


while pl <= pr:
    print(f'\n\n공유기간 최대거리 대입 범위(이진 탐색 범위)를 {pl}에서 {pr}로 설정하였습니다.')
    pc = (pl + pr) // 2  # p center 값 설정
    if possible(pc):  # c개 공유기로 설치 가능한 간격을 더 늘릴 수 있으면
        pl = pc + 1  # p left 를 p centr 우측으로 옮김 (더 넓은 간격이 가능한지 탐색)
    else:
        pr = pc - 1  # 공유기 설치 간격을 줄여야 하면 p right 를 p center 좌측으로 옮김 (더 좁은 간격으로 설치 가능한지 탐색)
print(f'\np left = {pl}')
print(f'p Center = {pc}')
print(f'p Right = {pr}\n')
print(f'{pr}')
