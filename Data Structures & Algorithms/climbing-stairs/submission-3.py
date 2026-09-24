class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 2
        cur = 0

        if n==1:
            return prev1
        if n==2:
            return prev2

        for i in range(2, n):
            cur = prev1 + prev2
            prev1 = prev2
            prev2 = cur

        return cur

        