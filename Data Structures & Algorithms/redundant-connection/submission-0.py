class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(1, len(edges) + 1)}


        

        def dfs(node, parent, visited):
            if node==parent:
                return True

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei, parent, visited): return True

            return False

        for u,v in edges:
            visited = set()
            if dfs(u,v, visited):
                return [u,v]
            
            adj[u].append(v)
            adj[v].append(u)

        return []


        # def dfs(node, target, visited):
        #     if node == target:
        #         return True

        #     visited.add(node)

        #     for nei in adj[node]:
        #         if nei not in visited:
        #             if dfs(nei, target, visited):
        #                 return True

        #     return False

        # for u, v in edges:
        #     visited = set()

        #     # If u and v are already connected,
        #     # adding this edge creates a cycle.
        #     if dfs(u, v, visited):
        #         return [u, v]

        #     adj[u].append(v)
        #     adj[v].append(u)

        # return []