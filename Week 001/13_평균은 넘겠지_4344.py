# 케이스 개수 지정
n = int(input())
# 각 케이스 마다 성적 입력을 담을 리스트 선언
scores = []

# 케이스 지정 개수 만큼 반복문, 리스트에 성적 입력
for i in range(n):
    # a = input()
    a = map(int, input().split())
    scores.append(a)

# 전역변수 선언
avg = []
only_scores = []
students_count = []

for k in scores:
    # 공백 기준으로 나누어 test 리스트에 요소 복사
    test = k.split(' ')
    # 문자열로 받은 요소를 int 로 변환
    test = list(map(int, test))

    # 0번 인덱스의 학생수를 반환과 동시에 리스트에서 삭제. students 변수에 학생수 받아옴.
    students = test.pop(0)
    students_count.append(students)
    # print("학생 수 : {}".format(students))
    # print("test 리스트 출력 : {}".format(test))
    # pop으로
    only_scores.append(test)

    total = sum(test)
    # print("점수 총합 : {}".format(total))

    # 평균 점수 계산
    avg_score = total / students
    # print("평균 점수 : {}".format(avg_score))
    # 전역변수 리스트에 저장
    avg.append(avg_score)

# print(avg)
# print(only_scores)
# print(students_count)

above_avg = 0
y = 0

for score in only_scores:
    q = 0
    for k in score:
        q += 1
        # print("{}와 평균점수 {} 비교".format(k,avg[y]))
        if k > avg[y]:
            above_avg += 1
    # print("평균 넘는 인원수 {}".format(above_avg))
    # print("케이스 학생수 {}".format(students_count[y]))
    percentage = (above_avg / students_count[y]) * 100
    print("{:.3f}%".format(percentage))
    above_avg = 0
    y += 1
