# 준규가 가지고 있는 동전은 N 종류
# 동전을 조합하여 가치의 합을 K
# 동전 종류 개수 N, 가치의 합 K가 주어질때 필요한 동전 개수의 최솟값을 구하라
import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())

coin_type = []
coin_available = []

for i in range(n):
    coin_type.append(int(input()))

for i in coin_type:
    if i <= m:
        coin_available.append(int(coin_type.index(i)))  # 가능한 최대 동전 종류

# for z in coin_available:
#     print(coin_type[z])

count = 0
count_total = 0

for e in reversed(coin_available):
    # print(f'{coin_type[e]} 동전에 대해 탐색')
    # coin_type[e] #1000, 500, 100, 50, 5, 1
    if m == 0:
        break
    else:
        # print(f'>>> {int(math.log10(coin_type[e]) + 1)}')
        # print(f'>>> {int(math.log10(m) + 1)}')
        if int(math.log10(coin_type[e]) + 1) <= int(math.log10(m) + 1):
            count = m // coin_type[e]
            m -= (count * coin_type[e])
            # print(f'동전 {coin_type[e]} {count}개 >>> 남은 m = {m}')
            count_total += count
            count = 0

print(count_total)
