#

'''
1. 아이디어 :
재귀를 사용해서 파티션 선을 하나씩 옮긴다.
평균값을 구할때마다 리스트를 새로 만들지 않고, prefix를 통해서 계산한다.

2. 시간복잡도 :
    O(n*n*k)

3. 자료구조/알고리즘 :
dfs, memoization, prefix sum

'''
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ans = 0.0

        prefix = [0] * (n + 1)

        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        def get_average(left: int, right: int) -> float:
            return (prefix[right] - prefix[left]) / (right - left)

        @cache
        def dfs(start: int, split: int) -> float:
            if split == 1:
                return get_average(start, n)

            ans = 0.0

            for end in range(start + 1, n - split + 2):
                curr = get_average(start, end)
                remain = dfs(end, split - 1)
                ans = max(ans, curr + remain)
            return ans

        return dfs(0, k)
