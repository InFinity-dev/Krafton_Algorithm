import sys
import heapq

input = sys.stdin.readline
q = []
n = int(input())  # 강의 개수
lecture = []
lecture_room = [0] * (n+1)

for l in range(n):
    lecture.append((list(map(int, input().split()))))
    # lecture[][0] : 강의 번호 / lecture[][1] : 강의 시작 시간 / lecture[][2] : 강의 종료 시간

lecture = sorted(lecture, key=lambda x: (x[1]))  # 강의 시작 시간 기준으로 정렬
print(f'강의 시작 시간 기준으로 Sorted Arr : {lecture}')
lecture_end_time_priority = sorted(lecture, key=lambda x: (x[2]))  # 강의 종료 시간 기준으로 정렬
print(f'강의 종료 시간 기준으로 Sorted Arr : {lecture_end_time_priority}')

for e in lecture_end_time_priority:
    heapq.heappush(q, e)

count = 1  # 첫 강의는 무조건 강의실이 할당 되기 때문에 카운트는 1에서 시작
# print(q)
# 새로운 강의싫 할당 조건 : 이전 강의에 대해 강의실을 할당 하고, 다음 강의의 시작 시간과 이전 강의 시간이 겹치면 새로운 강의실을 할당 해야된다.
# 다음 강의시작 시간 < 이전 강의 끝나는 시간 -> 강의실 새로 할당
for lecture_num, start_time, end_time in lecture:
    k = q[0]  # 종료 시간 기준으로 정렬한 heap 가장 앞 원소 peak
    print(f'{k[0]}강의 시작 시간 {k[1]}')
    if k[1] < end_time:  # 이전 강의와 시간이 겹치면 새 강의실을 할당하고 heapq에서 해당 강의 pop
        print('겹쳐서 새 강의실 할당')
        lecture_room[lecture_num] = count
        count += 1
        heapq.heappop(q)

print(count - 1) # 필요한 강의실 개수
print(*lecture_room[1:])
