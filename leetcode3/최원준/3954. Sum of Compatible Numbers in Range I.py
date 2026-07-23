#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(2k)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        ans = 0
        x = max(1, n-k)
        while abs(n-x) <= k:
            if n&x == 0:
                ans += x
            x+=1
        return ans
