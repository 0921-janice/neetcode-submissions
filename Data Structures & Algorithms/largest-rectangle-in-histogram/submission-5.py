class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maxArea = float("-inf")
        

        for i, h in enumerate(heights):
            print(stack, maxArea)
            popped = False
            while stack and h < stack[-1][0]:
                prev_i = stack[-1][1]
                area = stack[-1][0] * (i - prev_i)
                maxArea = max(maxArea, area)
                stack.pop()
                popped = True
            
            if popped:
                stack.append([h, prev_i])

            elif not stack or not popped:
                stack.append([h,i])

        print("-----")
        while stack:
            print(print(stack, maxArea))
            area = stack[-1][0] * (n - stack[-1][1])
            maxArea = max(maxArea, area)
            stack.pop()
        
        return maxArea

            
        