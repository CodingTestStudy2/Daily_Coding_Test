# LeetCode 3870. Count Commas in Range
class Solution:
    def countCommas(self, n: int) -> int:
        answer = 0

        for num in range(1, n + 1):
            formatted = f"{num:,}"
            answer += formatted.count(",")

        return answer


# 문제 파악
    # 1 부터 n 까지 모든 정수를 '표준 숫자 형식' 으로 썼을때 사용되는 '쉼표' 의 총 개수를 구하는 문제다.
        # 표준 숫자 형식을 이해하기 위해 예시를 참고해보면 '1,000', '2,000,000' 같은 형태임을 알 수 있다.

# 접근방법
    # 숫자를 문자열로 바꾼후, 쉼표의 갯수를 카운팅해서 반환한다.