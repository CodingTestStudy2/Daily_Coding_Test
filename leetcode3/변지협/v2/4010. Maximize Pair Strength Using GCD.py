
'''
1. 아이디어 :
완전탐색으로 풀려고 했으나, 시간복잡도가 너무 많이 나와서 실패.
유클리드 호제법으로 다시 풀려고 하는데 while문을 사용해서 접근하는데 지금 이해가 잘안감.

2. 시간복잡도 :
    O(n² × max(nums))

3. 자료구조/알고리즘 :
완전탐색
'''

class Solution(object):

    def gcd(self, a, b):
        # a를 b로 나누면 그 나머지와 b의 최대공약수는 같다.
        # 18 24
        # 18 % 24 = 18
        # 

        g = a % b
                
    def maxPairStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = -1
        for i in range(n-1):
            for j in range(i+1,n):
                x = nums[i] * nums[j] / self.gcd(nums[i],nums[j]) ** 2
                # print(self.gcd(nums[i],nums[j]), x)
                if ans < x:
                    ans = x
        
        return ans
        