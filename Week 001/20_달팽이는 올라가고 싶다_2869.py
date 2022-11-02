a, b, v = map(int, input().split())
# a : 낮에 오르는 높이
# b : 밤에 미끄러 지는 높이
# v : 나무의 높이
day = 0

if (v-b) % (a-b) == 0:
    day = (v-a) / (a-b)
else:
    day = (v-a) / (a-b) + 1

day += 1

print("{:.0f}".format(int(day)))
