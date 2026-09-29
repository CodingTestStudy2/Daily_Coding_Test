'''
1. 아이디어:
그냥 문제에 주어진대로 구현하면 됨.
2. 시간복잡도:
o(n+m)
3. 알고리즘:
'''

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)