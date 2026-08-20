class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        result = []
        x_count = s.count(x)#O(n)
        y_count = s.count(y)#O(n)

        if s.find(x) ==-1 or s.find(y) ==-1: #O(n)
            result.append(s)
        else:
            for s1 in s:
                if s1 == y:
                    result.insert(0,s1) #O(n^2)
                elif s1 != x:
                    result.append(s1)
            result.insert(y_count,x*x_count)
        return ''.join(result)

s = "zaodvxbsvqstlrbn"
x = "t"
y = "s"
solution = Solution()
print(solution.rearrangeString(s,x,y))


