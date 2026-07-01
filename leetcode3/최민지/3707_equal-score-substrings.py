class Solution:
    def scoreBalance(self, s: str) -> bool:
        #print(ord('a')) -96
        totalScore = 0
        nowScore = 0
        for i in range(len(s)):
            totalScore += ord(s[i])

        for i in s:
            if nowScore == totalScore / 2:
                return True
            else:
                nowScore += ord(i)
        return False
