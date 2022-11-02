nums = []

for _ in range(3):
    a = int(input())
    nums.append(a)

result = 1

for num in nums:
    result = result * num

num_split = []
for i in str(result):
    num_split.append(i)

count = [0 for k in range(10)]

for digit_num in num_split:
    conv_digitnum = int(digit_num)
    count[conv_digitnum] += 1
    # if conv_digitnum == 0:
    #     count[0] += 1
    # elif conv_digitnum == 1:
    #     count[1] += 1
    # elif conv_digitnum == 2:
    #     count[2] += 1
    # elif conv_digitnum == 3:
    #     count[3] += 1
    # elif conv_digitnum == 4:
    #     count[4] += 1
    # elif conv_digitnum == 5:
    #     count[5] += 1
    # elif conv_digitnum == 6:
    #     count[6] += 1
    # elif conv_digitnum == 7:
    #     count[7] += 1
    # elif conv_digitnum == 8:
    #     count[8] += 1
    # else:
    #     count[9] += 1

print(*count, sep='\n')
