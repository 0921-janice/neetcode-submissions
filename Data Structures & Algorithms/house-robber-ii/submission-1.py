class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_range(start, end):
            rob1, rob2 = 0,0
            for i in range(start, end):
                rob1, rob2 = rob2, max(rob1+nums[i], rob2)

            return rob2

        
        return max(nums[0], rob_range(0,len(nums)-1), rob_range(1, len(nums)))
