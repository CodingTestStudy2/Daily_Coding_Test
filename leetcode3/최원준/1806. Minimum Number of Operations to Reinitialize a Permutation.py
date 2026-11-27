class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1

        i = 2
        count = 1

        while i != 1:
            i = (2 * i) % (n - 1)
            count += 1

        return count
