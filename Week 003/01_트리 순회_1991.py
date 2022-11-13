import sys

# alias 지정
input = sys.stdin.readline

n = int(input())
inputs = []
for _ in range(n):
    inputs.append(input().split())


class Node:  # 노드 클래스 정의 : 해당 노드의 값(item), Left Child, Right Child를 인스턴스로 가짐
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):  # 전위 순회법
    print(node.item, end='')  # 본인 노드 출력
    if node.left != '.':  # 왼쪽 노드가 비어있지 않으면 왼쪽으로 진행
        preorder(tree[node.left])
    if node.right != '.':  # 오른쪽 노드가 비어있지 않으면 오른쪽으로 진행
        preorder(tree[node.right])


def inorder(node):  # 중위 순회법
    if node.left != '.':  # 왼쪽 노드가 비어있지 않으면 왼쪽으로 진행
        inorder(tree[node.left])
    print(node.item, end='')  # 본인 노드 출력
    if node.right != '.':  # 오른쪽 노드가 비어있지 않으면 오른쪽으로 진행
        inorder(tree[node.right])


def postorder(node):  # 후위 순회법
    if node.left != '.':  # 왼쪽 노드가 비어있지 않으면 왼쪽으로 진행
        postorder(tree[node.left])
    if node.right != '.':  # 오른쪽 노드가 비어있지 않으면 오른쪽으로 진행
        postorder(tree[node.right])
    print(node.item, end='')  # 본인 노드 출력


tree = {}  # 트리 구조 튜플 자료형 선언
for item, left, right in inputs:
    tree[item] = Node(item, left, right)  # 튜플의 각 원소는 노드 클래스로 들어간다

preorder(tree['A'])  # 전위 순회법 출력
print()
inorder(tree['A'])  # 중위 순회법 출력
print()
postorder(tree['A'])  # 후위 순회법 출력
