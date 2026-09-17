# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            return NestedInteger(int(s))

        s = s[1:len(s)-1]
        n = len(s)

        def dfs(index):
            contains = NestedInteger()

            num = 0
            is_positive = 1
            has_num = False

            while index < n:
                if s[index] == "[":
                    child, index = dfs(index + 1)
                    contains.add(child)

                elif s[index] == "-":
                    is_positive = -1

                elif s[index].isdigit():
                    num = num * 10 + int(s[index])
                    has_num = True

                elif s[index] == ",":
                    if has_num:
                        contains.add(NestedInteger(num * is_positive))
                        num = 0
                        is_positive = 1
                        has_num = False

                elif s[index] == "]":
                    if has_num:
                        contains.add(NestedInteger(num * is_positive))

                    return contains, index

                index += 1

            if has_num:
                if not is_positive:
                    num *= -1

                contains.add(NestedInteger(num))

            return contains, index

        ans, _ = dfs(0)
        return ans
