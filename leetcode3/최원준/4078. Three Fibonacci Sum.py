#

'''
1. 아이디어 :
fibonacci를 n보다 커질때까지 리스트를 만들고,
리스트를 순회하며 3개씩 합친다.

2. 시간복잡도 :
    O(n + n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        nums = [0, 1]
        while nums[-1] <= n:
            nums.append(nums[-2] + nums[-1])
            print(nums)
        
        if len(nums) < 3:
            return False
        
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] + nums[i+2] == n:
                return True
        return False
