'''
1. 아이디어:
문제에 주어진 대로 풀이. 스택 사용
2. 시간복잡도:
o(n)
3. 알고리즘:
스택
'''

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)
        
