from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 모든 숫자의 등장 횟수 찾기
        counts = Counter(deck).values()
        g = 0

        # 등장 횟수 간의 최대 공약수 찾기
        for count in counts:
            g = math.gcd(g, count)

        # 최대 공약수가 1이면 배열 구할 수 없음
        if g > 1:
            return True
        return False
        
