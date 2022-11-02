# import numpy as np

t = input()
arr = [str(input()) for y in range(int(t))]
arr_dict = []
for a in arr:
    str_len = len(a)
    # a 요소와 길이를 담은 2차원 배열 생성
    arr_dict.append([a, str_len])
# # 단어 기준 우선 정렬
# arr_dict.sort(key=lambda x:x[0])
# # 글자수 기준 2차 정렬
# arr_dict.sort(key=lambda x:x[1])

# 위 두 라인 동시에
arr_dict.sort(key=lambda x: (x[1], x[0]))
# print(*arr_dict, sep='\n')
# print_arr = np.array(arr_dict).T[0]

# print(*print_arr, sep='\n')
# print(*arr_dict, sep='\n')
# for p in arr_dict:
#     print(p[0])
arr_redundent = []
for value in arr_dict:
    if value[0] not in arr_redundent:
        arr_redundent.append(value[0])
print(*arr_redundent, sep='\n')
