'''
1. 아이디어 :
- 문자열을 정제한 후, 정제된 문자열이 회문인지 확인.
2. 시간복잡도 :
o(n)
3. 자료구조/알고리즘 :

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        small = 'abcdefghijklmnopqrstuvwxyz'
        big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        dic = {}
        
        for i in range(26):
            dic[small[i]] = small[i]
            dic[big[i]] = small[i]
        
        for i in '0123456789':
            dic[i] = i

        refined = ''
        for i in s:
            if i in dic:
                refined += dic[i]
        
        print(refined)

        return refined == refined[::-1]