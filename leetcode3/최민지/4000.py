class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        # 불가능한 경우
        if n > s or s > 9 * n:
            return -1

        result = 0
        for i in range(n):
            for j in range(9,0,-1):
                after_sum = s - j
                after_digit = n -i -1

                if after_digit <= after_sum <= after_digit * 9:
                    result = result * 10 + j
                    s = after_sum
                    break

        return result





        