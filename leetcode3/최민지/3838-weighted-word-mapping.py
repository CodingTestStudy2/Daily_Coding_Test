class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        weight_alpha = []
        for word in words:
            word_sum = 0
            
            for w in word:
                word_sum += weights[ord(w)-ord('a')]
            weight_alpha.append(chr(ord('z') - word_sum % 26))
        return ''.join(weight_alpha)

        