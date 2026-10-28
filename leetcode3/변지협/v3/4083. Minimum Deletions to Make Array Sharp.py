'''
1. 아이디어 :
- 인접한 두 수의 XOR이 0이라는 건 두 수가 같다는 뜻이므로, "sharp"는 인접한 원소가 모두 다른 배열이다.
- 왼쪽부터 훑으면서 직전에 남긴 값과 같은 값이면 버리고, 다르면 남긴다.
- 연속된 같은 값 그룹마다 1개씩만 남게 되므로, 삭제 수 = len(nums) - len(남긴 리스트).
2. 시간복잡도 :
O(n)
3. 자료구조/알고리즘 :
- 그리디 / 배열 순회

'''

class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        lst = []
        for num in nums:
            if lst and num ^ lst[-1] == 0:
                continue
            lst.append(num)

        return len(nums) - len(lst)
