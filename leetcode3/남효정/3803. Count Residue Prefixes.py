class Solution:
    def residuePrefixes(self, s: str) -> int:
        ans = 0
        check = set()

        for i, char in enumerate(s):
            check.add(char)

            # 종류가 3가지 이상이 되면 더 계산할 필요 없음
            if len(check) >= 3:
                break
            
            # 문제에서 원하는 조건 만족할 때마다 정답 개수 += 1
            if len(check) == (i + 1) % 3:
                ans += 1
        return ans