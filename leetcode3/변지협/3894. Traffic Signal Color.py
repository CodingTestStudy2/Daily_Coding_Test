
'''
1. 아이디어 :

2. 시간복잡도 :
    O(1)

3. 자료구조/알고리즘 :
'''

class Solution(object):
    def trafficSignal(self, timer):
        """
        :type timer: int
        :rtype: str
        """

        if timer == 0: return "Green"
        elif timer == 30: return "Orange"
        elif 30 < timer <= 90: return "Red"
        else: return "Invalid"