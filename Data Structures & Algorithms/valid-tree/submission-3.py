class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False


        edgesMap = {i:[] for i in range(n)}

        #0: 1,2,3
        #1: 4
        for e1, e2 in edges:
            edgesMap[e1].append(e2)
            edgesMap[e2].append(e1)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False


            visited.add(node)
            for nei in edgesMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node): return False
            
            return True

        for i in range(n):
            if i not in visited:
                if not dfs(i, -1): return False

        return True