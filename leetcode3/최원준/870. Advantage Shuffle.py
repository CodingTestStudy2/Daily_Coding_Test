class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def get_sorted_queue(nums):
            num = [[nums[i], i] for i in range(len(nums))]
            num.sort()
            return deque(num)

        queue1 = get_sorted_queue(nums1)
        queue2 = get_sorted_queue(nums2)
        ans = [0] * len(nums1)

        while queue1 and queue2:
            biggest1, _ = queue1[-1]
            smallest1, _ = queue1[0]

            biggest2, index1 = queue2[-1]
            smallest2, index2 = queue2[0]

            if biggest1 > biggest2:
                biggest1, _ = queue1.pop()
                biggest2, index1 = queue2.pop()
                ans[index1] = biggest1
            else:
                smallest1, _ = queue1.popleft()
                biggest2, index2 = queue2.pop()
                ans[index2] = smallest1
        
        return ans
