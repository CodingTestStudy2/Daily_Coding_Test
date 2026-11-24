'''
실패 (시간초과)
o(n^2)

1. 아이디어 :
local inversion = 이웃한 두 원소가 뒤집힌 경우 → for문 한 번으로 센다.
global inversion = i < j 인데 nums[i] > nums[j] 인 쌍 → 지금까지 넣은 값들을
정렬된 리스트로 유지하면서, 이분탐색으로 새 값보다 큰 원소의 개수를 더해준다.

2. 시간복잡도 :
o(n^2) — global inversion을 세는 쪽에서 이분탐색으로 위치는 o(logn)에 찾지만
list.insert가 뒤 원소들을 밀어야 해서 o(n). 총 o(n^2) 이라 n=10^5 에서 시간초과.
(정렬 배열 대신 펜윅트리/세그먼트트리 쓰면 o(nlogn))

3. 자료구조/알고리즘 :
정렬 유지 리스트 + 이분탐색(lower_bound), divide and conquer

'''

from collections import defaultdict

class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        local = 0
        n = len(nums)

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                local +=1

        glob = 0
        lst = []
        for i in nums:
            a,b = 0,len(lst)

            while a < b:
                mid = (a+b) // 2
                if lst[mid] <= i:
                    a = mid + 1
                else:
                    b = mid
                
            glob += len(lst) - a
            lst.insert(a,i)
        
        return glob == local
