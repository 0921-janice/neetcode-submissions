class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0

        adj = {i:[] for i in range(n)}

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
            return

        for i in range(n):
            if i not in visited:
                res +=1
                dfs(i)

        return res