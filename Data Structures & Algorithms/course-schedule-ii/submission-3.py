class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.res = []
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()
        processed = set()

        def dfs(crs):
            if crs in visited:
                return False

            if crs in processed:
                return True

            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            processed.add(crs)
            self.res.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs): return []

        return self.res
        