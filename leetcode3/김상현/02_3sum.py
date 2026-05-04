# LeetCode 15. 3Sum
def threeSum(nums):
    nums.sort()
    answer = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                answer.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return answer


# 문제파악
    # 정수 배열 nums가 주어질 때, 합이 0이 되는 서로 다른 세 수 조합을 모두 찾는 문제다.

# 접근 방법
    # 3중 반복문으로 모든 조합을 확인할 수 있지만 그럴 경우 시간복잡도는 n^3 이다.
    # 2s um 을 푸는 방식 투포인터, 딕셔너리 활용 중 적용 가능한 투포인터를 우선 적용해본다(이 경우 시간복잡도는 정렬 시간 복잡도인 nLogn)

# 풀이
    # 1. nums[i] 하나 고정
    # 2. 나머지에서 두 개 찾기 (투포인터)
    # 3. left = i+1, right = 끝
    # 4. 합 비교하면서 좁혀간다.

# 커서 이미지화(i, left, right)
    # [-4, -1, -1, 0, 1, 2]
    #   i   L         R

