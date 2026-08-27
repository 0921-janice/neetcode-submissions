class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(closed, opened, sub):
            if n == closed:
                res.append(''.join(sub.copy()))
                return

            if opened < n:
                sub.append('(')
                backtrack(closed, opened + 1, sub)
                sub.pop()

            if closed < opened:
                sub.append(')')
                backtrack(closed + 1, opened, sub)
                sub.pop()

        backtrack(0, 0, [])
        return res
