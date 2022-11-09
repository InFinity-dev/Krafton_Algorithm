# 크기가 NxN 행렬 a
# a 의 b 제곱을 구하는 프로그램
import sys

# alias 지정
input = sys.stdin.readline

n, b = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]


def mul(i, j):
    n_target = len(j)
    mul_result = [[0] * n_target for _ in range(n_target)]

    for row in range(n_target):
        for col in range(n_target):
            temp_result = 0
            for k in range(n_target):
                temp_result += i[row][k] * j[k][col]
            mul_result[row][col] = temp_result % 1000

    return mul_result


def square(a_sq, b_sq):
    if b_sq == 1:
        for x in range(len(a_sq)):
            for y in range(len(a_sq)):
                a_sq[x][y] %= 1000
        return a_sq

    tmp = square(a_sq, b_sq // 2)
    if b_sq % 2:
        return mul(mul(tmp, tmp), a_sq)
    else:
        return mul(tmp, tmp)


result = square(a, b)
for r in result:
    print(*r)
