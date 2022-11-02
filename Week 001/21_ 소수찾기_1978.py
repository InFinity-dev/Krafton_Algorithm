# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
n = input()
arr = [int(n) for n in input().split()]


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


count_arr = []
for n in arr:
    if is_prime(n) == 1:
        count_arr.append(n)
print(len(count_arr))
