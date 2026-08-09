class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        # 동일한 구간이라도 왼쪽에 안 지우고 남긴 같은 색 박스 개수에 따라 정답 달라짐
        # 선택지 2개로 나눠서 생각해야 함

        # 정답 기록해놓는 배열
        memo = [[[0] * n for _ in range(n)] for _ in range(n)]

        def dp(i, j, k):
            # i: 현재 처리 중인 구간의 시작 인덱스
            # j: 현재 처리 중인 구간의 끝 인덱스
            # k: boxes[i] 왼쪽에 붙어 있는 boxes[i]와 같은 색상의 박스 개수

            # 박스 없으면 점수 0점
            if i > j:
                return 0

            # 예전에 계산한 적 있으면 바로 반환
            if memo[i][j][k] > 0:
                return memo[i][j][k]

            # 하나씩 인덱스 늘리면서 연속된 같은 색상 압축
            orig_i, orig_k = i, k
            while i < j and boxes[i] == boxes[i + 1]:
                i += 1
                k += 1

            # 선택지 1: 현재 박스 바로 터트리기 (왼쪽 k개 + 자기자신 1개)
            # 점수는 (k + 1)^2가 된다. 남은 구간은 dp(i + 1, j, 0) 계산
            res = (k + 1) ** 2 + dp(i + 1, j, 0)

            # 선택지 2: 중간 박스 지우고 뒤쪽의 같은 색과 합치기
            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    # i+1 ~ m-1 사이의 다른 색 박스들을 먼저 삭제 
                    # -> dp(i + 1, m - 1, 0)
                    # 그 결과 boxes[i]와 boxes[m]이 합쳐짐 
                    # -> boxes[m] 기준 왼쪽에 (k + 1)개 박스가 붙게 됨 
                    # -> dp(m, j, k + 1)
                    res = max(res, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))

            # 계산 결과 기록
            memo[orig_i][j][orig_k] = res
            return res

        return dp(0, n - 1, 0)