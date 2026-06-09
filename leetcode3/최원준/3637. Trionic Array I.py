#

'''
1. 아이디어 :
2번 꺾이는지 확인합니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :


'''
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        if nums[0] >= nums[1] or nums[n-2] >= nums[n-1]:
            return False

        for i in range(1, n-1):
            prev, curr, next = nums[i-1], nums[i], nums[i+1]
            if prev == curr or curr == next:
                return False

            if prev < curr and curr > next:
                count+=1
            elif prev > curr and curr < next:
                count+=1
        return count == 2

