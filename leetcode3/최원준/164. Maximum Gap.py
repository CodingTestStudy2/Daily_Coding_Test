#

'''
1. 아이디어 :
counting_sort

2. 시간복잡도/공간복잡도 :
    O(n) / O(n)

3. 자료구조/알고리즘 :
카운팅 정렬

'''

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        cmin = float('inf')
        cmax = 0
        for num in nums:
            cmin = min(cmin, num)
            cmax = max(cmax, num)


        counting_list = [0] * (cmax - cmin + 1)
        for num in nums:
            counting_list[num - cmin] = 1
        
        ans = 0
        prev = cmin

        for i in range(len(counting_list)):
            if counting_list[i] == 0:
                continue

            curr = i + cmin

            ans = max(ans, curr - prev)
            prev = curr
        
        return ans

        
