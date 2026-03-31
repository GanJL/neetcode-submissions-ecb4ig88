class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        heapq.heapify(heap)

        for stone in stones:
            heapq.heappush(heap,stone*-1)

        while len(heap) > 1:
            currA = heapq.heappop(heap) * - 1
            currB = heapq.heappop(heap) * - 1

            if currA > currB:
                heapq.heappush(heap,(currA-currB)*-1)
            elif currA < currB:
                heapq.heappush((currB-currA)*-1)

        return heapq.heappop(heap) * -1 if len(heap) > 0 else 0
