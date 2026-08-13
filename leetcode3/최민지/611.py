class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        # 삼각형 조건: a + b > c

        count = 0
        for i in range(len(nums)-1, -1, -1):
            c = nums[i]
            
            left = 0
            right = i-1

            while left < right:
                if nums[left] + nums[right] > c:
                    count += right - left
                    right -= 1
                else:
                    left += 1

            #for j in range(i-1, -1, -1):
            #    b = nums[j]
            #    for k in range(j-1,-1, -1):
            #        a = nums[k]

            #        if a + b > c:
            #            count += 1

        return count

