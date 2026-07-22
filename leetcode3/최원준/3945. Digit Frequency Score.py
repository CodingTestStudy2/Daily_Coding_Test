class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(num) * freq for num, freq in Counter(str(n)).items())
