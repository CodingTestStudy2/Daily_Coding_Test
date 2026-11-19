#

'''
1. 아이디어 :
- index 값이 1씩 오를때 얼마나 오르는지 O(1)로 계산해야한다. 
왼쪽, 오른쪽 등차 계산: (첫 숫자 + 마지막 숫자) x 갯수 / 2
계산하는 거리가 실제 존재하는 숫자보다 많은 경우 등차 계산으로는 초과하는 숫자들까지 포함되어서 else로 분기.
- 거리를 1씩 올리게 되면 (n)이고 시간초과. 이분탐색으로 logn으로 찾는다

2. 시간복잡도 :
    O(logn)

3. 자료구조/알고리즘 :
이분탐색

'''
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:


        left_nums = index
        right_nums = n-index-1

        def get_total(distance, count):
            if distance > count:
                return (distance - 1 + distance - count) * count // 2
            else:
                return distance * (distance - 1) // 2 + (count - distance + 1)

        def calculate_total(distance):
            left_total = get_total(distance, left_nums)
            right_total = get_total(distance, right_nums)
            return left_total + distance + right_total

        
        ans = 0

        left = 1
        right = maxSum + 1

        while left <= right:
            mid = (left + right) // 2

            if calculate_total(mid) <= maxSum:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
            
        return ans

        
