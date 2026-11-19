'''
Time Limit Exceeded
53 / 370 testcases passed
'''
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        x=1
        cap_left = index
        cap_right = n-index-1
        left = 0
        right = 0
        left_sum = 0
        right_sum = 0
        _sum = 0
        while True:
            # print(x,left,right, left_sum, right_sum, _sum)
            if x >=3 and cap_left > left:
                left += 1
            if x >=3 and cap_right > right:
                right += 1
            left_sum += left
            right_sum += right
            _sum = left_sum + right_sum + n + x - 1
            x+=1
            if _sum > maxSum:
                break
        
        return x -2 
        

                