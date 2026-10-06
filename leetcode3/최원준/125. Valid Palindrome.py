#

'''
1. 아이디어 :


2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :


'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                ans += c
        return ans.lower() == ans[::-1].lower()
