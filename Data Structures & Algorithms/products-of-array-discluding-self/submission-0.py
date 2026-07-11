class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        suf = [1] * n

        for i in range(n):
            pre[i] = pre[i-1] * nums[i-1] if i != 0 else 1
            
        
        for i in range(n-1,-1, -1):
            suf[i] = suf[i+1] * nums[i+1] if i != n-1 else 1


        return [suf[i] * pre[i] for i in range(n)]
        