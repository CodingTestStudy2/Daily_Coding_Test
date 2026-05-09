#

'''
1. 아이디어 :
- total은 중앙값 근처에서 최소가 됩니다.
- 배열을 정렬 후에 중앙값과 가까운 후보들을 추출합니다.

2. 시간복잡도 :
    O(n log n)

3. 자료구조/알고리즘 :
그리디

'''


from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[len(nums) // 2]

        candidates = self.candidates(m)

        return min(
            sum(abs(num - target) for num in nums)
            for target in candidates
            if 1 <= target < 10 ** 9
        )

    def candidates(self, x: int) -> set[int]:
        s = str(x)
        n = len(s)
        half = (n + 1) // 2
        prefix = int(s[:half])

        result = {
            10 ** (n - 1) - 1,
            10 ** n + 1,
            }

        for p in [prefix - 1, prefix, prefix + 1]:
            if p <= 0:
                continue

            left = str(p)

            if n % 2 == 0:
                result.add(int(left + left[::-1]))
            else:
                result.add(int(left + left[-2::-1]))

        return result