#
'''
1. 아이디어 :


2. 시간복잡도 :
    O()

3. 자료구조/알고리즘 :


'''

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        m_count = [0] * m
        n_count = [0] * n

        for a, b in indices:
            m_count[a] += 1
            n_count[b] += 1

        count = 0

        for row in range(m):
            for col in range(n):
                value = m_count[row] + n_count[col]
                if value % 2 == 1:
                    count += 1

        return count
