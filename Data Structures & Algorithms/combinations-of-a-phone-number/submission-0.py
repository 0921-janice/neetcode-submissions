class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(chars, i):
            if i >= len(digits):
                res.append(''.join(chars.copy()))
                return

            for j in range(len(digitToChar[digits[i]])):
                chars.append(digitToChar[digits[i]][j])
                backtrack(chars, i + 1)
                chars.pop()

        backtrack([], 0)
        return res