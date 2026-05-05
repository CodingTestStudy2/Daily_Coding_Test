#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
'''
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        arr = [0] * n
        for i in range(n):
            arr[edges[i]] += i
        
        # print(arr)

        return arr.index(max(arr))
            