class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset, count):
            if count == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[count])
            backtrack(subset, count + 1)
            subset.pop()
            backtrack(subset, count + 1)

        backtrack([], 0)
        return res