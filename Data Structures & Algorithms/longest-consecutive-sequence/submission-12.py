class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)

        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num+1 in numSet:
                    length +=1
                    num+=1

                longest = max(longest, length)

        return longest






















        # longest = 0
        # for num in nums:
        #     if num - 1 not in numSet:
        #         length = 1
        #         while num + 1 in numSet:
        #             length += 1
        #             num += 1

        #         longest = max(longest, length)

        # return longest

                

