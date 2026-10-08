class Solution:
    def merge(self, nums1: list[int], n: int, nums2: list[int], m: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2 = len(nums1), len(nums2)
        index1, index2 = n-1, m-1
        insert_index = len(nums1)-1

        while insert_index >= 0:
            num1 = nums1[index1] if index1>=0 else -float('inf')
            num2 = nums2[index2] if index2>=0 else -float('inf')

            if num1 > num2:
                nums1[insert_index] = num1
                index1-=1
            else:
                nums1[insert_index] = num2
                index2-=1

            insert_index-=1
