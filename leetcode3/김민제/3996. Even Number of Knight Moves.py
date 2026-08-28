class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        start_parity = (start[0]+start[1])%2
        target_paritiy = (target[0]+target[1])%2

        if start_parity == target_paritiy:
            return True
        else:
            return False
