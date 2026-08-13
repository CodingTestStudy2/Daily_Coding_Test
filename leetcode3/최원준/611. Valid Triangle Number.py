#

'''
1. 아이디어 :
투포인터를 사용.
i에 위치한 숫자가 왼쪽+오른쪽 값보다 작으면 삼각형이 만들어진다.
오른쪽 포인터를 이동하여 유요한지 확인
else
왼쪽 포인터를 이동.

2. 시간복잡도 :
    O(n*n)

3. 자료구조/알고리즘 :
투포인터

'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n-1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans

        # nums.sort()
        # def binary_search(side1, side2, mid_index):
        #     left = mid_index
        #     right = n

        #     while left < right:
        #         mid = (left+right) // 2
        #         longest = nums[mid]
        #         if longest < side1 + side2:
        #             left = mid+1
        #         else:
        #             right = mid
        #     return left

        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     if nums[i] == 0:
        #         continue
        #     for j in range(i+1, n):
        #         end = binary_search(nums[i], nums[j], j+1)
        #         ans += end - (j+1)
        # return ans
