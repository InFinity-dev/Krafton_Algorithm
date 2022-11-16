class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class AdjGraph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # 간선 추가
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # 그래프 출력 정의
    def print_agraph(self):
        for i in range(self.V):
            print(f'노드 {str(i)} : ', end='')
            temp = self.graph[i]
            while temp:
                print(f'-> {temp.vertex}', end='')
                temp = temp.next
            print(" \n")


V = 4
# 그래프 정의 , 간선 정의
graph = AdjGraph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)

graph.print_agraph()
