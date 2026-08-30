# 풀이 실패
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # 첫 점프는 무조건 1칸이라 1번 돌 없으면 바로 실패임
        if stones[1] != 1:
            return False

        # 각 돌 위치별 도달했던 점프 거리(k) 집합 초기화
        jumps = {stone: set() for stone in stones}
        jumps[0].add(0)

        for stone in stones:
            for k in jumps[stone]:
                # 이동 가능한 다음 점프 거리 반복문
                for step in (k - 1, k, k + 1):
                    next_pos = stone + step
                    if step > 0 and next_pos in jumps:
                        jumps[next_pos].add(step)

        # 마지막 돌에 도달 기록 있으면 성공임
        return len(jumps[stones[-1]]) > 0


        