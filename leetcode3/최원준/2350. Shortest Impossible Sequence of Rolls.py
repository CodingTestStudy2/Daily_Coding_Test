class Solution:
    def shortestSequence(self, rolls: list[int], k: int) -> int:
        seen = set()
        ans = 1

        for num in rolls:
            seen.add(num)

            if len(seen) == k:
                ans += 1
                seen.clear()

        return ans
