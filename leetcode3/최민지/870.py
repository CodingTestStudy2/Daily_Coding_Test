class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        nums2_sort = sorted([(value, i) for i, value in enumerate(nums)])
        
        n = len(nums1)
        answer = [0] * n
        left = 0
        right = n-1

        #for value, i in reversed(nums2_sort):
        #    if nums1[i] > value:
        #        answer[i] = nums1[right]
        #        right -= 1
        #    else
        return ans