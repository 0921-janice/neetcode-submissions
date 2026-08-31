class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0

        maxlongest, longest = 0,0
        count = set()

        while r < len(s):
            while r < len(s) and s[r] not in count:
                count.add(s[r])
                r += 1
            
            maxlongest = max(maxlongest, len(count))

            while r < len(s) and s[r] in count:
                count.remove(s[l])
                l += 1

        return maxlongest

            




















        # while r < len(s):

        #     while r < len(s) and s[r] not in count:
        #         count.add(s[r])
        #         longest += 1
        #         r+=1
            
        #     maxlongest = max(longest, maxlongest)
            
        #     if r < len(s):
        #         while s[l] != s[r]:
        #             count.remove(s[l])
        #             longest -= 1
        #             l+=1
        #         count.remove(s[l])
        #         longest -= 1
        #         l+=1

        # return maxlongest

            

            