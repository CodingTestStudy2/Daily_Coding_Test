
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        arr =['a','e','i','o','u']
        cha = 0
        aeiou = 0

        for ch in range(len(s)):
            temp = s[ch]
            if temp in ('a','e','i','o','u'):
                aeiou+=1
            else:
                if ord(temp)>=97 and ord(temp)<=122:
                    cha+=1

        if cha==0:
            return 0
        else:
            return aeiou//cha



solution = Solution()
s = 'i3'
print(solution.vowelConsonantScore(s))
