class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        x_cnt = s.count(x)
        y_cnt = s.count(y)

        other_list = [char for char in s if char not in (x, y)]
        
        return y*y_cnt + ''.join(other_list) + x*x_cnt