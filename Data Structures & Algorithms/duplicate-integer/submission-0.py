from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = Counter(nums)
        print(nums_dict)
        for number in nums_dict.values():
            print(number)
            if number > 1:
                return True

        return False 
        