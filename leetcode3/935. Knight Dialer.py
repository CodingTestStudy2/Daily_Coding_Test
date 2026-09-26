from collections import defaultdict
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        candids = {
            1:{6, 8},
            2:{7,9},
            3:{4,8},
            4:{0,3,9},
            5:{},
            6:{0,1,7},
            7:{2,6},
            8:{1,3},
            9:{2,4},
            0:{4,6}
        }

        length = 1
        curr = defaultdict(int)
        for i in range(10):
            curr[i] = 1
        while length != n:
            temp = defaultdict(int)
            for i in range(10):
                curr_val = curr[i]
                for next_num in candids[i]:
                    temp[next_num] = (temp[next_num] + curr_val) % MOD
            length+=1
            curr = temp
        
        ans = 0
        for _, count in curr.items():
            ans = (ans+count)%MOD
        return ans
