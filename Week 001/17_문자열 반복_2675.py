# 입력할 테스트 케이스 횟수 사용자로부터 입력
t = int(input())
r_list = []
s_list = []

for k in range(t):
    r, s = map(str, input().split())
    r_list.append(int(r))
    s_list.append(s)

for i in range(len(r_list)):
    strK = ''
    for m in s_list[i]:
        strK += (m * int(r_list[i]))
    print(strK)
