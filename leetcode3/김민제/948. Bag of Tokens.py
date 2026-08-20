from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  #Olog(n)
        left = 0 #가장 작은 토큰
        right = len(tokens)-1 #가장 큰 토큰
        score = 0
        max_score = 0
        while left <=right:#O(n)
            if power >=tokens[left]:#face-up
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score,score)
            elif score > 0 and left < right:#face-down
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return max_score


tokens = [100,200,300,400]
power = 200
solution = Solution()
print(solution.bagOfTokensScore(tokens,power))
