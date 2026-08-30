class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        target = stones[-1]

        visited = set()

        def dfs(pos, k):
            if pos == target:
                return True

            if (pos, k) in visited:
                return False

            visited.add((pos, k))

            for next_k in [k - 1, k, k + 1]:
                if next_k <= 0:
                    continue

                next_pos = pos + next_k

                if next_pos in stone_set:
                    if dfs(next_pos, next_k):
                        return True

            return False

        return dfs(0, 0)
