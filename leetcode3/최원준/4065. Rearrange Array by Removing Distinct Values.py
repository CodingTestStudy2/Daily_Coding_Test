class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        visited = set()
        ans = []

        while len(visited) != n:

            candids = set()
            for i in range(n):
                if i in visited:
                    continue
                if nums[i] in candids:
                    continue
                visited.add(i)
                candids.add(nums[i])

            temp = []
            for num in candids:
                temp.append(num)
            temp.sort()
            for num in temp:
                ans.append(num)
        
        return ans
        
