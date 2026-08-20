
'''
1. 아이디어 :
그냥 y를 먼저 붙이고, 나머지 문자를 붙인다.
x 몰라도 그냥 풀림

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
'''

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = ''
        tmp = ''
        
        for i in s:
            if i == y:
                tmp += i
            else:
                ans += i
        
        return tmp+ans