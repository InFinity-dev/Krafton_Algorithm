import sys
input = sys.stdin.readline

n = int(input())
tmp = n
cnt = 0

while True:
    n = (n%10)*10 + ((n//10)+(n%10))%10
    cnt += 1
    if tmp == n:
        break

print(cnt)