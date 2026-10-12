'''
1. 아이디어 :
모든 (i, j) 쌍을 완전탐색하면서, 두 구간이 포함하는 정수 set을 각각 만들어
교집합이 비어있지 않으면 교차로 카운트한다.
닫힌 구간이라 끝점(경계)만 공유해도 교차로 세어진다.
2. 시간복잡도 :
o(n^2 * m)   # m = 구간 길이(end - start)
3. 자료구조/알고리즘 :
set(집합), 완전탐색
'''

class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        ans = 0

        for i in range(n-1):
            for j in range(i+1,n):
                st_a, st_b = set(), set()
                a1,a2 = intervals[i]
                b1,b2 = intervals[j]
                for a in range(a1,a2+1):
                    st_a.add(a)
                for b in range(b1,b2+1):
                    st_b.add(b)
                # print(st_a, st_b)
                if len(st_a & st_b) > 0:
                    ans +=1

        return ans
