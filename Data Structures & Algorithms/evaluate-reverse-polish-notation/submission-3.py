class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: a/b,
        }

        for token in tokens:
            if token not in ops.keys():
                stack.append(int(token))

            else:
                second_num = stack.pop()
                first_num = stack.pop()
                result = ops[token](first_num, second_num)
                stack.append(int(result))

        return stack[0]