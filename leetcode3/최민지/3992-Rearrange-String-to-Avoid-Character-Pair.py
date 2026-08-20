class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        result = ''
        s_list = list(s)

        while y in s_list:
            s_list.remove(y)
            result += y

        for i in s_list:
            result += i
            
        return result
        