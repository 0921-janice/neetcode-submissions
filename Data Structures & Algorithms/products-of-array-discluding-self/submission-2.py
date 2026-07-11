class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        res = [0] * n

        pre[0] = suf[n-1] = 1

        for i in range(1,n):
            pre[i] = nums[i-1] * pre[i - 1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i+1] * nums[i + 1]
        for i in range(n):
            res[i] = pre[i] * suf[i]
        return res

        # n = len(nums)
        # output = [1] * n
        # prod = 1

        # for i in range(n):
        #     output[i] = output[i-1] * nums[i-1] if i != 0 else 1
            
        
        # for i in range(n-1,-1, -1):
        #     output[i] *= prod
        #     prod *= nums[i]

        # return output
        