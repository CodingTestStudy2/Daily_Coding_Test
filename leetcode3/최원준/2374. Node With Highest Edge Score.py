#

'''
1. 아이디어 :
- O(n) scores 배열 초기화
- O(n) 출발, 도착에 대한 누적합 계산
- O(n) 누적합을 순회하며 최대 score 가진 노트를 찾습니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
누적합

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