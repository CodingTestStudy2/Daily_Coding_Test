#

'''
1. 아이디어 :
char별로 빈도수를 구하고 정렬 후, 가장 적은 빈도수들을 제거

2. 시간복잡도 :
    O(n + 26log26)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        c = Counter(s)
        char_freq = sorted([freq for char, freq in c.items()], reverse = True)
        ans = 0
        while len(char_freq) > k:
            ans += char_freq.pop()
        return ans
