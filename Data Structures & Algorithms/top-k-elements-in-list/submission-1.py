from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = Counter(nums)
        top_nums = sorted(nums_dict, key = nums_dict.get, reverse = True)[:k]
        return top_nums
        