class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [0] * len(height), [0] * len(height)

        maxHeightLeft = maxHeightRight = 0
        for i in range(len(height)):
            j = -i - 1
            left[i] = maxHeightLeft
            right[j] = maxHeightRight
            maxHeightLeft = max(maxHeightLeft, height[i])
            maxHeightRight = max(maxHeightRight, height[j])
        
        sum = 0
        for i in range(len(height)):
            maxWater = min(left[i], right[i])

            if maxWater - height[i] > 0:
                sum += (maxWater - height[i])

        return sum
