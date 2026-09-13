class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1_000_000_007
        
        aba = 6
        abc = 6

        for _ in range(1, n):
            aba, abc = (
                (aba * 3 + abc * 2) % MOD,
                (aba * 2 + abc * 2) % MOD
            )
        return (aba + abc) % MOD
