
'''
1. 아이디어 :
0과 1의 개수가 1 이하로 차이나면 ans에 넣는 식으로 구한다.

2. 시간복잡도 :
    o(n^2)

3. 자료구조/알고리즘 :
완전탐색
'''

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
            