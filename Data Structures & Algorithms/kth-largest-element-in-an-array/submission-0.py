class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = []
        heapq.heapify(minH)
        for i in range(len(nums)):
            heapq.heappush(minH, nums[i])
            if len(minH) > k:
                heapq.heappop(minH)
        return minH[0]

            