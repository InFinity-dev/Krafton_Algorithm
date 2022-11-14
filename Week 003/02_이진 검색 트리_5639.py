# 이진 검색 트리의 전위 순회 결과를 후위 순회 결과로 출력
import sys

# alias 지정
input = sys.stdin.readline

graph = []
while True:
    try:
        graph.append(int(input()))
    except:
        break


def dfs(start, end):
    if start > end:
        return

    temp = end + 1

    for i in range(start + 1, end + 1):  # 루트를 제외하고 루트 보다 큰 노드를 찾아서 해당 노드를 기준으로 왼쪽과 오른쪽 서브 트리를 나눈다
        if graph[start] < graph[i]:  # 루트 노드 보다 키 값이 큰 노드 = 오른쪽 서브 트리 첫 노드
            temp = i  # temp에 해당 노드의 인덱스를 저장
            break

    dfs(start + 1, temp - 1)  # 왼쪽 서브 트리에 대한 재귀 탐색
    dfs(temp, end)  # 오른쪽 서브 트리에 대한 재귀 탐색

    print(graph[start])  # 각 서브 트리의 루트 노드 출력


dfs(0, len(graph) - 1)
