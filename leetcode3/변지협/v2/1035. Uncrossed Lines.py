"""
2 5 1 2 5
  -   -   -
10 5 2 1 5 2
"""

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        selected = -1
        ans1 = 0
        for i in range(n1):
            # print(selected, i)
            q = selected if selected != -1 else 0
            # continuer = False
            for j in range(q, n2):
                # print('i,j,selected,nums1[i],nums2[j],ans',i,j,selected,nums1[i],nums2[j],ans)
                if nums1[i] == nums2[j]:
                    selected = j+1
                    ans1 +=1 
                    break

        selected = -1
        ans2 = 0
        for i in range(n2):
            # print(selected, i)
            q = selected if selected != -1 else 0
            # continuer = False
            for j in range(q, n1):
                # print('i,j,selected,nums1[i],nums2[j],ans',i,j,selected,nums1[i],nums2[j],ans)
                if nums1[j] == nums2[i]:
                    selected = j+1
                    ans2 +=1 
                    break

        return max(ans1,ans2)

        
                