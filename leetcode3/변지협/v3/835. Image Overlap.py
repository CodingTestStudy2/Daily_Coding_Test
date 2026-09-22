'''
1. 아이디어:
문제에 나와있는대로 img1을 전부 하나씩 이동하면서 최대값을 찾음.
2. 시간복잡도:
o(m*2*n*2*(m*n*2))
3. 알고리즘:
완전탐색
'''
class Solution:
    def move(self, img, dx, dy):
        m = len(img[0])
        n = len(img)
        
        ones = []
        for y in range(n):
            for x in range(m):
                if img[y][x] == 1:
                    ones.append((x,y))

        tmp = [[0] * m for _ in range(n)]
        while ones:
            x,y = ones.pop()
            
            if 0 <= x+dx < m and 0 <= y+dy < n:
                tmp[y+dy][x+dx] = 1

        return tmp

    def overlay(self, lst1, lst2):
        n = len(lst1[0])
        m = len(lst1)
        tmp = 0
        for y in range(m):
            for x in range(n):
                if lst1[y][x] == 1 and lst2[y][x] == 1:
                    tmp += 1

        return tmp 

    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        print(self.overlay(self.move(img1,1,1), img2))

        n = len(img1[0])
        m = len(img1)
        tmp = 0
        for dx in range(-m, m +1):
            for dy in range(-n, n+ 1):
                num = self.overlay(self.move(img1,dx,dy), img2)
                if num > tmp:
                    tmp = num

        return tmp        