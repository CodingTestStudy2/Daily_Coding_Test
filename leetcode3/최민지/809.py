class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        result = 0

        for word in words:
            i = 0
            j = 0
            ok = True

            while i < len(s) and j < len(word):

                # 현재 문자가 다르면 실패
                if s[i] != word[j]:
                    ok = False
                    break

                ch = s[i]

                # s에서 같은 문자 개수 세기
                cntS = 0
                while i < len(s) and s[i] == ch:
                    cntS += 1
                    i += 1

                # word에서 같은 문자 개수 세기
                cntW = 0
                while j < len(word) and word[j] == ch:
                    cntW += 1
                    j += 1

                # 규칙 검사
                if cntS < cntW:
                    ok = False
                    break

                if cntS > cntW and cntS < 3:
                    ok = False
                    break

            # 둘 다 끝까지 비교했는지 확인
            if ok and i == len(s) and j == len(word):
                result += 1

        return result