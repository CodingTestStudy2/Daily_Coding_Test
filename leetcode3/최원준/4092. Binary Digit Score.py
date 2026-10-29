#

'''
1. 아이디어 :


2. 시간복잡도 :
    O(1)

3. 자료구조/알고리즘 :


'''
class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        def count_set_bits(num):
            return bin(num)[2:].count("1")

        a_bin = count_set_bits(a)
        b_bin = count_set_bits(b)
        return a_bin * b_bin if a_bin >= b_bin else int(b_bin / a_bin)
        
