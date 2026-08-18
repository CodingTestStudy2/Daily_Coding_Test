class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        # ord()의 합과 알파벳 거꾸로 정렬한 순서의 합이 항상 122인 것을 이용
        for word in words:
            sum_score = 0
            for char in word:
                sum_score += weights[ord(char)-97]
            ans.append(chr(122 - sum_score % 26))
        
        return ''.join(ans)