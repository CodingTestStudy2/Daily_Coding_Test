'''
1. 아이디어 :
    점화식 세우기
2. 시간복잡도 :
    O(100*100)
3. 자료구조/알고리즘 :
    dp
'''
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        lst = [[0] * (i+1) for i in range(102)]

        lst[0][0] = poured

        for i in range(101):
            for j in range(i+1):
                t = lst[i][j]
                if t >= 1:
                    remain = t - 1
                    lst[i+1][j] += remain /2
                    lst[i+1][j+1] += remain /2
        
        # print(lst)

        return lst[query_row][query_glass] if lst[query_row][query_glass] < 1 else 1