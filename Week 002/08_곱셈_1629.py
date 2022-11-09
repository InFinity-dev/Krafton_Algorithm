# 자연수 A^B 구하기. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
import sys

# alias 지정
input = sys.stdin.readline

a, b, c = map(int, input().split())

# 나머지 연산(MOD)의 분배법칙
# (A + B) % p = ((A % p) + (B % p)) % p
# (A - B) % p = ((A % p) - (B % p) + p) % p
# (A * B) % p = ((A % p) * (B % p)) % p
# (A / B) % p = (A * B^(p-2)) % p = ((A % p) * (B^(p-2) % p)) % p

def power(i, j, k):
    if j == 1:
        return i % k
    else:
        temp = power(i, j // 2, k)
        if j % 2 == 0:
            return (temp * temp) % k
        else:
            return (temp * temp * i) % k


print(power(a, b, c))
