#

'''
1. 아이디어 :
각 row에 대해 오른쪽부터 연속된 0이 몇개인지 리스트로 유지한 후,
필요한 0의 갯수만큼 swap한다

2. 시간복잡도 :
    O(n*n + n*n)

3. 자료구조/알고리즘 :
greedy

'''
class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)

        zeros = []

        for row in range(n):
            zero = 0
            for col in range(n-1, -1, -1):
                if grid[row][col] == 1:
                    break
                zero += 1
            
            zeros.append(zero)

        ans = 0

        for i in range(n):
            needed = n - i - 1

            j = i

            while j < n and zeros[j] < needed:
                j += 1
            
            if j == n:
                return -1
            
            while j > i:
                zeros[j], zeros[j-1] = zeros[j-1], zeros[j]
                j -= 1
                ans += 1
        
        return ans
