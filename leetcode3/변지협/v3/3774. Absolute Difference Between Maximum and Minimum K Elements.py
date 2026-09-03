
'''
1. 아이디어 :
그냥 조건대로 풀면 된다.

2. 시간복잡도 :
o(n logn - 정렬)

3. 자료구조/알고리즘 :
'''

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        return sum(nums[::-1][:k]) - sum(nums[:k])