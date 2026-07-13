#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n * m)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        def encrypt(x):
            n = len(str(x))
            cmax = 0
            while x:
                remain = x%10
                cmax = max(cmax, remain)
                x = x//10
            return int(str(cmax) * n)

        return sum([encrypt(x) for x in nums])
