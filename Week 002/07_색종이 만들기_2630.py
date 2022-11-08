import sys

# alias 지정
input = sys.stdin.readline

n = int(input())
colored = [list(map(int, input().split())) for _ in range(n)]
white_cnt = blue_cnt = 0


def recursive(x, y, sq_paper):
    global white_cnt, blue_cnt
    temp_cnt = 0
    for i in range(x, x + sq_paper):
        for j in range(y, y + sq_paper):
            if colored[i][j]:
                temp_cnt += 1
    if not temp_cnt:
        white_cnt += 1
    elif temp_cnt == sq_paper ** 2:
        blue_cnt += 1
    else:
        recursive(x, y, sq_paper // 2)
        recursive(x + sq_paper // 2, y, sq_paper // 2)
        recursive(x, y + sq_paper // 2, sq_paper // 2)
        recursive(x + sq_paper // 2, y + sq_paper // 2, sq_paper // 2)
    return


recursive(0, 0, n)
print(white_cnt)
print(blue_cnt)
