# LeetCode 2374 Node With Highest Edge Score
def edgeScore(self, edges: List[int]) -> int:
    n = len(edges)
    scores = [0] * n

    # 각 노드로 들어오는 index 합 누적
    for i, target in enumerate(edges):
        scores[target] += i

    max_score = 0
    answer = 0

    # 최대점수 노드 찾기 (같닫면 작은 index 유지)
    for i, value in enumerate(scores):
        if value > max_score:
            max_score = value
            answer = i

    return answer


# 문제파악
    # 방향 그래프가 주어진다.
        # 노드는 0 ~ n-1
        # 각 노드는 하나의 간선만 가지고 있음
    # edge score (i를 가르키는 모든 노드 번호의 합)이 가장 큰 노드 번호를 반환해야한다
        # 점수가 같으면 번호가 작은 노드를 반환한다

# 접근방법
    # 결과적으로 edges 를 순회하면서 각 i(edge)를 가르키는 엣지의 누적합이 제일 큰 노드 번호를 반환해야 한다
        # 주어진 edges 순회하면서
        # 엣지 값 누적 후 비교

# 시간 복잡도
    # O(n)