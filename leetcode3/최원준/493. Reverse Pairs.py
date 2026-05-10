#

'''
1. 아이디어 :
시도1:
- 한번에 loop로 지나온 값들을 저장하되, 정렬되도록 하여 total 계산을 쉽게 하려고 했습니다.
- n * nlogn 으로 실패.

시도2:
- nums를 정렬함과 동시에 값을 계산.
- merge_sort를 통해 왼쪽 오른쪽을 나눠서 정렬을 하되, 정렬하는 과정에서 total을 계산
- 전체 시간복잡도는 O(n log n).
- 다만 nums[:mid], nums[mid:] 슬라이싱 때문에 추가 복사 비용이 발생하지만, 전체 Big-O는 여전히 O(n log n).

2. 시간복잡도 :
    O(n log n)

3. 자료구조/알고리즘 :
merge sort

'''

class Solution:

    def __init__(self):
        self.ans = 0

    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        self.merge_sort(nums)
        return self.ans

    def merge_sort(self, nums: List[int]):
        n = len(nums)
        if n==1:
            return nums

        mid = n//2
        left = self.merge_sort(nums[0:mid]) # 재귀: log n. 값 복사 n/2
        right = self.merge_sort(nums[mid:]) # 재귀: log n. 값 복사 n/2

        # ans 카운팅
        self.add_count(left, right) # n

        # 정렬
        return self.sort_two_lists(left, right) # n


    def add_count(self, left, right):
        left_p = 0
        right_p = 0
        while left_p < len(left) and right_p < len(right):
            if left[left_p] > right[right_p] * 2:
                self.ans+= len(left) - left_p
                right_p += 1
            else:
                left_p += 1

    def sort_two_lists(self, left, right):
        merged = []
        left_p = 0
        right_p = 0

        while left_p < len(left) and right_p < len(right):
            if left[left_p] <= right[right_p]:
                merged.append(left[left_p])
                left_p += 1
            else:
                merged.append(right[right_p])
                right_p += 1

        merged.extend(left[left_p:])
        merged.extend(right[right_p:])

        return merged


