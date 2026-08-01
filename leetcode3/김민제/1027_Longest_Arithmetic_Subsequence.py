from typing import List

'''
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
 
맨처음 문제를 보고 투포인터로 문제인줄 알았으나 DP문제라고 함.
-> 사실 DP개념만 알지 문제를 제대로 풀줄 모름.

hint : Subsequence가 들어가면 DP / subarray가 들어가면 투포인터

사실 아래 부분이 이해가 안됨... 
if diff in dp[j]:
    dp[i][diff] = dp[j][diff] + 1
else:
    dp[i][diff] = 2
answer = max(answer,dp[i][diff])
            
'''

def longestArithSeqLength(nums: List[int]) -> int:
    answer = 0
    n = len(nums)

    dp = [{} for _ in range(n)]

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]

            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
            else:
                dp[i][diff] = 2
            answer = max(answer,dp[i][diff])

    return answer


arr = [3, 6, 9, 12]
print(longestArithSeqLength(arr))
