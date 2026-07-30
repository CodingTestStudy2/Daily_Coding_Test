class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left_p = 0
        right_p = 1
        answer = []

        while(right_p<=len(nums)):
            answer.append()
            if right_p-left_p<k:
                right_p+=1