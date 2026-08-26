class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(total, i, cur):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            backtrack(total + candidates[i], i + 1, cur)

            cur.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(total, i + 1, cur)
            
        backtrack(0, 0, [])
        return res