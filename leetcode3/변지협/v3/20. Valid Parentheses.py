'''
1. 아이디어 :
스택을 이용한다. 여는 괄호나 스택 top과 짝이 맞지 않는 문자는 push하고,
스택 top과 짝이 맞는 닫는 괄호가 나오면 pop한다.
모든 문자를 처리한 뒤 스택이 비어 있으면 유효한 괄호 문자열, 아니면 유효하지 않다.

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
스택

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            if not stack:
                stack.append(e)
                continue

            if stack[len(stack)-1] == '(' and e == ')':
                stack.pop()
                continue
            elif stack[len(stack)-1] == '[' and e == ']':
                stack.pop()
                continue
            elif stack[len(stack)-1] == '{' and e == '}':
                stack.pop()
                continue

            stack.append(e)

        return True if not stack else False
