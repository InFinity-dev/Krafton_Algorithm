# 산성용액의 특성값은 1~1,000,000,000 까지의 양의 정수
# 알칼리성 용액의 특성값은 -1~-1,000,000,000까지의 음의 정수
# 같은 양의 두 용액을 혼합한 용액의 특성 값 = 혼합의 사용된 각 용액의 특성값의 합으로 정의
# 같은 양의 두 용액을 혼합하여 특성값이 0 에 가장 가까운 용액을 만들려고 함
# 전체 용액의 수 N
# 용액의 특성값을 나타내는 N 개의 정수 주어짐
# 특성값이 0에 가장 가까운 용액을 만들어 내는 두 용액의 특성값 오름차순 출력
import sys
import math

# alias 지정
input = sys.stdin.readline

# n : 용액의 개수
# arr : 용액의 특성 값을 받는 배열
n = int(input())
arr = [int(k) for k in input().split()]

arr.sort()  # 이분 탐색을 위해 집의 좌표를 오름차순으로 정렬 (산성 ~ 염기성 순으로)
# print(arr)

pl = 0
pr = len(arr) - 1
product = arr[pl] + arr[pr]  # 첫번째 용액과 마지막 용액을 합친 값을 product 의 최초값으로 둔다
product_min = math.inf
while pl < pr:
    # print(f'{pl}--> <--{pr}')
    product = arr[pl] + arr[pr]
    # print(f'새롭게 시도 해보는 조합의 결과 용액 특성 = {product}')

    if abs(product) < product_min:  # 새로운 용액 조합(product)가 이떄 까지의 product_min보다 "0에 가까우면"
        # print(f'새로운 최소값이 나왔습니다\n조합 = {arr[pl]} + {arr[pr]}')
        product_min = abs(product)  # product_min 에 새로운 용액 특성값의 절대값을 저장
        left = pl
        right = pr

        if product == 0:  # 두 용액의 특성값이 0이면 루프 탈출
            left = pl
            right = pr
            break

    if product < 0:  # 두 용액의 특성값 합이 0보다 작으면 (산성) 왼쪽 포인터만 땡겨주면 됨
        pl += 1
        # print(f'pl 우측으로 이동-->')
    else:  # 두 용액의 특성값 합이 0보다 크면 (염기성) 오른쪽 포인터만 땡겨주면 됨
        pr -= 1
        # print(f'<-- pr 좌측으로 이동')

print(f'{arr[left]} {arr[right]}')
