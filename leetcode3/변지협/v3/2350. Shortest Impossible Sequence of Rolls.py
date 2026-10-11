'''
실패
'''
from collections import defaultdict

class Solution:
    def shortestSequence(self, rolls: list[int], k: int) -> int:
        st = set()
        for roll in rolls:
            for s in list(st):
                st.add(s+(roll,))
            st.add((roll,))

        dic = defaultdict(int)

        for s in list(st):
            dic[len(s)] += 1
        # print(dic[1])
        # print(dic[2])
        # print(dic[3])

        num =1
        while True:
            if not dic[num] == k ** num:
                return num
            num += 1
