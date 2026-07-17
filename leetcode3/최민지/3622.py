class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        totalPlus = 0
        totalDupli = 1

        for i in s:
            totalPlus += int(i)
            totalDupli *= int(i)

        if n % (totalPlus + totalDupli) == 0:
            return True
        else:
            return False

        