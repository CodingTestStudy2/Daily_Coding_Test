#

'''
1. 아이디어 :
양쪽에 포인터를 두어서 계산합니다.
오른쪽 포인터는 왼쪽 포인터가 0인 경우 움직입니다.
왼쪽 포인터는 항상 움직이지만 왼쪽 포인터가 0이지만 오른쪽 포인터가 0이 아닌 경우 움직이지 않습니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
투포인터

'''

class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)

        left, right = 0, n-1
        ans = 0

        while left < right:
            left_value, right_value = nums[left], nums[right]

            if left_value != 0 and right_value != 0: # 3...3
                left+=1
            elif left_value == 0 and right_value != 0: # 0...3
                left+=1
                right-=1
                ans+=1
            elif left_value != 0 and right_value == 0: # 3...0
                left+=1
                right-=1
            elif left_value == 0 and right_value == 0: # 0...0
                right-=1
        return ans
