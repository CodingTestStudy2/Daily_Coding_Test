#

'''
1. 아이디어 :
가장 작은 숫자를 찾고, 왼쪽과 오른쪽 중 작은 숫자와 곱하여 ans에 더합니다. 그리고 작은 숫자를 제외한 리스트를 생성

2. 시간복잡도 :
    O(n * n)

3. 자료구조/알고리즘 :
그리디

'''
class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        ans = 0

        def get_smallest(nums):
            n = len(nums)
            smallest = float('inf')
            index = -1

            for i, num in enumerate(nums):
                if num < smallest:
                    smallest = num
                    index = i

            new_nums = []
            for i in range(n):
                if i == index:
                    continue
                new_nums.append(nums[i])
            
            if index == 0:
                product = nums[0] * nums[1]
            elif index == n-1:
                product = nums[-1] * nums[-2]
            else:
                product = nums[index] * min(nums[index-1], nums[index+1])
            
            return new_nums, product
        
        while len(arr) > 1:
            arr, product = get_smallest(arr)
            ans += product
        return ans
