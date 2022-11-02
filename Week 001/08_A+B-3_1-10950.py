t = int(input())
arr = []
for i in range(t):
    a, b = map(int, input().split())
    arr.append(a + b)
print(*arr, sep='\n')
