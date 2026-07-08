class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        arr = nums[:]
        ans = 0

        def sorted_array():
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        while not sorted_array():
            idx = 0
            min_sum = arr[0] + arr[1]

            # 가장 작은 인접한 합(동점이면 왼쪽)
            for i in range(1, len(arr) - 1):
                s = arr[i] + arr[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # 두 원소를 하나로 합치기
            arr[idx] = min_sum
            arr.pop(idx + 1)

            ans += 1

        return ans