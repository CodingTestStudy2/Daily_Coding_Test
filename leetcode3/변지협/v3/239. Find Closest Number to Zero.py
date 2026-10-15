'''
1. 아이디어 :
절대값 작은거 찾고, 해당 num을 기록해둠.
그리고 같은 절대값이 나오면 num끼리 비교해서 더 큰거 선택

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
'''
class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        _min, value = 9999999, 9999999
        
        for num in nums:
            print(num, _min,value)
            if abs(num) < _min:
                _min,value = abs(num), num
            elif abs(num) == _min:
                if num > value:
                    value = num
        
        return value
                