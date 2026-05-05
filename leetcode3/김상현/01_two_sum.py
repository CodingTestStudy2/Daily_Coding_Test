# LeetCode 1. Two Sum
def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        need = target - num

        if need in d:
            return [d[need], i]

        d[num] = i

# 1. 이중 반복문을 써서 쉽게 풀 수도 있지만, 시간복잡도가 n제곱이기 때문에 map 을 사용해서 시간복잡도를 n 으로 개선한 풀이 방식
# 2. target에서 주어진 num 을 뺀 need 가 dictionary 에 있는지 찾는다
#   2-1. 없으면 딕셔너리에 인덱스를 담는다
#   2-2. 반복하며 need 가 담긴걸 발견하면 해당 인덱스와 반복인덱스 2개를 배열에 담아 반환한다