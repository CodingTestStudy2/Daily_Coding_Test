class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in nums:
            if i % 2 == 0:
                if nums.count(i) == 1:
                    return i
        return -1

# 파이썬 count는 문자열의 개수, 리스트의 개수 세는 함수 
        