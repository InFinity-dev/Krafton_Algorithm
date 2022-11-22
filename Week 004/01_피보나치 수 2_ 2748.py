import sys

input = sys.stdin.readline


def fibo(n):  # n 번째 피보나치 수를 구하는 함수
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


dictionary = {1: 1, 2: 1}


def fibo_dict(n):
    if n in dictionary:  # n번째 피보나치 수를 저장하는 딕셔너리를 만든후 이미 있는 값에 대해서는 딕셔너리 값을 활용
        return dictionary[n]
    else:
        dictionary[n] = fibo_dict(n - 1) + fibo_dict(n - 2)
        return dictionary[n]


num = int(input())
print(fibo_dict(num))
