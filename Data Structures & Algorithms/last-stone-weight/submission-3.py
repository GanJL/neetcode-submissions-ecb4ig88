class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            currA = heapq.heappop(heap) * - 1
            currB = heapq.heappop(heap) * - 1

            if currA > currB: # A will always be bigger than B
                heapq.heappush(heap,(currA-currB)*-1)

        return -heap[0] if len(heap) > 0 else 0
