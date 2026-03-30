class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksMap = {}
        for task in tasks:
            if task in tasksMap:
                tasksMap[task] += 1
            else:
                tasksMap[task] = 1
        
        maxHeap = [-cnt for cnt in tasksMap.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                t_cnt = heapq.heappop(maxHeap)
                t_cnt += 1
                if t_cnt: #non-zeros are positive
                    q.append([t_cnt, time + n ])

            if q and q[0][1] == time:
                item = q.popleft()
                heapq.heappush(maxHeap,item[0])

        return time
