#

'''
1. 아이디어 :
diff가 다를때마다 자른다.
자른 길이를 재귀함수를 통해 경우의 수를 구한다

2. 시간복잡도 :
    O(n + n)

3. 자료구조/알고리즘 :
dfs

'''
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) <3:
            return 0

        @cache
        def calc(n):
            return n // 3 if n <= 3 else n-2 + calc(n-1)
        
        ans = 0
        prevs = [nums[0], nums[1]]
        diff = nums[1] - nums[0]

        for num in nums[2:]:
            if num - prevs[-1] == diff:
                prevs.append(num)

            elif num - prevs[-1] != diff:
                if len(prevs) >= 3:
                    ans += calc(len(prevs))
                
                diff = num - prevs[-1]
                prevs = [prevs[-1], num]
        ans += calc(len(prevs))
        return ans            

