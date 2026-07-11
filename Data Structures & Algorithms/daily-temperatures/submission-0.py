class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = []

        for i in range(n):
            print(stack)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                output[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return output
