class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        lmt = 0
        arr = arr[::-1]
        while True:
            if len(arr) == 0:
                lmt += 1
            elif arr[-1] == i:
                arr.pop()
            else:
                lmt += 1
            
            if lmt == k:
                break
            i += 1

        return i
