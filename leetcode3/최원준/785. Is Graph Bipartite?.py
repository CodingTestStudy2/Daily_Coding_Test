#

'''
1. 아이디어 :
Bipartite는 그래프에서 노드들을 2가지 색을 칠했을때, 인접한 노드와 다른 색일때 성립.
bfs를 통해 노드들의 색갈을 0 또는 1로 칠한다.
그래프가 끊긴 문제는 모든 노드들을 순회하게끔 한다.

2. 시간복잡도 :
    O(V + E) 노드, 간선

3. 자료구조/알고리즘 :
BFS

'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        for i in range(n):
            if colors[i] != -1:
                continue

            colors[i] = 0
            queue = deque()
            queue.append(i)

            while queue:
                start = queue.popleft()
                start_color = colors[start]
                
                for dest in graph[start]:
                    dest_color = colors[dest]
                    if start_color == dest_color:
                        return False

                    if dest_color == -1:
                        queue.append(dest)
                        colors[dest] = (1 + start_color) % 2
            # print(colors)
        return True

                

