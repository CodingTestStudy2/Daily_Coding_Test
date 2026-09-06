class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count = [1] * n
        answer = [0] * n

        # 1차 DFS
        # subtree 크기 + answer[0] 계산
        def dfs(node, parent, depth):
            answer[0] += depth

            for child in graph[node]:
                if child == parent:
                    continue

                dfs(child, node, depth + 1)
                count[node] += count[child]

        dfs(0, -1, 0)

        # 2차 DFS
        # root를 parent -> child로 옮기면서 answer 계산
        def reroot(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue

                answer[child] = (
                    answer[node]
                    - count[child]
                    + (n - count[child])
                )

                reroot(child, node)

        reroot(0, -1)

        return answer
