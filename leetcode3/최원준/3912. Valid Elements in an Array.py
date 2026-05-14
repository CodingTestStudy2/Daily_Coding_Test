#

'''
1. 아이디어 :
왼쪽부터 오른쪽(left_max), 오른쪽부터 왼쪽(right_max)으로 가면서 만나는 숫자들의 최대값을 저장하는 배열을 만듭니다.
nums를 순회하면서 left_max[i]보다 크거나 right_max[i]보다 크면 후보에 포함합니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''


class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left_max = [0] * n
        right_max = [0] * n

        for i in range(n-1):
            left_max[i+1] = max(left_max[i], nums[i])
            right_max[n-i-2] = max(right_max[n-i-1], nums[n-i-1])

        return [nums[i] for i in range(n) if nums[i] > left_max[i] or nums[i] > right_max[i]]