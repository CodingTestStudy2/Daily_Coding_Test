#

'''
1. 아이디어 :
투 포인터.
right는 하나씩 옮기면서 curr 값에 곱한다.
curr 값이 k가 넘어가면 left를 옮기면서 curr값을 나눈다.
ans += right - left + 1. (오른쪽 포인터의 숫자를 기준으로 갯수를 더함)

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
투포인터

'''

from collections import defaultdict
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        """
        [10, 5, 2, 6, 12, 9, 4, 3, 1, 100, 3] 100

        """
        ans = 0
        n = len(nums)

        left = 0
        right = 0
        curr = 1

        while right < n:
            curr *= nums[right]

            while curr >= k:
                curr /= nums[left]
                left+=1
                
            ans += right - left + 1
            right+=1
        return ans


