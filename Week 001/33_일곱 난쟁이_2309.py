# 아홉 난쟁이 중에 키의 합이 100이 되는 7명의 난쟁이를 찾아라
import sys

# alias 지정
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(int(input()))
total = sum(arr)
arr.sort()
# count = 0
for i in range(9):
    for j in range(i + 1, 9):
        # count += 1
        if (total - arr[i] - arr[j]) == 100:
            for k in range(9):
                if k != i and k != j:
                    print(arr[k])
            # print("총 탐색 횟수 : {}".format(count))
            exit()
