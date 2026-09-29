'''
1. 아이디어:
미분한다 생각하고 기울기를 구함.
만약 6개가 등차수열이면 해당 것은 4+3+2+1 = 10개가됨.
2. 시간복잡도:
o(n)
3. 알고리즘:
'''

"""
1 2 3 4 5 6
1 * 4 + 2 * 3 + 3 * 2 + 4 *1
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)

        tmp = []
        for i in range(n-1):
            tmp.append(nums[i+1] - nums[i])

        m = len(tmp)
        last = -10001
        streak = 0
        cases = []
        for i in range(m):
            print(last)
            if last == tmp[i]:
                streak += 1
            else:
                if streak >= 1:
                    cases.append(streak)
                streak = 0
            
            last = tmp[i]

        if streak >= 1:
            cases.append(streak)
        
        print(cases)

        ans = 0
        for c in cases:
            for i in range(1, c+1):
                ans += i
        return ans