# 풀이 실패
# 나이트는 1번 움직일 때마다 무조건 현재 칸과 다른 색의 칸으로 감
# 따라서 짝수 번 움직이면 원래 색으로 돌아감
# x + y 좌표 합의 홀짝으로 칸의 색상을 알 수 있음
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2