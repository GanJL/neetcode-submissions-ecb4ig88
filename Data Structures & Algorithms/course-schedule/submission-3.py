class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # preMap = {i:[] for i in range(numCourses)}

        # for course, pre in prerequisites:
        #     preMap[course].append(pre)

        # visited = set()

        # def dfs(course):

        #     if course in visited:
        #         return False

        #     if preMap[course] == []:
        #         return True

        #     #visited tracks the current DFS path, not globally visited
        #     visited.add(course)

        #     for neighbour in preMap[course]:
        #         if not dfs(neighbour):
        #             return False
            
        #     #remove visited as we reverse back to the start of the path to prevent false cycle detection
        #     visited.remove(course)

        #     #memoization - this course is fully processed and all pre-requisites are fulfiled 
        #     preMap[course] = []

        #     return True

        # for i in range(numCourses):
        #     if not dfs(i): 
        #         return False
        
        # return True

        # create adjacency list
        preMap = { i:[] for i in range(numCourses) }

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        # 3 things to track -> 
        # visited nodes -> appended to output
        # cycle nodes -> prevent cycles
        visited, cycle = set(), set()
        # output
        output = []
        
        # create dfs
        # run dfs on every node
        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False

            cycle.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.add(course)
            output.append(course)
            cycle.remove(course)

            return True

        for j in range(numCourses):
            if not dfs(j):
                return False
        
        return len(output) == numCourses

        

