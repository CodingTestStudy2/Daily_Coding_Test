#

'''
1. 아이디어 :
prime을 구하는법:
- 1 이하면 prime이 아니고,
- 2 면 prime이고,
- 2로 나뉘면 prime이고,
- 3부터 num의 제곱근까지 순회하면서 num 0으로 나누어 떨어지면 False
- 그 외 True

2. 시간복잡도 :
    O(n + n)

3. 자료구조/알고리즘 :
해시맵

'''

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(num):
            if num < 2:
                return False

            if num == 2:
                return True

            if num % 2 == 0:
                return False

            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False

            return True

        counts = Counter(nums)
        for num, freq in counts.items():
            if is_prime(freq):
                return True
        return False
