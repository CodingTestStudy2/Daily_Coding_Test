
class Solution:
    def run(self, hours):
        lst = [1 if hour > 8 else -1 for hour in hours]
        n = len(lst)
        tmp = [0] * n
        tmp[0] = max(lst[0],0)
        for i in range(1,n):
            tmp[i] = max(tmp[i-1]+lst[i],0)            
        print(tmp)

        streak = 0
        _max = -1
        for i in tmp:
            # print(i, streak, _max)
            if i != 0:
                streak +=1
            else:
                streak = 0
            
            if streak > _max:
                _max = streak
        
        return _max

    def longestWPI(self, hours: list[int]) -> int:
        return max(self.run(hours), self.run(hours[::-1]))