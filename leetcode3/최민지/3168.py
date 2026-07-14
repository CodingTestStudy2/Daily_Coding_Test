class Solution:
    def minimumChairs(self, s: str) -> int:
        maxCount = 0 # 필요한 의자 수 
        temp = 0 # 대기실에 있는 사람
        for i in range(len(s)):
            if s[i] == 'E':
                temp += 1
                maxCount = max(temp, maxCount)
            if s[i] == 'L':
                temp -= 1
                maxCount = max(temp, maxCount)

        return maxCount

        