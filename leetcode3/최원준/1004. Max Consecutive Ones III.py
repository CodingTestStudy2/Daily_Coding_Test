#

'''
1. 아이디어 :
슬라이딩 윈도우를 사용합니다.
오른쪽 포인터를 순회하면서 0, 1의 갯수를 새며,
0의 갯수가 k보다 크면 왼쪽 포인터를 옮깁니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
슬라이딩 윈도우

'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #sliding window
        n = len(nums)
        left = 0
        counter = [0, 0]
        ans = 0
        for right in range(n):
            right_num = nums[right]
            counter[right_num] += 1
            
            while counter[0] > k:
                left_num = nums[left]
                counter[left_num] -= 1
                left +=1 

            ans = max(ans, counter[0] + counter[1])
        return ans
