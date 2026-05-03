#

'''
1. 아이디어 :
- 현재 height 기준, 왼쪽과 오른쪽을 봤을때 최대 높이를 구합니다.
- 왼쪽과 오른쪽 최대 높이 중 작은 값에서 현재 height를 빼면, 현재 height에서 고일 수 있는 물의 양이 됩니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]
        right_max = [0]

        for i in range(n):
            left_max.append(height[i] if left_max[-1] < height[i] else left_max[-1])
            right_max.append(height[n-i-1] if right_max[-1] < height[n-i-1] else right_max[-1])

        ans = 0
        for i in range(1, n):
            ans += min(left_max[i], right_max[n+1-i]) - height[i-1]

        return ans