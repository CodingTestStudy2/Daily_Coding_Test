'''
1. 아이디어 :
set에 기록하고 길이 재서 구한다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
'''
class Solution:
    def residuePrefixes(self, s: str) -> int:
        n = len(s)
        ans = 0
        st = set()

        for i in range(n):
            st.add(s[i])
            # print(st, (i+1) % 3)
            if len(st) == (i + 1) % 3:
                ans += 1
            

        return ans