'''
1. 아이디어:
문제에 나와있는대로 구현하면 됨.
2. 시간복잡도:
o(n)
3. 알고리즘:
'''
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        wallet = {5: 0, 10: 0}
        
        for bill in bills:
            if bill == 5:
                wallet[5] += 1
            elif bill == 10:
                wallet[5] -= 1
                wallet[10] += 1

                if wallet[5] == -1:
                    return False
            else:
                if wallet[10] >= 1 and wallet[5] >= 1:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                else:
                    return False
        
        return True
            