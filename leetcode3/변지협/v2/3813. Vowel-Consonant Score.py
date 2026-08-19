'''
1. 아이디어 :
vowels와 consonants를 각각 count하고, v/c를 return. c가 0이면 0 return.

2. 시간복잡도 :
o(n * 26) = o(n)

3. 자료구조/알고리즘 :
'''
from math import floor
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        v = 0
        c = 0

        for i in s:
            if i in vowels:
                v += 1
            elif i in consonants:
                c += 1
        
        try:
            return floor(v/c)
        except:
            return 0