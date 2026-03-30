class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #create adj map
        edges = collections.defaultdict(list)
        for u,v,t in times:
            edges[u].append((v,t))
        minHeap = [(0,k)]
        heapq.heapify(minHeap)
        visited = set()
        t = 0
        #bfs
        while minHeap:
            current_t,current_v = heapq.heappop(minHeap) # this is the shortest path from k to current
            if current_v in visited:
                continue
            visited.add(current_v)
            t = max(t,current_t) # take the max ?

            for edge_v, edge_t in edges[current_v]:
                if edge_v not in visited:
                    heapq.heappush(minHeap, (edge_t + current_t, edge_v) )

        return t if len(visited) == n else -1
        #use min heap for discretionary iteration