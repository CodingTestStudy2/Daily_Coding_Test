#

'''
1. 아이디어 :
더할때는 가장 큰것부터, 뺄때는 가장 작은것부터.

2. 시간복잡도 :
    O(nlogn)

3. 자료구조/알고리즘 :
two pointer

'''
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        tokens.sort()
        
        left = 0
        right = n-1
        score = 0
        ans = 0

        while left<=right:
            if power>=tokens[left]:
                power -= tokens[left]
                left+=1
                score+=1
                ans = max(ans, score)
            elif score>0:
                power += tokens[right]
                right-=1
                score-=1
            else:
                break
        return ans

        

        
