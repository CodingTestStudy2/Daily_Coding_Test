#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n * m) n = words.length , m =words[i].length

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join(chr(ord('z') - sum(weights[ord(c) - ord('a')] for c in word) %26 ) for word in words)
