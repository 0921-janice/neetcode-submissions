class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        goal = n
        index = goal - 1
        
        while index >= 0:
            if nums[index] + index >= goal:
                goal = index
                index = goal - 1


            else:
                index -= 1

        return True if goal==0 else False
