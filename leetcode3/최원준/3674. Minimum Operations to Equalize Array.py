#

'''
1. 아이디어 :
답은 항상 1이거나 0이다.
모두 같은 숫자면 바꿀 필요없고, 하나라도 다르다면 모조리 바꿔버리면 된다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return int(any(nums[i] != nums[i+1] for i in range(len(nums) -1)))
        
