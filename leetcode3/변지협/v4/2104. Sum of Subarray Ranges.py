'''
1. 아이디어 :
모든 부분 배열을 직접 순회한다. 시작점 i를 고정하고 끝점 j를 늘려가면서,
직전 구간의 최솟값/최댓값에 nums[j]를 반영해 갱신하면
구간 [i, j]의 (최댓값 - 최솟값)을 O(1)에 구할 수 있다.

2. 시간복잡도 :
o(n^2)

3. 자료구조/알고리즘 :
브루트포스 / 구간 최솟값·최댓값 누적

'''

class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            _min = nums[i]
            _max = nums[i]
            for j in range(i,n):
                _min = min(nums[j], _min)
                _max = max(nums[j], _max)
                ans += _max - _min

        return ans
