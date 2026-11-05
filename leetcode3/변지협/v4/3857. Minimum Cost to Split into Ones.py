class Solution:
    def minCost(self, n: int) -> int:
        dic = {}
        dic[1] = 0
        dic[2] = 1
        dic[3] = 3
        dic[4] = 6

        for i in range(5,n+1):
            a = 1
            b = i - 1
            tmp = 10e9
            while a < b:
                tmp = min(tmp, a * b + dic[a] + dic[b])
                a+=1
                b-=1
            dic[i] = tmp
        
        return dic[n]
        