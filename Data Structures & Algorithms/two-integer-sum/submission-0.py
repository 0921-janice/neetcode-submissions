class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for index, num in enumerate(nums):
            if (target - num) in num_dict:
                return ([min(index, num_dict[target - num]), max(index, num_dict[target - num])])

            else:
                num_dict[num] = index