#

'''
1. 아이디어 :
[i][a][b]는 i번째 알파뱃을 입력하고 난 후 왼손의 위치(a), 오른손의 위치(b)의 최소값입니다.
다음 알파뱃인 c를 입력하기 위해서는
- dp[i]에서 왼손을 움직이거나(dp[i][a][c])
- dp[i]에서 오른손을 움직입니다(dp[i+1][c][b])

2. 시간복잡도 :
    O(n * 27 * 27)

3. 자료구조/알고리즘 :
3차원 dp

'''
class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        # 3차원 DP
        n = len(word)
        dp = [[[float('inf')] * 27 for _ in range(27)] for _ in range(n + 1)]

        dp[0][26][26] = 0

        for i in range(n):
            c = ord(word[i]) - ord('A')

            for a in range(27):
                for b in range(27):
                    curr = dp[i][a][b]

                    if curr == float('inf'):
                        continue
                    
                    dp[i+1][c][b] = min( dp[i+1][c][b], curr + dist(a, c)) # 왼손

                    dp[i+1][a][c] = min( dp[i+1][a][c], curr + dist(b, c)) # 오른손
        
        ans = float('inf')
        for a in range(27):
            for b in range(27):
                ans = min(ans, dp[n][a][b])
        return ans
