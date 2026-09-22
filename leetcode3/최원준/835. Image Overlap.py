#

'''
1. 아이디어 :
한칸씩 옮긴다음 계산한다.

2. 시간복잡도 :
    O(n**4)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        
        def get_count(offset_x, offset_y):
            count = 0

            for x in range(n):
                for y in range(n):
                    mx = x + offset_x
                    my = y + offset_y
                    if 0<=mx<n and 0<=my<n and img1[x][y] and img2[mx][my]:
                        count+=1
                        
            return count
        
        # def get_count(img1, img2):
        #     count=0
        #     for x in range(n):
        #         for y in range(n):
        #             if img1[x][y] and img2[x][y]:
        #                 count+=1
        #     return count
        
        ans = 0
        for i in range(-n, n):
            for j in range(-n, n):
                ans = max(ans, get_count(i, j))
        return ans
