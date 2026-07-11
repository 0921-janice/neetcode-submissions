class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        output = [1] * n
        prod = 1

        for i in range(n):
            output[i] = output[i-1] * nums[i-1] if i!=0 else 1
        
        for i in range(n-1,-1,-1):
            output[i] *= prod
            prod *= nums[i]
        return output

        # n = len(nums)
        # output = [1] * n
        # prod = 1

        # for i in range(n):
        #     output[i] = output[i-1] * nums[i-1] if i != 0 else 1
            
        
        # for i in range(n-1,-1, -1):
        #     output[i] *= prod
        #     prod *= nums[i]

        # return output
        