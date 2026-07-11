import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        def canFinish(k):
            if sum(math.ceil(pile/k) for pile in piles) <= h:
                return True
            
            else:
                return False
        

        left, right = 1, max(piles)
        k = max(piles)

        while left <= right:
            mid = left + (right - left)//2

            if not canFinish(mid):
                left = mid + 1
            
            else:
                right = mid - 1
                k = min(k, mid)
            

        return k
