'''
1. 아이디어 :
- 인덱스 1 ~ n-2만 검사한다 (양 끝은 peak/valley가 될 수 없음).
- nums[i]가 양옆보다 엄격히 크면 peak, 엄격히 작으면 valley.
  두 조건은 동시에 성립할 수 없으므로 elif로 처리해도 안전하다.
- 값이 같은 경우(>=, <=)는 어느 쪽에도 해당하지 않으므로 자연히 제외된다.
- peak 값의 합에서 valley 값의 합을 빼서 반환한다.
2. 시간복잡도 :
O(n)
3. 자료구조/알고리즘 :
- 배열 순회 / 구현

'''

class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peaks = []
        valleys = []
        n = len(nums)
        for i in range(1,n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                peaks.append(nums[i])
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                valleys.append(nums[i])

        return sum(peaks) - sum(valleys)
