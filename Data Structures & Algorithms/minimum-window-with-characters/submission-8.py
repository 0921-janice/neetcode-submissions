from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        res, resLen = [-1, -1], float('inf')
        targetCounter = Counter(t)
        windowCounter = {}
        l = 0
        have, need = 0, len(targetCounter)

        for r in range(len(s)):
            windowCounter[s[r]] = 1 + windowCounter.get(s[r], 0)
            if s[r] in targetCounter and targetCounter[s[r]] == windowCounter[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l,r]
            
                windowCounter[s[l]] -= 1
                if s[l] in targetCounter and targetCounter[s[l]] > windowCounter[s[l]]:
                    have -= 1

                l += 1
            
        l, r = res

        return s[l:r+1] if resLen!=float('inf') else ""

                


        