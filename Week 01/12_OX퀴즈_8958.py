# 케이스 개수 지정
n = int(input())
# 각 케이스 마다 정답 입력을 담을 리스트 선언
answers = []

# 케이스 지정 개수 만큼 반복문, 리스트에 정답 입력
for i in range(n):
    a = input()
    answers.append(a)

# print(answers)
correct = 0
score = []

for k in answers:
    # print("\n다음 시험")
    case = list(k)
    # print(">>>>case : {}".format(case))
    temp_correct = 0

    for t in case:
        if t == 'O':
            # print("{}는 정답입니다.".format(k))
            temp_correct = temp_correct + 1
            # print(temp_correct)
            correct = correct + temp_correct
        else:
            # print("{}는 오답입니다.".format(k))
            temp_correct = 0
    score.append(correct)
    correct = 0

# print(score)
for s in score:
    print(s)
