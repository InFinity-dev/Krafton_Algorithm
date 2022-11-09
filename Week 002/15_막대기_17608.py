import sys

# alias 지정
input = sys.stdin.readline

n = int(input())  # 막대기 개수

stack = []
visual_cnt = 1  # 보이는 막대기 개수. 막대기 한개는 무조건 보임

for _ in range(n):
    stack.append(int(input()))

# 가장 긴 막대기는 스택에 최상위에 둠
high = stack[-1]

# 최대 길이 막대기로 저장된 값 보다 크면 보인다. visual_cnt 값 1 증가 시키고 high 값 갱신
for i in range(len(stack) - 1, -1, -1):
    if stack[i] > high:
        visual_cnt += 1
        high = stack[i]

print(visual_cnt)
