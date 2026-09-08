class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False


        edgesMap = {i:[] for i in range(n)}
        visited = set([0])
        for e1, e2 in edges:
            edgesMap[e1].append(e2)
            edgesMap[e2].append(e1)
        queue = collections.deque()
        queue.append(0)

        while queue:
            node = queue.popleft()

            for nei in edgesMap[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return len(visited) == n