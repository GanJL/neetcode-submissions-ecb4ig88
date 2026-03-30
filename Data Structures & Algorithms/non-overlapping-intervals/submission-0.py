class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        memo = {}

        intervals.sort()

        def dfs(i,prev_end):

            if i >= len(intervals):
                return 0

            if (i, prev_end) in memo:
                return memo[(i, prev_end)]

            # skip current interval
            skip = dfs(i + 1, prev_end)

            # take current interval
            take = 0
            if intervals[i][0] >= prev_end:
                take = 1 + dfs(i + 1, intervals[i][1])

            memo[(i, prev_end)] = max(take, skip)
            return memo[(i, prev_end)]


        max_keep = dfs(0, float('-inf'))
        return len(intervals) - max_keep
            