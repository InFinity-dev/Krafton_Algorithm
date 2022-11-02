a = int(input())
if 90 <= a:
    print('A')
# 이미 위에서 비교한 조건에 대해서는 다시 연산 해줄 필요가 없다
elif 80 <= a:
    print('B')
elif 70 <= a:
    print('C')
elif 60 <= a:
    print('D')
else:
    print('F')
