#

'''
1. 아이디어 :
정렬 후, set을 사용하여 방문한 숫자들을 체크

2. 시간복잡도 :
    O(nlogn)

3. 자료구조/알고리즘 :
해시셋, 정렬

'''
class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        visited = set()
        nums = sorted(nums, reverse = True)
        
        ans = []
        counts = 0

        for num in nums:
            if num in visited:
                continue
            
            ans.append(num)
            visited.add(num)
            counts += 1
            if counts == k:
                return ans
        return ans
