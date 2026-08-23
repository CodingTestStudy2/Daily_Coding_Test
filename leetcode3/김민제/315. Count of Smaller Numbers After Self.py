from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        n = len(nums)
        counts = [0] * n

        # (값, 원래 index)
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):

            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            temp = []

            i = left
            j = mid + 1

            # 오른쪽에서 이미 가져온 작은 원소 개수
            right_smaller = 0

            while i <= mid and j <= right:

                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    right_smaller += 1
                    j += 1

                else:
                    # arr[i]보다 작은 오른쪽 원소들의 개수
                    counts[arr[i][1]] += right_smaller

                    temp.append(arr[i])
                    i += 1

            # 왼쪽에 남은 원소
            while i <= mid:
                counts[arr[i][1]] += right_smaller

                temp.append(arr[i])
                i += 1

            # 오른쪽에 남은 원소
            while j <= right:
                temp.append(arr[j])
                j += 1

            # 정렬된 결과를 원래 배열에 반영
            arr[left:right + 1] = temp

        merge_sort(0, n - 1)

        return counts
