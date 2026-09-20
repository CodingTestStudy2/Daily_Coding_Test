class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers = []

        for q, w in zip(quality, wage):
            workers.append((w / q, q))

        workers.sort()

        heap = []
        quality_sum = 0
        answer = float('inf')

        for ratio, q in workers:
            heapq.heappush(heap, -q)
            quality_sum += q

            if len(heap) > k:
                largest_q = -heapq.heappop(heap)
                quality_sum -= largest_q

            if len(heap) == k:
                answer = min(
                    answer,
                    quality_sum * ratio
                )

        return answer
        