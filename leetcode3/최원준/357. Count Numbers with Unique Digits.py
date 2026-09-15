#

'''
1. 아이디어 :
백트래킹으로 모든 경우를 구한다.
현재 숫자에 방문하지 않은 숫자를 더한다.

2. 시간복잡도 :
    약 O(10 ** 8)

3. 자료구조/알고리즘 :
backtracking

'''
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        visited = set()
    
        def backtrack(length, total_length):
            if length == total_length:
                return 1

            total = 0

            for i in range(10):
                if length == 0 and i ==0:
                    continue # 0
                
                if i in visited:
                    continue
                
                visited.add(i)
                total += backtrack(length+1, total_length)
                visited.remove(i)

            return total
        
        ans = 0
        for length in range(n+1):
            ans += backtrack(0, length)
        return ans

