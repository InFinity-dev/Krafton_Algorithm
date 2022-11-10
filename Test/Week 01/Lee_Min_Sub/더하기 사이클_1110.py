n = str(input()) #숫자를 문자열 형태로 입력받고
print(int(n))
arr=[]
for i in n: # 배열에 각 자리수를 나누어 담는다
    arr.append(int(i))
print(arr)
temp = []
cycle_count = 0

while True:
    arr = list(map(int,arr))
    for k in str(sum(arr)): # arr 요소의 합을 문자열 형태로 나누어 temp 리스트에 한자리씩 담음
        temp.append(k)
    print("새로운 수의 뒷자리 >> {}".format(temp[-1])) # 새로운 수의 뒷자리
    arr=[str(arr[-1]),str(temp[-1])] # 이전 배열의 맨 뒷자리와 새로운 수의 뒷자리를 담는 리스트
    n_made = "".join(arr) # 하나의 수 형태로 합침
    print("arr >> {}".format(arr))
    print("새로 만들어진 수 >> {}".format(n_made))
    print("원래 입력된 수 >> {}".format(n))
    temp = []
    cycle_count+=1
    if int(n) == int(n_made):
        print(cycle_count)
        break
