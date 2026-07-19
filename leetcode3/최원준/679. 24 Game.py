#

'''
1. 아이디어 :
숫자 4개 중 2개를 골라 +, -, *, / 연산 결과를 만든다.
선택한 두 숫자를 제거하고, 연산 결과를 넣어 DFS를 반복한다.
숫자가 1개 남았을 때 값이 24에 가까우면 True, 아니면 False를 반환한다.

2. 시간복잡도 :
    O(6ⁿ · n! · n!)

3. 자료구조/알고리즘 :
dfs

'''
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6

        def dfs(nums: List[float]) -> bool:
            # 모든 연산이 끝난 경우
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            n = len(nums)

            # 서로 다른 숫자 2개 선택
            for i in range(n):
                for j in range(i + 1, n):
                    a = nums[i]
                    b = nums[j]

                    # 선택하지 않은 숫자들
                    remaining = [
                        nums[k]
                        for k in range(n)
                        if k != i and k != j
                    ]

                    # a와 b로 만들 수 있는 결과
                    candidates = [
                        a + b,
                        a - b,
                        b - a,
                        a * b,
                    ]

                    # 0으로 나누는 경우 제외
                    if abs(b) > EPSILON:
                        candidates.append(a / b)

                    if abs(a) > EPSILON:
                        candidates.append(b / a)

                    for result in candidates:
                        remaining.append(result)

                        if dfs(remaining):
                            return True

                        remaining.pop()

            return False

        return dfs([float(card) for card in cards])
