#

'''
1. 아이디어 :
재귀로 풀 수 있다.
nestedList를 순회하면서 숫자면 배열에 추가, 아니라면 nestedList를 재귀로 호출하여 반복.

2. 시간복잡도 :
    O(n), O(1), O(1)

3. 자료구조/알고리즘 :
배열, dfs

'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.idx = 0
        
        def dfs(nestedList):
            for e in nestedList:
                if e.isInteger():
                    self.arr.append(e.getInteger())
                else:
                    dfs(e.getList())
        
        dfs(nestedList)
    
    def next(self) -> int:
        self.idx += 1
        return self.arr[self.idx-1]
    
    def hasNext(self) -> bool:
        return self.idx < len(self.arr)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
