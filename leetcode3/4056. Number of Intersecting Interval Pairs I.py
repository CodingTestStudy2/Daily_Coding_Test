class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        
        def check_intersect(point1, point2):
            s1, e1 = point1
            s2, e2 = point2

            if e1 < s2:
                return False
            if e2 < s1:
                return False
            return True
        
        n = len(intervals)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if check_intersect(intervals[i], intervals[j]):
                    ans+=1
        return ans
