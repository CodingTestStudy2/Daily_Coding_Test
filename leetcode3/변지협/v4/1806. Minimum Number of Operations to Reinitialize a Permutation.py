'''
1. 아이디어 :
문제에 주어진 연산을 그대로 시뮬레이션한다.
i가 짝수면 arr[i] = perm[i//2], 홀수면 arr[i] = perm[n//2 + (i-1)//2] 로 arr를 채우고
perm을 arr로 교체한다. perm이 초기 상태인 range(n)과 같아질 때까지 반복하고 횟수를 센다.

2. 시간복잡도 :
o(n * answer) — 한 번의 연산이 o(n)이고, 초기 상태로 돌아올 때까지 answer번 반복한다.

3. 자료구조/알고리즘 :
배열 시뮬레이션

'''

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        arr = [0] * n
        perm = list(range(n))
        init = list(range(n))
        ans = 0

        while True:
            if perm == init and ans > 0:
                return ans

            for i in range(n):
                if i%2 == 0:
                    arr[i] = perm[i//2]
                else:
                    arr[i] = perm[n//2 + (i-1)//2]

            perm = arr.copy()
            ans += 1
