class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visited = set()

        def dfs(course):

            if course in visited:
                return False

            if preMap[course] == []:
                return True

            #visited tracks the current DFS path, not globally visited
            visited.add(course)

            for neighbour in preMap[course]:
                if not dfs(neighbour):
                    return False
            
            #remove visited as we reverse back to the start of the path to prevent false cycle detection
            visited.remove(course)

            preMap[course] = []

            return True

        for i in range(numCourses):
            if not dfs(i): 
                return False
        
        return True
        

