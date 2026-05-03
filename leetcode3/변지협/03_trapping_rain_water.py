#

'''
1. 아이디어 :
- trap

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
- min, max 미리 구해놓기
'''

'''
          o
o         o
o     o   o
o o   o o o
o o   o o o
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        left = [0] * len(height)
        right = [0] * len(height)
        
        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i])

        right[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2 , -1, -1):
            # print(i)
            right[i] = max(right[i+1], height[i])
            
        # print(right)

        for i in range(1, len(height)-1):
            a = min(left[i], right[i]) - height[i]
            if a > 0:
                ans += a
        
        return ans
             