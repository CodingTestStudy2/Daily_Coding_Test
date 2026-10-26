'''
1. 아이디어 :
- 모든 (i, j) 쌍을 완전탐색하면서 nums[i] + nums[j] == target 이고 nums[i] > nums[j] 인 쌍만 본다.
- 그중 nums[i] * nums[j] 가 최대가 되는 쌍을 갱신하고, 반환은 큰 값의 인덱스가 앞에 오도록 [i, j] 순서를 맞춘다.
- 유효한 쌍이 하나도 없으면 초기값 그대로 [-1, -1] 이 반환된다.
2. 시간복잡도 :
O(n^2)
3. 자료구조/알고리즘 :
- 완전탐색(Brute Force)

'''

class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        mul = -99999
        it = -1
        jt = -1
        for j in range(n-1):
            for i in range(j+1,n):
                if nums[i] + nums[j] == target and not nums[i] == nums[j]:
                    if nums[i] * nums[j] > mul:
                        mul = nums[i] * nums[j]
                        if nums[i] > nums[j]:
                            it = i
                            jt = j
                        else:
                            it = j
                            jt = i

        return [it,jt]
