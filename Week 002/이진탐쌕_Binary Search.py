from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    a.sort()  # 이진 탐색은 정렬된 배열을 탐색할때 가장 빠르다. 받아온 배열을 정렬.
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


num = int(input('원소 수를 입력하세요 : '))
x = [None] * num

print('배열 데이터 입력')

for i in range(num):
    x[i] = int(input(f'x[{i}] : '))

ky = int(input('검색 할 값을 입력하세요 : '))

idx = bin_search(x, ky)

if idx == 0:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값이 있습니다.')
