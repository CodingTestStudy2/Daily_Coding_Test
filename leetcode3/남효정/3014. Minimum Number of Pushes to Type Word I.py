# 풀이방법: 단어의 글자수에 따라 계산한다
# 점수계산: 몫은 순서대로 8을 곱하고 나머지는 몫+1 곱하기
# 예) 17개 -> 8*1 + 8*2 + 1*3 = 27
# 예) 5개  -> 8*0 + 5*1 = 5
# 예) 12개 -> 8*1 + 4*2 = 16
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = len(word) // 8
        ans = sum([i for i in range(cnt + 1)]) * 8
        ans += (cnt + 1) * (len(word) % 8)
        return ans