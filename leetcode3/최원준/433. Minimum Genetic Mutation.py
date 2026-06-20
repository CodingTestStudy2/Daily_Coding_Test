#

'''
1. 아이디어 :
Deque를 사용하여 만들 수 있는 gene, count를 저장한다.
하나씩 빼면서 이미 변환한 gene 체크 후, is_valid 함수로 1개의 char만 바꿀 수 있는지 확인. 

2. 시간복잡도 :
    O(n * 8)

3. 자료구조/알고리즘 :
Deque

'''

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        dq = deque()
        dq.append([startGene, 0])
        visited = set()

        while dq:
            s, count = dq.popleft()
            if s == endGene:
                return count

            for gene in bank:
                if gene in visited:
                    continue

                if self.is_valid(s, gene):
                    dq.append([gene, count+1])
                    visited.add(gene)

        return -1

    def is_valid(self, s1, s2):
        counts = 0
        for i in range(8):
            if s1[i] != s2[i]:
                counts+=1
        return counts == 1
