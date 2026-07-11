from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        if Counter(s) == Counter(t):
            return s

        res = ""
        length = float("inf")

        n = len(t)
        l,r = 0, n - 1

        target_count = Counter(t)
        window_count = Counter(s[l:r+1])

        print(target_count)
        while r-l+1 >= n and r<len(s):
            print(window_count)
            result = all(window_count[c] >= target_count[c] for c in target_count.keys())

            if result and (r-l+1) < length:
                res = s[l:r+1]
                length = min(length, r-l+1)
                

            if not result:
                r += 1
                if r<len(s):
                    window_count[s[r]] += 1
                
            else:
                window_count[s[l]] -= 1
                l += 1

        
        return res
        