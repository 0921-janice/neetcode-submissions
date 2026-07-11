from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        res, resLen = [-1,-1], float("inf")

        n = len(t)
        l = 0

        target_count = Counter(t)
        window_count = {}
        have, need = 0, len(target_count)
        
        for r in range(len(s)):
            c = s[r]
            window_count[c] = 1 + window_count.get(c,0)

            if c in target_count and target_count[c] == window_count[c]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1

                window_count[s[l]] -= 1
                if s[l] in target_count and target_count[s[l]] > window_count[s[l]]:
                    have -= 1
                l += 1
            
        l,r = res
        return s[l:r+1] if resLen!= float("inf") else ""

        