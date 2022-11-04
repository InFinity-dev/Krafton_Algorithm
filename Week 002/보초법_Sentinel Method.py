import copy


def seq_search(seq, key):
    print("검색 함수 호출됨!")
    a = copy.deepcopy(seq)
    a.append(key)  # 보초키를 추가 (검색할 값을 마지막 인덱스에 추가)
    print(f'복사되어 보초값 추가된 배열 by.deepcopy : {a}')

    k = 0
    while True:  # k 값을 추가 시키면서 탐색 대상 배열 순회
        # print("seq_search : While Loop 진입")
        print(f'탐색중인 인덱스 : {k}')
        if a[k] == key:
            break
        k += 1
    return -1 if k == len(seq) else k
    # 있으면 해당 값의 인덱스 값을 반환 (배열 길이와 비교하여 나온 값이 보초키값일 경우는 -1 반환)


num = int(input("원소 수를 입력하세요 : "))
x = [None] * num  # 원소 수가 num인 배열을 생성

for i in range(num):
    x[i] = int(input(f'x[{i}] : '))

ky = int(input('검색할 값을 입력하세요 : '))

idx = seq_search(x, ky)

if idx == -1:
    print("검색값을 갖는 원소가 존재하지 않습니다.")
else:
    print(f"검색값은 x[{idx}]에 있습니다.")
