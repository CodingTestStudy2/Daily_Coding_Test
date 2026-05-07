#

'''
1. 아이디어 :
- prefix sum을 구합니다.
- 같은 값이더라도 색상 set이 다르면 연속된 값이 아닌데, 조건중 color is distinct의 힌트를 보면,
- segment의 시작과 끝을 만나게 되면 항상 끊긴다는 의미를 갖습니다.
- 계산한 prefix sum을 순회하면서 구간들을 ans에 넣다가 segment의 시작/끝을 만나면 새로운 구간으로 만듭니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
- 누적합 / 해시셋

'''
 

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        ans = []
        end = max(segment[1] for segment in segments)

        prefix_sum = [0] * (end + 1)
        stops = set()

        for left, right, color in segments:
            prefix_sum[left] += color
            prefix_sum[right] -= color
            stops.add(left)
            stops.add(right)

        # stops = [stop for stop in stops]
        # stops.sort()

        # for i in range(1, len(prefix_sum)):
        #     prefix_sum[i] += prefix_sum[i - 1]

        # prev = -1
        # for curr in stops:
        #     if prev == -1:
        #         prev = curr
        #         continue
        #     if prefix_sum[prev] != 0:
        #         ans.append([prev, curr, prefix_sum[prev]])
        #     prev = curr

        prev = -1
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]
            if i in stops:
                if prev == -1:
                    prev = i
                    continue
                if prefix_sum[prev] != 0:
                    ans.append([prev, i, prefix_sum[prev]])
                prev = i

        return ans