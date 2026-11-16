'''
실패 (일부 테스트 케이스 오답)

1. 아이디어 :
연속으로 중복된 문자를 먼저 제거한 new_s를 만든 뒤, 뒤에서부터 문자를 스택(lst)에 쌓는다.
이미 스택에 있는 문자를 다시 만나면 그 문자를 맨 뒤로 옮긴 경우와 그대로 둔 경우를
비교해서, 사전순으로 더 작은 쪽을 택한다.

2. 시간복잡도 :
o(n^2)

3. 자료구조/알고리즘 :
스택, 그리디 (구현 실패)

'''

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lst = []

        last = ''
        new_s = ''

        for string in s:
            if last != string:
                new_s += string

            last = string

        for string in new_s[::-1]:
            if not string in lst:
                lst.append(string)
            else:
                tmp = lst.copy()
                tmp.remove(string)
                tmp.append(string)

                if ''.join(tmp)[::-1] < ''.join(lst)[::-1]:
                    lst = tmp

        return ''.join(lst)[::-1]
