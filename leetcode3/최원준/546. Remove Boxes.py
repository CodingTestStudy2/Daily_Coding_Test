#

'''
1. 아이디어 :
3차원 dp문제.
i부터 j까지의 최대값을 구하는 2차원 dp로는 풀기 어려움.
i포인터 옆에 동일한 숫자가 있을 수 있기에, 그것까지 고려해서 문제를 풀어야한다.
k는 i포인터 옆에 동일한 숫자가 몇개 더 있는지 고려한다.

2. 시간복잡도 :
    O(n*n)

3. 자료구조/알고리즘 :
dp

'''

from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes):
        
        @lru_cache(None)
        def dp(left, right, k):
            if left > right:
                return 0

            # left부터 같은 색이 연속되어 있으면 하나로 묶는다.
            while left < right and boxes[left] == boxes[left + 1]:
                left += 1
                k += 1

            # 1. boxes[left] 그룹을 지금 제거
            ans = (k + 1) * (k + 1) + dp(left + 1, right, 0)

            # 2. 뒤쪽의 같은 색과 합치기
            for i in range(left + 1, right + 1):
                if boxes[i] == boxes[left]:
                    ans = max(
                        ans,
                        dp(left + 1, i - 1, 0)
                        + dp(i, right, k + 1)
                    )

            return ans

        return dp(0, len(boxes) - 1, 0)
