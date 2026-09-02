class Solution:
    def countMonobit(self, n: int) -> int:
        def is_monobit(num):
            binary = bin(num)[2:]
            base = binary[0]
            for b in binary:
                if b != base:
                    return False
            return True

        ans = 0
        for i in range(n+1):
            ans += is_monobit(i)
        return ans

        
        
