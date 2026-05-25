
'''
1. 아이디어 :
2. 시간복잡도 :
    O(n)
3. 자료구조/알고리즘 :
'''

class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        prev_score = 0
        for num in nums:
            # print("num, k, ans, prev_score:",num, k, ans, prev_score)
            if ans and ans[-1] == num:
                if prev_score < k:
                    ans.append(num)
            else:
                ans.append(num)
                prev_score = 0
                
            prev_score +=1
        
        return ans