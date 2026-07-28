#

'''
1. 아이디어 :
완전탐색보다는 dp 문제
nums1[i], nums2[j]를 순회한다.
nums1[i] == nums2[j]인 경우, 
    i번째 다음, j번째 다음으로 매칭된 값 (i번째 숫자와 j번째 숫자가 모두 연결되지 않은 상태의 최대값)의 +1
아닌 경우,
    i-1번째 숫자의 최대값 또는 j-1번째 숫자의 최대값을 누적한다.

2. 시간복잡도 :
    O(n * m + n * m) -> O(m + n * m)

3. 자료구조/알고리즘 :
dp

'''
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # lines, start1, start2, 
        # dp
        # 가장 처음 만나는 숫자
        """
        [0],[0],[0],[0],[0],[0],[0]
        [0],[0],[0],[1],[1],[1],[2]
        [0],[0],[1],[1],[1],[2],[2]
        [0],[0],[1],[1],[2],[2],[2]
        [0],[0],[1],[2],[2],[2],[3]
        [0],[0],[1],[1],[1],[3],[3]
        """
        n = len(nums1)
        m = len(nums2)
        # dp = [[0] * (m+1) for _ in range(n+1)]

        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         if nums1[i-1] == nums2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]+1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        prev = [0] * (m+1)
        for i in range(1, n+1):
            curr = [0] * (m+1)
            for j in range(1, m+1):
                if nums1[i-1] == nums2[j-1]:
                    curr[j] = prev[j-1]+1
                else:
                    curr[j] = max(curr[j-1], prev[j])
            prev = curr
        
        return curr[m]
