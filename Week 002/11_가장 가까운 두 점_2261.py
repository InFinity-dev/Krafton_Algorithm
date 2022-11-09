# 2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점의 거리의 제곱 출력
# 입력 >>
# n
# x(0) , y(0)
# x(1) , y(1)
# ...    ...
# x(n) , y(n)
# 백준 오답 나옴 : 반례?

import sys
import math

# alias 지정
input = sys.stdin.readline

n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
xy_cord = []
point_x = []
point_y = []


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def arr2point(arr):
    global xy_cord, point_x, point_y
    for p in arr:
        point_x.append(p[0])
        point_y.append(p[1])


def trans_point2d(arr_x, arr_y):  # 배열로 받은 좌표를 정의한 Point2D 자료형으로 변환하여 xy_cord 에 배열로 저장
    global xy_cord
    for k in range(len(arr_x)):
        xy_cord.append(Point2D(x=arr_x[k], y=arr_y[k]))


def distance(point_1, point_2):  # 두 점간 거리 구하는 함수
    distance_x = point_1.x - point_2.x
    distance_y = point_1.y - point_2.y
    # print(f'두점 사이의 거리 = {int((math.sqrt(distance_x**2 + distance_y**2))**2)}')
    return int((math.sqrt(distance_x ** 2 + distance_y ** 2)) ** 2)


arr2point(a)
trans_point2d(point_x, point_y)


def mindistance(arr):
    arr_size = len(arr)
    min_dis = distance(arr[1], arr[0])

    for i in range(arr_size):
        for j in range(i + 1, arr_size):
            # print(f'두점 사이의 거리 = {distance(arr[j],arr[i])}')
            if distance(arr[j], arr[i]) < min_dis:
                min_dis = distance(arr[j], arr[i])

    return min_dis


print(mindistance(xy_cord))
