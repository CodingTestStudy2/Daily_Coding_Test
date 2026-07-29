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
    def reverseByType(self, s: str) -> str:
        # 0 char, 1 special
        chars = ""
        specials = ""

        for c in s:
            if c.isalpha():
                chars += c
            else:
                specials += c
        chars = chars[::-1]
        specials = specials[::-1]

        ans = ""
        char_idx = 0
        special_idx = 0

        for c in s:
            if c.isalpha():
                ans += chars[char_idx]
                char_idx += 1
            else:
                ans += specials[special_idx]
                special_idx += 1
        return ans
