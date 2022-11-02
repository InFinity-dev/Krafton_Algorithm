# 골드바흐의 추측 : 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
# 이러한 수를 골드바흐 수라고 하며, 짝수를 두 소수의 합으로 나타내는 표현을
# 그 수의 골드바흐 파티션이라고 한다.
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n 이 주어졌을때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
# (만약 가능한 n의 골드바흐 파티션이 여러가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.)
num = int(input())

n = 10000

# 에라토스테네스의 체
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

ans_list = []
for i in range(num):

    even = int(input())

    even_first = even // 2

    ans1 = even_first
    ans2 = even_first

    if ans1 not in primes and ans2 not in primes:
        while True:
            ans1 -= 1
            ans2 += 1

            if ans1 in primes and ans2 in primes:
                break

    ans_list.append("{} {}".format(ans1, ans2))

print(*ans_list, sep='\n')
