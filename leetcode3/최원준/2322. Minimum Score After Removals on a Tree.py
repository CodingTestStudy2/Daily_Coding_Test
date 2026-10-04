class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        sub_xor = [0] * n
        tin = [0] * n
        tout = [0] * n

        time = 0

        def dfs(node, parent):
            nonlocal time

            tin[node] = time
            time += 1

            xor_value = nums[node]

            for nxt in graph[node]:
                if nxt == parent:
                    continue

                dfs(nxt, node)
                xor_value ^= sub_xor[nxt]

            sub_xor[node] = xor_value

            tout[node] = time
            time += 1

        dfs(0, -1)

        total = sub_xor[0]

        def is_ancestor(a, b):
            return tin[a] <= tin[b] and tout[b] <= tout[a]

        ans = float("inf")

        # node i는
        # parent(i) - i 간선을 자른다는 의미
        #
        # root(0)는 부모 간선이 없으므로 제외
        for a in range(1, n):
            for b in range(a + 1, n):

                if is_ancestor(a, b):
                    # a 안에 b가 존재
                    x1 = sub_xor[b]
                    x2 = sub_xor[a] ^ sub_xor[b]
                    x3 = total ^ sub_xor[a]

                elif is_ancestor(b, a):
                    # b 안에 a가 존재
                    x1 = sub_xor[a]
                    x2 = sub_xor[b] ^ sub_xor[a]
                    x3 = total ^ sub_xor[b]

                else:
                    # 서로 독립된 subtree
                    x1 = sub_xor[a]
                    x2 = sub_xor[b]
                    x3 = total ^ sub_xor[a] ^ sub_xor[b]

                score = max(x1, x2, x3) - min(x1, x2, x3)
                ans = min(ans, score)

        return ans
