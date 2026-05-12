#

'''
1. 아이디어 :
맨위에 poured 만큼 저장하고 1을 뺀 만큼 아래로 나머지를 /2 보냅니다.

2. 시간복잡도 :
    O(100 * 100)

3. 자료구조/알고리즘 :
2차원 배열 / DP

'''


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0.0] * 101 for a in range(101)]
        glasses[0][0] = poured

        for row in range(query_row):
            for col in range(row+1):
                left_over = glasses[row][col]-1

                if left_over > 0:
                    glasses[row+1][col] += left_over/2
                    glasses[row+1][col+1] += left_over/2

                    glasses[row][col] = 1

        target = glasses[query_row][query_glass]
        return target if target < 1 else 1