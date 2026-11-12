#

'''
1. 아이디어 :
모든 경우의 수를 구할 수 있다.

2. 시간복잡도 :
    O(n ** k)

3. 자료구조/알고리즘 :
백트래킹

'''
class Solution:
    ans = float('inf')

    def distributeCookies(self, cookies: list[int], k: int) -> int:
        child_total = [0] * k

        def backtrack(idx):
            if idx == len(cookies):
                self.ans = min(self.ans, max(child_total))
                return
            
            for i in range(k):
                child_total[i] += cookies[idx]

                if child_total[i] < self.ans:
                    backtrack(idx+1)

                child_total[i] -= cookies[idx]
        
        backtrack(0)
        return self.ans
