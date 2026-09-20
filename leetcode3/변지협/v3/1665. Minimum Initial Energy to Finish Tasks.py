'''
1. 아이디어:
actual이 최소이고, minimum이 최대인 것일 수록 먼저 수행해야한다.
2. 시간복잡도:
o(nlogn)
3. 알고리즘:
정렬 후, 순회하면서 energy를 계산한다.
'''
class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks = sorted(tasks, key=lambda x: x[1] - x[0])
        print(tasks)
        
        energy = 0
        for actual, minimum in tasks:
            energy = max(minimum, actual + energy)
        
        return energy