#

'''
1. 아이디어 :
0과 1의 갯수 차이가 <= 1일때 성립한다

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        counts = [0, 0]
        ans = 0
        for char in s:
            counts[int(char)] += 1
            if abs(counts[0] - counts[1]) <= 1:
                ans+=1
        return ans
