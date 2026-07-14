#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        curr = 0
        for char in s:
            if char == "E":
                curr += 1
                ans = max(ans, curr)
            else:
                curr -= 1
        return ans
