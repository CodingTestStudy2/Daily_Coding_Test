'''
input: array with integers
output: integer - minimum number of operations to make all the elements equal

[1,2]
0001
0010
-> 0000  => 1

[5,5,5] -> equal already. 0

[2,3]
0010
0011
-> 0010 => [2,2] =>1

[5,6,7]
0101
0110
0111
-> 0100 -> [4,4,4]

- if the element in the array are the same, return 0
- otherwise return 1

TC: O(N), SC: O(N)

'''
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        
        return 1
        