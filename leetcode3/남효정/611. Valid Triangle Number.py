# 풀이 실패
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        N = len(nums)
        
        for k in range(N-1, 1, -1):
            left = 0
            right = k - 1

            # 투 포인터
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    cnt += right - left
                    right -= 1
                else:
                    left += 1

        return cnt
