class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 1
        cur = 0

        # if n==1:
        #     return prev1
        # if n==2:
        #     return prev2

        for i in range(n-1):
            prev1, prev2 = prev2, prev1 + prev2


        return prev2

        