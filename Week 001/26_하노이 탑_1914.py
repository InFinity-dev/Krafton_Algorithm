# if 원판 1개:
#     이동 = 시작기둥 -> 대상기둥
# if 원판이 2개 이상
#     원판 뭉치 이동 = 시작기둥 -> 보조기둥
#     이동 = 시작기둥 -> 대상기둥
#     원판 뭉치 이동 = 보조기둥 -> 대상기둥

# target_b : 이동목표 원판
# start_p : 시작기둥 (1)
# target_p : 대상기둥 (3)
# sub_p : 보조기둥 (2)

# 이동 횟수 카운트 전역 변수
move_count = 0

# 이동 경로 저장 리스트
move_list = []


# n >= 20 일때는 공식 적용
# (2**n)-1

def hanoi(target_b, start_p, target_p, sub_p):
    # 전역변수 참조 선언
    global move_count
    if target_b > 20:
        move_count = 2 ** target_b - 1
    else:
        if target_b == 1:
            move_list.append("{} {}".format(start_p, target_p))
            move_count += 1
        else:
            hanoi(target_b - 1, start_p, sub_p, target_p)
            move_count += 1
            move_list.append("{} {}".format(start_p, target_p))
            hanoi(target_b - 1, sub_p, target_p, start_p)


n = int(input())

hanoi(n, "1", "3", "2")
print(int(move_count))
if n <= 20:
    print(*move_list, sep='\n')
