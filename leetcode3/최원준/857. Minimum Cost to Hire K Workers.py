import heapq


class Solution:
    def mincostToHireWorkers(
        self,
        quality: list[int],
        wage: list[int],
        k: int
    ) -> float:
        workers = []

        for q, w in zip(quality, wage):
            workers.append((w / q, q))

        workers.sort()

        heap = []
        quality_sum = 0
        ans = float("inf")

        for ratio, q in workers:
            heapq.heappush(heap, -q)
            quality_sum += q

            if len(heap) > k:
                max_quality = -heapq.heappop(heap)
                quality_sum -= max_quality

            if len(heap) == k:
                ans = min(ans, ratio * quality_sum)

        return ans
