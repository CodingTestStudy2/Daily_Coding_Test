#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0] * n
        for start, end in enumerate(edges):
            score[end] += start

        highest = -1
        cmax = -1
        for node, value in enumerate(score):
            if (value > cmax):
                highest = node
                cmax = value

        return highest