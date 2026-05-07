# LeetCode 1943. Describe the Painting
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        points = set()

        # 색이 시작되거나 끝나는 부분을 set 으로 저장해둔다.
        for start, end, color in segments:
            points.add(start)
            points.add(end)

        points = sorted(points) # 이미지화하면 오름차순 숫자 라인이기 때문에 정렬해둔다
        answer = []

        # 색이 칠해진 작은 구간별로 탐색한다
        for i in range(len(points) - 1):
            left = points[i]
            right = points[i + 1]
            color_sum = 0

            # 작은 구간 별 색(숫자)를 구한다
            for start, end, color in segments:
                # segment 가 현재 구간을 포함하면 color 값을 더한다
                if start <= left and right <= end:
                    color_sum += color

            if color_sum > 0:
                answer.append([left, right, color_sum])

        return answer


# 문제 파악
    # Example 1 을 보면서 파악하는게 쉽다.
    # Input: segments = [[1,4,5],[4,7,7],[1,7,9]]
    # Output: [[1,4,14],[4,7,16]]

    # [1, 4, 5] 리스트가 주어지면 1~4 범위까지 5라는 '색'으로 칠한다는 의미이다.(주의점: 숫자를 색으로 판단)
    # [1, 7, 9] 가 주어지면 1~7 범위는 9라는 색으로 칠했다는 의미이다.
    # 1~4 구간 색이 5,9로 겹쳐지면 합해서 14가 되고 [1, 4, 14] 로 표현한다.
    # 위 원리로 4~7구간은 색의 합이 16이기 때문에 [4, 7, 16] 이 된다.
    # 답으로 이차원 배열 [[1, 4, 14],[4, 7, 16]] 을 반환하면 된다.

# 접근방법
    # 칠해지는 구간을 구하는게 먼저
    # 이후 구간별 숫자를 더하는 방식?

# 시간복잡도
    # 위 로직에서 제일 큰 시간 복잡도는 정렬할때 걸리는 nLogn 이기 떄문에 O(nLogn) 이 된다.