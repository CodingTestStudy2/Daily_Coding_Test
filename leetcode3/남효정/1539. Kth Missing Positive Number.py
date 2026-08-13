class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss_num = 0
        cnt = 0
        while True:
            miss_num += 1
            if miss_num not in arr:
                cnt += 1
            if k == cnt:
                return miss_num