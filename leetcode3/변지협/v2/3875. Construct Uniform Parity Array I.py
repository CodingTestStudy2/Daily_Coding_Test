class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        can_odd, can_even = False, False
        n = len(nums1)

        for i in range(n):
            if nums1[i] % 2 != 0:
                can_odd = True
                continue

            for j in range(n):
                # print('i,j,nums1[i] - nums1[j]:', i,j,nums1[i] - nums1[j])
                if i == j:
                    continue
                
                if (nums1[i] - nums1[j]) % 2 != 0:
                    can_odd = True
                    continue
            
            # can_odd = False

        for i in range(n):
            if nums1[i] % 2 == 0:
                can_even = True
                continue

            for j in range(n):
                if i == j:
                    continue
                
                if nums1[i] - nums1[j] % 2 == 0:
                    can_even = True
                    continue
            
            # can_even = False

        if can_even or can_odd:
            return True
        else:
            return False