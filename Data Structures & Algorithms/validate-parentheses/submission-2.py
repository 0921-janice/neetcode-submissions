class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {
            '}' : "{",
            ']' : '[',
            ')' : '('
        }

        if s[0] in paren_dict or (len(s)%2==1):
            return False

        stack = []
        for paren in s:
            print(stack)
            if paren in paren_dict.values():
                stack.append(paren)

            else:
                if not stack:
                    return False

                if paren_dict[paren] == stack[-1]:
                    stack.pop()
                
                else:
                    return False
        
        return not stack
