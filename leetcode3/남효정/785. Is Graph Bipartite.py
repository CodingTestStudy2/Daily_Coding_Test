# 풀이 실패
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {} # 노드별 색상

        def dfs(node, color):
            colors[node] = color

            for neighbor in graph[node]:
                # 인접한 노드가 같은 색상이면 실패
                if neighbor in colors:
                    if colors[neighbor] == color:
                        return False
                # 아직 색칠 안 된 노드면 재귀 호출
                else:
                    if not dfs(neighbor, -color):
                        return False
            return True

        # 분리된 그래프 누락하지 않게 전부 순회
        for i in range(len(graph)):
            if i not in colors:
                if not dfs(i, 1):
                    return False

        return True

