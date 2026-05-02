#

'''
1. 아이디어 :
- 정렬 후, 왼쪽 포인터를 두고, 나머지 두 숫자를 찾습니다.(왼쪽+1, 오른쪽끝에서 이분탐색)
- 왼쪽 포인터가 가리키는 숫자가 양수인 경우, 리턴.

2. 시간복잡도 :
    O( n^2 )

3. 자료구조/알고리즘 :
정렬, 투포인터

'''


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for left in range(n - 2):
            left_value = nums[left]

            if left > 0 and nums[left] == nums[left - 1]:
                continue

            if left_value > 0:
                break

            mid = left + 1
            right = n - 1

            while mid < right:
                total = left_value + nums[mid] + nums[right]

                if total == 0:
                    ans.append([left_value, nums[mid], nums[right]])

                    mid += 1
                    right -= 1

                    while mid < right and nums[mid] == nums[mid - 1]: mid += 1
                    while mid < right and nums[right] == nums[right + 1]: right -= 1

                elif total < 0:
                    mid += 1
                else:
                    right -= 1

        return ans