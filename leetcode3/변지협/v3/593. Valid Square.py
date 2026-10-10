'''
1. 아이디어 :
   4개 점 사이의 모든 순서쌍(12개) 거리를 유클리드 거리로 구해 딕셔너리에 카운트한다.
   정사각형이면 변 4개(양방향 8번)와 대각선 2개(양방향 4번)만 나오므로,
   거리별 개수를 정렬했을 때 [4, 8]이면 정사각형이다.
   (int(length) != 0 조건으로 좌표가 겹치는 점(거리 0)은 카운트에서 제외한다.)
2. 시간복잡도 :
   o(1) - 점이 항상 4개로 고정
3. 자료구조/알고리즘 :
   defaultdict(해시맵), 유클리드 거리
'''

from collections import defaultdict
import math


class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        lst = [p1, p2, p3, p4]
        dic = defaultdict(int)
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                x1, y1 = lst[i]
                x2, y2 = lst[j]
                length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if int(length) != 0:
                    dic[length] += 1
        tmp = [i for i in dic.values()]
        tmp.sort()

        return tmp == [4, 8]
