# 소수 K개를 입력받아 조합하여 곱한뒤 얻어진 오름차순의 수들중 N번째 수 구하기

import sys
import heapq

# alias 지정
input = sys.stdin.readline

k, n = map(int, input().split())
arr = list(map(int, input().split()))

p_list = list(arr)  # 입력받은 소수를 p_list 에 넣는다.
heapq.heapify(p_list)  # 힙에 넣어줌
...
pass
