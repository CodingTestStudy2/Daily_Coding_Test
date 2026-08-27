class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = []
        for i in range(1, len(arr)+1):
            for j in range(0, i):
                temp = arr[j:j+i]
                result.append(min(temp))
        return sum(result) % ( 10**9 + 7 )
        