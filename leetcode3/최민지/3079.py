class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            s = str(num)
            mx = max(s)
            encrypted = int(mx * len(s))
            ans += encrypted

        return ans