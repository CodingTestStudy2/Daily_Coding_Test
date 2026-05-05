# LeetCode 3099. Harshad Number
def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
    sum = 0
    for ch in str(x):
        sum += int(ch)

    if x % sum == 0:
        return sum
    return -1

# 문제파악
    # 정수 x가 주어졌을때 x의 각 자릿수 합을 구한다
    # 주어진 정수의 각 자리수 합으로 해당 정수가 나누어 떨어진다면
        # 해당 정수를 반환하고,
        # 아니라면 -1을 반환한다.

# 시간복잡도
    # 1 < x < 100 의 제한조건을 가진 x의 자릿수 만큼 반복하므로 정확히는 O(자릿수), 점근법에 의해 상수시간 O(1) 이다.