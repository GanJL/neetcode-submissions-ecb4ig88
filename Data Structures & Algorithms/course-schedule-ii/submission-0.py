class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
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
                return []
        
        return output













        

        