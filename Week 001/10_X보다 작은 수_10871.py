n, x = map(int, input().split())
arr = [int(num) for num in input().split()]
print(arr)
for i in arr:
    if i < x:
        print(i, end=' ')
