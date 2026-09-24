class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = 0,0
        n = len(cost)

        for i in range(n):
            prev1, prev2 = prev2, min(prev1, prev2) + cost[i]

        return min(prev1, prev2)






















        # for i in range(2, n + 1):
        #     cur = min(prev1 + cost[i-1], prev2 + cost[i-2])

        #     prev2 = prev1
        #     prev1 = cur

        # return cur