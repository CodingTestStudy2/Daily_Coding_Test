#

'''
1. 아이디어 :
s를 리스트로 변환 후, 비어있지 않고 마지막 char이 vowel이면 pop.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        chars = [c for c in s]
        vowels = {"a", "e", "i", "o", "u"}
        while chars and chars[-1] in vowels:
            chars.pop()

        return "".join(chars)
