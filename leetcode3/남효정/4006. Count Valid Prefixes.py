class Solution:
    def countValidPrefixes(self, s: str) -> int:
        ans, diff = 0, 0

        # 0, 1의 개수가 서로 1 이하면 됨
        for char in s:
            if char == '1':
                diff += 1
            else:
                diff -= 1
            
            if abs(diff) <= 1:
                ans += 1

        return ans