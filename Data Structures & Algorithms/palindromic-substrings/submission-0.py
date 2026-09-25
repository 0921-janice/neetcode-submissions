class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def palindrome(s, left, right):
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count+=1
                left-=1
                right+=1

            return count

        for i in range(len(s)):
            count += palindrome(s, i, i)
            count += palindrome(s, i, i + 1)


        return count


            
                

        