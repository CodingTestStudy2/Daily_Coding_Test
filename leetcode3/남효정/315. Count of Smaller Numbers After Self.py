# 풀이 실패
# 병합 정렬할 때 오른쪽에서 넘어간 개수 카운트하면 구할 수 있음
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(enum):
            half = len(enum) // 2
            if half:
                left, right = merge_sort(enum[:half]), merge_sort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0

                # 투 포인터 사용해서 병합 진행한다
                while i < m or j < n:
                    # 오른쪽 다 썼거나 왼쪽 값이 더 작거나 같은 경우
                    if j == n or (i < m and left[i][0] <= right[j][0]):
                        ans[left[i][1]] += j
                        enum[i + j] = left[i]
                        i += 1
                    else:
                        enum[i + j] = right[j]
                        j += 1

            return enum
            
        merge_sort(arr)
        return ans

        # 시간 복잡도 초과
        # ans = []
        # for i in range(len(nums)):
        #     if i == len(nums) - 1:
        #         ans.append(0)
        #         break
        #     check = 0
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] > nums[j]:
        #             check += 1
        #     ans.append(check)
        
        # return ans