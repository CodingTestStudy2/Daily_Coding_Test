#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(len(n))

3. 자료구조/알고리즘 :
dictionary

'''

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        c = Counter(str(n))
        ans = -1
        min_freq = float('inf')

        for num, freq in c.items():
            if freq == min_freq:
                ans = min(ans, int(num))
            elif freq < min_freq:
                min_freq = freq
                ans = int(num)
        return ans
