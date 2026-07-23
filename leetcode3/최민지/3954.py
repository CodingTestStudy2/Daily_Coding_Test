class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        
        # n - k <= x <= n + k
        x_list = []
        result = 0
        for i in range(n - k, n + k + 1):
            if i > 0:   
                x_list.append(i)

        for j in x_list:
            if n & j == 0:
                result += j
        
        return result
