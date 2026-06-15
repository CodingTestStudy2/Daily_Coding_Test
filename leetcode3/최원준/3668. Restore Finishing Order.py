#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n + m)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        friends_set = set(friends)
        for o in order:
            if o in friends_set:
                ans.append(o)

        return ans
