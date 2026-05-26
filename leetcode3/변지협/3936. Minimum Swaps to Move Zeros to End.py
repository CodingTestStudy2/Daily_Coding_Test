
'''
1. 아이디어 :
    더 효율적으로 푸는 방법이 있을 것 같았는데,
    0을 찾아서 뒤에 우겨넣는 방식으로 구현하였다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조/알고리즘 :
'''

class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        # print(self.is_zero_last([0,1,2,0]))

        while not self.is_zero_last(nums):
            idx_zero = nums.index(0)
            change = len(nums) - 1
            # print('nums, change, idx_zero:', nums, change, idx_zero)
            while True:
                # print(' change:', change)
                if nums[change] != 0:
                    break

                if nums[change] == 0:
                    change -= 1

            nums[idx_zero] = nums[change]
            nums[change] = 0             
            ans +=1

        # print(self.is_zero_last([0,1,0,3,12]))
                
        return ans
            
    
    def is_zero_last(self, arr):
        arr_copy = [i for i in arr]
        zero_num = len([0 for i in arr if i == 0])
        zero_sum = 0
        while True:
            if not arr_copy:
                return True
            
            element = arr_copy.pop()
            # print('arr, zero_num, zero_sum, element:', arr, zero_num, zero_sum, element)

            if element == 0:
                zero_sum += 1
                continue

            if zero_sum == zero_num:
                return True
            else:
                return False