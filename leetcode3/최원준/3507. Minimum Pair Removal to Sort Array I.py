#

'''
1. 아이디어 :
조건이 n <= 50 이라 n**2으로 풀 수 있다.
정렬일때까지(n):
  최소_sum 찾기(n)

2. 시간복잡도 :
    O(n**2)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        def check_sorted(nums: List[int]) -> bool:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        ans = 0

        while not check_sorted(nums):
            min_sum = float("inf")
            min_idx = 0

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]

                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i

            nums[min_idx] += nums[min_idx + 1]
            nums.pop(min_idx + 1)

            ans += 1

        return ans
