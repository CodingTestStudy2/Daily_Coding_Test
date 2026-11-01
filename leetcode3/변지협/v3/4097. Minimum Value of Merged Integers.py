'''
1. 아이디어 :
- nums를 앞에서부터 두 개씩 짝지어, 두 수의 자릿수를 그대로 이어붙인 정수를 만든다.
- 짝지어진 수들 중 최솟값을 반환한다.
2. 시간복잡도 :
o(n)
3. 자료구조/알고리즘 :
문자열, 완전탐색

'''

class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 10e10
        for i in range(0,n-1,2):
            tmp = int(f'{nums[i]}{nums[i+1]}')
            ans = min(tmp, ans)
        
        return ans
