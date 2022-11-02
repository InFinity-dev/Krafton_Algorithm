t = input()
arr = [int(input()) for y in range(int(t))]
arr.sort()
print(*arr, sep='\n')
