class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        graph = [[] for _ in range(n)]

        for rich, poor in richer:
            graph[poor].append(rich)

        answer = [-1] * n

        def dfs(x):
            # 이미 계산했다면 재사용
            if answer[x] != -1:
                return answer[x]

            # 자기 자신도 후보
            answer[x] = x

            for rich in graph[x]:
                candidate = dfs(rich)

                if quiet[candidate] < quiet[answer[x]]:
                    answer[x] = candidate

            return answer[x]

        for i in range(n):
            dfs(i)

        return answer
