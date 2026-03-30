class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list
        adj = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        res = 0
        visited = set()
        # create dfs - return number of visited nodes in this graph
        def dfs(i):
            # base case - reached end of subgraph
            if i not in visited and not adj[i]:
                visited.add(i)
                return
            
            visited.add(i)

            for nei in adj[i]:
                # if nei in visited means, that was parent node
                if nei not in visited:
                    dfs(nei)

            return

        # for every node, check if it is visited - if not visited +1 to count and start to visit
        for j in range(n):
            if j not in visited:
                res += 1
                dfs(j)
        return res


            


