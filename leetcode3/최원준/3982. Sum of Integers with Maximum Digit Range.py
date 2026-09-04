class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def calc_digit_range(num):
            largest = 0
            smallest = float('inf')
            while num:
                remain = num%10
                largest = max(largest, remain)
                smallest = min(smallest, remain)
                num = num // 10
            return largest - smallest
               
        digit_ranges = []
        largest = 0
        for num in nums:
            dr = calc_digit_range(num)
            largest = max(largest, dr)
            digit_ranges.append(dr)

        ans = 0
        for i in range(len(nums)):
            if digit_ranges[i] == largest:
                ans += nums[i]
        return ans
