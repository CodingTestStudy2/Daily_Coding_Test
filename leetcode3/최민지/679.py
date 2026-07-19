class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.dfs(cards)

    def dfs(self, nums):

        if len(nums) == 1:
            return abs(nums[0] -24) < 1e-6
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                
                a = nums[i]
                b = nums[j]

                # 선택되지 않은 숫자들(rest)를 만든다
                rest = []
                for k in range(len(nums)):
                    if k != i and k != j:
                        rest.append(nums[k])

                # 가능한 결과물
                results = [
                    a + b,
                    a - b,
                    b - a,
                    a * b
                ]
                if b != 0:
                    results.append(a / b)
                if a != 0:
                    results.append(b / a)

                # 결과 하나를 추가해서 다음 단계 진행
                for result in results:
                    if self.dfs(rest + [result]):
                        return True
        return False
            




        
        