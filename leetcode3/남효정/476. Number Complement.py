class Solution:
    def findComplement(self, num: int) -> int:
        cnt = 0

        # 2진수 최대 - 1 - num 으로 답을 구할 수 있음
        # 예) num = 14라면 2^4 - 1 - 14 = 1이 답임
        # 예) num = 24라면 2^5 - 1 - 24 = 7이 답임
        def makeBinary(num: int):
            nonlocal cnt
            cnt += 1
            if num // 2 == 0:
                return 
            makeBinary(num // 2)

        makeBinary(num)
        return 2 ** cnt - num - 1 
        