#

'''
1. 아이디어 :
n을 10으로 나눴을때의 몫 * 자릿수

2. 시간복잡도 :
    O(9)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        digit = 0
        while n>0:
            remain = n%10
            if remain != 0:
                ans.append(remain * (10**digit))
            n = int(n/10)
            digit+=1
        return ans[::-1]
