#

'''
1. 아이디어 :
i가 아닌부분(a), i인 부분(b)를 나눠서 계산

2. 시간복잡도 :
    O(1)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        def parse_and_remove(num: str) -> list:
            num = num.split("+")
            num[0] = int(num[0])
            num[1] = int(num[1][:-1])
            return num

        num1 = parse_and_remove(num1)
        num2 = parse_and_remove(num2)
        
        not_i = num1[0] * num2[0] - num1[1] * num2[1]
        i = num1[0] * num2[1] + num1[1] * num2[0]

        return str(not_i) + "+" + str(i) + "i"


        
