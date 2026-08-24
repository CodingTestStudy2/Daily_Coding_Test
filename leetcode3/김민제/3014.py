from collections import Counter

class Solution:
    def minimumPushes(self  ,word:str) -> int:
        count = Counter(word)
        frequencies = sorted(count.values(), reverse=True)

        answer = 0

        for i,freq in enumerate(frequencies):
            push = i//8 +1
            answer += push * freq

        return answer


input = 'aabcde'
solution = Solution()
print(solution.minimumPushes(input))
