
'''
1. 아이디어 :
점수를 잃을땐 최대 power를 얻고, 점수를 얻을 땐 최소 pwoer를 소모한다.

2. 시간복잡도 :
o(nlogn)

3. 자료구조/알고리즘 :
투포인터
'''


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        
        a = 0
        b = n - 1
        score = 0
        ans = 0

        while True:
            print('a,b,power,score:', a,b,power)
            if a > b:
                break
            
            if power >= tokens[a]:
                power -= tokens[a]
                score +=1
                ans = max([score, ans])
                a += 1
            else:
                if score == 0:
                    break
                power += tokens[b]
                score -= 1
                b -= 1
        
        return ans