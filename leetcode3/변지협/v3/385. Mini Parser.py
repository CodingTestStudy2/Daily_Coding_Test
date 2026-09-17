'''
겁나 이해하기 어려운 문제
s = "[123,456,[788,799,833],[[]],10,[]]" 이테스트 케이스 통과를 못함.
'''

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
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return int(s)



        s = [i for i in s]
        str_tmp = ''
        stack = []
        lst_tmp = []
        while s:
            now = s.pop(0)
            print('s,now:',s,now)
            
            if now == '[':
                if lst_tmp:
                    stack.append(lst_tmp)
                lst_tmp = []
                str_tmp = ''
                s.pop()
            elif now == ',':
                lst_tmp.append(str_tmp)
                str_tmp = ''
            else:
                str_tmp += now
        
        lst_tmp.append(str_tmp)
        stack.append(lst_tmp)
        
        print(stack)

        n = NestedInteger()
        n.add(NestedInteger(789))

        n1 = NestedInteger()
        n1.add(NestedInteger(456))
        n1.add(n)

        n2 = NestedInteger()
        n2.add(NestedInteger(123))
        n2.add(NestedInteger(234))
        n2.add(n1)

        tmp = []
        while stack:
            # print(tmp)
            s = stack.pop()
            s = s[::-1]
            n = NestedInteger()
            while s:
                t = s.pop()
                n.add(NestedInteger(int(t)))
            if tmp:
                n.add(tmp[0])
                tmp[0] = n
            else:
                tmp.append(n)

        return tmp[0]
