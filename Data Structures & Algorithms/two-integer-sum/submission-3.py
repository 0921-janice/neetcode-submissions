class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashT = {}

        for i, n in enumerate(nums):
            hashT[n] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in hashT and hashT[diff] != i:
                return [i, hashT[diff]]

        return []