#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
dict

'''
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        count = {5:0, 10:0, 20:0} #5, 10, 20

        def is_possible(payment):
            if payment == 20:
                if count[10] >= 1 and count[5] >= 1:
                    count[10] -= 1
                    count[5] -= 1
                    count[20] += 1
                    return True
                elif count[10] == 0 and count[5] >= 3:
                    count[5] -= 3
                    count[20] += 1
                    return True
            elif payment == 10:
                if count[5] >= 1:
                    count[5] -= 1
                    count[10] += 1
                    return True
            elif payment == 5:
                count[5] += 1
                return True
            
            return False

        for b in bills:
            if not is_possible(b):
                return False
        return True
                    
