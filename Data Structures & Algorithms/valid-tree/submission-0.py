class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # build adjacency list
        adj = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        # dfs method
        def dfs(i,prev):
            # loop found
            if i in visited:
                return False

            visited.add(i)

            # go through neigbours
            for j in adj[i]:

                # opposite node
                if j == prev:
                    continue
                # continue dfs path for each neigbour
                if not dfs(j,i):
                    return False

            # reached end of path
            return True 

        return dfs(0,-1) and len(visited) == n


