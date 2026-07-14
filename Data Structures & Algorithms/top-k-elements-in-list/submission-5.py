class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for i in range(len(nums) + 1)]

        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for key, value in freq.items():
            res[value].append(key)

        output = []
        for i in range(len(nums), 0, -1):
            for num in res[i]:
                output.append(num)

                if len(output) == k:
                    return output