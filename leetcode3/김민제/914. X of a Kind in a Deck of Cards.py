from collections import Counter
from math import gcd

def solution(deck):
    counts = Counter(deck).values()
    x = 0
    for count in counts:
        x = gcd(x,count)
    return x>1

arr = [1,2,3,4,4,3,2,1]
print(solution(arr))
