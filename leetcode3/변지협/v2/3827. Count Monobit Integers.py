class Solution:

    def countMonobit(self, n: int) -> int:
        ans = 0
        for i in range(n):
            first = bin(i)[0]
            print(first)