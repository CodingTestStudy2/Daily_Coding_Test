class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        l = 0
        r = len(tokens) - 1

        score = 0
        max_score = 0

        while l <= r:
            if power >= tokens[l]:
                print('l', l)
                score += 1
                power -= tokens[l]
                l += 1
                max_score = max(max_score, score)
            elif score >= 1 and l < r:
                print('r', r)
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        return max_score