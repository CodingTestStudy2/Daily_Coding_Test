#

'''
1. 아이디어 :
백트래킹을 사용합니다.
words를 set으로 관리하여 O(1)로 조회가 가능하도록하고,
""에서 a-z까지 순회하며 값을 붙여넣고, set에 있으면 재귀로 들어가고, 없으면 다음 알파벳으로 넘어갑니다.

2. 시간복잡도 :
    O(N * 26 * L) set에 있는 단어 수 * 알파벳 * 단어 길

3. 자료구조/알고리즘 :
백트래킹

'''
class Solution:
    def __init__(self):
        self.ans = ""

    def longestWord(self, words: List[str]) -> str:
        words_set = set(words)

        def backtrack(word):
            for i in range(26):
                next_char = chr(i+97)
                temp = word + next_char
                if temp in words_set:
                    if len(self.ans) < len(temp):
                        self.ans = temp
                    backtrack(temp)
            

        backtrack("")
        return self.ans
