'''
a b a
---
aba = 3
abc = 2

a b c
---
aba = 2
abc = 2a

'''
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        aba = 6
        abc = 6
        
        for i in range(n-1):
            new_aba = 2 * abc + 3 * aba
            new_abc = 2 * abc + 2 * aba
            aba,abc = new_aba, new_abc

        return (aba + abc) % mod
