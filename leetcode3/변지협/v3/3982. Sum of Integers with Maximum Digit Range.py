'''
1. 아이디어 :
그냥 조건대로 풀면 된다.

2. 시간복잡도 :
o(n * m) - n : nums의 길이, m : num의 자릿수

3. 자료구조/알고리즘 :
'''
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        digit_range = []
        for num in nums:
            lst = [int(i) for i in str(num)]
            digit_range.append(max(lst) - min(lst))
        
        max_digit_range = max(digit_range)
        ans = 0

        for num in nums:
            lst = [int(i) for i in str(num)]
            dr = max(lst) - min(lst)
            if dr == max_digit_range:
                ans += num

        return ans

