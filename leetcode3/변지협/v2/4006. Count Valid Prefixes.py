class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        ans = 0
        
        for i in range(n):
            selected = s[:i+1]
            one = len([i for i in selected if i == '1'])
            zero = len([i for i in selected if i == '0'])
            if one == zero or one + 1 == zero or one == zero + 1:
                ans += 1

        return ans
            