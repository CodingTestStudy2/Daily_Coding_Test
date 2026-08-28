'''
1. 아이디어 :
최대 nlogn 시간복잡도로 문제를 풀어야한다. (캐싱 또는 DP로 값 재사용)
i보다 왼쪽에 있는 인덱스 j 중, arr[i]보다 작은 arr[j]의 위치를 구한다. (monotonic stack)
dp[i]는 0~i까지 윈도우를 설정했을때의 총합을 유지.
j value를 포함하는 윈도우는 0~j까지의 합을 미리 구했기때문에 i-j 범위 * arr[i]

2. 시간복잡도 :
    O(2n)

3. 자료구조/알고리즘 :
dp + monotonic stack

'''
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1000000007
        n = len(arr)
        
        dp = [0] * n
        small_indexes = []

        for i in range(n):
            cval = arr[i]
            while small_indexes and arr[small_indexes[-1]] > cval:
                small_indexes.pop()
            
            if small_indexes:
                j = small_indexes[-1]
                dp[i] = dp[j] + cval * (i-j)
            else:
                dp[i] = cval * (i+1)
            
            small_indexes.append(i)
        
        return sum(dp) % MOD

