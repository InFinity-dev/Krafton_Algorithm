arr = []
for i in range(9):
    input_data = input()
    arr.append(int(input_data))

print('{}\n{}'.format(max(arr), (arr.index(max(arr))+1)))
