class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}

        for i in range(len(nums)):
            hashm[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashm and i!=hashm[diff]:
                return [i, hashm[diff]]

























        
        # hashT = {}

        # for i, n in enumerate(nums):
        #     diff = target - n

        #     if diff in hashT:
        #         return [hashT[diff], i]

        #     hashT[n] = i

        # return []