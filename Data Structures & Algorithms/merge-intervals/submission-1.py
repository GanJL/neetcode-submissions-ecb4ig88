class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []

        current_start, current_end = intervals[0]

        for i in range(1,len(intervals)):
            start, end = intervals[i]

            if start > current_end:
                # append whatever we have now
                res.append([current_start, current_end])
                # start accumulation
                current_start, current_end = start, end
            else:
                # extend accumulation
                current_end = max(current_end, end)

        # clear off whatever we have into res
        res.append([current_start,current_end])

        return res
