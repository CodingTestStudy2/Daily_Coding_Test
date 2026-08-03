#

'''
1. 아이디어 :


2. 시간복잡도 :
    O()

3. 자료구조/알고리즘 :


'''

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)

        count = 0
        for i in range(n):
            if nums1[i] % 2 == 0:
                count += 1
            else:
                for j in range(n):
                    if i == j:
                        continue
                    if abs(nums1[i] - nums1[j]) % 2 == 0:
                        count+=1
                        break
        
        if count == n:
            return True
        
        count = 0
        for i in range(n):
            if nums1[i] % 2 == 1:
                count += 1
            else:
                for j in range(n):
                    if i == j:
                        continue
                    if abs(nums1[i] - nums1[j]) % 2 == 1:
                        count+=1
                        break

        return count == n
