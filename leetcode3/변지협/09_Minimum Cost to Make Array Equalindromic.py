'''
1. 아이디어 :
    median 구해서 최소, 최대 palindrome 구해서 둘중에 더 작은거로 cost 계산
2. 시간복잡도 :
    n * log n - sort
3. 자료구조/알고리즘 :
'''
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        median = 0
        if len(nums) %2 == 0:
            median = sorted_nums[len(nums) //2 - 1] + sorted_nums[len(nums) //2]
            median //= 2
        else:
            median = sorted_nums[len(nums) //2]

        short = median
        while True:
            if self.is_pal(short):
                break
            
            short -= 1
        
        long = median
        while True:
            if self.is_pal(long):
                break
            
            long += 1

        # print(short, long)
        
        return min(sum([abs(num - short) for num in nums]), sum([abs(num - long) for num in nums]))

    def is_pal(self, num: int) -> bool:
        if len(str(num)) == 1:
            return True
        elif len(str(num)) %2 == 0 :
            # 123321 - 6 절반 = 3
            left = str(num)[:len(str(num))//2]
            right = str(num)[len(str(num))//2:]
            if left == right[::-1]:
                return True
        else:
            # 1234321 - 7 절반 = 3
            left = str(num)[:len(str(num))//2]
            right = str(num)[len(str(num))//2 + 1:]
            if left == right[::-1]:
                return True
        
        return False
            
            
            
            