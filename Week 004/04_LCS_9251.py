import sys

input = sys.stdin.readline

# 풀이 1 : 2차원 배열 이용
word1, word2 = input().strip(), input().strip()
h, w = len(word1), len(word2)
cache = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if word1[i - 1] == word2[j - 1]:
            cache[i][j] = cache[i - 1][j - 1] + 1
        else:
            cache[i][j] = max(cache[i][j - 1], cache[i - 1][j])
print(cache[-1][-1])

# 풀이 2 : 1차원 배열과 cnt 변수 활용
word1, word2 = input().strip(), input().strip()
l1, l2 = len(word1), len(word2)
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))
