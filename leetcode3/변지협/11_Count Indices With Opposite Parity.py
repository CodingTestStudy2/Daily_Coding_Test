'''
1. 아이디어 :
    완전탐색
2. 시간복잡도 :
    O(n^2)
3. 자료구조/알고리즘 :
'''
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        lst = []
        for i in range(len(nums)):
            is_even = True if nums[i] % 2 == 0 else False
            _sum = 0
            for j in range(i+1,len(nums)):
                if is_even and nums[j] % 2 != 0:
                    _sum+=1
                elif not is_even and nums[j] % 2 == 0:
                    _sum +=1
        
            lst.append(_sum)
        return lst