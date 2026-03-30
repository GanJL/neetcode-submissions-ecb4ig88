class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return False
        
        if len(edges) != n - 1:
            return False

        # build adjacency list
        adj = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        # dfs method
        def dfs(i,prev):
            # cycle found
            if i in visited:
                return False

            visited.add(i)

            # go through neigbours
            for j in adj[i]:

                # skip the parent node
                if j == prev:
                    continue
                # if any neighbour's DFS is cyclical, this whole graph is invalid
                # dfs returns if any of the subtree is invalid, if child is invalid, whole tree is invalid, so we early exit
                if not dfs(j,i):
                    return False

            # reached end of path / no cycles found in this subtree
            return True 

        return dfs(0,-1) and len(visited) == n


