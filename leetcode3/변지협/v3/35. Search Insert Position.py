'''
1. 아이디어 :
- nums를 앞에서부터 순회하면서 target과 같은 값을 만나면 그 인덱스를 바로 반환한다.
- target보다 작은 값이 나올 때마다 삽입 위치(ans)를 i+1로 갱신한다.
- 끝까지 같은 값이 없으면 target이 들어갈 위치(ans)를 반환한다.

2. 시간복잡도 :
o(n)  (최악의 경우 배열 전체를 한 번 순회)

3. 자료구조/알고리즘 :
- 배열 순회 (선형 탐색)

'''

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        ans = 0
        for i, num in enumerate(nums):
            if target == num:
                return i
            if target > num:
                ans = i+1
        
        return ans
