class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hasT = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for i in s:
            if i not in hasT:
                stack.append(i)

            else:
                if not stack or hasT[i] != stack[-1]:
                    return False

                else:
                    stack.pop()

        return True if not stack else False
            

