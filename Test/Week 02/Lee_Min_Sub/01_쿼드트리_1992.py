# 흑백 영상 압축 - 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 4분할 압축.
# 압축결과 영역별로 차례로 괄호 안에 묶어서 표현
# 분할정복 while 나누어진 행렬 전체가 0일경우 0 / 전체가 1일 경우 1

import sys

# alias 지정
input = sys.stdin.readline


def quad_split(n, y, x):
    if n == 1:  # 1x1까지 분할되었을 경우 압축 필요 없음 : 그대로 출력
        print(matrix[y][x], end="")
        return

    # 사분면 탐색 (x~x+n, y~y+n), 사분면 첫 행렬 값 = matrix[y][x]
    temp = True  # boolean 저장 플래그
    for i in range(y, y + n):  # y, y+n까지 범위 (나눠진 사분면 y축)
        if not temp:  # temp 가 True 면 break
            break
        for j in range(x, x + n):  # x, x+n까지 범위 (나눠진 사분면 x축)
            if matrix[y][x] != matrix[i][j]:  # 탐색중인 행렬 값이 사분면 행렬값과 같지 않으면 한번 더 분할 가능
                temp = False
                break

    if temp:  # temp 가 True면 압축 해서 출력, 사분면 전체 값 = matrix[y][x]
        print(matrix[y][x], end="")
    else:  # 사분면 다시 분할후 각 사분면마다 quad_split, 압축 가능 확인
        n_split = n // 2

        print("(", end="")
        quad_split(n_split, y, x)  # 왼쪽 위
        quad_split(n_split, y, x + n_split)  # 오른쪽 위
        quad_split(n_split, y + n_split, x)  # 왼쪽 아래
        quad_split(n_split, y + n_split, x + n_split)  # 오른쪽 아래
        print(")", end="")


size = int(input())  # 행렬 사이즈 입력
matrix = [list(input().strip()) for _ in range(size)]  # 배열 입력
x_start = y_start = 0  # (0,0) 행렬 부터 탐색 시작
quad_split(size, x_start, y_start)
