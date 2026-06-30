'''
1. 아이디어 :
n, m이 최대 100이기떄문에 n**2으로 쉽게 풀 수 있습니다.

2. 시간복잡도 :
    O(n * n)

3. 자료구조/알고리즘 :
-
'''

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for p in patterns:
            if p in word:
                ans+=1
        return ans
