class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLength = 0
        for n in nums:
            if (n-1) not in nums:
                length = 0
                while n+length in nums:
                    length+=1

                maxLength = max(maxLength, length)

        return maxLength