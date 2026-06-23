#

'''
1. 아이디어 :
- 해시맵을 통해 갯수를 비교합니다.

2. 시간복잡도 :
    O(7 + 1000*15)

3. 자료구조/알고리즘 :
HashMap

'''

from collections import defaultdict
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_dict = self.make_dict(licensePlate)
        
        ans = ""
        ans_length = float('inf')

        for word in words:
            word_dict = self.make_dict(word)
            if self.can_complete(license_dict, word_dict):
                if len(word) < ans_length:
                    ans = word
                    ans_length = len(word)
        return ans

    def make_dict(self, s):
        counter = defaultdict(int)

        for char in s:
            if not char.isalpha():
                continue
            counter[char.lower()]+=1
        return counter

    def can_complete(self, license_dict, word_dict):
        for char, rep in license_dict.items():
            if word_dict[char] < rep:
                return False
        return True
