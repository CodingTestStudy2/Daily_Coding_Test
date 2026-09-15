#

'''
1. 아이디어 :
x에 도달하기 위해서는 x-1에서 1칸 점프 + x-2에서 1칸 점프이므로, f(x) = f(x-1) + f(x-2)
길이 2의 배열을 활용하여 공간 절약

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
dp

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n

        ans = [1,2]
        for i in range(3, n+1):
            ans = [ans[1],ans[0] + ans[1]]
        return ans[1]

